# Git Flow do FiscalMind

Este documento descreve o fluxo adotado para a organização inicial. Até existir uma versão de produção, `main` representa a base estável do repositório.

## Branches permanentes

- `main`: versão estável e, quando houver, publicada.
- `develop`: integração das funcionalidades em desenvolvimento.

## Branches temporárias

| Tipo | Origem | Destino | Exemplo |
| --- | --- | --- | --- |
| Funcionalidade | develop | develop | feature/fm10-importacao-xml |
| Correção de desenvolvimento | develop | develop | bugfix/fm14-validacao-csv |
| Preparação de versão | develop | main e depois develop | release/0.1.0 |
| Correção urgente de produção | main | main e depois develop | hotfix/0.1.1 |

Use letras minúsculas, hífens e o identificador do cartão quando existir. Não é necessário criar branches temporárias antecipadamente.

## Fluxo de uma funcionalidade

```bash
git checkout develop
git pull origin develop
git checkout -b feature/fm10-importacao-xml
# Edite e revise os arquivos desejados.
git add caminho/do/arquivo
git commit -m "feat: iniciar importação de documentos"
git push -u origin feature/fm10-importacao-xml
```

Abra no GitHub um pull request de `feature/...` para `develop`. Indique critérios de aceite, validação, limitações e o cartão. Revise as diferenças e integre somente quando a mudança estiver pronta. Exclua a branch temporária depois que não for necessária.

## Release

Quando houver uma versão a disponibilizar, crie `release/x.y.z` a partir de `develop`. Conclua testes, documentação e eventuais correções. Abra PR para `main`, registre a versão com tag e incorpore as alterações da release de volta em `develop`. Não marque uma versão como publicada antes da implantação efetiva.

## Hotfix

Para um defeito urgente em uma versão de produção, crie `hotfix/x.y.z` a partir de `main`. Revise e teste a correção, integre-a por PR em `main` e depois em `develop`; crie uma tag após aprovação. Se uma release estiver em andamento, avalie também seu impacto nela.

## Proteção e automação

Revisão por PR, proteção das branches e verificações de CI são objetivos do projeto. Elas só estarão ativas quando configuradas no GitHub e verificadas. A configuração inicial de documentação, por si só, não as habilita.

## Notion

Ao iniciar ou concluir cada entrega, atualize o cartão correspondente com o estado real e links para PR, commit, testes e decisões. Ajuste os documentos afetados. O Notion organiza o trabalho; arquivos, comandos e contratos executáveis ficam no repositório.
