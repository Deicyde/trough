---
declaration: definition
origin: cited
lean: ProximityGap.proximityGap
statement: formalized
---

# Proximity Gap

A code $\mathcal{C}$ has a proximity gap at distance $d$ with bound $b$ if, for all words $u,v$ whose proximity measure exceeds $b$, the pair $(u,v)$ is within distance $d$ of the 2-fold interleaved code of $\mathcal{C}$.

## Depends on

- [Distance from a Code](def-distance-from-code.md)

## Lean

Formalized as [`ProximityGap.proximityGap`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/ProximityGap.proximityGap).

## Sources

- [ArkLib blueprint: coding_theory/defs.tex, line 106](https://github.com/Verified-zkEVM/ArkLib/blob/e1c185ba001d225d1f3ea84071d67a8c6c56d6a0/blueprint/src/coding_theory/defs.tex#L106)
