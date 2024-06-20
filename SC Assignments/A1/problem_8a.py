import numpy as np
from copy import copy, deepcopy
import pandas as pd

n = [10, 20, 30, 40]
x = []
mats_1 = []
hilbert_mats = []
rand_mats = []
b_dict = {10: {'hil': [],
               'rand': [],
               'ones': []},
          20: {'hil': [],
               'rand': [],
               'ones': []},
          30: {'hil': [],
               'rand': [],
               'ones': []},
          40: {'hil': [],
               'rand': [],
               'ones': []}
          }

ans = {10: {'hil': [0 for i in range(5)],
            'rand': [0 for i in range(5)],
            'ones': [0 for i in range(5)],
            'x': [1 for i in range(10)]},
       20: {'hil': [0 for i in range(5)],
            'rand': [0 for i in range(5)],
            'ones': [0 for i in range(5)],
            'x': [1 for i in range(20)]},
       30: {'hil': [0 for i in range(5)],
            'rand': [0 for i in range(5)],
            'ones': [0 for i in range(5)],
            'x': [1 for i in range(30)]},
       40: {'hil': [0 for i in range(5)],
            'rand': [0 for i in range(5)],
            'ones': [0 for i in range(5)],
            'x': [1 for i in range(40)]}
       }

for i in range(4):
    hilbert_mats.append([])
    rand_mats.append([])
    mats_1.append([])


def hilbert(n, num):  # num is the matrix of the n[i] size
    global hilbert_mats
    for a in range(n):
        hilbert_mats[num].append([0]*n)

    for i in range(n):
        for j in range(n):
            hilbert_mats[num][i][j] = 1/((i+1)+(j+1)-1)


def rand_mat(n, num):
    global rand_mats
    for a in range(n):
        rand_mats[num].append([0]*n)

    rand_mats[num] = np.random.sample(size=(n, n)).tolist()


def mat(n, num):
    global mats_1
    for a in range(n):
        mats_1[num].append([0]*n)

    for i in range(n):
        for j in range(n):
            if i > j:
                mats_1[num][i][j] = -1
            else:
                mats_1[num][i][j] = 1


for i in range(4):
    hilbert(n[i], i)
    rand_mat(n[i], i)
    mat(n[i], i)

for i in range(len(n)):
    x = [1 for i in range(n[i])]
    b_dict[n[i]]['hil'] = np.matmul(hilbert_mats[i], x)
    b_dict[n[i]]['rand'] = np.matmul(rand_mats[i], x)
    b_dict[n[i]]['ones'] = np.matmul(mats_1[i], x)


def wo_pivot(A, b, n):
    # print(A)
    temp = deepcopy(A)
    x = [0 for i in range(n)]
    for k in range(n-1):
        for i in range(k+1, n):
            atemp = temp[i][k]/temp[k][k]
            temp[i][k] = atemp
            for j in range(k+1, n):
                temp[i][j] = temp[i][j]-atemp*temp[k][j]
            b[i] = b[i]-atemp*b[k]

    x[n-1] = b[n-1]/temp[n-1][n-1]

    for i in range(n-2, -1, -1):
        sum = b[i]
        for j in range(i+1, n):
            sum = sum - temp[i][j]*x[j]

        x[i] = sum/temp[i][i]

    return x


wo_pivot_x = {10: {'hil': [],
                   'rand': [],
                   'ones': []},
              20: {'hil': [],
                   'rand': [],
                   'ones': []},
              30: {'hil': [],
                   'rand': [],
                   'ones': []},
              40: {'hil': [],
                   'rand': [],
                   'ones': []}
              }

for i in range(len(n)):
    wo_pivot_x[n[i]]['hil'] = wo_pivot(
        hilbert_mats[i], b_dict[n[i]]['hil'], n[i])
    wo_pivot_x[n[i]]['rand'] = wo_pivot(
        rand_mats[i], b_dict[n[i]]['rand'], n[i])
    wo_pivot_x[n[i]]['ones'] = wo_pivot(mats_1[i], b_dict[n[i]]['ones'], n[i])


