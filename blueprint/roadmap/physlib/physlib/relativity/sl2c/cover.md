---
declaration: module
origin: cited
lean: Lorentz.SL2C.exists_unitary_toLorentzGroup_eq, Lorentz.SL2C.exists_toVector_toLorentzGroup_eq, Lorentz.SL2C.toRestrictedLorentzGroup_surjective
statement: formalized
proof: formalized
---

# `SL(2, ℂ)` is a double cover of the restricted Lorentz group

The module `Physlib.Relativity.SL2C.Cover`, [Physlib/Relativity/SL2C/Cover.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/SL2C/Cover.lean): 3 declarations, 3 with a docstring.

## i. Overview

> The homomorphism `toRestrictedLorentzGroup` from `SL(2, ℂ)` to the restricted Lorentz group is
> surjective; together with the kernel `{1, -1}` (`toLorentzGroup_eq_one_iff`), this makes
> `SL(2, ℂ)` a double cover. Rotations come from the unitary elements, written with
> their Cayley–Klein parameters `a b`; the time axis is moved to any velocity by a lower
> triangular element. The proof follows the boost and rotation decomposition
> `LorentzGroup.exists_boost_mul_rotation`.

## ii. Key results

> - `exists_unitary_toLorentzGroup_eq` : every rotation is the image of a unitary element.
> - `toRestrictedLorentzGroup_surjective` : the homomorphism to the restricted Lorentz group is
>   surjective.

## iv. References

> * B. Oblak, *From the Lorentz Group to the Celestial Sphere*, arXiv:1508.00920,
>   Section 2.3.2.

## A. Rotations

**`Lorentz.SL2C.exists_unitary_toLorentzGroup_eq`**, a lemma, [line 58](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/SL2C/Cover.lean#L58).

> Every rotation is the image of a unitary element of `SL(2, ℂ)`.

```lean
lemma exists_unitary_toLorentzGroup_eq (Λ : LorentzGroup.Rotations 3) :
    ∃ M : SL(2, ℂ), M.1 ∈ unitaryGroup (Fin 2) ℂ ∧ toLorentzGroup M = Λ
```

## B. Boosts and surjectivity

**`Lorentz.SL2C.exists_toVector_toLorentzGroup_eq`**, a lemma, [line 119](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/SL2C/Cover.lean#L119).

> Every velocity is the image of the time axis under some element of `SL(2, ℂ)`.

```lean
lemma exists_toVector_toLorentzGroup_eq (u : Velocity 3) :
    ∃ M : SL(2, ℂ), LorentzGroup.toVector (toLorentzGroup M) = u.1
```

**`Lorentz.SL2C.toRestrictedLorentzGroup_surjective`**, a lemma, [line 139](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/SL2C/Cover.lean#L139).

> The homomorphism from `SL(2, ℂ)` to the restricted Lorentz group is surjective.

```lean
lemma toRestrictedLorentzGroup_surjective : Function.Surjective toRestrictedLorentzGroup
```

## Depends on

- [Rotations](../lorentzgroup/rotations.md)
- [The group SL(2, ℂ) and it's relation to the Lorentz group](basic.md)

## Proof depends on

- [The group SO(3)](../../mathematics/groups/so3-basic.md)
- [The construction of an element of the Lorentz group from a boost and a rotation](../lorentzgroup/restricted-fromboostrotation.md)
- [Cayley–Klein parameters](cayleyklein.md)

## Sources

- [Physlib/Relativity/SL2C/Cover.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/SL2C/Cover.lean)
