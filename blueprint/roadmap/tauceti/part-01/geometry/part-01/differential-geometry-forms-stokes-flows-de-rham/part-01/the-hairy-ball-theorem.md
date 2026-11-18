---
declaration: theorem
origin: cited
lean: TauCeti.exists_eq_zero_of_inner_eq_zero, TauCeti.exists_eq_zero_of_continuous_section, TauCeti.exists_eq_zero_of_continuous_of_inner_eq_zero
statement: formalized
proof: formalized
---

# The hairy ball theorem

A continuous tangent vector field on an even-dimensional unit
sphere vanishes somewhere: if `v : E → E` is continuous on the unit sphere `Sⁿ` of a real inner
product space `E` of dimension `n + 1`, with `n` even, and `⟪v x, x⟫ = 0` for `x ∈ Sⁿ`, then
`v x = 0` for some `x ∈ Sⁿ`.

```lean
TauCeti.exists_eq_zero_of_inner_eq_zero.{u_1} {E : Type u_1} [NormedAddCommGroup E]
  [InnerProductSpace ℝ E] {n : ℕ} [Fact (Module.finrank ℝ E = n + 1)] (hn : Even n) {v : E → E}
  (hv : ContinuousOn v (Metric.sphere 0 1)) (ht : ∀ x ∈ Metric.sphere 0 1, inner ℝ (v x) x = 0) :
  ∃ x ∈ Metric.sphere 0 1, v x = 0
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Homotopy invariance of the degree](homotopy-invariance-of-the-degree.md)
- [The inverse function theorem for a converging family](../../../../analysis/part-03/calculus/part-01/the-inverse-function-theorem-for-a-converging-fa.md)
- [Smooth tubular neighbourhood theorem](../../../part-02/manifold/part-04/smooth-tubular-neighbourhood-theorem.md)
- [TauCeti.degree](tauceti-degree.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.exists_eq_zero_of_inner_eq_zero`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Degree/HairyBall.html#TauCeti.exists_eq_zero_of_inner_eq_zero).

## Other forms

**The hairy ball theorem, section form.** Formalized in Tau Ceti as [`TauCeti.exists_eq_zero_of_continuous_section`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Degree/HairyBall.html#TauCeti.exists_eq_zero_of_continuous_section).

```lean
TauCeti.exists_eq_zero_of_continuous_section.{u_1} {E : Type u_1} [NormedAddCommGroup E]
  [InnerProductSpace ℝ E] {n : ℕ} [Fact (Module.finrank ℝ E = n + 1)] (hn : Even n)
  {V :
    (x : ↑(Metric.sphere 0 1)) → TangentSpace (modelWithCornersSelf ℝ (EuclideanSpace ℝ (Fin n))) x}
  (hV : Continuous fun x => ⟨x, V x⟩) : ∃ x, V x = 0
```

**The hairy ball theorem, sphere-domain form.** Formalized in Tau Ceti as [`TauCeti.exists_eq_zero_of_continuous_of_inner_eq_zero`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Degree/HairyBall.html#TauCeti.exists_eq_zero_of_continuous_of_inner_eq_zero).

```lean
TauCeti.exists_eq_zero_of_continuous_of_inner_eq_zero.{u_1} {E : Type u_1} [NormedAddCommGroup E]
  [InnerProductSpace ℝ E] {n : ℕ} [Fact (Module.finrank ℝ E = n + 1)] (hn : Even n)
  {v : ↑(Metric.sphere 0 1) → E} (hv : Continuous v)
  (ht : ∀ (x : ↑(Metric.sphere 0 1)), inner ℝ (v x) ↑x = 0) : ∃ x, v x = 0
```

## Sources

- [Tau Ceti documentation: `TauCeti.exists_eq_zero_of_inner_eq_zero`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Degree/HairyBall.html#TauCeti.exists_eq_zero_of_inner_eq_zero)
- [Source of `TauCeti.exists_eq_zero_of_inner_eq_zero` in TauCeti/Geometry/Manifold/Degree/HairyBall.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Geometry/Manifold/Degree/HairyBall.lean#L142)
