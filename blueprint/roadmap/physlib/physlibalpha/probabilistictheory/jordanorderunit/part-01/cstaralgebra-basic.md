---
declaration: module
origin: cited
lean: ProbabilisticTheory.JB.one_mul, ProbabilisticTheory.JB.mul_self_eq, ProbabilisticTheory.JB.mul_self_nonneg, ProbabilisticTheory.JB.instIsJordanOrderUnit, ProbabilisticTheory.JB.norm_mul_le', ProbabilisticTheory.JB.instNormedJordanAlgebra, ProbabilisticTheory.JB.instCompleteSpace, ProbabilisticTheory.JB.norm_mul_self'
statement: formalized
proof: formalized
---

# The self-adjoint part of a C⋆-algebra is a JB-algebra

The module `PhyslibAlpha.ProbabilisticTheory.JordanOrderUnit.CStarAlgebra.Basic`, [PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/CStarAlgebra/Basic.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/CStarAlgebra/Basic.lean): 13 declarations, 8 with a docstring.

> The self-adjoint elements of a unital C⋆-algebra form a JB-algebra under `½ (a b + b a)`.

## i. Overview

> The self-adjoint elements of a unital C⋆-algebra, with the Jordan product `a ∘ b = ½ (a b + b a)`,
> form a JB-algebra. With this normalization the Jordan square is the ordinary square and the
> quadratic representation is `U_a b = a b a`, and Jordan projections are the ordinary projections.
> The instances are scoped to `JB`.

## ii. Key results

> - `JB.instIsJordanOrderUnit`, `JB.instJBAlgebra` : the Jordan order-unit and JB-algebra structures.
> - `JB.mul_self_eq` : the Jordan square is the ordinary square.
> - `JB.quadRep_eq_conj` : `U_a b = a b a`.
> - `JB.isJordanProjection_iff_isIdempotentElem` : Jordan projections are the ordinary projections.
> - `JB.jordanOrthogonal_iff` : Jordan orthogonality of `p`, `q` is `p q + q p = 0`.

## iv. References

> * None.

## A. C⋆ order compatibility

**`ProbabilisticTheory.JB.one_mul`**, a lemma, [line 58](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/CStarAlgebra/Basic.lean#L58).

```lean
lemma one_mul (a : selfAdjoint A) : (1 : selfAdjoint A) * a = a
```

**`ProbabilisticTheory.JB.mul_self_eq`**, a lemma, [line 69](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/CStarAlgebra/Basic.lean#L69).

> The Jordan square of a self-adjoint element, for the normalized product, is exactly its
> ordinary (associative) square. This is the reason `moment`/`variance` computed via the abstract
> `IsJordanOrderUnit` layer agree with the operator-theoretic ones.

```lean
lemma mul_self_eq (a : selfAdjoint A) : ((a * a : selfAdjoint A) : A) = (a : A) * (a : A)
```

**`ProbabilisticTheory.JB.mul_self_nonneg`**, a lemma, [line 73](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/CStarAlgebra/Basic.lean#L73).

```lean
lemma mul_self_nonneg (a : selfAdjoint A) : 0 ≤ a * a
```

**`ProbabilisticTheory.JB.instIsJordanOrderUnit`**, an instance, [line 80](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/CStarAlgebra/Basic.lean#L80).

> The self-adjoint part of a C⋆-algebra is a Jordan order-unit space.

```lean
noncomputable scoped instance instIsJordanOrderUnit : IsJordanOrderUnit (selfAdjoint A)
```

## B. The JB-algebra instance

**`ProbabilisticTheory.JB.norm_mul_le'`**, a lemma, [line 96](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/CStarAlgebra/Basic.lean#L96).

```lean
lemma norm_mul_le' (a b : selfAdjoint A) : ‖a * b‖ ≤ ‖a‖ * ‖b‖
```

**`ProbabilisticTheory.JB.instNormedJordanAlgebra`**, an instance, [line 109](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/CStarAlgebra/Basic.lean#L109).

> The self-adjoint part carries one coherent normed Jordan structure inherited from the ambient
> Cstar algebra.

```lean
noncomputable scoped instance instNormedJordanAlgebra : NormedJordanAlgebra (selfAdjoint A)
```

**`ProbabilisticTheory.JB.instCompleteSpace`**, an instance, [line 123](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/CStarAlgebra/Basic.lean#L123).

> The self-adjoint part of a Cstar algebra is complete because it is the closed fixed-point set
> of the continuous star operation.

```lean
scoped instance instCompleteSpace : CompleteSpace (selfAdjoint A)
```

**`ProbabilisticTheory.JB.norm_mul_self'`**, a lemma, [line 126](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/CStarAlgebra/Basic.lean#L126).

```lean
lemma norm_mul_self' (a : selfAdjoint A) : ‖a * a‖ = ‖a‖ ^ 2
```

**`ProbabilisticTheory.JB.norm_mul_self_le_add'`**, a lemma, [line 131](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/CStarAlgebra/Basic.lean#L131).

```lean
lemma norm_mul_self_le_add' (a b : selfAdjoint A) : ‖a * a‖ ≤ ‖a * a + b * b‖
```

**`ProbabilisticTheory.JB.instJBAlgebra`**, an instance, [line 146](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/CStarAlgebra/Basic.lean#L146).

> The self-adjoint part of a unital C⋆-algebra is a JB-algebra under `a ∘ b = ½ (a b + b a)`.

```lean
scoped instance instJBAlgebra : JBAlgebra (selfAdjoint A)
```

## C. Squares, `U_a = aba` and projections

**`ProbabilisticTheory.JB.quadRep_eq_conj`**, a lemma, [line 156](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/CStarAlgebra/Basic.lean#L156).

> **`U_a b = a b a`** for self-adjoint elements of a C⋆-algebra.

```lean
lemma quadRep_eq_conj (a b : selfAdjoint A) :
    ((JordanAlgebra.quadRep a b : selfAdjoint A) : A) = (a : A) * (b : A) * (a : A)
```

**`ProbabilisticTheory.JB.isJordanProjection_iff_isIdempotentElem`**, a lemma, [line 176](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/CStarAlgebra/Basic.lean#L176).

> **Realization identity**: a Jordan projection for the normalized product is exactly an ordinary
> idempotent, `p² = p`.

```lean
lemma isJordanProjection_iff_isIdempotentElem {p : selfAdjoint A} :
    JordanAlgebra.IsJordanProjection p ↔ IsIdempotentElem (p : A)
```

**`ProbabilisticTheory.JB.jordanOrthogonal_iff`**, a lemma, [line 184](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/CStarAlgebra/Basic.lean#L184).

> **Realization identity**: Jordan orthogonality for the normalized product is exactly ordinary
> operator orthogonality `p q = 0`.

```lean
lemma jordanOrthogonal_iff {p q : selfAdjoint A} :
    JordanAlgebra.JordanOrthogonal p q ↔ (p : A) * (q : A) + (q : A) * (p : A) = 0
```

## Depends on

- [The observables of a C⋆-algebra](../../../../physlib/probabilistictheory/cstaralgebra/orderunit.md)
- [Normed Jordan algebras and JB-algebras](jb-basic.md)
- [Moments, variance and Jordan projections](observable.md)
- [The Jordan product of observables](../../staralgebra/jordan.md)

## Sources

- [PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/CStarAlgebra/Basic.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/CStarAlgebra/Basic.lean)
