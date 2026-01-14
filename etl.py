import json

users = [
    {"id": 1, "nome": "Daniel", "news": []},
    {"id": 2, "nome": "Jonatas", "news": []},
    {"id": 3, "nome": "Maria", "news": []}
]

def gerar_mesagem(user):
    if(user["id"] == 1):
        return f"Olá {user['nome']}, com investimento sua vida pode mudar muito!"
    elif(user["id"] == 2):
        return f"Olá {user['nome']}, dinheiro é algo que temos de ter cuidado! investimento é seguro."
    elif(user["id"] == 3):
        return f"Olá {user['nome']}, sabe aquela viagem da qual você tanto quer ir daqui um tempo? Com investimento é possível!"
    
for user in users:
    mensagem = gerar_mesagem(user)
    user["news"].append({"description": mensagem})

with open("resultado.json", "w", encoding="utf-8") as f:
    json.dump(users, f, ensure_ascii=False, indent=4)

print("ETL finalizado com sucesso!")