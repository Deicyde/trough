---
declaration: theorem
origin: cited
lean: Orientation.existsUnique_eq_smul_integrationCurrent_of_comp_extDerivCLM_eq_zero
statement: formalized
proof: formalized
---

# The constancy theorem

On a connected open subset `Ω` of an oriented real vector space of
dimension `k + 1`, a top-degree current with zero boundary, `T ∘ d = 0`, is a unique real multiple
of the oriented integration current `[[Ω]]`.

```lean
Orientation.existsUnique_eq_smul_integrationCurrent_of_comp_extDerivCLM_eq_zero.{u_1} {E : Type u_1}
  [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E] [MeasurableSpace E]
  [BorelSpace E] {Ω : TopologicalSpace.Opens E} {k : ℕ} (o : Orientation ℝ E (Fin (k + 1)))
  (hE : Module.finrank ℝ E = k + 1) (hΩ : IsConnected ↑Ω)
  {T : TestFunction Ω (E [⋀^Fin (k + 1)]→L[ℝ] ℝ) ⊤ →L[ℝ] ℝ}
  (hT : T ∘SL TestFunction.extDerivCLM = 0) : ∃! c, T = c • o.integrationCurrent Ω
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Constancy of distributions](constancy-of-distributions.md)

## Lean

Formalized in Tau Ceti as [`Orientation.existsUnique_eq_smul_integrationCurrent_of_comp_extDerivCLM_eq_zero`](https://taucetiproject.org/docs/TauCeti/Analysis/Distribution/Constancy/Current.html#Orientation.existsUnique_eq_smul_integrationCurrent_of_comp_extDerivCLM_eq_zero).

## Sources

- [Tau Ceti documentation: `Orientation.existsUnique_eq_smul_integrationCurrent_of_comp_extDerivCLM_eq_zero`](https://taucetiproject.org/docs/TauCeti/Analysis/Distribution/Constancy/Current.html#Orientation.existsUnique_eq_smul_integrationCurrent_of_comp_extDerivCLM_eq_zero)
- [Source of `Orientation.existsUnique_eq_smul_integrationCurrent_of_comp_extDerivCLM_eq_zero` in TauCeti/Analysis/Distribution/Constancy/Current.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/Distribution/Constancy/Current.lean#L99)
- [Tau Ceti roadmap status: Integral currents, geometric homology and minimizing hypersurfaces](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/GeometricCurrents/STATUS.md)
