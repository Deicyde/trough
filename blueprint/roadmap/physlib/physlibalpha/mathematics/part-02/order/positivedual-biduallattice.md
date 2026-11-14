---
declaration: module
origin: cited
lean: Bidual.splitValues, Bidual.splitValues_nonempty, Bidual.add_le_of_bound, Bidual.bddAbove_splitValues, Bidual.dsupFun, Bidual.le_dsupFun, Bidual.dsupFun_le, Bidual.dsupFun_add_le
statement: formalized
proof: formalized
---

# The bidual as a lattice

The module `PhyslibAlpha.Mathematics.Order.PositiveDual.BidualLattice`, [PhyslibAlpha/Mathematics/Order/PositiveDual/BidualLattice.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/PositiveDual/BidualLattice.lean): 15 declarations, 6 with a docstring.

> Least upper bounds in the bidual by the Riesz–Kantorovich formula; the bidual is a lattice.

## i. Overview

> When the positive functionals on `E` form a lattice, any two elements `x` and `y` of the bidual have
> a least upper bound. Its value on a positive functional `φ` is the best split of `φ` between `x`
> and `y`: the supremum of `x φ₁ + y φ₂` over `φ = φ₁ + φ₂`. This is the Riesz–Kantorovich formula
> with the roles of elements and functionals exchanged. The bidual then is a lattice.

## ii. Key results

> - `Bidual.dsup` : the least upper bound of two elements of the bidual.
> - `Bidual.isLUB_dsup` : it is the least upper bound.
> - `Bidual.instLattice` : when the positive functionals form a lattice, the bidual is a lattice.

## iv. References

> * None.

## A. Best splits of a positive functional

**`Bidual.splitValues`**, a def, [line 53](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/PositiveDual/BidualLattice.lean#L53).

> The values `x φ₁ + y φ₂` over the splittings `φ = φ₁ + φ₂`.

```lean
def splitValues (x y : Bidual E) (φ : E →ₚ[ℝ] ℝ) : Set ℝ
```

**`Bidual.splitValues_nonempty`**, a lemma, [line 57](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/PositiveDual/BidualLattice.lean#L57).

```lean
lemma splitValues_nonempty (x y : Bidual E) (φ : E →ₚ[ℝ] ℝ) : (splitValues x y φ).Nonempty
```

**`Bidual.add_le_of_bound`**, a lemma, [line 62](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/PositiveDual/BidualLattice.lean#L62).

> A split of `φ` evaluates to at most `φ (f + g)` when `f` dominates `x` and `g` dominates `y`.

```lean
lemma add_le_of_bound {x y : Bidual E} {f g : E} (hf : ∀ φ, |x φ| ≤ φ f) (hg : ∀ φ, |y φ| ≤ φ g)
    {φ φ₁ φ₂ : E →ₚ[ℝ] ℝ} (h : φ₁ + φ₂ = φ) : x φ₁ + y φ₂ ≤ φ (f + g)
```

**`Bidual.bddAbove_splitValues`**, a lemma, [line 72](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/PositiveDual/BidualLattice.lean#L72).

```lean
lemma bddAbove_splitValues (x y : Bidual E) (φ : E →ₚ[ℝ] ℝ) : BddAbove (splitValues x y φ)
```

**`Bidual.dsupFun`**, a def, [line 78](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/PositiveDual/BidualLattice.lean#L78).

> The best split of `φ` between `x` and `y`.

```lean
noncomputable def dsupFun (x y : Bidual E) (φ : E →ₚ[ℝ] ℝ) : ℝ
```

**`Bidual.le_dsupFun`**, a lemma, [line 81](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/PositiveDual/BidualLattice.lean#L81).

```lean
lemma le_dsupFun {x y : Bidual E} {φ φ₁ φ₂ : E →ₚ[ℝ] ℝ} (h : φ₁ + φ₂ = φ) :
    x φ₁ + y φ₂ ≤ dsupFun x y φ
```

**`Bidual.dsupFun_le`**, a lemma, [line 86](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/PositiveDual/BidualLattice.lean#L86).

```lean
lemma dsupFun_le {x y : Bidual E} {φ : E →ₚ[ℝ] ℝ} {r : ℝ}
    (h : ∀ φ₁ φ₂ : E →ₚ[ℝ] ℝ, φ₁ + φ₂ = φ → x φ₁ + y φ₂ ≤ r) : dsupFun x y φ ≤ r
```

**`Bidual.dsupFun_add_le`**, a lemma, [line 91](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/PositiveDual/BidualLattice.lean#L91).

```lean
lemma dsupFun_add_le (x y : Bidual E) (φ ψ : E →ₚ[ℝ] ℝ) :
    dsupFun x y φ + dsupFun x y ψ ≤ dsupFun x y (φ + ψ)
```

**`Bidual.dsupFun_add`**, a lemma, [line 108](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/PositiveDual/BidualLattice.lean#L108).

```lean
lemma dsupFun_add (x y : Bidual E) (φ ψ : E →ₚ[ℝ] ℝ) :
    dsupFun x y (φ + ψ) = dsupFun x y φ + dsupFun x y ψ
```

**`Bidual.dsupFun_zero`**, a lemma, [line 119](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/PositiveDual/BidualLattice.lean#L119).

```lean
lemma dsupFun_zero (x y : Bidual E) : dsupFun x y 0 = 0
```

**`Bidual.dsupFun_nnsmul`**, a lemma, [line 127](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/PositiveDual/BidualLattice.lean#L127).

```lean
lemma dsupFun_nnsmul (x y : Bidual E) (c : ℝ≥0) (φ : E →ₚ[ℝ] ℝ) :
    dsupFun x y (c • φ) = c * dsupFun x y φ
```

## B. The least upper bound

**`Bidual.dsup`**, a def, [line 154](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/PositiveDual/BidualLattice.lean#L154).

> The least upper bound of two elements of the bidual: the best split of each positive
> functional.

```lean
noncomputable def dsup (x y : Bidual E) : Bidual E
```

**`Bidual.dsup_apply`**, a lemma, [line 166](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/PositiveDual/BidualLattice.lean#L166).

```lean
lemma dsup_apply (x y : Bidual E) (φ : E →ₚ[ℝ] ℝ) : dsup hE x y φ = dsupFun x y φ
```

**`Bidual.isLUB_dsup`**, a lemma, [line 169](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/PositiveDual/BidualLattice.lean#L169).

> The best split is the least upper bound.

```lean
lemma isLUB_dsup (x y : Bidual E) : IsLUB {x, y} (dsup hE x y)
```

## C. The lattice structure

**`Bidual.instLattice`**, an instance, [line 193](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/PositiveDual/BidualLattice.lean#L193).

> When the positive functionals form a lattice, the bidual is a lattice.

```lean
noncomputable instance instLattice : Lattice (Bidual E)
```

## Depends on

- [The bidual](positivedual-bidual.md)
- [The Riesz–Kantorovich formula](positivedual-rieszkantorovich.md)

## Proof depends on

- [Approximate interpolation](positivedual-interpolation.md)

## Sources

- [PhyslibAlpha/Mathematics/Order/PositiveDual/BidualLattice.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/PositiveDual/BidualLattice.lean)
