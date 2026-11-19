---
declaration: def
origin: cited
lean: TauCeti.TopCat.arbitraryBaseSerreSpectralSequencePageXIsoGraded
statement: formalized
---

# Strong convergence of the Serre spectral sequence over an arbitrary base

Let `p : E ⟶ B`
be a Serre fibration, with no hypothesis on `B`. On every page `r ≥ 2` with `b + 3 ≤ r` and
`2 - a - 2b ≤ r`, the object at `pq = (a, b)` is the graded piece `F_{b+1} H / F_b H` of the
filtration of the abutment in degree `a + b`, which is `H_{-(a+b)}(E; R)` by
`TauCeti.TopCat.arbitraryBaseSerreAbutmentIso`.

```lean
TauCeti.TopCat.arbitraryBaseSerreSpectralSequencePageXIsoGraded.{u} {E B : TopCat} {p : E ⟶ B}
  (hp : TauCeti.TopCat.serreFibrations p) (R : Type u) [Ring R] (r : ℤ) (hr : 2 ≤ r) (pq : ℤ × ℤ)
  (hra : pq.2 + 3 ≤ r) (hrb : 2 - pq.1 - 2 * pq.2 ≤ r) :
  ((TopCat.Hom.arbitraryBaseSerreSpectralSequence p R).page r ⋯).X pq ≅
    CategoryTheory.Limits.cokernel
      ((TopCat.Hom.arbitraryBaseSerreSpectralObject p R).abutmentFiltrationMap pq.2 (pq.1 + pq.2))
```

## Depends on

- [The Serre spectral sequence over an arbitrary base](the-serre-spectral-sequence-over-an-arbitrary-ba.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.TopCat.arbitraryBaseSerreSpectralSequencePageXIsoGraded`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Singular/Fibration/ArbitraryBase.html#TauCeti.TopCat.arbitraryBaseSerreSpectralSequencePageXIsoGraded).

## Sources

- [Tau Ceti documentation: `TauCeti.TopCat.arbitraryBaseSerreSpectralSequencePageXIsoGraded`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Singular/Fibration/ArbitraryBase.html#TauCeti.TopCat.arbitraryBaseSerreSpectralSequencePageXIsoGraded)
- [Source of `TauCeti.TopCat.arbitraryBaseSerreSpectralSequencePageXIsoGraded` in TauCeti/AlgebraicTopology/Singular/Fibration/ArbitraryBase.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/AlgebraicTopology/Singular/Fibration/ArbitraryBase.lean#L255)
- [Tau Ceti roadmap status: Morse and Floer homology with DG local coefficients](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/DGFloer/STATUS.md)
