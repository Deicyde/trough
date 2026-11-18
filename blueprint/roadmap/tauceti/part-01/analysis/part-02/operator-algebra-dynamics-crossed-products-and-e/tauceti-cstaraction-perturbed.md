---
declaration: def
origin: cited
lean: TauCeti.CStarAction.perturbed
statement: formalized
---

# TauCeti.CStarAction.perturbed

The **perturbed dynamics** of `α` by a self-adjoint `P ∈ A`:
`α^P_t(a) = Γ t α_t(a) (Γ t)⋆`, where `Γ` is the perturbation cocycle of `P`. It is a group
of automorphisms by the cocycle identity, and its generator is `δ + i[P, ·]`, where `δ` is the
generator of `α` (`generator_perturbed`).

```lean
TauCeti.CStarAction.perturbed.{u_1} {A : Type u_1} [NonUnitalCStarAlgebra A]
  (α : TauCeti.CStarAction (Multiplicative ℝ) A) {P : A} (hP : IsSelfAdjoint P) :
  TauCeti.CStarAction (Multiplicative ℝ) A
```

## Depends on

- [TauCeti.dysonSeries](tauceti-dysonseries.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.CStarAction.perturbed`](https://taucetiproject.org/docs/TauCeti/Analysis/CStarAlgebra/Action/Perturbation.html#TauCeti.CStarAction.perturbed).

## Sources

- [Tau Ceti documentation: `TauCeti.CStarAction.perturbed`](https://taucetiproject.org/docs/TauCeti/Analysis/CStarAlgebra/Action/Perturbation.html#TauCeti.CStarAction.perturbed)
- [Source of `TauCeti.CStarAction.perturbed` in TauCeti/Analysis/CStarAlgebra/Action/Perturbation.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/CStarAlgebra/Action/Perturbation.lean#L188)
- [Tau Ceti roadmap status: Operator-algebra dynamics, crossed products, and equilibrium](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/OperatorAlgebraDynamics/STATUS.md)
