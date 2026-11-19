---
declaration: lemma
origin: cited
lean: antichain_L2
statement: formalized
proof: formalized
---

# L2 antichain

Each of the sets ${\mathfrak L}_2(k,n,j)$ is an antichain.

## Depends on

- [monotone cube metrics](../../proof-of-metric-space-carleson-overview/monotone-cube-metrics.md)

## Proof

Suppose that there are ${\mathfrak p}_0, {\mathfrak p}_1 \in {\mathfrak L}_2(k,n,j)$ with ${\mathfrak p}_0 \ne {\mathfrak p}_1$ and ${\mathfrak p}_0 \le {\mathfrak p}_1$. By [wiggle order 1](../part-01/wiggle-order-1.md) and [wiggle order 2](../part-01/wiggle-order-2.md), it follows that $2{\mathfrak p}_0 \lesssim 200{\mathfrak p}_1$. Since ${\mathfrak L}_2(k,n,j)$ is finite, there exists a maximal $l \ge 1$ such that there exists a chain $2{\mathfrak p}_0 \lesssim 200 {\mathfrak p}_1 \lesssim \dotsb \lesssim 200 {\mathfrak p}_l$ with all ${\mathfrak p}_i$ in ${\mathfrak C}_1(k,n,j)$ and ${\mathfrak p}_i \ne {\mathfrak p}_{i+1}$ for $i = 0, \dotsc, l-1$. If we have ${\mathfrak p}_l \in {\mathfrak U}_1(k,n,j)$, then it follows from $2{\mathfrak p}_0 \lesssim 200 {\mathfrak p}_l \lesssim {\mathfrak p}_l$ and [(14)](../README.md) that ${\mathfrak p}_0 \not\in {\mathfrak L}_2(k,n,j)$, a contradiction. Thus, by the definition [(13)](../README.md) of ${\mathfrak U}_1(k,n,j)$, there exists ${\mathfrak p}_{l+1} \in {\mathfrak C}_1(k,n,j)$ with ${\mathcal{I}}({\mathfrak p}_l) \subsetneq {\mathcal{I}}({\mathfrak p}_{l+1})$ and ${\vartheta} \in B_{{\mathfrak p}_l}({\mathcal{Q}}({\mathfrak p}_l), 100) \cap B_{{\mathfrak p}_{l+1}}({\mathcal{Q}}({\mathfrak p}_{l+1}), 100)$. Using the triangle inequality and [monotone cube metrics](../../proof-of-metric-space-carleson-overview/monotone-cube-metrics.md), one deduces that $200 {\mathfrak p}_l \lesssim 200{\mathfrak p}_{l+1}$. This contradicts maximality of $l$.

## Lean

Formalized as [`antichain_L2`](https://fpvandoorn.github.io/carleson/docs/find/#doc/antichain_L2).

## Sources

- [Carleson's theorem blueprint: chapter/main.tex, line 3338](https://github.com/fpvandoorn/carleson/blob/d4446d3cab5d096d936a94e998d24c413b2b017d/blueprint/src/chapter/main.tex#L3338)
