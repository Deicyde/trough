---
declaration: lemma
origin: cited
lean: URel.eq, URel.not_disjoint
statement: formalized
proof: formalized
---

# relation geometry

If ${\mathfrak u} \sim {\mathfrak u}'$, then ${\mathcal{I}}(u) = {\mathcal{I}}(u')$ and

$$
B_{{\mathfrak u}}({\mathcal{Q}}({\mathfrak u}), 100) \cap B_{{\mathfrak u}'}({\mathcal{Q}}({\mathfrak u}'), 100) \neq \emptyset\ .
$$

## Depends on

- [wiggle order 3](../part-01/wiggle-order-3.md)

## Proof

Let ${\mathfrak u}, {\mathfrak u}' \in {\mathfrak U}_2(k,n,j)$ with ${\mathfrak u} \sim {\mathfrak u}'$. If ${\mathfrak u} = {\mathfrak u}'$ then the conclusion of the Lemma clearly holds. Else, there exists ${\mathfrak p} \in {\mathfrak C}_1(k,n,j)$ such that ${\mathcal{I}}({\mathfrak p}) \ne {\mathcal{I}}({\mathfrak u})$ and $2 {\mathfrak p} \lesssim {\mathfrak u}$ and $10 {\mathfrak p} \lesssim {\mathfrak u}'$. Using [wiggle order 1](../part-01/wiggle-order-1.md) and [(40)](../part-01/wiggle-order-3.md) of [wiggle order 3](../part-01/wiggle-order-3.md), we deduce that

$$
100 {\mathfrak p}\lesssim 100 {\mathfrak u}\,, \qquad 100 {\mathfrak p} \lesssim 100{\mathfrak u}'\,.\qquad\text{(46)}
$$

Now suppose that $B_{{\mathfrak u}}({\mathcal{Q}}({\mathfrak u}), 100) \cap B_{{\mathfrak u}'}({\mathcal{Q}}({\mathfrak u}'), 100) = \emptyset$. Then we have $\mathfrak{B}({\mathfrak u}) \cap \mathfrak{B}({\mathfrak u}') = \emptyset$, by the definition [(8)](../README.md) of $\mathfrak{B}$ and the definition [(23)](../../proof-of-metric-space-carleson-overview/README.md) of $\lesssim$, but also $\mathfrak{B}({\mathfrak u}) \subset \mathfrak{B}({\mathfrak p})$ and $\mathfrak{B}({\mathfrak u}') \subset \mathfrak{B}({\mathfrak p})$, by [(8)](../README.md), [(23)](../../proof-of-metric-space-carleson-overview/README.md) and (46). Hence,

$$
|\mathfrak{B}({\mathfrak p})| \geq |\mathfrak{B}({\mathfrak u})| + |\mathfrak{B}({\mathfrak u}')| \geq 2^{j} + 2^j = 2^{j+1}\,,
$$

which contradicts ${\mathfrak p} \in {\mathfrak C}_1(k,n,j)$. Therefore we must have

$$
B_{{\mathfrak u}}({\mathcal{Q}}({\mathfrak u}), 100) \cap B_{{\mathfrak u}'}({\mathcal{Q}}({\mathfrak u}'), 100) \ne \emptyset\, .
$$

It follows from $2{\mathfrak p} \lesssim {\mathfrak u}$ and $10{\mathfrak p} \lesssim {\mathfrak u}'$ that ${\mathcal{I}}({\mathfrak p}) \subset {\mathcal{I}}({\mathfrak u})$ and ${\mathcal{I}}({\mathfrak p}) \subset {\mathcal{I}}({\mathfrak u}')$. By [(8)](../../proof-of-metric-space-carleson-overview/README.md), it follows that ${\mathcal{I}}({\mathfrak u})$ and ${\mathcal{I}}({\mathfrak u}')$ are nested. Combining this with the conclusion of the last paragraph and definition [(13)](../README.md) of ${\mathfrak U}_1(k,n,j)$, we obtain that ${\mathcal{I}}({\mathfrak u}) = {\mathcal{I}}({\mathfrak u}')$.

## Lean

Formalized as [`URel.eq`](https://fpvandoorn.github.io/carleson/docs/find/#doc/URel.eq), [`URel.not_disjoint`](https://fpvandoorn.github.io/carleson/docs/find/#doc/URel.not_disjoint).

## Sources

- [Carleson's theorem blueprint: chapter/main.tex, line 2945](https://github.com/fpvandoorn/carleson/blob/d4446d3cab5d096d936a94e998d24c413b2b017d/blueprint/src/chapter/main.tex#L2945)
