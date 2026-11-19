---
declaration: theorem
origin: cited
lean: TauCeti.Algebra.etale_of_isUnramifiedAt_height_eq_one_of_ringKrullDim_le_two
statement: formalized
proof: formalized
---

# Purity of the branch locus over a regular local ring of dimension one or two

Let `A` be
a regular local ring of dimension one or two and `B` a finite torsion-free `A`-algebra whose
localizations at maximal ideals are normal domains. If `B` is unramified over `A` at every prime
of height one, then `B` is étale over `A`.

```lean
TauCeti.Algebra.etale_of_isUnramifiedAt_height_eq_one_of_ringKrullDim_le_two.{u_1, u_2}
  {A : Type u_1} {B : Type u_2} [CommRing A] [CommRing B] [Algebra A B] [IsRegularLocalRing A]
  [Module.Finite A B] [Module.IsTorsionFree A B] (hdim₁ : 1 ≤ ringKrullDim A)
  (hdim₂ : ringKrullDim A ≤ 2)
  (hnormal :
    ∀ (𝔮 : Ideal B) [inst : 𝔮.IsMaximal],
      IsDomain (Localization.AtPrime 𝔮) ∧ IsIntegrallyClosed (Localization.AtPrime 𝔮))
  (hunram : ∀ (q : Ideal B) [inst : q.IsPrime], q.height = 1 → Algebra.IsUnramifiedAt A q) :
  Algebra.Etale A B
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Purity for a two-dimensional regular local ring (`TauCeti.Algebra.etale_of_finiteNormal_of_ringKrullDim_eq_two`)](../../../algebraic-geometry/finite-etale-covers-of-punctured-spectra-and-loc/purity-for-a-two-dimensional-regular-local-ring-2.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Algebra.etale_of_isUnramifiedAt_height_eq_one_of_ringKrullDim_le_two`](https://taucetiproject.org/docs/TauCeti/RingTheory/RegularLocalRing/Purity.html#TauCeti.Algebra.etale_of_isUnramifiedAt_height_eq_one_of_ringKrullDim_le_two).

## Sources

- [Tau Ceti documentation: `TauCeti.Algebra.etale_of_isUnramifiedAt_height_eq_one_of_ringKrullDim_le_two`](https://taucetiproject.org/docs/TauCeti/RingTheory/RegularLocalRing/Purity.html#TauCeti.Algebra.etale_of_isUnramifiedAt_height_eq_one_of_ringKrullDim_le_two)
- [Source of `TauCeti.Algebra.etale_of_isUnramifiedAt_height_eq_one_of_ringKrullDim_le_two` in TauCeti/RingTheory/RegularLocalRing/Purity.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/RingTheory/RegularLocalRing/Purity.lean#L83)
- [Tau Ceti roadmap status: Purity of the branch locus](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/PurityOfBranchLocus/STATUS.md)
