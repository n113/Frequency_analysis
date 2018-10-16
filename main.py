text="""
В общем, есть такая тема — частотный анализ текста. Утверждается, что для данного языка частота встречаемости отдельных букв в осмысленном тексте есть устойчивая величина. Устойчивыми также являются комбинации двух, трех (биграммы, триграммы) и четырех букв.
Этот факт, в частности, использовался в криптографии для вскрытия шифров.
"""


###############################################################################################
def letterCounter(text, letter):
    counter=0.0
    for i in range(len(text)):
        if text[i]==letter:
            counter+=1
    return counter / len(text.lower()) *100

#letterCounter(text,"ы")
dic={"0": 0}

abc="абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
for i in range(len(abc)):
    dic.update({abc[i]: float((letterCounter(text.lower(), abc[i])))})




sortedDIc = sorted(dic.items(), key=lambda x: x[1])

"""
#to print dict (note the key word items)
for k, v in dic.items():
    print (k, '-->', v)
"""

for i in range(len(sortedDIc)):
    print(sortedDIc[i])


