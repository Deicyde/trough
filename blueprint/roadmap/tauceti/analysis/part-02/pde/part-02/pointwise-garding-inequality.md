---
declaration: theorem
origin: cited
lean: TauCeti.PDE.garding_energyIntegrand_self_of_bounds
statement: formalized
proof: formalized
---

# Pointwise Gårding inequality

With a nonnegative mass coefficient (`c ≥ 0`), the
diagonal of the jet form is bounded below by `(λ/2)‖∇u‖² − (β²/2λ)|u|²`. The ellipticity
floor `λ‖∇u‖²` pays for the drift term via Young's inequality, leaving half the floor and a
mass defect proportional to `β²/λ`. Integrating over `Ω` this is Gårding's inequality
`a(u, u) ≥ (λ/2)‖∇u‖²_{L²} − (β²/2λ)‖u‖²_{L²}`.

```lean
TauCeti.PDE.garding_energyIntegrand_self_of_bounds.{u_1} {n : Type u_1} [Fintype n] {lam beta : ℝ}
  (hlam : 0 < lam) {A : Matrix n n ℝ} {b₀ : EuclideanSpace ℝ n} {c₀ : ℝ}
  (hQ : ∀ (ξ : EuclideanSpace ℝ n), lam * ‖ξ‖ ^ 2 ≤ A.toQuadraticForm' ξ.ofLp) (hb : ‖b₀‖ ≤ beta)
  (hc : 0 ≤ c₀) (U : ℝ × EuclideanSpace ℝ n) :
  lam / 2 * ‖U.2‖ ^ 2 - beta ^ 2 / (2 * lam) * U.1 ^ 2 ≤ ((TauCeti.PDE.energyIntegrand A b₀ c₀) U) U
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.PDE.garding_energyIntegrand_self_of_bounds`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/EnergyForm/Basic.html#TauCeti.PDE.garding_energyIntegrand_self_of_bounds).

## Sources

- [Tau Ceti documentation: `TauCeti.PDE.garding_energyIntegrand_self_of_bounds`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/EnergyForm/Basic.html#TauCeti.PDE.garding_energyIntegrand_self_of_bounds)
- [Source of `TauCeti.PDE.garding_energyIntegrand_self_of_bounds` in TauCeti/Analysis/PDE/EnergyForm/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/PDE/EnergyForm/Basic.lean#L273)
