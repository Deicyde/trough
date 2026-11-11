---
declaration: theorem
origin: cited
lean: Convex.addHaar_iUnion_vadd
statement: formalized
proof: formalized
---

# Volume of interior-disjoint translates

If the translates `v i +ᵥ interior K` of the
interior of a convex set `K` are pairwise disjoint, then the union of the finitely many translates
`v i +ᵥ K` has `card ι` times the additive Haar measure of `K`. The translates may share boundary
points, and `K` need not be closed, bounded or full-dimensional.

```lean
Convex.addHaar_iUnion_vadd.{u_1, u_2} {E : Type u_1} [NormedAddCommGroup E] [NormedSpace ℝ E]
  [FiniteDimensional ℝ E] [MeasurableSpace E] [BorelSpace E] {μ : MeasureTheory.Measure E}
  [μ.IsAddHaarMeasure] {K : Set E} (hK : Convex ℝ K) {ι : Type u_2} [Fintype ι] {v : ι → E}
  (h : Pairwise (Function.onFun Disjoint fun i => v i +ᵥ interior K)) :
  μ (⋃ i, v i +ᵥ K) = ↑(Fintype.card ι) * μ K
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`Convex.addHaar_iUnion_vadd`](https://taucetiproject.org/docs/TauCeti/Analysis/Convex/Measure.html#Convex.addHaar_iUnion_vadd).

## Sources

- [Tau Ceti documentation: `Convex.addHaar_iUnion_vadd`](https://taucetiproject.org/docs/TauCeti/Analysis/Convex/Measure.html#Convex.addHaar_iUnion_vadd)
- [Source of `Convex.addHaar_iUnion_vadd` in TauCeti/Analysis/Convex/Measure.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Convex/Measure.lean#L192)
- [Tau Ceti roadmap status: Successive minima and Minkowski's theorems](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/SuccessiveMinima/STATUS.md)
