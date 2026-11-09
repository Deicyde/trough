---
declaration: theorem
origin: cited
lean: TauCeti.subsingleton_setOf_mem_contactSet
statement: formalized
proof: formalized
---

# The twist theorem at a point

Suppose the cost is twisted at `x`: the map
`y ↦ Dₓ c (x, y)` is injective on the set of `y` for which the section `c (·, y)` is
differentiable at `x`. If the potential is differentiable at `x`, finite near `x`, and satisfies
the dual constraint near `x`, and the cost sections of the contact partners of `x` are
differentiable at `x`, then `x` has at most one contact partner.

```lean
TauCeti.subsingleton_setOf_mem_contactSet.{u_1, u_2} {E : Type u_1} {Y : Type u_2}
  [NormedAddCommGroup E] [NormedSpace ℝ E] {c : E × Y → ℝ} {φ : E → EReal} {ψ : Y → EReal} {x : E}
  (hfeas : ∀ (y : Y), ∀ᶠ (x' : E) in nhds x, φ x' + ψ y ≤ ↑(c (x', y)))
  (hfin : ∀ᶠ (x' : E) in nhds x, φ x' ≠ ⊥) (hφ : DifferentiableAt ℝ (fun x' => (φ x').toReal) x)
  (hc : ∀ (y : Y), (x, y) ∈ TauCeti.contactSet c φ ψ → DifferentiableAt ℝ (fun x' => c (x', y)) x)
  (htwist :
    Set.InjOn (fun y => fderiv ℝ (fun x' => c (x', y)) x)
      {y | DifferentiableAt ℝ (fun x' => c (x', y)) x}) :
  {y | (x, y) ∈ TauCeti.contactSet c φ ψ}.Subsingleton
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.subsingleton_setOf_mem_contactSet`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/OptimalTransport/Twist/Basic.html#TauCeti.subsingleton_setOf_mem_contactSet).

## Sources

- [Tau Ceti documentation: `TauCeti.subsingleton_setOf_mem_contactSet`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/OptimalTransport/Twist/Basic.html#TauCeti.subsingleton_setOf_mem_contactSet)
- [Source of `TauCeti.subsingleton_setOf_mem_contactSet` in TauCeti/MeasureTheory/OptimalTransport/Twist/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/MeasureTheory/OptimalTransport/Twist/Basic.lean#L155)
