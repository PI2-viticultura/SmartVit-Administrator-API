Feature: criar requisicao e enviar dados do pedido ao microsservico admin-api atraves do BFF 
  Como Sistema, quero registrar um pedido na aplicacao,
  e armazenar no meu servico.

  Context: O administrador criar os pedidos na aplicacao
    Dado que os dados sejam resgistrados e utilizem o servico atraves do BFF

    Scenario: Administrador cadastra os pedidos na aplicacao
        Given a pagina de criar novo pedido
        When ele regista novo conteudo do pedido da solicitacao
        Then o bff requisita o microsservico para criar pedido