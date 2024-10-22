import pandas as pd
import matplotlib.pyplot as plt


dates = []
hours = []
names = []
messages = []
file = open("_chat.txt","r",encoding="utf-8")
count = 0
for line in file:
    if(count==0):
        count+=1
        continue
    try:
        date = line.split("]")[0].replace('[','').split(",")[0].strip()
        hour = line.split("]")[0].replace('[','').split(",")[1].strip()
        name = line.split("]")[1].replace('~','').split(':')[0].strip()
        message = line.split("]")[1].replace('~','').split(':')[1].strip()

        dates.append(date)
        hours.append(hour)
        names.append(name)
        messages.append(messages)
        count +=1
    except:
        message = messages.pop()
        messages.append(line)

df = pd.DataFrame({"name":names,"message":messages,"date":dates,"hour":hours})


while 1:
    op = input("""Escreva:
    1==Resumo das conversas
    2==Histórico de remetente
    3==Grafico de Pizza
    4==Grafico de linha
    """)

    match op:
        case '1':
            print(df.groupby("name").size().sort_values(ascending=False))
        case '2':
            name = input("Escreva o nome do remetente: ")
            result = df[df["name"] == name]
            print(result)
        case '3':
            message_counts = df.groupby("name").size().sort_values(ascending=False)
            plt.figure(figsize=(8, 8))
            plt.pie(message_counts, labels=message_counts.index, autopct='%1.1f%%', startangle=90, colors=plt.cm.Paired.colors)
            plt.title("Distribuição de mensagens por remetente")
            plt.axis('equal')
            plt.show()
        case '4':
            messages_per_day = df.groupby('date').size()
            plt.bar(messages_per_day.index, messages_per_day.values)  # Passa as datas como índice e contagem de mensagens como valores
            plt.xlabel("Data")
            plt.ylabel("Número de Mensagens")
            plt.title("Número total de mensagens ao longo do tempo")
            plt.xticks(rotation=45)
            plt.tight_layout()
            plt.show()
        case _:
            print("valor invalido!!")

    











        