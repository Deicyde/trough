---
declaration: theorem
origin: cited
lean: TauCeti.differentiableOn_schwarzReflection_of_symmetric
statement: formalized
proof: formalized
---

# Schwarz reflection principle (real axis)

On a conjugation-symmetric open set `Ω`, if `f`
is continuous on the closed upper part, holomorphic on the open upper part, and real-valued on
the real axis of `Ω`, then the explicit reflection extension `schwarzReflection f` is holomorphic
on all of `Ω` — in particular across the real axis.

The gluing calculus (continuity everywhere, holomorphy off the axis, the conjugation symmetry) is
`Reflection/Basic.lean`; the missing holomorphy at the axis is Painlevé removability,
`differentiableOn_of_continuousOn_of_differentiableOn_im_ne_zero`.

```lean
TauCeti.differentiableOn_schwarzReflection_of_symmetric {f : ℂ → ℂ} {Ω : Set ℂ} (hΩopen : IsOpen Ω)
  (hΩ : Set.MapsTo (⇑(starRingEnd ℂ)) Ω Ω) (hcont : ContinuousOn f (Ω ∩ {z | 0 ≤ z.im}))
  (hholo : DifferentiableOn ℂ f (Ω ∩ {z | 0 < z.im})) (hreal : ∀ z ∈ Ω, z.im = 0 → (f z).im = 0) :
  DifferentiableOn ℂ (TauCeti.schwarzReflection f) Ω
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.differentiableOn_schwarzReflection_of_symmetric`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Conformal/Reflection/Principle.html#TauCeti.differentiableOn_schwarzReflection_of_symmetric).

## Sources

- [Tau Ceti documentation: `TauCeti.differentiableOn_schwarzReflection_of_symmetric`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Conformal/Reflection/Principle.html#TauCeti.differentiableOn_schwarzReflection_of_symmetric)
- [Source of `TauCeti.differentiableOn_schwarzReflection_of_symmetric` in TauCeti/Analysis/Complex/Conformal/Reflection/Principle.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Complex/Conformal/Reflection/Principle.lean#L54)
- [Tau Ceti roadmap status: Conformal mapping and the geometric theory of holomorphic functions](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/ConformalMapping/STATUS.md)
