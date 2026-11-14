---
declaration: module
origin: cited
lean: ProbabilisticTheory.Effect, ProbabilisticTheory.Effect.mem_iff_mem_posCone_and_one_sub_mem_posCone, ProbabilisticTheory.Effect.instZero, ProbabilisticTheory.Effect.instOne, ProbabilisticTheory.Effect.instNonempty, ProbabilisticTheory.Effect.coe_zero, ProbabilisticTheory.Effect.coe_one, ProbabilisticTheory.Effect.exists_pos_smul_mem
statement: formalized
proof: formalized
---

# Effects

The module `Physlib.ProbabilisticTheory.Effect.Basic`, [Physlib/ProbabilisticTheory/Effect/Basic.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/Effect/Basic.lean): 8 declarations, 3 with a docstring.

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

**`ProbabilisticTheory.Effect`**, an abbrev, [line 51](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/Effect/Basic.lean#L51).

> A bounded measurement outcome.

```lean
abbrev Effect (E : Type*) [PartialOrder E] [One E] [Zero E]
```

**`ProbabilisticTheory.Effect.mem_iff_mem_posCone_and_one_sub_mem_posCone`**, a lemma, [line 60](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/Effect/Basic.lean#L60).

> An effect is a positive element whose complement from the order unit is positive.

```lean
lemma mem_iff_mem_posCone_and_one_sub_mem_posCone {A : E} :
    A ∈ Effect E ↔ A ∈ PosCone E ∧ 1 - A ∈ PosCone E
```

**`ProbabilisticTheory.Effect.instZero`**, an instance, [line 70](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/Effect/Basic.lean#L70).

```lean
instance instZero : Zero (Effect E)
```

**`ProbabilisticTheory.Effect.instOne`**, an instance, [line 72](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/Effect/Basic.lean#L72).

```lean
instance instOne : One (Effect E)
```

**`ProbabilisticTheory.Effect.instNonempty`**, an instance, [line 74](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/Effect/Basic.lean#L74).

```lean
instance instNonempty : Nonempty (Effect E)
```

**`ProbabilisticTheory.Effect.coe_zero`**, a lemma, [line 76](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/Effect/Basic.lean#L76).

```lean
lemma coe_zero : ((0 : Effect E) : E) = 0
```

**`ProbabilisticTheory.Effect.coe_one`**, a lemma, [line 78](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/Effect/Basic.lean#L78).

```lean
lemma coe_one : ((1 : Effect E) : E) = 1
```

**`ProbabilisticTheory.Effect.exists_pos_smul_mem`**, a lemma, [line 82](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/Effect/Basic.lean#L82).

> Every nonnegative observable becomes an effect after scaling it down by a large enough
> positive real: the effect interval reaches in every direction the positive cone does.

```lean
lemma exists_pos_smul_mem {B : E} (hB : 0 ≤ B) :
    ∃ r : ℝ, 0 < r ∧ r • B ∈ Effect E
```

## Depends on

- [Ordered positive cones](../orderunit/cone.md)

## Sources

- [Physlib/ProbabilisticTheory/Effect/Basic.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/Effect/Basic.lean)
