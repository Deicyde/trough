---
declaration: module
origin: cited
lean: PositiveLinearMap.upperEnvelope, PositiveLinearMap.upperBounds_nonempty, PositiveLinearMap.upperEnvelope_le, PositiveLinearMap.le_upperEnvelope, PositiveLinearMap.exists_mem_upperBounds_lt, PositiveLinearMap.add_mem_upperBounds, PositiveLinearMap.smul_mem_upperBounds, PositiveLinearMap.upperEnvelope_add_family_le
statement: formalized
proof: formalized
---

# Upper envelopes

The module `PhyslibAlpha.Mathematics.Order.PositiveDual.UpperEnvelope`, [PhyslibAlpha/Mathematics/Order/PositiveDual/UpperEnvelope.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/PositiveDual/UpperEnvelope.lean): 15 declarations, 5 with a docstring.

> Splittings of a positive functional attain the upper envelope of a finite family.

## i. Overview

> Take finitely many elements `A₁, …, Aₙ` of a directed ordered real vector space and a positive
> functional `φ`. Their upper envelope at `φ` is the smallest value `φ B` over all common upper
> bounds `B` of the `Aᵢ`.
>
> Split `φ` into positive pieces `φ₁ + … + φₙ` and let each piece evaluate its own element. The
> total `φ₁ A₁ + … + φₙ Aₙ` never exceeds the upper envelope, and by the Hahn–Banach theorem some
> splitting reaches it.

## ii. Key results

> - `PositiveLinearMap.upperEnvelope` is the upper envelope of finitely many elements.
> - `PositiveLinearMap.sum_apply_le_upperEnvelope` proves that splittings stay below the upper
>   envelope.
> - `PositiveLinearMap.exists_sum_eq_upperEnvelope` proves that some splitting reaches it.

## iv. References

> - E. M. Alfsen, *Compact Convex Sets and Boundary Integrals*, Springer, 1971, ch. I.3, II.3.

## A. Upper envelopes

