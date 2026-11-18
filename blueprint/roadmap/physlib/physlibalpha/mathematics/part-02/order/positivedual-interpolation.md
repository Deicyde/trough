---
declaration: module
origin: cited
lean: HasLatticeDualCone.exists_table, Interpolation.slacks, Interpolation.gauge, Interpolation.slacks_nonempty, Interpolation.slacks_bddBelow, Interpolation.gauge_le, Interpolation.add_mem_slacks, Interpolation.gauge_add_le
statement: formalized
proof: formalized
---

# Approximate interpolation

The module `PhyslibAlpha.Mathematics.Order.PositiveDual.Interpolation`, [PhyslibAlpha/Mathematics/Order/PositiveDual/Interpolation.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/PositiveDual/Interpolation.lean): 22 declarations, 10 with a docstring.

> Approximate interpolation between finite families when the positive functionals form a lattice.

## i. Overview

> Given finitely many lower elements `a i` below finitely many upper elements `b j` of an ordered
> real vector space with an order unit `u`, an interpolant is an element `g` with `a i ≤ g ≤ b j` for
> all `i` and `j`. When the positive functionals form a lattice, interpolants exist up to any error:
> for every `ε > 0` some `g` has `a i ≤ g + ε • u` and `g ≤ b j + ε • u`. The proof measures the
> failure to interpolate by a sublinear gauge; Hahn–Banach turns a linear functional below it into
> positive functionals, and refining these in the lattice of positive functionals shows the gauge is
> not positive.

## ii. Key results

> - `HasLatticeDualCone.exists_table` : two finite families of positive functionals with the same sum
>   have a common refinement.
> - `Interpolation.gauge` : the interpolation gauge.
> - `Interpolation.exists_linear_le_gauge` : a linear functional below the interpolation gauge.
> - `HasLatticeDualCone.exists_approx_interpolant` : approximate interpolants exist.

## iv. References

> * None.

## A. Refinement tables

