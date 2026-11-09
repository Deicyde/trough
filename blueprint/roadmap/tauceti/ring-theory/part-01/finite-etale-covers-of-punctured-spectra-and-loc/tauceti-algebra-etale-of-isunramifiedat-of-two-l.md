---
declaration: theorem
origin: cited
lean: TauCeti.Algebra.etale_of_isUnramifiedAt_of_two_le_ringKrullDim
statement: formalized
proof: formalized
---

# TauCeti.Algebra.etale_of_isUnramifiedAt_of_two_le_ringKrullDim

A finite flat algebra over a Noetherian local ring of dimension at least two is étale
everywhere if it is unramified at each prime not lying over the closed point. This is the finite
flat case of local purity, with no regularity or normality assumptions.

```lean
TauCeti.Algebra.etale_of_isUnramifiedAt_of_two_le_ringKrullDim.{u_1, u_2} {A : Type u_1}
  {B : Type u_2} [CommRing A] [CommRing B] [Algebra A B] [IsNoetherianRing A] [IsLocalRing A]
  [Module.Finite A B] [Module.Flat A B] (hdim : 2 ≤ ringKrullDim A)
  (h :
    ∀ (q : Ideal B) [inst : q.IsPrime],
      Ideal.under A q ≠ IsLocalRing.maximalIdeal A → Algebra.IsUnramifiedAt A q) :
  Algebra.Etale A B
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [TauCeti.Algebra.etale_iff_etale_fiber_of_height_le_one](tauceti-algebra-etale-iff-etale-fiber-of-height.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Algebra.etale_of_isUnramifiedAt_of_two_le_ringKrullDim`](https://taucetiproject.org/docs/TauCeti/RingTheory/Etale/Purity.html#TauCeti.Algebra.etale_of_isUnramifiedAt_of_two_le_ringKrullDim).

## Sources

- [Tau Ceti documentation: `TauCeti.Algebra.etale_of_isUnramifiedAt_of_two_le_ringKrullDim`](https://taucetiproject.org/docs/TauCeti/RingTheory/Etale/Purity.html#TauCeti.Algebra.etale_of_isUnramifiedAt_of_two_le_ringKrullDim)
- [Source of `TauCeti.Algebra.etale_of_isUnramifiedAt_of_two_le_ringKrullDim` in TauCeti/RingTheory/Etale/Purity.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RingTheory/Etale/Purity.lean#L67)
- [Tau Ceti roadmap status: Finite étale covers of punctured spectra and local purity](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/LocalPurity/STATUS.md)
