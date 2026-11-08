---
declaration: theorem
origin: cited
lean: TauCeti.ae_existsUnique_isPositive_isLittleO, ConvexOn.ae_existsUnique_isPositive_isLittleO, TauCeti.ae_existsUnique_isPositive_forall_mem_subdifferential_norm_sub_le
statement: formalized
proof: formalized
---

# Alexandrov's theorem

Let `f : E → EReal` be convex (convex real epigraph, never `⊥`) on a
finite-dimensional real inner product space with an additive Haar measure `μ`, and let
`F x = (f x).toReal`. At `μ`-almost every point `x` of the effective domain, `F` has a
second-order Taylor expansion
`F x' = F x + ⟪∇F x, x' - x⟫ + ⟪A (x' - x), x' - x⟫ / 2 + o(‖x' - x‖ ^ 2)`
with a positive operator `A`, the only positive operator giving such an expansion.

```lean
TauCeti.ae_existsUnique_isPositive_isLittleO.{u_1} {E : Type u_1} [NormedAddCommGroup E]
  [InnerProductSpace ℝ E] [FiniteDimensional ℝ E] [MeasurableSpace E] [BorelSpace E]
  {μ : MeasureTheory.Measure E} [μ.IsAddHaarMeasure] {f : E → EReal}
  (hf : Convex ℝ {p | f p.1 ≤ ↑p.2}) (hbot : ∀ (x : E), f x ≠ ⊥) :
  ∀ᵐ (x : E) ∂μ,
    f x ≠ ⊤ →
      ∃! A,
        A.IsPositive ∧
          (fun x' =>
              (f x').toReal - (f x).toReal -
                  inner ℝ (gradient (fun x' => (f x').toReal) x) (x' - x) -
                inner ℝ (A (x' - x)) (x' - x) / 2) =o[nhds x]
            fun x' => ‖x' - x‖ ^ 2
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Rademacher's theorem for locally Lipschitz functions](../../part-01/calculus/part-01/rademachers-theorem-for-locally-lipschitz-functi.md)
- [Sard's lemma on the flat stratum](../../part-01/analytic-heegaard-floer-homology/sards-lemma-on-the-flat-stratum.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.ae_existsUnique_isPositive_isLittleO`](https://taucetiproject.org/docs/TauCeti/Analysis/Convex/Alexandrov.html#TauCeti.ae_existsUnique_isPositive_isLittleO).

## Other forms

**Alexandrov's theorem for a real convex function.** Formalized in Tau Ceti as [`ConvexOn.ae_existsUnique_isPositive_isLittleO`](https://taucetiproject.org/docs/TauCeti/Analysis/Convex/Alexandrov.html#ConvexOn.ae_existsUnique_isPositive_isLittleO).

```lean
ConvexOn.ae_existsUnique_isPositive_isLittleO.{u_1} {E : Type u_1} [NormedAddCommGroup E]
  [InnerProductSpace ℝ E] [FiniteDimensional ℝ E] [MeasurableSpace E] [BorelSpace E]
  {μ : MeasureTheory.Measure E} [μ.IsAddHaarMeasure] {Ω : Set E} {u : E → ℝ} (hu : ConvexOn ℝ Ω u) :
  ∀ᵐ (x : E) ∂μ,
    x ∈ Ω →
      DifferentiableAt ℝ u x ∧
        ∃! A,
          A.IsPositive ∧
            (fun x' =>
                u x' - u x - inner ℝ (gradient u x) (x' - x) -
                  inner ℝ (A (x' - x)) (x' - x) / 2) =o[nhds x]
              fun x' => ‖x' - x‖ ^ 2
```

**Alexandrov's theorem for the subdifferential.** Formalized in Tau Ceti as [`TauCeti.ae_existsUnique_isPositive_forall_mem_subdifferential_norm_sub_le`](https://taucetiproject.org/docs/TauCeti/Analysis/Convex/Alexandrov.html#TauCeti.ae_existsUnique_isPositive_forall_mem_subdifferential_norm_sub_le).

```lean
TauCeti.ae_existsUnique_isPositive_forall_mem_subdifferential_norm_sub_le.{u_1} {E : Type u_1}
  [NormedAddCommGroup E] [InnerProductSpace ℝ E] [FiniteDimensional ℝ E] [MeasurableSpace E]
  [BorelSpace E] {μ : MeasureTheory.Measure E} [μ.IsAddHaarMeasure] {f : E → EReal}
  (hf : Convex ℝ {p | f p.1 ≤ ↑p.2}) (hbot : ∀ (x : E), f x ≠ ⊥) :
  ∀ᵐ (x : E) ∂μ,
    f x ≠ ⊤ →
      ∃! A,
        A.IsPositive ∧
          ∀ ε > 0,
            ∀ᶠ (x' : E) in nhds x,
              ∀ y' ∈ TauCeti.subdifferential (innerₗ E) f x',
                ‖y' - gradient (fun x' => (f x').toReal) x - A (x' - x)‖ ≤ ε * ‖x' - x‖
```

## Sources

- [Tau Ceti documentation: `TauCeti.ae_existsUnique_isPositive_isLittleO`](https://taucetiproject.org/docs/TauCeti/Analysis/Convex/Alexandrov.html#TauCeti.ae_existsUnique_isPositive_isLittleO)
- [Source of `TauCeti.ae_existsUnique_isPositive_isLittleO` in TauCeti/Analysis/Convex/Alexandrov.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Convex/Alexandrov.lean#L597)
