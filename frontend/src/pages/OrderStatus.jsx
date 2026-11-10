import { useEffect, useState } from "react";
import { useParams, Link } from "react-router-dom";
import { getOrder } from "../services/api";

export default function OrderStatus() {
  const { id } = useParams();
  const [order, setOrder] = useState(null);
  const [error, setError] = useState("");

  useEffect(() => {
    getOrder(id).then(setOrder).catch((e) => setError(e.message));
  }, [id]);

  if (error) return <p className="error">{error}</p>;
  if (!order) return <p>Loading order...</p>;

  return (
    <>
      <h2>✅ Order #{order.id}</h2>
      <p>Status: <span className="badge">{order.status}</span></p>
      <p>Name: {order.customer.name} | Phone: {order.customer.phone}</p>
      <p>Address: {order.customer.address}</p>
      <ul>
        {order.items.map((i) => (
          <li key={i.product_id}>{i.name} × {i.quantity} = ₹{i.price * i.quantity}</li>
        ))}
      </ul>
      <h3>Total: ₹{order.total}</h3>
      <Link to="/">Order more</Link>
    </>
  );
}