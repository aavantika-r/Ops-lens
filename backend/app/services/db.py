import os
from contextlib import contextmanager

from psycopg2.extras import RealDictCursor
from psycopg2.pool import ThreadedConnectionPool

_pool = None


def get_pool():
    global _pool
    if _pool is None:
        dsn = os.environ.get(
            "DATABASE_URL", "postgresql://opslens:opslens@localhost:5432/opslens"
        )
        _pool = ThreadedConnectionPool(1, 10, dsn)
    return _pool


@contextmanager
def get_cursor():
    pool = get_pool()
    conn = pool.getconn()
    try:
        with conn.cursor(cursor_factory=RealDictCursor) as cur:
            yield cur
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        pool.putconn(conn)