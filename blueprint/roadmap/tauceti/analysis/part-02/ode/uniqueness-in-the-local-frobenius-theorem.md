---
declaration: theorem
origin: cited
lean: TauCeti.eventuallyEq_of_eventually_hasFDerivAt
statement: formalized
proof: formalized
---

# Uniqueness in the local Frobenius theorem

Two solutions of the total differential
equation `D u x = f (x, u x)` near `x₀` taking the same value at `x₀` agree near `x₀`, as soon as
`f` is Lipschitz near `(x₀, u₁ x₀)`. Neither integrability nor finite dimensionality is needed:
along each ray from `x₀` both solutions solve the same ordinary differential equation.

```lean
TauCeti.eventuallyEq_of_eventually_hasFDerivAt.{u_1, u_2} {E : Type u_1} {F : Type u_2}
  [NormedAddCommGroup E] [NormedSpace ℝ E] [NormedAddCommGroup F] [NormedSpace ℝ F]
  {f : E × F → E →L[ℝ] F} {u₁ u₂ : E → F} {x₀ : E} {K : NNReal} {s : Set (E × F)}
  (hs : s ∈ nhds (x₀, u₁ x₀)) (hf : LipschitzOnWith K f s)
  (hu₁ : ∀ᶠ (x : E) in nhds x₀, HasFDerivAt u₁ (f (x, u₁ x)) x)
  (hu₂ : ∀ᶠ (x : E) in nhds x₀, HasFDerivAt u₂ (f (x, u₂ x)) x) (h₀ : u₁ x₀ = u₂ x₀) :
  u₁ =ᶠ[nhds x₀] u₂
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.eventuallyEq_of_eventually_hasFDerivAt`](https://taucetiproject.org/docs/TauCeti/Analysis/ODE/Frobenius.html#TauCeti.eventuallyEq_of_eventually_hasFDerivAt).

## Sources

- [Tau Ceti documentation: `TauCeti.eventuallyEq_of_eventually_hasFDerivAt`](https://taucetiproject.org/docs/TauCeti/Analysis/ODE/Frobenius.html#TauCeti.eventuallyEq_of_eventually_hasFDerivAt)
- [Source of `TauCeti.eventuallyEq_of_eventually_hasFDerivAt` in TauCeti/Analysis/ODE/Frobenius.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/ODE/Frobenius.lean#L385)
