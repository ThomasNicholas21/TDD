
# Atividade Prática 03 - Test-Driven Development (TDD)

### Acadêmico: Thomas Nicholas Pedrosa Matias  
**Matrícula:** 2120-657

---

## Objetivo

Esta atividade tem como foco a aplicação do Test-Driven Development (TDD) para desenvolver um algoritmo em Python que calcula a média de três notas. O processo segue as etapas de criação dos testes (Fase Red), implementação do código para satisfazer esses testes (Fase Green) e refatoração do código (Fase Refactor).

---

## Estrutura do Projeto

O projeto está organizado em um repositório com a seguinte estrutura:
- **Arquivo principal:** `media_calculator.py`, onde o algoritmo é implementado.
- **Arquivo de testes:** `test_calcula_media.py`, onde os casos de teste para o algoritmo são definidos.

## Tecnologias e Ferramentas

- **Linguagem de Programação:** Python
- **Ferramenta de Teste:** Pytest
- **Ambiente Virtual:** venv (para isolamento de dependências)

## Etapas do Desenvolvimento

1. ### Preparação

   - Definida a linguagem de programação como Python.
   - Preparação do ambiente de desenvolvimento com a biblioteca `venv` para evitar conflitos de dependências com outros projetos.
   - Instalação da ferramenta de teste `pytest` para criação e execução dos testes.

2. ### Fase Red
   - Nesta etapa, foram escritos testes para o algoritmo de cálculo de média de três notas, incluindo casos especiais como:
     - Todas as notas iguais a zero.
     - Algumas ou todas as notas com valores máximos possíveis.
     - Notas com valores decimais.
   - Os testes foram executados inicialmente e, como esperado, falharam, pois o código ainda não havia sido implementado.

3. ### Fase Green
   - Implementação da função `calcula_media` no arquivo `media_calculator.py` para calcular a média de três notas.
   - Execução dos testes para garantir que a função atende a todos os cenários de teste previamente definidos. Todos os testes passaram.

4. ### Fase Refactor
   - Refatoração da função `calcula_media` para garantir que os parâmetros sejam sempre numéricos, evitando entradas inválidas.
   - Atualização das mensagens de erro nos testes para facilitar a identificação de possíveis falhas e torná-los mais descritivos.
   - Execução dos testes novamente para garantir que a refatoração manteve a funcionalidade correta.

---

## Como Executar o Projeto

1. **Clonar o repositório:**
   ```bash
   git clone <link-do-repositorio>
   cd <nome-do-repositorio>
   ```

2. **Criar e ativar o ambiente virtual:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
   ```

3. **Instalar dependências:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Executar os testes:**
   ```bash
   pytest test_calcula_media.py
   ```

---

## Considerações

Este projeto demonstra o uso do TDD em Python com a biblioteca `pytest`, incluindo a importância do isolamento de ambiente com `venv`. Ele oferece uma base sólida para entender a abordagem iterativa do TDD com foco na qualidade e manutenção do código.
