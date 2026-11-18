---
declaration: module
origin: cited
lean: PhyslibAlpha.Sl2.finrank_standardSl2Module, PhyslibAlpha.Sl2.commuting_classification_finrank, PhyslibAlpha.Sl2.commuting_classification
statement: formalized
proof: formalized
---

# Classification for two commuting sl₂ actions

The module `PhyslibAlpha.Mathematics.RepresentationTheory.Sl2.CommutingActions`, [PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/CommutingActions.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/CommutingActions.lean): 3 declarations, 3 with a docstring.

> Uses the bivariate basis to obtain a tensor-product vector-space description.

## i. Overview

> For two commuting `sl₂` triples acting jointly irreducibly, the bivariate ladder basis
> gives a linear equivalence with a tensor product of standard modules and a corresponding
> dimension formula. The equivalence is only one of vector spaces; it does not assert that the
> actions intertwine.

## ii. Key results

> - `commuting_classification` gives the vector-space equivalence.
> - `commuting_classification_finrank` gives the dimension formula.

## iv. References

> - Mathlib, `Mathlib.Algebra.Lie.Sl2`.

## A. Two commuting actions

**`PhyslibAlpha.Sl2.finrank_standardSl2Module`**, a lemma, [line 51](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/CommutingActions.lean#L51).

> The standard module `V(k)` has dimension `k + 1`.

```lean
lemma finrank_standardSl2Module (k : ℕ) : Module.finrank K (StandardSl2Module K k) = k + 1
```

**`PhyslibAlpha.Sl2.commuting_classification_finrank`**, a lemma, [line 67](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/CommutingActions.lean#L67).

> Dimension consequence of `commuting_classification`: `finrank K V = (m+1)(n+1)`.

```lean
lemma commuting_classification_finrank :
    ∃ m n : ℕ, Module.finrank K V = (m + 1) * (n + 1)
```

**`PhyslibAlpha.Sl2.commuting_classification`**, a lemma, [line 82](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/CommutingActions.lean#L82).

> Classification of jointly irreducible commuting `sl₂`-actions.
> Two `sl₂`-triples of operators on a
> finite-dimensional space `V`, commuting with each other and with no proper
> subspace invariant under both, force `V` to be linearly isomorphic to a tensor
> product `V(m) ⊗ V(n)` of standard modules.
>
> The equivalence is obtained from a dimension count. An equivalence intertwining the two
> actions remains to be constructed.

```lean
lemma commuting_classification :
    ∃ m n : ℕ, Nonempty (V ≃ₗ[K] StandardSl2Module K m ⊗[K] StandardSl2Module K n)
```

## Depends on

- [A basis for two commuting sl₂ actions](sl2-bivariatebasis.md)

## Sources

- [PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/CommutingActions.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/CommutingActions.lean)
