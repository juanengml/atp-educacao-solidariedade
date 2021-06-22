
import streamlit as st
from datetime import datetime as dt 
from streamlit_player import st_player
import streamlit.components.v1 as components


def main():
  st.title(" FLAVOR TREE  ")
  option = st.sidebar.selectbox('Como usar este App',("Inicio","Copo Sustentavel","Empreendorismo Social"))
  if option == "Inicio":
      st.title("Você sabe o que é Desenvolvimento Sustentavel ? ou Empreendedorismo Social ?")
      left_column, right_column = st.beta_columns(2)
      with left_column:
         st.header("Desenvolvimento Sustentavel ONU")
         st.image("https://cdn4.ecycle.com.br/cache/images/2021-01/50-650-ods.png")
         st.write("https://odsbrasil.gov.br/")
      with right_column:
         st.header("Empreendedorismo Social")
         st_player(url="https://www.youtube.com/watch?v=HLodRmvRXJk")

      st.header("Como Posso Contribuir para Desenvolvimento Sustentavel ?")
      st_player(url="https://www.youtube.com/watch?v=w7v41GlFSvo",height=400)

    

  if option == "Copo Sustentavel":
      st.title("Copo Sustentavel ")
      col1, col2 = st.beta_columns(2)
      with col1:
         st.header("""
         Este projeto é bastante simples e com ele é possivel reduzir a quantidade de copos consumidos 
         Nas escolas, atualmente a maioria das escolas publicas do brasil, usam copos como este ao lado que vc 
         esta vendo. Alunos usam e compatilham do mesmo copo. 
         """)
         st.write("## O Principal Objetivo é Reduzir o consumo de copos plásticos para copos de papel ecológico")
         st.image("https://www.meucopoeco.com.br/site/wp-content/uploads/2016/12/foto6.jpg")
         st.write("⬇️ ")
         st.image("https://i.pinimg.com/originals/75/ef/c5/75efc5c504cebcaeab51766b5eff9bcf.gif",width=150)


      with col2:
         st.header("Papel de Sementes") 
         st.write("Preserve a Vida - Papeis retornaveis e plantaveis - Empreendedorismo Social e Eco")
         st.image("https://http2.mlstatic.com/D_NQ_NP_629119-MLB41997980502_052020-O.jpg")
         
      
      st.write("---")
      st.title(""" 💡 Mas como posso fazer um copo com papel ?""")
      st.write("É simples, basta seguir o video abaixo ^_^")
      st_player("https://www.youtube.com/watch?v=ID5Toa_lp3Q")
      col3, col4 = st.beta_columns(2)
      with col3:
          st.write("## 🥤 Beba agua  ")
          st.image("https://media1.giphy.com/media/l4vcQYDDqFqy8rZunn/giphy.gif")
      with col4:
          st.write("## 🌱 Plante !!! ")
          st.image("https://brmais.net/storage/posts/April2018/bOQruwOikG5wpyvzGlWD.png") 


  if option=="Empreendorismo Social":
      st.title("Empreendorismo Social")
      st.write("Um empreendedor social é aquele que apresenta e desenvolve soluções inovadoras para atender aos problemas sociais. São profissionais ambiciosos e persistentes, que se preocupam com as grandes questões sociais e estão em busca de ideias que tragam mudanças em grande escala.")
      st.write("""
      ## Gerando Falcões

Iniciativa de Eduardo Lyra, jovem nascido na periferia de São Paulo, que resolveu se dedicar a melhorar a vida de crianças que passam pelas mesmas dificuldades que enfrentou na infância. Cerca de 30 mil estudantes têm sido impactados pelas ações do projeto, que tem como meta central promover o protagonismo dos jovens e fortalecê-los enquanto motores da transformação da sociedade.

www.jovensfalcoes.com.br

## Instituto Chapada

Iniciativa que tem como mentora e principal líder a pedagoga Cybele Oliveira, é uma organização focada em ajudar a melhorar a qualidade da educação pública. A entidade faz isso oferecendo, principalmente, apoio à formação continuada de professores e gestores de escolas. Além disso, auxilia a criação de redes colaborativas voltada a fortalecer o ensino formal e políticas púbicas de educação.

www.institutochapada.org.br

## Graacc

Desde 1991, essa iniciativa do oncologista pediátrico Antonio Sergio Petrilli tem sido uma forte aliada do combate ao câncer infantil no Brasil. A entidade já tratou mais de 5 mil pacientes, com uma taxa de cura que fica em torno de 70%. A organização funciona com base em um rigoroso sistema de gestão e atendimento que envolve pesquisadores de universidades, a iniciativa privada e a sociedade.

www.graacc.org.br/

## Asid

Iniciada como trabalho de faculdade, a Ação Social para Igualdade das Diferenças atua desde 2010 com um compromisso central: auxiliar na gestão de escolas e instituições que trabalham com pessoas especiais. Alexandre Amorim, Luiz Ribas e Diego Moreira conduzem a organização, que desenvolveu uma metodologia administrativa que aplicam nas entidades atendidas, com o objetivo de melhorar a qualidade do ensino gratuito oferecido a pessoas especiais.

www.asidbrasil.org.br/

## Adaptsurf

Usando o esporte como instrumento, o projeto tem como objetivo promover a inclusão e integração social das pessoas com deficiência ou mobilidade reduzida. Uma das formas encontradas para tanto foi o surf adaptado. O Instituto promove, divulga e difunde o surf como modalidade de esporte adaptado, desenvolvendo parcerias com entidades ligadas ao esporte, escolas de surf e outros projetos.

www.adaptsurf.org.br/
      """)  
  st.write(dt.now())

if __name__ == "__main__":
   main()

