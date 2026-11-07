---
declaration: theorem
origin: cited
lean: OrthonormalBasis.volume_weighted_crosspolytope
statement: formalized
proof: formalized
---

# OrthonormalBasis.volume\_weighted\_crosspolytope

The canonical Euclidean volume of a weighted cross-polytope in an arbitrary real basis.
The index type may be empty, in which case the volume and the empty products are one.

```lean
OrthonormalBasis.volume_weighted_crosspolytope.{u_1, u_2} {ι : Type u_1} {E : Type u_2} [Fintype ι]
  [DecidableEq ι] [NormedAddCommGroup E] [InnerProductSpace ℝ E] [FiniteDimensional ℝ E]
  [MeasurableSpace E] [BorelSpace E] (o : OrthonormalBasis ι ℝ E) (b : Module.Basis ι ℝ E)
  (a : ι → ℝ) (ha : ∀ (i : ι), 0 < a i) :
  MeasureTheory.volume {x | ∑ i, a i * |(b.repr x) i| ≤ 1} =
    ENNReal.ofReal
      (2 ^ Fintype.card ι / ↑(Fintype.card ι).factorial * |o.toBasis.det ⇑b| / ∏ i, a i)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`OrthonormalBasis.volume_weighted_crosspolytope`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Measure/Lebesgue/Weighted/Crosspolytope.html#OrthonormalBasis.volume_weighted_crosspolytope).

## Sources

- [Tau Ceti documentation: `OrthonormalBasis.volume_weighted_crosspolytope`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Measure/Lebesgue/Weighted/Crosspolytope.html#OrthonormalBasis.volume_weighted_crosspolytope)
- [Source of `OrthonormalBasis.volume_weighted_crosspolytope` in TauCeti/MeasureTheory/Measure/Lebesgue/Weighted/Crosspolytope.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/MeasureTheory/Measure/Lebesgue/Weighted/Crosspolytope.lean#L96)
- [Tau Ceti roadmap status: Successive minima and Minkowski's theorems](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/SuccessiveMinima/STATUS.md)
