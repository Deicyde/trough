---
declaration: theorem
origin: cited
lean: Orientation.integrationCurrent_extDerivCLM, Orientation.formCurrent_comp_extDerivCLM_of_extDeriv_eq_zero, Orientation.formCurrent_comp_extDerivCLM
statement: formalized
proof: formalized
---

# Stokes' theorem for test forms

the integration current annihilates every exact test
form.

```lean
Orientation.integrationCurrent_extDerivCLM.{u_1} {E : Type u_1} [NormedAddCommGroup E]
  [NormedSpace ℝ E] [FiniteDimensional ℝ E] [MeasurableSpace E] [BorelSpace E] {k : ℕ}
  (o : Orientation ℝ E (Fin (k + 1))) (Ω : TopologicalSpace.Opens E)
  (ω : TestFunction Ω (E [⋀^Fin k]→L[ℝ] ℝ) ⊤) :
  (o.integrationCurrent Ω) (TestFunction.extDerivCLM ω) = 0
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`Orientation.integrationCurrent_extDerivCLM`](https://taucetiproject.org/docs/TauCeti/Analysis/Distribution/TestFunction/IntegrationCurrent.html#Orientation.integrationCurrent_extDerivCLM).

## Other forms

**Stokes' theorem for the current of a closed form.** Formalized in Tau Ceti as [`Orientation.formCurrent_comp_extDerivCLM_of_extDeriv_eq_zero`](https://taucetiproject.org/docs/TauCeti/Analysis/Distribution/TestFunction/FormCurrent.html#Orientation.formCurrent_comp_extDerivCLM_of_extDeriv_eq_zero).

```lean
Orientation.formCurrent_comp_extDerivCLM_of_extDeriv_eq_zero.{u_1} {E : Type u_1}
  [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E] [MeasurableSpace E]
  [BorelSpace E] {j : ℕ} {ω : E → E [⋀^Fin j]→L[ℝ] ℝ} {k : ℕ}
  (o : Orientation ℝ E (Fin (j + (k + 1)))) (Ω : TopologicalSpace.Opens E)
  (hω : ContDiffOn ℝ 1 ω ↑Ω) (hdω : Set.EqOn (extDeriv ω) 0 ↑Ω) :
  o.formCurrent Ω ω ∘SL TestFunction.extDerivCLM = 0
```

**Stokes' theorem for the current of a form.** Formalized in Tau Ceti as [`Orientation.formCurrent_comp_extDerivCLM`](https://taucetiproject.org/docs/TauCeti/Analysis/Distribution/TestFunction/FormCurrent.html#Orientation.formCurrent_comp_extDerivCLM).

```lean
Orientation.formCurrent_comp_extDerivCLM.{u_1} {E : Type u_1} [NormedAddCommGroup E]
  [NormedSpace ℝ E] [FiniteDimensional ℝ E] [MeasurableSpace E] [BorelSpace E] {j : ℕ}
  {ω : E → E [⋀^Fin j]→L[ℝ] ℝ} {k : ℕ} (o : Orientation ℝ E (Fin (j + (k + 1))))
  (Ω : TopologicalSpace.Opens E) (hω : ContDiffOn ℝ 1 ω ↑Ω) :
  o.formCurrent Ω ω ∘SL TestFunction.extDerivCLM =
    (-1) ^ (j + 1) • ((Orientation.reindex ℝ E (finCongr ⋯)) o).formCurrent Ω (extDeriv ω)
```

## Sources

- [Tau Ceti documentation: `Orientation.integrationCurrent_extDerivCLM`](https://taucetiproject.org/docs/TauCeti/Analysis/Distribution/TestFunction/IntegrationCurrent.html#Orientation.integrationCurrent_extDerivCLM)
- [Source of `Orientation.integrationCurrent_extDerivCLM` in TauCeti/Analysis/Distribution/TestFunction/IntegrationCurrent.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/Distribution/TestFunction/IntegrationCurrent.lean#L145)
