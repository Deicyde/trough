---
declaration: module
origin: cited
lean: PositiveLinearMap.restrict, ProbabilisticTheory.UnitalPositiveLinearMap.restrict, PositiveLinearMap.restrictSA, PositiveLinearMap.coe_restrictSA_apply, PositiveLinearMap.restrictSAC, PositiveLinearMap.coe_restrictSAC_apply, ProbabilisticTheory.UnitalPositiveLinearMap.restrictSA, ProbabilisticTheory.UnitalPositiveLinearMap.coe_restrictSA_apply
statement: formalized
proof: formalized
---

# Restricting positive maps

The module `PhyslibAlpha.ProbabilisticTheory.StarAlgebra.Restrict`, [PhyslibAlpha/ProbabilisticTheory/StarAlgebra/Restrict.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/Restrict.lean): 10 declarations, 6 with a docstring.

> Restricting positive linear maps to submodules and to the self-adjoint elements.

## i. Overview

> A positive linear map restricts to submodules, in particular to the self-adjoint elements, where a
> complex state becomes a real one.

## ii. Key results

> - `PositiveLinearMap.restrict`, `UnitalPositiveLinearMap.restrict` : restriction to a submodule.
> - `UnitalPositiveLinearMap.restrictSA` : restriction to self-adjoint elements.

## iv. References

> * None.

## A. Restriction to submodules

**`PositiveLinearMap.restrict`**, a def, [line 56](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/Restrict.lean#L56).

> Restrict a positive linear map to submodules it preserves.

```lean
def _root_.PositiveLinearMap.restrict (f : E₁ →ₚ[R] E₂) {F₁ : Submodule S E₁} {F₂ : Submodule S E₂}
    (h : ∀ ⦃x⦄, x ∈ F₁ → f x ∈ F₂) : F₁ →ₚ[S] F₂
```

**`ProbabilisticTheory.UnitalPositiveLinearMap.restrict`**, a def, [line 64](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/Restrict.lean#L64).

> Restrict a unital positive linear map to submodules it preserves.

```lean
def UnitalPositiveLinearMap.restrict (f : E₁ →ₚ₁[R] E₂) {F₁ : Submodule S E₁} {F₂ : Submodule S E₂}
    [One F₁] [One F₂] (h₁ : ↑(1 : F₁) = (1 : E₁)) (h₂ : ↑(1 : F₂) = (1 : E₂))
    (h : ∀ ⦃x⦄, x ∈ F₁ → f x ∈ F₂) : F₁ →ₚ₁[S] F₂
```

## B. Positive maps on self-adjoint elements

**`PositiveLinearMap.restrictSA`**, a def, [line 98](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/Restrict.lean#L98).

> A positive linear map induces a positive real-linear map on self-adjoint elements.

```lean
noncomputable def restrictSA (f : A₁ →ₚ[ℂ] A₂) : selfAdjoint A₁ →ₚ[ℝ] selfAdjoint A₂
```

**`PositiveLinearMap.coe_restrictSA_apply`**, a lemma, [line 103](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/Restrict.lean#L103).

```lean
lemma coe_restrictSA_apply (f : A₁ →ₚ[ℂ] A₂) (x : selfAdjoint A₁) :
    ↑(f.restrictSA x) = f ↑x
```

**`PositiveLinearMap.restrictSAC`**, a def, [line 113](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/Restrict.lean#L113).

> A positive complex-linear functional induces a positive real-linear functional on
> self-adjoint elements.

```lean
noncomputable def restrictSAC (f : A₁ →ₚ[ℂ] ℂ) : selfAdjoint A₁ →ₚ[ℝ] ℝ
```

**`PositiveLinearMap.coe_restrictSAC_apply`**, a lemma, [line 117](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/Restrict.lean#L117).

```lean
lemma coe_restrictSAC_apply (f : A₁ →ₚ[ℂ] ℂ) (x : selfAdjoint A₁) :
    (f.restrictSAC x : ℂ) = f (x : A₁)
```

## C. Unital positive maps on self-adjoint elements

**`ProbabilisticTheory.UnitalPositiveLinearMap.restrictSA`**, a def, [line 156](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/Restrict.lean#L156).

> A unital positive linear map induces a unital positive real-linear map on
> self-adjoint elements.

```lean
noncomputable def restrictSA (f : A₁ →ₚ₁[ℂ] A₂) : selfAdjoint A₁ →ₚ₁[ℝ] selfAdjoint A₂
```

**`ProbabilisticTheory.UnitalPositiveLinearMap.coe_restrictSA_apply`**, a lemma, [line 162](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/Restrict.lean#L162).

```lean
lemma coe_restrictSA_apply (f : A₁ →ₚ₁[ℂ] A₂) (x : selfAdjoint A₁) :
    ↑(f.restrictSA x) = f ↑x
```

**`ProbabilisticTheory.UnitalPositiveLinearMap.restrictSAC`**, a def, [line 171](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/Restrict.lean#L171).

> A unital positive complex-linear functional induces a unital positive real-linear functional
> on self-adjoint elements.

```lean
noncomputable def restrictSAC (f : A₁ →ₚ₁[ℂ] ℂ) : selfAdjoint A₁ →ₚ₁[ℝ] ℝ
```

**`ProbabilisticTheory.UnitalPositiveLinearMap.coe_restrictSAC_apply`**, a lemma, [line 175](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/Restrict.lean#L175).

```lean
lemma coe_restrictSAC_apply (f : A₁ →ₚ₁[ℂ] ℂ) (x : selfAdjoint A₁) :
    (f.restrictSAC x : ℂ) = f (x : A₁)
```

## Depends on

- [Self-adjoint elements](selfadjoint.md)

## Sources

- [PhyslibAlpha/ProbabilisticTheory/StarAlgebra/Restrict.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/Restrict.lean)
