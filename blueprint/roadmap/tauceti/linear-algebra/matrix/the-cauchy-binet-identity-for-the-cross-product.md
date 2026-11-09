---
declaration: theorem
origin: cited
lean: Matrix.mulVec_cross_mulVec
statement: formalized
proof: formalized
---

# The Cauchy--Binet identity for the cross product

A matrix `M` sends the cross product of
`u` and `w` to the cross product of their images up to the transposed adjugate of `M`:
`(M u) ⨯₃ (M w) = (adj M)ᵀ (u ⨯₃ w)`.

```lean
Matrix.mulVec_cross_mulVec.{u_1} {R : Type u_1} [CommRing R] (M : Matrix (Fin 3) (Fin 3) R)
  (u w : Fin 3 → R) :
  (crossProduct (M.mulVec u)) (M.mulVec w) = M.adjugate.transpose.mulVec ((crossProduct u) w)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`Matrix.mulVec_cross_mulVec`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/Matrix/CrossProduct.html#Matrix.mulVec_cross_mulVec).

## Sources

- [Tau Ceti documentation: `Matrix.mulVec_cross_mulVec`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/Matrix/CrossProduct.html#Matrix.mulVec_cross_mulVec)
- [Source of `Matrix.mulVec_cross_mulVec` in TauCeti/LinearAlgebra/Matrix/CrossProduct.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/LinearAlgebra/Matrix/CrossProduct.lean#L56)
