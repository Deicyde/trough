---
declaration: lemma
origin: cited
lean: equivalenceOn_urel
statement: formalized
proof: formalized
---

# equivalence relation

For each $k,n,j$, the relation $\sim$ on ${\mathfrak U}_2(k,n,j)$ is an equivalence relation.

## Depends on

- [relation geometry](relation-geometry.md)

## Proof

Reflexivity holds by definition. For transitivity, suppose that

$$
{\mathfrak u}, {\mathfrak u}', {\mathfrak u}'' \in {\mathfrak U}_1(k,n,j)
$$

and ${\mathfrak u} \sim {\mathfrak u}'$, ${\mathfrak u}' \sim {\mathfrak u}''$. By [relation geometry](relation-geometry.md), it follows that ${\mathcal{I}}({\mathfrak u}) ={\mathcal{I}}({\mathfrak u}') = {\mathcal{I}}({\mathfrak u}'')$, that there exists

$$
{\vartheta} \in B_{{\mathfrak u}}({\mathcal{Q}}({\mathfrak u}), 100) \cap B_{{\mathfrak u}'}({\mathcal{Q}}({\mathfrak u}'), 100)
$$

and that there exists

$$
{\theta} \in B_{{\mathfrak u}'}({\mathcal{Q}}({\mathfrak u}'), 100) \cap B_{{\mathfrak u}''}({\mathcal{Q}}({\mathfrak u}''), 100)\, .
$$

If ${\mathfrak u} = {\mathfrak u}'$, then ${\mathfrak u} \sim {\mathfrak u}''$ holds by assumption. Else, there exists by the definition of $\sim$ some ${\mathfrak p} \in \mathfrak{T}_1({\mathfrak u})$ with $10{\mathfrak p}\lesssim {\mathfrak u}'$. Then we have $2{\mathfrak p} \lesssim {\mathfrak u}$ and ${\mathfrak p} \ne {\mathfrak u}$ by definition of $\mathfrak{T}_1({\mathfrak u})$, so $4 {\mathfrak p} \lesssim 500 {\mathfrak u}$ by [(41)](../part-01/wiggle-order-3.md). For $q \in B_{{\mathfrak u}''}({\mathcal{Q}}({\mathfrak u}''), 1)$ it follows by the triangle inequality that

