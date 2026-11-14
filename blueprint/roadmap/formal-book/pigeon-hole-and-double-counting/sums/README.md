# Sums

- [Claim](ch28claim4.md)

Let us turn to the second principle: counting in two ways. By this we mean the following.

- [Double counting](double-counting.md)

There is a useful way to picture the set $S$. Consider the matrix $A = (a_{pq})$, the incidence matrix of $S$, where the rows and columns of $A$ are indexed by the elements of $R$ and $C$, respectively, with

$$
a_{pq} = \begin{cases} 1 & \text{if } (p, q) \in S, \\ 0 & \text{if } (p, q) \notin S. \end{cases}
$$

With this set-up, $r_p$ is the sum of the $p$-th row of $A$ and $c_q$ is the sum of the $q$-th column. Hence the first sum in (3) adds the entries of $A$ (that is, counts the elements in $S$) by rows, and the second sum by columns.
