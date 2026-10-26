# Teste do domínio inicial

Com Python 3.10 ou superior, na raiz do repositório:

```sh
cd backend
python -m unittest discover -s tests -v
```

Não são necessárias dependências externas para estes testes. Eles verificam apenas a função de sugestão em memória. A comparação de identificadores de empresa não substitui autenticação, autorização nem testes de isolamento no banco ou na API.
