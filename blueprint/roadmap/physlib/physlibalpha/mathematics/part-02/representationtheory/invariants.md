---
declaration: module
origin: cited
lean: Representation.IntertwiningMap.apply_mem_invariants, Representation.IntertwiningMap.apply_one_mem_invariants, Representation.IntertwiningMap.ext_one, Representation.IntertwiningMap.exists_eq_smul_of_invariants_eq_span, Representation.IntertwiningMap.eq_zero_of_invariants_eq_bot, Representation.invariants_eq_span_singleton, Representation.invariants_eq_bot_of_forall, Representation.exists_eq_smul_of_invariants_eq_span
statement: formalized
proof: formalized
---

# Invariants and intertwining maps out of the trivial representation

The module `PhyslibAlpha.Mathematics.RepresentationTheory.Invariants`, [PhyslibAlpha/Mathematics/RepresentationTheory/Invariants.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/RepresentationTheory/Invariants.lean): 14 declarations, 14 with a docstring.

> How the invariants of a representation control the intertwining maps out of the trivial one.

## i. Overview

> The classifications of invariants are stated in one form, `σ.invariants = k ∙ v`,
> `σ.invariants = Submodule.span k s` or `σ.invariants = ⊥`. This file turns that form into the
> others.
>
> An intertwining map `φ` from the trivial representation on `k` into `σ` is fixed by its value
> `φ 1`, which is an invariant of `σ` (A). So once the invariants of `σ` are known to be a line
> `k ∙ φ₀ 1`, every such `φ` is a multiple of `φ₀`, and once they are known to be zero, so is every
> such `φ`. Likewise every invariant element is a multiple of `v`, or zero (B).
>
> The invariants in the range of an intertwining map `f` out of `σ`, `ρ.invariants ⊓ f.range`,
> generalise the invariants of `σ`, which they are for `f` the identity. When every invariant in the
> range of `f` is the image of an invariant of `σ`, a descent property, they are the image of the
> invariants of `σ`, so a line or zero along with them (C). A Reynolds element of `σ` gives this
> property, through `Representation.IsReynolds.exists_mem_invariants_map_eq`. A bijective
> intertwining map has it too, and carries the invariants onto the invariants.

## ii. Key results

> - `Representation.IntertwiningMap.apply_one_mem_invariants` : the value at `1` of an intertwining
>   map out of the trivial representation is invariant.
> - `Representation.IntertwiningMap.exists_eq_smul_of_invariants_eq_span` : when the invariants are
>   a line, the intertwining maps out of the trivial representation are the multiples of one map.
> - `Representation.IntertwiningMap.eq_zero_of_invariants_eq_bot` : when there are no invariants,
>   there are no such maps but zero.
> - `Representation.exists_eq_smul_of_invariants_eq_span`,
>   `Representation.eq_zero_of_invariants_eq_bot` : the invariant elements, from the invariants.
> - `Representation.invariants_inf_range_eq_map_of_descent` : with descent, the invariants in the
>   range are the image of the invariants.
> - `Representation.invariants_inf_range_eq_span_of_descent`,
>   `Representation.invariants_inf_range_eq_bot_of_descent` : the line or zero in the range.
> - `Representation.IsReynolds.invariants_inf_range_eq_map` : descent from a Reynolds element.
> - `Representation.invariants_eq_map_of_bijective` : a bijective intertwining map carries the
>   invariants onto the invariants.

## iv. References

> * None.

## A. Intertwining maps out of the trivial representation

