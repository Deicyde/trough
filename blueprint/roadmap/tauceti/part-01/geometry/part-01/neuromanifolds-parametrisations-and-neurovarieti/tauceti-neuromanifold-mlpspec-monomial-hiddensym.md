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
- [Source of `TauCeti.Neuromanifold.MLPSpec.monomial_hiddenSymmetrySetoid_le_parameterSetoid` in TauCeti/Geometry/Neuromanifold/MLP/Symmetry.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Geometry/Neuromanifold/MLP/Symmetry.lean#L324)
- [Tau Ceti roadmap status: Neuromanifolds, parametrisations, and neurovarieties](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/Neuromanifolds/STATUS.md)
