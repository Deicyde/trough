---
declaration: module
origin: cited
lean: LorentzGroup.fermionicParity, LorentzGroup.toSelfAdjointMap_fermionicParity, LorentzGroup.toLorentzGroup_fermionicParity, LorentzGroup.fermionicParity_sq, LorentzGroup.fermionicParity_ne_one, LorentzGroup.complexCoVector_SL2CRep_fermionicParity, LorentzGroup.rightHandedWeyl_rep_fermionicParity
statement: formalized
proof: formalized
---

# Fermionic parity

The module `PhyslibAlpha.Relativity.LorentzGroup.FermionicParity`, [PhyslibAlpha/Relativity/LorentzGroup/FermionicParity.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/FermionicParity.lean): 7 declarations, 6 with a docstring.

## i. Overview

> The homomorphism `SL(2, ℂ) → LorentzGroup 3` is two-to-one, and the nontrivial element of its
> kernel is `-1`. Physically it is the rotation by `2π`: it acts as the identity on every tensor,
> and as `-1` on every spinor, so it measures the parity of the number of fermionic indices
> carried by a quantity. We call it the *fermionic parity*.
>
> Because it lies in the Lorentz group's double cover and projects to the identity, any quantity
> required to be invariant under `SL(2, ℂ)` is fixed by it. A quantity carrying an odd number of
> spinor indices is negated by it, and therefore vanishes: this is the selection rule that forbids
> terms with an odd number of fermions.

## ii. Key results

> - `LorentzGroup.fermionicParity` : the nontrivial element of the kernel of the covering
>   `SL(2, ℂ) → LorentzGroup 3`.
> - `LorentzGroup.toSelfAdjointMap_fermionicParity` : it acts trivially on self-adjoint matrices.
> - `LorentzGroup.toLorentzGroup_fermionicParity` : it projects to the identity Lorentz
>   transformation.
> - `LorentzGroup.fermionicParity_sq` : it squares to one.
> - `LorentzGroup.fermionicParity_ne_one` : it is not itself the identity.

## iv. References

> * None.

## A. Fermionic parity

**`LorentzGroup.fermionicParity`**, a def, [line 63](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/FermionicParity.lean#L63).

> Fermionic parity: the nontrivial element `-1` of the kernel of the two-to-one homomorphism
> `SL(2, ℂ) → LorentzGroup 3`, that is the rotation by `2π`. It acts trivially on tensors and by
> `-1` on spinors.

```lean
def fermionicParity : SL(2, ℂ)
```

**`LorentzGroup.toSelfAdjointMap_fermionicParity`**, a lemma, [line 67](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/FermionicParity.lean#L67).

> Fermionic parity acts trivially on self-adjoint matrices: conjugation by `-1` is the
> identity.

```lean
lemma toSelfAdjointMap_fermionicParity :
    Lorentz.SL2C.toSelfAdjointMap fermionicParity = LinearMap.id
```

**`LorentzGroup.toLorentzGroup_fermionicParity`**, a lemma, [line 75](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/FermionicParity.lean#L75).

> Fermionic parity projects to the identity Lorentz transformation: it is invisible on
> tensors.

```lean
lemma toLorentzGroup_fermionicParity :
    Lorentz.SL2C.toLorentzGroup fermionicParity = 1
```

**`LorentzGroup.fermionicParity_sq`**, a lemma, [line 84](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/FermionicParity.lean#L84).

```lean
lemma fermionicParity_sq : fermionicParity ^ 2 = 1
```

**`LorentzGroup.fermionicParity_ne_one`**, a lemma, [line 90](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/FermionicParity.lean#L90).

> Fermionic parity is not the identity of `SL(2, ℂ)`: the covering is genuinely
> two-to-one.

```lean
lemma fermionicParity_ne_one : fermionicParity ≠ 1
```

## B. The action on vectors and on spinors

> Fermionic parity is invisible on Lorentz vectors and acts by `-1` on Weyl spinors: this is what
> makes it measure the parity of the number of spinor indices.

**`LorentzGroup.complexCoVector_SL2CRep_fermionicParity`**, a lemma, [line 109](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/FermionicParity.lean#L109).

> Fermionic parity acts trivially on complex covariant Lorentz vectors, since it projects to
> the identity Lorentz transformation.

```lean
lemma complexCoVector_SL2CRep_fermionicParity :
    Lorentz.ComplexCoVector.SL2CRep fermionicParity = LinearMap.id
```

**`LorentzGroup.rightHandedWeyl_rep_fermionicParity`**, a lemma, [line 118](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/FermionicParity.lean#L118).

> Fermionic parity acts by `-1` on right-handed Weyl spinors.

```lean
lemma rightHandedWeyl_rep_fermionicParity :
    Fermion.RightHandedWeyl.rep fermionicParity = -LinearMap.id
```

## Depends on

- [Right handed Weyl fermions](../../../physlib/relativity/fermions/weyl/righthanded.md)
- [Physlib.Relativity.Tensors.ComplexTensor.Vector.Modules](../../../physlib/relativity/tensors/part-02/complextensor-vector-modules.md)

## Proof depends on

- [Complex Lorentz vectors](../../../physlib/relativity/tensors/part-02/complextensor-vector-basic.md)

## Sources

- [PhyslibAlpha/Relativity/LorentzGroup/FermionicParity.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/FermionicParity.lean)
