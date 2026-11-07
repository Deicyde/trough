---
declaration: theorem
origin: cited
lean: TauCeti.integral_posDef_multivariateGamma
statement: formalized
proof: formalized
---

# The multivariate Gamma integral

For `((p : ℝ) - 1) / 2 < a`, the integral of
`(det A) ^ (a - (p + 1) / 2) * exp (-trace A)` over the cone of positive-definite symmetric
`p × p` matrices, against `TauCeti.symmetricLebesgue p`, is `Γ_p(a)`.

```lean
TauCeti.integral_posDef_multivariateGamma {p : ℕ} {a : ℝ} (ha : (↑p - 1) / 2 < a) :
  ∫ (A : ↥(selfAdjoint.submodule ℝ (Matrix (Fin p) (Fin p) ℝ))) in {A | (↑A).PosDef},
      (↑A).det ^ (a - (↑p + 1) / 2) * Real.exp (-(↑A).trace) ∂TauCeti.symmetricLebesgue p =
    TauCeti.multivariateGamma p a
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.integral_posDef_multivariateGamma`](https://taucetiproject.org/docs/TauCeti/Analysis/SpecialFunctions/MultivariateGamma/Integral.html#TauCeti.integral_posDef_multivariateGamma).

## Sources

- [Tau Ceti documentation: `TauCeti.integral_posDef_multivariateGamma`](https://taucetiproject.org/docs/TauCeti/Analysis/SpecialFunctions/MultivariateGamma/Integral.html#TauCeti.integral_posDef_multivariateGamma)
- [Source of `TauCeti.integral_posDef_multivariateGamma` in TauCeti/Analysis/SpecialFunctions/MultivariateGamma/Integral.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/SpecialFunctions/MultivariateGamma/Integral.lean#L165)
- [Tau Ceti roadmap status: Standard probability distributions and their elementary theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/StandardDistributions/STATUS.md)
