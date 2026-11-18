---
declaration: module
origin: cited
lean: fderivInnerCLM', HasFDerivAt.inner', fderiv_inner_apply', deriv_inner_apply', DifferentiableAt.inner'
statement: formalized
proof: formalized
---

# Generalization of calculus results to `InnerProductSpace'`

The module `Physlib.Mathematics.InnerProductSpace.Calculus`, [Physlib/Mathematics/InnerProductSpace/Calculus.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/InnerProductSpace/Calculus.lean): 5 declarations, 1 with a docstring.

**`fderivInnerCLM'`**, a def, [line 24](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/InnerProductSpace/Calculus.lean#L24).

> Derivative of the inner product for the instance `InnerProductSpace'`.

```lean
noncomputable def fderivInnerCLM' [InnerProductSpace' ℝ E] (p : E × E) : E × E →L[ℝ] ℝ
```

**`HasFDerivAt.inner'`**, a lemma, [line 27](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/InnerProductSpace/Calculus.lean#L27).

```lean
lemma HasFDerivAt.inner' {f g : E → F}
    {f' g' : E →L[ℝ] F} (hf : HasFDerivAt f f' x) (hg : HasFDerivAt g g' x) :
    HasFDerivAt (fun t => ⟪f t, g t⟫) ((fderivInnerCLM' (f x, g x)).comp <| f'.prod g') x
```

**`fderiv_inner_apply'`**, a lemma, [line 34](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/InnerProductSpace/Calculus.lean#L34).

```lean
lemma fderiv_inner_apply'
    {f g : E → F} {x : E}
    (hf : DifferentiableAt ℝ f x) (hg : DifferentiableAt ℝ g x) (y : E) :
    fderiv ℝ (fun t => ⟪f t, g t⟫) x y = ⟪f x, fderiv ℝ g x y⟫ + ⟪fderiv ℝ f x y, g x⟫
```

**`deriv_inner_apply'`**, a lemma, [line 42](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/InnerProductSpace/Calculus.lean#L42).

```lean
lemma deriv_inner_apply'
    {f g : ℝ → F} {x : ℝ}
    (hf : DifferentiableAt ℝ f x) (hg : DifferentiableAt ℝ g x) :
    deriv (fun t => ⟪f t, g t⟫) x = ⟪f x, deriv g x⟫ + ⟪deriv f x, g x⟫
```

**`DifferentiableAt.inner'`**, a lemma, [line 50](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/InnerProductSpace/Calculus.lean#L50).

```lean
lemma DifferentiableAt.inner' {f g : E → F} {x}
    (hf : DifferentiableAt ℝ f x) (hg : DifferentiableAt ℝ g x) :
    DifferentiableAt ℝ (fun x => ⟪f x, g x⟫) x
```

## Depends on

- [Inner product space](basic.md)

## Sources

- [Physlib/Mathematics/InnerProductSpace/Calculus.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/InnerProductSpace/Calculus.lean)
