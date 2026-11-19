---
declaration: theorem
origin: cited
lean: TauCeti.IsLocalRing.purityHolds_of_ringKrullDim_eq_two
statement: formalized
proof: formalized
---

# Purity for a two-dimensional regular local ring (`TauCeti.IsLocalRing.purityHolds_of_ringKrullDim_eq_two`)

If `A` is a regular local ring of
dimension two, every finite étale cover of the punctured spectrum of `A` extends to a finite étale
scheme over `Spec A`.

```lean
TauCeti.IsLocalRing.purityHolds_of_ringKrullDim_eq_two.{u} {A : Type u} [CommRing A]
  [IsRegularLocalRing A] (hdim : ringKrullDim A = 2) : TauCeti.IsLocalRing.PurityHolds A
```

## Depends on

- [TauCeti.IsLocalRing.PurityHolds](tauceti-islocalring-purityholds.md)

## Proof depends on

- [Algebraic Hartogs principle](../other-results/algebraic-hartogs-principle.md)
- [Algebraic Hartogs principle for fractions](../../ring-theory/part-02/other-results/part-01/algebraic-hartogs-principle-for-fractions.md)
- [The global dimension of a regular local ring is its Krull dimension](../../ring-theory/part-01/purity-of-the-branch-locus/the-global-dimension-of-a-regular-local-ring-is.md)
- [Hartogs principle for `M~` on `Spec R`](../other-results/hartogs-principle-for-m-on-spec-r.md)
- [Purity for a two-dimensional regular local ring (`TauCeti.Algebra.etale_of_finiteNormal_of_ringKrullDim_eq_two`)](purity-for-a-two-dimensional-regular-local-ring-2.md)
- [Serre's theorem (`TauCeti.IsRegularLocalRing.of_hasProjectiveDimensionLE`)](../../ring-theory/part-01/purity-of-the-branch-locus/serres-theorem-tauceti-isregularlocalring-of-has.md)
- [TauCeti.globalDimension](../../ring-theory/part-01/purity-of-the-branch-locus/tauceti-globaldimension.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.IsLocalRing.purityHolds_of_ringKrullDim_eq_two`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/FiniteEtale/Purity.html#TauCeti.IsLocalRing.purityHolds_of_ringKrullDim_eq_two).

## Sources

- [Tau Ceti documentation: `TauCeti.IsLocalRing.purityHolds_of_ringKrullDim_eq_two`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/FiniteEtale/Purity.html#TauCeti.IsLocalRing.purityHolds_of_ringKrullDim_eq_two)
- [Source of `TauCeti.IsLocalRing.purityHolds_of_ringKrullDim_eq_two` in TauCeti/AlgebraicGeometry/FiniteEtale/Purity.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/AlgebraicGeometry/FiniteEtale/Purity.lean#L49)
- [Tau Ceti roadmap status: Finite étale covers of punctured spectra and local purity](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/LocalPurity/STATUS.md)
