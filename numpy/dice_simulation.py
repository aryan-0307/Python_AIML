import numpy as np

x = np.random.randint(1,7,1000)

values,counts = np.unique(x, return_counts=True)

probabilities = counts / len(x)
    
print("Probability Distribution:\n")

for v,p in zip(values,probabilities):
    print(f"{v} ---> {p:3f}")

