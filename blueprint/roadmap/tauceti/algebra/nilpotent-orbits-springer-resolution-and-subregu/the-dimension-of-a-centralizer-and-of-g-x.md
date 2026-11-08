---
declaration: theorem
origin: cited
lean: TauCeti.ringKrullDim_quotient_centralizerHopfIdeal_add_finrank_range_ad
statement: formalized
proof: formalized
---

# The dimension of a centralizer and of `[𝔤, x]`

Over a field of characteristic zero, the
dimension of a finite-type affine group `G` is the dimension of the centralizer `C_G(x)` of an
element `x` of its Lie algebra `𝔤` plus the rank of `ad x`, the dimension of `[𝔤, x]`.

```lean
TauCeti.ringKrullDim_quotient_centralizerHopfIdeal_add_finrank_range_ad.{u} {k : Type u} [Field k]
  [CharZero k] {H : Type u} [CommRing H] [HopfAlgebra k H] [Algebra.FiniteType k H]
  (x : Module.Dual k (TauCeti.Bialgebra.CotangentSpace k H)) :
  ringKrullDim (H ⧸ (TauCeti.centralizerHopfIdeal H x).toIdeal) +
      ↑(Module.finrank k
          ↥(LinearMap.range
              ((LieAlgebra.ad k (Module.Dual k (TauCeti.Bialgebra.CotangentSpace k H))) x))) =
    ringKrullDim H
```

## Depends on

- [TauCeti.centralizerHopfIdeal](tauceti-centralizerhopfideal.md)

## Proof depends on

- [Cartier's theorem](../algebraic-group/cartiers-theorem.md)
- [The Jacobian criterion for étaleness](../../ring-theory/other-results/part-01/the-jacobian-criterion-for-etaleness.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.ringKrullDim_quotient_centralizerHopfIdeal_add_finrank_range_ad`](https://taucetiproject.org/docs/TauCeti/Algebra/AlgebraicGroup/Tangent/Lie/Adjoint/Centralizer/Basic.html#TauCeti.ringKrullDim_quotient_centralizerHopfIdeal_add_finrank_range_ad).

## Sources

- [Tau Ceti documentation: `TauCeti.ringKrullDim_quotient_centralizerHopfIdeal_add_finrank_range_ad`](https://taucetiproject.org/docs/TauCeti/Algebra/AlgebraicGroup/Tangent/Lie/Adjoint/Centralizer/Basic.html#TauCeti.ringKrullDim_quotient_centralizerHopfIdeal_add_finrank_range_ad)
- [Source of `TauCeti.ringKrullDim_quotient_centralizerHopfIdeal_add_finrank_range_ad` in TauCeti/Algebra/AlgebraicGroup/Tangent/Lie/Adjoint/Centralizer/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Algebra/AlgebraicGroup/Tangent/Lie/Adjoint/Centralizer/Basic.lean#L239)
- [Tau Ceti roadmap status: Nilpotent orbits, Springer resolution and subregular geometry](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/NilpotentOrbits/STATUS.md)