**`HasLatticeDualCone.exists_table`**, a lemma, [line 65](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/PositiveDual/Interpolation.lean#L65).

> Two finite families of positive functionals with the same sum have a common refinement: a table
> whose rows add up to the first family and whose columns add up to the second.

```lean
lemma exists_table {n : ℕ} (θ : Fin n → E →ₚ[ℝ] ℝ) : ∀ {m : ℕ} (θ' : Fin m → E →ₚ[ℝ] ℝ),
    ∑ i, θ i = ∑ j, θ' j → ∃ τ : Fin n → Fin m → E →ₚ[ℝ] ℝ,
      (∀ i, ∑ j, τ i j = θ i) ∧ ∀ j, ∑ i, τ i j = θ' j
  | 0, θ', h => ⟨fun _ j => j.elim0, fun i => by
      simp only [Finset.univ_eq_empty, Finset.sum_empty] at h ⊢
      exact (le_antisymm (h ▸ le_sum θ (Finset.mem_univ i)) (zero_le _)).symm,
      fun j => j.elim0⟩
  | m + 1, θ', h => by
    rw [Fin.sum_univ_succ] at h
    obtain ⟨ψ₁, ψ₂, hψ, s₁, s₂⟩
```

## B. The interpolation gauge

**`Interpolation.slacks`**, a def, [line 95](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/PositiveDual/Interpolation.lean#L95).

> The slacks `μ` for which some `g` satisfies `v.1 i - g ≤ μ • u` and `g + v.2 j ≤ μ • u`.

```lean
def slacks (v : (Fin n → E) × (Fin m → E)) : Set ℝ
```

**`Interpolation.gauge`**, a def, [line 100](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/PositiveDual/Interpolation.lean#L100).

> The interpolation gauge: the least slack.

```lean
noncomputable def gauge (v : (Fin n → E) × (Fin m → E)) : ℝ
```

**`Interpolation.slacks_nonempty`**, a lemma, [line 103](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/PositiveDual/Interpolation.lean#L103).

```lean
lemma slacks_nonempty (v : (Fin n → E) × (Fin m → E)) : (slacks u v).Nonempty
```

**`Interpolation.slacks_bddBelow`**, a lemma, [line 110](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/PositiveDual/Interpolation.lean#L110).

```lean
lemma slacks_bddBelow (v : (Fin n → E) × (Fin m → E)) : BddBelow (slacks u v)
```

**`Interpolation.gauge_le`**, a lemma, [line 125](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/PositiveDual/Interpolation.lean#L125).

```lean
lemma gauge_le {v : (Fin n → E) × (Fin m → E)} {μ : ℝ} (hμ : μ ∈ slacks u v) : gauge u v ≤ μ
```

**`Interpolation.add_mem_slacks`**, a lemma, [line 129](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/PositiveDual/Interpolation.lean#L129).

```lean
lemma add_mem_slacks {v w : (Fin n → E) × (Fin m → E)} {μ ν : ℝ} (hμ : μ ∈ slacks u v)
    (hν : ν ∈ slacks u w) : μ + ν ∈ slacks u (v + w)
```

**`Interpolation.gauge_add_le`**, a lemma, [line 142](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/PositiveDual/Interpolation.lean#L142).

```lean
lemma gauge_add_le (v w : (Fin n → E) × (Fin m → E)) : gauge u (v + w) ≤ gauge u v + gauge u w
```

**`Interpolation.slacks_smul`**, a lemma, [line 150](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/PositiveDual/Interpolation.lean#L150).

```lean
lemma slacks_smul {c : ℝ} (hc : 0 < c) (v : (Fin n → E) × (Fin m → E)) :
    slacks u (c • v) = c • slacks u v
```

**`Interpolation.gauge_smul`**, a lemma, [line 168](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/PositiveDual/Interpolation.lean#L168).

```lean
lemma gauge_smul {c : ℝ} (hc : 0 < c) (v : (Fin n → E) × (Fin m → E)) :
    gauge u (c • v) = c * gauge u v
```

**`Interpolation.gauge_zero`**, a lemma, [line 174](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/PositiveDual/Interpolation.lean#L174).

```lean
lemma gauge_zero : gauge u (0 : (Fin n → E) × (Fin m → E)) = 0
```

**`Interpolation.gauge_nonpos`**, a lemma, [line 184](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/PositiveDual/Interpolation.lean#L184).

```lean
lemma gauge_nonpos {v : (Fin n → E) × (Fin m → E)} (hv₁ : ∀ i, v.1 i ≤ 0) (hv₂ : ∀ j, v.2 j ≤ 0) :
    gauge u v ≤ 0
```

**`Interpolation.mul_gauge_le`**, a lemma, [line 190](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/PositiveDual/Interpolation.lean#L190).

> The gauge scales at least linearly, also by negative factors.

```lean
lemma mul_gauge_le (t : (Fin n → E) × (Fin m → E)) (c : ℝ) : c * gauge u t ≤ gauge u (c • t)
```

**`Interpolation.exists_linear_le_gauge`**, a lemma, [line 201](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/PositiveDual/Interpolation.lean#L201).

> A linear functional below the interpolation gauge that attains it at `t`.

```lean
lemma exists_linear_le_gauge (t : (Fin n → E) × (Fin m → E)) :
    ∃ Λ : (Fin n → E) × (Fin m → E) →ₗ[ℝ] ℝ, (∀ v, Λ v ≤ gauge u v) ∧ Λ t = gauge u t
```

## C. Approximate interpolants

**`Interpolation.lowerPart`**, a def, [line 218](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/PositiveDual/Interpolation.lean#L218).

> The part of a linear functional acting on the `i`-th lower observable.

```lean
def lowerPart (Λ : (Fin n → E) × (Fin m → E) →ₗ[ℝ] ℝ) (i : Fin n) : E →ₗ[ℝ] ℝ
```

**`Interpolation.upperPart`**, a def, [line 223](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/PositiveDual/Interpolation.lean#L223).

> The part of a linear functional acting on the `j`-th upper observable.

```lean
def upperPart (Λ : (Fin n → E) × (Fin m → E) →ₗ[ℝ] ℝ) (j : Fin m) : E →ₗ[ℝ] ℝ
```

**`Interpolation.apply_eq_sum`**, a lemma, [line 228](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/PositiveDual/Interpolation.lean#L228).

```lean
lemma apply_eq_sum (v : (Fin n → E) × (Fin m → E)) :
    Λ v = ∑ i, lowerPart Λ i (v.1 i) + ∑ j, upperPart Λ j (v.2 j)
```

**`Interpolation.lowerPart_nonneg`**, a lemma, [line 241](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/PositiveDual/Interpolation.lean#L241).

```lean
lemma lowerPart_nonneg (i : Fin n) {x : E} (hx : 0 ≤ x) : 0 ≤ lowerPart Λ i x
```

**`Interpolation.upperPart_nonneg`**, a lemma, [line 250](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/PositiveDual/Interpolation.lean#L250).

```lean
lemma upperPart_nonneg (j : Fin m) {x : E} (hx : 0 ≤ x) : 0 ≤ upperPart Λ j x
```

**`Interpolation.sum_lowerPart`**, a lemma, [line 260](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/PositiveDual/Interpolation.lean#L260).

> The lower and the upper parts of a functional below the gauge have the same total.

```lean
lemma sum_lowerPart (h : E) : ∑ i, lowerPart Λ i h = ∑ j, upperPart Λ j h
```

**`HasLatticeDualCone.gauge_nonpos`**, a lemma, [line 281](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/PositiveDual/Interpolation.lean#L281).

> When the positive functionals form a lattice, lower observables below upper observables leave
> no positive interpolation slack.

```lean
lemma gauge_nonpos : gauge u (a, -b) ≤ 0
```

**`HasLatticeDualCone.exists_approx_interpolant`**, a lemma, [line 298](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/PositiveDual/Interpolation.lean#L298).

> **Approximate interpolation.** When the positive functionals form a lattice, lower observables
> below upper observables admit an interpolant up to any error.

```lean
lemma exists_approx_interpolant {ε : ℝ} (hε : 0 < ε) :
    ∃ g : E, (∀ i, a i ≤ g + ε • u) ∧ ∀ j, g ≤ b j + ε • u
```

## Depends on

- [The Riesz–Kantorovich formula](positivedual-rieszkantorovich.md)

## Proof depends on

- [Linear minorants of sublinear functionals](../../part-01/sublinear.md)

## Sources

- [PhyslibAlpha/Mathematics/Order/PositiveDual/Interpolation.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/PositiveDual/Interpolation.lean)
