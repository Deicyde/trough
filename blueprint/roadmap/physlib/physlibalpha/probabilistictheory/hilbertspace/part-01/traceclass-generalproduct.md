---
declaration: module
origin: cited
lean: ProbabilisticTheory.diagonal_star_mul_eq_inner, ProbabilisticTheory.isTraceClass_mul_of_isHilbertSchmidt, ProbabilisticTheory.isHilbertSchmidt_polarFactor_mul_sqrt_abs_and_sqrt_abs, ProbabilisticTheory.isTraceClass_add, ProbabilisticTheory.isTraceClass_mul_mul, ProbabilisticTheory.isTraceClass_star
statement: formalized
proof: formalized
---

# Products of Hilbert–Schmidt operators

The module `PhyslibAlpha.ProbabilisticTheory.HilbertSpace.TraceClass.GeneralProduct`, [PhyslibAlpha/ProbabilisticTheory/HilbertSpace/TraceClass/GeneralProduct.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/TraceClass/GeneralProduct.lean): 6 declarations, 6 with a docstring.

> Products of Hilbert–Schmidt operators are trace class; trace class is a ⋆-closed ideal.

## i. Overview

> A product of two Hilbert–Schmidt operators is trace class. Every trace-class operator `T` factors as
> `(U √|T|) √|T|` with both factors Hilbert–Schmidt, so trace-class operators form a two-sided ideal
> closed under sums and adjoints.

## ii. Key results

> - `isTraceClass_mul_of_isHilbertSchmidt` : a product of two Hilbert–Schmidt operators is trace
>   class.
> - `isTraceClass_add` : trace-class operators are closed under addition.
> - `isTraceClass_mul_mul` : trace-class operators form a two-sided ideal.
> - `isTraceClass_star` : trace-class operators are closed under the adjoint.

## iv. References

> * None.

## A. Products of Hilbert–Schmidt operators

**`ProbabilisticTheory.diagonal_star_mul_eq_inner`**, a lemma, [line 61](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/TraceClass/GeneralProduct.lean#L61).

> The diagonal of `star W * (R * S)` (for any contraction `W`) unwinds to a Hilbert–Schmidt
> Cauchy–Schwarz pairing. This is the pointwise identity feeding both the master product theorem and
> the general additive/ideal closure results below.

```lean
lemma diagonal_star_mul_eq_inner {R S W : H →L[ℂ] H} {w : Set H} (b : HilbertBasis w ℂ H)
    (i : w) :
    ⟪b i, (star W * (R * S)) (b i)⟫_ℂ = ⟪(ContinuousLinearMap.adjoint R * W) (b i), S (b i)⟫_ℂ
```

**`ProbabilisticTheory.isTraceClass_mul_of_isHilbertSchmidt`**, a lemma, [line 71](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/TraceClass/GeneralProduct.lean#L71).

> **A product of two Hilbert–Schmidt operators is trace class.**

```lean
lemma isTraceClass_mul_of_isHilbertSchmidt {R S : H →L[ℂ] H}
    (hR : IsHilbertSchmidt R) (hS : IsHilbertSchmidt S) : IsTraceClass (R * S)
```

**`ProbabilisticTheory.isHilbertSchmidt_polarFactor_mul_sqrt_abs_and_sqrt_abs`**, a lemma, [line 106](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/TraceClass/GeneralProduct.lean#L106).

> Every trace-class operator factors as a product of two Hilbert–Schmidt operators: the polar
> factor composed with the Hilbert–Schmidt square root of `|T|`, and that same square root again.

```lean
lemma isHilbertSchmidt_polarFactor_mul_sqrt_abs_and_sqrt_abs {T : H →L[ℂ] H}
    (hT : IsTraceClass T) :
    IsHilbertSchmidt (Polar.polarFactor T * CFC.sqrt (CFC.abs T)) ∧
      IsHilbertSchmidt (CFC.sqrt (CFC.abs T)) ∧
      Polar.polarFactor T * CFC.sqrt (CFC.abs T) * CFC.sqrt (CFC.abs T) = T
```

## B. Closure properties of trace class

**`ProbabilisticTheory.isTraceClass_add`**, a lemma, [line 125](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/TraceClass/GeneralProduct.lean#L125).

> Trace-class operators are closed under addition.

```lean
lemma isTraceClass_add {T T' : H →L[ℂ] H} (hT : IsTraceClass T) (hT' : IsTraceClass T') :
    IsTraceClass (T + T')
```

**`ProbabilisticTheory.isTraceClass_mul_mul`**, a lemma, [line 186](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/TraceClass/GeneralProduct.lean#L186).

> **Trace-class operators form a two-sided ideal**: `A T B` is trace class for trace-class `T` and
> bounded `A`, `B`.

```lean
lemma isTraceClass_mul_mul {A B T : H →L[ℂ] H} (hT : IsTraceClass T) :
    IsTraceClass (A * T * B)
```

**`ProbabilisticTheory.isTraceClass_star`**, a lemma, [line 201](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/TraceClass/GeneralProduct.lean#L201).

> Taking the adjoint preserves trace class.

```lean
lemma isTraceClass_star {T : H →L[ℂ] H} (hT : IsTraceClass T) : IsTraceClass (star T)
```

## Depends on

- [Hilbert–Schmidt operators](traceclass-hilbertschmidt.md)
- [Polar decomposition of bounded operators](traceclass-polar.md)

## Proof depends on

- [Basis independence of the trace](traceclass-generalideal.md)

## Sources

- [PhyslibAlpha/ProbabilisticTheory/HilbertSpace/TraceClass/GeneralProduct.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/TraceClass/GeneralProduct.lean)
