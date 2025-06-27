#### Justificativa da Escolha do Banco de Dados – MongoDB para o Cenário B
> Uma justificativa para a escolha do banco para o cenário atribuído à sua equipe. Essa deve conter uma discussão incluindo todos os seguintes aspectos: forma de armazenamento de arquivos, linguagem e processamento de consultas, processamento e controle de transações, mecanismos de recuperação e segurança. 

Analisando o cenário fornecido, foi possível identificar que o banco de dados mais adequado para atender às necessidades apresentadas é o MongoDB. A seguir, uma justificativa relativa a cada aspecto exigido:

#### Forma de armazenamento de arquivos
O MongoDB, como exigido pelo Cenário B, possui uma forma flexível de armazenar os dados, pois é um banco baseado em documentos BSON (Binary JSON), que consegue armazenar informações no formato JSON, porém mais otimizado por ficar na forma binária. Por conta disso, o banco consegue armazenar dados que variam bastante em suas propriedades.

Ademais, a estrutura em JSON permite incluir novos dados e campos sem a necessidade de alterar o esquema do banco, como ocorre em Bancos de Dados Relacionais. Além disso, possibilita a inserção de dados com certa tolerância a erro, que pode ser definida pelo criador do banco. Outra vantagem de armazenar as informações em arquivos JSON é que esse formato é amplamente usado entre APIs e, com a storage engine do MongoDB, seu acesso é rápido e eficiente.

Por fim, o MongoDB realiza particionamento automático (Sharding), em que divide os dados em diversos servidores, garantindo um balanceamento de carga pelo sistema e possibilitando uma escalabilidade horizontal, além de garantir que múltiplos acessos possam ser feitos sem sobrecarregar a aplicação.

#### Linguagem e processamento de consultas
A MongoDB Query Language é projetada especificamente para trabalhar diretamente com dados armazenados em documentos do tipo JSON/BSON. Assim, toda a sintaxe de consulta é pensada na estrutura de arquivos JSON e prioriza a consulta direta em documentos com entidades completas, com as informações agregadas.

Dessa forma, as consultas com MongoDB não exigem tantas operações de agregação e conseguem ser mais rápidas. Isso garante uma baixa latência em operações CRUD, uma vez que as entidades completas estão com todas as informações em um mesmo documento.

#### Processamento e controle de transações
A utilização do MongoDB garante atomicidade nas operações nos documentos, sendo assim, atende bem a aplicações que realizam operações CRUD simples em entidades completas.

Ainda, o MongoDB oferece suporte a transações multi-documento com propriedade ACID, permitindo que várias operações sejam realizadas em diferentes documentos de forma atômica e consistente. Porém, mesmo havendo essa possibilidade, transações multi-documento são mais lentas e não são o foco do banco em questão.

#### Mecanismos de recuperação
Existem dois mecanismos principais utilizados pelo MongoDB para garantir a recuperação de dados:

O principal consiste no Journaling, que mantém um registro do histórico de operações de escrita feitas no banco. Assim, no caso de falha no sistema, o MongoDB consegue fazer uma recuperação para o último estado consistente antes da falha, garantindo a integridade dos dados.

Outro mecanismo é o uso de Replica Set, que faz cópias dos dados de forma sincronizada em servidores diferentes. Com isso, se houver uma falha no servidor principal, um dos servidores secundários assume a liderança e substitui o principal, garantindo a recuperação dos dados e constante disponibilidade.

#### Segurança
No caso da segurança, o Cenário B não exigia nada específico. Mesmo assim, o MongoDB conta com diversos recursos para garantir a integridade do banco de dados: autenticação de usuários, autorização com controle baseado em papéis de diferentes níveis, protocolos de segurança nas comunicações via TLS/SSL, criptografia em repouso (Encryption at Rest), entre outros.