b_dict_wo = {10: {'hil': [],
                  'rand': [],
                  'ones': []},
             20: {'hil': [],
             'rand': [],
                  'ones': []},
             30: {'hil': [],
             'rand': [],
                  'ones': []},
             40: {'hil': [],
             'rand': [],
                  'ones': []}
             }

for i in range(len(n)):
    b_dict_wo[n[i]]['hil'] = np.matmul(
        hilbert_mats[i], wo_pivot_x[n[i]]['hil'])
    b_dict_wo[n[i]]['rand'] = np.matmul(rand_mats[i], wo_pivot_x[n[i]]['rand'])
    b_dict_wo[n[i]]['ones'] = np.matmul(mats_1[i], wo_pivot_x[n[i]]['ones'])

xsolve = {10: {'hil': [],
               'rand': [],
               'ones': []},
          20: {'hil': [],
               'rand': [],
               'ones': []},
          30: {'hil': [],
               'rand': [],
               'ones': []},
          40: {'hil': [],
               'rand': [],
               'ones': []}
          }

for i in range(len(n)):
    xsolve[n[i]]['hil'] = np.linalg.solve(hilbert_mats[i], b_dict[n[i]]['hil'])
    xsolve[n[i]]['rand'] = np.linalg.solve(rand_mats[i], b_dict[n[i]]['rand'])
    xsolve[n[i]]['ones'] = np.linalg.solve(mats_1[i], b_dict[n[i]]['ones'])

bsolve = {10: {'hil': [],
               'rand': [],
               'ones': []},
          20: {'hil': [],
               'rand': [],
               'ones': []},
          30: {'hil': [],
               'rand': [],
               'ones': []},
          40: {'hil': [],
               'rand': [],
               'ones': []}
          }

for i in range(len(n)):
    bsolve[n[i]]['hil'] = np.matmul(hilbert_mats[i], xsolve[n[i]]['hil'])
    bsolve[n[i]]['rand'] = np.matmul(rand_mats[i], xsolve[n[i]]['rand'])
    bsolve[n[i]]['ones'] = np.matmul(mats_1[i], xsolve[n[i]]['ones'])


def geterror(xtrue, xcomp):
    error_mat = np.subtract(xtrue, xcomp)
    error = np.linalg.norm(error_mat)

    return error


def getresidual(btrue, bcomp):
    res_mat = np.subtract(btrue, bcomp)
    residual = np.linalg.norm(res_mat)

    return residual


for i in range(len(n)):
    ans[n[i]]['hil'][0] = np.linalg.cond(
        hilbert_mats[i])  # cond number of the matrix
    ans[n[i]]['rand'][0] = np.linalg.cond(rand_mats[i])
    ans[n[i]]['ones'][0] = np.linalg.cond(mats_1[i])

    true_x = ans[n[i]]['x']  # error from wo pivot
    ans[n[i]]['hil'][1] = geterror(true_x, wo_pivot_x[n[i]]['hil'])
    ans[n[i]]['rand'][1] = geterror(true_x, wo_pivot_x[n[i]]['rand'])
    ans[n[i]]['ones'][1] = geterror(true_x, wo_pivot_x[n[i]]['ones'])

    true_b = b_dict[n[i]]  # residual from wo pivot
    ans[n[i]]['hil'][2] = getresidual(true_b['hil'], b_dict_wo[n[i]]['hil'])
    ans[n[i]]['rand'][2] = getresidual(true_b['rand'], b_dict_wo[n[i]]['rand'])
    ans[n[i]]['ones'][2] = getresidual(true_b['ones'], b_dict_wo[n[i]]['ones'])

    ans[n[i]]['hil'][3] = geterror(
        true_x, xsolve[n[i]]['hil'])  # error from solve
    ans[n[i]]['rand'][3] = geterror(true_x, xsolve[n[i]]['rand'])
    ans[n[i]]['ones'][3] = geterror(true_x, xsolve[n[i]]['ones'])

    ans[n[i]]['hil'][4] = getresidual(
        true_b['hil'], bsolve[n[i]]['hil'])  # residual from solve
    ans[n[i]]['rand'][4] = getresidual(true_b['rand'], bsolve[n[i]]['rand'])
    ans[n[i]]['ones'][4] = getresidual(true_b['ones'], bsolve[n[i]]['ones'])

