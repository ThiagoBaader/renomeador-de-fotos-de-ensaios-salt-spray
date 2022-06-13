Instalação

A PyCEPCorreios pode ser facilmente instalada com o comando a seguir:

pip install pycep-correios

Atualmente, a PyCEPCorreios possui suporte para Python 3.5+.
Como usar

A PyCEPCorreios foi desenvolvida para integração de consultas sob demandas em páginas web. A consulta de CEPs em massa através de scripts ou qualquer outros meios não é recomendada.

A PyCEPCorreios utiliza por padrão de consulta a API provida pelo serviço ApiCEP. Para utilização de outros serviços, devemos indica o serviço desejado ao chamar a função get_address_from_cep. O CEP sempre deve ser uma string e pode ou não conter pontuação.
Exemplo de consulta ao serviço ApiCEP (default):

from pycep_correios import get_address_from_cep, WebService

address = get_address_from_cep('37503-130', webservice=WebService.APICEP)

Exemplo de consulta ao serviço ViaCEP:

from pycep_correios import get_address_from_cep, WebService

address = get_address_from_cep('37503-130', webservice=WebService.VIACEP)

Exemplo de consulta ao serviço dos Correios:

from pycep_correios import get_address_from_cep, WebService

address = get_address_from_cep('37503-130', webservice=WebService.CORREIOS)

Obs.: O serviço de busca de CEP dos Correios é parte integrante do serviço SIGEPWeb e para uso do mesmo é necessário ter contrato com os Correios, conforme indicado no capítulo Introdução presente no manual de integração do serviço.
Retorno e Exceptions

Independente do serviço escolhido, o formato de resposta sempre será um objeto dict contendo as seguintes chaves:

{
    'bairro': 'str',
    'cep': 'str',
    'cidade': 'str',
    'logradouro': 'str',
    'uf': 'str',
    'complemento': 'str',
}

A PyCEPCorreios tambem dá suporte a um grupo de exceptions que podem ser utilizadas para tratamento de quaisquer erros que ocorram durante o processo de consulta.

from pycep_correios import get_address_from_cep, WebService, exceptions

try:

    address = get_address_from_cep('37503-130', webservice=WebService.APICEP)

except exceptions.InvalidCEP as eic:
    print(eic)

except exceptions.CEPNotFound as ecnf:
    print(ecnf)

except exceptions.ConnectionError as errc:
    print(errc)

except exceptions.Timeout as errt:
    print(errt)

except exceptions.HTTPError as errh:
    print(errh)

except exceptions.BaseException as e:
    print(e)

Como contribuir

Deseja participar do desenvolvimento da PyCEPCorreios? Veja a guideline de contribuição aqui.
Créditos

Copyright (C) 2016-2021 por Michell Stuttgart
