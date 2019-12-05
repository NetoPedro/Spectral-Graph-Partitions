# Spectral-Graph-Partitons

Final project for the CS-E4600 - Algorithmic Methods of Data Mining course at Aalto University, Finland.

## How to reproduce
Edit the file partition.py and set FILENAME to the desired file.

```
git clone https://github.com/NetoPedro/Spectral-Graph-Partitons.git
cd Spectral-Graph-Partitons
python3 partition.py
```

## Overview 

This project aims to develop a solution for the graph partitioning problem, based on spectral graph analysis and K means. 

The problem required the minimization of the ration cut function. To achieve this, the Fiedler vector of the Laplacian was combined with an implementation of the K-Means algorithm to cluster the values of this eigenvector, the one with the second smallest eigenvalue, into K clusters. 

### Spectral Graph Analysis

Spectral graph analysis is a subfield of data mining and graph mining that focus on working with the eigenvalues and eigenvectors of the Laplacian matrix of a graph. It explores these spectral components and tries to identify relations with other properties of the graph structure, as well as cuts and bipartiteness. Some of the eigenvectors, like for example, the second smallest hold some interesting properties that make them really useful for tasks like graph partition. 

### Laplacian

The Laplacian matrix can be seen as a matrix representation of the graph. This matrix is constructed from the adjency and the degree matrix. They have V columns and V rows, being V the number of vertices. On the adjency matrix each pair i,j (i is the number of the row and j the number of the column), if there is a connection from the vertice i to the vertice j, then the entry is filled with 1, otherwise 0. The degree matrix has the diagonal filled with the degree of each vertice. The subtraction of the adjency matrix from the degree one gives the Laplacian.

Some property of these Laplacian matrices are: if a given graph is undirected then the Laplacian is symmetric; if we sum any row it always gives 0, and the same holds for columns. This is also a central element of the spectral graph analysis theory. 

### Fiedler Vector

The Fiedler Vector is another name given to the second smallest eigenvector computed from the Laplacian matrix of a given graph. It does hold some useful properties for the spectral graph partitioning problem, especially when working with just one connected component. This vector approximates the min-cut, thus having significant value for clustering. 

### K-Means

K-Means is a popular clustering algorithm of the literature, being useful to cluster a set of elements into K partitions. It initializes with K centroids, and uses the mean distance, of the centroids to the points that are closer than to it than to other centroids, to adjust the centroid to a new position, thus being closer to final results. This happens for a few iterations. It is also known that the initialization of the centroids is a matter of great importance to the final solution, hence the implementation given by the Sckit-Learn package repeats the process several times with different initializations for the centroids.  

### Final Algorithm

```
 G = Read Graph
 K = Read K from file
 A = G.adjency
 
 D = diag(G.degrees)
 
 Laplacian = D - A
 
 fiedler_vec = find_eigen(Laplacian).sort()[1]
 
 clusters = KMeans(clusters=k, data=fiedler_vec)
 
 return clusters
 
```

The implementation in algorithm mentioned above is rather naive and does not scale to large graphs, due to the fact that it tries to calculate too many eigenvectors, sort them by the eigenvalue to finally only select the second smallest. One other aspect is that it uses dense matrixes, when the problem the Laplacian matrix is sparse, being mostly composed of 0 values.


## Experiments 

This section regards experiments and also the final results of these experiments. 

### Scipy vs Scipy.sparse

The first step to improve the algorithm is to improve the matrix representation of the graph. Therefore, the initial implementation using regular SciPy was discarded in favor of SciPy.sparse, where these sparse matrix can be represented and managed with special functions optimized to handle huge matrices mostly filled with 0. The methods present in both are very similar so the change was rather fast.

Secondly, it was not necessary to compute a large number of eigenvectors and values, since this package allows us to select how many we want to compute and if we want the smallest ones or the biggest ones. Therefore the first 2 smallest eigenvectors are now the only two computed. This further improved the performance enabling the algorithm to better scale. 

### Scipy.sparse vs Networkx

After some time, I have found a method in the Networkx package, the one used to handle the graph operations and to store the graph, that computed the Fiedler vector without me having to previously compute the Laplacian in my code. After some comparison of both solutions on the smaller graphs, and trying the different methods offered to compute the eigenvectors, I concluded that the networkx implementation with LU factorization to solve the eigenvector problem was the fastest and the computation time difference greatly increased on larger graphs. Hence it was the option to the final version of this solution.

### Results


| Graph Name        | Vertices           | Edges  | K        | Ratio-Cut          |Ratio V-E  |
|:------------- |:-------------| :-----|:------------- |:-------------|:-----|
| ca-GrQc      | 4 158 | 13 428 |2| 0.083| 3.23 |
|  Oregon-1      | 10 670      |   22 002 |5| 1.034| 2.062 |
| soc-Epinions1 | 75 877      |   405 739 |10| 31.200 | 5.347 |
| web-NotreDame  | 325 729     |   1 117 563 |20 | 0.609 | 3.43 |
| roadNet-CA |  1 957 027    |    2 760 388|50 | 0.850 | 1.41 |

The table shows the score obtained on the different graphs with the final solution. Not only that, but it also shows the ratio between vertices and edges. This ratio I believe is the reason why my solution achieves a poor score on the "soc-Epinions1" graph, because each vertex has much more edges connecting to other vertices, hence increasing the difficulty of the problem. To solve this aspect, a better solution that takes in consideration the balance in the size of each cluster should be implemented. Nevertheless the remaining 4 graphs have shown some decent results, although not competing with the ones of the solutions submitted into the competition. 

