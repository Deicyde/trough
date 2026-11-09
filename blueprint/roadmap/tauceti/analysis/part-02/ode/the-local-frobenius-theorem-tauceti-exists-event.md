---
declaration: theorem
origin: cited
lean: TauCeti.exists_eventually_hasFDerivAt_of_isFrobeniusIntegrableAt
statement: formalized
proof: formalized
---

# The local Frobenius theorem (`TauCeti.exists_eventually_hasFDerivAt_of_isFrobeniusIntegrableAt`)

Let `E` and `F` be finite-dimensional real normed spaces and
let `f : E × F → (E →L[ℝ] F)` be `C^(n+1)` near `(x₀, y₀)`, for instance `C¹`. If `f` satisfies the
Frobenius integrability condition near `(x₀, y₀)`, then the total differential equation
`D u x = f (x, u x)` has a local solution `u` with `u x₀ = y₀`, which is `C^(n+1)` at `x₀`.

```lean
TauCeti.exists_eventually_hasFDerivAt_of_isFrobeniusIntegrableAt.{u} {E F : Type u}
  [NormedAddCommGroup E] [NormedSpace ℝ E] [NormedAddCommGroup F] [NormedSpace ℝ F]
  [FiniteDimensional ℝ E] [FiniteDimensional ℝ F] {n : ℕ∞} {f : E × F → E →L[ℝ] F} {s : Set (E × F)}
  {x₀ : E} {y₀ : F} (hf : ContDiffOn ℝ (↑n + 1) f s) (hs : s ∈ nhds (x₀, y₀))
  (hint : ∀ᶠ (p : E × F) in nhds (x₀, y₀), TauCeti.IsFrobeniusIntegrableAt f p) :
  ∃ u, u x₀ = y₀ ∧ ContDiffAt ℝ (↑n + 1) u x₀ ∧ ∀ᶠ (x : E) in nhds x₀, HasFDerivAt u (f (x, u x)) x
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.exists_eventually_hasFDerivAt_of_isFrobeniusIntegrableAt`](https://taucetiproject.org/docs/TauCeti/Analysis/ODE/Frobenius.html#TauCeti.exists_eventually_hasFDerivAt_of_isFrobeniusIntegrableAt).

## Sources

- [Tau Ceti documentation: `TauCeti.exists_eventually_hasFDerivAt_of_isFrobeniusIntegrableAt`](https://taucetiproject.org/docs/TauCeti/Analysis/ODE/Frobenius.html#TauCeti.exists_eventually_hasFDerivAt_of_isFrobeniusIntegrableAt)
- [Source of `TauCeti.exists_eventually_hasFDerivAt_of_isFrobeniusIntegrableAt` in TauCeti/Analysis/ODE/Frobenius.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/ODE/Frobenius.lean#L812)
