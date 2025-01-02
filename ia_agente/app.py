from http import HTTPStatus

from fastapi import FastAPI

from ia_agente.schemas import Mensagem

app = FastAPI()


@app.get('/', status_code=HTTPStatus.OK, response_model=Mensagem)
def read_root():
    return {'message': 'Olá mundo!'}
