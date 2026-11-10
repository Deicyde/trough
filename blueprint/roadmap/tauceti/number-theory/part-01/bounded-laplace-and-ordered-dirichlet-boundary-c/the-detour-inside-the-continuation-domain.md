---
declaration: theorem
origin: cited
lean: TauCeti.LSeries.exists_convex_newmanDetour_subset
statement: formalized
proof: formalized
---

# The detour inside the continuation domain

If `Ω` is open and contains the closed
half-plane `0 ≤ re z`, then for some `δ > 0` the right semicircle of radius `R` and the detour
`newmanDetour R δ` lie in a common open convex subset of `Ω`.

```lean
TauCeti.LSeries.exists_convex_newmanDetour_subset {R : ℝ} {Ω : Set ℂ} (hΩ : IsOpen Ω)
  (hcover : {z | 0 ≤ z.re} ⊆ Ω) (hR : 0 ≤ R) :
  ∃ δ > 0,
    ∃ U ⊆ Ω,
      IsOpen U ∧
        Convex ℝ U ∧
          (∀ θ ∈ Set.Icc (-Real.pi / 2) (Real.pi / 2), circleMap 0 R θ ∈ U) ∧
            ∀ s ∈ Set.Icc (-1) 1, TauCeti.LSeries.newmanDetour R δ s ∈ U
```

## Depends on

- [Newman's left detour](newmans-left-detour.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.LSeries.exists_convex_newmanDetour_subset`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LSeries/Newman/Detour.html#TauCeti.LSeries.exists_convex_newmanDetour_subset).

## Sources

- [Tau Ceti documentation: `TauCeti.LSeries.exists_convex_newmanDetour_subset`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LSeries/Newman/Detour.html#TauCeti.LSeries.exists_convex_newmanDetour_subset)
- [Source of `TauCeti.LSeries.exists_convex_newmanDetour_subset` in TauCeti/NumberTheory/LSeries/Newman/Detour.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/LSeries/Newman/Detour.lean#L140)
- [Tau Ceti roadmap status: Bounded Laplace and ordered Dirichlet boundary convergence](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/TauberianBoundaryConvergence/STATUS.md)
