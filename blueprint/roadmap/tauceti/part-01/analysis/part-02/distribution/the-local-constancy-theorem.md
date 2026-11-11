---
declaration: theorem
origin: cited
lean: Orientation.existsUnique_comp_monoCLM_eq_smul_integrationCurrent
statement: formalized
proof: formalized
---

# The local constancy theorem

A top-degree current with zero boundary on an arbitrary open
subset `Ω` of an oriented real vector space of dimension `k + 1` restricts, on every connected open
subset `U ⊆ Ω`, to a unique real multiple of the integration current `[[U]]`. (If `U ⊄ Ω` the
restriction map `monoCLM` is zero, and the multiple is `0`.)

```lean
Orientation.existsUnique_comp_monoCLM_eq_smul_integrationCurrent.{u_1} {E : Type u_1}
  [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E] [MeasurableSpace E]
  [BorelSpace E] {Ω U : TopologicalSpace.Opens E} {k : ℕ} (o : Orientation ℝ E (Fin (k + 1)))
  (hE : Module.finrank ℝ E = k + 1) {T : TestFunction Ω (E [⋀^Fin (k + 1)]→L[ℝ] ℝ) ⊤ →L[ℝ] ℝ}
  (hT : T ∘SL TestFunction.extDerivCLM = 0) (hUc : IsConnected ↑U) :
  ∃! c, T ∘SL TestFunction.monoCLM ℝ = c • o.integrationCurrent U
```

## Depends on

- [Orientation.integrationCurrent](../../part-01/integral-currents-geometric-homology-and-minimiz/orientation-integrationcurrent.md)
- [TestFunction.extDerivCLM](../../part-01/integral-currents-geometric-homology-and-minimiz/testfunction-extderivclm.md)

## Proof depends on

- [The constancy theorem](the-constancy-theorem.md)

## Lean

Formalized in Tau Ceti as [`Orientation.existsUnique_comp_monoCLM_eq_smul_integrationCurrent`](https://taucetiproject.org/docs/TauCeti/Analysis/Distribution/Constancy/Current.html#Orientation.existsUnique_comp_monoCLM_eq_smul_integrationCurrent).

## Sources

- [Tau Ceti documentation: `Orientation.existsUnique_comp_monoCLM_eq_smul_integrationCurrent`](https://taucetiproject.org/docs/TauCeti/Analysis/Distribution/Constancy/Current.html#Orientation.existsUnique_comp_monoCLM_eq_smul_integrationCurrent)
- [Source of `Orientation.existsUnique_comp_monoCLM_eq_smul_integrationCurrent` in TauCeti/Analysis/Distribution/Constancy/Current.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Distribution/Constancy/Current.lean#L129)
