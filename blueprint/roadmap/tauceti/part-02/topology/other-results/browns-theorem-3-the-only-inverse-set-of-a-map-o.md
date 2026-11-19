---
declaration: theorem
origin: cited
lean: TauCeti.isCellularSet_closedBall_inter_preimage_of_finrank_eq
statement: formalized
proof: formalized
---

# Brown's Theorem 3: the only inverse set of a map of a cell is cellular

Let `E` and `F`
be finite-dimensional real normed spaces of the same dimension and `f : E → F` a map continuous on
the closed unit ball, injective on it away from the nonempty fibre
`M = closedBall 0 1 ∩ f ⁻¹' {p}`, which lies in the open unit ball. Then `M` is cellular.

```lean
TauCeti.isCellularSet_closedBall_inter_preimage_of_finrank_eq.{u_1, u_2} {E : Type u_1}
  {F : Type u_2} [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E]
  [NormedAddCommGroup F] [NormedSpace ℝ F] [FiniteDimensional ℝ F] {f : E → F} {p : F}
  (hEF : Module.finrank ℝ E = Module.finrank ℝ F) (hf : ContinuousOn f (Metric.closedBall 0 1))
  (hinj : Set.InjOn f (Metric.closedBall 0 1 \ f ⁻¹' {p}))
  (hM : Metric.closedBall 0 1 ∩ f ⁻¹' {p} ⊆ Metric.ball 0 1) (hp : p ∈ f '' Metric.closedBall 0 1) :
  TauCeti.IsCellularSet E (Metric.closedBall 0 1 ∩ f ⁻¹' {p})
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Brown's Theorem 0, for one inverse set](../../../part-01/algebraic-topology/singular/browns-theorem-0-for-one-inverse-set.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.isCellularSet_closedBall_inter_preimage_of_finrank_eq`](https://taucetiproject.org/docs/TauCeti/Topology/CellularSet/InverseSet/Normed.html#TauCeti.isCellularSet_closedBall_inter_preimage_of_finrank_eq).

## Sources

- [Tau Ceti documentation: `TauCeti.isCellularSet_closedBall_inter_preimage_of_finrank_eq`](https://taucetiproject.org/docs/TauCeti/Topology/CellularSet/InverseSet/Normed.html#TauCeti.isCellularSet_closedBall_inter_preimage_of_finrank_eq)
- [Source of `TauCeti.isCellularSet_closedBall_inter_preimage_of_finrank_eq` in TauCeti/Topology/CellularSet/InverseSet/Normed.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Topology/CellularSet/InverseSet/Normed.lean#L135)
