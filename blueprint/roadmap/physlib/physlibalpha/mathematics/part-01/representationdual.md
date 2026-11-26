---
declaration: module
origin: cited
lean: Representation.dual_apply_dualBasis, LinearMap.range_eq_iSup_span_coord
statement: formalized
proof: formalized
---

# Dual representations on a dual basis

The module `PhyslibAlpha.Mathematics.RepresentationDual`, [PhyslibAlpha/Mathematics/RepresentationDual.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/RepresentationDual.lean): 2 declarations, 2 with a docstring.

> The dual of a representation on a dual basis, and the range of a linear map out of a dual space.

## i. Overview

> The dual of a representation acts on the dual basis by the transpose of the inverse. If
> `ρ g⁻¹` has matrix `M` in a basis, then `ρ.dual g` sends each dual basis vector to the
> combination given by the corresponding row of `M`.
>
> A linear map out of the dual of a finite-dimensional space is determined by its values on the
> coordinate functionals of a basis, so its range is the join of the lines through those values.

## ii. Key results

> - `Representation.dual_apply_dualBasis` : the dual representation on a dual basis.
> - `LinearMap.range_eq_iSup_span_coord` : the range of a map out of a dual space as a join of
>   lines.

## iv. References

> * None.

## A. The dual representation on a dual basis

**`Representation.dual_apply_dualBasis`**, a lemma, [line 53](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/RepresentationDual.lean#L53).

> The components of a dual representation on a dual basis: if `ρ g⁻¹` has
> matrix `M` in the basis `b` (columns indexing the argument), then `ρ.dual g`
> acts on the dual basis by the rows of `M`.

```lean
lemma dual_apply_dualBasis {k G V ι : Type*} [CommRing k]
    [Group G] [AddCommGroup V] [Module k V] [Fintype ι] [DecidableEq ι]
    (ρ : Representation k G V) (b : Module.Basis ι k V) (g : G) (i : ι)
    (M : Matrix ι ι k) (hM : ∀ j, ρ g⁻¹ (b j) = ∑ l, M l j • b l) :
    ρ.dual g (b.dualBasis i) = ∑ j, M i j • b.dualBasis j
```

## B. Maps out of a dual space

**`LinearMap.range_eq_iSup_span_coord`**, a lemma, [line 74](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/RepresentationDual.lean#L74).

> The range of a linear map out of the dual of a space with a finite basis is the join of the
> lines through its values on the coordinate functionals of the basis.

```lean
lemma range_eq_iSup_span_coord {k V M ι : Type*} [CommRing k] [AddCommGroup V] [Module k V]
    [AddCommGroup M] [Module k M] [Fintype ι] [DecidableEq ι]
    (b : Module.Basis ι k V) (f : Module.Dual k V →ₗ[k] M) :
    LinearMap.range f = ⨆ j, Submodule.span k {f (b.coord j)}
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [PhyslibAlpha/Mathematics/RepresentationDual.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/RepresentationDual.lean)
