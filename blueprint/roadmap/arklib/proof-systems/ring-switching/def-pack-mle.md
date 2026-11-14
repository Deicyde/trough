---
declaration: definition
origin: cited
lean: RingSwitching.packMLE
statement: formalized
---

# Multilinear packing

With $\ell = \ell' + \kappa$, a small-field multilinear $t$ in $\ell$ variables is packed into a large-field multilinear $t'$ in $\ell'$ variables by bundling each block of $2^\kappa$ coefficients into one $L$-element:

$$
t'(w) \;=\; \sum_{v \in \{0,1\}^\kappa} t(v, w)\,\beta_v, \qquad w \in \{0,1\}^{\ell'}.
$$

## Depends on

- [Ring-switching profile](def-ring-switching-profile.md)

## Lean

Formalized as [`RingSwitching.packMLE`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/RingSwitching.packMLE).

## Sources

- [ArkLib blueprint: proof_systems/ring_switching.tex, line 105](https://github.com/Verified-zkEVM/ArkLib/blob/e1c185ba001d225d1f3ea84071d67a8c6c56d6a0/blueprint/src/proof_systems/ring_switching.tex#L105)
