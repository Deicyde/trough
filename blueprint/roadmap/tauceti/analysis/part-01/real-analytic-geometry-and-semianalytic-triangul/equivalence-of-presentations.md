---
declaration: theorem
origin: cited
lean: TauCeti.semianalyticAt_iff_exists_iUnion
statement: formalized
proof: formalized
---

# Equivalence of presentations

A set is semianalytic at `x` if and only if, on some
neighbourhood `U` of `x`, it agrees with a finite union of sets
`{y | f y = 0 ∧ 0 < g₁ y ∧ ⋯ ∧ 0 < gₖ y}` with `f, g₁, …, gₖ` analytic on `U`.

```lean
TauCeti.semianalyticAt_iff_exists_iUnion.{u_1} {E : Type u_1} [NormedAddCommGroup E]
  [NormedSpace ℝ E] {s : Set E} {x : E} :
  TauCeti.SemianalyticAt s x ↔
    ∃ U ∈ nhds x,
      ∃ m k f g,
        (∀ (i : Fin m), AnalyticOnNhd ℝ (f i) U) ∧
          (∀ (i : Fin m) (j : Fin k), AnalyticOnNhd ℝ (g i j) U) ∧
            s ∩ U = (⋃ i, {y | f i y = 0} ∩ ⋂ j, {y | 0 < g i j y}) ∩ U
```

## Depends on

- [TauCeti.SemianalyticAt](tauceti-semianalyticat.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.semianalyticAt_iff_exists_iUnion`](https://taucetiproject.org/docs/TauCeti/Geometry/RealAnalytic/Semianalytic/Basic.html#TauCeti.semianalyticAt_iff_exists_iUnion).

## Sources

- [Tau Ceti documentation: `TauCeti.semianalyticAt_iff_exists_iUnion`](https://taucetiproject.org/docs/TauCeti/Geometry/RealAnalytic/Semianalytic/Basic.html#TauCeti.semianalyticAt_iff_exists_iUnion)
- [Source of `TauCeti.semianalyticAt_iff_exists_iUnion` in TauCeti/Geometry/RealAnalytic/Semianalytic/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Geometry/RealAnalytic/Semianalytic/Basic.lean#L397)
- [Tau Ceti roadmap status: Real-analytic geometry and semianalytic triangulation](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/RealAnalyticGeometry/STATUS.md)
