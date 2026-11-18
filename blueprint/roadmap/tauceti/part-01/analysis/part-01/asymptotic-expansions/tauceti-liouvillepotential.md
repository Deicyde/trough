---
declaration: def
origin: cited
lean: TauCeti.liouvillePotential
statement: formalized
---

# TauCeti.liouvillePotential

The potential after Liouville rescaling: the pulled-back potential plus the
correction coming from the second derivative of the inverse square-root factor.
This is the coefficient `ψ` of DLMF (2.8.4) when `q` is the lower-order potential.

```lean
TauCeti.liouvillePotential (z q : ℝ → ℝ) (ξ : ℝ) : ℝ
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.liouvillePotential`](https://taucetiproject.org/docs/TauCeti/Analysis/ODE/LiouvilleTransformation.html#TauCeti.liouvillePotential).

## Sources

- [Tau Ceti documentation: `TauCeti.liouvillePotential`](https://taucetiproject.org/docs/TauCeti/Analysis/ODE/LiouvilleTransformation.html#TauCeti.liouvillePotential)
- [Source of `TauCeti.liouvillePotential` in TauCeti/Analysis/ODE/LiouvilleTransformation.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/ODE/LiouvilleTransformation.lean#L128)
- [Tau Ceti roadmap status: Asymptotic expansions](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/AsymptoticExpansions/STATUS.md)
