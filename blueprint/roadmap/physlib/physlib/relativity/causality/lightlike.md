---
declaration: module
origin: cited
lean: Lorentz.Vector.lightLike_iff_norm_sq_zero, Lorentz.Vector.causalCharacter_zero, Lorentz.Vector.causallyPrecedes_refl, Lorentz.Vector.lightlike_eq_spatial_norm_of_eq_time, Lorentz.Vector.lightlike_spatial_parallel_implies_proportional
statement: formalized
proof: formalized
---

# Physlib.Relativity.Causality.LightLike

The module `Physlib.Relativity.Causality.LightLike`, [Physlib/Relativity/Causality/LightLike.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Causality/LightLike.lean): 5 declarations, 3 with a docstring.

## Properties of light like vectors

**`Lorentz.Vector.lightLike_iff_norm_sq_zero`**, a lemma, [line 25](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Causality/LightLike.lean#L25).

```lean
lemma lightLike_iff_norm_sq_zero {d : ℕ} (p : Vector d) :
    causalCharacter p = CausalCharacter.lightLike ↔ ⟪p, p⟫ₘ = 0
```

**`Lorentz.Vector.causalCharacter_zero`**, a lemma, [line 32](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Causality/LightLike.lean#L32).

```lean
lemma causalCharacter_zero {d : ℕ} : causalCharacter (0 : Vector d) =
    CausalCharacter.lightLike
```

**`Lorentz.Vector.causallyPrecedes_refl`**, a lemma, [line 38](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Causality/LightLike.lean#L38).

> Causally preceding is reflexive

```lean
lemma causallyPrecedes_refl {d : ℕ} (p : Vector d) : causallyPrecedes p p
```

**`Lorentz.Vector.lightlike_eq_spatial_norm_of_eq_time`**, a lemma, [line 43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Causality/LightLike.lean#L43).

> For two lightlike vectors with equal time components, their spatial parts
> have equal Euclidean norms

```lean
lemma lightlike_eq_spatial_norm_of_eq_time {d : ℕ} {v w : Vector d}
    (hv : causalCharacter v = .lightLike) (hw : causalCharacter w = .lightLike)
    (h_time : timeComponent v = timeComponent w) :
    ⟪spatialPart v, spatialPart v⟫_ℝ = ⟪spatialPart w, spatialPart w⟫_ℝ
```

**`Lorentz.Vector.lightlike_spatial_parallel_implies_proportional`**, a lemma, [line 58](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Causality/LightLike.lean#L58).

> If two lightlike vectors have parallel spatial components, their temporal components
> must also be proportional, which implies the entire vectors are proportional

```lean
lemma lightlike_spatial_parallel_implies_proportional {d : ℕ} {v w : Vector d}
    (hv : causalCharacter v = .lightLike) (hw : causalCharacter w = .lightLike)
    (h_spatial_parallel : ∃ (r : ℝ), v = r • w) :
    ∃ (r : ℝ), |v (Sum.inl 0)| = |r| * |w (Sum.inl 0)|
```

## Depends on

- [Physlib.Relativity.Causality.Basic](basic.md)

## Sources

- [Physlib/Relativity/Causality/LightLike.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Causality/LightLike.lean)
