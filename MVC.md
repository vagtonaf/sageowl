Model-View-Controller

O Model-View-Controller, ou MVC, é um padrão de desenvolvimento utilizado atualmente com o objetivo de separar as "tarefas" de interface e visualização das tarefas de acesso a dados e negócio. Para tal foi criada uma camada denominada controlador (Contoller), que conforme o nome, controla as tarefas de geração de interface (View) e acesso a dados (Model).

Originalmente foi criado como padrão de projeto arquitetural desenvolvido para o ambiente Smalltalk, porém hoje este tipo de arquitetura vem sido utilizado para qualquer aplicação interativa, principalmente Web.

Modelo(Model)

Representa o "domínio" específico da informação em que a aplicação em si opera. Em nosso caso o aluno, professor e a turma fazem parte do domínio de nosso sitema de avaliação. Lógica de domínio adiciona sentido a dados crus (por exemplo, calcular se hoje é aniversário do usuário, ou calcular o total de impostos e fretes sobre um determinado carrinho de compras).

Em nossa aplicações usaremos um Banco de Dados para armazenar os dados. MVC não cita especificamente a camada para acesso aos dados, porque subentende-se que estes métodos estariam encapsulados pelo Model.

Visualização(View)

Representa toda visualização "Renderizada" pela camada de Modelo de maeria a permitir a interação, geralmente uma interface de usuário.

Controlador (Controller)

Processa e responde a eventos, geralmente ações do usuário do sistema, e pode invocar alterações da camada de Modelo. Nesta camada é feita a validação dos dados e também é onde as entradas dos dados dos usuários são filtradas.
