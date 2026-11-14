---
declaration: lemma
origin: cited
lean: pairwiseDisjoint_E1
statement: formalized
proof: formalized
---

# pairwise disjoint

If ${\mathfrak p}, {\mathfrak p}' \in {\mathfrak{M}}(k,n)$ and

$$
{E_1}({\mathfrak p})\cap {E_1}({\mathfrak p}')\neq \emptyset,\qquad\text{(28)}
$$

then ${\mathfrak p}={\mathfrak p}'$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof

Let ${\mathfrak p},{\mathfrak p}'$ be as in the lemma. By definition of $E_1$, we have $E_1({\mathfrak p})\subset {\mathcal{I}}({\mathfrak p})$ and analogously for ${\mathfrak p}'$, we conclude from (28) that ${\mathcal{I}}({\mathfrak p})\cap {\mathcal{I}}({\mathfrak p}')\neq \emptyset$. Let without loss of generality ${\mathcal{I}}({\mathfrak p})$ be maximal in $\{{\mathcal{I}}({\mathfrak p}),{\mathcal{I}}({\mathfrak p}')\}$, then ${\mathcal{I}}({\mathfrak p}')\subset {\mathcal{I}}({\mathfrak p})$. By (28), we conclude by definition of $E_1$ that ${\Omega}({\mathfrak p})\cap {\Omega}({\mathfrak p}')\neq \emptyset$. By [(14)](../../proof-of-metric-space-carleson-overview/README.md) we conclude ${\Omega}({\mathfrak p})\subset {\Omega}({\mathfrak p}')$. It follows that ${\mathfrak p}'\le {\mathfrak p}$. By maximality [(5)](../README.md) of ${\mathfrak p}'$, we have ${\mathfrak p}'={\mathfrak p}$. This proves the lemma.

## Lean

Formalized as [`pairwiseDisjoint_E1`](https://fpvandoorn.github.io/carleson/docs/find/#doc/pairwiseDisjoint_E1).

## Sources

- [Carleson's theorem blueprint: chapter/main.tex, line 2271](https://github.com/fpvandoorn/carleson/blob/d4446d3cab5d096d936a94e998d24c413b2b017d/blueprint/src/chapter/main.tex#L2271)
