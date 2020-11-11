Feature: criar requisicao e enviar dados do contrato ao microsservico admin-api atraves do BFF 
  Como Sistema, quero registrar um contrato na aplicacao,
  e armazenar no meu servico.

  Context: O administrador criar os contratos na aplicacao
    Dado que os dados sejam resgistrados e utilizem o servico atraves do BFF

    Scenario: Administrador cadastra os contratos na aplicacao
        Given a pagina de criar novo contrato
        When ele regista novo conteudo do contrato da solicitacao
        Then o bff requisita o microsservico para criar contrato