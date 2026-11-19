---
declaration: def
origin: cited
lean: TauCeti.PenalizedConvex
statement: formalized
---

# TauCeti.PenalizedConvex

The energy `φ` is *penalized convex* with parameter `m` and time step `τ`: for every base point
`w` and any two points `v₀`, `v₁` with `φ v₀ ≠ ⊤` and `φ v₁ ≠ ⊤` (energy `⊥` is allowed), some
curve `γ` from `v₀` to `v₁` makes the penalized energy `z ↦ φ z + d(w, z)² / (2τ)` of the resolvent
`(m + 1 / τ)`-convex along it. This is Assumption 4.0.1 of Ambrosio–Gigli–Savaré at the time step
`τ`, there stated with the coefficient `(1 + m τ) / τ = m + 1 / τ`.

```lean
TauCeti.PenalizedConvex.{u_1} {X : Type u_1} [PseudoMetricSpace X] (m : ℝ) (τ : NNReal)
  (φ : X → EReal) : Prop
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.PenalizedConvex`](https://taucetiproject.org/docs/TauCeti/Analysis/GradientFlow/MoreauYosida/Convex.html#TauCeti.PenalizedConvex).

## Sources

- [Tau Ceti documentation: `TauCeti.PenalizedConvex`](https://taucetiproject.org/docs/TauCeti/Analysis/GradientFlow/MoreauYosida/Convex.html#TauCeti.PenalizedConvex)
- [Source of `TauCeti.PenalizedConvex` in TauCeti/Analysis/GradientFlow/MoreauYosida/Convex.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/GradientFlow/MoreauYosida/Convex.lean#L104)
- [Tau Ceti roadmap status: Optimal transport and Wasserstein geometry](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/OptimalTransport/STATUS.md)
