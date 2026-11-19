---
declaration: theorem
origin: cited
lean: Orientation.existsUnique_eq_smul_integrationCurrent_of_finrank_eq_zero
statement: formalized
proof: formalized
---

# The constancy theorem in degree zero

On a zero-dimensional oriented real vector space
every `0`-current on a connected open set, which is then the whole point, is a unique real multiple
of the integration current, the signed Dirac current at the origin. No boundary condition enters:
the boundary of a `0`-current is zero.

```lean
Orientation.existsUnique_eq_smul_integrationCurrent_of_finrank_eq_zero.{u_1} {E : Type u_1}
  [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E] [MeasurableSpace E]
  [BorelSpace E] {Ω : TopologicalSpace.Opens E} (o : Orientation ℝ E (Fin 0))
  (hE : Module.finrank ℝ E = 0) (hΩ : IsConnected ↑Ω)
  (T : TestFunction Ω (E [⋀^Fin 0]→L[ℝ] ℝ) ⊤ →L[ℝ] ℝ) : ∃! c, T = c • o.integrationCurrent Ω
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Constancy of distributions](constancy-of-distributions.md)

## Lean

Formalized in Tau Ceti as [`Orientation.existsUnique_eq_smul_integrationCurrent_of_finrank_eq_zero`](https://taucetiproject.org/docs/TauCeti/Analysis/Distribution/Constancy/Current.html#Orientation.existsUnique_eq_smul_integrationCurrent_of_finrank_eq_zero).

## Sources

- [Tau Ceti documentation: `Orientation.existsUnique_eq_smul_integrationCurrent_of_finrank_eq_zero`](https://taucetiproject.org/docs/TauCeti/Analysis/Distribution/Constancy/Current.html#Orientation.existsUnique_eq_smul_integrationCurrent_of_finrank_eq_zero)
- [Source of `Orientation.existsUnique_eq_smul_integrationCurrent_of_finrank_eq_zero` in TauCeti/Analysis/Distribution/Constancy/Current.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/Distribution/Constancy/Current.lean#L143)
