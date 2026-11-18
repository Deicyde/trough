---
declaration: theorem
origin: cited
lean: TauCeti.lsCategoryCount_univ_le_totalCriticalCount
statement: formalized
proof: formalized
---

# The Lusternik–Schnirelmann theorem

On a compact boundaryless manifold `M`, the
Lusternik–Schnirelmann count of `M` is at most the number of critical points of any smooth
function on `M`. The critical points may be degenerate; if there are infinitely many, their count
is `⊤`.

```lean
TauCeti.lsCategoryCount_univ_le_totalCriticalCount.{u_1, u_2, u_3} {E : Type u_1}
  [NormedAddCommGroup E] [NormedSpace ℝ E] {H : Type u_2} [TopologicalSpace H]
  {I : ModelWithCorners ℝ E H} {M : Type u_3} [TopologicalSpace M] [ChartedSpace H M] {f : M → ℝ}
  [FiniteDimensional ℝ E] [T2Space M] [I.Boundaryless] [IsManifold I (↑⊤) M] [CompactSpace M]
  (hf : ContMDiff I (modelWithCornersSelf ℝ ℝ) (↑⊤) f) :
  TauCeti.lsCategoryCount M Set.univ ≤ TauCeti.totalCriticalCount I f
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Lusternik–Schnirelmann bound on the torus](the-lusternik-schnirelmann-bound-on-the-torus.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.lsCategoryCount_univ_le_totalCriticalCount`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Morse/LusternikSchnirelmann.html#TauCeti.lsCategoryCount_univ_le_totalCriticalCount).

## Sources

- [Tau Ceti documentation: `TauCeti.lsCategoryCount_univ_le_totalCriticalCount`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Morse/LusternikSchnirelmann.html#TauCeti.lsCategoryCount_univ_le_totalCriticalCount)
- [Source of `TauCeti.lsCategoryCount_univ_le_totalCriticalCount` in TauCeti/Geometry/Manifold/Morse/LusternikSchnirelmann.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Geometry/Manifold/Morse/LusternikSchnirelmann.lean#L217)
- [Tau Ceti roadmap status: Morse functions, sublevel topology and Morse–Bott attachments](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/MorseTheory/STATUS.md)
