import { useCart } from "../context/CartContext";

export default function ProductCard({ product }) {
  const { add } = useCart();
  return (
    <div className="card">
      <div className="emoji">{product.emoji}</div>
      <h3>{product.name}</h3>
      <p className="muted">{product.description}</p>
      <div className="row">
        <strong>₹{product.price}</strong>
        <button onClick={() => add(product)}>Add</button>
      </div>
    </div>
  );
}