---
declaration: module
origin: cited
lean: ProbabilisticTheory.JB.nonneg_iff_exists_jpow_two, ProbabilisticTheory.JB.quadRep_nonneg, ProbabilisticTheory.JB.JordanAlgebra.IsJordanProjection.conditionCStar, ProbabilisticTheory.JB.jordanOrthogonal_posPart_negPart
statement: formalized
proof: formalized
---

# Jordan positivity in a C⋆-algebra

The module `PhyslibAlpha.ProbabilisticTheory.JordanOrderUnit.CStarAlgebra.Positivity`, [PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/CStarAlgebra/Positivity.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/CStarAlgebra/Positivity.lean): 5 declarations (1 instance with no name), 5 with a docstring.

> In a C⋆-algebra, nonnegative observables are Jordan squares and `a₊ ∘ a₋ = 0`.

## i. Overview

> In a C⋆-algebra an observable is nonnegative iff it is a Jordan square, and its positive and
> negative parts are Jordan orthogonal.

## ii. Key results

> - `JB.nonneg_iff_exists_jpow_two` : the positive observables are the Jordan squares.
> - `JB.jordanOrthogonal_posPart_negPart` : positive and negative parts are Jordan orthogonal.
> - `JB.quadRep_nonneg` : the quadratic representation `U_a` preserves positivity.
> - `JB.JordanAlgebra.IsJordanProjection.conditionCStar` : conditioning a state on a projection.

## iv. References

> * None.

## A. Positivity via the Jordan square

**`ProbabilisticTheory.JB.nonneg_iff_exists_jpow_two`**, a lemma, [line 57](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/CStarAlgebra/Positivity.lean#L57).

> An observable is positive exactly when it is the Jordan square of an observable — the Jordan
> form of `Observable.nonneg_iff_exists_observable_sq`, via `mul_self_eq` identifying the Jordan
> square of a single element with its ordinary square.

```lean
lemma nonneg_iff_exists_jpow_two (a : selfAdjoint A) :
    0 ≤ (a : A) ↔
      ∃ b : selfAdjoint A, (a : A) = ((JordanAlgebra.jpow b 2 : selfAdjoint A) : A)
```

**`ProbabilisticTheory.JB.quadRep_nonneg`**, a lemma, [line 65](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/CStarAlgebra/Positivity.lean#L65).

> The quadratic representation of a C⋆-algebra preserves positivity, since `U_a b = a b a`.

```lean
lemma quadRep_nonneg (a : selfAdjoint A) {b : selfAdjoint A} (hb : 0 ≤ b) :
    0 ≤ JordanAlgebra.quadRep a b
```

**An instance with no name**, [line 75](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/CStarAlgebra/Positivity.lean#L75).

> The canonical self-adjoint Cstar realization supplies the abstract quadratic-order
> capability.  Thus generic Jordan measurement code can use `U_a` as a positive operation without
> depending on this realization; this instance is only the concrete discharge of that capability.

```lean
instance : JordanAlgebra.IsQuadraticallyPositive (selfAdjoint A)
```

**`ProbabilisticTheory.JB.JordanAlgebra.IsJordanProjection.conditionCStar`**, a def, [line 81](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/CStarAlgebra/Positivity.lean#L81).

> Projection conditioning in the canonical Cstar Jordan realization.  In contrast to the
> abstract constructor, no separate quadratic-positivity argument is required: it is supplied by
> the shared `IsQuadraticallyPositive` instance.

```lean
noncomputable def JordanAlgebra.IsJordanProjection.conditionCStar {p : selfAdjoint A}
    (hp : JordanAlgebra.IsJordanProjection p) (ω : 𝓢[ℝ, selfAdjoint A]) (hmass : 0 < ω p) :
    𝓢[ℝ, selfAdjoint A]
```

## B. Orthogonality of the Jordan decomposition

**`ProbabilisticTheory.JB.jordanOrthogonal_posPart_negPart`**, a lemma, [line 90](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/CStarAlgebra/Positivity.lean#L90).

> The positive and negative parts of an observable are Jordan-orthogonal, `a₊ ∘ a₋ = 0`: the
> Jordan form of `Observable.posPart_mul_negPart`/`.negPart_mul_posPart`.

```lean
lemma jordanOrthogonal_posPart_negPart (a : selfAdjoint A) :
    JordanAlgebra.JordanOrthogonal (Observable.posPart a).1 (Observable.negPart a).1
```

## Depends on

- [Positive and negative parts of observables](../../cstaralgebra/jordandecomposition.md)
- [Conditioning a state on a projection](conditioning.md)
- [The self-adjoint part of a C⋆-algebra is a JB-algebra](cstaralgebra-basic.md)

## Sources

- [PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/CStarAlgebra/Positivity.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/CStarAlgebra/Positivity.lean)
