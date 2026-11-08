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

- [Orientation.integrationCurrent](../../part-01/integral-currents-geometric-homology-and-minimiz/orientation-integrationcurrent.md)
- [TestFunction.extDerivCLM](../../part-01/integral-currents-geometric-homology-and-minimiz/testfunction-extderivclm.md)

## Proof depends on

- [A distribution has finite order on each compact set](../../part-01/integral-currents-geometric-homology-and-minimiz/a-distribution-has-finite-order-on-each-compact.md)
- [The derivative of a regularization](../../part-01/integral-currents-geometric-homology-and-minimiz/the-derivative-of-a-regularization.md)
- [Distributions with vanishing derivatives have locally constant regularizations](../../part-01/integral-currents-geometric-homology-and-minimiz/distributions-with-vanishing-derivatives-have-lo.md)
- [Uniform first-order Taylor estimate in a parameter](../../part-01/calculus/part-02/uniform-first-order-taylor-estimate-in-a-paramet.md)

## Lean

Formalized in Tau Ceti as [`Orientation.existsUnique_eq_smul_integrationCurrent_of_comp_extDerivCLM_eq_zero`](https://taucetiproject.org/docs/TauCeti/Analysis/Distribution/Constancy/Current.html#Orientation.existsUnique_eq_smul_integrationCurrent_of_comp_extDerivCLM_eq_zero).

## Sources

- [Tau Ceti documentation: `Orientation.existsUnique_eq_smul_integrationCurrent_of_comp_extDerivCLM_eq_zero`](https://taucetiproject.org/docs/TauCeti/Analysis/Distribution/Constancy/Current.html#Orientation.existsUnique_eq_smul_integrationCurrent_of_comp_extDerivCLM_eq_zero)
- [Source of `Orientation.existsUnique_eq_smul_integrationCurrent_of_comp_extDerivCLM_eq_zero` in TauCeti/Analysis/Distribution/Constancy/Current.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Distribution/Constancy/Current.lean#L99)
