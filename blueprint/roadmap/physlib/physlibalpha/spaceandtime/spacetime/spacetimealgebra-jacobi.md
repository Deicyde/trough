---
declaration: module
origin: cited
lean: SpaceTimeAlgebra.pderiv_finset_prod, SpaceTimeAlgebra.jacobi
statement: formalized
proof: formalized
---

# Jacobi's formula for matrices of jets

The module `PhyslibAlpha.SpaceAndTime.SpaceTime.SpaceTimeAlgebra.Jacobi`, [PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeAlgebra/Jacobi.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeAlgebra/Jacobi.lean): 2 declarations, 2 with a docstring.

## i. Overview

> Jacobi's formula `∂ det M = tr (∂M · adj M)` for a square matrix of jets, in the generality
> needed by the jets of any special unitary group: it is what makes the Maurer–Cartan form
> `i (∂U) U⁻¹` of an `SU(n)` jet traceless, since `det U = 1` and `U⁻¹ = adj U`.

## ii. Key results

> - `SpaceTimeAlgebra.pderiv_finset_prod` : the Leibniz rule for a finite product.
> - `SpaceTimeAlgebra.jacobi` : Jacobi's formula.

## iv. References

> * None.

## A. The Leibniz rule for a finite product

**`SpaceTimeAlgebra.pderiv_finset_prod`**, a lemma, [line 49](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeAlgebra/Jacobi.lean#L49).

> The Leibniz rule for a finite product.

```lean
lemma pderiv_finset_prod {ι : Type*} [DecidableEq ι] (μ : Fin 1 ⊕ Fin 3) (s : Finset ι)
    (f : ι → SpaceTimeAlgebra) :
    pderiv μ (∏ i ∈ s, f i) = ∑ i ∈ s, (∏ j ∈ s.erase i, f j) * pderiv μ (f i)
```

## B. Jacobi's formula

**`SpaceTimeAlgebra.jacobi`**, a lemma, [line 71](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeAlgebra/Jacobi.lean#L71).

> **Jacobi's formula**: the derivative of a determinant is the trace of the derivative
> against the adjugate.

```lean
lemma jacobi {κ : Type} [Fintype κ] [DecidableEq κ] (M : Matrix κ κ SpaceTimeAlgebra)
    (μ : Fin 1 ⊕ Fin 3) :
    pderiv μ M.det = (M.map (pderiv μ) * M.adjugate).trace
```

## Depends on

- [The spacetime algebra](../../../physlib/spaceandtime/spacetime/spacetimealgebra-basic.md)

## Sources

- [PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeAlgebra/Jacobi.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/SpaceAndTime/SpaceTime/SpaceTimeAlgebra/Jacobi.lean)
