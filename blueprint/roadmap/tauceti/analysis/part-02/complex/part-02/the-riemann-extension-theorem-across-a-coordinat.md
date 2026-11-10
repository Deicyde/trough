---
declaration: theorem
origin: cited
lean: TauCeti.exists_analyticOnNhd_prod_eqOn
statement: formalized
proof: formalized
---

# The Riemann extension theorem across a coordinate hyperplane

Let `U ⊆ V` and `s ⊆ ℂ` be
open. If `f` is analytic on `U × (s \ {c})` and, when `c ∈ s`, each slice `z ↦ f (w, z)`, for
`w ∈ U`, is bounded on a punctured neighbourhood of `c`, then some `g` analytic on `U × s` agrees
with `f` on `U × (s \ {c})`. Such a `g` is unique on `U × s` by
`eqOn_prod_of_eqOn_prod_diff_singleton`.

```lean
TauCeti.exists_analyticOnNhd_prod_eqOn.{u_1, u_2} {E : Type u_1} [NormedAddCommGroup E]
  [NormedSpace ℂ E] [CompleteSpace E] {V : Type u_2} [NormedAddCommGroup V] [NormedSpace ℂ V]
  {f : V × ℂ → E} {U : Set V} {s : Set ℂ} {c : ℂ} [FiniteDimensional ℂ V] (hU : IsOpen U)
  (hs : IsOpen s) (hf : AnalyticOnNhd ℂ f (U ×ˢ (s \ {c})))
  (hb : c ∈ s → ∀ w ∈ U, ∃ t ∈ nhds c, BddAbove ((norm ∘ fun z => f (w, z)) '' (t \ {c}))) :
  ∃ g, AnalyticOnNhd ℂ g (U ×ˢ s) ∧ Set.EqOn g f (U ×ˢ (s \ {c}))
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Osgood's lemma](../../../../geometry/part-01/complex-manifolds-dolbeault-theory-and-kahler-ge/osgoods-lemma.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.exists_analyticOnNhd_prod_eqOn`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/RemovableSingularity.html#TauCeti.exists_analyticOnNhd_prod_eqOn).

## Sources

- [Tau Ceti documentation: `TauCeti.exists_analyticOnNhd_prod_eqOn`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/RemovableSingularity.html#TauCeti.exists_analyticOnNhd_prod_eqOn)
- [Source of `TauCeti.exists_analyticOnNhd_prod_eqOn` in TauCeti/Analysis/Complex/RemovableSingularity.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Complex/RemovableSingularity.lean#L91)