**`PositiveLinearMap.upperEnvelope`**, a def, [line 61](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/PositiveDual/UpperEnvelope.lean#L61).

> The upper envelope of a finite family at a positive functional: the least value
> of the functional on a common upper bound of the family.

```lean
noncomputable def upperEnvelope (s : ι → E) (α : E →ₚ[ℝ] ℝ) : ℝ
```

**`PositiveLinearMap.upperBounds_nonempty`**, a lemma, [line 66](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/PositiveDual/UpperEnvelope.lean#L66).

> A finite family in a directed order has an upper bound.

```lean
lemma upperBounds_nonempty (s : ι → E) : (upperBounds (range s)).Nonempty
```

**`PositiveLinearMap.upperEnvelope_le`**, a lemma, [line 72](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/PositiveDual/UpperEnvelope.lean#L72).

```lean
lemma upperEnvelope_le [Nonempty ι] {b : E} (hb : b ∈ upperBounds (range s)) :
    upperEnvelope s α ≤ α b
```

**`PositiveLinearMap.le_upperEnvelope`**, a lemma, [line 79](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/PositiveDual/UpperEnvelope.lean#L79).

```lean
lemma le_upperEnvelope {r : ℝ} (h : ∀ b ∈ upperBounds (range s), r ≤ α b) :
    r ≤ upperEnvelope s α
```

**`PositiveLinearMap.exists_mem_upperBounds_lt`**, a lemma, [line 84](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/PositiveDual/UpperEnvelope.lean#L84).

```lean
lemma exists_mem_upperBounds_lt {r : ℝ} (h : upperEnvelope s α < r) :
    ∃ b ∈ upperBounds (range s), α b < r
```

**`PositiveLinearMap.add_mem_upperBounds`**, a lemma, [line 90](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/PositiveDual/UpperEnvelope.lean#L90).

```lean
lemma add_mem_upperBounds {c c' : ι → E} {b b' : E} (hb : b ∈ upperBounds (range c))
    (hb' : b' ∈ upperBounds (range c')) : b + b' ∈ upperBounds (range (c + c'))
```

**`PositiveLinearMap.smul_mem_upperBounds`**, a lemma, [line 96](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/PositiveDual/UpperEnvelope.lean#L96).

```lean
lemma smul_mem_upperBounds {c : ι → E} {b : E} {t : ℝ} (ht : 0 ≤ t)
    (hb : b ∈ upperBounds (range c)) : t • b ∈ upperBounds (range (t • c))
```

**`PositiveLinearMap.upperEnvelope_add_family_le`**, a lemma, [line 104](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/PositiveDual/UpperEnvelope.lean#L104).

```lean
lemma upperEnvelope_add_family_le (c c' : ι → E) :
    upperEnvelope (c + c') α ≤ upperEnvelope c α + upperEnvelope c' α
```

**`PositiveLinearMap.upperEnvelope_smul_family`**, a lemma, [line 115](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/PositiveDual/UpperEnvelope.lean#L115).

```lean
lemma upperEnvelope_smul_family {t : ℝ} (ht : 0 < t) (c : ι → E) :
    upperEnvelope (t • c) α = t * upperEnvelope c α
```

**`PositiveLinearMap.upperEnvelope_const_le`**, a lemma, [line 128](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/PositiveDual/UpperEnvelope.lean#L128).

```lean
lemma upperEnvelope_const_le (x : E) : upperEnvelope (fun _ : ι => x) α ≤ α x
```

**`PositiveLinearMap.upperEnvelope_single_le`**, a lemma, [line 132](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/PositiveDual/UpperEnvelope.lean#L132).

```lean
lemma upperEnvelope_single_le [DecidableEq ι] (i : ι) {x : E} (hx : x ≤ 0) :
    upperEnvelope (Pi.single i x) α ≤ 0
```

## B. Splittings attain the upper envelope

**`PositiveLinearMap.sum_apply_le_upperEnvelope`**, a lemma, [line 146](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/PositiveDual/UpperEnvelope.lean#L146).

> Splitting a functional and letting each piece evaluate its own element stays below the
> upper envelope.

```lean
lemma sum_apply_le_upperEnvelope {ψ : ι → E →ₚ[ℝ] ℝ} (hψ : ∑ i, ψ i = α) :
    ∑ i, ψ i (s i) ≤ upperEnvelope s α
```

**`PositiveLinearMap.piece`**, a def, [line 153](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/PositiveDual/UpperEnvelope.lean#L153).

> A linear functional on families below the upper envelope, seen on one member.

```lean
noncomputable def piece [DecidableEq ι] (g : (ι → E) →ₗ[ℝ] ℝ)
    (hg : ∀ c, g c ≤ upperEnvelope c α) (i : ι) : E →ₚ[ℝ] ℝ
```

**`PositiveLinearMap.sum_piece`**, a lemma, [line 162](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/PositiveDual/UpperEnvelope.lean#L162).

```lean
lemma sum_piece [DecidableEq ι] (g : (ι → E) →ₗ[ℝ] ℝ) (hg : ∀ c, g c ≤ upperEnvelope c α) :
    ∑ i, piece g hg i = α
```

**`PositiveLinearMap.exists_sum_eq_upperEnvelope`**, a lemma, [line 174](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/PositiveDual/UpperEnvelope.lean#L174).

> **Duality**: some splitting of the functional attains the upper envelope.

```lean
lemma exists_sum_eq_upperEnvelope (s : ι → E) (α : E →ₚ[ℝ] ℝ) :
    ∃ ψ : ι → E →ₚ[ℝ] ℝ, ∑ i, ψ i = α ∧ ∑ i, ψ i (s i) = upperEnvelope s α
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Proof depends on

- [Linear minorants of sublinear functionals](../../part-01/sublinear.md)

## Sources

- [PhyslibAlpha/Mathematics/Order/PositiveDual/UpperEnvelope.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/PositiveDual/UpperEnvelope.lean)
