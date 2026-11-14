---
declaration: definition
origin: cited
lean: ProximityGap.foldWord
statement: formalized
---

# fn_folding

Let $f:\mathcal{L}\rightarrow\mathbb{F}$ be a function, $k\in\mathbb{N}$ a folding parameter and $\alpha\in\mathbb{F}$. For every $x\in{\mathcal{L}}^k$, let $\hat{p}_x\in\mathbb{F}^{\lt k}[X]$ be the polynomial where $\hat{p}_x(y)=f(y)$ for every $y\in{\mathcal{L}}$ such that $y^k=x$. We define $\mathsf{Fold}(f,k,\alpha):{\mathcal{L}}^k\rightarrow\mathbb{F}$ as follows.

$$
\mathsf{Fold}(f,k,\alpha)(x):=\hat{p}_x(\alpha).
$$

In order to compute $\mathsf{Fold}(f,k,\alpha)(x)$ it suffices to interpolate the $k$ values $\{f(y):y\in\mathcal{L}\text{ s.t. }y^k=x\}$ into the polynomial $\hat{p}_x$ and evaluate this polynomial at $\alpha$. The formalization takes $\mathcal{L}$ to be a smooth coset FFT domain of size $2^n$ and a folding parameter of the form $2^k$.

## Depends on

Its statement uses no other node of the blueprint.

## Lean

Formalized as [`ProximityGap.foldWord`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/ProximityGap.foldWord).

## Sources

- [ArkLib blueprint: proof_systems/stir.tex, line 161](https://github.com/Verified-zkEVM/ArkLib/blob/e1c185ba001d225d1f3ea84071d67a8c6c56d6a0/blueprint/src/proof_systems/stir.tex#L161)
