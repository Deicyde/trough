---
declaration: module
origin: cited
lean: LpBall.eq_one_of_mem_extremePoints, LpBall.abs_rpow_combo_lt, LpBall.abs_rpow_combo_le, LpBall.sum_abs_rpow_combo_lt, LpBall.extremePoints_lpBall, LpBall.vertex, LpBall.vertex_mem_l1Ball, LpBall.eq_vertex_of_mul_eq_one
statement: formalized
proof: formalized
---

# Extreme points of `ℓq` balls

The module `PhyslibAlpha.Mathematics.Convex.LpBall`, [PhyslibAlpha/Mathematics/Convex/LpBall.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Convex/LpBall.lean): 22 declarations, 11 with a docstring.

> The extreme points of the `ℓq` ball are its unit sphere, those of the `ℓ1` ball its vertices.

## i. Overview

> The closed `ℓq` ball `{a | ∑ |a i| ^ q ≤ 1}` in `ℝⁿ` is strictly convex for `1 < q < ∞`: its
> extreme points are its whole unit sphere. The `ℓ1` ball is instead a polytope, the convex hull of
> its `2n` vertices `± eᵢ`, and these vertices are its only extreme points.

## ii. Key results

> - `LpBall.extremePoints_lpBall` : the extreme points of the `ℓq` ball are its unit sphere.
> - `LpBall.l1Ball_eq_convexHull` : the `ℓ1` ball is the convex hull of its vertices.
> - `LpBall.vertex_isExtreme`, `LpBall.eq_vertex_of_isExtreme` : the extreme points of the `ℓ1` ball
>   are its vertices.

## iv. References

> * None.

## A. Extreme points of the `ℓq` ball

