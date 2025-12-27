def product_list(brand , *args):
    if not args :
        print(f"{brand}: No products available")
        return
    
    lable = "products" if len(args) > 1 else "product"
    items = ", ".join(args) 
    print(f'{brand} {lable}: {items}')

product_list('Toyota', 'Camry', 'Yaris', 'Fortuner')
product_list('Honda', 'Accord', 'Civic', 'CRV')
product_list('Tesla')