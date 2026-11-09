---
declaration: theorem
origin: cited
lean: TauCeti.lsCategoryCount_sublevel_le_encard, TauCeti.lsCategoryCount_univ_le_encard_criticalPoints_inter
statement: formalized
proof: formalized
---

# The Lusternik–Schnirelmann bound on sublevels

Let `f` be smooth and `t < b`, and suppose
that the sublevel `{f ≤ b}` is compact and contains only finitely many critical points of `f`. Then
the Lusternik–Schnirelmann count of `{f ≤ t}` is at most the number of critical points of `f` in
`{f ≤ t}`. The critical points may be degenerate.

```lean
TauCeti.lsCategoryCount_sublevel_le_encard.{u_1, u_2, u_3} {E : Type u_1} [NormedAddCommGroup E]
  [NormedSpace ℝ E] {H : Type u_2} [TopologicalSpace H] {I : ModelWithCorners ℝ E H} {M : Type u_3}
  [TopologicalSpace M] [ChartedSpace H M] {f : M → ℝ} [FiniteDimensional ℝ E] [T2Space M]
  [I.Boundaryless] [IsManifold I (↑⊤) M] (hf : ContMDiff I (modelWithCornersSelf ℝ ℝ) (↑⊤) f)
  {t b : ℝ} (htb : t < b) (hb : IsCompact {x | f x ≤ b})
  (hfin : (TauCeti.criticalPoints I f ∩ {x | f x ≤ b}).Finite) :
  TauCeti.lsCategoryCount M {x | f x ≤ t} ≤ (TauCeti.criticalPoints I f ∩ {x | f x ≤ t}).encard
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Fermat's theorem on a manifold](fermats-theorem-on-a-manifold.md)

## Informally uses

- [The Lusternik–Schnirelmann theorem](the-lusternik-schnirelmann-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.lsCategoryCount_sublevel_le_encard`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Morse/LusternikSchnirelmann.html#TauCeti.lsCategoryCount_sublevel_le_encard).

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

## Sources

- [Tau Ceti documentation: `TauCeti.lsCategoryCount_sublevel_le_encard`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Morse/LusternikSchnirelmann.html#TauCeti.lsCategoryCount_sublevel_le_encard)
- [Source of `TauCeti.lsCategoryCount_sublevel_le_encard` in TauCeti/Geometry/Manifold/Morse/LusternikSchnirelmann.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Geometry/Manifold/Morse/LusternikSchnirelmann.lean#L153)
