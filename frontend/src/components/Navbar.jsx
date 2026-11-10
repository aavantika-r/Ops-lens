import { Link } from "react-router-dom";
import { useCart } from "../context/CartContext";

export default function Navbar() {
  const { count } = useCart();
  return (
    <nav className="navbar">
      <Link to="/" className="brand">🍽️ FoodHub</Link>
      <Link to="/cart" className="cart-link">Cart ({count})</Link>
    </nav>
  );
}