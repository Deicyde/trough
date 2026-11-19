---
declaration: lemma
origin: cited
lean: ordConnected_tilesAt
statement: formalized
proof: formalized
---

# P convex

For each $k$, the collection ${\mathfrak P}(k)$ is convex.

## Depends on

Its statement uses no other node of the blueprint.

## Proof

Suppose that ${\mathfrak p} \le {\mathfrak p}' \le {\mathfrak p}''$ and ${\mathfrak p}, {\mathfrak p}'' \in {\mathfrak P}(k)$. By [(3)](../README.md) we have ${\mathcal{I}}({\mathfrak p}), {\mathcal{I}}({\mathfrak p}'') \in \mathcal{C}(G,k)$, so there exists by [(1)](../README.md) some $J \in \mathcal{D}$ with

$$
{\mathcal{I}}({\mathfrak p}') \subset {\mathcal{I}}({\mathfrak p}'') \subset J
$$

and $\mu(G \cap J) > 2^{-k-1} \mu(J)$. Thus [(1)](../README.md) holds for ${\mathcal{I}}({\mathfrak p}')$. On the other hand, by [(2)](../README.md), there exists no $J \in \mathcal{D}$ with ${\mathcal{I}}({\mathfrak p}) \subset J$ and $\mu(G \cap J) > 2^{-k} \mu(J)$. Since ${\mathcal{I}}({\mathfrak p}) \subset {\mathcal{I}}({\mathfrak p}')$, this implies that [(2)](../README.md) holds for ${\mathcal{I}}({\mathfrak p}')$. Hence ${\mathcal{I}}({\mathfrak p}') \in \mathcal{C}(G,k)$, and therefore by [(3)](../README.md) ${\mathfrak p}' \in {\mathfrak P}(k)$.

## Lean

Formalized as [`ordConnected_tilesAt`](https://fpvandoorn.github.io/carleson/docs/find/#doc/ordConnected_tilesAt).

## Sources

- [Carleson's theorem blueprint: chapter/main.tex, line 2723](https://github.com/fpvandoorn/carleson/blob/d4446d3cab5d096d936a94e998d24c413b2b017d/blueprint/src/chapter/main.tex#L2723)
