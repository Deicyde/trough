---
declaration: theorem
origin: cited
lean: TauCeti.IsNashAt.exists_isNashAt_eventually_eq_zero_iff
statement: formalized
proof: formalized
---

# The Nash implicit root theorem

A Nash scalar equation with a simple zero admits a
Nash root germ in the parameter variables. Near the given point its zero set is exactly the
graph of this root. No polynomial equation or global semialgebraic domain is required.

```lean
TauCeti.IsNashAt.exists_isNashAt_eventually_eq_zero_iff.{u_1} {σ : Type u_1} [Fintype σ]
  {f : (σ ⊕ Unit → ℝ) → ℝ} {x : σ → ℝ} {z : ℝ} (hf : TauCeti.IsNashAt f (Sum.elim x fun x => z))
  (hz : f (Sum.elim x fun x => z) = 0) (hd : deriv (fun t => f (Sum.elim x fun x => t)) z ≠ 0) :
  ∃ g,
    TauCeti.IsNashAt g x ∧
      g x = z ∧
        (∀ᶠ (y : σ → ℝ) in nhds x, f (Sum.elim y fun x => g y) = 0) ∧
          ∀ᶠ (p : σ ⊕ Unit → ℝ) in nhds (Sum.elim x fun x => z),
            f p = 0 ↔ g (p ∘ Sum.inl) = p (Sum.inr ())
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The analytic implicit root theorem](../../../analysis/part-01/analytic/the-analytic-implicit-root-theorem.md)
- [The local Nash graph criterion](the-local-nash-graph-criterion.md)
- [The Tarski–Seidenberg theorem](../real-algebraic-geometry-sign-determination-and-c/the-tarski-seidenberg-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.IsNashAt.exists_isNashAt_eventually_eq_zero_iff`](https://taucetiproject.org/docs/TauCeti/Geometry/RealAlgebraic/Nash/Implicit.html#TauCeti.IsNashAt.exists_isNashAt_eventually_eq_zero_iff).

## Sources

- [Tau Ceti documentation: `TauCeti.IsNashAt.exists_isNashAt_eventually_eq_zero_iff`](https://taucetiproject.org/docs/TauCeti/Geometry/RealAlgebraic/Nash/Implicit.html#TauCeti.IsNashAt.exists_isNashAt_eventually_eq_zero_iff)
- [Source of `TauCeti.IsNashAt.exists_isNashAt_eventually_eq_zero_iff` in TauCeti/Geometry/RealAlgebraic/Nash/Implicit.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Geometry/RealAlgebraic/Nash/Implicit.lean#L98)
