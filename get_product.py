import requests

def get_product(product_id):
    url = f"https://dev.shopalyst.com/shopalyst-service/v1/products/{product_id}"

    response = requests.get(url)
    dataset = []
    if response.status_code == 200:
        data = response.json() 
        attribute_names = data.get("attributeNames",[])
        attribute_values = data.get("attributeValues",[])
        color_index = None
        title_dict = {attr.get("id"):attr.get("title") for attr in attribute_values}

        for value in attribute_names:
            if value.get("name", "") == "color":
                color_index = value.get("id")
        
        

        skuset = data.get("skuSet",[])
        
        index = 0
        for sku in skuset:
            index+=1
            data_dict = {}
            data_dict["product"] = index
            data_dict["skuId"] = sku.get("skuId",0)
            data_dict["shade"] = sku.get("attributes",{}).get(color_index,"")
            data_dict["offer_price"] = sku.get("offerPrice",0)
            data_dict["title"] = title_dict.get(data_dict.get("shade"))
            dataset.append(data_dict)

    else:
        print("Failed to fetch data:", response.status_code)
    
    print(dataset)

get_product("12C7BFC3752D4209")
