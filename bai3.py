from fastapi import FastAPI

app = FastAPI()

products = [
    {"id": 1, "name": "Laptop", "price": 15000000},
    {"id": 2, "name": "Mouse", "price": 200000},
    {"id": 3, "name": "Keyboard", "price": 500000},
    {"id": 4, "name": "Monitor", "price": 3000000}
]

@app.get('/products')
def get_students(keyword: str = None, max_price: int = None):
    if keyword is None and max_price is None:
        return products
    
    
    list_products = []
    
    for pro in products:
            
        if max_price != None and keyword != None:
            if keyword.lower() in pro.get('name').lower() and max_price > pro.get('price'):
                list_products.append(pro)
                
        elif max_price != None or keyword != None:
            if keyword != None:
                if keyword.lower() in pro.get('name').lower()   :
                    list_products.append(pro)
            
            if max_price != None:
                if max_price < 0:
                    return {
                            "detail": "max_price không được âm"
                            }
                if max_price > pro.get('price'):
                    list_products.append(pro)
                
    return list_products
