---
declaration: module
origin: cited
lean: ProbabilisticTheory.Effect, ProbabilisticTheory.Effect.mem_iff_mem_posCone_and_one_sub_mem_posCone, ProbabilisticTheory.Effect.instZero, ProbabilisticTheory.Effect.instOne, ProbabilisticTheory.Effect.instNonempty, ProbabilisticTheory.Effect.coe_zero, ProbabilisticTheory.Effect.coe_one, ProbabilisticTheory.Effect.exists_pos_smul_mem
statement: formalized
proof: formalized
---

# Effects (Physlib)

The module `Physlib.ProbabilisticTheory.Effect.Basic`, [Physlib/ProbabilisticTheory/Effect/Basic.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/ProbabilisticTheory/Effect/Basic.lean): 8 declarations, 3 with a docstring.

## i. Overview

> An effect models a yes/no measurement outcome, ranging continuously between the impossible
> outcome `0` and the certain outcome `1`. Formally, it is a point of the order interval `[0, 1]`
> inside `P.Observables`. For self-adjoint matrices, effects are exactly the operators
> `0 ≤ M ≤ 1` — the elements of a POVM.

## ii. Key results

> - `ProbabilisticTheory.Effect` : a bounded measurement outcome, the
>   order interval `[0, 1]` of its observables.
> - `Effect.mem_iff_mem_posCone_and_one_sub_mem_posCone` : an effect is exactly a positive element
>   whose complement from the order unit is also positive.
> - `Effect.exists_pos_smul_mem` : every positive observable becomes an effect after scaling it down
>   enough.

## iv. References

> - G. Ludwig, *Foundations of Quantum Mechanics I*, Springer, 1983.
>   <https://link.springer.com/book/10.1007/978-3-642-86751-4>

## A. Effects

**`ProbabilisticTheory.Effect`**, an abbrev, [line 52](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/ProbabilisticTheory/Effect/Basic.lean#L52).

> A bounded measurement outcome.

```lean
abbrev ProbabilisticTheory.Effect (P : ProbabilisticTheory)
```

**`ProbabilisticTheory.Effect.mem_iff_mem_posCone_and_one_sub_mem_posCone`**, a lemma, [line 59](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/ProbabilisticTheory/Effect/Basic.lean#L59).

> An effect is a positive element whose complement from the order unit is positive.

```lean
lemma mem_iff_mem_posCone_and_one_sub_mem_posCone {A : P.Observables} :
    A ∈ P.Effect ↔ A ∈ PosCone P ∧ 1 - A ∈ PosCone P
```

**`ProbabilisticTheory.Effect.instZero`**, an instance, [line 63](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/ProbabilisticTheory/Effect/Basic.lean#L63).

```lean
instance instZero : Zero P.Effect
```

**`ProbabilisticTheory.Effect.instOne`**, an instance, [line 65](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/ProbabilisticTheory/Effect/Basic.lean#L65).

```lean
instance instOne : One P.Effect
```

**`ProbabilisticTheory.Effect.instNonempty`**, an instance, [line 67](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/ProbabilisticTheory/Effect/Basic.lean#L67).

```lean
instance instNonempty : Nonempty P.Effect
```

**`ProbabilisticTheory.Effect.coe_zero`**, a lemma, [line 69](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/ProbabilisticTheory/Effect/Basic.lean#L69).

```lean
lemma coe_zero : ((0 : P.Effect) : P.Observables) = 0
```

**`ProbabilisticTheory.Effect.coe_one`**, a lemma, [line 71](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/ProbabilisticTheory/Effect/Basic.lean#L71).

```lean
lemma coe_one : ((1 : P.Effect) : P.Observables) = 1
```

**`ProbabilisticTheory.Effect.exists_pos_smul_mem`**, a lemma, [line 75](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/ProbabilisticTheory/Effect/Basic.lean#L75).

> Every nonnegative observable becomes an effect after scaling it down by a large enough
> positive real: the effect interval reaches in every direction the positive cone does.

```lean
lemma exists_pos_smul_mem {B : P.Observables} (hB : 0 ≤ B) :
    ∃ r : ℝ, 0 < r ∧ r • B ∈ P.Effect
```

## Depends on

- [Ordered positive cones (Physlib)](../orderunit/cone.md)

## Sources

- [Physlib/ProbabilisticTheory/Effect/Basic.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/ProbabilisticTheory/Effect/Basic.lean)
