---
declaration: module
origin: cited
lean: Lorentz.Vector.causallyFollows_zero_iff, Lorentz.Vector.causallyFollows_zero_sub, Lorentz.Vector.norm_spatialPart_le_timeComponent_of_causallyFollows, Lorentz.Vector.sqrt_mul_sqrt_le_minkowskiProduct_of_causallyFollows, Lorentz.Vector.sqrt_add_sqrt_le_sqrt_add_of_causallyFollows, Lorentz.Vector.causallyFollows_zero_add_of_causallyFollows, Lorentz.Vector.minkowskiProduct_eq_iff_of_causallyFollows, Lorentz.Vector.sqrt_add_eq_iff_of_causallyFollows
statement: formalized
proof: formalized
---

# Vectors in the causal future of the origin

The module `Physlib.Relativity.Causality.CausallyFollows`, [Physlib/Relativity/Causality/CausallyFollows.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Causality/CausallyFollows.lean): 8 declarations, 8 with a docstring.

## i. Overview

> A vector `u` with `causallyFollows 0 u` is future-directed causal: time-like or light-like with a
> nonnegative time component (`causallyFollows_zero_iff`). For two such vectors of Minkowski space
> (signature `+---`), the Minkowski product dominates the product of the Minkowski norms,
> `⟪u, v⟫ₘ ≥ √⟪u, u⟫ₘ √⟪v, v⟫ₘ` (reverse Cauchy-Schwarz inequality), and the Minkowski norm of the
> sum dominates the sum of the norms, `√⟪u + v, u + v⟫ₘ ≥ √⟪u, u⟫ₘ + √⟪v, v⟫ₘ` (reverse triangle
> inequality). The proofs reduce to the elementary inequality `√(a² - c²) √(b² - d²) ≤ a b - c d` for
> `0 ≤ c ≤ a`, `0 ≤ d ≤ b`, applied to the time components and the Euclidean norms of the spatial
> parts, together with the Euclidean Cauchy-Schwarz inequality.

## ii. Key results

> - `causallyFollows_zero_iff`: `causallyFollows 0 u ↔ 0 ≤ ⟪u, u⟫ₘ ∧ 0 ≤ u⁰`;
>   `causallyFollows_zero_sub`: `q - p` is in the causal future of `0` when `q` causally follows `p`.
> - `norm_spatialPart_le_timeComponent_of_causallyFollows`: `‖u_spatial‖ ≤ u⁰`.
> - `sqrt_mul_sqrt_le_minkowskiProduct_of_causallyFollows`: the reverse Cauchy-Schwarz inequality.
> - `sqrt_add_sqrt_le_sqrt_add_of_causallyFollows`: the reverse triangle inequality;
>   `causallyFollows_zero_add_of_causallyFollows`.
> - `minkowskiProduct_eq_iff_of_causallyFollows`: equality in the reverse Cauchy-Schwarz inequality
>   holds if and only if the two vectors are proportional (with a nonnegative factor).
> - `sqrt_add_eq_iff_of_causallyFollows`: equality in the reverse triangle inequality holds if and
>   only if equality holds in the reverse Cauchy-Schwarz inequality.

## A. The causal future of the origin

