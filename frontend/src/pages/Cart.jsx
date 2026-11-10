import { Link } from "react-router-dom";
import { useCart } from "../context/CartContext";

export default function Cart() {
  const { items, updateQty, remove, total } = useCart();

  if (items.length === 0)
    return (<><h2>Your Cart</h2><p>Cart empty. <Link to="/">Browse menu</Link></p></>);

  return (
    <>
      <h2>Your Cart</h2>
      {items.map((i) => (
        <div key={i.id} className="cart-row">
          <span>{i.emoji} {i.name}</span>
          <span className="qty">
            <button onClick={() => updateQty(i.id, -1)}>−</button>
            {i.qty}
            <button onClick={() => updateQty(i.id, 1)}>+</button>
          </span>
          <span>₹{i.price * i.qty}</span>
          <button className="link" onClick={() => remove(i.id)}>Remove</button>
        </div>
      ))}
      <h3>Total: ₹{total}</h3>
      <Link to="/checkout"><button>Proceed to Checkout</button></Link>
    </>
  );
}