def item_detail(**kwargs):
    details = [f'{k} : {v}' for k , v in kwargs.items()]
    result = ", ".join(details)
    print(result)

item_detail(name="iPhone" , price = 30_000)
item_detail(name="Xamxi" , price = 50_000)
