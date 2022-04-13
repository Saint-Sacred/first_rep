from matplotlib import pyplot as plt
from scipy import integrate
import numpy as np

f1 = lambda x: 6*(np.sin(2*np.pi*x)+1)
f2 = lambda x: 3*2/((x-1)+1)
f3 = lambda x: 1.5*2/((x-2)+1)
#Теоретическое значение интеграла:
true_value = integrate.quad(f1, 0, 1)[0] + integrate.quad(f2, 1, 2)[0] + integrate.quad(f3, 2, 3)[0]
print('True value:', true_value)

x1 = np.arange(0,1,0.001)
x2 = np.arange(1,2,0.001)
x3 = np.arange(2,3,0.001)

plt.plot(x1,f1(x1), label = '6*(np.sin(2*np.pi*x)+1)')
plt.plot(x2,f2(x2), label = '3*2/((x-1)+1)')
plt.plot(x3,f3(x3), label = '1.5*2/((x-2)+1)')
plt.legend()
plt.show()

all_score = [] # общее количество успешных событий для всех выборок
for i in range(0,15):
    f_rez = []
    for j in range (2**i):
        x = np.random.uniform(0, 3)
        if x<1:
            f_rez.append(f1(x))
        elif 1<=x<2:
             f_rez.append(f2(x))
        else:
            f_rez.append(f3(x))
    all_score.append(3*sum(f_rez)/2**i)

[print('2^', i, ' tests - %.4f' % all_score[i], sep='') for i in range(len(all_score))]

plt.plot(range(len(all_score)), all_score, label='calculated values')
plt.plot(range(len(all_score)), [true_value]*len(all_score), color='red', label='true values')
plt.xticks(range(len(all_score)) ,[r'$2^{'+str(i)+'}$' for i in range(len(all_score))])
plt.legend()
plt.title("F'(N)")
plt.show()
