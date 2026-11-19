---
declaration: definition
origin: cited
lean: ReedSolomon.constrainedCode
statement: formalized
---

# Constrained Code

For a smooth domain $\mathcal{L}$ of size $2^n$, $m\in\mathbb{N}$, a weight polynomial $\hat{w}\in\mathbb{F}[Z,X_1,\ldots,X_m]$ and $\sigma\in\mathbb{F}$, the constrained code $\mathrm{CRS}[\mathbb{F},\mathcal{L},m,\hat{w},\sigma]$ consists of the codewords $f\in\mathrm{RS}[\mathbb{F},\mathcal{L},2^m]$ whose multilinear polynomial $\hat{f}$ satisfies $\sum_{b\in\{0,1\}^m}\hat{w}(\hat{f}(b),b)=\sigma$.

## Depends on

Its statement uses no other node of the blueprint.

## Lean

Formalized as [`ReedSolomon.constrainedCode`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/ReedSolomon.constrainedCode).

## Sources

- [ArkLib blueprint: coding_theory/defs.tex, line 77](https://github.com/Verified-zkEVM/ArkLib/blob/e1c185ba001d225d1f3ea84071d67a8c6c56d6a0/blueprint/src/coding_theory/defs.tex#L77)
