const PRODUCTS = [
  { id: 1, name: "Margherita Pizza", category: "Pizza", price: 249, emoji: "🍕", description: "Classic cheese and tomato" },
  { id: 2, name: "Veg Burger", category: "Burgers", price: 149, emoji: "🍔", description: "Crispy patty with fresh veggies" },
  { id: 3, name: "Chicken Biryani", category: "Rice", price: 229, emoji: "🍛", description: "Aromatic basmati with spices" },
  { id: 4, name: "French Fries", category: "Snacks", price: 99, emoji: "🍟", description: "Golden and crunchy" },
  { id: 5, name: "Paneer Wrap", category: "Wraps", price: 139, emoji: "🌯", description: "Spiced paneer in soft roti" },
  { id: 6, name: "Cold Coffee", category: "Drinks", price: 119, emoji: "🥤", description: "Chilled and creamy" },
];

const delay = (ms = 300) => new Promise((r) => setTimeout(r, ms));

// MOCK: Phase 5 la fetch('/api/...') ku replace pannuvom
export async function getProducts() {
  await delay();
  return PRODUCTS;
}

export async function createOrder(order) {
  await delay();
  const saved = { ...order, id: Date.now(), status: "Placed", created_at: new Date().toISOString() };
  localStorage.setItem(`order-${saved.id}`, JSON.stringify(saved));
  return saved;
}

export async function getOrder(id) {
  await delay();
  const raw = localStorage.getItem(`order-${id}`);
  if (!raw) throw new Error("Order not found");
  return JSON.parse(raw);
}