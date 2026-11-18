---
declaration: theorem
origin: cited
lean: TauCeti.existsUnique_discrete_volterra_solution
statement: formalized
proof: formalized
---

# Volterra summation equations

Under the hypotheses of
`exists_discrete_volterra_solution`, the summation equation
`h n = ∑_{m > n} K n m • (J m + ψ m • h m)` has exactly one solution that is `O(P)` at
infinity.

```lean
TauCeti.existsUnique_discrete_volterra_solution.{u_1, u_2} {𝕜 : Type u_1} {E : Type u_2}
  [NormedField 𝕜] [NormedAddCommGroup E] [NormedSpace 𝕜 E] {K : ℕ → ℕ → 𝕜} {J : ℕ → E} {ψ : ℕ → 𝕜}
  {P Q : ℕ → ℝ} [CompleteSpace E] (hP : ∀ (n : ℕ), 0 ≤ P n) (hQ : ∀ (m : ℕ), 0 ≤ Q m)
  (hK : ∀ (n m : ℕ), n < m → ‖K n m‖ ≤ P n * Q m) (hJ : Summable fun m => Q m * ‖J m‖)
  (hψ : Summable fun m => P m * Q m * ‖ψ m‖) :
  ∃! h,
    (∀ (n : ℕ), h n = ∑' (m : ↑(Set.Ioi n)), K n ↑m • (J ↑m + ψ ↑m • h ↑m)) ∧ h =O[Filter.atTop] P
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.existsUnique_discrete_volterra_solution`](https://taucetiproject.org/docs/TauCeti/Analysis/Asymptotics/DiscreteVolterra.html#TauCeti.existsUnique_discrete_volterra_solution).

## Sources

- [Tau Ceti documentation: `TauCeti.existsUnique_discrete_volterra_solution`](https://taucetiproject.org/docs/TauCeti/Analysis/Asymptotics/DiscreteVolterra.html#TauCeti.existsUnique_discrete_volterra_solution)
- [Source of `TauCeti.existsUnique_discrete_volterra_solution` in TauCeti/Analysis/Asymptotics/DiscreteVolterra.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/Asymptotics/DiscreteVolterra.lean#L368)
- [Tau Ceti roadmap status: Asymptotic expansions](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/AsymptoticExpansions/STATUS.md)
