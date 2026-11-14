---
declaration: module
origin: cited
lean: ProbabilisticTheory.JBAlgebra.nonneg_iff_exists_mul_self
statement: formalized
proof: formalized
---

# The positive cone of a JB-algebra

The module `PhyslibAlpha.ProbabilisticTheory.JordanOrderUnit.JB.Order`, [PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/JB/Order.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/JB/Order.lean): 1 declaration, 1 with a docstring.

> In an ordered JB-algebra the nonnegative observables are exactly the squares.

## i. Overview

> In an ordered JB-algebra the nonnegative observables are exactly the squares: every nonnegative
> observable is a square in its closed one-generator subalgebra.

## ii. Key results

> - `JBAlgebra.nonneg_iff_exists_mul_self` : the nonnegative observables are the squares.

## iv. References

> * None.

## A. Nonnegative observables are squares

**`ProbabilisticTheory.JBAlgebra.nonneg_iff_exists_mul_self`**, a lemma, [line 46](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/JB/Order.lean#L46).

> **The nonnegative observables of an ordered JB-algebra are the squares.**

```lean
lemma nonneg_iff_exists_mul_self (a : E) :
    0 ≤ a ↔ ∃ b : E, b * b = a
```

## Depends on

- [Normed Jordan algebras and JB-algebras](../part-01/jb-basic.md)

## Proof depends on

- [Positive elements of `C(a)`](jb-generatedbyone-posinvertibility.md)

## Sources

- [PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/JB/Order.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/JB/Order.lean)
