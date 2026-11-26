---
declaration: module
origin: cited
lean: ProbabilisticTheory.Effect.IsSharp, ProbabilisticTheory.Effect.isSharp_zero, ProbabilisticTheory.Effect.isSharp_complement, ProbabilisticTheory.Effect.isSharp_complement_iff, ProbabilisticTheory.Effect.isSharp_one
statement: formalized
proof: formalized
---

# Sharp effects (Physlib)

The module `Physlib.ProbabilisticTheory.Effect.Sharp`, [Physlib/ProbabilisticTheory/Effect/Sharp.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/ProbabilisticTheory/Effect/Sharp.lean): 5 declarations, 5 with a docstring.

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

**`ProbabilisticTheory.Effect.IsSharp`**, a def, [line 52](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/ProbabilisticTheory/Effect/Sharp.lean#L52).

> An effect is sharp when it is an extreme point of the effect interval: it cannot be written as
> a nontrivial mixture of two distinct effects.

```lean
def IsSharp (e : P.Effect) : Prop
```

**`ProbabilisticTheory.Effect.isSharp_zero`**, a lemma, [line 55](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/ProbabilisticTheory/Effect/Sharp.lean#L55).

> The impossible outcome 0 is sharp.

```lean
lemma isSharp_zero : IsSharp (0 : P.Effect)
```

**`ProbabilisticTheory.Effect.isSharp_complement`**, a lemma, [line 63](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/ProbabilisticTheory/Effect/Sharp.lean#L63).

> Sharpness is preserved by taking the complement:
> `e ↦ 1 - e` is an affine involution of the effect interval.

```lean
lemma isSharp_complement {e : P.Effect} (h : IsSharp e) : IsSharp (complement e)
```

**`ProbabilisticTheory.Effect.isSharp_complement_iff`**, a lemma, [line 72](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/ProbabilisticTheory/Effect/Sharp.lean#L72).

> Sharpness is preserved by taking the complement, in either direction.

```lean
lemma isSharp_complement_iff {e : P.Effect} : IsSharp (complement e) ↔ IsSharp e
```

**`ProbabilisticTheory.Effect.isSharp_one`**, a lemma, [line 76](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/ProbabilisticTheory/Effect/Sharp.lean#L76).

> The certain outcome 1 is sharp.

```lean
lemma isSharp_one : IsSharp (1 : P.Effect)
```

## Depends on

- [Complementary effects (Physlib)](complement.md)

## Sources

- [Physlib/ProbabilisticTheory/Effect/Sharp.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/ProbabilisticTheory/Effect/Sharp.lean)
