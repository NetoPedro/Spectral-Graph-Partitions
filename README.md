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

K-Means is a popular clustering algorithm of the literature, being useful to cluster a set of elements into K partitions. It initializes with K centroids, and uses the mean distance, of the centroids to the points that are closer than to it than to other centroids, to adjust the centroid to a new position, thus being closer to final results. This happens for a few iterations \cite{macqueen1967}. It is also known that the initialization of the centroids is a matter of great importance to the final solution, hence the implementation given by the Sckit-Learn package repeats the process several times with different initializations for the centroids.  

### Final Algorithm

```
 G = Read Graph\;
 K = Read K from file\;
 A = G.adjency\;
 
 D = diag(G.degrees)\;
 
 Laplacian = D - A\;
 
 fiedler\_vec = find\_eigen(Laplacian).sort()[1]\;
 
 clusters = KMeans(clusters=k, data=fiedler\_vec)\;
 
 return clusters\;
 
```

The implementation in algorithm mentioned above is rather naive and does not scale to large graphs, due to the fact that it tries to calculate too many eigenvectors, sort them by the eigenvalue to finally only select the second smallest. One other aspect is that it uses dense matrixes, when the problem the Laplacian matrix is sparse, being mostly composed of 0 values.
