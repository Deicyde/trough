---
declaration: def
origin: cited
lean: MeasureTheory.successiveMin
statement: formalized
---

# MeasureTheory.successiveMin

The `i`-th successive minimum of a set `s` around the origin with respect to a submodule `L`:
the infimum of the `r : ℝ≥0` such that `r • s ∩ L` spans a real subspace of dimension greater than
`i`. The index is zero-based, so `successiveMin L s 0` is the first minimum. At indices for which
no such `r` exists, for instance beyond the dimension of `E`, its value is the junk value `0`.

```lean
MeasureTheory.successiveMin.{u_1} {E : Type u_1} [NormedAddCommGroup E] [NormedSpace ℝ E]
  (L : Submodule ℤ E) (s : Set E) (i : ℕ) : NNReal
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`MeasureTheory.successiveMin`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Group/GeometryOfNumbers/SuccessiveMinima.html#MeasureTheory.successiveMin).

## Sources

- [Tau Ceti documentation: `MeasureTheory.successiveMin`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Group/GeometryOfNumbers/SuccessiveMinima.html#MeasureTheory.successiveMin)
- [Source of `MeasureTheory.successiveMin` in TauCeti/MeasureTheory/Group/GeometryOfNumbers/SuccessiveMinima.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/MeasureTheory/Group/GeometryOfNumbers/SuccessiveMinima.lean#L79)
- [Tau Ceti roadmap status: Successive minima and Minkowski's theorems](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/SuccessiveMinima/STATUS.md)
