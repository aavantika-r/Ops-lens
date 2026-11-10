import { useEffect, useState } from "react";
import { getProducts } from "../services/api";
import ProductCard from "../components/ProductCard";

export default function Menu() {
  const [products, setProducts] = useState([]);
  const [category, setCategory] = useState("All");
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    getProducts().then((d) => { setProducts(d); setLoading(false); });
  }, []);

  const categories = ["All", ...new Set(products.map((p) => p.category))];
  const visible = category === "All" ? products : products.filter((p) => p.category === category);

  if (loading) return <p>Loading menu...</p>;

  return (
    <>
      <h2>Our Menu</h2>
      <div className="chips">
        {categories.map((c) => (
          <button key={c} className={c === category ? "chip active" : "chip"} onClick={() => setCategory(c)}>
            {c}
          </button>
        ))}
      </div>
      <div className="grid">
        {visible.map((p) => <ProductCard key={p.id} product={p} />)}
      </div>
    </>
  );
}