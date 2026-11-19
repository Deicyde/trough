---
declaration: definition
origin: cited
lean: Code.distFromCode
statement: formalized
---

# Distance from a Code

The distance $\Delta(u,\mathcal{C})$ of a word $u$ from a code $\mathcal{C}$ is the least Hamming distance between $u$ and a codeword, valued in $\mathbb{N}\cup\{\infty\}$ (it is $\infty$ when $\mathcal{C}$ is empty).

## Depends on

Its statement uses no other node of the blueprint.

## Lean

Formalized as [`Code.distFromCode`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/Code.distFromCode).

## Sources

- [ArkLib blueprint: coding_theory/defs.tex, line 13](https://github.com/Verified-zkEVM/ArkLib/blob/e1c185ba001d225d1f3ea84071d67a8c6c56d6a0/blueprint/src/coding_theory/defs.tex#L13)
