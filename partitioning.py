import networkx as nx
import scipy.sparse as sparse
import time
import sklearn.cluster as cluster
import numpy as np
import networkx.algorithms as algo
import networkx.linalg.algebraicconnectivity as  algebraicconnectivity
start_time = time.time()


FILENAME = "soc-Epinions1.txt"
first_line = []
with open("graphs_processed/" + FILENAME) as f:
    first_line = f.readline()

line = first_line
first_line = line.split()
k = first_line[4]





start_time = time.time()

G=nx.read_edgelist("graphs_processed/"+FILENAME)

vec = algebraicconnectivity.fiedler_vector(G,method="tracemin_lu")
vec = np.asarray(vec).reshape(-1,1)
clusters = cluster.KMeans(int(k)).fit_predict(vec)


cost = 0
nodes = np.asarray(list(G.nodes._nodes.keys()))


for i in range(int(k)):
    size = sum(clusters == i)
    print(size)
    cost +=  algo.cut_size(G,nodes[clusters == i])/size

print("Cost: ", cost)
print("--- %s seconds ---" % (time.time() - start_time))

f= open("results/"+FILENAME,"w+")


sort_ix = np.argsort(nodes.astype(int))

nodes = nodes[sort_ix]

clusters = clusters[sort_ix]
f.write(line)
i = 0
for node in nodes :
    f.write(str(node) + " " +  str(clusters[i]) + "\n")
    i = i+1
f.close()
