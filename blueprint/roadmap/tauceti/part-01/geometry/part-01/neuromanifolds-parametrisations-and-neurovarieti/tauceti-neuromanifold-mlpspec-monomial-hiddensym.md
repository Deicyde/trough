---
declaration: theorem
origin: cited
lean: TauCeti.Neuromanifold.MLPSpec.monomial_hiddenSymmetrySetoid_le_parameterSetoid
statement: formalized
proof: formalized
---

# TauCeti.Neuromanifold.MLPSpec.monomial_hiddenSymmetrySetoid_le_parameterSetoid

The hidden-neuron symmetries of a monomial MLP preserve its bias-free realization.

```lean
TauCeti.Neuromanifold.MLPSpec.monomial_hiddenSymmetrySetoid_le_parameterSetoid.{u_1} {K : Type u_1}
  {L : ℕ} [CommSemiring K] (d : Fin (L + 2) → ℕ) (r : Fin L → ℕ) :
  (TauCeti.Neuromanifold.MLPSpec.monomial d r).hiddenSymmetrySetoid r ≤
    TauCeti.Neuromanifold.parameterSetoid
      (TauCeti.Neuromanifold.MLPSpec.monomial d r).realizeWeights
```

## Depends on

- [TauCeti.Neuromanifold.MLPSpec](tauceti-neuromanifold-mlpspec.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Neuromanifold.MLPSpec.monomial_hiddenSymmetrySetoid_le_parameterSetoid`](https://taucetiproject.org/docs/TauCeti/Geometry/Neuromanifold/MLP/Symmetry.html#TauCeti.Neuromanifold.MLPSpec.monomial_hiddenSymmetrySetoid_le_parameterSetoid).

## Sources

- [Tau Ceti documentation: `TauCeti.Neuromanifold.MLPSpec.monomial_hiddenSymmetrySetoid_le_parameterSetoid`](https://taucetiproject.org/docs/TauCeti/Geometry/Neuromanifold/MLP/Symmetry.html#TauCeti.Neuromanifold.MLPSpec.monomial_hiddenSymmetrySetoid_le_parameterSetoid)
- [Source of `TauCeti.Neuromanifold.MLPSpec.monomial_hiddenSymmetrySetoid_le_parameterSetoid` in TauCeti/Geometry/Neuromanifold/MLP/Symmetry.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Geometry/Neuromanifold/MLP/Symmetry.lean#L324)
- [Tau Ceti roadmap status: Neuromanifolds, parametrisations, and neurovarieties](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/Neuromanifolds/STATUS.md)
