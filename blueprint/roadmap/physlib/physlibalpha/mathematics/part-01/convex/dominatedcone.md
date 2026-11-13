---
declaration: module
origin: cited
lean: IsDominatedCone, IsDominatedCone.gaugeSet, IsDominatedCone.gaugeSet_nonempty, IsDominatedCone.bddBelow_gaugeSet, IsDominatedCone.add_mem_gaugeSet, IsDominatedCone.gaugeSet_smul, IsDominatedCone.gauge, IsDominatedCone.gauge_le
statement: formalized
proof: formalized
---

# Separation from dominated cones

The module `PhyslibAlpha.Mathematics.Convex.DominatedCone`, [PhyslibAlpha/Mathematics/Convex/DominatedCone.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Convex/DominatedCone.lean): 12 declarations, 4 with a docstring.

> Hahn–Banach separation of vectors from a convex cone dominated by a vector.

## i. Overview

> A convex cone `C` in a real vector space is dominated by `u ∈ C` when every vector plus some
> multiple of `u` lies in `C`, as the positive cone of an order-unit space is dominated by its unit.
> The least such multiple is a sublinear gauge. Whenever some linear functional is nonnegative on `C`
> and positive at `u`, the gauge is finite and Hahn–Banach turns it into separating functionals: a
> vector `v` with `v + ε • u ∉ C` is sent to a negative number by a functional nonnegative on `C`.
> No topology is involved.

## ii. Key results

> - `IsDominatedCone` : a convex cone dominated by a vector.
> - `IsDominatedCone.gauge` : the gauge of the cone relative to the dominating vector.
> - `IsDominatedCone.exists_apply_neg` : separation of a vector from a dominated cone.

## iv. References

> * None.

## A. Dominated cones and their gauge

**`IsDominatedCone`**, a structure, [line 51](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Convex/DominatedCone.lean#L51).

> A convex cone with a dominating element `u`: every vector plus a multiple of `u` lies in it.

```lean
structure IsDominatedCone (C : Set V) (u : V) : Prop where
  zero_mem : (0 : V) ∈ C
  add_mem : ∀ a ∈ C, ∀ b ∈ C, a + b ∈ C
  smul_mem : ∀ c : ℝ, 0 ≤ c → ∀ a ∈ C, c • a ∈ C
  mem : u ∈ C
  dominates : ∀ v, ∃ t : ℝ, v + t • u ∈ C
```

**`IsDominatedCone.gaugeSet`**, a def, [line 65](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Convex/DominatedCone.lean#L65).

> The multiples `t` of `u` with `t • u - w` in the cone.

```lean
def gaugeSet (C : Set V) (u w : V) : Set ℝ
```

**`IsDominatedCone.gaugeSet_nonempty`**, a lemma, [line 68](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Convex/DominatedCone.lean#L68).

```lean
lemma gaugeSet_nonempty (hC : IsDominatedCone C u) (w : V) : (gaugeSet C u w).Nonempty
```

**`IsDominatedCone.bddBelow_gaugeSet`**, a lemma, [line 75](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Convex/DominatedCone.lean#L75).

```lean
lemma bddBelow_gaugeSet (w : V) : BddBelow (gaugeSet C u w)
```

**`IsDominatedCone.add_mem_gaugeSet`**, a lemma, [line 82](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Convex/DominatedCone.lean#L82).

```lean
lemma add_mem_gaugeSet {w w' : V} {t t' : ℝ} (ht : t ∈ gaugeSet C u w)
    (ht' : t' ∈ gaugeSet C u w') : t + t' ∈ gaugeSet C u (w + w')
```

**`IsDominatedCone.gaugeSet_smul`**, a lemma, [line 89](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Convex/DominatedCone.lean#L89).

```lean
lemma gaugeSet_smul {c : ℝ} (hc : 0 < c) (w : V) :
    gaugeSet C u (c • w) = c • gaugeSet C u w
```

**`IsDominatedCone.gauge`**, a def, [line 105](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Convex/DominatedCone.lean#L105).

> The gauge of the cone with respect to `u`.

```lean
noncomputable def gauge (C : Set V) (u w : V) : ℝ
```

**`IsDominatedCone.gauge_le`**, a lemma, [line 108](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Convex/DominatedCone.lean#L108).

```lean
lemma gauge_le {w : V} {t : ℝ} (ht : t ∈ gaugeSet C u w) : gauge C u w ≤ t
```

**`IsDominatedCone.gauge_add_le`**, a lemma, [line 111](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Convex/DominatedCone.lean#L111).

```lean
lemma gauge_add_le (w w' : V) : gauge C u (w + w') ≤ gauge C u w + gauge C u w'
```

**`IsDominatedCone.gauge_smul`**, a lemma, [line 120](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Convex/DominatedCone.lean#L120).

```lean
lemma gauge_smul {c : ℝ} (hc : 0 < c) (w : V) : gauge C u (c • w) = c * gauge C u w
```

**`IsDominatedCone.gauge_zero`**, a lemma, [line 123](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Convex/DominatedCone.lean#L123).

```lean
lemma gauge_zero : gauge C u 0 = 0
```

## B. Separation

**`IsDominatedCone.exists_apply_neg`**, a lemma, [line 134](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Convex/DominatedCone.lean#L134).

> **Separation from a cone.** If `v + ε • u` is outside the cone, a linear functional that is
> nonnegative on the cone is negative at `v`.

```lean
lemma exists_apply_neg {v : V} {ε : ℝ} (hε : 0 < ε) (hv : v + ε • u ∉ C) :
    ∃ Λ : V →ₗ[ℝ] ℝ, (∀ c ∈ C, 0 ≤ Λ c) ∧ Λ v < 0
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Proof depends on

- [Linear minorants of sublinear functionals](../sublinear.md)

## Sources

- [PhyslibAlpha/Mathematics/Convex/DominatedCone.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Convex/DominatedCone.lean)
