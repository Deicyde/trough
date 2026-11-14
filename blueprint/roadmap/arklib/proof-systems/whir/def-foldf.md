---
declaration: definition
origin: cited
lean: ProximityGap.foldWord, ProximityGap.foldWord_k_1
statement: formalized
---

# foldf

Let $f : \mathcal{L}^{2^k} \to \mathbb{F}$ be a function, and $\alpha \in \mathbb{F}$. We define $\mathrm{Fold_f}(f, {\alpha}) : \mathcal{L}^{2^{k+1}} \to \mathbb{F}$ as follows: for $y \in \mathcal{L}^{2^{k+1}}$ and $x := \mathsf{extract}(y)$,

$$
\mathrm{Fold_f}(f, \alpha)(y) := \frac{f(x) + f(-x)}{2} + \alpha \cdot \frac{f(x) - f(-x)}{2 \cdot x}.
$$

In order to compute $\mathrm{Fold_f}(f, \alpha)(y)$ it suffices to query $f$ at $x$ and $-x$, by retrieving $x=\mathsf{extract}(y)$. The formalization defines folding by interpolation on each block of $2^k$-th roots and proves that its $k=1$ case is the displayed formula.

## Depends on

- [extract](def-extract.md)

## Lean

Formalized as [`ProximityGap.foldWord`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/ProximityGap.foldWord), [`ProximityGap.foldWord_k_1`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/ProximityGap.foldWord_k_1).

## Sources

- [ArkLib blueprint: proof_systems/whir.tex, line 218](https://github.com/Verified-zkEVM/ArkLib/blob/e1c185ba001d225d1f3ea84071d67a8c6c56d6a0/blueprint/src/proof_systems/whir.tex#L218)
