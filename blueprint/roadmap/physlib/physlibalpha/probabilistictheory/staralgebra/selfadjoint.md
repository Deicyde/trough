---
declaration: module
origin: cited
lean: selfAdjoint.mem_selfAdjoint_iff_isSelfAdjoint, selfAdjoint.submodule_mem_iff, selfAdjoint.submoduleEquiv, selfAdjoint.submodulePLM, selfAdjoint.submodulePLMSymm, selfAdjoint.val_one_submodule, selfAdjoint.submoduleEquiv_one, selfAdjoint.submoduleEquiv_symm_one
statement: formalized
proof: formalized
---

# Self-adjoint elements

The module `PhyslibAlpha.ProbabilisticTheory.StarAlgebra.SelfAdjoint`, [PhyslibAlpha/ProbabilisticTheory/StarAlgebra/SelfAdjoint.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/SelfAdjoint.lean): 12 declarations (1 instance with no name), 6 with a docstring.

> Relating the predicate, subgroup and submodule descriptions of self-adjoint elements.

## i. Overview

> Mathlib describes self-adjointness by the predicate `IsSelfAdjoint`, the additive subgroup
> `selfAdjoint A` and a real submodule. This file relates these descriptions.

## ii. Key results

> - `selfAdjoint.submoduleEquiv` : the subgroup and the submodule of self-adjoint elements agree.
> - `selfAdjoint.submoduleUPLM` : the corresponding channel.

## iv. References

> * None.

## A. Membership in the self-adjoint part

**`selfAdjoint.mem_selfAdjoint_iff_isSelfAdjoint`**, a lemma, [line 48](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/SelfAdjoint.lean#L48).

```lean
lemma mem_selfAdjoint_iff_isSelfAdjoint {R : Type*} [AddGroup R] [StarAddMonoid R] (x : R) :
    x ∈ selfAdjoint R ↔ IsSelfAdjoint x
```

**`selfAdjoint.submodule_mem_iff`**, a lemma, [line 55](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/SelfAdjoint.lean#L55).

```lean
lemma submodule_mem_iff {x : A} : (x ∈ submodule R A) ↔ (x ∈ selfAdjoint A)
```

## B. Forgetting the submodule structure

**`selfAdjoint.submoduleEquiv`**, a def, [line 62](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/SelfAdjoint.lean#L62).

> The linear equivalence that forgets the `Submodule` structure on self-adjoint elements.

```lean
def submoduleEquiv : selfAdjoint.submodule R A ≃ₗ[R] selfAdjoint A
```

**`selfAdjoint.submodulePLM`**, a def, [line 72](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/SelfAdjoint.lean#L72).

> Forget the `Submodule` structure as a positive linear map.

```lean
def submodulePLM : submodule R A →ₚ[R] selfAdjoint A
```

**`selfAdjoint.submodulePLMSymm`**, a def, [line 78](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/SelfAdjoint.lean#L78).

> Inverse of `submodulePLM`. (There is no `PositiveLinearEquivalence` type.)

```lean
def submodulePLMSymm : selfAdjoint A →ₚ[R] submodule R A
```

## C. The unit and unital maps

**An instance with no name**, [line 86](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/SelfAdjoint.lean#L86).

```lean
instance : One (submodule R A)
```

**`selfAdjoint.val_one_submodule`**, a lemma, [line 89](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/SelfAdjoint.lean#L89).

```lean
lemma val_one_submodule : ↑(1 : submodule R A) = (1 : A)
```

**`selfAdjoint.submoduleEquiv_one`**, a lemma, [line 90](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/SelfAdjoint.lean#L90).

```lean
lemma submoduleEquiv_one : ↑(submoduleEquiv (R := R) (A := A) 1) = 1
```

**`selfAdjoint.submoduleEquiv_symm_one`**, a lemma, [line 91](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/SelfAdjoint.lean#L91).

```lean
lemma submoduleEquiv_symm_one : ↑(submoduleEquiv (R := R) (A := A).symm 1) = 1
```

**`selfAdjoint.submoduleUPLM`**, a def, [line 96](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/SelfAdjoint.lean#L96).

> Forget the `Submodule` structure as a unital positive linear map.

```lean
def submoduleUPLM : submodule R A →ₚ₁[R] selfAdjoint A
```

**`selfAdjoint.submoduleUPLMSymm`**, a def, [line 103](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/SelfAdjoint.lean#L103).

> Inverse of `submoduleUPLM`. (There is no `UnitalPositiveLinearEquivalence` type.)

```lean
def submoduleUPLMSymm : selfAdjoint A →ₚ₁[R] submodule R A
```

## D. Self-adjoint complex numbers

**`Complex.selfAdjointUPLM`**, a def, [line 118](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/SelfAdjoint.lean#L118).

> The map from self-adjoint complex numbers to real numbers as a unital positive linear map.

```lean
noncomputable def _root_.Complex.selfAdjointUPLM : selfAdjoint ℂ →ₚ₁[ℝ] ℝ
```

## Depends on

- [Channels](../channel/basic.md)

## Sources

- [PhyslibAlpha/ProbabilisticTheory/StarAlgebra/SelfAdjoint.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/SelfAdjoint.lean)