**`Lorentz.Vector.causallyFollows_zero_iff`**, a lemma, [line 63](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Causality/CausallyFollows.lean#L63).

> A vector is in the causal future of the origin if and only if it is time-like or light-like
> (`0 ≤ ⟪u, u⟫ₘ`) with a nonnegative time component.

```lean
lemma causallyFollows_zero_iff {d : ℕ} {u : Vector d} :
    causallyFollows 0 u ↔ 0 ≤ ⟪u, u⟫ₘ ∧ 0 ≤ u.timeComponent
```

**`Lorentz.Vector.causallyFollows_zero_sub`**, a lemma, [line 85](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Causality/CausallyFollows.lean#L85).

> The vector from `p` to `q` is in the causal future of the origin when `q` causally
> follows `p`.

```lean
lemma causallyFollows_zero_sub {d : ℕ} {p q : Vector d} (h : causallyFollows p q) :
    causallyFollows 0 (q - p)
```

## B. The reverse Cauchy-Schwarz inequality

**`Lorentz.Vector.norm_spatialPart_le_timeComponent_of_causallyFollows`**, a lemma, [line 98](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Causality/CausallyFollows.lean#L98).

> For a vector in the causal future of the origin, the Euclidean norm of the spatial part is at
> most the time component.

```lean
lemma norm_spatialPart_le_timeComponent_of_causallyFollows {d : ℕ} {u : Vector d}
    (hu : causallyFollows 0 u) : ‖u.spatialPart‖ ≤ u.timeComponent
```

**`Lorentz.Vector.sqrt_mul_sqrt_le_minkowskiProduct_of_causallyFollows`**, a lemma, [line 106](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Causality/CausallyFollows.lean#L106).

> The reverse Cauchy-Schwarz inequality: for `u`, `v` in the causal future of the origin,
> `√⟪u, u⟫ₘ √⟪v, v⟫ₘ ≤ ⟪u, v⟫ₘ`.

```lean
lemma sqrt_mul_sqrt_le_minkowskiProduct_of_causallyFollows {d : ℕ} {u v : Vector d}
    (hu : causallyFollows 0 u) (hv : causallyFollows 0 v) : √⟪u, u⟫ₘ * √⟪v, v⟫ₘ ≤ ⟪u, v⟫ₘ
```

## C. The reverse triangle inequality

**`Lorentz.Vector.sqrt_add_sqrt_le_sqrt_add_of_causallyFollows`**, a lemma, [line 138](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Causality/CausallyFollows.lean#L138).

> The reverse triangle inequality: for `u`, `v` in the causal future of the origin,
> `√⟪u, u⟫ₘ + √⟪v, v⟫ₘ ≤ √⟪u + v, u + v⟫ₘ`.

```lean
lemma sqrt_add_sqrt_le_sqrt_add_of_causallyFollows {d : ℕ} {u v : Vector d}
    (hu : causallyFollows 0 u) (hv : causallyFollows 0 v) :
    √⟪u, u⟫ₘ + √⟪v, v⟫ₘ ≤ √⟪u + v, u + v⟫ₘ
```

**`Lorentz.Vector.causallyFollows_zero_add_of_causallyFollows`**, a lemma, [line 151](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Causality/CausallyFollows.lean#L151).

> The sum of two vectors in the causal future of the origin is in the causal future of the
> origin.

```lean
lemma causallyFollows_zero_add_of_causallyFollows {d : ℕ} {u v : Vector d}
    (hu : causallyFollows 0 u) (hv : causallyFollows 0 v) : causallyFollows 0 (u + v)
```

## D. The equality cases

**`Lorentz.Vector.minkowskiProduct_eq_iff_of_causallyFollows`**, a lemma, [line 174](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Causality/CausallyFollows.lean#L174).

> Equality in the reverse Cauchy-Schwarz inequality: for `u`, `v` in the causal future of the
> origin, `⟪u, v⟫ₘ = √⟪u, u⟫ₘ √⟪v, v⟫ₘ` if and only if one of the vectors is a nonnegative
> multiple of the other.

```lean
lemma minkowskiProduct_eq_iff_of_causallyFollows {d : ℕ} {u v : Vector d} (hu : causallyFollows 0 u)
    (hv : causallyFollows 0 v) :
    ⟪u, v⟫ₘ = √⟪u, u⟫ₘ * √⟪v, v⟫ₘ ↔ ∃ μ : ℝ, 0 ≤ μ ∧ (v = μ • u ∨ u = μ • v)
```

**`Lorentz.Vector.sqrt_add_eq_iff_of_causallyFollows`**, a lemma, [line 255](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Causality/CausallyFollows.lean#L255).

> Equality in the reverse triangle inequality holds if and only if equality holds in the
> reverse Cauchy-Schwarz inequality.

```lean
lemma sqrt_add_eq_iff_of_causallyFollows {d : ℕ} {u v : Vector d} (hu : causallyFollows 0 u)
    (hv : causallyFollows 0 v) :
    √⟪u + v, u + v⟫ₘ = √⟪u, u⟫ₘ + √⟪v, v⟫ₘ ↔ ⟪u, v⟫ₘ = √⟪u, u⟫ₘ * √⟪v, v⟫ₘ
```

## Depends on

- [Physlib.Relativity.Causality.Basic](basic.md)

## Proof depends on

- [Physlib.Relativity.Causality.LightLike](lightlike.md)
- [Physlib.Relativity.Causality.TimeLike](timelike.md)

## Sources

- [Physlib/Relativity/Causality/CausallyFollows.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Causality/CausallyFollows.lean)
