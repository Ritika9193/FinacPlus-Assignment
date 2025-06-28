
# Question: Imagine you work for amazon, what is the Meta data information you will store for an item in your Database. For E.g. the item is a shirt, once you have stored the Meta data how will use the information?

---

## 1. Metadata to Store for a Product

When storing a product like a **shirt**, we capture various metadata to support core business functions: search, filtering, inventory, recommendations, and more.

### Basic Product Metadata
- `product_id`: Unique identifier
- `name`: "Men's Cotton Shirt"
- `description`: Full product description
- `brand`: "Levi's"
- `category`: "Apparel > Men > Shirts"
- `gender`: "Male"
- `fit`: "Slim", "Regular"
- `material`: "100% Cotton"
- `created_at`, `updated_at`: Timestamps

### Pricing Metadata
- `price`: 799.00
- `discount_percent`: 10%
- `final_price`: 719.10 (computed)
- `currency`: INR

### Variant Metadata
- `size`: S, M, L, XL
- `color`: Blue, White, Black
- `sku`: Unique identifier for each variant
- `weight`: 300g
- `dimensions`: 30x25x2 cm
- `is_returnable`: true

### Media Metadata
- `main_image_url`
- `gallery_images`: List of image URLs
- `video_url`: Optional

### Review & Rating Metadata
- `average_rating`: 4.3
- `total_reviews`: 1450
- `reviews`: Linked review records

### Tagging & Filtering
- `tags`: ["Summer", "Slim Fit", "Cotton", "Trendy"]
- `occasion`: "Casual"
- `season`: "Summer"

### Inventory & Warehouse Metadata
- `stock_count`: Per variant and per warehouse
- `warehouse_location`: ["BLR", "DEL"]

### Search & SEO Metadata
- `slug`: "mens-cotton-slim-shirt"
- `keywords`: ["shirt", "cotton shirt", "men’s summer shirt"]
- `meta_title`, `meta_description`

---

## 2. Relational Database Schema (3NF)

Here's the normalized schema structure:

---

### `products`

```sql
CREATE TABLE products (
    product_id UUID PRIMARY KEY,
    name TEXT NOT NULL,
    brand_id UUID REFERENCES brands(brand_id),
    category_id UUID REFERENCES categories(category_id),
    description TEXT,
    material TEXT,
    fit TEXT,
    gender TEXT CHECK (gender IN ('Male', 'Female', 'Unisex')),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

---

### `brands`

```sql
CREATE TABLE brands (
    brand_id UUID PRIMARY KEY,
    name TEXT UNIQUE NOT NULL
);
```

---

### `categories`

```sql
CREATE TABLE categories (
    category_id UUID PRIMARY KEY,
    name TEXT NOT NULL,
    parent_category_id UUID REFERENCES categories(category_id) ON DELETE SET NULL
);
```

---

### `product_variants`

```sql
CREATE TABLE product_variants (
    variant_id UUID PRIMARY KEY,
    product_id UUID REFERENCES products(product_id) ON DELETE CASCADE,
    color TEXT,
    size TEXT,
    sku TEXT UNIQUE NOT NULL,
    price DECIMAL(10,2) NOT NULL,
    discount_percent DECIMAL(5,2) DEFAULT 0,
    final_price DECIMAL(10,2) GENERATED ALWAYS AS (
        price - (price * discount_percent / 100)
    ) STORED,
    stock_count INT DEFAULT 0,
    weight_in_grams INT,
    length_cm DECIMAL,
    width_cm DECIMAL,
    height_cm DECIMAL,
    is_returnable BOOLEAN DEFAULT TRUE
);
```

---

### `images`

```sql
CREATE TABLE images (
    image_id UUID PRIMARY KEY,
    product_id UUID REFERENCES products(product_id) ON DELETE CASCADE,
    variant_id UUID REFERENCES product_variants(variant_id),
    url TEXT NOT NULL,
    is_main BOOLEAN DEFAULT FALSE,
    media_type TEXT CHECK (media_type IN ('image', 'video')),
    alt_text TEXT
);
```

---

### `tags`

```sql
CREATE TABLE tags (
    tag_id UUID PRIMARY KEY,
    name TEXT UNIQUE NOT NULL
);
```

---

### `product_tags`

```sql
CREATE TABLE product_tags (
    product_id UUID REFERENCES products(product_id) ON DELETE CASCADE,
    tag_id UUID REFERENCES tags(tag_id) ON DELETE CASCADE,
    PRIMARY KEY (product_id, tag_id)
);
```

---

### `reviews`

```sql
CREATE TABLE reviews (
    review_id UUID PRIMARY KEY,
    variant_id UUID REFERENCES product_variants(variant_id),
    user_id UUID,
    rating INT CHECK (rating BETWEEN 1 AND 5),
    review_text TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

---

### `product_keywords`

```sql
CREATE TABLE product_keywords (
    product_id UUID REFERENCES products(product_id) ON DELETE CASCADE,
    slug TEXT UNIQUE,
    meta_title TEXT,
    meta_description TEXT,
    keywords TEXT[]
);
```

---

### `warehouses`

```sql
CREATE TABLE warehouses (
    warehouse_id UUID PRIMARY KEY,
    name TEXT,
    location TEXT
);
```

---

### `variant_inventory`

```sql
CREATE TABLE variant_inventory (
    variant_id UUID REFERENCES product_variants(variant_id),
    warehouse_id UUID REFERENCES warehouses(warehouse_id),
    stock_count INT DEFAULT 0,
    PRIMARY KEY (variant_id, warehouse_id)
);
```

---

## 3. How This Metadata is Used

### a. Frontend Display
- Show product name, brand, price, color/size selectors, images, rating
- Use metadata like `fit`, `material`, `tags` to help users decide

### b. Search & Filtering
- `tags`, `category`, `gender`, and `fit` used for filters
- `keywords` and `meta_description` boost SEO ranking
- Users can search for "men's slim fit summer shirt cotton"

### c. Recommendation System
- Recommend similar products by analyzing:
  - Category
  - Tags
  - Average rating
  - Co-viewed/co-purchased items

### d. Inventory & Fulfillment
- Use `variant_inventory` to show real-time stock
- Ship from nearest `warehouse_location`

### e. Analytics & Reporting
- Track fast-moving sizes/colors
- Identify products with high returns (via `is_returnable`)
- Analyze review sentiment

### f. Dynamic Pricing & Promotions
- Metadata like `discount_percent` helps generate limited-time deals
- Real-time recalculation of `final_price`


