---
declaration: theorem
origin: cited
lean: TauCeti.exists_cost_eq_finiteMultiDualValue
statement: formalized
proof: formalized
---

# Finite multi-marginal Kantorovich duality

For a nonempty finite family of finite
spaces, the primal and dual problems have the same value and both attain it.

```lean
TauCeti.exists_cost_eq_finiteMultiDualValue.{u, v} {ι : Type u} {X : ι → Type v} [Fintype ι]
  [(i : ι) → Fintype (X i)] (c : ((i : ι) → X i) → ℝ) (μ : (i : ι) → PMF (X i)) [Nonempty ι] :
  ∃ π φ,
    (∀ (σ : TauCeti.FiniteMultiCoupling μ),
        TauCeti.FiniteMultiCoupling.cost c π ≤ TauCeti.FiniteMultiCoupling.cost c σ) ∧
      TauCeti.FiniteMultiDualFeasible c φ ∧
        TauCeti.FiniteMultiCoupling.cost c π = TauCeti.finiteMultiDualValue μ φ
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.exists_cost_eq_finiteMultiDualValue`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/OptimalTransport/MultiMarginal/Finite/Duality.html#TauCeti.exists_cost_eq_finiteMultiDualValue).

## Sources

- [Tau Ceti documentation: `TauCeti.exists_cost_eq_finiteMultiDualValue`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/OptimalTransport/MultiMarginal/Finite/Duality.html#TauCeti.exists_cost_eq_finiteMultiDualValue)
- [Source of `TauCeti.exists_cost_eq_finiteMultiDualValue` in TauCeti/MeasureTheory/OptimalTransport/MultiMarginal/Finite/Duality.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/MeasureTheory/OptimalTransport/MultiMarginal/Finite/Duality.lean#L751)
