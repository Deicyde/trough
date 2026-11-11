---
declaration: theorem
origin: cited
lean: TauCeti.rouche, TauCeti.rouche_add, TauCeti.rouche_add_exists_eq_zero_iff, TauCeti.rouche_exists_eq_zero_iff, TauCeti.rouche_symm_exists_eq_zero_iff, TauCeti.rouche_windingNumber_comp, TauCeti.rouche_add_windingNumber_comp, TauCeti.rouche_symm_windingNumber_comp, TauCeti.rouche_add_nullHomologous, TauCeti.rouche_nullHomologous, TauCeti.rouche_symm_nullHomologous_of_analyticOnNhd, TauCeti.rouche_symm_nullHomologous, TauCeti.rouche_symm
statement: formalized
proof: formalized
---

# Rouché's theorem for a disc, classical form

If `f` and `g` are holomorphic on the closed
disc `closedBall c R` and `‖f z - g z‖ < ‖f z‖` at every point `z` of the bounding circle, then `f`
and `g` have the same number of zeros in `ball c R`, each counted with multiplicity.

This is the special case of `TauCeti.rouche_symm` obtained by discarding the nonnegative summand
`‖g z‖` from the symmetric hypothesis.

```lean
TauCeti.rouche {f g : ℂ → ℂ} {c : ℂ} {R : ℝ} (hf : AnalyticOnNhd ℂ f (Metric.closedBall c R))
  (hg : AnalyticOnNhd ℂ g (Metric.closedBall c R))
  (hs : ∀ z ∈ Metric.sphere c R, ‖f z - g z‖ < ‖f z‖) :
  ∑ᶠ (z : ℂ) (_ : z ∈ Metric.ball c R), analyticOrderNatAt f z =
    ∑ᶠ (z : ℂ) (_ : z ∈ Metric.ball c R), analyticOrderNatAt g z
```

## Depends on

- [Generalized winding number (HW Def 2.1)](../../../part-01/contour-integration-and-the-hungerbuhler-wasem-g/generalized-winding-number-hw-def-2-1.md)

## Proof depends on

