---
declaration: module
origin: cited
lean: Physlib.MultiIndex, Physlib.MultiIndex.order, Physlib.MultiIndex.increment, Physlib.MultiIndex.ext, Physlib.MultiIndex.zero_apply, Physlib.MultiIndex.add_apply, Physlib.MultiIndex.increment_apply_same, Physlib.MultiIndex.increment_apply_ne
statement: formalized
proof: formalized
---

# Multi-indices

The module `Physlib.SpaceAndTime.Space.Derivatives.MultiIndex`, [Physlib/SpaceAndTime/Space/Derivatives/MultiIndex.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Derivatives/MultiIndex.lean): 24 declarations (3 instances with no name), 5 with a docstring.

## i. Overview

> This module defines the basic type of multi-indices used to index iterated partial derivatives.
>
> A multi-index on `d` source coordinates is represented as a structure with an underlying function
> `Fin d → ℕ`, together with the first basic operations needed later in the local Classical Field
> Theory development.

## ii. Key results

> - `Physlib.MultiIndex` : multi-indices on `d` coordinates.
> - `MultiIndex.order` : the order `|I|` of a multi-index.
> - `MultiIndex.increment` : increment a single coordinate of a multi-index.
> - `MultiIndex.toList` : the canonical ordered list of directions encoded by a multi-index.

## iv. References

> * None.

## A. The basic type of multi-indices

**`Physlib.MultiIndex`**, a structure, [line 53](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Derivatives/MultiIndex.lean#L53).

> A multi-index on `d` source coordinates.

```lean
structure MultiIndex (d : ℕ) where
  /-- The coordinates of the multi-index. -/
  toFun : Fin d → ℕ
deriving DecidableEq
```

**An instance with no name**, [line 62](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Derivatives/MultiIndex.lean#L62).

```lean
instance : CoeFun (MultiIndex d) (fun _ => Fin d → ℕ)
```

**An instance with no name**, [line 64](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Derivatives/MultiIndex.lean#L64).

```lean
instance : Zero (MultiIndex d)
```

**An instance with no name**, [line 66](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Derivatives/MultiIndex.lean#L66).

```lean
instance : Add (MultiIndex d)
```

### A.1. Basic operations

**`Physlib.MultiIndex.order`**, a def, [line 74](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Derivatives/MultiIndex.lean#L74).

> The order `|I|` of a multi-index `I`, defined as the sum of its components.

```lean
def order (I : MultiIndex d) : Nat
```

**`Physlib.MultiIndex.increment`**, a def, [line 77](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Derivatives/MultiIndex.lean#L77).

> Increment the `i`-th coordinate of a multi-index by one.

```lean
def increment (I : MultiIndex d) (i : Fin d) : MultiIndex d
```

### A.2. Basic lemmas

**`Physlib.MultiIndex.ext`**, a lemma, [line 85](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Derivatives/MultiIndex.lean#L85).

```lean
lemma ext {I J : MultiIndex d} (h : ∀ i, I i = J i) : I = J
```

**`Physlib.MultiIndex.zero_apply`**, a lemma, [line 94](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Derivatives/MultiIndex.lean#L94).

```lean
lemma zero_apply (i : Fin d) : (0 : MultiIndex d) i = 0
```

**`Physlib.MultiIndex.add_apply`**, a lemma, [line 97](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Derivatives/MultiIndex.lean#L97).

```lean
lemma add_apply (I J : MultiIndex d) (i : Fin d) : (I + J) i = I i + J i
```

**`Physlib.MultiIndex.increment_apply_same`**, a lemma, [line 100](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Derivatives/MultiIndex.lean#L100).

```lean
lemma increment_apply_same (I : MultiIndex d) (i : Fin d) :
    increment I i i = I i + 1
```

**`Physlib.MultiIndex.increment_apply_ne`**, a lemma, [line 105](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Derivatives/MultiIndex.lean#L105).

```lean
lemma increment_apply_ne (I : MultiIndex d) {i j : Fin d} (h : j ≠ i) :
    increment I i j = I j
```

**`Physlib.MultiIndex.order_zero`**, a lemma, [line 110](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Derivatives/MultiIndex.lean#L110).

```lean
lemma order_zero : order (0 : MultiIndex d) = 0
```

**`Physlib.MultiIndex.order_add`**, a lemma, [line 113](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Derivatives/MultiIndex.lean#L113).

```lean
lemma order_add (I J : MultiIndex d) : order (I + J) = order I + order J
```

**`Physlib.MultiIndex.order_single`**, a lemma, [line 117](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Derivatives/MultiIndex.lean#L117).

```lean
lemma order_single (i : Fin d) : order (⟨Pi.single i 1⟩ : MultiIndex d) = 1
```

**`Physlib.MultiIndex.order_increment`**, a lemma, [line 128](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Derivatives/MultiIndex.lean#L128).

```lean
lemma order_increment (I : MultiIndex d) (i : Fin d) :
    order (increment I i) = order I + 1
```

### A.3. Canonical ordered lists of directions

**`Physlib.MultiIndex.tail`**, a def, [line 138](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Derivatives/MultiIndex.lean#L138).

> The tail of a multi-index on `d + 1` coordinates, dropping the `0`-th coordinate.

```lean
def tail (I : MultiIndex d.succ) : MultiIndex d
```

**`Physlib.MultiIndex.toList`**, a def, [line 141](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Derivatives/MultiIndex.lean#L141).

> The canonical ordered list of coordinate directions encoded by a multi-index.

```lean
def toList : {d : ℕ} → MultiIndex d → List (Fin d)
```

**`Physlib.MultiIndex.tail_zero`**, a lemma, [line 146](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Derivatives/MultiIndex.lean#L146).

```lean
lemma tail_zero : tail (0 : MultiIndex d.succ) = 0
```

**`Physlib.MultiIndex.tail_increment_zero`**, a lemma, [line 151](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Derivatives/MultiIndex.lean#L151).

```lean
lemma tail_increment_zero (I : MultiIndex d.succ) : tail (increment I 0) = tail I
```

**`Physlib.MultiIndex.tail_increment_succ`**, a lemma, [line 156](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Derivatives/MultiIndex.lean#L156).

```lean
lemma tail_increment_succ (I : MultiIndex d.succ) (i : Fin d) :
    tail (increment I i.succ) = increment (tail I) i
```

**`Physlib.MultiIndex.toList_zero`**, a lemma, [line 165](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Derivatives/MultiIndex.lean#L165).

```lean
lemma toList_zero : toList (0 : MultiIndex d) = []
```

**`Physlib.MultiIndex.length_toList`**, a lemma, [line 171](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Derivatives/MultiIndex.lean#L171).

```lean
lemma length_toList (I : MultiIndex d) : I.toList.length = I.order
```

**`Physlib.MultiIndex.toList_increment_zero`**, a lemma, [line 179](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Derivatives/MultiIndex.lean#L179).

```lean
lemma toList_increment_zero (I : MultiIndex d.succ) :
    toList (increment I 0) = 0 :: toList I
```

**`Physlib.MultiIndex.toList_single`**, a lemma, [line 186](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Derivatives/MultiIndex.lean#L186).

```lean
lemma toList_single (i : Fin d) : toList (increment 0 i : MultiIndex d) = [i]
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [Physlib/SpaceAndTime/Space/Derivatives/MultiIndex.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Derivatives/MultiIndex.lean)
