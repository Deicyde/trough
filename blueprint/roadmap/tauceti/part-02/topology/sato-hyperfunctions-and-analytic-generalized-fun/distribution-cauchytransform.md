---
declaration: def
origin: cited
lean: Distribution.cauchyTransform
statement: formalized
---

# Distribution.cauchyTransform

The **Cauchy transform** of a complex-valued distribution `u` on an open set `Ω ⊆ ℝ`, with
cutoff `χ`: the function `z ↦ (2πi)⁻¹ ⟨u_t, χ(t) / (t - z)⟩` on `ℂ ∖ ℝ`, extended by zero to `ℝ`.

```lean
Distribution.cauchyTransform {Ω : TopologicalSpace.Opens ℝ} (u : Distribution Ω ℂ ⊤)
  (χ : TestFunction Ω ℝ ⊤) (z : ℂ) : ℂ
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`Distribution.cauchyTransform`](https://taucetiproject.org/docs/TauCeti/Analysis/Hyperfunction/CauchyTransform.html#Distribution.cauchyTransform).

## Sources

- [Tau Ceti documentation: `Distribution.cauchyTransform`](https://taucetiproject.org/docs/TauCeti/Analysis/Hyperfunction/CauchyTransform.html#Distribution.cauchyTransform)
- [Source of `Distribution.cauchyTransform` in TauCeti/Analysis/Hyperfunction/CauchyTransform.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/Hyperfunction/CauchyTransform.lean#L131)
- [Tau Ceti roadmap status: Sato hyperfunctions and analytic generalized functions](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/Hyperfunctions/STATUS.md)
