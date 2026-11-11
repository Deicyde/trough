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
- [The global dimension of a regular local ring is its Krull dimension](../../../ring-theory/part-01/purity-of-the-branch-locus/the-global-dimension-of-a-regular-local-ring-is.md)
- [The Jacobian criterion for étaleness](../../../ring-theory/part-02/other-results/part-02/the-jacobian-criterion-for-etaleness.md)
- [Serre's theorem (`TauCeti.IsRegularLocalRing.of_hasProjectiveDimensionLE`)](../../../ring-theory/part-01/purity-of-the-branch-locus/serres-theorem-tauceti-isregularlocalring-of-has.md)
- [TauCeti.globalDimension](../../../ring-theory/part-01/purity-of-the-branch-locus/tauceti-globaldimension.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.ringKrullDim_quotient_centralizerHopfIdeal_add_finrank_range_ad`](https://taucetiproject.org/docs/TauCeti/Algebra/AlgebraicGroup/Tangent/Lie/Adjoint/Centralizer/Basic.html#TauCeti.ringKrullDim_quotient_centralizerHopfIdeal_add_finrank_range_ad).

## Sources

- [Tau Ceti documentation: `TauCeti.ringKrullDim_quotient_centralizerHopfIdeal_add_finrank_range_ad`](https://taucetiproject.org/docs/TauCeti/Algebra/AlgebraicGroup/Tangent/Lie/Adjoint/Centralizer/Basic.html#TauCeti.ringKrullDim_quotient_centralizerHopfIdeal_add_finrank_range_ad)
- [Source of `TauCeti.ringKrullDim_quotient_centralizerHopfIdeal_add_finrank_range_ad` in TauCeti/Algebra/AlgebraicGroup/Tangent/Lie/Adjoint/Centralizer/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Algebra/AlgebraicGroup/Tangent/Lie/Adjoint/Centralizer/Basic.lean#L239)
- [Tau Ceti roadmap status: Nilpotent orbits, Springer resolution and subregular geometry](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/NilpotentOrbits/STATUS.md)
