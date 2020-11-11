Feature: aptar requisicao feita no frontend e enviar dados do contrato ao microsservico admin atraves do BFF 
  Como Sistema, quero pegar os dados do contrato informados no frontend pelo administrador,
  e visualiza-los no meu servico.

  Context: O administrador ver os contratos cadastrados 
    Dado que os dados que foram resgistrados utilizem o servico atraves do BFF

    Scenario: Administrador visualiza os contratos cadastrados na aplicacao
        Given a pagina de gerenciar contratos
        When ele visualizar os contratos desejados
        Then o bff requisita o microsservico com os contratos