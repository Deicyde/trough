---
declaration: theorem
origin: cited
lean: AnalyticOnNhd.exists_complexification_pi
statement: formalized
proof: formalized
---

# Complexification of a real analytic map on an open set

A map from `ι → ℝ` to `κ → ℝ`,
with `ι` and `κ` finite, that is analytic on an open set `U` extends to a map
`F : (ι → ℂ) → (κ → ℂ)` that is complex analytic on an open set `W` whose real points are exactly
those of `U`. The set `W` is invariant under complex conjugation, `F` agrees with `f` at the real
points of `U`, and `F` commutes with complex conjugation.

```lean
AnalyticOnNhd.exists_complexification_pi.{u_1, u_2} {ι : Type u_1} {κ : Type u_2} [Fintype ι]
  [Fintype κ] {f : (ι → ℝ) → κ → ℝ} {U : Set (ι → ℝ)} (hf : AnalyticOnNhd ℝ f U) (hU : IsOpen U) :
  ∃ W,
    IsOpen W ∧
      (∀ (x : ι → ℝ), (fun i => ↑(x i)) ∈ W ↔ x ∈ U) ∧
        (∀ (z : ι → ℂ), star z ∈ W ↔ z ∈ W) ∧
          ∃ F,
            AnalyticOnNhd ℂ F W ∧
              (∀ x ∈ U, (F fun i => ↑(x i)) = fun k => ↑(f x k)) ∧
                ∀ (z : ι → ℂ), F (star z) = star (F z)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`AnalyticOnNhd.exists_complexification_pi`](https://taucetiproject.org/docs/TauCeti/Analysis/Analytic/Complexification/Neighborhood.html#AnalyticOnNhd.exists_complexification_pi).

## Sources

- [Tau Ceti documentation: `AnalyticOnNhd.exists_complexification_pi`](https://taucetiproject.org/docs/TauCeti/Analysis/Analytic/Complexification/Neighborhood.html#AnalyticOnNhd.exists_complexification_pi)
- [Source of `AnalyticOnNhd.exists_complexification_pi` in TauCeti/Analysis/Analytic/Complexification/Neighborhood.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Analytic/Complexification/Neighborhood.lean#L140)
- [Tau Ceti roadmap status: Real-analytic geometry and semianalytic triangulation](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/RealAnalyticGeometry/STATUS.md)
