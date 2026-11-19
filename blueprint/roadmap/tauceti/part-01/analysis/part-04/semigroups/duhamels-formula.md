---
declaration: theorem
origin: cited
lean: TauCeti.Semigroups.StronglyContinuousSemigroup.isForcedMildSolution_realOperator_add_duhamel
statement: formalized
proof: formalized
---

# Duhamel's formula

For a forcing term `F` locally integrable on `[0, ∞)`, the function
`t ↦ S(t) x + ∫_{(0,t]} S(t - s) F(s) ds` is a mild solution of `u' = A u + F`, `u(0) = x`.

```lean
TauCeti.Semigroups.StronglyContinuousSemigroup.isForcedMildSolution_realOperator_add_duhamel.{u_1}
  {X : Type u_1} [NormedAddCommGroup X] [NormedSpace ℝ X]
  (S : TauCeti.Semigroups.StronglyContinuousSemigroup X) {F : ℝ → X} [CompleteSpace X]
  (hF : MeasureTheory.LocallyIntegrableOn F (Set.Ici 0) MeasureTheory.volume) (x : X) :
  TauCeti.Semigroups.IsForcedMildSolution S.generator F x fun t =>
    (S.realOperator t) x + S.duhamel F t
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.Semigroups.StronglyContinuousSemigroup.isForcedMildSolution_realOperator_add_duhamel`](https://taucetiproject.org/docs/TauCeti/Analysis/Semigroups/CauchyProblem/Inhomogeneous.html#TauCeti.Semigroups.StronglyContinuousSemigroup.isForcedMildSolution_realOperator_add_duhamel).

## Sources

- [Tau Ceti documentation: `TauCeti.Semigroups.StronglyContinuousSemigroup.isForcedMildSolution_realOperator_add_duhamel`](https://taucetiproject.org/docs/TauCeti/Analysis/Semigroups/CauchyProblem/Inhomogeneous.html#TauCeti.Semigroups.StronglyContinuousSemigroup.isForcedMildSolution_realOperator_add_duhamel)
- [Source of `TauCeti.Semigroups.StronglyContinuousSemigroup.isForcedMildSolution_realOperator_add_duhamel` in TauCeti/Analysis/Semigroups/CauchyProblem/Inhomogeneous.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/Semigroups/CauchyProblem/Inhomogeneous.lean#L435)
