---
declaration: theorem
origin: cited
lean: TauCeti.lsCategoryCount_univ_le_totalCriticalCount, TauCeti.lsCategoryCount_univ_le_encard_criticalPoints_inter, TauCeti.lsCategoryCount_sublevel_le_encard, TauCeti.lsCategoryCount_univ_le_minCriticalCount
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

- [Fermat's theorem on a manifold](fermats-theorem-on-a-manifold.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.lsCategoryCount_univ_le_totalCriticalCount`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Morse/LusternikSchnirelmann.html#TauCeti.lsCategoryCount_univ_le_totalCriticalCount).

## Other forms

**The Lusternik–Schnirelmann bound on a compact open part.** Formalized in Tau Ceti as [`TauCeti.lsCategoryCount_univ_le_encard_criticalPoints_inter`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Morse/LusternikSchnirelmann.html#TauCeti.lsCategoryCount_univ_le_encard_criticalPoints_inter).

```lean
TauCeti.lsCategoryCount_univ_le_encard_criticalPoints_inter.{u_1, u_2, u_3} {E : Type u_1}
  [NormedAddCommGroup E] [NormedSpace ℝ E] {H : Type u_2} [TopologicalSpace H]
  {I : ModelWithCorners ℝ E H} {M : Type u_3} [TopologicalSpace M] [ChartedSpace H M] {f : M → ℝ}
  [FiniteDimensional ℝ E] [T2Space M] [I.Boundaryless] [IsManifold I (↑⊤) M] {C : Set M}
  (hf : ContMDiffOn I (modelWithCornersSelf ℝ ℝ) (↑⊤) f C) (hCo : IsOpen C) (hCc : IsCompact C) :
  TauCeti.lsCategoryCount (↑C) Set.univ ≤ (TauCeti.criticalPoints I f ∩ C).encard
```

**The Lusternik–Schnirelmann bound on sublevels.** Formalized in Tau Ceti as [`TauCeti.lsCategoryCount_sublevel_le_encard`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Morse/LusternikSchnirelmann.html#TauCeti.lsCategoryCount_sublevel_le_encard).

```lean
TauCeti.lsCategoryCount_sublevel_le_encard.{u_1, u_2, u_3} {E : Type u_1} [NormedAddCommGroup E]
  [NormedSpace ℝ E] {H : Type u_2} [TopologicalSpace H] {I : ModelWithCorners ℝ E H} {M : Type u_3}
  [TopologicalSpace M] [ChartedSpace H M] {f : M → ℝ} [FiniteDimensional ℝ E] [T2Space M]
  [I.Boundaryless] [IsManifold I (↑⊤) M] (hf : ContMDiff I (modelWithCornersSelf ℝ ℝ) (↑⊤) f)
  {t b : ℝ} (htb : t < b) (hb : IsCompact {x | f x ≤ b})
  (hfin : (TauCeti.criticalPoints I f ∩ {x | f x ≤ b}).Finite) :
  TauCeti.lsCategoryCount M {x | f x ≤ t} ≤ (TauCeti.criticalPoints I f ∩ {x | f x ≤ t}).encard
```

**The Lusternik–Schnirelmann lower bound for `c(M)`.** Formalized in Tau Ceti as [`TauCeti.lsCategoryCount_univ_le_minCriticalCount`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Morse/MinCriticalCount.html#TauCeti.lsCategoryCount_univ_le_minCriticalCount).

```lean
TauCeti.lsCategoryCount_univ_le_minCriticalCount.{u_1, u_2, u_3} {E : Type u_1}
  [NormedAddCommGroup E] [NormedSpace ℝ E] {H : Type u_2} [TopologicalSpace H]
  {I : ModelWithCorners ℝ E H} {M : Type u_3} [TopologicalSpace M] [ChartedSpace H M]
  [I.Boundaryless] [CompactSpace M] [FiniteDimensional ℝ E] [T2Space M] [IsManifold I (↑⊤) M] :
  TauCeti.lsCategoryCount M Set.univ ≤ TauCeti.minCriticalCount I M
```

## Sources

- [Tau Ceti documentation: `TauCeti.lsCategoryCount_univ_le_totalCriticalCount`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Morse/LusternikSchnirelmann.html#TauCeti.lsCategoryCount_univ_le_totalCriticalCount)
- [Source of `TauCeti.lsCategoryCount_univ_le_totalCriticalCount` in TauCeti/Geometry/Manifold/Morse/LusternikSchnirelmann.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Geometry/Manifold/Morse/LusternikSchnirelmann.lean#L217)
- [Tau Ceti roadmap status: Morse functions, sublevel topology and Morse–Bott attachments](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/MorseTheory/STATUS.md)
