---
declaration: module
origin: cited
lean: Physlib.DerivativeIndex, Physlib.DerivativeIndex.coe_zero, Physlib.DerivativeIndex.zero_apply
statement: formalized
proof: formalized
---

# Bounded derivative indices

The module `Physlib.SpaceAndTime.Space.Derivatives.DerivativeIndex`, [Physlib/SpaceAndTime/Space/Derivatives/DerivativeIndex.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Derivatives/DerivativeIndex.lean): 6 declarations (3 instances with no name), 1 with a docstring.

## i. Overview

> This module defines bounded derivative indices on `Space d`, i.e. multi-indices of total order at
> most `k`.
>
> These are the finite indexing objects used later for finite-order local jet coordinates, while
> remaining independent of any specific jet or field-theory construction.

## ii. Key results

> - `Physlib.DerivativeIndex`

## iv. References

> * None.

## A. Definition and basic instances

**`Physlib.DerivativeIndex`**, an abbrev, [line 44](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Derivatives/DerivativeIndex.lean#L44).

> The multi-indices on `d` coordinates of order at most `k`.

```lean
abbrev DerivativeIndex (d k : ℕ)
```

**An instance with no name**, [line 46](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Derivatives/DerivativeIndex.lean#L46).

```lean
noncomputable instance (d k : ℕ) : Fintype (DerivativeIndex d k)
```

**An instance with no name**, [line 64](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Derivatives/DerivativeIndex.lean#L64).

```lean
instance (d k : ℕ) : DecidableEq (DerivativeIndex d k)
```

**An instance with no name**, [line 66](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Derivatives/DerivativeIndex.lean#L66).

```lean
instance (d k : ℕ) : Zero (DerivativeIndex d k)
```

**`Physlib.DerivativeIndex.coe_zero`**, a lemma, [line 72](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Derivatives/DerivativeIndex.lean#L72).

```lean
lemma coe_zero (d k : ℕ) :
    ((0 : DerivativeIndex d k) : MultiIndex d) = 0
```

**`Physlib.DerivativeIndex.zero_apply`**, a lemma, [line 76](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Derivatives/DerivativeIndex.lean#L76).

```lean
lemma zero_apply (d k : ℕ) (i : Fin d) :
    ((0 : DerivativeIndex d k) : MultiIndex d) i = 0
```

## Depends on

- [Multi-indices](../part-02/derivatives-multiindex.md)

## Sources

- [Physlib/SpaceAndTime/Space/Derivatives/DerivativeIndex.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Derivatives/DerivativeIndex.lean)
