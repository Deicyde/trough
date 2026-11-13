---
declaration: module
origin: cited
lean: PhyslibAlpha.Sl2.sum_arithmetic_progression, PhyslibAlpha.Sl2.clebsch_gordan_finrank_aux, PhyslibAlpha.Sl2.clebsch_gordan_finrank, PhyslibAlpha.Sl2.clebsch_gordan
statement: formalized
proof: formalized
---

# The Clebsch–Gordan dimension identity

The module `PhyslibAlpha.Mathematics.RepresentationTheory.Sl2.ClebschGordan`, [PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/ClebschGordan.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/ClebschGordan.lean): 4 declarations, 4 with a docstring.

> Computes the dimensions in the tensor-product decomposition of standard `sl₂` modules.

## i. Overview

> The product of the dimensions of two standard modules equals the sum of the dimensions
> expected in their Clebsch–Gordan decomposition. Finite-dimensional linear algebra then gives
> a nonempty type of vector-space equivalences. No equivariance or Clebsch–Gordan coefficients
> are established.

## ii. Key results

> - `clebsch_gordan_finrank` proves the dimension identity.
> - `clebsch_gordan` gives a vector-space equivalence by dimension counting.

## iv. References

> - Mathlib, `Mathlib.Algebra.Lie.Sl2`.

## A. Dimension counting

**`PhyslibAlpha.Sl2.sum_arithmetic_progression`**, a lemma, [line 50](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/ClebschGordan.lean#L50).

> The arithmetic progression underlying the Clebsch–Gordan dimension count.

```lean
lemma sum_arithmetic_progression (m d : ℕ) :
    ∑ k ∈ Finset.range (m + 1), (d + 2 * k + 1) = (m + 1) * (d + m + 1)
```

**`PhyslibAlpha.Sl2.clebsch_gordan_finrank_aux`**, a lemma, [line 61](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/ClebschGordan.lean#L61).

> Reindex the dimension sum when `m ≤ n`.

```lean
lemma clebsch_gordan_finrank_aux (m n : ℕ) (h : m ≤ n) :
    (m + 1) * (n + 1) = ∑ k ∈ Finset.range (m + 1), (m + n - 2 * k + 1)
```

**`PhyslibAlpha.Sl2.clebsch_gordan_finrank`**, a lemma, [line 79](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/ClebschGordan.lean#L79).

> Clebsch–Gordan decomposition, dimension form:
> the numerical shadow `(m+1)(n+1) = ∑_{k=0}^{min(m,n)} (m+n-2k+1)` of the module
> isomorphism `V(m) ⊗ V(n) ≅ ⊕_k V(m+n-2k)`.

```lean
lemma clebsch_gordan_finrank (m n : ℕ) :
    (m + 1) * (n + 1) = ∑ k ∈ Finset.range (min m n + 1), (m + n - 2 * k + 1)
```

**`PhyslibAlpha.Sl2.clebsch_gordan`**, a lemma, [line 92](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/ClebschGordan.lean#L92).

> Clebsch–Gordan decomposition, vector-space form:
> `V(m) ⊗ V(n)` is linearly isomorphic to `⊕_{k=0}^{min(m,n)} V(m+n-2k)`.
>
> The equivalence follows only from equal dimensions. It does not identify the diagonal
> `sl₂` action with the action on the direct sum or provide Clebsch–Gordan coefficients.

```lean
lemma clebsch_gordan (m n : ℕ) :
    Nonempty (StandardSl2Module K m ⊗[K] StandardSl2Module K n ≃ₗ[K]
      ⨁ _k : Fin (min m n + 1), StandardSl2Module K (m + n - 2 * (_k : ℕ)))
```

## Depends on

- [Explicit standard sl₂ modules](sl2-construction.md)

## Sources

- [PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/ClebschGordan.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/ClebschGordan.lean)
