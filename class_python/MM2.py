list_mu = [3,6,7,3,9,3,70,45,43,56]
for i in range(len(list_mu)-1):
    for j in range(len(list_mu)-i-1):
        if list_mu[j]>list_mu[j+1]:list_mu[j],list_mu[j+1] = list_mu[j+1],list_mu[j]
print(list_mu)


def Mod(a,b):
    print("没有加return")
    sum = a+b
    return sum
mod = Mod(1,2)
print(mod)

