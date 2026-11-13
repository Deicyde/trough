---
declaration: module
origin: cited
lean: ProbabilisticTheory.Observable.nonneg_iff_exists_observable_sq, ProbabilisticTheory.Observable.posPart, ProbabilisticTheory.Observable.negPart, ProbabilisticTheory.Observable.posPart_sub_negPart, ProbabilisticTheory.Observable.posPart_mul_negPart, ProbabilisticTheory.Observable.negPart_mul_posPart, ProbabilisticTheory.Observable.posPart_negPart_unique
statement: formalized
proof: formalized
---

# Positive and negative parts of observables

The module `PhyslibAlpha.ProbabilisticTheory.CStarAlgebra.JordanDecomposition`, [PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/JordanDecomposition.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/JordanDecomposition.lean): 7 declarations, 7 with a docstring.

> Every observable of a C⋆-algebra splits uniquely into orthogonal positive and negative parts.

## i. Overview

> Every observable `a` of a C⋆-algebra splits uniquely as `a = a⁺ - a⁻` with `a⁺`, `a⁻` positive and
> orthogonal, `a⁺ a⁻ = 0`. This is the Jordan decomposition, the analogue of splitting a function or a
> signed measure into its positive and negative parts. Mathlib builds `a⁺` and `a⁻` by the continuous
> functional calculus; here they are positive observables.

## ii. Key results

> - `Observable.posPart`, `Observable.negPart` : the positive and negative parts.
> - `Observable.posPart_sub_negPart` : `a⁺ - a⁻ = a`.
> - `Observable.posPart_mul_negPart` : the parts are orthogonal.
> - `Observable.posPart_negPart_unique` : the decomposition is unique.

## iv. References

> * None.

## A. Positive observables

**`ProbabilisticTheory.Observable.nonneg_iff_exists_observable_sq`**, a lemma, [line 53](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/JordanDecomposition.lean#L53).

> An observable is positive exactly when it is the square of an observable.

```lean
lemma nonneg_iff_exists_observable_sq (a : Observable A) :
    0 ≤ (a : A) ↔ ∃ b : Observable A, (a : A) = (b : A) * b
```

## B. Positive and negative parts

**`ProbabilisticTheory.Observable.posPart`**, a def, [line 67](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/JordanDecomposition.lean#L67).

> The positive part of an observable.

```lean
noncomputable def posPart (a : Observable A) : PositiveObservable A
```

**`ProbabilisticTheory.Observable.negPart`**, a def, [line 71](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/JordanDecomposition.lean#L71).

> The negative part of an observable.

```lean
noncomputable def negPart (a : Observable A) : PositiveObservable A
```

**`ProbabilisticTheory.Observable.posPart_sub_negPart`**, a lemma, [line 75](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/JordanDecomposition.lean#L75).

> Every observable is the difference of its positive and negative parts.

```lean
lemma posPart_sub_negPart (a : Observable A) :
    (posPart a).1 - (negPart a).1 = a
```

**`ProbabilisticTheory.Observable.posPart_mul_negPart`**, a lemma, [line 81](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/JordanDecomposition.lean#L81).

> The positive and negative parts of an observable are orthogonal.

```lean
lemma posPart_mul_negPart (a : Observable A) :
    ((posPart a).1 : A) * (negPart a).1 = 0
```

**`ProbabilisticTheory.Observable.negPart_mul_posPart`**, a lemma, [line 86](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/JordanDecomposition.lean#L86).

> The negative and positive parts are orthogonal in the opposite order as well.

```lean
lemma negPart_mul_posPart (a : Observable A) :
    ((negPart a).1 : A) * (posPart a).1 = 0
```

**`ProbabilisticTheory.Observable.posPart_negPart_unique`**, a lemma, [line 92](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/JordanDecomposition.lean#L92).

> The positive/negative decomposition is the unique decomposition into orthogonal positive
> observables: this is the Jordan decomposition theorem.

```lean
lemma posPart_negPart_unique (a : Observable A) (b c : PositiveObservable A)
    (hsub : (a : A) = (b.1 : A) - c.1)
    (horth : (b.1 : A) * c.1 = 0) :
    posPart a = b ∧ negPart a = c
```

## Depends on

- [Observables](../staralgebra/observable.md)

## Sources

- [PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/JordanDecomposition.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/JordanDecomposition.lean)
