---
declaration: module
origin: cited
lean: HasAdjoint, adjoint, HasAdjoint.adjoint_inner_right, ContinuousLinearMap.hasAdjoint, adjoint_eq_clm_adjoint, HasAdjoint.adjoint_apply_zero, HasAdjoint.adjoint, HasAdjoint.congr_adj
statement: formalized
proof: formalized
---

# Adjoint of a linear map

The module `Physlib.Mathematics.InnerProductSpace.Adjoint`, [Physlib/Mathematics/InnerProductSpace/Adjoint.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/InnerProductSpace/Adjoint.lean): 19 declarations, 1 with a docstring.

> This module defines the adjoint of a linear map `f : E → F` where
> `E` and `F` carry the instances of `InnerProductSpace'` over a field `𝕜`.
>
> This is a generalization of the usual adjoint defined on `InnerProductSpace` for
> continuous linear maps.

**`HasAdjoint`**, a structure, [line 38](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/InnerProductSpace/Adjoint.lean#L38).

> Adjoint of a linear map `f` such that `∀ x y, ⟪adjoint 𝕜 f y, x⟫ = ⟪y, f x⟫`.
>
> This computes adjoint of a linear map the same way as `ContinuousLinearMap.adjoint` but it is
> defined over `InnerProductSpace'`, which is a generalization of `InnerProductSpace` that provides
> instances for products and function types. These instances make it easier to perform computations
> compared to using the standard `InnerProductSpace` class.

```lean
structure HasAdjoint (f : E → F) (f' : F → E) where
  adjoint_inner_left (x : E) (y : F) : ⟪f' y, x⟫ = ⟪y, f x⟫
```

**`adjoint`**, a def, [line 45](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/InnerProductSpace/Adjoint.lean#L45).

```lean
def adjoint (f : E → F)
```

**`HasAdjoint.adjoint_inner_right`**, a lemma, [line 50](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/InnerProductSpace/Adjoint.lean#L50).

```lean
lemma HasAdjoint.adjoint_inner_right {f : E → F} (hf : HasAdjoint 𝕜 f f') :
    ⟪x, f' y⟫ = ⟪f x, y⟫
```

**`ContinuousLinearMap.hasAdjoint`**, a lemma, [line 57](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/InnerProductSpace/Adjoint.lean#L57).

```lean
lemma ContinuousLinearMap.hasAdjoint [CompleteSpace E] [CompleteSpace F] (f : E →L[𝕜] F) :
    HasAdjoint 𝕜 f (fun y => fromL2 𝕜 (((toL2 𝕜) ∘L f ∘L (fromL2 𝕜)).adjoint (toL2 𝕜 y)))
```

**`adjoint_eq_clm_adjoint`**, a lemma, [line 62](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/InnerProductSpace/Adjoint.lean#L62).

```lean
lemma adjoint_eq_clm_adjoint [CompleteSpace E] [CompleteSpace F] (f : E →L[𝕜] F) :
    _root_.adjoint 𝕜 f = fromL2 𝕜 ∘L (toL2 𝕜 ∘L f ∘L fromL2 𝕜).adjoint ∘L (toL2 𝕜)
```

**`HasAdjoint.adjoint_apply_zero`**, a lemma, [line 69](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/InnerProductSpace/Adjoint.lean#L69).

```lean
lemma HasAdjoint.adjoint_apply_zero {f : E → F} {f' : F → E}
    (hf : HasAdjoint 𝕜 f f') : f' 0 = 0
```

**`HasAdjoint.adjoint`**, a lemma, [line 73](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/InnerProductSpace/Adjoint.lean#L73).

```lean
lemma HasAdjoint.adjoint
    {f : E → F} {f' : F → E}
    (hf : HasAdjoint 𝕜 f f') : adjoint 𝕜 f = f'
```

**`HasAdjoint.congr_adj`**, a lemma, [line 84](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/InnerProductSpace/Adjoint.lean#L84).

```lean
lemma HasAdjoint.congr_adj (f : E → F) (f' g')
    (adjoint : HasAdjoint 𝕜 f g')
    (eq : g' = f') : HasAdjoint 𝕜 f f'
```

**`hasAdjoint_id`**, a lemma, [line 88](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/InnerProductSpace/Adjoint.lean#L88).

```lean
lemma hasAdjoint_id : HasAdjoint 𝕜 (fun x : E => x) (fun x => x)
```

**`hasAdjoint_zero`**, a lemma, [line 91](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/InnerProductSpace/Adjoint.lean#L91).

```lean
lemma hasAdjoint_zero : HasAdjoint 𝕜 (fun _ : E => (0 : F)) (fun _ => 0)
```

**`HasAdjoint.comp`**, a lemma, [line 94](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/InnerProductSpace/Adjoint.lean#L94).

```lean
lemma HasAdjoint.comp {f : F → G} {g : E → F} {f' g'}
    (hf : HasAdjoint 𝕜 f f') (hg : HasAdjoint 𝕜 g g') :
    HasAdjoint 𝕜 (fun x : E => f (g x)) (fun x => g' (f' x))
```

**`HasAdjoint.prodMk`**, a lemma, [line 100](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/InnerProductSpace/Adjoint.lean#L100).

```lean
lemma HasAdjoint.prodMk {f : E → F} {g : E → G} {f' g'}
    (hf : HasAdjoint 𝕜 f f') (hg : HasAdjoint 𝕜 g g') :
    HasAdjoint 𝕜 (fun x : E => (f x, g x)) (fun yz => f' yz.1 + g' yz.2)
```

**`HasAdjoint.fst`**, a lemma, [line 108](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/InnerProductSpace/Adjoint.lean#L108).

```lean
lemma HasAdjoint.fst {f : E → F×G} {f'} (hf : HasAdjoint 𝕜 f f') :
    HasAdjoint 𝕜 (fun x : E => (f x).1) (fun y => f' (y, 0))
```

**`HasAdjoint.snd`**, a lemma, [line 114](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/InnerProductSpace/Adjoint.lean#L114).

```lean
lemma HasAdjoint.snd {f : E → F×G} {f'} (hf : HasAdjoint 𝕜 f f') :
    HasAdjoint 𝕜 (fun x : E => (f x).2) (fun z => f' (0, z))
```

**`HasAdjoint.neg`**, a lemma, [line 119](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/InnerProductSpace/Adjoint.lean#L119).

```lean
lemma HasAdjoint.neg {f : E → F} {f'} (hf : HasAdjoint 𝕜 f f') :
    HasAdjoint 𝕜 (fun x : E => -f x) (fun y => -f' y)
```

**`HasAdjoint.add`**, a lemma, [line 124](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/InnerProductSpace/Adjoint.lean#L124).

```lean
lemma HasAdjoint.add {f g : E → F} {f' g'}
    (hf : HasAdjoint 𝕜 f f') (hg : HasAdjoint 𝕜 g g') :
    HasAdjoint 𝕜 (fun x : E => f x + g x) (fun y => f' y + g' y)
```

**`HasAdjoint.sub`**, a lemma, [line 131](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/InnerProductSpace/Adjoint.lean#L131).

```lean
lemma HasAdjoint.sub {f g : E → F} {f' g'}
    (hf : HasAdjoint 𝕜 f f') (hg : HasAdjoint 𝕜 g g') :
    HasAdjoint 𝕜 (fun x : E => f x - g x) (fun y => f' y - g' y)
```

**`HasAdjoint.smul_left`**, a lemma, [line 139](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/InnerProductSpace/Adjoint.lean#L139).

```lean
lemma HasAdjoint.smul_left {f : E → F} {f'} (c : 𝕜)
    (hf : HasAdjoint 𝕜 f f') :
    HasAdjoint 𝕜 (fun x : E => c • f x) (fun y => (conj c) • f' y)
```

**`HasAdjoint.smul_right`**, a lemma, [line 146](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/InnerProductSpace/Adjoint.lean#L146).

```lean
lemma HasAdjoint.smul_right {f : E → 𝕜} {f'} (v : F)
    (hf : HasAdjoint 𝕜 f f') :
    HasAdjoint 𝕜 (fun x : E => f x • v) (fun y => f' (conj ⟪y, v⟫))
```

## Depends on

- [Inner product space](basic.md)

## Sources

- [Physlib/Mathematics/InnerProductSpace/Adjoint.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/InnerProductSpace/Adjoint.lean)
