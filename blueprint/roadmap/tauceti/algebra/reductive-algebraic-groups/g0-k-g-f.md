---
declaration: def
origin: cited
lean: TauCeti.FiniteField.rationalPointsMulEquivFixedSubgroupGeometricFrobenius
statement: formalized
---

# `G₀(K) ≃ G^F`

The `K`-rational points of `H` are isomorphic to the points of the base
change `k ⊗[K] H` over a domain `k` fixed by the geometric Frobenius. The isomorphism sends a
rational point `g` to `s ⊗ h ↦ s * g h`.

```lean
TauCeti.FiniteField.rationalPointsMulEquivFixedSubgroupGeometricFrobenius.{u_1, u_2, u_3}
  (K : Type u_1) [Field K] [Fintype K] (k : Type u_2) [CommRing k] [IsDomain k] [Algebra K k]
  (H : Type u_3) [CommSemiring H] [HopfAlgebra K H] :
  WithConv (H →ₐ[K] K) ≃*
    ↥(TauCeti.fixedSubgroup (TauCeti.FiniteField.geometricFrobeniusBialgHom K k H).mapDomain)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.FiniteField.rationalPointsMulEquivFixedSubgroupGeometricFrobenius`](https://taucetiproject.org/docs/TauCeti/Algebra/AlgebraicGroup/Frobenius/FiniteField.html#TauCeti.FiniteField.rationalPointsMulEquivFixedSubgroupGeometricFrobenius).

## Sources

- [Tau Ceti documentation: `TauCeti.FiniteField.rationalPointsMulEquivFixedSubgroupGeometricFrobenius`](https://taucetiproject.org/docs/TauCeti/Algebra/AlgebraicGroup/Frobenius/FiniteField.html#TauCeti.FiniteField.rationalPointsMulEquivFixedSubgroupGeometricFrobenius)
- [Source of `TauCeti.FiniteField.rationalPointsMulEquivFixedSubgroupGeometricFrobenius` in TauCeti/Algebra/AlgebraicGroup/Frobenius/FiniteField.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Algebra/AlgebraicGroup/Frobenius/FiniteField.lean#L431)
- [Tau Ceti roadmap status: Reductive algebraic groups](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/ReductiveGroups/STATUS.md)