**`LpBall.eq_one_of_mem_extremePoints`**, a lemma, [line 51](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Convex/LpBall.lean#L51).

> An extreme point of a sublevel set `{g ≤ 1}` of a continuous function lies on `{g = 1}`.

```lean
lemma eq_one_of_mem_extremePoints {E : Type*} [NormedAddCommGroup E] [NormedSpace ℝ E]
    [Nontrivial E] {g : E → ℝ} (hg : Continuous g) {a : E}
    (ha : a ∈ Set.extremePoints ℝ {b | g b ≤ 1}) : g a = 1
```

**`LpBall.abs_rpow_combo_lt`**, a lemma, [line 60](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Convex/LpBall.lean#L60).

> `x ↦ |x| ^ p` is strictly convex for `p > 1`.

```lean
lemma abs_rpow_combo_lt (hp : 1 < p) {x y : ℝ} (hxy : x ≠ y) {t : ℝ} (ht0 : 0 < t)
    (ht1 : t < 1) : |t * x + (1 - t) * y| ^ p < t * |x| ^ p + (1 - t) * |y| ^ p
```

**`LpBall.abs_rpow_combo_le`**, a lemma, [line 75](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Convex/LpBall.lean#L75).

```lean
lemma abs_rpow_combo_le (hp : 1 < p) (x y t : ℝ) (ht0 : 0 ≤ t) (ht1 : t ≤ 1) :
    |t * x + (1 - t) * y| ^ p ≤ t * |x| ^ p + (1 - t) * |y| ^ p
```

**`LpBall.sum_abs_rpow_combo_lt`**, a lemma, [line 86](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Convex/LpBall.lean#L86).

```lean
lemma sum_abs_rpow_combo_lt (hp : 1 < p) {x y : Fin n → ℝ} (hxy : x ≠ y) {t : ℝ} (ht0 : 0 < t)
    (ht1 : t < 1) : ∑ i, |t * x i + (1 - t) * y i| ^ p <
      t * ∑ i, |x i| ^ p + (1 - t) * ∑ i, |y i| ^ p
```

**`LpBall.extremePoints_lpBall`**, a lemma, [line 95](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Convex/LpBall.lean#L95).

> The extreme points of the closed `ℓq` ball are its unit sphere.

```lean
lemma extremePoints_lpBall (hpq : p.HolderConjugate q) [NeZero n] :
    Set.extremePoints ℝ {a : Fin n → ℝ | ∑ i, |a i| ^ q ≤ 1} = {a | ∑ i, |a i| ^ q = 1}
```

## B. Extreme points of the `ℓ1` ball

**`LpBall.vertex`**, a def, [line 114](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Convex/LpBall.lean#L114).

> The vertex of the `ℓ1` ball with coordinate `s` at `i` and `0` elsewhere.

```lean
def vertex (i : Fin m) (s : ℝ) : Fin m → ℝ
```

**`LpBall.vertex_mem_l1Ball`**, a lemma, [line 116](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Convex/LpBall.lean#L116).

```lean
lemma vertex_mem_l1Ball (i : Fin m) {s : ℝ} (hs : |s| ≤ 1) : ∑ k, |vertex i s k| ≤ 1
```

**`LpBall.eq_vertex_of_mul_eq_one`**, a lemma, [line 120](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Convex/LpBall.lean#L120).

> A point of the `ℓ1` ball with `s * x i = 1`, `s = ±1`, is the vertex `vertex i s`.

```lean
lemma eq_vertex_of_mul_eq_one {x : Fin m → ℝ} (hx : ∑ k, |x k| ≤ 1) {i : Fin m} {s : ℝ}
    (hs : s = 1 ∨ s = -1) (h : s * x i = 1) : x = vertex i s
```

**`LpBall.mul_apply_le_one`**, a lemma, [line 132](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Convex/LpBall.lean#L132).

```lean
lemma mul_apply_le_one {x : Fin m → ℝ} (hx : ∑ k, |x k| ≤ 1) (i : Fin m) {s : ℝ}
    (hs : |s| = 1) : s * x i ≤ 1
```

**`LpBall.vertex_isExtreme`**, a lemma, [line 139](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Convex/LpBall.lean#L139).

> Every vertex of the `ℓ1` ball is extreme.

```lean
lemma vertex_isExtreme (i : Fin m) {s : ℝ} (hs : s = 1 ∨ s = -1) :
    vertex i s ∈ Set.extremePoints ℝ {a : Fin m → ℝ | ∑ k, |a k| ≤ 1}
```

**`LpBall.signedVertex`**, an abbrev, [line 152](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Convex/LpBall.lean#L152).

> The vertex `vertex i s` with `s = 1` or `s = -1` according to `b`.

```lean
abbrev signedVertex (j : Fin m × Bool) : Fin m → ℝ
```

**`LpBall.signedVertex_mem_l1Ball`**, a lemma, [line 154](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Convex/LpBall.lean#L154).

```lean
lemma signedVertex_mem_l1Ball (j : Fin m × Bool) : ∑ k, |signedVertex j k| ≤ 1
```

**`LpBall.signedVertex_isExtreme`**, a lemma, [line 157](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Convex/LpBall.lean#L157).

```lean
lemma signedVertex_isExtreme (j : Fin m × Bool) :
    signedVertex j ∈ Set.extremePoints ℝ {a : Fin m → ℝ | ∑ k, |a k| ≤ 1}
```

**`LpBall.signedVertex_injective`**, a lemma, [line 161](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Convex/LpBall.lean#L161).

```lean
lemma signedVertex_injective : Function.Injective (signedVertex (m := m))
```

**`LpBall.l1Weight`**, a def, [line 170](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Convex/LpBall.lean#L170).

> Convex weights on the signed vertices recovering a point of the `ℓ1` ball: the positive and
> negative parts of each coordinate, with the missing mass spread evenly.

```lean
noncomputable def l1Weight (a : Fin m → ℝ) (j : Fin m × Bool) : ℝ
```

**`LpBall.l1Weight_nonneg`**, a lemma, [line 173](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Convex/LpBall.lean#L173).

```lean
lemma l1Weight_nonneg {a : Fin m → ℝ} (ha : ∑ k, |a k| ≤ 1) (j : Fin m × Bool) :
    0 ≤ l1Weight a j
```

**`LpBall.sum_l1Weight`**, a lemma, [line 177](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Convex/LpBall.lean#L177).

```lean
lemma sum_l1Weight [NeZero m] (a : Fin m → ℝ) : ∑ j, l1Weight a j = 1
```

**`LpBall.sum_l1Weight_smul`**, a lemma, [line 186](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Convex/LpBall.lean#L186).

```lean
lemma sum_l1Weight_smul (a : Fin m → ℝ) : ∑ j, l1Weight a j • signedVertex j = a
```

**`LpBall.mem_convexHull_signedVertex`**, a lemma, [line 192](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Convex/LpBall.lean#L192).

> The `ℓ1` ball lies in the convex hull of its vertices.

```lean
lemma mem_convexHull_signedVertex [NeZero m] {a : Fin m → ℝ} (ha : ∑ k, |a k| ≤ 1) :
    a ∈ convexHull ℝ (Set.range signedVertex)
```

**`LpBall.convex_l1Ball`**, a lemma, [line 197](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Convex/LpBall.lean#L197).

```lean
lemma convex_l1Ball : Convex ℝ {a : Fin m → ℝ | ∑ k, |a k| ≤ 1}
```

**`LpBall.l1Ball_eq_convexHull`**, a lemma, [line 208](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Convex/LpBall.lean#L208).

> The `ℓ1` ball is the convex hull of its vertices.

```lean
lemma l1Ball_eq_convexHull [NeZero m] :
    {a : Fin m → ℝ | ∑ k, |a k| ≤ 1} = convexHull ℝ (Set.range signedVertex)
```

**`LpBall.eq_vertex_of_isExtreme`**, a lemma, [line 214](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Convex/LpBall.lean#L214).

> Every extreme point of the `ℓ1` ball is a vertex.

```lean
lemma eq_vertex_of_isExtreme [NeZero m] {a : Fin m → ℝ}
    (ha : a ∈ Set.extremePoints ℝ {a : Fin m → ℝ | ∑ k, |a k| ≤ 1}) :
    ∃ i s, (s = 1 ∨ s = -1) ∧ a = vertex i s
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [PhyslibAlpha/Mathematics/Convex/LpBall.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Convex/LpBall.lean)
