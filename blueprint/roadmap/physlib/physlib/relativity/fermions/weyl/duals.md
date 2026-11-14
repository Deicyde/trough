---
declaration: module
origin: cited
lean: Fermion.LeftHandedWeyl.dual, Fermion.LeftHandedWeyl.dual_hom_apply, Fermion.DualLeftHandedWeyl.dual, Fermion.DualLeftHandedWeyl.dual_hom_apply, Fermion.LeftHandedWeyl.dualEquiv, Fermion.LeftHandedWeyl.dualEquiv_hom_hom_apply, Fermion.LeftHandedWeyl.dualEquiv_inv_hom_apply
statement: formalized
proof: formalized
---

# Duals for fermions

The module `Physlib.Relativity.Fermions.Weyl.Duals`, [Physlib/Relativity/Fermions/Weyl/Duals.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/Duals.lean): 7 declarations, 5 with a docstring.

> In this file we give the relationship between Weyl fermions
> and their duals.

## Duals of Weyl fermions

> The dual of `LeftHandedWeyl` is `DualLeftHandedWeyl`, and the dual of `RightHandedWeyl` is
> `DualRightHandedWeyl`.

**`Fermion.LeftHandedWeyl.dual`**, a def, [line 45](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/Duals.lean#L45).

> The morphism between the representation `leftHanded` and the representation
> `dualLeftHanded` defined by multiplying an element of
> `leftHanded` by the matrix `εᵃ⁰ᵃ¹ = !![0, 1; -1, 0]]`.

```lean
def LeftHandedWeyl.dual : LeftHandedWeyl.rep.IntertwiningMap DualLeftHandedWeyl.rep
```

**`Fermion.LeftHandedWeyl.dual_hom_apply`**, a lemma, [line 66](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/Duals.lean#L66).

```lean
lemma LeftHandedWeyl.dual_hom_apply (ψ : LeftHandedWeyl) :
    LeftHandedWeyl.dual ψ =
    DualLeftHandedWeyl.toFin2ℂEquiv.symm (!![0, 1; -1, 0] *ᵥ ψ.toFin2ℂ)
```

**`Fermion.DualLeftHandedWeyl.dual`**, a def, [line 73](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/Duals.lean#L73).

> The morphism from `dualLeftHanded` to
> `leftHanded` defined by multiplying an element of
> DualLeftHandedWeyl by the matrix `εₐ₁ₐ₂ = !![0, -1; 1, 0]`.

```lean
def DualLeftHandedWeyl.dual : DualLeftHandedWeyl.rep.IntertwiningMap LeftHandedWeyl.rep
```

**`Fermion.DualLeftHandedWeyl.dual_hom_apply`**, a lemma, [line 97](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/Duals.lean#L97).

```lean
lemma DualLeftHandedWeyl.dual_hom_apply (ψ : DualLeftHandedWeyl) :
    DualLeftHandedWeyl.dual ψ =
    LeftHandedWeyl.toFin2ℂEquiv.symm (!![0, -1; 1, 0] *ᵥ ψ.toFin2ℂ)
```

**`Fermion.LeftHandedWeyl.dualEquiv`**, a def, [line 104](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/Duals.lean#L104).

> The equivalence between the representation `leftHanded` and the representation
> `dualLeftHanded` defined by multiplying an element of
> `leftHanded` by the matrix `εᵃ⁰ᵃ¹ = !![0, 1; -1, 0]]`.

```lean
def LeftHandedWeyl.dualEquiv : LeftHandedWeyl.rep.Equiv DualLeftHandedWeyl.rep
```

**`Fermion.LeftHandedWeyl.dualEquiv_hom_hom_apply`**, a lemma, [line 125](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/Duals.lean#L125).

> `leftHandedDualEquiv` acting on an element `ψ : leftHanded` corresponds
> to multiplying `ψ` by the matrix `!![0, 1; -1, 0]`.

```lean
lemma LeftHandedWeyl.dualEquiv_hom_hom_apply (ψ : LeftHandedWeyl) :
    LeftHandedWeyl.dualEquiv ψ =
    DualLeftHandedWeyl.toFin2ℂEquiv.symm (!![0, 1; -1, 0] *ᵥ ψ.toFin2ℂ)
```

**`Fermion.LeftHandedWeyl.dualEquiv_inv_hom_apply`**, a lemma, [line 131](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/Duals.lean#L131).

> The inverse of `leftHandedDualEquiv` acting on an element`ψ : dualLeftHanded` corresponds
> to multiplying `ψ` by the matrix `!![0, -1; 1, 0]`.

```lean
lemma LeftHandedWeyl.dualEquiv_inv_hom_apply (ψ : DualLeftHandedWeyl) :
    LeftHandedWeyl.dualEquiv.symm ψ =
    LeftHandedWeyl.toFin2ℂEquiv.symm (!![0, -1; 1, 0] *ᵥ ψ.toFin2ℂ)
```

## Depends on

- [Physlib.Meta.Informal.Basic](../../../meta/informal/basic.md)
- [Dual left handed Weyl fermions](duallefthanded.md)
- [Left handed Weyl fermions](lefthanded.md)

## Proof depends on

- [The group SL(2, ℂ) and it's relation to the Lorentz group](../../sl2c/basic.md)

## Sources

- [Physlib/Relativity/Fermions/Weyl/Duals.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Fermions/Weyl/Duals.lean)
