---
declaration: module
origin: cited
lean: fderiv_uncurry, fderiv_curry_fst, fderiv_curry_snd, fderiv_uncurry_clm_comp, fderiv_wrt_prod, fderiv_wrt_prod_clm_comp, fderiv_curry_clm_apply, fderiv_uncurry_comp_fst
statement: formalized
proof: formalized
---

# fderiv currying lemmas

The module `Physlib.Mathematics.ForMathlib.FDerivCurry`, [Physlib/Mathematics/ForMathlib/FDerivCurry.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/FDerivCurry.lean): 24 declarations, none with a docstring.

> Various lemmas related to fderiv on curried/uncurried functions.

**`fderiv_uncurry`**, a lemma, [line 22](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/FDerivCurry.lean#L22).

```lean
lemma fderiv_uncurry (f : X → Y → Z) (xy dxy : X × Y)
    (hf : DifferentiableAt 𝕜 (↿f) xy) :
    fderiv 𝕜 ↿f xy dxy
    =
    fderiv 𝕜 (f · xy.2) xy.1 dxy.1 + fderiv 𝕜 (f xy.1 ·) xy.2 dxy.2
```

**`fderiv_curry_fst`**, a lemma, [line 37](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/FDerivCurry.lean#L37).

```lean
lemma fderiv_curry_fst (f : X × Y → Z) (x : X) (y : Y)
    (h : DifferentiableAt 𝕜 f (x,y)) (dx : X) :
    fderiv 𝕜 (fun x' => Function.curry f x' y) x dx = fderiv 𝕜 f (x,y) (dx, 0)
```

**`fderiv_curry_snd`**, a lemma, [line 49](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/FDerivCurry.lean#L49).

```lean
lemma fderiv_curry_snd (f : X × Y → Z) (x : X) (y : Y)
    (h : DifferentiableAt 𝕜 f (x,y)) (dy : Y) :
    fderiv 𝕜 (Function.curry f x) y dy = fderiv 𝕜 (f) (x,y) (0, dy)
```

**`fderiv_uncurry_clm_comp`**, a lemma, [line 62](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/FDerivCurry.lean#L62).

```lean
lemma fderiv_uncurry_clm_comp (f : X → Y → Z) (hf : Differentiable 𝕜 (↿f)) :
    fderiv 𝕜 ↿f
    =
    fun xy =>
      (fderiv 𝕜 (f · xy.2) xy.1).comp (ContinuousLinearMap.fst 𝕜 X Y)
      +
      (fderiv 𝕜 (f xy.1 ·) xy.2).comp (ContinuousLinearMap.snd 𝕜 X Y)
```

**`fderiv_wrt_prod`**, a lemma, [line 77](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/FDerivCurry.lean#L77).

```lean
lemma fderiv_wrt_prod {f : X × Y → Z} {xy} (hf : DifferentiableAt 𝕜 f xy) :
    fderiv 𝕜 f xy
    =
    (fderiv 𝕜 (fun x' => f (x',xy.2)) xy.1).comp (ContinuousLinearMap.fst 𝕜 X Y)
    +
    (fderiv 𝕜 (fun y' => f (xy.1,y')) xy.2).comp (ContinuousLinearMap.snd 𝕜 X Y)
```

**`fderiv_wrt_prod_clm_comp`**, a lemma, [line 86](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/FDerivCurry.lean#L86).

```lean
lemma fderiv_wrt_prod_clm_comp (f : X × Y → Z) (hf : Differentiable 𝕜 f) :
    fderiv 𝕜 f
    =
    fun xy =>
      (fderiv 𝕜 (fun x' => f (x',xy.2)) xy.1).comp (ContinuousLinearMap.fst 𝕜 X Y)
      +
      (fderiv 𝕜 (fun y' => f (xy.1,y')) xy.2).comp (ContinuousLinearMap.snd 𝕜 X Y)
```

**`fderiv_curry_clm_apply`**, a lemma, [line 95](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/FDerivCurry.lean#L95).

```lean
lemma fderiv_curry_clm_apply (f : X → Y →L[𝕜] Z) (y : Y) (x dx : X) (h : Differentiable 𝕜 f) :
    fderiv 𝕜 f x dx y
    =
    fderiv 𝕜 (f · y) x dx
```

**`fderiv_uncurry_comp_fst`**, a lemma, [line 102](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/FDerivCurry.lean#L102).

```lean
lemma fderiv_uncurry_comp_fst (f : X → Y → Z) (y : Y) (hf : Differentiable 𝕜 (↿f)) :
    fderiv 𝕜 (fun x' => (↿f) (x', y))
    =
    fun x => (fderiv 𝕜 (↿f) ((·, y) x)).comp (fderiv 𝕜 (·, y) x)
```

**`fderiv_uncurry_comp_snd`**, a lemma, [line 114](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/FDerivCurry.lean#L114).

```lean
lemma fderiv_uncurry_comp_snd (f : X → Y → Z) (x : X) (hf : Differentiable 𝕜 (↿f)) :
    fderiv 𝕜 (fun y' => (↿f) (x, y'))
    =
    fun y => (fderiv 𝕜 (↿f) ((x, ·) y)).comp (fderiv 𝕜 (x, ·) y)
```

**`fderiv_curry_comp_fst`**, a lemma, [line 126](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/FDerivCurry.lean#L126).

```lean
lemma fderiv_curry_comp_fst (f : X → Y → Z) (x dx : X) (y : Y)
    (hf : Differentiable 𝕜 (↿f)) :
    (fderiv 𝕜 (fun x' => f x' y) x) dx
    =
    (fderiv 𝕜 (↿f) ((·, y) x)) ((fderiv 𝕜 (·, y) x) dx)
```

**`fderiv_curry_comp_snd`**, a lemma, [line 139](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/FDerivCurry.lean#L139).

```lean
lemma fderiv_curry_comp_snd (f : X → Y → Z) (x : X) (y dy : Y)
    (hf : Differentiable 𝕜 (↿f)) :
    (fderiv 𝕜 (fun y' => f x y') y) dy
    =
    (fderiv 𝕜 (↿f) ((x, ·) y)) ((fderiv 𝕜 (x, ·) y) dy)
```

**`fderiv_inr_fst_clm`**, a lemma, [line 152](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/FDerivCurry.lean#L152).

```lean
lemma fderiv_inr_fst_clm (x : X) (y : Y) :
    (fderiv 𝕜 (x, ·) y) = ContinuousLinearMap.inr 𝕜 X Y
```

**`fderiv_inl_snd_clm`**, a lemma, [line 156](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/FDerivCurry.lean#L156).

```lean
lemma fderiv_inl_snd_clm (x : X) (y : Y) :
    (fderiv 𝕜 (·, y) x) = ContinuousLinearMap.inl 𝕜 X Y
```

**`function_differentiableAt_fst`**, a lemma, [line 162](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/FDerivCurry.lean#L162).

```lean
lemma function_differentiableAt_fst (f : X → Y → Z) (x : X) (y : Y) (hf : Differentiable 𝕜 (↿f)) :
    DifferentiableAt 𝕜 (fun x' => f x' y) x
```

**`function_differentiableAt_snd`**, a lemma, [line 171](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/FDerivCurry.lean#L171).

```lean
lemma function_differentiableAt_snd (f : X → Y → Z) (x : X) (y : Y) (hf : Differentiable 𝕜 (↿f)) :
    DifferentiableAt 𝕜 (fun y' => f x y') y
```

**`fderiv_uncurry_differentiable_fst`**, a lemma, [line 181](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/FDerivCurry.lean#L181).

```lean
lemma fderiv_uncurry_differentiable_fst (f : X → Y → Z) (y : Y) (hf : ContDiff 𝕜 2 ↿f) :
    Differentiable 𝕜 (fderiv 𝕜 fun x' => (↿f) (x', y))
```

**`fderiv_uncurry_differentiable_snd`**, a lemma, [line 186](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/FDerivCurry.lean#L186).

```lean
lemma fderiv_uncurry_differentiable_snd (f : X → Y → Z) (x : X) (hf : ContDiff 𝕜 2 ↿f) :
    Differentiable 𝕜 (fderiv 𝕜 fun y' => (↿f) (x, y'))
```

**`fderiv_uncurry_differentiable_fst_comp_snd`**, a lemma, [line 191](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/FDerivCurry.lean#L191).

```lean
lemma fderiv_uncurry_differentiable_fst_comp_snd (f : X → Y → Z) (x : X) (hf : ContDiff 𝕜 2 ↿f) :
    Differentiable 𝕜 (fun y' => fderiv 𝕜 (fun x' => (↿f) (x', y')) x)
```

**`fderiv_uncurry_differentiable_fst_comp_snd_apply`**, a lemma, [line 196](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/FDerivCurry.lean#L196).

```lean
lemma fderiv_uncurry_differentiable_fst_comp_snd_apply (f : X → Y → Z) (x δx : X)
    (hf : ContDiff 𝕜 2 ↿f) :
    Differentiable 𝕜 (fun y' => fderiv 𝕜 (fun x' => (↿f) (x', y')) x δx)
```

**`fderiv_uncurry_differentiable_snd_comp_fst`**, a lemma, [line 202](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/FDerivCurry.lean#L202).

```lean
lemma fderiv_uncurry_differentiable_snd_comp_fst (f : X → Y → Z) (y : Y) (hf : ContDiff 𝕜 2 ↿f) :
    Differentiable 𝕜 (fun x' => fderiv 𝕜 (fun y' => (↿f) (x', y')) y)
```

**`fderiv_uncurry_differentiable_snd_comp_fst_apply`**, a lemma, [line 207](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/FDerivCurry.lean#L207).

```lean
lemma fderiv_uncurry_differentiable_snd_comp_fst_apply (f : X → Y → Z) (y δy : Y)
    (hf : ContDiff 𝕜 2 ↿f) :
    Differentiable 𝕜 (fun x' => fderiv 𝕜 (fun y' => (↿f) (x', y')) y δy)
```

**`fderiv_curry_differentiableAt_fst_comp_snd`**, a lemma, [line 213](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/FDerivCurry.lean#L213).

```lean
lemma fderiv_curry_differentiableAt_fst_comp_snd (f : X → Y → Z) (x dx : X) (y : Y)
    (hf : ContDiff 𝕜 2 ↿f) :
    DifferentiableAt 𝕜 (fun y' => (fderiv 𝕜 (fun x' => f x' y') x) dx) y
```

**`fderiv_curry_differentiableAt_snd_comp_fst`**, a lemma, [line 219](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/FDerivCurry.lean#L219).

```lean
lemma fderiv_curry_differentiableAt_snd_comp_fst (f : X → Y → Z) (x : X) (y dy : Y)
    (hf : ContDiff 𝕜 2 ↿f) :
    DifferentiableAt 𝕜 (fun x' => (fderiv 𝕜 (fun y' => f x' y') y) dy) x
```

**`fderiv_swap`**, a lemma, [line 226](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/FDerivCurry.lean#L226).

```lean
lemma fderiv_swap [IsRCLikeNormedField 𝕜] (f : X → Y → Z) (x dx : X) (y dy : Y)
    (hf : ContDiff 𝕜 2 ↿f) :
    fderiv 𝕜 (fun x' => fderiv 𝕜 (fun y' => f x' y') y dy) x dx
    =
    fderiv 𝕜 (fun y' => fderiv 𝕜 (fun x' => f x' y') x dx) y dy
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [Physlib/Mathematics/ForMathlib/FDerivCurry.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/ForMathlib/FDerivCurry.lean)
