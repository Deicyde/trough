---
declaration: module
origin: cited
lean: QuantumMechanics.OneDimension.HilbertSpace.gaussian_integrable, QuantumMechanics.OneDimension.HilbertSpace.gaussian_aestronglyMeasurable, QuantumMechanics.OneDimension.HilbertSpace.gaussian_memHS, QuantumMechanics.OneDimension.HilbertSpace.exp_mul_gaussian_integrable, QuantumMechanics.OneDimension.HilbertSpace.exp_abs_mul_gaussian_integrable, QuantumMechanics.OneDimension.HilbertSpace.mul_gaussian_mem_Lp_one, QuantumMechanics.OneDimension.HilbertSpace.mul_gaussian_mem_Lp_two, QuantumMechanics.OneDimension.HilbertSpace.abs_mul_gaussian_integrable
statement: formalized
proof: formalized
---

# Gaussians and the hilbert space

The module `Physlib.QuantumMechanics.HilbertSpaces.OneDimension.Gaussians`, [Physlib/QuantumMechanics/HilbertSpaces/OneDimension/Gaussians.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/OneDimension/Gaussians.lean): 10 declarations, none with a docstring.

## Gaussians

**`QuantumMechanics.OneDimension.HilbertSpace.gaussian_integrable`**, a lemma, [line 41](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/OneDimension/Gaussians.lean#L41).

```lean
lemma gaussian_integrable {b : ℝ} (c : ℝ) (hb : 0 < b) :
    MeasureTheory.Integrable (fun x => (Real.exp (- b * (x - c)^ 2) : ℂ))
```

**`QuantumMechanics.OneDimension.HilbertSpace.gaussian_aestronglyMeasurable`**, a lemma, [line 46](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/OneDimension/Gaussians.lean#L46).

```lean
lemma gaussian_aestronglyMeasurable {b : ℝ} (c : ℝ) (hb : 0 < b) :
    AEStronglyMeasurable (fun x => (Real.exp (- b * (x - c) ^2) : ℂ)) volume
```

**`QuantumMechanics.OneDimension.HilbertSpace.gaussian_memHS`**, a lemma, [line 50](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/OneDimension/Gaussians.lean#L50).

```lean
lemma gaussian_memHS {b : ℝ} (c : ℝ) (hb : 0 < b) :
    MemHS (fun x => (Real.exp (- b * (x - c) ^2) : ℂ))
```

**`QuantumMechanics.OneDimension.HilbertSpace.exp_mul_gaussian_integrable`**, a lemma, [line 72](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/OneDimension/Gaussians.lean#L72).

```lean
lemma exp_mul_gaussian_integrable (b c : ℝ) (hb : 0 < b) :
    MeasureTheory.Integrable (fun x => Real.exp (c * x) * Real.exp (- b * x ^ 2))
```

**`QuantumMechanics.OneDimension.HilbertSpace.exp_abs_mul_gaussian_integrable`**, a lemma, [line 86](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/OneDimension/Gaussians.lean#L86).

```lean
lemma exp_abs_mul_gaussian_integrable (b c : ℝ) (hb : 0 < b) :
    MeasureTheory.Integrable (fun x => Real.exp (|c * x|) * Real.exp (- b * x ^ 2))
```

**`QuantumMechanics.OneDimension.HilbertSpace.mul_gaussian_mem_Lp_one`**, a lemma, [line 112](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/OneDimension/Gaussians.lean#L112).

```lean
lemma mul_gaussian_mem_Lp_one (f : ℝ → ℂ) (hf : MemHS f) (b c : ℝ) (hb : 0 < b) :
    MeasureTheory.MemLp (fun x => f x * Real.exp (- b * (x - c) ^ 2)) 1 volume
```

**`QuantumMechanics.OneDimension.HilbertSpace.mul_gaussian_mem_Lp_two`**, a lemma, [line 130](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/OneDimension/Gaussians.lean#L130).

```lean
lemma mul_gaussian_mem_Lp_two (f : ℝ → ℂ) (hf : MemHS f) (b c : ℝ) (hb : 0 < b) :
    MeasureTheory.MemLp (fun x => f x * Real.exp (- b * (x - c) ^ 2)) 2 volume
```

**`QuantumMechanics.OneDimension.HilbertSpace.abs_mul_gaussian_integrable`**, a lemma, [line 145](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/OneDimension/Gaussians.lean#L145).

```lean
lemma abs_mul_gaussian_integrable (f : ℝ → ℂ) (hf : MemHS f) (b c : ℝ) (hb : 0 < b) :
    MeasureTheory.Integrable (fun x => norm (f x) * Real.exp (- b * (x - c)^2))
```

**`QuantumMechanics.OneDimension.HilbertSpace.exp_mul_abs_mul_gaussian_integrable`**, a lemma, [line 161](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/OneDimension/Gaussians.lean#L161).

```lean
lemma exp_mul_abs_mul_gaussian_integrable (f : ℝ → ℂ) (hf : MemHS f)
    (b c : ℝ) (hb : 0 < b) : MeasureTheory.Integrable
    (fun x => Real.exp (c * x) * norm (f x) * Real.exp (- b * x ^ 2))
```

**`QuantumMechanics.OneDimension.HilbertSpace.exp_abs_mul_abs_mul_gaussian_integrable`**, a lemma, [line 181](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/OneDimension/Gaussians.lean#L181).

```lean
lemma exp_abs_mul_abs_mul_gaussian_integrable (f : ℝ → ℂ) (hf : MemHS f) (b c : ℝ) (hb : 0 < b) :
    MeasureTheory.Integrable
    (fun x => Real.exp (|c * x|) * norm (f x) * Real.exp (- b * x ^ 2))
```

## Depends on

- [Hilbert space for one dimension quantum mechanics](onedimension-basic.md)

## Sources

- [Physlib/QuantumMechanics/HilbertSpaces/OneDimension/Gaussians.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/OneDimension/Gaussians.lean)
