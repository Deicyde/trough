---
declaration: definition
origin: cited
lean: RingSwitching.tensorProductProfile
statement: formalized
---

# Tensor-product profile

For commutative rings $B$ and $L$, with $L$ a $B$-algebra and a chosen rank-$2^\kappa$ $B$-basis, the profile takes $A := L \otimes_B L$, with $\varphi_0(\alpha) = \alpha \otimes 1$ and $\varphi_1(\alpha) = 1 \otimes \alpha$. The coordinate maps use this basis in the left and right $L$-module structures on $A$, giving columns and rows respectively. Thus $z = \sum_v z_v \otimes \beta_v = \sum_u \beta_u \otimes z_u$. Basis reconstruction gives the two reconstruction laws and the row inverse; the column inverse follows from the profile laws. Base compatibility follows by moving scalars across the tensor product. Binius uses this constructor with its binary-tower basis.

## Depends on

- [Ring-switching profile](def-ring-switching-profile.md)

## Lean

Formalized as [`RingSwitching.tensorProductProfile`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/RingSwitching.tensorProductProfile).

## Sources

- [ArkLib blueprint: proof_systems/ring_switching.tex, line 71](https://github.com/Verified-zkEVM/ArkLib/blob/e1c185ba001d225d1f3ea84071d67a8c6c56d6a0/blueprint/src/proof_systems/ring_switching.tex#L71)
