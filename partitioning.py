import networkx as nx
import scipy.sparse

first_line = ""
with open("graphs_processed/Oregon-1.txt") as f:
    first_line = f.readline().split()

k = first_line[4]
vertices = first_line[2]
G=nx.read_edgelist("graphs_processed/Oregon-1.txt")

def find_laplacian(nodelist):

    if nodelist is None:
        nodelist = list(G)
    A = nx.to_scipy_sparse_matrix(G, nodelist=nodelist, weight=None,
                                  format='csr')
    n, m = A.shape
    diags = A.sum(axis=1)
    D = scipy.sparse.spdiags(diags.flatten(), [0], m, n, format='csr')
    return D - A

laplacian = find_laplacian(G.nodes)
print("ok")