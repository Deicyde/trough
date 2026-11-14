# Graphs

Let $G$ be a finite simple graph with vertex set $V$ and edge set $E$. The degree $d(v)$ of a vertex $v$ is the number of edges which have $v$ as an end-vertex.

Almost every book in graph theory starts with the following result:

- [Handshaking](handshaking.md)

We want to single out the following beautiful application to an extremal problem on graphs. Here is the problem:

> Suppose $G = (V, E)$ has $n$ vertices and contains no cycle of length $4$ (denoted by $C_4$). How many edges can $G$ have at most?

Let us tackle the general problem. Let $G$ be a graph on $n$ vertices without a $4$-cycle. We count the following set $S$ in two ways: $S$ is the set of pairs $(u, \{v, w\})$ where $u$ is adjacent to $v$ and to $w$, with $v \neq w$. In other words, we count all occurrences of a “cherry” (path of length $2$ centered at $u$).

Summing over $u$, we find $|S| = \sum_{u \in V} \binom{d(u)}{2}$. On the other hand, every pair $\{v, w\}$ has at most one common neighbor (by the $C_4$-condition). Hence $|S| \leq \binom{n}{2}$, and we conclude

$$
\sum_{u \in V} \binom{d(u)}{2} \leq \binom{n}{2}
$$

or

$$
\sum_{u \in V} d(u)^2 \leq n(n-1) + \sum_{u \in V} d(u).
$$

Next we apply the Cauchy–Schwarz inequality to the vectors $(d(u_1), \dots, d(u_n))$ and $(1, 1, \dots, 1)$, obtaining

$$
\left(\sum_{u \in V} d(u)\right)^2 \leq n \sum_{u \in V} d(u)^2,
$$

and hence by (5)

$$
\left(\sum_{u \in V} d(u)\right)^2 \leq n^2(n-1) + n \sum_{u \in V} d(u).
$$

Invoking (4) we find

$$
4|E|^2 \leq n^2(n-1) + 2n|E|
$$

or

$$
|E|^2 - \frac{n}{2}|E| - \frac{n^2(n-1)}{4} \leq 0.
$$

Solving the corresponding quadratic equation we thus obtain the following result of István Reiman.

- [Reiman](ch28theorem.md)
- [Cherry counting](ch28-sum-choose.md)