**`Representation.IntertwiningMap.apply_mem_invariants`**, a lemma, [line 81](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/RepresentationTheory/Invariants.lean#L81).

> An intertwining map sends invariants to invariants.

```lean
lemma apply_mem_invariants (f : σ.IntertwiningMap ρ) {v : V} (hv : v ∈ σ.invariants) :
    f v ∈ ρ.invariants
```

**`Representation.IntertwiningMap.apply_one_mem_invariants`**, a lemma, [line 85](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/RepresentationTheory/Invariants.lean#L85).

> The value at `1` of an intertwining map out of the trivial representation is invariant.

```lean
lemma apply_one_mem_invariants (φ : (trivial k G k).IntertwiningMap σ) : φ 1 ∈ σ.invariants
```

**`Representation.IntertwiningMap.ext_one`**, a lemma, [line 89](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/RepresentationTheory/Invariants.lean#L89).

> An intertwining map out of the trivial representation is fixed by its value at `1`.

```lean
lemma ext_one {φ ψ : (trivial k G k).IntertwiningMap σ} (h : φ 1 = ψ 1) : φ = ψ
```

## B. From the invariants to invariant maps and elements

**`Representation.IntertwiningMap.exists_eq_smul_of_invariants_eq_span`**, a lemma, [line 100](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/RepresentationTheory/Invariants.lean#L100).

> When the invariants of `σ` are the line through `φ₀ 1`, every intertwining map out of the
> trivial representation is a multiple of `φ₀`.

```lean
lemma exists_eq_smul_of_invariants_eq_span {φ₀ : (trivial k G k).IntertwiningMap σ}
    (h : σ.invariants = k ∙ φ₀ 1) (φ : (trivial k G k).IntertwiningMap σ) :
    ∃ z : k, φ = z • φ₀
```

**`Representation.IntertwiningMap.eq_zero_of_invariants_eq_bot`**, a lemma, [line 110](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/RepresentationTheory/Invariants.lean#L110).

> When `σ` has no invariants but zero, the only intertwining map out of the trivial
> representation is zero.

```lean
lemma eq_zero_of_invariants_eq_bot (h : σ.invariants = ⊥)
    (φ : (trivial k G k).IntertwiningMap σ) : φ = 0
```

**`Representation.invariants_eq_span_singleton`**, a lemma, [line 120](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/RepresentationTheory/Invariants.lean#L120).

> The invariants are the line through an invariant `v` when every invariant is a multiple of
> it.

```lean
lemma invariants_eq_span_singleton {v : V} (hv : v ∈ σ.invariants)
    (h : ∀ x ∈ σ.invariants, ∃ a : k, x = a • v) : σ.invariants = k ∙ v
```

**`Representation.invariants_eq_bot_of_forall`**, a lemma, [line 127](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/RepresentationTheory/Invariants.lean#L127).

> There are no invariants but zero when every invariant vanishes.

```lean
lemma invariants_eq_bot_of_forall (h : ∀ x ∈ σ.invariants, x = 0) : σ.invariants = ⊥
```

**`Representation.exists_eq_smul_of_invariants_eq_span`**, a lemma, [line 131](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/RepresentationTheory/Invariants.lean#L131).

> When the invariants of `σ` are the line through `v`, every invariant is a multiple of `v`.

```lean
lemma exists_eq_smul_of_invariants_eq_span {v : V} (h : σ.invariants = k ∙ v) {x : V}
    (hx : ∀ g, σ g x = x) : ∃ a : k, x = a • v
```

**`Representation.eq_zero_of_invariants_eq_bot`**, a lemma, [line 138](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/RepresentationTheory/Invariants.lean#L138).

> When `σ` has no invariants but zero, every invariant is zero.

```lean
lemma eq_zero_of_invariants_eq_bot (h : σ.invariants = ⊥) {x : V} (hx : ∀ g, σ g x = x) :
    x = 0
```

## C. Invariants in the range of an intertwining map

**`Representation.invariants_inf_range_eq_map_of_descent`**, a lemma, [line 150](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/RepresentationTheory/Invariants.lean#L150).

> The invariants in the range of `f` are the image of the invariants of `σ` when every
> invariant in the range is the image of an invariant, the descent property `hd`.

```lean
lemma invariants_inf_range_eq_map_of_descent (f : σ.IntertwiningMap ρ)
    (hd : ∀ v, f v ∈ ρ.invariants → ∃ w ∈ σ.invariants, f w = f v) :
    ρ.invariants ⊓ f.range.toSubmodule = σ.invariants.map f.toLinearMap
```

**`Representation.invariants_inf_range_eq_span_of_descent`**, a lemma, [line 161](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/RepresentationTheory/Invariants.lean#L161).

> With descent, the invariants in the range of `f` are the line through `f v` when the
> invariants of `σ` are the line through `v`.

```lean
lemma invariants_inf_range_eq_span_of_descent {v : V} (h : σ.invariants = k ∙ v)
    (f : σ.IntertwiningMap ρ) (hd : ∀ v, f v ∈ ρ.invariants → ∃ w ∈ σ.invariants, f w = f v) :
    ρ.invariants ⊓ f.range.toSubmodule = k ∙ f v
```

**`Representation.invariants_inf_range_eq_bot_of_descent`**, a lemma, [line 168](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/RepresentationTheory/Invariants.lean#L168).

> With descent, the invariants in the range of `f` are zero when those of `σ` are.

```lean
lemma invariants_inf_range_eq_bot_of_descent (h : σ.invariants = ⊥) (f : σ.IntertwiningMap ρ)
    (hd : ∀ v, f v ∈ ρ.invariants → ∃ w ∈ σ.invariants, f w = f v) :
    ρ.invariants ⊓ f.range.toSubmodule = ⊥
```

**`Representation.IsReynolds.invariants_inf_range_eq_map`**, a lemma, [line 175](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/RepresentationTheory/Invariants.lean#L175).

> A Reynolds element of `σ` on all of `V` gives descent along every intertwining map, so the
> invariants in the range of `f` are the image of the invariants of `σ`.

```lean
lemma IsReynolds.invariants_inf_range_eq_map {r : MonoidAlgebra k G} (hr : σ.IsReynolds ⊤ r)
    (f : σ.IntertwiningMap ρ) :
    ρ.invariants ⊓ f.range.toSubmodule = σ.invariants.map f.toLinearMap
```

**`Representation.invariants_eq_map_of_bijective`**, a lemma, [line 184](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/RepresentationTheory/Invariants.lean#L184).

> A bijective intertwining map carries the invariants onto the invariants.

```lean
lemma invariants_eq_map_of_bijective (f : σ.IntertwiningMap ρ) (hf : Function.Bijective f) :
    ρ.invariants = σ.invariants.map f.toLinearMap
```

## Depends on

- [Reynolds elements](reynolds-basic.md)

## Sources

- [PhyslibAlpha/Mathematics/RepresentationTheory/Invariants.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/RepresentationTheory/Invariants.lean)
