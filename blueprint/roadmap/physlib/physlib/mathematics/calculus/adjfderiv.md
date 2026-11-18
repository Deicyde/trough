---
declaration: module
origin: cited
lean: adjFDeriv, HasAdjFDerivAt, HasAdjFDerivAt.adjFDeriv, DifferentiableAt.hasAdjFDerivAt, ContinuousLinearMap.adjoint.isBoundedBilinearMap_real, HasAdjFDerivAt.contDiffAt_deriv, gradient_eq_adjFDeriv, hasAdjFDerivAt_id
statement: formalized
proof: formalized
---

# Adjoint Fréchet derivative

The module `Physlib.Mathematics.Calculus.AdjFDeriv`, [Physlib/Mathematics/Calculus/AdjFDeriv.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Calculus/AdjFDeriv.lean): 33 declarations, 2 with a docstring.

> `adjFDeriv 𝕜 f x = (fderiv 𝕜 f x).adjoint`
>
> The main purpose of defining `adjFDeriv` is to compute `gradient f x = adjFDeriv 𝕜 f x 1`.
> The advantage of working with `adjFDeriv` is that we can formulate composition theorem.
>
> The reason why we do not want to compute `fderiv` and then `adjoint` is that to compute `fderiv 𝕜 f`
> or `adjoint f` we decompose `f = f₁ ∘ ... ∘ fₙ` and then apply composition theorem. The problem is
> that this decomposition has to be done differently for `fderiv` and `adjoint`. The problem is
> that when working with `fderiv` the natural product type is `X × Y` but when working with `adjoint`
> the natural product is `WithLp 2 (X × Y)`.
> For example:

