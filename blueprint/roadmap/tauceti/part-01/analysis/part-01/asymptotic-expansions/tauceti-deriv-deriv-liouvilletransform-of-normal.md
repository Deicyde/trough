---
declaration: theorem
origin: cited
lean: TauCeti.deriv_deriv_liouvilleTransform_of_normalized
statement: formalized
proof: formalized
---

# TauCeti.deriv_deriv_liouvilleTransform_of_normalized

The normalized Liouville transformation (Case I): if `z'² f ∘ z = 1`, then
`w'' = (u² f + g) w` becomes `W'' = (u² + ψ) W`, with `ψ = liouvillePotential z g`.
No nonvanishing assumption on the solution or on the parameter `u` is needed.

```lean
TauCeti.deriv_deriv_liouvilleTransform_of_normalized (z w f g : ℝ → ℝ) (u : ℝ) {ξ : ℝ}
  (hz : ContDiffAt ℝ 3 z ξ) (hw : ContDiffAt ℝ 2 w (z ξ)) (hpos : 0 < deriv z ξ)
  (heq : deriv (deriv w) (z ξ) = (u ^ 2 * f (z ξ) + g (z ξ)) * w (z ξ))
  (hnorm : deriv z ξ ^ 2 * f (z ξ) = 1) :
  deriv (deriv (TauCeti.liouvilleTransform z w)) ξ =
    (u ^ 2 + TauCeti.liouvillePotential z g ξ) * TauCeti.liouvilleTransform z w ξ
```

## Depends on

- [TauCeti.liouvillePotential](tauceti-liouvillepotential.md)
- [TauCeti.liouvilleTransform](tauceti-liouvilletransform.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.deriv_deriv_liouvilleTransform_of_normalized`](https://taucetiproject.org/docs/TauCeti/Analysis/ODE/LiouvilleTransformation.html#TauCeti.deriv_deriv_liouvilleTransform_of_normalized).

## Sources

- [Tau Ceti documentation: `TauCeti.deriv_deriv_liouvilleTransform_of_normalized`](https://taucetiproject.org/docs/TauCeti/Analysis/ODE/LiouvilleTransformation.html#TauCeti.deriv_deriv_liouvilleTransform_of_normalized)
- [Source of `TauCeti.deriv_deriv_liouvilleTransform_of_normalized` in TauCeti/Analysis/ODE/LiouvilleTransformation.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/ODE/LiouvilleTransformation.lean#L174)
- [Tau Ceti roadmap status: Asymptotic expansions](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/AsymptoticExpansions/STATUS.md)
