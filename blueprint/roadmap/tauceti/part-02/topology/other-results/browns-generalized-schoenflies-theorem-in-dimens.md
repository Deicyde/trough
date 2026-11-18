---
declaration: theorem
origin: cited
lean: TauCeti.exists_homeomorph_closure_connectedComponentIn_compl_range_of_finrank_eq_one
statement: formalized
proof: formalized
---

# Brown's generalized Schoenflies theorem in dimension `1`

Let `σ` be an injective map from
the unit sphere `S⁰` of a real normed space `E` of dimension `1` into the unit sphere `S¹` of a
real normed space of dimension `2`, with image `Σ`. The closure of each connected component
of `S¹ ∖ Σ` is homeomorphic to the closed unit ball `D¹` of `E`, by a homeomorphism `h` which
inverts `σ` on `Σ` and carries exactly `Σ` onto the boundary sphere `S⁰` of `D¹`.

```lean
TauCeti.exists_homeomorph_closure_connectedComponentIn_compl_range_of_finrank_eq_one.{u_1, u_2}
  {E : Type u_1} {F : Type u_2} [NormedAddCommGroup E] [NormedSpace ℝ E] [NormedAddCommGroup F]
  [NormedSpace ℝ F] {σ : ↑(Metric.sphere 0 1) → ↑(Metric.sphere 0 1)}
  (hEF : Module.finrank ℝ F = Module.finrank ℝ E + 1) (hE : Module.finrank ℝ E = 1)
  (hσ : Function.Injective σ) {y : ↑(Metric.sphere 0 1)} (hy : y ∉ Set.range σ) :
  ∃ h,
    (∀ (z : ↑(closure (connectedComponentIn (Set.range σ)ᶜ y))) (x : ↑(Metric.sphere 0 1)),
        ↑z = σ x → ↑(h z) = ↑x) ∧
      ∀ (z : ↑(closure (connectedComponentIn (Set.range σ)ᶜ y))),
        ↑(h z) ∈ Metric.sphere 0 1 ↔ ↑z ∈ Set.range σ
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.exists_homeomorph_closure_connectedComponentIn_compl_range_of_finrank_eq_one`](https://taucetiproject.org/docs/TauCeti/Topology/Circle/Schoenflies.html#TauCeti.exists_homeomorph_closure_connectedComponentIn_compl_range_of_finrank_eq_one).

## Sources

- [Tau Ceti documentation: `TauCeti.exists_homeomorph_closure_connectedComponentIn_compl_range_of_finrank_eq_one`](https://taucetiproject.org/docs/TauCeti/Topology/Circle/Schoenflies.html#TauCeti.exists_homeomorph_closure_connectedComponentIn_compl_range_of_finrank_eq_one)
- [Source of `TauCeti.exists_homeomorph_closure_connectedComponentIn_compl_range_of_finrank_eq_one` in TauCeti/Topology/Circle/Schoenflies.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Topology/Circle/Schoenflies.lean#L418)
