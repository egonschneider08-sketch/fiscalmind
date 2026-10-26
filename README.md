# FiscalMind

Plataforma em planejamento para ajudar pequenas empresas a organizar documentos fiscais, extratos e possíveis divergências, com revisão humana.

## Situação

Este repositório contém a base de organização do projeto. O aplicativo, as integrações e os testes de produto ainda não foram implementados.

## MVP proposto

- Importar documentos fiscais e extratos em formatos a definir.
- Sugerir correspondências e apontar pendências para revisão.
- Registrar confirmações e disponibilizar uma visão dos resultados.

Emissão fiscal e conexão bancária automática são evoluções posteriores sujeitas a validação.

## Organização

- `backend/`: área reservada para regras de negócio e API.
- `frontend/`: área reservada para a interface.
- `docs/`: decisões técnicas e orientações de desenvolvimento.
- `.github/`: modelos para colaboração no GitHub.

As tecnologias e a estrutura interna ainda precisam de validação; não há comandos de instalação ou execução do aplicativo nesta versão.

## Fluxo de trabalho

A branch `main` representa versões estáveis; `develop` integra o trabalho em andamento. Funcionalidades saem de `develop` em branches `feature/...` e retornam por pull request. Veja [Git Flow](docs/GITFLOW.md) e [Como contribuir](CONTRIBUTING.md).

O planejamento completo e o Kanban são mantidos no Notion do projeto. Alterações no código e decisões relevantes devem ser refletidas lá.

## Privacidade

Use somente dados fictícios em exemplos e testes. Não adicione senhas, certificados, notas ou extratos reais ao repositório.
