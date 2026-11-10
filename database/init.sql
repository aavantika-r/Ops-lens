CREATE TABLE IF NOT EXISTS products (
    id          SERIAL PRIMARY KEY,
    name        VARCHAR(100) NOT NULL,
    category    VARCHAR(50)  NOT NULL,
    price       INTEGER      NOT NULL CHECK (price > 0),
    emoji       VARCHAR(10),
    description TEXT
);

CREATE TABLE IF NOT EXISTS customers (
    id         SERIAL PRIMARY KEY,
    name       VARCHAR(100) NOT NULL,
    phone      VARCHAR(20)  NOT NULL,
    address    TEXT         NOT NULL,
    created_at TIMESTAMPTZ  NOT NULL DEFAULT now()
);

CREATE TABLE IF NOT EXISTS orders (
    id          SERIAL PRIMARY KEY,
    customer_id INTEGER     NOT NULL REFERENCES customers(id),
    total       INTEGER     NOT NULL,
    status      VARCHAR(30) NOT NULL DEFAULT 'Placed',
    created_at  TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE IF NOT EXISTS order_items (
    id         SERIAL PRIMARY KEY,
    order_id   INTEGER NOT NULL REFERENCES orders(id) ON DELETE CASCADE,
    product_id INTEGER NOT NULL REFERENCES products(id),
    quantity   INTEGER NOT NULL CHECK (quantity > 0),
    price      INTEGER NOT NULL
);

INSERT INTO products (id, name, category, price, emoji, description) VALUES
 (1, 'Margherita Pizza', 'Pizza',   249, '🍕', 'Classic cheese and tomato'),
 (2, 'Veg Burger',       'Burgers', 149, '🍔', 'Crispy patty with fresh veggies'),
 (3, 'Chicken Biryani',  'Rice',    229, '🍛', 'Aromatic basmati with spices'),
 (4, 'French Fries',     'Snacks',   99, '🍟', 'Golden and crunchy'),
 (5, 'Paneer Wrap',      'Wraps',   139, '🌯', 'Spiced paneer in soft roti'),
 (6, 'Cold Coffee',      'Drinks',  119, '🥤', 'Chilled and creamy')
ON CONFLICT (id) DO NOTHING;

SELECT setval(pg_get_serial_sequence('products', 'id'), (SELECT MAX(id) FROM products));