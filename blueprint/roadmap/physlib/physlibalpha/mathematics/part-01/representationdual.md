---
declaration: module
origin: cited
lean: Representation.dual_apply_dualBasis
statement: formalized
proof: formalized
---

# Dual representations on a dual basis

The module `PhyslibAlpha.Mathematics.RepresentationDual`, [PhyslibAlpha/Mathematics/RepresentationDual.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationDual.lean): 1 declaration, 1 with a docstring.

## i. Overview

> The dual of a representation acts on the dual basis by the transpose of the inverse: if
> `ρ g⁻¹` has matrix `M` in a basis, then `ρ.dual g` sends each dual basis vector to the
> combination given by the corresponding row of `M`.

## ii. Key results

> - `Representation.dual_apply_dualBasis` : the dual representation on a dual basis.

## iv. References

> * None.

## A. The dual representation on a dual basis

**`Representation.dual_apply_dualBasis`**, a lemma, [line 45](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationDual.lean#L45).

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

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [PhyslibAlpha/Mathematics/RepresentationDual.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationDual.lean)
