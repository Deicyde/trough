---
declaration: lemma
origin: cited
lean: ordConnected_C2
statement: formalized
proof: formalized
---

# C2 convex

For each $k,n,j$, the collection ${\mathfrak C}_2(k,n,j)$ is convex.

## Depends on

- [C1 convex](c1-convex.md)

## Proof

Let ${\mathfrak p} \le {\mathfrak p}' \le {\mathfrak p}''$ with ${\mathfrak p}, {\mathfrak p}'' \in {\mathfrak C}_2(k,n,j)$. By [(12)](../README.md), we have

$$
{\mathfrak C}_2(k,n,j) \subset {\mathfrak C}_1(k,n,j)\ .
$$

Combined with [C1 convex](c1-convex.md), it follows that ${\mathfrak p}' \in {\mathfrak C}_1(k,n,j)$. If ${\mathfrak p}={\mathfrak p}'$ the statement is trivially true, otherwise suppose that ${\mathfrak p}' \notin {\mathfrak C}_2(k,n,j)$. By [(12)](../README.md), this implies that there exists $0 \le l' \le Z(n+1)$ with ${\mathfrak p}' \in {\mathfrak L}_1(k,n,j,l')$. By the definition [(11)](../README.md) of ${\mathfrak L}_1(k,n,j,l')$, this implies that ${\mathfrak p}'$ is minimal with respect to $\le$ in ${\mathfrak C}_1(k,n,j) \setminus \bigcup_{l < l'} {\mathfrak L}_1(k,n,j,l)$. Since ${\mathfrak p}\le{\mathfrak p}'$ and ${\mathfrak p}\in{\mathfrak C}_2(k,n,j)$, ${\mathfrak p}={\mathfrak p}'$, a contradiction.

## Lean

Formalized as [`ordConnected_C2`](https://fpvandoorn.github.io/carleson/docs/find/#doc/ordConnected_C2).

## Sources

- [Carleson's theorem blueprint: chapter/main.tex, line 2778](https://github.com/fpvandoorn/carleson/blob/d4446d3cab5d096d936a94e998d24c413b2b017d/blueprint/src/chapter/main.tex#L2778)