- [Cauchy–Goursat for a pole-free meromorphic function](../../contour/cauchy-goursat-for-a-pole-free-meromorphic-funct.md)
- [The classical residue theorem for a null-homologous contour cycle](../../../part-01/contour-integration-and-the-hungerbuhler-wasem-g/the-classical-residue-theorem-for-a-null-homolog.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.rouche`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Conformal/Rouche.html#TauCeti.rouche).

## Other forms

**Rouché's theorem, in the additive phrasing of most textbooks.** Formalized in Tau Ceti as [`TauCeti.rouche_add`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Conformal/Rouche.html#TauCeti.rouche_add).

```lean
TauCeti.rouche_add {f g : ℂ → ℂ} {c : ℂ} {R : ℝ} (hf : AnalyticOnNhd ℂ f (Metric.closedBall c R))
  (hg : AnalyticOnNhd ℂ g (Metric.closedBall c R)) (hs : ∀ z ∈ Metric.sphere c R, ‖g z‖ < ‖f z‖) :
  ∑ᶠ (z : ℂ) (_ : z ∈ Metric.ball c R), analyticOrderNatAt f z =
    ∑ᶠ (z : ℂ) (_ : z ∈ Metric.ball c R), analyticOrderNatAt (fun w => f w + g w) z
```

**Rouché's theorem as a zero-detection principle, additive form.** Formalized in Tau Ceti as [`TauCeti.rouche_add_exists_eq_zero_iff`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Conformal/Rouche.html#TauCeti.rouche_add_exists_eq_zero_iff).

```lean
TauCeti.rouche_add_exists_eq_zero_iff {f g : ℂ → ℂ} {c : ℂ} {R : ℝ}
  (hf : AnalyticOnNhd ℂ f (Metric.closedBall c R)) (hg : AnalyticOnNhd ℂ g (Metric.closedBall c R))
  (hs : ∀ z ∈ Metric.sphere c R, ‖g z‖ < ‖f z‖) :
  (∃ z ∈ Metric.ball c R, f z = 0) ↔ ∃ z ∈ Metric.ball c R, f z + g z = 0
```

**Rouché's theorem as a zero-detection principle, classical form.** Formalized in Tau Ceti as [`TauCeti.rouche_exists_eq_zero_iff`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Conformal/Rouche.html#TauCeti.rouche_exists_eq_zero_iff).

```lean
TauCeti.rouche_exists_eq_zero_iff {f g : ℂ → ℂ} {c : ℂ} {R : ℝ}
  (hf : AnalyticOnNhd ℂ f (Metric.closedBall c R)) (hg : AnalyticOnNhd ℂ g (Metric.closedBall c R))
  (hs : ∀ z ∈ Metric.sphere c R, ‖f z - g z‖ < ‖f z‖) :
  (∃ z ∈ Metric.ball c R, f z = 0) ↔ ∃ z ∈ Metric.ball c R, g z = 0
```

**Rouché's theorem as a zero-detection principle, symmetric form.** Formalized in Tau Ceti as [`TauCeti.rouche_symm_exists_eq_zero_iff`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Conformal/Rouche.html#TauCeti.rouche_symm_exists_eq_zero_iff).

```lean
TauCeti.rouche_symm_exists_eq_zero_iff {f g : ℂ → ℂ} {c : ℂ} {R : ℝ}
  (hf : AnalyticOnNhd ℂ f (Metric.closedBall c R)) (hg : AnalyticOnNhd ℂ g (Metric.closedBall c R))
  (hs : ∀ z ∈ Metric.sphere c R, ‖f z - g z‖ < ‖f z‖ + ‖g z‖) :
  (∃ z ∈ Metric.ball c R, f z = 0) ↔ ∃ z ∈ Metric.ball c R, g z = 0
```

**Rouché's theorem as an equality of image winding numbers, classical form.** Formalized in Tau Ceti as [`TauCeti.rouche_windingNumber_comp`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Conformal/Rouche.html#TauCeti.rouche_windingNumber_comp).

```lean
TauCeti.rouche_windingNumber_comp {f g : ℂ → ℂ} {γ : ℝ → ℂ} {a b : ℝ}
  (hγ : TauCeti.IsPiecewiseC1On γ a b) (hclosed : γ a = γ b)
  (hfa : ∀ t ∈ Set.uIcc a b, AnalyticAt ℂ f (γ t)) (hga : ∀ t ∈ Set.uIcc a b, AnalyticAt ℂ g (γ t))
  (hs : ∀ t ∈ Set.uIcc a b, ‖f (γ t) - g (γ t)‖ < ‖f (γ t)‖) :
  TauCeti.Contour.windingNumber (f ∘ γ) a b 0 = TauCeti.Contour.windingNumber (g ∘ γ) a b 0
```

**Rouché's theorem as an equality of image winding numbers, additive form.** Formalized in Tau Ceti as [`TauCeti.rouche_add_windingNumber_comp`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Conformal/Rouche.html#TauCeti.rouche_add_windingNumber_comp).

```lean
TauCeti.rouche_add_windingNumber_comp {f g : ℂ → ℂ} {γ : ℝ → ℂ} {a b : ℝ}
  (hγ : TauCeti.IsPiecewiseC1On γ a b) (hclosed : γ a = γ b)
  (hfa : ∀ t ∈ Set.uIcc a b, AnalyticAt ℂ f (γ t)) (hga : ∀ t ∈ Set.uIcc a b, AnalyticAt ℂ g (γ t))
  (hs : ∀ t ∈ Set.uIcc a b, ‖g (γ t)‖ < ‖f (γ t)‖) :
  TauCeti.Contour.windingNumber (f ∘ γ) a b 0 =
    TauCeti.Contour.windingNumber ((fun w => f w + g w) ∘ γ) a b 0
```

**Rouché's theorem as an equality of image winding numbers, symmetric form — the "dog on a leash" statement.** Formalized in Tau Ceti as [`TauCeti.rouche_symm_windingNumber_comp`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Conformal/Rouche.html#TauCeti.rouche_symm_windingNumber_comp).

```lean
TauCeti.rouche_symm_windingNumber_comp {f g : ℂ → ℂ} {γ : ℝ → ℂ} {a b : ℝ}
  (hγ : TauCeti.IsPiecewiseC1On γ a b) (hclosed : γ a = γ b)
  (hfa : ∀ t ∈ Set.uIcc a b, AnalyticAt ℂ f (γ t)) (hga : ∀ t ∈ Set.uIcc a b, AnalyticAt ℂ g (γ t))
  (hs : ∀ t ∈ Set.uIcc a b, ‖f (γ t) - g (γ t)‖ < ‖f (γ t)‖ + ‖g (γ t)‖) :
  TauCeti.Contour.windingNumber (f ∘ γ) a b 0 = TauCeti.Contour.windingNumber (g ∘ γ) a b 0
```

**Rouché's theorem for a null-homologous cycle, additive form.** Formalized in Tau Ceti as [`TauCeti.rouche_add_nullHomologous`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Conformal/Rouche.html#TauCeti.rouche_add_nullHomologous).

```lean
TauCeti.rouche_add_nullHomologous {f g : ℂ → ℂ} {U : Set ℂ} {S : Finset ℂ} {γ : ℝ → ℂ} {a b : ℝ}
  (hU : IsOpen U) (hf : AnalyticOnNhd ℂ f U) (hg : AnalyticOnNhd ℂ g U)
  (hfS : ∀ z ∈ U, f z = 0 → z ∈ S) (hsumS : ∀ z ∈ U, f z + g z = 0 → z ∈ S)
  (hγ : TauCeti.IsPiecewiseC1On γ a b) (hγU : ∀ t ∈ Set.uIcc a b, γ t ∈ U) (hclosed : γ a = γ b)
  (hnull : TauCeti.Contour.IsNullHomologous γ a b U)
  (hs : ∀ t ∈ Set.uIcc a b, ‖g (γ t)‖ < ‖f (γ t)‖) :
  ∑ z ∈ S, TauCeti.Contour.windingNumber γ a b z * ↑(analyticOrderNatAt f z) =
    ∑ z ∈ S, TauCeti.Contour.windingNumber γ a b z * ↑(analyticOrderNatAt (fun w => f w + g w) z)
```

**Rouché's theorem for a null-homologous cycle, classical form.** Formalized in Tau Ceti as [`TauCeti.rouche_nullHomologous`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Conformal/Rouche.html#TauCeti.rouche_nullHomologous).

```lean
TauCeti.rouche_nullHomologous {f g : ℂ → ℂ} {U : Set ℂ} {S : Finset ℂ} {γ : ℝ → ℂ} {a b : ℝ}
  (hU : IsOpen U) (hf : AnalyticOnNhd ℂ f U) (hg : AnalyticOnNhd ℂ g U)
  (hfS : ∀ z ∈ U, f z = 0 → z ∈ S) (hgS : ∀ z ∈ U, g z = 0 → z ∈ S)
  (hγ : TauCeti.IsPiecewiseC1On γ a b) (hγU : ∀ t ∈ Set.uIcc a b, γ t ∈ U) (hclosed : γ a = γ b)
  (hnull : TauCeti.Contour.IsNullHomologous γ a b U)
  (hs : ∀ t ∈ Set.uIcc a b, ‖f (γ t) - g (γ t)‖ < ‖f (γ t)‖) :
  ∑ z ∈ S, TauCeti.Contour.windingNumber γ a b z * ↑(analyticOrderNatAt f z) =
    ∑ z ∈ S, TauCeti.Contour.windingNumber γ a b z * ↑(analyticOrderNatAt g z)
```

**Rouché's theorem for a null-homologous cycle, holomorphic form.** Formalized in Tau Ceti as [`TauCeti.rouche_symm_nullHomologous_of_analyticOnNhd`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Conformal/Rouche.html#TauCeti.rouche_symm_nullHomologous_of_analyticOnNhd).

```lean
TauCeti.rouche_symm_nullHomologous_of_analyticOnNhd {f g : ℂ → ℂ} {U : Set ℂ} {S : Finset ℂ}
  {γ : ℝ → ℂ} {a b : ℝ} (hU : IsOpen U) (hf : AnalyticOnNhd ℂ f U) (hg : AnalyticOnNhd ℂ g U)
  (hfS : ∀ z ∈ U, f z = 0 → z ∈ S) (hgS : ∀ z ∈ U, g z = 0 → z ∈ S)
  (hγ : TauCeti.IsPiecewiseC1On γ a b) (hγU : ∀ t ∈ Set.uIcc a b, γ t ∈ U) (hclosed : γ a = γ b)
  (hnull : TauCeti.Contour.IsNullHomologous γ a b U)
  (hs : ∀ t ∈ Set.uIcc a b, ‖f (γ t) - g (γ t)‖ < ‖f (γ t)‖ + ‖g (γ t)‖) :
  ∑ z ∈ S, TauCeti.Contour.windingNumber γ a b z * ↑(analyticOrderNatAt f z) =
    ∑ z ∈ S, TauCeti.Contour.windingNumber γ a b z * ↑(analyticOrderNatAt g z)
```

**Rouché's theorem for a null-homologous cycle, symmetric form (Estermann).** Formalized in Tau Ceti as [`TauCeti.rouche_symm_nullHomologous`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Conformal/Rouche.html#TauCeti.rouche_symm_nullHomologous).

```lean
TauCeti.rouche_symm_nullHomologous {f g : ℂ → ℂ} {U : Set ℂ} {S : Finset ℂ} {γ : ℝ → ℂ} {a b : ℝ}
  {ordf ordg : ℂ → ℤ} (hU : IsOpen U) (hfoff : ∀ z ∈ U, z ∉ S → AnalyticAt ℂ f z ∧ f z ≠ 0)
  (hgoff : ∀ z ∈ U, z ∉ S → AnalyticAt ℂ g z ∧ g z ≠ 0)
  (hfmero : ∀ s ∈ S, s ∈ U → MeromorphicAt f s) (hgmero : ∀ s ∈ S, s ∈ U → MeromorphicAt g s)
  (hford : ∀ s ∈ S, s ∈ U → meromorphicOrderAt f s = ↑(ordf s))
  (hgord : ∀ s ∈ S, s ∈ U → meromorphicOrderAt g s = ↑(ordg s)) (hγ : TauCeti.IsPiecewiseC1On γ a b)
  (hγU : ∀ t ∈ Set.uIcc a b, γ t ∈ U) (hclosed : γ a = γ b) (hγoff : ∀ t ∈ Set.uIcc a b, γ t ∉ ↑S)
  (hnull : TauCeti.Contour.IsNullHomologous γ a b U)
  (hs : ∀ t ∈ Set.uIcc a b, ‖f (γ t) - g (γ t)‖ < ‖f (γ t)‖ + ‖g (γ t)‖) :
  ∑ z ∈ S, TauCeti.Contour.windingNumber γ a b z * ↑(ordf z) =
    ∑ z ∈ S, TauCeti.Contour.windingNumber γ a b z * ↑(ordg z)
```

**Rouché's theorem, symmetric form (Estermann).** Formalized in Tau Ceti as [`TauCeti.rouche_symm`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Conformal/Rouche.html#TauCeti.rouche_symm).

```lean
TauCeti.rouche_symm {f g : ℂ → ℂ} {c : ℂ} {R : ℝ} (hf : AnalyticOnNhd ℂ f (Metric.closedBall c R))
  (hg : AnalyticOnNhd ℂ g (Metric.closedBall c R))
  (hs : ∀ z ∈ Metric.sphere c R, ‖f z - g z‖ < ‖f z‖ + ‖g z‖) :
  ∑ᶠ (z : ℂ) (_ : z ∈ Metric.ball c R), analyticOrderNatAt f z =
    ∑ᶠ (z : ℂ) (_ : z ∈ Metric.ball c R), analyticOrderNatAt g z
```

## Sources

- [Tau Ceti documentation: `TauCeti.rouche`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Conformal/Rouche.html#TauCeti.rouche)
- [Source of `TauCeti.rouche` in TauCeti/Analysis/Complex/Conformal/Rouche.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Complex/Conformal/Rouche.lean#L290)
