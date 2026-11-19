---
declaration: lemma
origin: cited
lean: ProximityGap.iteratedFoldWord_eq_evalOnPoints_powAlgHom
statement: formalized
---

# fold_fg

Let $f : \mathcal{L} \to \mathbb{F}$ be a function, $\vec{\alpha} \in \mathbb{F}^k$ folding randomness and let $g := \mathrm{Fold}(f, \vec{\alpha})$, where $1\le k \leq m\le n$. If $f \in \mathrm{RS}[\mathbb{F}, \mathcal{L}, 2^m]$, then $g \in \mathrm{RS}[\mathbb{F}, \mathcal{L}^{2^k}, 2^{m - k}]$, and further the multilinear extension of $g$ is given by $\hat{g}(X_k, \ldots, X_{m-1}) := \hat{f}(\vec{\alpha}, X_k, \ldots, X_{m-1})$ where $\hat{f}$ is the multilinear extension of $f$.

## Depends on

- [fold_k](def-fold-k.md)
- [Smooth Reed-Solomon Code](../../supporting-theories/coding-theory/def-smooth-rs-code.md)

## Lean

Stated as [`ProximityGap.iteratedFoldWord_eq_evalOnPoints_powAlgHom`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/ProximityGap.iteratedFoldWord_eq_evalOnPoints_powAlgHom); the blueprint marks no proof of it as formalized.

## Sources

- [ArkLib blueprint: proof_systems/whir.tex, line 245](https://github.com/Verified-zkEVM/ArkLib/blob/e1c185ba001d225d1f3ea84071d67a8c6c56d6a0/blueprint/src/proof_systems/whir.tex#L245)