**`adjFDeriv`**, a def, [line 49](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Calculus/AdjFDeriv.lean#L49).

> Adjoint Fréchet derivative
>
>   `adjFDeriv 𝕜 f x = (fderiv 𝕜 f x).adjoint`
>
> The main purpose of this function is to compute `gradient f x = adjFDeriv 𝕜 f x 1`. We provide
> easy to use API to compute `adjFDeriv`.

```lean
def adjFDeriv (f : E → F) (x : E) (dy : F) : E
```

**`HasAdjFDerivAt`**, a structure, [line 62](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Calculus/AdjFDeriv.lean#L62).

> Function `f` has adjoint Fréchet derivative `f'` at `x`
>
>   `f' = adjFDeriv 𝕜 f x = (fderiv 𝕜 f x).adjoint`
>
> The main purpose is to compute `gradient f x = f' 1 = adjFDeriv 𝕜 f x 1`.
>
> This structure is analogous to `HasFDerivAt` and it is often easier to use as theorems for
> `HasAdjFDeriv` do not require differentiability assumptions unlike theorems for `adjFDeriv`.

```lean
structure HasAdjFDerivAt (f : E → F) (f' : F → E) (x : E) where
  differentiableAt : DifferentiableAt 𝕜 f x
  hasAdjoint_fderiv : HasAdjoint 𝕜 (fderiv 𝕜 f x) f'
```

**`HasAdjFDerivAt.adjFDeriv`**, a lemma, [line 66](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Calculus/AdjFDeriv.lean#L66).

```lean
protected lemma HasAdjFDerivAt.adjFDeriv {f : E → F} {f'} {x} (hf : HasAdjFDerivAt 𝕜 f f' x) :
    adjFDeriv 𝕜 f x = f'
```

**`DifferentiableAt.hasAdjFDerivAt`**, a lemma, [line 72](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Calculus/AdjFDeriv.lean#L72).

```lean
protected lemma DifferentiableAt.hasAdjFDerivAt [CompleteSpace E] [CompleteSpace F]
    {f : E → F} {x} (hf : DifferentiableAt 𝕜 f x) :
    HasAdjFDerivAt 𝕜 f (adjFDeriv 𝕜 f x) x
```

**`ContinuousLinearMap.adjoint.isBoundedBilinearMap_real`**, a lemma, [line 88](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Calculus/AdjFDeriv.lean#L88).

```lean
lemma adjoint.isBoundedBilinearMap_real :
    IsBoundedBilinearMap ℝ (fun (fy : (X →L[ℝ] Y)×Y) => fy.1.adjoint fy.2)
```

**`HasAdjFDerivAt.contDiffAt_deriv`**, a lemma, [line 109](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Calculus/AdjFDeriv.lean#L109).

```lean
protected lemma HasAdjFDerivAt.contDiffAt_deriv
    {E : Type*} [NormedAddCommGroup E] [NormedSpace ℝ E]
    {F : Type*} [NormedAddCommGroup F] [NormedSpace ℝ F] [InnerProductSpace' ℝ F]
    {G : Type*} [NormedAddCommGroup G] [NormedSpace ℝ G] [InnerProductSpace' ℝ G]
    [CompleteSpace F] [CompleteSpace G]
    {f : E → F → G} {f' : E → F → _} (hf : ∀ x y, HasAdjFDerivAt ℝ (f x) (f' x y) y)
    (hf' : ContDiff ℝ (n+1) (↿f)) :
    ContDiff ℝ n (fun x : E×F×G => f' x.1 x.2.1 x.2.2)
```

**`gradient_eq_adjFDeriv`**, a lemma, [line 129](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Calculus/AdjFDeriv.lean#L129).

```lean
lemma gradient_eq_adjFDeriv
    {f : U → 𝕜} {x : U} (hf : DifferentiableAt 𝕜 f x) :
    gradient f x = adjFDeriv 𝕜 f x 1
```

**`hasAdjFDerivAt_id`**, a lemma, [line 138](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Calculus/AdjFDeriv.lean#L138).

```lean
lemma hasAdjFDerivAt_id (x : E) : HasAdjFDerivAt 𝕜 (fun x : E => x) (fun dx => dx) x
```

**`adjFDeriv_id`**, a lemma, [line 143](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Calculus/AdjFDeriv.lean#L143).

```lean
lemma adjFDeriv_id : adjFDeriv 𝕜 (fun x : E => x) = fun _ dx => dx
```

**`adjFDeriv_id'`**, a lemma, [line 147](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Calculus/AdjFDeriv.lean#L147).

```lean
lemma adjFDeriv_id' : adjFDeriv 𝕜 (id : E → E) = fun _ dx => dx
```

**`hasAdjFDerivAt_const`**, a lemma, [line 150](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Calculus/AdjFDeriv.lean#L150).

```lean
lemma hasAdjFDerivAt_const (x : E) (y : F) :
    HasAdjFDerivAt 𝕜 (fun _ : E => y) (fun _ => 0) x
```

**`adjFDeriv_const`**, a lemma, [line 156](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Calculus/AdjFDeriv.lean#L156).

```lean
lemma adjFDeriv_const (y : F) : adjFDeriv 𝕜 (fun _ : E => y) = fun _ _ => 0
```

**`HasAdjFDerivAt.comp`**, a lemma, [line 160](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Calculus/AdjFDeriv.lean#L160).

```lean
lemma HasAdjFDerivAt.comp {f : F → G} {g : E → F} {f' g'} {x : E}
    (hf : HasAdjFDerivAt 𝕜 f f' (g x)) (hg : HasAdjFDerivAt 𝕜 g g' x) :
    HasAdjFDerivAt 𝕜 (fun x => f (g x)) (fun dz => g' (f' dz)) x
```

**`adjFDeriv_comp`**, a lemma, [line 169](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Calculus/AdjFDeriv.lean#L169).

```lean
lemma adjFDeriv_comp [CompleteSpace E] [CompleteSpace F] [CompleteSpace G]
    {f : F → G} {g : E → F} {x : E}
    (hf : DifferentiableAt 𝕜 f (g x)) (hg : DifferentiableAt 𝕜 g x) :
    adjFDeriv 𝕜 (fun x => f (g x)) x = fun dy => adjFDeriv 𝕜 g x (adjFDeriv 𝕜 f (g x) dy)
```

**`HasAdjFDerivAt.prodMk`**, a lemma, [line 178](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Calculus/AdjFDeriv.lean#L178).

```lean
lemma HasAdjFDerivAt.prodMk {f : E → F} {g : E → G} {f' g'} {x : E}
    (hf : HasAdjFDerivAt 𝕜 f f' x) (hg : HasAdjFDerivAt 𝕜 g g' x) :
    HasAdjFDerivAt 𝕜 (fun x => (f x, g x)) (fun dyz => f' dyz.fst + g' dyz.snd) x
```

**`HasAjdFDerivAt.fst`**, a lemma, [line 188](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Calculus/AdjFDeriv.lean#L188).

```lean
lemma HasAjdFDerivAt.fst {f : E → F×G} {f'} {x : E} (hf : HasAdjFDerivAt 𝕜 f f' x) :
    HasAdjFDerivAt 𝕜 (fun x => (f x).fst) (fun dy => f' (dy, 0)) x
```

**`adjFDeriv_fst`**, a lemma, [line 195](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Calculus/AdjFDeriv.lean#L195).

```lean
lemma adjFDeriv_fst [CompleteSpace E] [CompleteSpace F] [CompleteSpace G]
    {f : E → F×G} {x : E} (hf : DifferentiableAt 𝕜 f x) :
    adjFDeriv 𝕜 (fun x => (f x).fst) x = fun dy => adjFDeriv 𝕜 f x (dy, 0)
```

**`adjFDeriv_prod_fst`**, a lemma, [line 202](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Calculus/AdjFDeriv.lean#L202).

```lean
lemma adjFDeriv_prod_fst [CompleteSpace E] [CompleteSpace F] {x : F × E} :
    adjFDeriv 𝕜 (Prod.fst : F × E → F) x = fun a => (a, 0)
```

**`HasAjdFDerivAt.snd`**, a lemma, [line 210](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Calculus/AdjFDeriv.lean#L210).

```lean
lemma HasAjdFDerivAt.snd {f : E → F×G} {f'} {x : E} (hf : HasAdjFDerivAt 𝕜 f f' x) :
    HasAdjFDerivAt 𝕜 (fun x => (f x).snd) (fun dz => f' (0, dz)) x
```

**`adjFDeriv_snd`**, a lemma, [line 217](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Calculus/AdjFDeriv.lean#L217).

```lean
lemma adjFDeriv_snd [CompleteSpace E] [CompleteSpace F] [CompleteSpace G]
    {f : E → F×G} {x : E} (hf : DifferentiableAt 𝕜 f x) :
    adjFDeriv 𝕜 (fun x => (f x).snd) x = fun dy => adjFDeriv 𝕜 f x (0, dy)
```

**`adjFDeriv_prod_snd`**, a lemma, [line 224](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Calculus/AdjFDeriv.lean#L224).

```lean
lemma adjFDeriv_prod_snd [CompleteSpace E] [CompleteSpace F] {x : F × E} :
    adjFDeriv 𝕜 (Prod.snd : F × E → E) x = fun a => (0, a)
```

**`hasAdjFDerivAt_uncurry`**, a lemma, [line 232](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Calculus/AdjFDeriv.lean#L232).

```lean
lemma hasAdjFDerivAt_uncurry {f : E → F → G} {xy} {fx' fy'}
    (hf : DifferentiableAt 𝕜 (↿f) xy)
    (hfx : HasAdjFDerivAt 𝕜 (f · xy.2) fx' xy.1) (hfy : HasAdjFDerivAt 𝕜 (f xy.1 ·) fy' xy.2) :
    HasAdjFDerivAt 𝕜 (↿f) (fun dz => (fx' dz, fy' dz)) xy
```

**`adjFDeriv_uncurry`**, a lemma, [line 248](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Calculus/AdjFDeriv.lean#L248).

```lean
lemma adjFDeriv_uncurry [CompleteSpace E] [CompleteSpace F] [CompleteSpace G]
    {f : E → F → G} {xy} (hfx : DifferentiableAt 𝕜 (↿f) xy) :
    adjFDeriv 𝕜 (↿f) xy = fun dz => (adjFDeriv 𝕜 (f · xy.snd) xy.fst dz,
                                    adjFDeriv 𝕜 (f xy.fst ·) xy.snd dz)
```

**`HasAdjFDerivAt.neg`**, a lemma, [line 258](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Calculus/AdjFDeriv.lean#L258).

```lean
lemma HasAdjFDerivAt.neg {f : E → F} {f'} {x : E} (hf : HasAdjFDerivAt 𝕜 f f' x) :
    HasAdjFDerivAt 𝕜 (fun x => - f x) (fun dy => - f' dy) x
```

**`adjFDeriv_neg`**, a lemma, [line 263](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Calculus/AdjFDeriv.lean#L263).

```lean
lemma adjFDeriv_neg [CompleteSpace E] [CompleteSpace F]
    {f : E → F} {x : E} (hf : DifferentiableAt 𝕜 f x) :
    adjFDeriv 𝕜 (fun x => - f x) x = fun dy => - adjFDeriv 𝕜 f x dy
```

**`HasAjdFDerivAt.add`**, a lemma, [line 269](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Calculus/AdjFDeriv.lean#L269).

```lean
lemma HasAjdFDerivAt.add {f g : E → F} {f' g'} {x : E}
    (hf : HasAdjFDerivAt 𝕜 f f' x) (hg : HasAdjFDerivAt 𝕜 g g' x) :
    HasAdjFDerivAt 𝕜 (fun x => f x + g x) (fun dy => f' dy + g' dy) x
```

**`adjFDeriv_add`**, a lemma, [line 277](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Calculus/AdjFDeriv.lean#L277).

```lean
lemma adjFDeriv_add [CompleteSpace E] [CompleteSpace F]
    {f g : E → F} {x : E}
    (hf : DifferentiableAt 𝕜 f x) (hg : DifferentiableAt 𝕜 g x) :
    adjFDeriv 𝕜 (fun x => f x + g x) x = fun dy => adjFDeriv 𝕜 f x dy + adjFDeriv 𝕜 g x dy
```

**`HasAdjFDerivAt.sub`**, a lemma, [line 286](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Calculus/AdjFDeriv.lean#L286).

```lean
lemma HasAdjFDerivAt.sub
    {f g : E → F} {f' g'} {x : E}
    (hf : HasAdjFDerivAt 𝕜 f f' x) (hg : HasAdjFDerivAt 𝕜 g g' x) :
    HasAdjFDerivAt 𝕜 (fun x => f x - g x) (fun dy => f' dy - g' dy) x
```

**`adjFDeriv_sub`**, a lemma, [line 295](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Calculus/AdjFDeriv.lean#L295).

```lean
lemma adjFDeriv_sub [CompleteSpace E] [CompleteSpace F] {f g : E → F} {x : E}
    (hf : DifferentiableAt 𝕜 f x) (hg : DifferentiableAt 𝕜 g x) :
    adjFDeriv 𝕜 (fun x => f x - g x) x = fun dy => adjFDeriv 𝕜 f x dy - adjFDeriv 𝕜 g x dy
```

**`HasAdjFDerivAt.smul`**, a lemma, [line 304](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Calculus/AdjFDeriv.lean#L304).

```lean
lemma HasAdjFDerivAt.smul {f : E → F} {g : E → 𝕜} {f' g'}
    (hf : HasAdjFDerivAt 𝕜 f f' x) (hg : HasAdjFDerivAt 𝕜 g g' x) :
    HasAdjFDerivAt 𝕜 (fun x => g x • f x)
      (fun dy => conj (g x) • f' dy + g' (conj (inner 𝕜 dy (f x)))) x
```

**`adjFDeriv_smul`**, a lemma, [line 316](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Calculus/AdjFDeriv.lean#L316).

```lean
lemma adjFDeriv_smul [CompleteSpace E] [CompleteSpace F]
    {f : E → F} {g : E → 𝕜} {x : E}
    (hf : DifferentiableAt 𝕜 f x) (hg : DifferentiableAt 𝕜 g x) :
    adjFDeriv 𝕜 (fun x => g x • f x) x = fun dy => conj (g x) • adjFDeriv 𝕜 f x dy +
                                                  adjFDeriv 𝕜 g x (conj (inner 𝕜 dy (f x)))
```

**`HasAdjFDerivAt.inner`**, a lemma, [line 328](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Calculus/AdjFDeriv.lean#L328).

```lean
lemma HasAdjFDerivAt.inner {E : Type*} [NormedAddCommGroup E] [NormedSpace ℝ E]
    [InnerProductSpace' ℝ E] (x : E × E) :
    HasAdjFDerivAt ℝ (fun (x : E × E) => ⟪x.1, x.2⟫_ℝ) (fun y => y • (x.2, x.1)) x
```

**`adjFDeriv_inner`**, a lemma, [line 348](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Calculus/AdjFDeriv.lean#L348).

```lean
lemma adjFDeriv_inner {E : Type*} [NormedAddCommGroup E] [NormedSpace ℝ E] [InnerProductSpace' ℝ E]
    (x : E × E) :
    adjFDeriv ℝ (fun (x : E × E) => ⟪x.1, x.2⟫_ℝ) x =
      fun y => y • (x.2, x.1)
```

## Depends on

- [Adjoint of a linear map](../innerproductspace/adjoint.md)

## Proof depends on

- [fderiv currying lemmas](../formathlib/fderivcurry.md)
- [Generalization of calculus results to `InnerProductSpace'`](../innerproductspace/calculus.md)

## Sources

- [Physlib/Mathematics/Calculus/AdjFDeriv.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Calculus/AdjFDeriv.lean)
