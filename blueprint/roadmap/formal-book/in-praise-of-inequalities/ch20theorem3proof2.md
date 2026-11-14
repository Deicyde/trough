---
declaration: theorem
origin: cited
lean: mantel_amgm
statement: formalized
proof: formalized
---

# ch20theorem3proof2

Suppose $G$ is a graph on $n$ vertices without triangles. Then $G$ has at most $\frac{n^2}{4}$ edges, and equality holds only when $n$ is even and $G$ is the complete bipartite graph $K_{n/2, n/2}$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof

The following proof of Theorem 3, using the inequality of the arithmetic and the geometric mean, is a folklore Book Proof. Let $\alpha$ be the size of a largest independent set $A$, and set $\beta = n - \alpha$. Since $G$ is triangle-free, the neighbors of a vertex $i$ form an independent set, and we infer $d_i \le \alpha$ for all $i$.

The set $B = V \setminus A$ of size $\beta$ meets every edge of $G$. Counting the edges of $G$ according to their endvertices in $B$, we obtain $|E| \le \sum_{i \in B} d_i$. The inequality of the arithmetic and geometric mean now yields

$$
|E| \le \sum_{i \in B} d_i \le \alpha\beta \le \left(\frac{\alpha + \beta}{2}\right)^2 = \frac{n^2}{4},
$$

and again the case of equality is easily dealt with.

## Lean

Formalized as [`mantel_amgm`](https://mo271.github.io/FormalBook/docs/find/#doc/mantel_amgm).

## Sources

- [Formal Book blueprint: chapter/chapter20.tex, line 270](https://github.com/mo271/FormalBook/blob/7df264a4d5e57f9036acdf85f7a2702b3ad82a06/blueprint/src/chapter/chapter20.tex#L270)
