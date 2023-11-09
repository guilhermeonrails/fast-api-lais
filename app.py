from fastapi import FastAPI, Query

app = FastAPI()

data = [
    {'id':1, 'company':'Hamburger', 'item': 'lanche'},
    {'id':2, 'company':'Hamburger', 'item': 'Coca-cola'},
    {'id':3, 'company':'Lasanha', 'item': 'Massa'},
    {'id':4, 'company':'Lasanha', 'item': 'Pizza'},
    {'id':5, 'company':'Lasanha', 'item': 'Macarrão'},
]

@app.get('/api/hello')
def say_hello():
    return {'Hello':'World'}


@app.get('/api/company/')
def get_company(company: str = Query(None)):
    if company is None:
        return {'data': data}
    itens = []
    for valor in data:
        if valor['company'] == company:
            itens.append(valor['item'])
    return {'company': company, 'itens': itens}