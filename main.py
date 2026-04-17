texto = "Hello world!"

print("Hello World!")
from fastapi import FastAPI
app = FastAPI()

@app.get("/information/{user}")
def mostrar_texto(user: str):
    return {"texto": f"ola mr {user}"}


credit_cards = {
    "zolmar": "214214124412",
    "lua": "645646545645"
}

def verificar_solicitacao_de_cartao(user, cartao_novo):
    checar_score(user)
    requisitos_cartao_novo = get_requisitos_cartao_novo(cartao_novo)

    if requisitos_cartao_novo.investimentos <= user.investimentos:
        return True
    else:
        return False


@app.get("/information-creditcard/{user}")
def mostrar_texto(user: str):
    print(f"buscando dados do cartao de credito de {user}")
    cartao_de_credito = credit_cards[user] if user in credit_cards else "nao tem cartao"
    return {"texto": f"ola mr {user} seu cartao de credito é {cartao_de_credito}"}
