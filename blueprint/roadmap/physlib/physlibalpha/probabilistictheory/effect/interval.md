---
declaration: module
origin: cited
lean: PhyslibAlpha.ProbabilisticTheory.Effect, PhyslibAlpha.ProbabilisticTheory.Effect.mem_iff_mem_posCone_and_one_sub_mem_posCone, PhyslibAlpha.ProbabilisticTheory.Effect.instZero, PhyslibAlpha.ProbabilisticTheory.Effect.instOne, PhyslibAlpha.ProbabilisticTheory.Effect.instNonempty, PhyslibAlpha.ProbabilisticTheory.Effect.coe_zero, PhyslibAlpha.ProbabilisticTheory.Effect.coe_one, PhyslibAlpha.ProbabilisticTheory.Effect.exists_pos_smul_mem
statement: formalized
proof: formalized
---

# Effects (PhyslibAlpha)

The module `PhyslibAlpha.ProbabilisticTheory.Effect.Interval`, [PhyslibAlpha/ProbabilisticTheory/Effect/Interval.lean](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ProbabilisticTheory/Effect/Interval.lean): 8 declarations, 3 with a docstring.

## i. Overview

> An effect models a yes/no measurement outcome, ranging continuously between the impossible
> outcome `0` and the certain outcome `1`. Formally, it is a point of the order interval `[0, 1]`
> inside `E`. For self-adjoint matrices, effects are exactly the operators `0 ≤ M ≤ 1` — the
> elements of a POVM.

## ii. Key results

> - `Effect` : a bounded measurement outcome, the order interval `[0, 1]`.
> - `Effect.mem_iff_mem_posCone_and_one_sub_mem_posCone` : an effect is exactly a positive element
>   whose complement from the order unit is also positive.
> - `Effect.exists_pos_smul_mem` : every positive observable becomes an effect after scaling it down
>   enough.

## iv. References

> - G. Ludwig, *Foundations of Quantum Mechanics I*, Springer, 1983.
>   <https://link.springer.com/book/10.1007/978-3-642-86751-4>

## A. Effects

**`PhyslibAlpha.ProbabilisticTheory.Effect`**, an abbrev, [line 51](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ProbabilisticTheory/Effect/Interval.lean#L51).

> A bounded measurement outcome.

```lean
abbrev Effect (E : Type*) [PartialOrder E] [One E] [Zero E]
```

**`PhyslibAlpha.ProbabilisticTheory.Effect.mem_iff_mem_posCone_and_one_sub_mem_posCone`**, a lemma, [line 60](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ProbabilisticTheory/Effect/Interval.lean#L60).

> An effect is a positive element whose complement from the order unit is positive.

```lean
lemma mem_iff_mem_posCone_and_one_sub_mem_posCone {A : E} :
    A ∈ Effect E ↔ A ∈ PosCone E ∧ 1 - A ∈ PosCone E
```

**`PhyslibAlpha.ProbabilisticTheory.Effect.instZero`**, an instance, [line 70](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ProbabilisticTheory/Effect/Interval.lean#L70).

```lean
instance instZero : Zero (Effect E)
```

**`PhyslibAlpha.ProbabilisticTheory.Effect.instOne`**, an instance, [line 72](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ProbabilisticTheory/Effect/Interval.lean#L72).

```lean
instance instOne : One (Effect E)
```

**`PhyslibAlpha.ProbabilisticTheory.Effect.instNonempty`**, an instance, [line 74](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ProbabilisticTheory/Effect/Interval.lean#L74).

```lean
instance instNonempty : Nonempty (Effect E)
```

**`PhyslibAlpha.ProbabilisticTheory.Effect.coe_zero`**, a lemma, [line 76](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ProbabilisticTheory/Effect/Interval.lean#L76).

```lean
lemma coe_zero : ((0 : Effect E) : E) = 0
```

**`PhyslibAlpha.ProbabilisticTheory.Effect.coe_one`**, a lemma, [line 78](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ProbabilisticTheory/Effect/Interval.lean#L78).

```lean
lemma coe_one : ((1 : Effect E) : E) = 1
```

**`PhyslibAlpha.ProbabilisticTheory.Effect.exists_pos_smul_mem`**, a lemma, [line 82](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ProbabilisticTheory/Effect/Interval.lean#L82).

> Every nonnegative observable becomes an effect after scaling it down by a large enough
> positive real: the effect interval reaches in every direction the positive cone does.

```lean
lemma exists_pos_smul_mem {B : E} (hB : 0 ≤ B) :
    ∃ r : ℝ, 0 < r ∧ r • B ∈ Effect E
```

## Depends on

- [Ordered positive cones (PhyslibAlpha)](../orderunit/cone.md)

## Sources

- [PhyslibAlpha/ProbabilisticTheory/Effect/Interval.lean at 8c87bdfb](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ProbabilisticTheory/Effect/Interval.lean)
