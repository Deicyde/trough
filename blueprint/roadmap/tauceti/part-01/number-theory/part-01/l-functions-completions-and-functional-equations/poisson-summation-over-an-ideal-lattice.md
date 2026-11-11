---
declaration: theorem
origin: cited
lean: TauCeti.NumberField.mixedEmbedding.tsum_idealLattice_eq_tsum_mixedDual_mixedFourier
statement: formalized
proof: formalized
---

# Poisson summation over an ideal lattice

the lattice `σ(I)` of a fractional ideal `I` in
the mixed space, at `v = 0`. Its covolume `ZLattice.covolume (idealLattice K I)` is
`N(I) * 2 ^ (-r₂) * √|d_K|` by Mathlib's `NumberField.mixedEmbedding.covolume_idealLattice`.

```lean
TauCeti.NumberField.mixedEmbedding.tsum_idealLattice_eq_tsum_mixedDual_mixedFourier.{u_1}
  (K : Type u_1) [Field K] [NumberField K]
  (I : (FractionalIdeal (nonZeroDivisors (NumberField.RingOfIntegers K)) K)ˣ)
  (f : SchwartzMap (NumberField.mixedEmbedding.mixedSpace K) ℂ) :
  ∑' (x : ↥(NumberField.mixedEmbedding.idealLattice K I)), f ↑x =
    (↑(ZLattice.covolume (NumberField.mixedEmbedding.idealLattice K I) MeasureTheory.volume))⁻¹ *
      ∑' (m :
        ↥(TauCeti.NumberField.mixedEmbedding.mixedDual K
            (NumberField.mixedEmbedding.idealLattice K I))),
        TauCeti.NumberField.mixedEmbedding.mixedFourier K ⇑f ↑m
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Poisson's summation formula](../../../analysis/part-02/fourier/poissons-summation-formula.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.NumberField.mixedEmbedding.tsum_idealLattice_eq_tsum_mixedDual_mixedFourier`](https://taucetiproject.org/docs/TauCeti/NumberTheory/NumberField/CanonicalEmbedding/PoissonSummation.html#TauCeti.NumberField.mixedEmbedding.tsum_idealLattice_eq_tsum_mixedDual_mixedFourier).

## Sources

- [Tau Ceti documentation: `TauCeti.NumberField.mixedEmbedding.tsum_idealLattice_eq_tsum_mixedDual_mixedFourier`](https://taucetiproject.org/docs/TauCeti/NumberTheory/NumberField/CanonicalEmbedding/PoissonSummation.html#TauCeti.NumberField.mixedEmbedding.tsum_idealLattice_eq_tsum_mixedDual_mixedFourier)
- [Source of `TauCeti.NumberField.mixedEmbedding.tsum_idealLattice_eq_tsum_mixedDual_mixedFourier` in TauCeti/NumberTheory/NumberField/CanonicalEmbedding/PoissonSummation.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/NumberTheory/NumberField/CanonicalEmbedding/PoissonSummation.lean#L361)
- [Tau Ceti roadmap status: L-functions — completions and functional equations](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/LFunctions/STATUS.md)
