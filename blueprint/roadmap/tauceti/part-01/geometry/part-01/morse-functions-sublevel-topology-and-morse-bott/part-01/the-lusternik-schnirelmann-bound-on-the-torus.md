---
declaration: theorem
origin: cited
lean: TauCeti.card_add_one_le_totalCriticalCount_torus, TauCeti.lsCategoryCount_univ_le_encard_criticalPoints_inter, TauCeti.lsCategoryCount_sublevel_le_encard
statement: formalized
proof: formalized
---

# The Lusternik–Schnirelmann bound on the torus

Every smooth function on the torus
`Tᵐ = ∀ i, AddCircle (p i)` has at least `m + 1` critical points, degenerate or not, since the
Lusternik–Schnirelmann count of `Tᵐ` is `m + 1`. For Morse functions the stronger bound `2ᵐ` holds
(`TauCeti.IsMorse.two_pow_card_le_totalCriticalCount_torus`).

```lean
TauCeti.card_add_one_le_totalCriticalCount_torus.{u_1} {ι : Type u_1} [Fintype ι] {p : ι → ℝ}
  [∀ (i : ι), Fact (0 < p i)] {f : ((i : ι) → AddCircle (p i)) → ℝ}
  (hf :
    ContMDiff (ModelWithCorners.pi fun x => modelWithCornersSelf ℝ ℝ) (modelWithCornersSelf ℝ ℝ)
      (↑⊤) f) :
  ↑(Fintype.card ι) + 1 ≤
    TauCeti.totalCriticalCount (ModelWithCorners.pi fun x => modelWithCornersSelf ℝ ℝ) f
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [A maximal integral curve confined to a compact set is defined for all time](../../geodesics-the-exponential-map-and-the-hopf-rinow/a-maximal-integral-curve-confined-to-a-compact-s.md)
- [Fermat's theorem on a manifold](fermats-theorem-on-a-manifold.md)
- [The Lusternik–Schnirelmann count of the torus `Tᵐ` is `m + 1`](the-lusternik-schnirelmann-count-of-the-torus-tm.md)

## Informally uses

- [The Lusternik–Schnirelmann theorem](the-lusternik-schnirelmann-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.card_add_one_le_totalCriticalCount_torus`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Morse/MinCriticalCount.html#TauCeti.card_add_one_le_totalCriticalCount_torus).

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

## Sources

- [Tau Ceti documentation: `TauCeti.card_add_one_le_totalCriticalCount_torus`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Morse/MinCriticalCount.html#TauCeti.card_add_one_le_totalCriticalCount_torus)
- [Source of `TauCeti.card_add_one_le_totalCriticalCount_torus` in TauCeti/Geometry/Manifold/Morse/MinCriticalCount.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Geometry/Manifold/Morse/MinCriticalCount.lean#L234)
