---
declaration: theorem
origin: cited
lean: TauCeti.Contour.cauchyIntegralFormula_iteratedDeriv_nullHomologous, TauCeti.Contour.Cycle.cauchyIntegralFormula_nullHomologous, TauCeti.Contour.Cycle.cauchyIntegralFormula_deriv_nullHomologous, TauCeti.Contour.Cycle.cauchyIntegralFormula_deriv_smul_nullHomologous, TauCeti.Contour.Cycle.cauchyIntegralFormula_smul_nullHomologous, TauCeti.Contour.Cycle.cauchyIntegralFormula_iteratedDeriv_nullHomologous, TauCeti.Contour.Cycle.cauchyIntegralFormula_iteratedDeriv_smul_nullHomologous, TauCeti.Contour.cauchyIntegralFormula_deriv_nullHomologous, TauCeti.Contour.dixonH2_eq_windingNumber_mul_f_of_dixonFunction_eq_zero, TauCeti.Contour.cauchyIntegralFormula_ball, TauCeti.Contour.cauchyIntegralFormula_iteratedDeriv_ball, TauCeti.Contour.cauchyIntegralFormula_starConvex, TauCeti.Contour.cauchyIntegralFormula_iteratedDeriv_starConvex, TauCeti.Contour.cauchyIntegralFormula_nullHomologous
statement: formalized
proof: formalized
---

# Cauchy's integral formula for the `k`-th derivative, homology form

Let `f` be holomorphic
on an open `U`, let `γ` be a closed piecewise-`C¹` curve in `U` that is null-homologous there, and
let `z ∈ U` lie off the curve. Then for every `k`,

`∫ t in a..b, γ' t • (f (γ t) / (γ t − z) ^ (k + 1)) = 2πi · n_z(γ) · f⁽ᵏ⁾(z) / k !`,

the `k`-th Taylor coefficient of `f` at `z` weighted by the generalized winding number of `γ` about
`z`. Only the residue at `z` contributes: the residue theorem for a null-homologous cycle applied
to the Cauchy kernel `w ↦ f w / (w − z) ^ (k + 1)`, whose only possible singularity in `U` is at
`z`, leaves the single residue `iteratedDeriv k f z / k !`.

```lean
TauCeti.Contour.cauchyIntegralFormula_iteratedDeriv_nullHomologous {f : ℂ → ℂ} {U : Set ℂ}
  {γ : ℝ → ℂ} {a b : ℝ} {z : ℂ} (hU : IsOpen U) (hf : DifferentiableOn ℂ f U)
  (hγ : TauCeti.IsPiecewiseC1On γ a b) (hγU : ∀ t ∈ Set.uIcc a b, γ t ∈ U) (hclosed : γ a = γ b)
  (hnull : TauCeti.Contour.IsNullHomologous γ a b U) (hz : z ∈ U)
  (hoff : ∀ t ∈ Set.uIcc a b, γ t ≠ z) (k : ℕ) :
  ∫ (t : ℝ) in a..b, deriv γ t • (f (γ t) / (γ t - z) ^ (k + 1)) =
    2 * ↑Real.pi * Complex.I * TauCeti.Contour.windingNumber γ a b z *
      (iteratedDeriv k f z / ↑k.factorial)
```

## Depends on

- [Generalized winding number (HW Def 2.1)](generalized-winding-number-hw-def-2-1.md)
- [TauCeti.Contour.Cycle](tauceti-contour-cycle.md)

## Proof depends on

- [The residue of the Cauchy kernel](the-residue-of-the-cauchy-kernel.md)

## Informally uses