# for n=10
tab_10 = {'Values': ['Condition Number', 'Error', 'Residual', 'Error(from solve)', 'Residual(from solve)'],
          'Hilbert Matrix': [ans[10]['hil'][0], ans[10]['hil'][1], ans[10]['hil'][2], ans[10]['hil'][3], ans[10]['hil'][4]],
          'Random Matrix': [ans[10]['rand'][0], ans[10]['rand'][1], ans[10]['rand'][2], ans[10]['rand'][3], ans[10]['rand'][4]],
          'One\'s Matrix': [ans[10]['ones'][0], ans[10]['ones'][1], ans[10]['ones'][2], ans[10]['ones'][3], ans[10]['ones'][4]]
          }
# print(tab_10)
df_10 = pd.DataFrame(tab_10)
df_10.set_index('Values', inplace=True)
print('For n=10: ')
print()
print(df_10.head())
print()
print('---------------------------------------------------------------------------------')
print()

# for n=20
tab_20 = {'Values': ['Condition Number', 'Error', 'Residual', 'Error(from solve)', 'Residual(from solve)'],
          'Hilbert Matrix': [ans[20]['hil'][0], ans[20]['hil'][1], ans[20]['hil'][2], ans[20]['hil'][3], ans[20]['hil'][4]],
          'Random Matrix': [ans[20]['rand'][0], ans[20]['rand'][1], ans[20]['rand'][2], ans[20]['rand'][3], ans[20]['rand'][4]],
          'One\'s Matrix': [ans[20]['ones'][0], ans[20]['ones'][1], ans[20]['ones'][2], ans[20]['ones'][3], ans[20]['ones'][4]]
          }

df_20 = pd.DataFrame(tab_20)
df_20.set_index('Values', inplace=True)
print('For n=20: ')
print()
print(df_20.head())
print()
print('---------------------------------------------------------------------------------')
print()

# for n=30
tab_30 = {'Values': ['Condition Number', 'Error', 'Residual', 'Error(from solve)', 'Residual(from solve)'],
          'Hilbert Matrix': [ans[30]['hil'][0], ans[30]['hil'][1], ans[30]['hil'][2], ans[30]['hil'][3], ans[30]['hil'][4]],
          'Random Matrix': [ans[30]['rand'][0], ans[30]['rand'][1], ans[30]['rand'][2], ans[30]['rand'][3], ans[30]['rand'][4]],
          'One\'s Matrix': [ans[30]['ones'][0], ans[30]['ones'][1], ans[30]['ones'][2], ans[30]['ones'][3], ans[30]['ones'][4]]
          }

df_30 = pd.DataFrame(tab_30)
df_30.set_index('Values', inplace=True)
print('For n=30: ')
print()
print(df_30.head())
print()
print('---------------------------------------------------------------------------------')
print()

# for n=40
tab_40 = {'Values': ['Condition Number', 'Error', 'Residual', 'Error(from solve)', 'Residual(from solve)'],
          'Hilbert Matrix': [ans[40]['hil'][0], ans[40]['hil'][1], ans[40]['hil'][2], ans[40]['hil'][3], ans[40]['hil'][4]],
          'Random Matrix': [ans[40]['rand'][0], ans[40]['rand'][1], ans[40]['rand'][2], ans[40]['rand'][3], ans[40]['rand'][4]],
          'One\'s Matrix': [ans[40]['ones'][0], ans[40]['ones'][1], ans[40]['ones'][2], ans[40]['ones'][3], ans[40]['ones'][4]]
          }
# print(tab_10)
df_40 = pd.DataFrame(tab_40)
df_40.set_index('Values', inplace=True)
print('For n=40: ')
print()
print(df_40.head())
print()
