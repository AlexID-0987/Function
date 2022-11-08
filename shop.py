class Products():
    def __init__(self, capacity) -> None:
        self.cap=capacity
        self.product=[]
    def add_product(self, newProducts):
        if not self.capacityProducts():
            return False
        self.product.append(newProducts)
        return True
    def capacityProducts(self):
        return self.cap-len(self.product)
    
product=Products(5)
products=['Milk','Potayto','Carlik','Meat','Coffe','Choklet']
for pr in products:
    success=product.add_product(pr)
    if success:
        print(f"Products added {pr}")
    else:
        print(f"Not added products {pr}")