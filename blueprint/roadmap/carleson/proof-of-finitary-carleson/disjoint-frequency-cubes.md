---
declaration: lemma
origin: cited
lean: Construction.disjoint_frequency_cubes
statement: formalized
proof: formalized
---

# disjoint frequency cubes

For each $I \in \mathcal{D}$, and ${\mathfrak p}_1, {\mathfrak p}_2\in {\mathfrak P}(I)$, if

$$
\Omega_1({\mathfrak p}_1)\cap \Omega_1({\mathfrak p}_2)\neq \emptyset,
$$

then ${\mathfrak p}_1={\mathfrak p}_2$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof

By the definition of the map ${\mathcal{I}}$, we have

$$
{\mathfrak P}(I) = \{(I, z) \, : \, z \in \mathcal{Z}(I)\}\,.
$$

By [(30)](README.md), the set $\Omega_1((I, z_k))$ is disjoint from each $\Omega_1((I, z_i))$ with $i < k$. Thus the sets $\Omega_1({\mathfrak p})$, ${\mathfrak p} \in {\mathfrak P}(I)$ are pairwise disjoint.

## Lean

Formalized as [`Construction.disjoint_frequency_cubes`](https://fpvandoorn.github.io/carleson/docs/find/#doc/Construction.disjoint_frequency_cubes).

## Sources

- [Carleson's theorem blueprint: chapter/main.tex, line 1829](https://github.com/fpvandoorn/carleson/blob/d4446d3cab5d096d936a94e998d24c413b2b017d/blueprint/src/chapter/main.tex#L1829)
