# The spectral theorem and Hadamard's determinant problem

We start with some preliminary facts. Let $O(n) \subseteq \mathbb{R}^{n \times n}$ be the set of real orthogonal matrices of order $n$. Since

$$
(PQ)^{-1} = Q^{-1} P^{-1} = Q^T P^T = (PQ)^T
$$

for $P, Q \in O(n)$, we see that the set $O(n)$ is a group. Regarding any matrix in $\mathbb{R}^{n \times n}$ as a vector in $\mathbb{R}^{n^2}$, we find that $O(n)$ is a compact set. Indeed, as the columns of an orthogonal matrix $Q = (q_{ij})$ are unit vectors, we have $|q_{ij}| \le 1$ for all $i$ and $j$, thus $O(n)$ is bounded. Furthermore, the set $O(n)$ is defined as a subset of $\mathbb{R}^{n^2}$ by the equations

$$
x_{i1} x_{j1} + x_{i2} x_{j2} + \dots + x_{in} x_{jn} = \delta_{ij} \quad \text{for } 1 \le i, j \le n,
$$

hence it is closed, and thus compact.

For any real square matrix $A$ let $\operatorname{Od}(A) = \sum_{i \ne j} a_{ij}^2$ be the sum of the squares of the off-diagonal entries.

- [diagonalize_real_symmetric](diagonalize-real-symmetric.md)
