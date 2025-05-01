# Banco de Dados de Energia

## Autores
- [Ainaras Marão](https://github.com/MaraoLT)  (182338)
- [Douglas Henrique R. A. Pereira](https://github.com/Dourialp)  (245202)
- [Yan Oliveira da Silva](https://github.com/Cl4nyz)  (236363)

## Descrição do Projeto

O presente projeto tem como objetivo correlacionar dados sobre energia, PIB, território, demografia e emissão de gases de diferentes países. Para isso, foram realizadas 5 pesquisas (queries) não triviais utilizando os arquivos CSV fornecidos. O projeto busca explorar relações entre essas variáveis, permitindo uma análise mais profunda e integrada dos dados.

## Estrutura do Projeto

- **bancos/**: Contém os arquivos CSV com os dados brutos utilizados nas análises.
  - `energia_processada.csv`: Dados relacionados à energia, incluindo capacidade, emissões, demanda e geração por diferentes fontes e regiões.
  - `WDI_processado.csv`: Dados processados do World Development Indicators (WDI), incluindo PIB, população e área territorial.
- **processamento_dados/**: Scripts para processamento e filtragem dos dados brutos.
  - `process_world_data.ipynb`: Notebook para processar os dados do WDI e gerar o arquivo `WDI_processado.csv`.
- **populate_and_query.ipynb**: Notebook principal para criação de tabelas, população do banco de dados e execução das queries.
- **resultados/**: Contém os resultados das queries em formato CSV.
  - `resultado_query_1.csv` a `resultado_query_5.csv`: Resultados das análises realizadas.
- **modelos/**: Contém o modelo físico do banco de dados.
  - `fisico`: Script SQL para criação das tabelas no banco de dados.
- **README.md**: Documento explicativo sobre o projeto.

## Objetivos das Pesquisas

As pesquisas realizadas têm como foco:

1. **Porcentagem de energia renovável produzida por grupo econômico e ano**  
   Detecta a porcentagem de energia renovável em relação à energia total gerada por grupo econômico a cada ano.

2. **PIB por energia (per capita)**  
   Compara os valores de Produto Interno Bruto per capita e energia per capita por país.

3. **Relação entre matriz energética e emissão de CO2 per capita**  
   Analisa a relação entre a geração de energias não renováveis e a emissão de CO2 por país e ano.

4. **Energia gerada por km² de área florestal**  
   Traça a relação entre geração de energia e área florestal no ano de 2015.

5. **Razão entre habitantes rurais e urbanos por razão entre energia renovável e não renovável**  
   Compara as taxas para valores não nulos, buscando correlações entre demografia e matriz energética.

## Como Utilizar

1. **Configuração do Banco de Dados**  
   Certifique-se de ter um banco de dados PostgreSQL configurado. Atualize as credenciais no arquivo `populate_and_query.ipynb`:
   ```python
   NAME = 'projeto_mc536'
   USER = 'postgres'
   PASSWORD = 'sua_senha_aqui'
   HOST = 'localhost'
   PORT = '5432'
```

3. Execute os scripts SQL disponíveis para realizar as análises.
4. Analise os resultados das consultas para obter insights sobre as correlações entre as variáveis.

## Requisitos

- Banco de dados compatível com SQL (PostgreSQL).
- Ferramenta para manipulação de dados CSV (opcional).

