Feature: criar requisicao e enviar dados do pedido ao microsservico admin-api atraves do BFF 
  Como Sistema, quero registrar um pedido na aplicacao,
  e armazenar no meu servico.

  Context: O administrador criar os pedidos na aplicacao
    Dado que os dados sejam resgistrados e utilizem o servico atraves do BFF

    Scenario: Administrador cadastra os pedidos na aplicacao
        Given a pagina de criar novo pedido
        When ele regista novo conteudo do pedido da solicitacao
        | description | name         | email          | phoneNumber | status |
        | Testar bdd  | Joao Ninguem | test@gmail.com | 61996853214 | 0      |
        Then certifica que o pedido foi feito
        | description | name         | email          | phoneNumber | status |
        | Testar bdd  | Joao Ninguem | test@gmail.com | 61996853214 | 0      |