Feature: criar requisicao e enviar dados do contrato ao microsservico admin-api atraves do BFF 
  Como Sistema, quero registrar um contrato na aplicacao,
  e armazenar no meu servico.

  Context: O administrador criar os contratos na aplicacao
    Dado que os dados sejam resgistrados e utilizem o servico atraves do BFF

    Scenario: Administrador cadastra os contratos na aplicacao
        Given a pagina de criar novo contrato
        When ele regista novo conteudo do contrato da solicitacao
        | contractor          | cpf_cnpj    | address       | phoneNumber | initialDate | status | endDate    | winery                   |
        | joaoalves@gmail.com | 45212563455 | rua Sao Paulo | 61996853214 | 25-01-2020  | 1      | 25-01-2021 | 5fa6f3398799b84e7c71ba39 |
        Then certifica que o contrato foi feito