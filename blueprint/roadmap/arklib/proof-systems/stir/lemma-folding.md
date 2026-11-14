---
declaration: lemma
origin: cited
lean: ProximityGap.folding_preserves_distance
statement: formalized
---

# folding

Let $\mathcal{L}$ be a smooth coset FFT domain of size $2^n$, let $d=2^{d}$ and let the folding parameter be $2^{k}$ with $1\le k\le d\le n$. Let $\rho:=\frac{d}{|\mathcal{L}|}$. For every function $f:\mathcal{L}\rightarrow\mathbb{F}$ and distance parameter $\delta\in(0,\min\{\Delta(f,\mathrm{RS}[\mathbb{F},\mathcal{L},d]),1-{\mathsf{B}}^*(\rho)\})$,

$$
\Pr_{r^{\mathsf{fold}}\gets\mathbb{F}}[\Delta(\mathsf{Fold}(f,2^k,r^{\mathsf{fold}}),\mathrm{RS}[\mathbb{F},{\mathcal{L}}^{2^k}, d/2^k])\le\delta]\le\mathsf{err}^*(d/2^k,\rho,\delta,2^k).
$$

Above, ${\mathsf{B}}^*$ and ${\mathsf{err}}^*$ are the proximity bound and error (respectively) described in Section [Random linear combination as a proximity generator](README.md).

## Depends on

- [Reed-Solomon Code](../../supporting-theories/coding-theory/def-reed-solomon-code.md)
- [fn_folding](def-fn-folding.md)
- [Distance from a Code](../../supporting-theories/coding-theory/def-distance-from-code.md)

## Lean

Stated as [`ProximityGap.folding_preserves_distance`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/ProximityGap.folding_preserves_distance); the blueprint marks no proof of it as formalized.

## Sources

- [ArkLib blueprint: proof_systems/stir.tex, line 175](https://github.com/Verified-zkEVM/ArkLib/blob/e1c185ba001d225d1f3ea84071d67a8c6c56d6a0/blueprint/src/proof_systems/stir.tex#L175)
