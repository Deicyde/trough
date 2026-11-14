---
declaration: module
origin: cited
lean: ProbabilisticTheory.JB.isJordanCompatible_of_commute
statement: formalized
proof: formalized
---

# Commuting observables are Jordan compatible

The module `PhyslibAlpha.ProbabilisticTheory.JordanOrderUnit.CStarAlgebra.Compatibility`, [PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/CStarAlgebra/Compatibility.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/CStarAlgebra/Compatibility.lean): 1 declaration, 1 with a docstring.

> Commuting self-adjoint elements of a C⋆-algebra are Jordan compatible.

## i. Overview

> If two self-adjoint elements of a C⋆-algebra commute, their Jordan multiplication operators commute.
> Expanding `a ∘ (b ∘ x)` and `b ∘ (a ∘ x)` in the associative product, the terms agree using `a b = b
> a`.

## ii. Key results

> - `JB.isJordanCompatible_of_commute` : commuting observables are Jordan compatible.

## iv. References

> * None.

## A. Commuting observables

**`ProbabilisticTheory.JB.isJordanCompatible_of_commute`**, a lemma, [line 50](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/CStarAlgebra/Compatibility.lean#L50).

> Commuting self-adjoint elements are Jordan compatible.

```lean
lemma isJordanCompatible_of_commute {a b : selfAdjoint A}
    (hcomm : (a : A) * (b : A) = (b : A) * (a : A)) :
    JordanAlgebra.IsJordanCompatible a b
```

## Depends on

- [Compatible observables](compatibility.md)
- [The self-adjoint part of a C⋆-algebra is a JB-algebra](cstaralgebra-basic.md)

## Sources

- [PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/CStarAlgebra/Compatibility.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/CStarAlgebra/Compatibility.lean)
