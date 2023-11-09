criar o ambiente virtual

```
python -m venv ./venv
```

ativa o ambiente Linux/MAC 

```
source venv/bin/activate
```

```
venv/Scripts/Activate
```

instala o fastAPI e suas dependências

```
pip install fastapi uvicorn
```

sobe o servidor da fastapi

```
uvicorn app:app --reload
```

Mostra os endpoints

```
http://127.0.0.1:8000/api/company
http://127.0.0.1:8000/api/company/?company=Lasanha
```

E documentação

```
localhost:8000/docs
localhost:8000/redoc 
```

