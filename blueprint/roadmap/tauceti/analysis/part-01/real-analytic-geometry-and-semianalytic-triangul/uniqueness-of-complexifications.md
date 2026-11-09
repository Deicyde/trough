---
declaration: theorem
origin: cited
lean: AnalyticOnNhd.exists_eqOn_of_forall_real
statement: formalized
proof: formalized
---

# Uniqueness of complexifications

Two complex analytic functions of finitely many variables
on an open neighborhood `W` of the real points of an open set `U`, agreeing at those real points,
agree on a smaller open set `V ⊆ W` that is invariant under complex conjugation and whose real
points are exactly those of `U`.

```lean
AnalyticOnNhd.exists_eqOn_of_forall_real.{u_1, u_3} {ι : Type u_1} [Fintype ι] {E : Type u_3}
  [NormedAddCommGroup E] [NormedSpace ℂ E] {F G : (ι → ℂ) → E} {U : Set (ι → ℝ)} {W : Set (ι → ℂ)}
  (hF : AnalyticOnNhd ℂ F W) (hG : AnalyticOnNhd ℂ G W) (hU : IsOpen U) (hW : IsOpen W)
  (hUW : ∀ x ∈ U, (fun i => ↑(x i)) ∈ W) (hFG : ∀ x ∈ U, (F fun i => ↑(x i)) = G fun i => ↑(x i)) :
  ∃ V ⊆ W,
    IsOpen V ∧
      (∀ (x : ι → ℝ), (fun i => ↑(x i)) ∈ V ↔ x ∈ U) ∧
        (∀ (z : ι → ℂ), star z ∈ V ↔ z ∈ V) ∧ Set.EqOn F G V
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Identity theorem on the real points](identity-theorem-on-the-real-points.md)

## Lean

Formalized in Tau Ceti as [`AnalyticOnNhd.exists_eqOn_of_forall_real`](https://taucetiproject.org/docs/TauCeti/Analysis/Analytic/Complexification/Neighborhood.html#AnalyticOnNhd.exists_eqOn_of_forall_real).

## Sources

- [Tau Ceti documentation: `AnalyticOnNhd.exists_eqOn_of_forall_real`](https://taucetiproject.org/docs/TauCeti/Analysis/Analytic/Complexification/Neighborhood.html#AnalyticOnNhd.exists_eqOn_of_forall_real)
- [Source of `AnalyticOnNhd.exists_eqOn_of_forall_real` in TauCeti/Analysis/Analytic/Complexification/Neighborhood.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Analytic/Complexification/Neighborhood.lean#L154)
- [Tau Ceti roadmap status: Real-analytic geometry and semianalytic triangulation](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/RealAnalyticGeometry/STATUS.md)
