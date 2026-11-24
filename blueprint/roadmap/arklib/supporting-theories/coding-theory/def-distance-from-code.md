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

- [ArkLib blueprint: coding_theory/defs.tex, line 13](https://github.com/Verified-zkEVM/ArkLib/blob/e9bcc82d3d33a1814822b9b9e6b135bc80d614ee/blueprint/src/coding_theory/defs.tex#L13)
