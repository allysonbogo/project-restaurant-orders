# Project Restaurant Orders
#### _by [Allyson Belli Bogo](https://www.linkedin.com/in/allysonbogo/)_

## :page_with_curl: Sobre

Neste projeto, o objetivo foi finalizar uma ferramenta de construção de cardápios de um restaurante já iniciada. Foram construídos testes para as classes existentes, desenvolvida uma classe para mapear pratos e receitas, criada uma classe para gerar cardápios e outra para gerenciar o estoque de ingredientes. O objetivo era melhorar a gestão das receitas e do estoque, otimizando processos baseados em arquivos CSV por um sistema mais eficaz e fácil de usar.


## :man_technologist: Habilidades Desenvolvidas

* Conceito de <code>Hashmaps</code> através das estruturas de dados <code>Dict</code> e <code>Set</code>
* Testes automatizados em Python
* Conceitos de Programação Orientada e Objetos (POO)
* Princípios SOLID


## ⚙️ Como Executar

<details>
  <summary> Passo a passo </summary>
  <br>

  1. Clone o repositório em uma pasta de preferência

  ```
  git clone git@github.com:allysonbogo/project-restaurant-orders.git
  ```
  2. Entre na pasta raíz do projeto e crie o ambiente virtual para o projeto

  ```
  python3 -m venv .venv && source .venv/bin/activate
  ```
  3. Instale as dependências

  ```
  python3 -m pip install -r dev-requirements.txt
  ```
</details>


## ⚙️ Funcionalidades

O algoritmo desenvolvido neste projeto conta com módulos para a gestão de pratos e receitas de um restaurante, a construção de cardápios considerando restrições alimentares e a verificação da disponibilidade de ingredientes no estoque.

<details>
  <summary> <code>menu_data</code> </summary>
  
  Esse módulo realiza a leitura do arquivo CSV que contém as informações do cardápio do restaurante e faz o relacionamento do prato com sua respectiva receita, detalhando ingredientes e quantidades.

</details>

<details>
  <summary> <code>menu_builder</code> </summary>
  
  Esse módulo inclui uma classe que integra cardápios e estoque, permitindo filtrar pratos de acordo com restrições alimentares ou que não tenham quantidade suficiente de ingredientes em estoque.

</details>

<details>
  <summary> <code>inventory_control</code> </summary>
  
  Esse módulo inclui um método para a verificação da disponibilidade em estoque de ingredientes de determinadas receitas, passadas como parâmetro para o método. Além disso, também conta com um método que realiza a subtração destes ingredientes do estoque. A subtração somente é realizada caso todos os ingredientes da receita estejam disponíveis em estoque.

</details>
<br>