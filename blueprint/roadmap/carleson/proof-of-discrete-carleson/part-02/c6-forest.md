---
declaration: lemma
origin: cited
lean: C6_forest
statement: formalized
proof: formalized
---

# C6 forest

We have

$$
{\mathfrak C}_6(k,n,j)=\bigcup_{{\mathfrak u}\in {\mathfrak U}_3(k,n,j)}\mathfrak{T}_2({\mathfrak u})\, .
$$

## Depends on

- [equivalence relation](equivalence-relation.md)

## Proof

Let ${\mathfrak p} \in {\mathfrak C}_6(k,n,j)$. By [(17)](../README.md) and [(20)](../README.md), we have ${\mathfrak p} \in {\mathfrak C}_3(k,n,j)$. By [(14)](../README.md) and [(15)](../README.md), there exists ${\mathfrak u} \in {\mathfrak U}_1(k,n,j)$ with $2{\mathfrak p} \lesssim {\mathfrak u}$ and ${\mathcal{I}}({\mathfrak p}) \ne {\mathcal{I}}({\mathfrak u})$, that is, with ${\mathfrak p} \in \mathfrak{T}_1({\mathfrak u})$. Then $\mathfrak{T}_1({\mathfrak u})$ is clearly nonempty, so ${\mathfrak u} \in {\mathfrak U}_2(k,n,j)$. By the definition of ${\mathfrak U}_3(k,n,j)$, there exists ${\mathfrak u}' \in {\mathfrak U}_3(k,n,j)$ with ${\mathfrak u} \sim {\mathfrak u}'$. By [(48)](README.md), we have ${\mathfrak p} \in \mathfrak{T}_2({\mathfrak u}')$.

## Lean

Formalized as [`C6_forest`](https://fpvandoorn.github.io/carleson/docs/find/#doc/C6_forest).

## Sources

- [Carleson's theorem blueprint: chapter/main.tex, line 3046](https://github.com/fpvandoorn/carleson/blob/d4446d3cab5d096d936a94e998d24c413b2b017d/blueprint/src/chapter/main.tex#L3046)
