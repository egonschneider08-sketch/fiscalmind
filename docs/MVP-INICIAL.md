# FiscalMind — escopo inicial (hipóteses a validar)

Este primeiro incremento contém apenas regras experimentais de sugestão em memória. Não há aplicação, autenticação, importação, persistência ou confirmação. Não usar dados reais.

## Decisões de produto propostas

- Gestor administra empresa e membros; operador importa e revisa; contador convidado acompanha conforme permissão. Papéis e recuperação de conta ainda precisam de desenho e testes.
- Primeiro documento: XML NF-e suportado, com chave, data, valor, emissor e destinatário revisáveis. PDF apenas como anexo futuro; NFS-e não está abrangida. Validar versões e amostras com contador.
- CSV inicial, UTF-8, cabeçalho `data,descricao,valor,id_transacao`, data ISO `AAAA-MM-DD`, valor decimal com ponto e sinal negativo para saída. Exemplo fictício: `2026-01-10,Fornecedor exemplo,-105.00,tx-001`. Adaptadores bancários e mapeamento devem ser validados; não implementados.
- Duplicidade: chave NF-e por empresa; extrato por identificador estável fornecido pela fonte e conta. Quando não houver ID confiável, sinalizar possível repetição para revisão, sem excluir automaticamente.
- Primeira regra experimental: valor exato em centavos e diferença absoluta entre datas de até 7 dias. Todas as alternativas são sugestões explicáveis; mesmo valor não comprova pagamento. A janela depende de validação e datas de emissão podem ser pouco adequadas para pagamentos.
- Confirmar, rejeitar e desfazer exigirão autorização por empresa, auditoria e operação atômica. Impedir duplicidade e alocação acima do saldo; tratar concorrência no banco. Ainda não implementados.
- Arquivos inválidos recebem erros por linha/campo; itens incompletos permanecem pendentes. Sem leitura silenciosa ou confirmação automática.
- Fora do primeiro recorte: emissão fiscal, integração bancária automática e OCR. O D04 também propõe exportação, PDF de apoio e solicitações de dados; mantidos como requisitos a priorizar, não considerados já implementados nem descartados.

## Arquitetura

Monólito modular: React/TypeScript, FastAPI e PostgreSQL são escolhas candidatas adequadas por clareza e transações, ainda não instaladas ou verificadas neste incremento. Funções de domínio devem funcionar sem HTTP ou banco. A estrutura existente `backend/` e `frontend/` é preservada, em vez do caminho alternativo `apps/` sugerido no Notion. Worker e fila ficam para necessidade demonstrada.

## Ordem sugerida

1. Ambiente reproduzível, API e automação de testes.
2. Identidade, empresas e autorização, com testes de isolamento.
3. Armazenamento e importação segura de XML e CSV.
4. Sugestões, confirmação humana, reversão e auditoria transacional.
5. Painel e exportações priorizadas; testes integrados e preparação de piloto.

Antes de dados reais: revisão de segurança, controle de acesso, tratamento e retenção de dados, backups, limites de arquivo, observabilidade e responsabilidades devem ser definidos e verificados.