- [The classical residue theorem for a null-homologous contour cycle](the-classical-residue-theorem-for-a-null-homolog.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Contour.cauchyIntegralFormula_iteratedDeriv_nullHomologous`](https://taucetiproject.org/docs/TauCeti/Analysis/Contour/Cauchy/HomologyFormula.html#TauCeti.Contour.cauchyIntegralFormula_iteratedDeriv_nullHomologous).

## Other forms

**Cauchy's integral formula for a cycle (roadmap Layer 3).** Formalized in Tau Ceti as [`TauCeti.Contour.Cycle.cauchyIntegralFormula_nullHomologous`](https://taucetiproject.org/docs/TauCeti/Analysis/Contour/Cycle/Residue.html#TauCeti.Contour.Cycle.cauchyIntegralFormula_nullHomologous).

```lean
TauCeti.Contour.Cycle.cauchyIntegralFormula_nullHomologous {f : ℂ → ℂ} {U : Set ℂ} {z : ℂ}
  (hU : IsOpen U) (hf : DifferentiableOn ℂ f U) {C : TauCeti.Contour.Cycle} (hCU : C.IsIn U)
  (hnull : C.IsNullHomologous U) (hz : z ∈ U) (hoff : z ∉ C.trace) :
  (TauCeti.Contour.Cycle.integral fun w => f w / (w - z)) C =
    2 * ↑Real.pi * Complex.I * (TauCeti.Contour.Cycle.windingNumber z) C * f z
```

**Cauchy's integral formula for a cycle, first derivative.** Formalized in Tau Ceti as [`TauCeti.Contour.Cycle.cauchyIntegralFormula_deriv_nullHomologous`](https://taucetiproject.org/docs/TauCeti/Analysis/Contour/Cycle/Residue.html#TauCeti.Contour.Cycle.cauchyIntegralFormula_deriv_nullHomologous).

```lean
TauCeti.Contour.Cycle.cauchyIntegralFormula_deriv_nullHomologous {f : ℂ → ℂ} {U : Set ℂ} {z : ℂ}
  (hU : IsOpen U) (hf : DifferentiableOn ℂ f U) {C : TauCeti.Contour.Cycle} (hCU : C.IsIn U)
  (hnull : C.IsNullHomologous U) (hz : z ∈ U) (hoff : z ∉ C.trace) :
  (TauCeti.Contour.Cycle.integral fun w => f w / (w - z) ^ 2) C =
    2 * ↑Real.pi * Complex.I * (TauCeti.Contour.Cycle.windingNumber z) C * deriv f z
```

**Cauchy's integral formula for a cycle, first derivative of a Banach-valued function.** Formalized in Tau Ceti as [`TauCeti.Contour.Cycle.cauchyIntegralFormula_deriv_smul_nullHomologous`](https://taucetiproject.org/docs/TauCeti/Analysis/Contour/Cycle/Residue.html#TauCeti.Contour.Cycle.cauchyIntegralFormula_deriv_smul_nullHomologous).

```lean
TauCeti.Contour.Cycle.cauchyIntegralFormula_deriv_smul_nullHomologous.{u_1} {U : Set ℂ}
  {E : Type u_1} [NormedAddCommGroup E] [NormedSpace ℂ E] [CompleteSpace E] {f : ℂ → E} {z : ℂ}
  (hU : IsOpen U) (hf : DifferentiableOn ℂ f U) {C : TauCeti.Contour.Cycle} (hCU : C.IsIn U)
  (hnull : C.IsNullHomologous U) (hz : z ∈ U) (hoff : z ∉ C.trace) :
  (TauCeti.Contour.Cycle.integral fun w => ((w - z) ^ 2)⁻¹ • f w) C =
    (2 * ↑Real.pi * Complex.I * (TauCeti.Contour.Cycle.windingNumber z) C) • deriv f z
```

**Cauchy's integral formula for a cycle, for a Banach-valued function.** Formalized in Tau Ceti as [`TauCeti.Contour.Cycle.cauchyIntegralFormula_smul_nullHomologous`](https://taucetiproject.org/docs/TauCeti/Analysis/Contour/Cycle/Residue.html#TauCeti.Contour.Cycle.cauchyIntegralFormula_smul_nullHomologous).

```lean
TauCeti.Contour.Cycle.cauchyIntegralFormula_smul_nullHomologous.{u_1} {U : Set ℂ} {E : Type u_1}
  [NormedAddCommGroup E] [NormedSpace ℂ E] [CompleteSpace E] {f : ℂ → E} {z : ℂ} (hU : IsOpen U)
  (hf : DifferentiableOn ℂ f U) {C : TauCeti.Contour.Cycle} (hCU : C.IsIn U)
  (hnull : C.IsNullHomologous U) (hz : z ∈ U) (hoff : z ∉ C.trace) :
  (TauCeti.Contour.Cycle.integral fun w => (w - z)⁻¹ • f w) C =
    (2 * ↑Real.pi * Complex.I * (TauCeti.Contour.Cycle.windingNumber z) C) • f z
```

**Cauchy's integral formula for a cycle, for the `k`-th derivative.** Formalized in Tau Ceti as [`TauCeti.Contour.Cycle.cauchyIntegralFormula_iteratedDeriv_nullHomologous`](https://taucetiproject.org/docs/TauCeti/Analysis/Contour/Cycle/Residue.html#TauCeti.Contour.Cycle.cauchyIntegralFormula_iteratedDeriv_nullHomologous).

```lean
TauCeti.Contour.Cycle.cauchyIntegralFormula_iteratedDeriv_nullHomologous {f : ℂ → ℂ} {U : Set ℂ}
  {z : ℂ} (hU : IsOpen U) (hf : DifferentiableOn ℂ f U) {C : TauCeti.Contour.Cycle} (hCU : C.IsIn U)
  (hnull : C.IsNullHomologous U) (hz : z ∈ U) (hoff : z ∉ C.trace) (k : ℕ) :
  (TauCeti.Contour.Cycle.integral fun w => f w / (w - z) ^ (k + 1)) C =
    2 * ↑Real.pi * Complex.I * (TauCeti.Contour.Cycle.windingNumber z) C *
      (iteratedDeriv k f z / ↑k.factorial)
```

**Cauchy's integral formula for a cycle, for the `k`-th derivative of a Banach-valued function.** Formalized in Tau Ceti as [`TauCeti.Contour.Cycle.cauchyIntegralFormula_iteratedDeriv_smul_nullHomologous`](https://taucetiproject.org/docs/TauCeti/Analysis/Contour/Cycle/Residue.html#TauCeti.Contour.Cycle.cauchyIntegralFormula_iteratedDeriv_smul_nullHomologous).

```lean
TauCeti.Contour.Cycle.cauchyIntegralFormula_iteratedDeriv_smul_nullHomologous.{u_1} {U : Set ℂ}
  {E : Type u_1} [NormedAddCommGroup E] [NormedSpace ℂ E] [CompleteSpace E] {f : ℂ → E} {z : ℂ}
  (hU : IsOpen U) (hf : DifferentiableOn ℂ f U) {C : TauCeti.Contour.Cycle} (hCU : C.IsIn U)
  (hnull : C.IsNullHomologous U) (hz : z ∈ U) (hoff : z ∉ C.trace) (k : ℕ) :
  (TauCeti.Contour.Cycle.integral fun w => ((w - z) ^ (k + 1))⁻¹ • f w) C =
    (2 * ↑Real.pi * Complex.I * (TauCeti.Contour.Cycle.windingNumber z) C / ↑k.factorial) •
      iteratedDeriv k f z
```

**Cauchy's integral formula for the first derivative, homology form.** Formalized in Tau Ceti as [`TauCeti.Contour.cauchyIntegralFormula_deriv_nullHomologous`](https://taucetiproject.org/docs/TauCeti/Analysis/Contour/Cauchy/HomologyFormula.html#TauCeti.Contour.cauchyIntegralFormula_deriv_nullHomologous).

```lean
TauCeti.Contour.cauchyIntegralFormula_deriv_nullHomologous {f : ℂ → ℂ} {U : Set ℂ} {γ : ℝ → ℂ}
  {a b : ℝ} {z : ℂ} (hU : IsOpen U) (hf : DifferentiableOn ℂ f U)
  (hγ : TauCeti.IsPiecewiseC1On γ a b) (hγU : ∀ t ∈ Set.uIcc a b, γ t ∈ U) (hclosed : γ a = γ b)
  (hnull : TauCeti.Contour.IsNullHomologous γ a b U) (hz : z ∈ U)
  (hoff : ∀ t ∈ Set.uIcc a b, γ t ≠ z) :
  ∫ (t : ℝ) in a..b, deriv γ t • (f (γ t) / (γ t - z) ^ 2) =
    2 * ↑Real.pi * Complex.I * TauCeti.Contour.windingNumber γ a b z * deriv f z
```

**Cauchy's integral formula from pointwise Dixon-vanishing.** Formalized in Tau Ceti as [`TauCeti.Contour.dixonH2_eq_windingNumber_mul_f_of_dixonFunction_eq_zero`](https://taucetiproject.org/docs/TauCeti/Analysis/Contour/Cauchy/IntegralFormula.html#TauCeti.Contour.dixonH2_eq_windingNumber_mul_f_of_dixonFunction_eq_zero).

```lean
TauCeti.Contour.dixonH2_eq_windingNumber_mul_f_of_dixonFunction_eq_zero {f : ℂ → ℂ} {U : Set ℂ}
  {γ : ℝ → ℂ} {a b : ℝ} {w : ℂ} (h_cont : ContinuousOn γ (Set.uIcc a b)) (hw : w ∈ U)
  (hoff : ∀ t ∈ Set.uIcc a b, γ t ≠ w) (h_zero_at : TauCeti.Contour.dixonFunction f U γ a b w = 0)
  (h_cauchy_int :
    IntervalIntegrable (fun t => f (γ t) / (γ t - w) * deriv γ t) MeasureTheory.volume a b)
  (h_base_int : IntervalIntegrable (fun t => (γ t - w)⁻¹ * deriv γ t) MeasureTheory.volume a b) :
  TauCeti.Contour.dixonH2 f γ a b w =
    2 * ↑Real.pi * Complex.I * TauCeti.Contour.windingNumber γ a b w * f w
```

**Cauchy's integral formula on a disc.** Formalized in Tau Ceti as [`TauCeti.Contour.cauchyIntegralFormula_ball`](https://taucetiproject.org/docs/TauCeti/Analysis/Contour/StarConvex.html#TauCeti.Contour.cauchyIntegralFormula_ball).

```lean
TauCeti.Contour.cauchyIntegralFormula_ball {f : ℂ → ℂ} {γ : ℝ → ℂ} {a b : ℝ} {c : ℂ} {r : ℝ} {z : ℂ}
  (hf : DifferentiableOn ℂ f (Metric.ball c r)) (hγ : TauCeti.IsPiecewiseC1On γ a b)
  (hγr : ∀ t ∈ Set.uIcc a b, γ t ∈ Metric.ball c r) (hclosed : γ a = γ b) (hz : z ∈ Metric.ball c r)
  (hoff : ∀ t ∈ Set.uIcc a b, γ t ≠ z) :
  ∫ (t : ℝ) in a..b, deriv γ t • (f (γ t) / (γ t - z)) =
    2 * ↑Real.pi * Complex.I * TauCeti.Contour.windingNumber γ a b z * f z
```

**Cauchy's integral formula on a disc, for the `k`-th derivative.** Formalized in Tau Ceti as [`TauCeti.Contour.cauchyIntegralFormula_iteratedDeriv_ball`](https://taucetiproject.org/docs/TauCeti/Analysis/Contour/StarConvex.html#TauCeti.Contour.cauchyIntegralFormula_iteratedDeriv_ball).

```lean
TauCeti.Contour.cauchyIntegralFormula_iteratedDeriv_ball {f : ℂ → ℂ} {γ : ℝ → ℂ} {a b : ℝ} {c : ℂ}
  {r : ℝ} {z : ℂ} (hf : DifferentiableOn ℂ f (Metric.ball c r)) (hγ : TauCeti.IsPiecewiseC1On γ a b)
  (hγr : ∀ t ∈ Set.uIcc a b, γ t ∈ Metric.ball c r) (hclosed : γ a = γ b) (hz : z ∈ Metric.ball c r)
  (hoff : ∀ t ∈ Set.uIcc a b, γ t ≠ z) (k : ℕ) :
  ∫ (t : ℝ) in a..b, deriv γ t • (f (γ t) / (γ t - z) ^ (k + 1)) =
    2 * ↑Real.pi * Complex.I * TauCeti.Contour.windingNumber γ a b z *
      (iteratedDeriv k f z / ↑k.factorial)
```

**Cauchy's integral formula on a star-shaped open set.** Formalized in Tau Ceti as [`TauCeti.Contour.cauchyIntegralFormula_starConvex`](https://taucetiproject.org/docs/TauCeti/Analysis/Contour/StarConvex.html#TauCeti.Contour.cauchyIntegralFormula_starConvex).

```lean
TauCeti.Contour.cauchyIntegralFormula_starConvex {f : ℂ → ℂ} {Ω : Set ℂ} {γ : ℝ → ℂ} {a b : ℝ}
  {x z : ℂ} (hstar : StarConvex ℝ x Ω) (hopen : IsOpen Ω) (hf : DifferentiableOn ℂ f Ω)
  (hγ : TauCeti.IsPiecewiseC1On γ a b) (hγΩ : ∀ t ∈ Set.uIcc a b, γ t ∈ Ω) (hclosed : γ a = γ b)
  (hz : z ∈ Ω) (hoff : ∀ t ∈ Set.uIcc a b, γ t ≠ z) :
  ∫ (t : ℝ) in a..b, deriv γ t • (f (γ t) / (γ t - z)) =
    2 * ↑Real.pi * Complex.I * TauCeti.Contour.windingNumber γ a b z * f z
```

**Cauchy's integral formula on a star-shaped open set, for the `k`-th derivative.** Formalized in Tau Ceti as [`TauCeti.Contour.cauchyIntegralFormula_iteratedDeriv_starConvex`](https://taucetiproject.org/docs/TauCeti/Analysis/Contour/StarConvex.html#TauCeti.Contour.cauchyIntegralFormula_iteratedDeriv_starConvex).

```lean
TauCeti.Contour.cauchyIntegralFormula_iteratedDeriv_starConvex {f : ℂ → ℂ} {Ω : Set ℂ} {γ : ℝ → ℂ}
  {a b : ℝ} {x z : ℂ} (hstar : StarConvex ℝ x Ω) (hopen : IsOpen Ω) (hf : DifferentiableOn ℂ f Ω)
  (hγ : TauCeti.IsPiecewiseC1On γ a b) (hγΩ : ∀ t ∈ Set.uIcc a b, γ t ∈ Ω) (hclosed : γ a = γ b)
  (hz : z ∈ Ω) (hoff : ∀ t ∈ Set.uIcc a b, γ t ≠ z) (k : ℕ) :
  ∫ (t : ℝ) in a..b, deriv γ t • (f (γ t) / (γ t - z) ^ (k + 1)) =
    2 * ↑Real.pi * Complex.I * TauCeti.Contour.windingNumber γ a b z *
      (iteratedDeriv k f z / ↑k.factorial)
```

**Cauchy's integral formula, homology form.** Formalized in Tau Ceti as [`TauCeti.Contour.cauchyIntegralFormula_nullHomologous`](https://taucetiproject.org/docs/TauCeti/Analysis/Contour/Cauchy/HomologyFormula.html#TauCeti.Contour.cauchyIntegralFormula_nullHomologous).

```lean
TauCeti.Contour.cauchyIntegralFormula_nullHomologous {f : ℂ → ℂ} {U : Set ℂ} {γ : ℝ → ℂ} {a b : ℝ}
  {z : ℂ} (hU : IsOpen U) (hf : DifferentiableOn ℂ f U) (hγ : TauCeti.IsPiecewiseC1On γ a b)
  (hγU : ∀ t ∈ Set.uIcc a b, γ t ∈ U) (hclosed : γ a = γ b)
  (hnull : TauCeti.Contour.IsNullHomologous γ a b U) (hz : z ∈ U)
  (hoff : ∀ t ∈ Set.uIcc a b, γ t ≠ z) :
  ∫ (t : ℝ) in a..b, deriv γ t • (f (γ t) / (γ t - z)) =
    2 * ↑Real.pi * Complex.I * TauCeti.Contour.windingNumber γ a b z * f z
```

## Sources

- [Tau Ceti documentation: `TauCeti.Contour.cauchyIntegralFormula_iteratedDeriv_nullHomologous`](https://taucetiproject.org/docs/TauCeti/Analysis/Contour/Cauchy/HomologyFormula.html#TauCeti.Contour.cauchyIntegralFormula_iteratedDeriv_nullHomologous)
- [Source of `TauCeti.Contour.cauchyIntegralFormula_iteratedDeriv_nullHomologous` in TauCeti/Analysis/Contour/Cauchy/HomologyFormula.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Contour/Cauchy/HomologyFormula.lean#L71)
- [Tau Ceti roadmap status: Contour integration and the Hungerbühler–Wasem generalized residue theorem](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/ContourIntegration/STATUS.md)
