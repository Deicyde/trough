---
declaration: lemma
origin: cited
lean: Construction.iUnion_ball_subset_iUnion_Ω₁, Construction.ball_subset_Ω₁, Construction.Ω₁_subset_ball
statement: formalized
proof: formalized
---

# frequency cube cover

For each $I \in \mathcal{D}$, it holds that

$$
\bigcup_{z \in \mathcal{Z}(I)} B_{I^\circ}(z, 0.7)\subset \bigcup_{{\mathfrak p} \in {\mathfrak P}(I)} \Omega_1({\mathfrak p})\,.\qquad\text{(31)}
$$

For every ${\mathfrak p} \in {\mathfrak P}$, it holds that

$$
B_{{\mathfrak p}}({\mathcal{Q}}({\mathfrak p}), 0.3) \subset \Omega_1({\mathfrak p}) \subset B_{{\mathfrak p}}({\mathcal{Q}}({\mathfrak p}), 0.7)\,.\qquad\text{(32)}
$$

## Depends on

Its statement uses no other node of the blueprint.

## Proof

For (32) let ${\mathfrak p} = (I, z)$. The second inclusion in (32) then follows from [(30)](README.md) and the equality $B_{{\mathfrak p}}({\mathcal{Q}}({\mathfrak p}), 0.7) = B_{I^\circ}(z, 0.7)$, which is true by definition. For the first inclusion in (32) let ${\vartheta} \in B_{{\mathfrak p}}({\mathcal{Q}}({\mathfrak p}),0.3)$. Let $k$ be such that $z = z_k$ in the enumeration we chose above. It follows immediately from [(30)](README.md) and [(28)](README.md) that ${\vartheta} \notin \Omega_1((I, z_i))$ for all $i < k$. Thus, again from [(30)](README.md), we have ${\vartheta} \in \Omega_1((I,z_k))$.

To show (31) let ${\vartheta} \in \bigcup_{z \in \mathcal{Z}(I)} B_{I^\circ}(z,0.7)$. If there exists $z \in \mathcal{Z}(I)$ with ${\vartheta} \in B_{I^\circ}(z,0.3)$, then

$$
z \in \Omega_1((I, z)) \subset \bigcup_{{\mathfrak p} \in {\mathfrak P}(I)} \Omega_1({\mathfrak p})
$$

by the first inclusion in (32).

Now suppose that there exists no $z \in \mathcal{Z}(I)$ with ${\vartheta} \in B_{I^\circ}(z, 0.3)$. Let $k$ be minimal such that ${\vartheta} \in B_{I^\circ}(z_k, 0.7)$. Since $\Omega_1((I, z_i)) \subset B_{I^\circ}(z_i, 0.7)$ for each $i$ by [(30)](README.md), we have that ${\vartheta} \notin \Omega_1((I, z_i))$ for all $i < k$. Hence ${\vartheta} \in \Omega_1((I, z_k))$, again by [(30)](README.md).

## Lean

Formalized as [`Construction.iUnion_ball_subset_iUnion_Ω₁`](https://fpvandoorn.github.io/carleson/docs/find/#doc/Construction.iUnion_ball_subset_iUnion_Ω₁), [`Construction.ball_subset_Ω₁`](https://fpvandoorn.github.io/carleson/docs/find/#doc/Construction.ball_subset_Ω₁), [`Construction.Ω₁_subset_ball`](https://fpvandoorn.github.io/carleson/docs/find/#doc/Construction.Ω₁_subset_ball).

## Sources

- [Carleson's theorem blueprint: chapter/main.tex, line 1846](https://github.com/fpvandoorn/carleson/blob/d4446d3cab5d096d936a94e998d24c413b2b017d/blueprint/src/chapter/main.tex#L1846)
