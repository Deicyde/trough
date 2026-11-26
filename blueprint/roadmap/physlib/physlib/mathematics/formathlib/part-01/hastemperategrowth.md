---
declaration: module
origin: cited
lean: Function.HasTemperateGrowth.prod, Function.HasTemperateGrowth.fderiv, Function.HasTemperateGrowth.polynomial_eval, Function.HasTemperateGrowth.integrable_mul_schwartzMap
statement: formalized
proof: formalized
---

# Functions of temperate growth

The module `Physlib.Mathematics.ForMathlib.HasTemperateGrowth`, [Physlib/Mathematics/ForMathlib/HasTemperateGrowth.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/Mathematics/ForMathlib/HasTemperateGrowth.lean): 4 declarations, 4 with a docstring.

> This file is intended to collect useful general properties of `HasTemperateGrowth` which are not
> (yet) in Mathlib.

**`Function.HasTemperateGrowth.prod`**, a lemma, [line 26](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/Mathematics/ForMathlib/HasTemperateGrowth.lean#L26).

> The finite product of functions of temperate growth is again of temperate growth.

```lean
lemma prod {ι : Type*} {s : Finset ι} {E F : Type*} [NormedAddCommGroup E]
    [NormedSpace ℝ E] [NormedCommRing F] [NormedAlgebra ℝ F] {f : ι → E → F}
    (hf : ∀ i ∈ s, HasTemperateGrowth (f i)) : HasTemperateGrowth (∏ i ∈ s, f i)
```

**`Function.HasTemperateGrowth.fderiv`**, a lemma, [line 37](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/Mathematics/ForMathlib/HasTemperateGrowth.lean#L37).

> The derivative of a function of temperate growth is again of temperate growth.

```lean
lemma fderiv {E F : Type*} [NormedAddCommGroup E] [NormedSpace ℝ E] [NormedAddCommGroup F]
    [NormedSpace ℝ F] {f : E → F} (hf : HasTemperateGrowth f) :
    HasTemperateGrowth (fderiv ℝ f)
```

**`Function.HasTemperateGrowth.polynomial_eval`**, a lemma, [line 45](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/Mathematics/ForMathlib/HasTemperateGrowth.lean#L45).

> A polynomial evaluated on a function of temperate growth is again of temperate growth.

```lean
lemma polynomial_eval {E F : Type*} [NormedAddCommGroup E] [NormedSpace ℝ E] [NormedCommRing F]
    [NormedAlgebra ℝ F] {f : E → F} (hf : HasTemperateGrowth f) (p : Polynomial F) :
    HasTemperateGrowth (fun x => p.eval (f x))
```

**`Function.HasTemperateGrowth.integrable_mul_schwartzMap`**, a lemma, [line 57](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/Mathematics/ForMathlib/HasTemperateGrowth.lean#L57).

> The product of a function of temperate growth and a Schwartz map is integrable.

```lean
lemma integrable_mul_schwartzMap {E : Type*} [NormedAddCommGroup E] [NormedSpace ℝ E]
    [MeasurableSpace E] [BorelSpace E] [SecondCountableTopology E] {μ : MeasureTheory.Measure E}
    [μ.HasTemperateGrowth] {g : E → ℂ} (hg : HasTemperateGrowth g) (ψ : SchwartzMap E ℂ) :
    MeasureTheory.Integrable (fun x => g x * ψ x) μ
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [Physlib/Mathematics/ForMathlib/HasTemperateGrowth.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/Mathematics/ForMathlib/HasTemperateGrowth.lean)
