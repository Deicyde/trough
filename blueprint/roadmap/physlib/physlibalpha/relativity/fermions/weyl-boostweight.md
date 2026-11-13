---
declaration: module
origin: cited
lean: Lorentz.weylWeight, Lorentz.rightHandedWeyl_rep_boostAxis_two_basis, Lorentz.leftHandedWeyl_rep_boostAxis_two_basis
statement: formalized
proof: formalized
---

# The boost weights of a Weyl spinor

The module `PhyslibAlpha.Relativity.Fermions.Weyl.BoostWeight`, [PhyslibAlpha/Relativity/Fermions/Weyl/BoostWeight.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/Fermions/Weyl/BoostWeight.lean): 3 declarations, 3 with a docstring.

## i. Overview

> Along the `z`-axis the `SL(2,ℂ)` boost is the diagonal matrix `diag (t, t⁻¹)`, so both
> Weyl bases are bases of boost eigenvectors: the first component carries weight `+1` and
> the second weight `-1`.  A Weyl spinor is a half-vector.

## ii. Key results

> - `weylWeight` : the boost weight of a Weyl-spinor index
> - `rightHandedWeyl_rep_boostAxis_two_basis` : the right-handed Weyl basis diagonalises the
>   `z`-boost, with weights `±1`
> - `leftHandedWeyl_rep_boostAxis_two_basis` : the left-handed Weyl basis diagonalises the `z`-boost,
>   with weights `±1`

## iv. References

> * None.

## A. The boost weight along the `z`-axis

**`Lorentz.weylWeight`**, a def, [line 53](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/Fermions/Weyl/BoostWeight.lean#L53).

> The boost weight of a Weyl-spinor index. Along the `z`-axis the `SL(2,ℂ)` boost is
> the diagonal matrix `diag (t, t⁻¹)`, so the first spinor component carries weight `+1` and
> the second weight `-1`; a Weyl spinor is a half-vector.

```lean
def weylWeight (k : Fin 2) : ℤ
```

**`Lorentz.rightHandedWeyl_rep_boostAxis_two_basis`**, a lemma, [line 56](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/Fermions/Weyl/BoostWeight.lean#L56).

> The right-handed Weyl basis diagonalises the `z`-boost, with weights `±1`.

```lean
lemma rightHandedWeyl_rep_boostAxis_two_basis (t : ℝ) (ht : t ≠ 0) (k : Fin 2) :
    Fermion.RightHandedWeyl.rep (SL2C.boostAxis 2 t ht) (Fermion.RightHandedWeyl.basis k)
      = ((t : ℝ) : ℂ) ^ (weylWeight k) • Fermion.RightHandedWeyl.basis k
```

**`Lorentz.leftHandedWeyl_rep_boostAxis_two_basis`**, a lemma, [line 64](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/Fermions/Weyl/BoostWeight.lean#L64).

> The left-handed Weyl basis diagonalises the `z`-boost, with weights `±1`.

```lean
lemma leftHandedWeyl_rep_boostAxis_two_basis (t : ℝ) (ht : t ≠ 0) (k : Fin 2) :
    Fermion.LeftHandedWeyl.rep (SL2C.boostAxis 2 t ht) (Fermion.LeftHandedWeyl.basis k)
      = ((t : ℝ) : ℂ) ^ (weylWeight k) • Fermion.LeftHandedWeyl.basis k
```

## Depends on

- [Left handed Weyl fermions](../../../physlib/relativity/fermions/weyl/lefthanded.md)
- [Right handed Weyl fermions](../../../physlib/relativity/fermions/weyl/righthanded.md)
- [Coordinate-axis boosts in `SL(2,ℂ)` and the Lorentz group](../../../physlib/relativity/lorentzgroup/boosts-axis.md)

## Sources

- [PhyslibAlpha/Relativity/Fermions/Weyl/BoostWeight.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/Fermions/Weyl/BoostWeight.lean)
