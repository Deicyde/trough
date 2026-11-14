---
declaration: lemma
origin: cited
lean: frequency_ball_cover
statement: formalized
proof: formalized
---

# frequency ball cover

For each $I \in \mathcal{D}$, we have

$$
{Q}(X) \subset \bigcup_{z \in \mathcal{Z}(I)} B_{I^\circ}(z, 0.7)\,.\qquad\text{(29)}
$$

## Depends on

Its statement uses no other node of the blueprint.

## Proof

Let ${\theta} \in \bigcup_{{\vartheta} \in {Q}(X)} B_{I^\circ}({\vartheta}, 1)$. By maximality of $\mathcal{Z}(I)$, there must be a point $z \in \mathcal{Z}(I)$ such that $B_{I^\circ}(z, 0.3) \cap B_{I^\circ}({\theta}, 0.3) \ne \emptyset$. Else, $\mathcal{Z}(I) \cup \{{\theta}\}$ would be a set of larger cardinality than $\mathcal{Z}(I)$ satisfying [(27)](README.md) and [(28)](README.md). Fix such $z$, and fix a point $z_1 \in B_{I^\circ}(z, 0.3) \cap B_{I^\circ}({\theta}, 0.3)$. By the triangle inequality, we deduce that

$$
d_{I^\circ}(z,{\theta}) \le d_{I^\circ}(z,z_1) + d_{I^\circ}({\theta}, z_1) < 0.3 + 0.3 = 0.6\,,
$$

and hence ${\theta} \in B_{I^\circ}(z, 0.7)$.

## Lean

Formalized as [`frequency_ball_cover`](https://fpvandoorn.github.io/carleson/docs/find/#doc/frequency_ball_cover).

## Sources

- [Carleson's theorem blueprint: chapter/main.tex, line 1789](https://github.com/fpvandoorn/carleson/blob/d4446d3cab5d096d936a94e998d24c413b2b017d/blueprint/src/chapter/main.tex#L1789)
