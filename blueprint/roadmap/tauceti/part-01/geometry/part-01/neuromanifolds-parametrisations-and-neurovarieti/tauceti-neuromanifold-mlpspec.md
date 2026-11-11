---
declaration: structure
origin: cited
lean: TauCeti.Neuromanifold.MLPSpec
statement: formalized
---

# TauCeti.Neuromanifold.MLPSpec

A multilayer perceptron specification of depth `L`: widths `width i` for the layers
`0 ≤ i ≤ L`, and an activation `activation j` for the hidden layer `j + 1`, for `j < L - 1`.
The output layer carries no activation.

```lean
TauCeti.Neuromanifold.MLPSpec.{u_1} (K : Type u_1) (L : ℕ) : Type u_1
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.Neuromanifold.MLPSpec`](https://taucetiproject.org/docs/TauCeti/Geometry/Neuromanifold/MLP/Basic.html#TauCeti.Neuromanifold.MLPSpec).

## Sources

- [Tau Ceti documentation: `TauCeti.Neuromanifold.MLPSpec`](https://taucetiproject.org/docs/TauCeti/Geometry/Neuromanifold/MLP/Basic.html#TauCeti.Neuromanifold.MLPSpec)
- [Source of `TauCeti.Neuromanifold.MLPSpec` in TauCeti/Geometry/Neuromanifold/MLP/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Geometry/Neuromanifold/MLP/Basic.lean#L53)
- [Tau Ceti roadmap status: Neuromanifolds, parametrisations, and neurovarieties](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/Neuromanifolds/STATUS.md)
