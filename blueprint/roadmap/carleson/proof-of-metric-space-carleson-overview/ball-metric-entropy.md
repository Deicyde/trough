---
declaration: lemma
origin: cited
lean: Θ.finite_and_mk_le_of_le_dist
statement: formalized
proof: formalized
---

# ball metric entropy

Let $B' \subset X$ be a ball. Let $r > 0$, ${\vartheta} \in {\Theta}$ and $k \in \mathbb{N}$. Suppose that $\mathcal{Z} \subset B_{B'}({\vartheta}, r2^k)$ satisfies that $\{B_{B'}(z,r)\mid z \in \mathcal{Z}\}$ is a collection of pairwise disjoint sets. Then

$$
|\mathcal{Z}| \le 2^{ka}\,.
$$

## Depends on

Its statement uses no other node of the blueprint.

## Proof

By applying property [(11)](../introduction/README.md) $k$ times, we obtain a collection $\mathcal{Z}' \subset {\Theta}$ with $|\mathcal{Z}'| = 2^{ka}$ and

$$
B_{B'}({\vartheta},r2^k) \subset \bigcup_{z' \in \mathcal{Z}'} B_{B'}(z', \frac{r}{2})\,.
$$

Then each $z \in \mathcal{Z}$ is contained in one of the balls $B(z', \frac{r}{2})$, but by the separation assumption no such ball contains more than one element of $\mathcal{Z}$. Thus $|\mathcal{Z}| \le |\mathcal{Z}'| = 2^{ka}$.

## Lean

Formalized as [`Θ.finite_and_mk_le_of_le_dist`](https://fpvandoorn.github.io/carleson/docs/find/#doc/Θ.finite_and_mk_le_of_le_dist).

## Sources

- [Carleson's theorem blueprint: chapter/main.tex, line 804](https://github.com/fpvandoorn/carleson/blob/d4446d3cab5d096d936a94e998d24c413b2b017d/blueprint/src/chapter/main.tex#L804)
