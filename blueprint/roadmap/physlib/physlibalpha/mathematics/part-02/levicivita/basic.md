---
declaration: module
origin: cited
lean: cast_leviCivitaSymbol, sum_leviCivitaSymbol_mul_prod
statement: formalized
proof: formalized
---

# Contracting the Levi-Civita symbol against a matrix

The module `PhyslibAlpha.Mathematics.LeviCivita.Basic`, [PhyslibAlpha/Mathematics/LeviCivita/Basic.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/LeviCivita/Basic.lean): 2 declarations, 2 with a docstring; 1 private, not shown.

> The symbol is a tensor density of weight one.

## i. Overview

> Contracting the Levi-Civita symbol against the rows of a matrix `M` picked out by an index
> family `a` gives `det M` times the symbol of `a`. This is the statement that `ε` transforms as
> a tensor density of weight one, and it is what makes an `ε` contraction invariant under a
> determinant-one group.
>
> Both sides are the determinant of the matrix of those rows: on the left by expanding it along
> the Leibniz formula, on the right by the product rule, the row selection being the matrix of
> Kronecker deltas of `a`. The bridge to an arbitrary commutative ring is `cast_leviCivitaSymbol`,
> which carries the integer determinant of the delta matrix along the ring map from `ℤ`.

## ii. Key results

> - `cast_leviCivitaSymbol` : the symbol as a determinant over any commutative ring.
> - `sum_leviCivitaSymbol_mul_prod` : contracted against the rows of `M` selected by `a`, the
>   symbol gives `det M` times the symbol of `a`.

## iv. References

> * https://en.wikipedia.org/wiki/Levi-Civita\_symbol. [ref: wiki\_levi\_civita\_symbol]

## A. Contraction against a matrix

> Contracting the symbol against the rows of a matrix `M` picked out by `a` gives `det M` times
> the symbol of `a`. Both sides are the determinant of the matrix of those rows: on the left by
> expanding it along the Leibniz formula, on the right by the product rule, the row selection
> being the matrix of Kronecker deltas of `a`.

**`cast_leviCivitaSymbol`**, a lemma, [line 63](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/LeviCivita/Basic.lean#L63).

> The symbol as a determinant over any commutative ring, the integer determinant carried
> along the ring map from `ℤ`.

```lean
lemma cast_leviCivitaSymbol (g : ι → ι) :
    ((leviCivitaSymbol g : ℤ) : R)
      = (Matrix.of fun i j : ι => if g i = j then (1 : R) else 0).det
```

**`sum_leviCivitaSymbol_mul_prod`**, a lemma, [line 85](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/LeviCivita/Basic.lean#L85).

> Contracted against the rows of `M` selected by `a`, the symbol gives `det M` times the
> symbol of `a`.

```lean
lemma sum_leviCivitaSymbol_mul_prod (M : Matrix ι ι R) (a : ι → ι) :
    ∑ g : ι → ι, ((leviCivitaSymbol g : ℤ) : R) * ∏ i, M (a i) (g i)
      = M.det * ((leviCivitaSymbol a : ℤ) : R)
```

## Depends on

- [The Levi-Civita symbol in general dimension](../../../../physlib/mathematics/levicivita/basic.md)

## Sources

- [PhyslibAlpha/Mathematics/LeviCivita/Basic.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/LeviCivita/Basic.lean)
