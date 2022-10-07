from io import StringIO
import csv

def task(csvString):
    f = StringIO(csvString)
    reader = csv.reader(f, delimiter=',')
    gr = []
    for row in reader:
        gr.append(row)
    for x in gr:
        for y in x:
            y = int(y)

    A_1 = []
    A_2 = []
    A_3 = []
    A_4 = []
    A_5 = []

    for x in gr:
        if x[0] not in A_1:
            A_1.append(str(x[0]))

    for x in gr:
        if x[1] not in A_2:
            A_2.append(str(x[1]))

    f = gr
    g = gr
    for i in range(len(f)):
        for j in range(len(g)):
            if i != j and f[i][1] == g[j][0] and f[i][0] not in A_3:
                A_3.append(str(f[i][0]))

    for i in range(len(f)):
        for j in range(len(g)):
            if i != j and f[i][0] == g[j][1] and f[i][1] not in A_4:
                A_4.append(str(f[i][1]))

    for i in range(len(f)):
        for j in range(len(g)):
            if i != j and f[i][0] == g[j][0] and f[i][1] not in A_5:
                A_5.append(str(f[i][1]))

    return [A_1, A_2, A_3, A_4, A_5]

def main():
    print(task("1,2\n1,3\n3,4\n3,5"))
if __name__ == "__main__":
    print(task("1,2\n1,3\n3,4\n3,5"))
