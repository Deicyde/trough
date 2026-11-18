---
declaration: module
origin: cited
lean: ProbabilisticTheory.NormedJordanAlgebra.jordanPolyEval, ProbabilisticTheory.NormedJordanAlgebra.aevalCoe_eq_jordanPolyEval, ProbabilisticTheory.NormedJordanAlgebra.jordanPolyEval_add, ProbabilisticTheory.NormedJordanAlgebra.jordanPolyEval_comp_sq, ProbabilisticTheory.NormedJordanAlgebra.jordanCfc_toContinuousMapOnAlgHom, ProbabilisticTheory.NormedJordanAlgebra.norm_jordanPolyEval_sub_jordanCfc_le, ProbabilisticTheory.NormedJordanAlgebra.exists_polynomialRepresentative_of_mem, ProbabilisticTheory.NormedJordanAlgebra.exists_polynomial_approx_sqrt
statement: formalized
proof: formalized
---

# Uniqueness of the positive square root

The module `PhyslibAlpha.ProbabilisticTheory.JordanOrderUnit.JB.GeneratedByOne.SqrtUniqueness`, [PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/JB/GeneratedByOne/SqrtUniqueness.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/JB/GeneratedByOne/SqrtUniqueness.lean): 10 declarations, 10 with a docstring.

> A nonnegative square root of an observable equals its functional-calculus square root.

## i. Overview

> Every nonnegative `b` with `b ∘ b = a` is the square root of `a` from the functional calculus.
> Evaluating polynomials by Jordan multiplication does not depend on the subalgebra in which it is
> computed, so `p(a) = (p ∘ X²)(b)` for every polynomial `p`. Approximating the square root by
> polynomials on both sides gives `b = √a`.

## ii. Key results

> - `NormedJordanAlgebra.jordanPolyEval` : evaluating a polynomial by Jordan multiplication.
> - `NormedJordanAlgebra.jordanPolyEval_comp_sq` : `(p ∘ X²)(b) = p(b ∘ b)`.
> - `NormedJordanAlgebra.jordanSqrt_eq_of_nonneg_of_mul_self` : the positive square root is unique.

## iv. References

> * None.

## A. The ambient-independent polynomial evaluation

