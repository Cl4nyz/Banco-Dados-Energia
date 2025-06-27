# Justificativa da Escolha
> Uma justificativa para a escolha do banco para o cenário atribuído à sua equipe. Essa deve conter uma discussão incluindo todos os seguintes aspectos: forma de armazenamento de arquivos, linguagem e processamento de consultas, processamento e controle de transações, mecanismos de recuperação e segurança. 

Analisando o cenário fornecido, foi possível identificar que o banco de dados mais adequado para atender às necessidades apresentadas é o **MongoDB**. A seguir uma justificativa relativa a cada aspecto exigido:

- ##### Forma de armazenamento de arquivos
O MongoDB, como exigido pelo Cenário B, possui uma forma flexível de armazenar os dados, pois é um banco baseado em documentos **BJSON (Binary JSON)**, que conseguem armazenar informações no formato JSON, porém, mais otimizado por ficar na forma binária. Por conta disso, o banco consegue armazenar dados que variam bastante em suas propriedades. Ademais, a estrutura em JSON permite incluir novos dados e campos sem a necessidade de alterar o esquema do banco, como ocorre em Bancos de Dados Relacionais. Outra vantagem de armazenar as informações em arquivos JSON é que esse formato é amplamente usado entre APIs e, com a __storage engine__ do MongoDB, seu acesso é rápido e eficiente.

- ##### Linguagem e processamento de consultas
A MongoDB Query Language é projetada especificamente para trabalhar diretamente com dados armazenados em documentos do tipo JSON/BJSON. Assim, toda a sintaxe de consulta é pensada na estrutura de arquivos JSON e prioriza a consulta direta em documentos com entidades completas com as informações agregadas. Dessa forma, as consultas com MongoDB não exigem tantas operações de agregação e conseguem ser mais rápidas. Isso garante uma baixa latência em operações CRUD, uma vez que, as entidades completas estão com todas as informações em um mesmo documento.

- ##### Processamento e controle  de transações


- ##### Mecanismos de recuperação
Existem dois mecanismos principais utilizados pelo MongoDB para garantir a recuperação de dados:

O principal consiste no **Journaling** que mantém um registro do histórico de operações de escrita feitas no banco. Assim, no caso de falha no sistema, o MongoDB consegue fazer uma recuperação para o último estado consistente antes da falha, garantindo a integridade dos dados.

Outro mecanismo é o uso de **Replica Set** que faz cópias dos dados de forma sincornizada em servidores diferentes. Com isso, se houver uma falha no servidor principal, um dos servidores secundários assume a liderança e substitui o principal, garantindo recuperação dos dados e alta disponibiliade.

Dessa forma, o MongoDB satisfaz os requerimentos de suporte a replicação e par
- ##### Segurança




#### 🟢 Cenário B
Seu desafio é desenvolver um sistema para armazenamento de dados **semi-estruturados** que podem **variar bastante em suas propriedades**. O modelo de dados deve permitir a **inclusão de novos campos sem exigir alterações** no esquema ou migrações. O volume de **acessos simultâneos** é alto, especialmente por APIs que manipulam **entidades completas** (com todas as suas informações agregadas). Há uma exigência de **escalabilidade horizontal** e suporte a **replicação e particionamento automático**.

#### Requisitos Técnicos:
- [X] Estrutura de dados flexível, com esquemas dinâmicos.
- [X] Manipulação (leitura e escrita) de entidades completas.
- [ ] Alta escalabilidade e tolerância a falhas.
- [X] Baixa latência em operações CRUD (Create Read Update Delete).
- [ ] Suporte a replicação, particionamento e balanceamento de carga.