$$
\begin{aligned}
d_{{\mathfrak u}}({\mathcal{Q}}({\mathfrak u}), q) &\le d_{{\mathfrak u}}({\mathcal{Q}}({\mathfrak u}), {\vartheta}) + d_{{\mathfrak u}}({\vartheta}, {\mathcal{Q}}({\mathfrak u}'))\\
&\quad+ d_{{\mathfrak u}}({\mathcal{Q}}({\mathfrak u}'), {\theta}) + d_{{\mathfrak u}}({\theta}, {\mathcal{Q}}({\mathfrak u}'')) +
d_{{\mathfrak u}}({\mathcal{Q}}({\mathfrak u}''), q)\,.
\end{aligned}
$$

Using [(16)](../../proof-of-metric-space-carleson-overview/README.md) and the fact that ${\mathcal{I}}({\mathfrak u}) = {\mathcal{I}}({\mathfrak u}') = {\mathcal{I}}({\mathfrak u}'')$ this equals

$$
\begin{aligned}
&\quad d_{{\mathfrak u}}({\mathcal{Q}}({\mathfrak u}), {\vartheta}) + d_{{\mathfrak u}'}({\vartheta}, {\mathcal{Q}}({\mathfrak u}'))\\
&\quad+ d_{{\mathfrak u}'}({\mathcal{Q}}({\mathfrak u}'), {\theta}) + d_{{\mathfrak u}''}({\theta}, {\mathcal{Q}}({\mathfrak u}'')) +
d_{{\mathfrak u}''}({\mathcal{Q}}({\mathfrak u}''), q)\\
&< 100 + 100 + 100 + 100 + 1 < 500\,.
\end{aligned}
$$

Since $4{\mathfrak p} \lesssim 500 {\mathfrak u}$, it follows that $d_{{\mathfrak p}}({\mathcal{Q}}({\mathfrak p}), q) < 4 < 10$. We have shown that $B_{{\mathfrak u}''}({\mathcal{Q}}({\mathfrak u}''), 1) \subset B_{{\mathfrak p}}({\mathcal{Q}}({\mathfrak p}), 10)$, combining this with ${\mathcal{I}}({\mathfrak u}'') = {\mathcal{I}}({\mathfrak u})$ gives ${\mathfrak u} \sim {\mathfrak u}''$.

For symmetry suppose that ${\mathfrak u} \sim {\mathfrak u}'$. By Lemma [relation geometry](relation-geometry.md), it follows that ${\mathcal{I}}({\mathfrak u}) = {\mathcal{I}}({\mathfrak u}')$ and that there exists ${\vartheta} \in B_{{\mathfrak u}}({\mathcal{Q}}({\mathfrak u}), 100) \cap B_{{\mathfrak u}'}({\mathcal{Q}}({\mathfrak u}'), 100)$. Again, for ${\mathfrak u} = {\mathfrak u}'$ symmetry is obvious, so suppose that ${\mathfrak u} \ne {\mathfrak u}'$. There exists ${\mathfrak p} \in \mathfrak{T}_1({\mathfrak u}')$, which then satisfies $2{\mathfrak p}\lesssim {\mathfrak u}'$ and ${\mathcal{I}}({\mathfrak p}) \neq {\mathcal{I}}({\mathfrak u}')$. By [wiggle order 1](../part-01/wiggle-order-1.md) and [(41)](../part-01/wiggle-order-3.md), it follows that

$$
10{\mathfrak p} \lesssim 4{\mathfrak p} \lesssim 500 {\mathfrak u}'\,.\qquad\text{(47)}
$$

If $q \in B_{{\mathfrak u}}({\mathcal{Q}}({\mathfrak u}),1)$ then we have from the triangle inequality and the fact that ${\mathcal{I}}({\mathfrak u}) = {\mathcal{I}}({\mathfrak u}')$:

$$
\begin{aligned}
d_{{\mathfrak u}'}({\mathcal{Q}}({\mathfrak u}'), q) &\le d_{{\mathfrak u}'}({\mathcal{Q}}({\mathfrak u}'), {\vartheta}) + d_{{\mathfrak u}'}({\vartheta}, {\mathcal{Q}}({\mathfrak u})) + d_{{\mathfrak u}'}({\mathcal{Q}}({\mathfrak u}), q)\\
&= d_{{\mathfrak u}'}({\mathcal{Q}}({\mathfrak u}'), {\vartheta}) + d_{{\mathfrak u}}({\vartheta}, {\mathcal{Q}}({\mathfrak u})) + d_{{\mathfrak u}}({\mathcal{Q}}({\mathfrak u}), q)\\
&< 100 + 100 + 1 < 500\,.
\end{aligned}
$$

Combining this with (47) and [(23)](../../proof-of-metric-space-carleson-overview/README.md), we get

$$
B_{{\mathfrak u}}({\mathcal{Q}}({\mathfrak u}), 1) \subset B_{{\mathfrak p}}({\mathcal{Q}}({\mathfrak p}), 10)\, .
$$

Since $2{\mathfrak p} \lesssim {\mathfrak u}'$, we have ${\mathcal{I}}({\mathfrak p}) \subset {\mathcal{I}}({\mathfrak u}') = {\mathcal{I}}({\mathfrak u})$. Thus, $10{\mathfrak p} \lesssim {\mathfrak u}$ which completes the proof of ${\mathfrak u}' \sim {\mathfrak u}$.

## Lean

Formalized as [`equivalenceOn_urel`](https://fpvandoorn.github.io/carleson/docs/find/#doc/equivalenceOn_urel).

## Sources

- [Carleson's theorem blueprint: chapter/main.tex, line 2979](https://github.com/fpvandoorn/carleson/blob/d4446d3cab5d096d936a94e998d24c413b2b017d/blueprint/src/chapter/main.tex#L2979)
