---
declaration: module
origin: cited
lean: analyticAt_complexLaplaceIntegrand, eventually_integrable_complexLaplaceIntegrand_of_mem_interior_convergenceDomain, analyticAt_complexLaplaceTransform_of_mem_interior_convergenceDomain, ComplexLaplaceIntegrand, ComplexLaplaceTransform, ComplexLaplaceConvergenceDomain, measurable_complexLaplaceIntegrand, continuousAt_complexLaplaceTransform_of_mem_interior_convergenceDomain
statement: formalized
proof: formalized
---

# QuantumInfo.ForMathlib.ComplexLaplaceTransform

The module `QuantumInfo.ForMathlib.ComplexLaplaceTransform`, [QuantumInfo/ForMathlib/ComplexLaplaceTransform.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/ComplexLaplaceTransform.lean): 9 declarations, 6 with a docstring, 3 listed as significant; 8 private, not shown.

**`ComplexLaplaceIntegrand`**, a def, [line 18](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/ComplexLaplaceTransform.lean#L18).

> The integrand of the complex Laplace transform of a possibly infinite-valued energy function.

```lean
def ComplexLaplaceIntegrand {α : Type*} (E : α → WithTop ℝ) (z : ℂ) (x : α) : ℂ
```

**`ComplexLaplaceTransform`**, a def, [line 22](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/ComplexLaplaceTransform.lean#L22).

> The complex Laplace transform of a possibly infinite-valued energy function.

```lean
def ComplexLaplaceTransform {α : Type*} [MeasureTheory.MeasureSpace α]
    (E : α → WithTop ℝ) (z : ℂ) : ℂ
```

**`ComplexLaplaceConvergenceDomain`**, a def, [line 27](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/ComplexLaplaceTransform.lean#L27).

> The complex convergence domain of a Laplace transform.

```lean
def ComplexLaplaceConvergenceDomain {α : Type*} [MeasureTheory.MeasureSpace α]
    (E : α → WithTop ℝ) : Set ℂ
```

**`analyticAt_complexLaplaceIntegrand`**, a theorem, [line 116](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/ComplexLaplaceTransform.lean#L116). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> For each configuration, the complex Laplace integrand is analytic in the parameter.

```lean
theorem analyticAt_complexLaplaceIntegrand
    {α : Type*} (E : α → WithTop ℝ) (x : α) (z : ℂ) :
    AnalyticAt ℂ (fun w : ℂ => ComplexLaplaceIntegrand E w x) z
```

**`measurable_complexLaplaceIntegrand`**, a lemma, [line 124](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/ComplexLaplaceTransform.lean#L124).

```lean
lemma measurable_complexLaplaceIntegrand
    {α : Type*} [MeasurableSpace α] {E : α → WithTop ℝ} (hE : Measurable E) (z : ℂ) :
    Measurable (ComplexLaplaceIntegrand E z)
```

**`eventually_integrable_complexLaplaceIntegrand_of_mem_interior_convergenceDomain`**, a theorem, [line 151](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/ComplexLaplaceTransform.lean#L151). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> Interior convergence gives integrability throughout a neighborhood of the parameter.

```lean
theorem eventually_integrable_complexLaplaceIntegrand_of_mem_interior_convergenceDomain
    {α : Type*} [MeasureTheory.MeasureSpace α] {E : α → WithTop ℝ} {z : ℂ}
    (hz : z ∈ interior (ComplexLaplaceConvergenceDomain E)) :
    ∀ᶠ w in nhds z,
      MeasureTheory.Integrable (μ := MeasureTheory.volume) (ComplexLaplaceIntegrand E w)
```

**`continuousAt_complexLaplaceTransform_of_mem_interior_convergenceDomain`**, a lemma, [line 158](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/ComplexLaplaceTransform.lean#L158).

```lean
lemma continuousAt_complexLaplaceTransform_of_mem_interior_convergenceDomain
    {α : Type*} [MeasureTheory.MeasureSpace α] {E : α → WithTop ℝ} {z : ℂ}
    (hz : z ∈ interior (ComplexLaplaceConvergenceDomain E)) :
    ContinuousAt (ComplexLaplaceTransform E) z
```

**`continuousOn_complexLaplaceTransform_interior_convergenceDomain`**, a lemma, [line 188](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/ComplexLaplaceTransform.lean#L188).

```lean
lemma continuousOn_complexLaplaceTransform_interior_convergenceDomain
    {α : Type*} [MeasureTheory.MeasureSpace α] {E : α → WithTop ℝ} :
    ContinuousOn (ComplexLaplaceTransform E) (interior (ComplexLaplaceConvergenceDomain E))
```

**`analyticAt_complexLaplaceTransform_of_mem_interior_convergenceDomain`**, a theorem, [line 306](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/ComplexLaplaceTransform.lean#L306). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> A complex Laplace transform is analytic on the interior of its convergence domain.

```lean
theorem analyticAt_complexLaplaceTransform_of_mem_interior_convergenceDomain
    {α : Type*} [MeasureTheory.MeasureSpace α]
    [MeasureTheory.SFinite (MeasureTheory.volume : MeasureTheory.Measure α)] {E : α → WithTop ℝ} {z : ℂ}
    (hE : Measurable E)
    (hz : z ∈ interior (ComplexLaplaceConvergenceDomain E)) :
    AnalyticAt ℂ (ComplexLaplaceTransform E) z
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [QuantumInfo/ForMathlib/ComplexLaplaceTransform.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/ComplexLaplaceTransform.lean)
