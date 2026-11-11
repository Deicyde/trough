---
declaration: theorem
origin: cited
lean: MeasureTheory.LocallyIntegrableOn.exists_ae_eq_const_Ioo_of_integral_deriv_smul_eq_zero, ContinuousOn.exists_eqOn_const_Ioo_of_integral_deriv_smul_eq_zero
statement: formalized
proof: formalized
---

# The du Bois-Reymond lemma

A function locally integrable on an open interval whose
pairing with the derivative of every test function on the interval vanishes,
`∫ x, deriv ψ x • f x = 0`, is almost everywhere equal to a constant on the interval.

```lean
MeasureTheory.LocallyIntegrableOn.exists_ae_eq_const_Ioo_of_integral_deriv_smul_eq_zero.{u_1}
  {F : Type u_1} [NormedAddCommGroup F] [NormedSpace ℝ F] [CompleteSpace F] {a b : ℝ} {f : ℝ → F}
  (hf : MeasureTheory.LocallyIntegrableOn f (Set.Ioo a b) MeasureTheory.volume)
  (h :
    ∀ (ψ : ℝ → ℝ), ContDiff ℝ (↑⊤) ψ → tsupport ψ ⊆ Set.Ioo a b → ∫ (x : ℝ), deriv ψ x • f x = 0) :
  ∃ c, f =ᵐ[MeasureTheory.volume.restrict (Set.Ioo a b)] fun x => c
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`MeasureTheory.LocallyIntegrableOn.exists_ae_eq_const_Ioo_of_integral_deriv_smul_eq_zero`](https://taucetiproject.org/docs/TauCeti/Analysis/Distribution/DuBoisReymond.html#MeasureTheory.LocallyIntegrableOn.exists_ae_eq_const_Ioo_of_integral_deriv_smul_eq_zero).

## Other forms

**The du Bois-Reymond lemma for continuous functions.** Formalized in Tau Ceti as [`ContinuousOn.exists_eqOn_const_Ioo_of_integral_deriv_smul_eq_zero`](https://taucetiproject.org/docs/TauCeti/Analysis/Distribution/DuBoisReymond.html#ContinuousOn.exists_eqOn_const_Ioo_of_integral_deriv_smul_eq_zero).

```lean
ContinuousOn.exists_eqOn_const_Ioo_of_integral_deriv_smul_eq_zero.{u_1} {F : Type u_1}
  [NormedAddCommGroup F] [NormedSpace ℝ F] [CompleteSpace F] {a b : ℝ} {f : ℝ → F}
  (hf : ContinuousOn f (Set.Ioo a b))
  (h :
    ∀ (ψ : ℝ → ℝ), ContDiff ℝ (↑⊤) ψ → tsupport ψ ⊆ Set.Ioo a b → ∫ (x : ℝ), deriv ψ x • f x = 0) :
  ∃ c, Set.EqOn f (fun x => c) (Set.Ioo a b)
```

## Sources

- [Tau Ceti documentation: `MeasureTheory.LocallyIntegrableOn.exists_ae_eq_const_Ioo_of_integral_deriv_smul_eq_zero`](https://taucetiproject.org/docs/TauCeti/Analysis/Distribution/DuBoisReymond.html#MeasureTheory.LocallyIntegrableOn.exists_ae_eq_const_Ioo_of_integral_deriv_smul_eq_zero)
- [Source of `MeasureTheory.LocallyIntegrableOn.exists_ae_eq_const_Ioo_of_integral_deriv_smul_eq_zero` in TauCeti/Analysis/Distribution/DuBoisReymond.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Distribution/DuBoisReymond.lean#L118)
