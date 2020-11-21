Feature: aptar requisicao feita no frontend e enviar dados do pedido ao microsservico admin atraves do BFF 
  Como Sistema, quero pegar os dados do pedido informados no frontend pelo administrador,
  e visualiza-los no meu servico.

  Context: O administrador ver os pedidos cadastrados 
    Dado que os dados que foram resgistrados utilizem o servico atraves do BFF

    Scenario: Administrador visualiza os pedidos cadastrados na aplicacao
        Given a pagina de gerenciar pedidos
        When ele visualizar os pedidos desejados
        Then pega os pedidos registrados