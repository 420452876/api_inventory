import json
from app import BASE_DIR

def get_stock():
    filename = BASE_DIR + '/data/stock_data.json'
    with open(filename,'r',encoding='utf-8') as f :
        data = json.load(f)
        jsonData = data.get('add_stock')
        print(jsonData)
        case_list = []
    http_code = jsonData.get('http_code')
    provider = jsonData.get('Provider')
    model = jsonData.get('Model')
    price = jsonData.get('Price')
    inventory = jsonData.get('Inventory')
    quantity = jsonData.get('Quantity')

    case_list.append((http_code,provider,model,price,inventory,quantity))
    return case_list

print(get_stock())
