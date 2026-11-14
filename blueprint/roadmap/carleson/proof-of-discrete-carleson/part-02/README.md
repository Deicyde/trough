---
navigation: transparent
---

# C3 convex to L1 L3 antichain

- [C3 convex](c3-convex.md)
- [C4 convex](c4-convex.md)
- [C5 convex](c5-convex.md)
- [dens compare](dens-compare.md)
- [C dens1](c-dens1.md)

## Proof of the Forest Union Lemma

Fix $k,n,j\ge 0$. Define

$$
{\mathfrak C}_6(k,n,j)
$$

to be the set of all tiles ${\mathfrak p} \in {\mathfrak C}_5(k,n,j)$ such that ${\mathcal{I}}({\mathfrak p}) \not\subset G'$. The following chain of lemmas establishes that the set ${\mathfrak C}_6(k,n,j)$ can be written as a union of a small number of $n$-forests.

For ${\mathfrak u}\in {\mathfrak U}_1(k,n,j)$, define

$$
\mathfrak{T}_1({\mathfrak u}):= \{{\mathfrak p} \in {\mathfrak C}_1(k,n,j) \ : {\mathcal{I}}({\mathfrak p})\neq {\mathcal{I}}({\mathfrak u}), \ 2{\mathfrak p} \lesssim {\mathfrak u}\}\,.\qquad\text{(44)}
$$

Define

$$
{\mathfrak U}_2(k,n,j) := \{ {\mathfrak u} \in {\mathfrak U}_1(k,n,j) \, : \, \mathfrak{T}_1({\mathfrak u}) \cap {\mathfrak C}_6(k,n,j) \ne \emptyset\}\,.\qquad\text{(45)}
$$

Define a relation $\sim$ on ${\mathfrak U}_2(k,n,j)$ by setting ${\mathfrak u}\sim {\mathfrak u}'$ for ${\mathfrak u},{\mathfrak u}'\in {\mathfrak U}_2(k,n,j)$ if ${\mathfrak u}={\mathfrak u}'$ or there exists ${\mathfrak p}$ in $\mathfrak{T}_1({\mathfrak u})$ with $10 {\mathfrak p}\lesssim {\mathfrak u}'$.

- [relation geometry](relation-geometry.md)
- [equivalence relation](equivalence-relation.md)

Choose a set ${\mathfrak U}_3(k,n,j)$ of representatives for the equivalence classes of $\sim$ in ${\mathfrak U}_2(k,n,j)$. Define for each ${\mathfrak u}\in {\mathfrak U}_3(k,n,j)$

$$
{\mathfrak T}_2({\mathfrak u}):=
\bigcup_{{\mathfrak u}\sim {\mathfrak u}'}\mathfrak{T}_1({\mathfrak u}')\cap {\mathfrak C}_6(k,n,j)\, .\qquad\text{(48)}
$$

- [C6 forest](c6-forest.md)
- [forest geometry](forest-geometry.md)
- [forest convex](forest-convex.md)
- [forest separation](forest-separation.md)
- [forest inner](forest-inner.md)
- [forest stacking](forest-stacking.md)

We now turn to the proof of [forest union](../part-01/forest-union.md).

*Proof of forest union: shown with [forest union](../part-01/forest-union.md).*

## Proof of the Forest Complement Lemma

Define ${\mathfrak P}_{G \setminus G'}$ to be the set of all ${\mathfrak p} \in {\mathfrak P}$ such that $\mu({\mathcal{I}}({\mathfrak p}) \cap (G \setminus G')) > 0$.

- [antichain decomposition](antichain-decomposition.md)
- [L0 antichain](l0-antichain.md)
- [L2 antichain](l2-antichain.md)
- [L1 L3 antichain](l1-l3-antichain.md)

We now turn to the proof of [forest complement](../part-01/forest-complement.md).

*Proof of forest complement: shown with [forest complement](../part-01/forest-complement.md).*
