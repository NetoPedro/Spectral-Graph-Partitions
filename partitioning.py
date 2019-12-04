import networkx as nx
import scipy.sparse as sparse
import time
start_time = time.time()


G=nx.read_edgelist("graphs_processed/Oregon-1.txt")

def find_laplacian(nodelist):

    if nodelist is None:
        nodelist = list(G)
    A = nx.to_scipy_sparse_matrix(G, nodelist=nodelist, weight=None)
    n, m = A.shape
    diags = A.sum(axis=1)
    D = sparse.spdiags(diags.flatten(), [0], m, n)
    return D - A

laplacian = find_laplacian(G.nodes)
laplacian = laplacian.asfptype()
eigval, eigvec = sparse.linalg.eigsh(laplacian, 2, sigma=0, which='LM')
print(eigval)
print("ok")
print("--- %s seconds ---" % (time.time() - start_time))