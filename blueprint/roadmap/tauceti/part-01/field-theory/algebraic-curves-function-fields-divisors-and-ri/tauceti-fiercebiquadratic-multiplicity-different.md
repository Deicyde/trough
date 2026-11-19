---
declaration: theorem
origin: cited
lean: TauCeti.FierceBiquadratic.multiplicity_differentIdeal_ne_finsum_ringYZ
statement: formalized
proof: formalized
---

# TauCeti.FierceBiquadratic.multiplicity_differentIdeal_ne_finsum_ringYZ

Hilbert's lower-ramification-group formula fails without separability of the
residue extension, even for this finite free extension of DVRs.

```lean
TauCeti.FierceBiquadratic.multiplicity_differentIdeal_ne_finsum_ringYZ.{u_1} {A : Type u_1}
  [CommRing A] [CharP A 2] [IsDomain A] [IsDiscreteValuationRing A] {t s u : A}
  [IsDomain (TauCeti.FierceBiquadratic.RingYZ t s u)]
  [IsLocalRing (TauCeti.FierceBiquadratic.RingYZ t s u)] (ht : Irreducible t)
  (hs : ∀ (a : IsLocalRing.ResidueField A), a ^ 2 ≠ (IsLocalRing.residue A) s)
  (hu :
    ∀ (a b : IsLocalRing.ResidueField A),
      a ^ 2 + (IsLocalRing.residue A) s * b ^ 2 ≠ (IsLocalRing.residue A) u) :
  multiplicity (IsLocalRing.maximalIdeal (TauCeti.FierceBiquadratic.RingYZ t s u))
      (differentIdeal A (TauCeti.FierceBiquadratic.RingYZ t s u)) ≠
    ∑ᶠ (i : ℕ),
      (Nat.card
          ↥(TauCeti.IsLocalRing.ramificationGroup
              (TauCeti.FierceBiquadratic.RingYZ t s u ≃ₐ[A] TauCeti.FierceBiquadratic.RingYZ t s u)
              (TauCeti.FierceBiquadratic.RingYZ t s u) ↑i) -
        1)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The global dimension of a regular local ring is its Krull dimension](../../ring-theory/part-01/purity-of-the-branch-locus/the-global-dimension-of-a-regular-local-ring-is.md)
- [Serre's criterion for the ramification filtration](../../ring-theory/part-01/local-ring/serres-criterion-for-the-ramification-filtration.md)
- [Serre's theorem (`TauCeti.IsRegularLocalRing.of_hasProjectiveDimensionLE`)](../../ring-theory/part-01/purity-of-the-branch-locus/serres-theorem-tauceti-isregularlocalring-of-has.md)
- [TauCeti.globalDimension](../../ring-theory/part-01/purity-of-the-branch-locus/tauceti-globaldimension.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.FierceBiquadratic.multiplicity_differentIdeal_ne_finsum_ringYZ`](https://taucetiproject.org/docs/TauCeti/RingTheory/DiscreteValuationRing/FierceBiquadratic/Different.html#TauCeti.FierceBiquadratic.multiplicity_differentIdeal_ne_finsum_ringYZ).

## Sources

- [Tau Ceti documentation: `TauCeti.FierceBiquadratic.multiplicity_differentIdeal_ne_finsum_ringYZ`](https://taucetiproject.org/docs/TauCeti/RingTheory/DiscreteValuationRing/FierceBiquadratic/Different.html#TauCeti.FierceBiquadratic.multiplicity_differentIdeal_ne_finsum_ringYZ)
- [Source of `TauCeti.FierceBiquadratic.multiplicity_differentIdeal_ne_finsum_ringYZ` in TauCeti/RingTheory/DiscreteValuationRing/FierceBiquadratic/Different.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/RingTheory/DiscreteValuationRing/FierceBiquadratic/Different.lean#L220)
- [Tau Ceti roadmap status: Algebraic curves — function fields, divisors, and Riemann–Roch](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/AlgebraicCurves/STATUS.md)
