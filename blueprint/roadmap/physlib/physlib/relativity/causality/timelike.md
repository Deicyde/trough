---
declaration: module
origin: cited
lean: Lorentz.Vector.timelike_neg_time_component_product, Lorentz.Vector.timeLike_iff_norm_sq_pos, Lorentz.Vector.timelike_time_dominates_space, Lorentz.Vector.minkowskiProduct_ne_zero_of_timeLike, Lorentz.Vector.time_component_ne_zero_of_timelike, Lorentz.Vector.timelike_time_component_ne_zero, Lorentz.Vector.minkowskiProduct_self_neg_of_timeLike_orthogonal, Lorentz.Vector.timeLike_iff_time_lt_space
statement: formalized
proof: formalized
---

# Physlib.Relativity.Causality.TimeLike

The module `Physlib.Relativity.Causality.TimeLike`, [Physlib/Relativity/Causality/TimeLike.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Causality/TimeLike.lean): 10 declarations, 10 with a docstring.

## Properties of time like vectors

**`Lorentz.Vector.timelike_neg_time_component_product`**, a lemma, [line 28](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Causality/TimeLike.lean#L28).

> For timelike vectors with negative time components,
> their time components multiply to give a positive number

```lean
lemma timelike_neg_time_component_product {d : ℕ} (v w : Vector d)
    (hv_neg : v (Sum.inl 0) < 0) (hw_neg : w (Sum.inl 0) < 0) :
    v (Sum.inl 0) * w (Sum.inl 0) > 0
```

**`Lorentz.Vector.timeLike_iff_norm_sq_pos`**, a lemma, [line 34](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Causality/TimeLike.lean#L34).

> For timelike vectors, the Minkowski inner product is positive

```lean
lemma timeLike_iff_norm_sq_pos {d : ℕ} (p : Vector d) :
    causalCharacter p = CausalCharacter.timeLike ↔ 0 < ⟪p, p⟫ₘ
```

**`Lorentz.Vector.timelike_time_dominates_space`**, a lemma, [line 48](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Causality/TimeLike.lean#L48).

> For timeLike vectors in Minkowski space, the inner product of the spatial part
> is less than the square of the time component

```lean
lemma timelike_time_dominates_space {d : ℕ} {v : Vector d}
    (hv : causalCharacter v = .timeLike) :
    ⟪spatialPart v, spatialPart v⟫_ℝ < (timeComponent v) * (timeComponent v)
```

**`Lorentz.Vector.minkowskiProduct_ne_zero_of_timeLike`**, a lemma, [line 68](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Causality/TimeLike.lean#L68).

> Two timelike vectors have nonzero Minkowski inner product.

```lean
lemma minkowskiProduct_ne_zero_of_timeLike {d : ℕ} {u v : Vector d}
    (hu : causalCharacter u = .timeLike) (hv : causalCharacter v = .timeLike) :
    ⟪u, v⟫ₘ ≠ 0
```

**`Lorentz.Vector.time_component_ne_zero_of_timelike`**, a lemma, [line 87](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Causality/TimeLike.lean#L87).

> For nonzero timelike vectors, the time component is nonzero

```lean
lemma time_component_ne_zero_of_timelike {d : ℕ} {v : Vector d}
    (hv : causalCharacter v = .timeLike) :
    v (Sum.inl 0) ≠ 0
```

**`Lorentz.Vector.timelike_time_component_ne_zero`**, a lemma, [line 101](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Causality/TimeLike.lean#L101).

> For timelike vectors, the time component is nonzero

```lean
lemma timelike_time_component_ne_zero {d : ℕ} {v : Vector d}
    (hv : causalCharacter v = .timeLike) :
    timeComponent v ≠ 0
```

**`Lorentz.Vector.minkowskiProduct_self_neg_of_timeLike_orthogonal`**, a lemma, [line 106](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Causality/TimeLike.lean#L106).

> A nonzero vector orthogonal to a timelike vector has negative Minkowski self-product.

```lean
lemma minkowskiProduct_self_neg_of_timeLike_orthogonal {d : ℕ} {u v : Lorentz.Vector d}
    (hu : causalCharacter u = .timeLike) (hv : v ≠ 0) (horth : ⟪u, v⟫ₘ = 0) :
    ⟪v, v⟫ₘ < 0
```

**`Lorentz.Vector.timeLike_iff_time_lt_space`**, a lemma, [line 132](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Causality/TimeLike.lean#L132).

> A vector is timelike if and only if its time component squared is less than
> the sum of its spatial components squared

```lean
lemma timeLike_iff_time_lt_space {d : ℕ} {v : Vector d} :
    causalCharacter v = .timeLike ↔
    ⟪spatialPart v, spatialPart v⟫_ℝ < v (Sum.inl 0) * v (Sum.inl 0)
```

**`Lorentz.Vector.timeComponent_squared_pos_of_timelike`**, a lemma, [line 146](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Causality/TimeLike.lean#L146).

> Time component squared is positive for timelike vectors

```lean
lemma timeComponent_squared_pos_of_timelike {d : ℕ} {v : Vector d}
    (hv : causalCharacter v = .timeLike) :
    0 < (timeComponent v)^2
```

**`Lorentz.Vector.timelike_spatial_lt_time_squared`**, a lemma, [line 153](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Causality/TimeLike.lean#L153).

> For timelike vectors, the spatial norm squared is strictly less
> than the time component squared

```lean
lemma timelike_spatial_lt_time_squared {d : ℕ} {v : Vector d}
    (hv : causalCharacter v = .timeLike) :
    ⟪spatialPart v, spatialPart v⟫_ℝ < (timeComponent v)^2
```

## Depends on

- [Physlib.Relativity.Causality.Basic](basic.md)

## Sources

- [Physlib/Relativity/Causality/TimeLike.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Causality/TimeLike.lean)
