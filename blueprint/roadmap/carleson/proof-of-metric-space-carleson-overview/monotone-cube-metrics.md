---
declaration: lemma
origin: cited
lean: Grid.dist_mono, Grid.dist_strictMono
statement: formalized
proof: formalized
---

# monotone cube metrics

Let $(\mathcal{D}, c, s)$ be a grid structure. Denote for cubes $I \in \mathcal{D}$

$$
I^\circ := B(c(I), \frac{1}{4} D^{s(I)})\,.
$$

Let $I, J \in \mathcal{D}$ with $I \subset J$. Then for all ${\vartheta}, {\theta} \in{\Theta}$ we have

$$
d_{I^\circ}({\vartheta}, {\theta}) \le d_{J^\circ}({\vartheta}, {\theta})\,,
$$

and if $I \ne J$ then we have

$$
d_{I^\circ}({\vartheta}, {\theta}) \le 2^{-95a} d_{J^\circ}({\vartheta}, {\theta})\,.
$$

## Depends on

Its statement uses no other node of the blueprint.

## Proof

If $s(I) \ge s(J)$ then [(8)](README.md) and the assumption $I\subset J$ imply $I = J$. Then the lemma holds by reflexivity.

If $s(J) \ge s(I)+1$, then using the monotonicity property [(9)](../introduction/README.md), [(1)](README.md) and [(10)](../introduction/README.md), we get

$$
d_{I^\circ}({\vartheta}, {\theta}) \le d_{B(c(I), 4 D^{s(I)})}({\vartheta}, {\theta}) \le 2^{-100a} d_{B(c(I), 4D^{s(J)})}({\vartheta}, {\theta})\,.\qquad\text{(64)}
$$

Using [(10)](README.md), together with the inclusion $I \subset J$, we obtain

$$
c(I) \in I \subset J \subset B(c(J), 4 D^{s(J)})
$$

and consequently by the triangle inequality

$$
B(c(I), 4 D^{s(J)}) \subset B(c(J), 8 D^{s(J)})\,.
$$

Using this together with the monotonicity property [(9)](../introduction/README.md) and [(8)](../introduction/README.md) in (64), we obtain

$$
\begin{aligned}
d_{I^\circ}({\vartheta}, {\theta}) &\le 2^{-100a} d_{B(c(J), 8D^{s(J)})}({\vartheta}, {\theta})\\
&\le 2^{-100a + 5a} d_{B(c(J), \frac{1}{4}D^{s(J)})}({\vartheta}, {\theta})\\
&= 2^{-95a}d_{J^\circ}({\vartheta}, {\theta})\,.
\end{aligned}
$$

This proves the second inequality claimed in the Lemma, from which the first follows since $a \ge 4$ and hence $2^{-95a} \le 1$.

## Lean

Formalized as [`Grid.dist_mono`](https://fpvandoorn.github.io/carleson/docs/find/#doc/Grid.dist_mono), [`Grid.dist_strictMono`](https://fpvandoorn.github.io/carleson/docs/find/#doc/Grid.dist_strictMono).

## Sources

- [Carleson's theorem blueprint: chapter/main.tex, line 825](https://github.com/fpvandoorn/carleson/blob/d4446d3cab5d096d936a94e998d24c413b2b017d/blueprint/src/chapter/main.tex#L825)
