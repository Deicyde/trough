---
declaration: theorem
origin: cited
lean: TauCeti.GeometryOfNumbers.ncard_inter_pi_closedBall_two_le_pow_mul_of_discreteTopology
statement: formalized
proof: formalized
---

# TauCeti.GeometryOfNumbers.ncard_inter_pi_closedBall_two_le_pow_mul_of_discreteTopology

Doubling for a discrete integral submodule, in particular a full `ZLattice`.
Compactness supplies the finiteness hypothesis of the measure-free subgroup estimate.

```lean
TauCeti.GeometryOfNumbers.ncard_inter_pi_closedBall_two_le_pow_mul_of_discreteTopology.{u_1}
  {ι : Type u_1} [Fintype ι] (r : ι → ℝ) (hr : ∀ (i : ι), 0 < r i) (L : Submodule ℤ (ι → ℂ))
  [DiscreteTopology ↥L] :
  ↑(↑L ∩ Set.univ.pi fun i => Metric.closedBall 0 (2 * r i)).ncard ≤
    49 ^ Fintype.card ι * ↑(↑L ∩ Set.univ.pi fun i => Metric.closedBall 0 (r i)).ncard
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.GeometryOfNumbers.ncard_inter_pi_closedBall_two_le_pow_mul_of_discreteTopology`](https://taucetiproject.org/docs/TauCeti/NumberTheory/GeometryOfNumbers/Doubling.html#TauCeti.GeometryOfNumbers.ncard_inter_pi_closedBall_two_le_pow_mul_of_discreteTopology).

## Sources

- [Tau Ceti documentation: `TauCeti.GeometryOfNumbers.ncard_inter_pi_closedBall_two_le_pow_mul_of_discreteTopology`](https://taucetiproject.org/docs/TauCeti/NumberTheory/GeometryOfNumbers/Doubling.html#TauCeti.GeometryOfNumbers.ncard_inter_pi_closedBall_two_le_pow_mul_of_discreteTopology)
- [Source of `TauCeti.GeometryOfNumbers.ncard_inter_pi_closedBall_two_le_pow_mul_of_discreteTopology` in TauCeti/NumberTheory/GeometryOfNumbers/Doubling.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/NumberTheory/GeometryOfNumbers/Doubling.lean#L335)
- [Tau Ceti roadmap status: Effective arithmetic bounds and geometry of numbers](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/Completed/EffectiveBounds/STATUS.md)
