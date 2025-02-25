import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

@st.cache  # Carregar os dados
def load_data():
    return pd.read_csv('train.csv')

df = load_data()  # Carregar o arquivo

# Definindo as cores azul e vermelho para todos os gráficos
cores = ['#1E90FF', '#FF4500']  # Azul e Vermelho (azul para sobrevivente, vermelho para mortalidade)

# Título do dashboard
st.title('Dashboard Titanic')

# Número total de pessoas, homens e mulheres
total_pessoas = len(df)
total_homens = len(df[df['Sex'] == 'male'])
total_mulheres = len(df[df['Sex'] == 'female'])

# Exibindo as informações no início da página com o uso do st.metric
col1, col2, col3 = st.columns(3)  # Criar 3 colunas para exibir os cards lado a lado

with col1:
    st.metric(label="Total de Pessoas", value=str(total_pessoas))

with col2:
    st.metric(label="Total de Homens", value=str(total_homens))

with col3:
    st.metric(label="Total de Mulheres", value=str(total_mulheres))

# Exibir as primeiras linhas do DataFrame
st.subheader('Primeiras linhas do dataset')
st.write(df.head())

# Gráfico de box plot invertido (vertical) para a variável 'Age' com caixa menor
st.subheader('Diagrama de Caixa de Idade')
# Criando o boxplot invertido (vertical) e com caixa mais estreita
plt.figure(figsize=(8, 6))  # Ajuste do tamanho da figura
sns.boxplot(data=df, y='Age', palette="pastel", width=0.3)  # Usando y='Age' e ajustando a largura
# Títulos e rótulos
plt.title('Distribuição da Idade (Diagrama de Caixa)')
plt.ylabel('Idade')
# Exibir o gráfico no Streamlit
st.pyplot()


# Gráfico de distribuição de sobreviventes (Pizza)
st.subheader('Distribuição de sobreviventes')
# Contagem de sobreviventes e não sobreviventes
sobreviventes = df['Survived'].value_counts()
# Criando o gráfico de pizza
plt.figure(figsize=(6, 6))
# Usando as cores fortes (vermelho e azul)
plt.pie(sobreviventes, labels=['Sobreviveu', 'Não Sobreviveu'], autopct='%1.1f%%', startangle=90, colors=cores)
plt.title('Distribuição de Sobreviventes')
st.pyplot()


# Gráfico de porcentagem de sobreviventes por classe de passageiro (Pclass)
st.subheader('Porcentagem de Sobreviventes por Classe de Passageiro')
# Calculando a porcentagem de sobreviventes e não sobreviventes por classe
sobreviventes_por_classe = df.groupby(['Pclass', 'Survived']).size().unstack(fill_value=0)
sobreviventes_por_classe = sobreviventes_por_classe.div(sobreviventes_por_classe.sum(axis=1), axis=0) * 100
# Definindo as cores corretamente: vermelho para 'Não' e azul para 'Sim'
cores = ['#FF4500', '#1E90FF']  # Vermelho para "Não" e Azul para "Sim"
# Criando o gráfico de barras empilhadas
sobreviventes_por_classe.plot(kind='bar', stacked=True, color=cores, figsize=(8, 6))
# Títulos e rótulos
plt.title('Porcentagem de Sobreviventes por Classe de Passageiro')
plt.xlabel('Classe de Passageiro')
plt.ylabel('Porcentagem (%)')
plt.xticks([0, 1, 2], ['Classe 1', 'Classe 2', 'Classe 3'], rotation=0)
plt.legend(title='Sobreviveu', labels=['Não', 'Sim'])
# Exibir o gráfico no Streamlit
st.pyplot()


# Gráfico de porcentagem de sobreviventes por sexo
st.subheader('Porcentagem de Sobreviventes por Sexo')
# Calculando a porcentagem de sobreviventes e não sobreviventes por sexo
sobreviventes_por_sexo = df.groupby(['Sex', 'Survived']).size().unstack(fill_value=0)
sobreviventes_por_sexo = sobreviventes_por_sexo.div(sobreviventes_por_sexo.sum(axis=1), axis=0) * 100
# Definindo as cores corretamente: vermelho para 'Não' e azul para 'Sim'
cores = ['#1E90FF', '#FF4500']  # Vermelho para "Não" e Azul para "Sim"
# Criando o gráfico de barras empilhadas
sobreviventes_por_sexo.plot(kind='bar', stacked=True, color=cores, figsize=(8, 6))
# Títulos e rótulos
plt.title('Porcentagem de Sobreviventes por Sexo')
plt.xlabel('Sexo')
plt.ylabel('Porcentagem (%)')
plt.xticks([0, 1], ['Masculino', 'Feminino'], rotation=0)
plt.legend(title='Sobreviveu', labels=['Sim', 'Não'])
# Exibir o gráfico no Streamlit
st.pyplot()


# Gráfico de idade
st.subheader('Distribuição de Idades')
sns.histplot(df['Age'].dropna(), kde=True, color=cores[0])  # Usando o azul forte para o histograma
plt.title('Distribuição de Idades')  # Título em português
plt.xlabel('Idade')  # Rótulo em português
plt.ylabel('Frequência')  # Rótulo em português
st.pyplot()

