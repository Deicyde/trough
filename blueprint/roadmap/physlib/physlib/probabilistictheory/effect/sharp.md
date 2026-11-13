---
declaration: module
origin: cited
lean: ProbabilisticTheory.Effect.IsSharp, ProbabilisticTheory.Effect.isSharp_zero, ProbabilisticTheory.Effect.isSharp_complement, ProbabilisticTheory.Effect.isSharp_complement_iff, ProbabilisticTheory.Effect.isSharp_one
statement: formalized
proof: formalized
---

# Sharp effects

The module `Physlib.ProbabilisticTheory.Effect.Sharp`, [Physlib/ProbabilisticTheory/Effect/Sharp.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/Effect/Sharp.lean): 5 declarations, 5 with a docstring.

> Sharp effects: extreme points of the effect interval, preserved by taking complements.

## i. Overview

> The effect interval `[0, 1]` is convex. A sharp effect is an extreme point of it: one that cannot
> be written as a nontrivial mixture of two distinct effects. Sharp effects generalize projections.

## ii. Key results

> - `Effect.IsSharp` : an effect that cannot be written as a nontrivial mixture of two distinct
>   effects.
> - `Effect.isSharp_complement_iff` : sharpness is preserved by taking the complement.

## iv. References

> * None.

## A. Sharp effects

**`ProbabilisticTheory.Effect.IsSharp`**, a def, [line 54](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/Effect/Sharp.lean#L54).

> An effect is sharp when it is an extreme point of the effect interval: it cannot be written as
> a nontrivial mixture of two distinct effects.

```lean
def IsSharp (e : Effect E) : Prop
```

**`ProbabilisticTheory.Effect.isSharp_zero`**, a lemma, [line 57](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/Effect/Sharp.lean#L57).

> The impossible outcome 0 is sharp.

```lean
lemma isSharp_zero : IsSharp (0 : Effect E)
```

**`ProbabilisticTheory.Effect.isSharp_complement`**, a lemma, [line 65](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/Effect/Sharp.lean#L65).

> Sharpness is preserved by taking the complement:
> `e ↦ 1 - e` is an affine involution of the effect interval.

```lean
lemma isSharp_complement {e : Effect E} (h : IsSharp e) : IsSharp (complement e)
```

**`ProbabilisticTheory.Effect.isSharp_complement_iff`**, a lemma, [line 74](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/Effect/Sharp.lean#L74).

> Sharpness is preserved by taking the complement, in either direction.

```lean
lemma isSharp_complement_iff {e : Effect E} : IsSharp (complement e) ↔ IsSharp e
```

**`ProbabilisticTheory.Effect.isSharp_one`**, a lemma, [line 78](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/Effect/Sharp.lean#L78).

> The certain outcome 1 is sharp.

```lean
lemma isSharp_one : IsSharp (1 : Effect E)
```

## Depends on

- [Complementary effects](complement.md)

## Sources

- [Physlib/ProbabilisticTheory/Effect/Sharp.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/Effect/Sharp.lean)