**`ProbabilisticTheory.NormedJordanAlgebra.jordanPolyEval`**, a def, [line 61](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/JB/GeneratedByOne/SqrtUniqueness.lean#L61).

> Evaluate a real polynomial at a Jordan element by repeated Jordan multiplication. Unlike
> `Polynomial.aeval (closedGenerator x) p`, this definition makes no reference to any particular
> closed one-generator algebra: it is visibly a function of `x` and `p` alone.

```lean
def jordanPolyEval (x : E) (p : Polynomial ℝ) : E
```

**`ProbabilisticTheory.NormedJordanAlgebra.aevalCoe_eq_jordanPolyEval`**, a lemma, [line 65](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/JB/GeneratedByOne/SqrtUniqueness.lean#L65).

> Evaluating a polynomial in any `C(u)` containing `x` gives its Jordan evaluation at `x`.

```lean
lemma aevalCoe_eq_jordanPolyEval {u : E} (x : ClosedGeneratedByOne u) (p : Polynomial ℝ) :
    (Polynomial.aeval x p : E) = jordanPolyEval (x : E) p
```

**`ProbabilisticTheory.NormedJordanAlgebra.jordanPolyEval_add`**, a lemma, [line 74](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/JB/GeneratedByOne/SqrtUniqueness.lean#L74).

> `jordanPolyEval` is additive in the polynomial argument.

```lean
lemma jordanPolyEval_add (x : E) (p q : Polynomial ℝ) :
    jordanPolyEval x (p + q) = jordanPolyEval x p + jordanPolyEval x q
```

**`ProbabilisticTheory.NormedJordanAlgebra.jordanPolyEval_comp_sq`**, a lemma, [line 85](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/JB/GeneratedByOne/SqrtUniqueness.lean#L85).

> The key algebraic identity behind square-root uniqueness: substituting `X ^ 2` before
> evaluating at `v` agrees with evaluating directly at `v * v`. This is a purely algebraic identity,
> with no order or norm hypothesis on `v`.

```lean
lemma jordanPolyEval_comp_sq (v : E) (p : Polynomial ℝ) :
    jordanPolyEval v (p.comp (Polynomial.X ^ 2)) = jordanPolyEval (v * v) p
```

## B. Approximation of the polynomial calculus

**`ProbabilisticTheory.NormedJordanAlgebra.jordanCfc_toContinuousMapOnAlgHom`**, a lemma, [line 110](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/JB/GeneratedByOne/SqrtUniqueness.lean#L110).

> `jordanCfc` applied to a polynomial function is exactly `jordanPolyEval` at the same
> polynomial. This connects the ambient-independent algebraic evaluation of §A to the intrinsic
> continuous functional calculus.

```lean
lemma jordanCfc_toContinuousMapOnAlgHom [Nontrivial E] (a : E) (p : Polynomial ℝ) :
    jordanCfc a (Polynomial.toContinuousMapOnAlgHom (jordanSpectrum a) p) = jordanPolyEval a p
```

**`ProbabilisticTheory.NormedJordanAlgebra.norm_jordanPolyEval_sub_jordanCfc_le`**, a lemma, [line 133](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/JB/GeneratedByOne/SqrtUniqueness.lean#L133).

> Norm bound transporting a uniform polynomial approximation of a continuous target function
> into a norm bound between `jordanPolyEval` and the intrinsic calculus.

```lean
lemma norm_jordanPolyEval_sub_jordanCfc_le [Nontrivial E]
    (a : E) (p : Polynomial ℝ) (F : C(jordanSpectrum a, ℝ)) {δ : ℝ} (hδ : 0 ≤ δ)
    (hbound : ∀ x : jordanSpectrum a, |p.eval (x : ℝ) - F x| ≤ δ) :
    ‖jordanPolyEval a p - jordanCfc a F‖ ≤ δ
```

## C. Uniform polynomial approximation of the square root

**`ProbabilisticTheory.NormedJordanAlgebra.exists_polynomialRepresentative_of_mem`**, a lemma, [line 153](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/JB/GeneratedByOne/SqrtUniqueness.lean#L153).

> Every polynomial function on a compact real interval `[0, M]` extends to a global real
> polynomial. This is the interval specialization of the general fact used for `jordanSpectrum`.

```lean
lemma exists_polynomialRepresentative_of_mem {s : Set ℝ} {g : C(s, ℝ)}
    (hg : g ∈ (polynomialFunctions s : Set C(s, ℝ))) :
    ∃ p : Polynomial ℝ, Polynomial.toContinuousMapOnAlgHom s p = g
```

**`ProbabilisticTheory.NormedJordanAlgebra.exists_polynomial_approx_sqrt`**, a lemma, [line 161](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/JB/GeneratedByOne/SqrtUniqueness.lean#L161).

> Classical uniform polynomial approximation of the real square root on a compact interval
> `[0, M]`. This is ordinary Stone--Weierstrass applied on a fixed real interval, entirely
> independent of any Jordan spectrum.

```lean
lemma exists_polynomial_approx_sqrt (M : ℝ) (ε : ℝ) (hε : 0 < ε) :
    ∃ p : Polynomial ℝ, ∀ s ∈ Set.Icc (0 : ℝ) M, |p.eval s - Real.sqrt s| < ε
```

## D. Unrestricted uniqueness of the positive square root

**`ProbabilisticTheory.NormedJordanAlgebra.jordanSqrt_eq_of_nonneg_of_mul_self`**, a lemma, [line 191](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/JB/GeneratedByOne/SqrtUniqueness.lean#L191).

> **The positive square root is unique**: every nonnegative `b` with `b ∘ b = a` is `√a`.

```lean
lemma jordanSqrt_eq_of_nonneg_of_mul_self [Nontrivial E]
    (a : E) (ha : 0 ≤ a) (b : E) (hb0 : 0 ≤ b) (hb : b * b = a) :
    b = jordanSqrt a ha
```

**`ProbabilisticTheory.NormedJordanAlgebra.eq_of_nonneg_of_mul_self_eq_mul_self`**, a lemma, [line 276](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/JB/GeneratedByOne/SqrtUniqueness.lean#L276).

> Uniqueness of the positive square root, restated as equality of two arbitrary nonnegative
> roots of the same element.

```lean
lemma eq_of_nonneg_of_mul_self_eq_mul_self [Nontrivial E]
    {a b c : E} (hb0 : 0 ≤ b) (hc0 : 0 ≤ c) (hb : b * b = a) (hc : c * c = a) : b = c
```

## Depends on

- [Continuous functional calculus in JB-algebras](jb-generatedbyone-cfc.md)

## Sources

- [PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/JB/GeneratedByOne/SqrtUniqueness.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/JB/GeneratedByOne/SqrtUniqueness.lean)
