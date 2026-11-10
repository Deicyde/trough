---
declaration: theorem
origin: cited
lean: TauCeti.ae_subsingleton_setOf_mem_contactSet
statement: formalized
proof: formalized
---

# The twist theorem

If the cost is differentiable in its first variable at contact
partners and `y ↦ Dₓ c (x, y)` is injective among differentiable sections at almost every `x`,
and a dual feasible pair has a first potential finite near, and differentiable at,
`μ`-almost every point, then the contact fibres
`{y | (x, y) ∈ contactSet c φ ψ}` are subsingletons for `μ`-almost every `x`. Combined with
`TauCeti.IsCoupling.ae_exists_condKernel_eq_dirac`, a finite coupling of `μ` concentrated on the
contact set has, for `μ`-almost every `x`, the Dirac mass at the unique contact partner of `x`
as its conditional law.

```lean
TauCeti.ae_subsingleton_setOf_mem_contactSet.{u_1, u_2} {E : Type u_1} {Y : Type u_2}
  [NormedAddCommGroup E] [NormedSpace ℝ E] {c : E × Y → ℝ} {φ : E → EReal} {ψ : Y → EReal}
  [MeasurableSpace E] (μ : MeasureTheory.Measure E)
  (hfeas : ∀ (x : E) (y : Y), φ x + ψ y ≤ ↑(c (x, y)))
  (hφ :
    ∀ᵐ (x : E) ∂μ,
      (∀ᶠ (x' : E) in nhds x, φ x' ≠ ⊥) ∧ DifferentiableAt ℝ (fun x' => (φ x').toReal) x)
  (hc :
    ∀ᵐ (x : E) ∂μ,
      ∀ (y : Y), (x, y) ∈ TauCeti.contactSet c φ ψ → DifferentiableAt ℝ (fun x' => c (x', y)) x)
  (htwist :
    ∀ᵐ (x : E) ∂μ,
      Set.InjOn (fun y => fderiv ℝ (fun x' => c (x', y)) x)
        {y | DifferentiableAt ℝ (fun x' => c (x', y)) x}) :
  ∀ᵐ (x : E) ∂μ, {y | (x, y) ∈ TauCeti.contactSet c φ ψ}.Subsingleton
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The twist theorem at a point](the-twist-theorem-at-a-point.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.ae_subsingleton_setOf_mem_contactSet`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/OptimalTransport/Twist/Basic.html#TauCeti.ae_subsingleton_setOf_mem_contactSet).

## Sources

- [Tau Ceti documentation: `TauCeti.ae_subsingleton_setOf_mem_contactSet`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/OptimalTransport/Twist/Basic.html#TauCeti.ae_subsingleton_setOf_mem_contactSet)
- [Source of `TauCeti.ae_subsingleton_setOf_mem_contactSet` in TauCeti/MeasureTheory/OptimalTransport/Twist/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/MeasureTheory/OptimalTransport/Twist/Basic.lean#L237)
