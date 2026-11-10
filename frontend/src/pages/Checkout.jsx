import { useState } from "react";
import { useNavigate } from "react-router-dom";
import { useCart } from "../context/CartContext";
import { createOrder } from "../services/api";

export default function Checkout() {
  const { items, total, clear } = useCart();
  const navigate = useNavigate();
  const [form, setForm] = useState({ name: "", phone: "", address: "" });
  const [submitting, setSubmitting] = useState(false);
  const [error, setError] = useState("");

  const change = (e) => setForm({ ...form, [e.target.name]: e.target.value });

  const submit = async (e) => {
    e.preventDefault();
    if (items.length === 0) return setError("Cart is empty");
    setSubmitting(true);
    try {
      const order = await createOrder({
        customer: form,
        items: items.map((i) => ({ product_id: i.id, name: i.name, quantity: i.qty, price: i.price })),
        total,
      });
      clear();
      navigate(`/orders/${order.id}`);
    } catch {
      setError("Order failed. Try again.");
      setSubmitting(false);
    }
  };

  return (
    <>
      <h2>Checkout</h2>
      <form onSubmit={submit} className="form">
        <input name="name" placeholder="Full name" value={form.name} onChange={change} required />
        <input name="phone" placeholder="Phone" value={form.phone} onChange={change} required pattern="[0-9]{10}" title="10 digit number" />
        <textarea name="address" placeholder="Delivery address" value={form.address} onChange={change} required />
        <p><strong>Total: ₹{total}</strong></p>
        {error && <p className="error">{error}</p>}
        <button disabled={submitting}>{submitting ? "Placing..." : "Place Order"}</button>
      </form>
    </>
  );
}