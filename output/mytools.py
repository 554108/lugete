import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams["front.sans-serif"] = ["SimHei"] ?# ��������
def ��������������ͳ�Ʊ�(������������):
? ? result = ����[������].value_counts(sort=False)
? ? ����ͳ��ͼ = pd.DataFrame(result)
? ? ����ͳ��ͼ['����'] = ����ͳ��ͼ['count'] / ����ͳ��ͼ['count'].sum()
? ? ����ͳ��ͼ['�ۼƱ���'] = ����ͳ�Ʊ�['����'].cumsum()
? ? return ����ͳ�Ʊ�
def ����ֱ��ͼ(����):
? ? x = ������index
? ? y = ����['count'].values
? ? fig. ax2 = plt.subplots()
? ? ax2.bar(x, y)
? ? plt.show()