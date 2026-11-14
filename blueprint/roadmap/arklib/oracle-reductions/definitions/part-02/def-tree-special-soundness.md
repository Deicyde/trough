---
declaration: definition
origin: cited
lean: Verifier.treeSpecialSound, Verifier.specialSound, Verifier.coordinateWiseSpecialSound, Verifier.coordinateWiseSpecialSoundWith
statement: formalized
---

# Tree Special Soundness

A verifier is **tree special sound** for a shape $S$ and relations $R_{\text{in}}, R_{\text{out}}$ if there is a tree-based extractor such that, for every input statement and every challenge tree that satisfies $S$ and on which the verifier accepts every leaf, the extractor returns a valid input witness from every valid witnessing of the leaves. *$(k_i)$-special soundness* is the instance in which the $k_i$ sibling challenges at each round are pairwise distinct. *Coordinate-wise special soundness* ([Fenzi et al. 2024](https://doi.org/10.1007/s00145-024-09511-8)) is the instance with arity $\ell_i(k_i - 1) + 1$ and the coordinate-wise sibling condition.

## Depends on

- [Challenge Tree](def-challenge-tree.md)

## Lean

Formalized as [`Verifier.treeSpecialSound`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/Verifier.treeSpecialSound), [`Verifier.specialSound`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/Verifier.specialSound), [`Verifier.coordinateWiseSpecialSound`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/Verifier.coordinateWiseSpecialSound), [`Verifier.coordinateWiseSpecialSoundWith`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/Verifier.coordinateWiseSpecialSoundWith).

## Sources

- [ArkLib blueprint: oracle_reductions/defs.tex, line 745](https://github.com/Verified-zkEVM/ArkLib/blob/e1c185ba001d225d1f3ea84071d67a8c6c56d6a0/blueprint/src/oracle_reductions/defs.tex#L745)
