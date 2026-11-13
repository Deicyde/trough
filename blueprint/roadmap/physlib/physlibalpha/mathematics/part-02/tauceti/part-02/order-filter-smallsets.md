---
declaration: module
origin: cited
lean: TauCeti.comap_val_smallSets_neBot
statement: formalized
proof: formalized
---

# Indexing a net by the members of a filter

The module `PhyslibAlpha.Mathematics.TauCeti.Order.Filter.SmallSets`, [PhyslibAlpha/Mathematics/TauCeti/Order/Filter/SmallSets.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Order/Filter/SmallSets.lean): 1 declaration, 1 with a docstring.

> A family indexed by the members of a filter `l` — a net of the shape `k : {s : Set α // s ∈ l} → β`
> — is naturally taken along `Filter.comap Subtype.val l.smallSets`, for which `∀ᶠ s in _, p s` says
> that `p` holds for every small enough member of `l`.

## i. Overview

> A family indexed by the members of a filter `l` — a net of the shape `k : {s : Set α // s ∈ l} → β`
> — is naturally taken along `Filter.comap Subtype.val l.smallSets`, for which `∀ᶠ s in _, p s` says
> that `p` holds for every small enough member of `l`. This file records that this index filter is
> never the bottom filter, so that convergence along it has content.

## ii. Key results

> This file proves the statement described in the overview.

## iv. References

> * Standard material; the statements and proofs are original to this formalization.

## A. Development

**`TauCeti.comap_val_smallSets_neBot`**, a lemma, [line 49](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Order/Filter/SmallSets.lean#L49).

> **A filter indexes a nontrivial net by its own members.** A net indexed by the members of a
> filter `l` converges along this filter, the members read through `Filter.smallSets`, so that
> `∀ᶠ s in _, p s` says that `p` holds for every small enough member of `l`; it is not the bottom
> filter, every member of `l` being an index below itself.

```lean
lemma comap_val_smallSets_neBot {α : Type*} (l : Filter α) :
    NeBot (comap (Subtype.val : {s : Set α // s ∈ l} → Set α) l.smallSets)
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [PhyslibAlpha/Mathematics/TauCeti/Order/Filter/SmallSets.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/TauCeti/Order/Filter/SmallSets.lean)
