---
declaration: module
origin: cited
lean: Tensor.Variance, Tensor.Variance.up, Tensor.Variance.down, Tensor.Variance.dual, Tensor.Color, Tensor.Color.dual, Tensor.Color.dual_dual
statement: formalized
proof: formalized
---

# Colors of tensor indices

The module `Physlib.Mathematics.Tensors.Color`, [Physlib/Mathematics/Tensors/Color.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Tensors/Color.lean): 7 declarations, 7 with a docstring.

> A color gives the kind of an index of a tensor and whether the index is up or down.

## i. Overview

> A color `⟨κ, v⟩` is a kind of index `κ : K` and a variance `v`, `up` or `down`. For Lorentz
> tensors there is one kind, `vec`. The vector index of `v^μ` has color `⟨vec, up⟩` and the
> covector index of `w_μ` has color `⟨vec, down⟩`. Complex Lorentz tensors have three kinds, one
> for each of the two types of Weyl spinor index and one for the vector index.
>
> A tensor has one color per index. A species (`Species.lean`) gives each color a space, and a
> tensor is an element of the tensor product of the spaces of its indices. Each index has a color
> rather than a space, so that whether two indices can be contracted is an equation of colors,
> `c j = (c i).dual`, which Lean checks by computation when the colors are known. When two colors
> are equal only through a proof, vectors are moved between their spaces by `S.cast`
> (`Species.lean`, §C).
>
> The dual of `⟨κ, v⟩` is `⟨κ, v.dual⟩`, the same kind with the other variance. A contraction such
> as `v^μ w_μ` pairs an index of color `c` with an index of color `c.dual`. `Color K` is a structure
> rather than the product `K × Variance`, so that `c.dual` works as dot notation.

## ii. Key results

> - `Variance` : the variance of an index, with `Variance.up`, `Variance.down` and
>   `Variance.dual`.
> - `Color` : a kind of index and a variance.
> - `Color.dual` : the dual color, and `Color.dual_dual` : `c.dual.dual = c` by `rfl`.

## iv. References

> There are no known references for the material in this module.

## A. Variance

> `Variance` is two booleans, and `dual` swaps them. So `c.dual.dual` is `c` by definition, also for
> a variable color `c`, and the spaces `S.V c.dual.dual` and `S.V c` of a species are the same type.

**`Tensor.Variance`**, a structure, [line 65](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Tensors/Color.lean#L65).

> The variance of an index, up (contravariant, `v^μ`) or down (covariant, `w_μ`).

```lean
structure Variance where
  /-- Whether the index is up. -/
  isUp : Bool
  /-- Whether the index is down. -/
  isDown : Bool
  /-- An index is either up or down. -/
  ne : isUp ≠ isDown
```

**`Tensor.Variance.up`**, an abbrev, [line 78](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Tensors/Color.lean#L78).

> An upper index, as in `v^μ`.

```lean
abbrev up : Variance
```

**`Tensor.Variance.down`**, an abbrev, [line 82](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Tensors/Color.lean#L82).

> A lower index, as in `w_μ`.

```lean
abbrev down : Variance
```

**`Tensor.Variance.dual`**, an abbrev, [line 86](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Tensors/Color.lean#L86).

> The dual variance, exchanging up and down. It is an abbrev, so that `simp` and `rw` see
> `c.dual.dual` as `c`.

```lean
abbrev dual (v : Variance) : Variance
```

## B. Colors

**`Tensor.Color`**, a structure, [line 97](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Tensors/Color.lean#L97).

> A color `⟨κ, v⟩`, made of a kind of index `κ : K` and its variance `v`.

```lean
structure Color (K : Type) where
  /-- The kind of index, such as a Lorentz vector index or a left-handed Weyl spinor index. -/
  kind : K
  /-- Whether the index is up or down. -/
  variance : Variance
```

**`Tensor.Color.dual`**, an abbrev, [line 105](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Tensors/Color.lean#L105).

> The dual color, with the same kind and the other variance.

```lean
abbrev Color.dual {K : Type} (c : Color K) : Color K
```

**`Tensor.Color.dual_dual`**, a lemma, [line 108](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Tensors/Color.lean#L108).

> Taking the dual twice gives back the color.

```lean
lemma Color.dual_dual {K : Type} (c : Color K) : c.dual.dual = c
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [Physlib/Mathematics/Tensors/Color.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Tensors/Color.lean)
