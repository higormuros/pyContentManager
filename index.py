import json
from AICliente import GoogleAIStudioClient
from pydantic import BaseModel

if __name__ == "__main__":
    prompt = """ Use este JSON schema:

        Return = {'titulo': str, 'paragrafos': list[str], 'tags': list[str]}"""

    client = GoogleAIStudioClient()
    modelo = "gemini-2.0-flash"
    texto_para_enviar = "O texto a seguir foi escrito por mim e gostaria de um resumo dele. A resposta deve incluir um titulo, tags (pois o texto retornado será postado no meu blog) e um array de strings, sendo cada string um parágrafo do texto. Gostaria de que você me retornasse um resumo do texto no formato informado. Os parágrafos não podem ter mais de 2000 caracteres e desejo apenas 3 parágrafos. Este é o texto para resumir: Muito tem sido dito e publicado a respeito do sistema de saúde brasileiro. Em todos os cursos de formação na área de saúde do país são dedicados um, dois ou mais semestres a esse complexo e original sistema. E o desafio dos professores é sempre o mesmo: como motivar os alunos ao estudo das políticas de saúde e à compreensão da organização do sistema e, principalmente, da importância que esse conhecimento exercerá em sua prática profissional? Não são raros os momentos em que, para discutir com alunos uma situação de saúde vivida nas unidades de saúde, nos cenários diversificados ou em um hospital universitário, é necessário compreender em maior profundidade as origens da Reforma Sanitária, o financiamento do sistema, as relações de trabalho na saúde, o modelo de atenção, a participação popular na elaboração de políticas de saúde e tantos outros temas que perpassam as salas de aula dos cursos de saúde brasileiros, sejam técnicos ou universitários, de graduação ou pós-graduação. A coletânea Saúde e democracia: história e perspectivas do sistema é um importante instrumento de apoio ao desafio cotidiano dos professores na labuta da formação permanente em saúde. Escrita por 25 autores, todos pesquisadores e professores com vasta experiência nos temas desenvolvidos. Os organizadores desta coletânea convidaram pesquisadores atuantes no país para produzirem um amplo painel do passado e do presente da construção do sistema de saúde brasileiro. Em resultado, o leitor é presenteado com uma rica coleção de análises que enfoca os aspectos mais importantes, tanto os históricos quanto os relativos às principais questões a serem enfrentadas hoje, como é o caso do mais recente (década de 1990) programa de Saúde. {prompt}"


    resposta = client.enviar_texto(modelo, texto_para_enviar)

    if resposta:
        print(json.dumps(resposta, indent=2, ensure_ascii=False))
    else:
        print("Falha ao obter a resposta.")