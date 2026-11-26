---
declaration: module
origin: cited
lean: ProbabilisticTheory.State, ProbabilisticTheory.State.toPositiveLinearMap, ProbabilisticTheory.State.toLinearMap, ProbabilisticTheory.State.toPositiveLinearMap_apply, ProbabilisticTheory.State.comap, ProbabilisticTheory.State.comap_apply
statement: formalized
proof: formalized
---

# States

The module `Physlib.ProbabilisticTheory.State.Basic`, [Physlib/ProbabilisticTheory/State/Basic.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/ProbabilisticTheory/State/Basic.lean): 7 declarations (1 instance with no name), 4 with a docstring.

## i. Overview

> A state assigns each observable its expectation value. It is a channel into the real numbers:
> positive (`0 ≤ A ⟹ 0 ≤ ω A`) and normalized so the certain outcome reads `ω 1 = 1`. In quantum
> mechanics, `ω A = tr(ρA)` for a density matrix `ρ`.

## ii. Key results

> - `ProbabilisticTheory.State` : normalized real expectation functionals on observables.
> - `ProbabilisticTheory.State.comap` : pull back a state by evaluating observables through a
>   channel.

## iv. References

## A. States

**`ProbabilisticTheory.State`**, an abbrev, [line 43](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/ProbabilisticTheory/State/Basic.lean#L43).

> States assign normalized real expectation values to observables.

```lean
abbrev ProbabilisticTheory.State (P : ProbabilisticTheory)
```

**An instance with no name**, [line 49](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/ProbabilisticTheory/State/Basic.lean#L49).

```lean
instance : FunLike P.State P.Observables ℝ
```

**`ProbabilisticTheory.State.toPositiveLinearMap`**, an abbrev, [line 53](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/ProbabilisticTheory/State/Basic.lean#L53).

> The real positive functional underlying a state.

```lean
abbrev toPositiveLinearMap (ω : P.State) : P.Observables →ₚ[ℝ] ℝ
```

**`ProbabilisticTheory.State.toLinearMap`**, an abbrev, [line 57](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/ProbabilisticTheory/State/Basic.lean#L57).

> The real linear functional underlying a state.

```lean
abbrev toLinearMap (ω : P.State) : P.Observables →ₗ[ℝ] ℝ
```

**`ProbabilisticTheory.State.toPositiveLinearMap_apply`**, a lemma, [line 61](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/ProbabilisticTheory/State/Basic.lean#L61).

```lean
lemma toPositiveLinearMap_apply (ω : P.State) (A : P.Observables) :
    ω.toPositiveLinearMap A = ω A
```

## B. Transporting states along channels

**`ProbabilisticTheory.State.comap`**, a def, [line 71](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/ProbabilisticTheory/State/Basic.lean#L71).

> Pull back a state by applying the channel before evaluating each observable.

```lean
def comap (ω : Q.State) (f : Channel P Q) : P.State
```

**`ProbabilisticTheory.State.comap_apply`**, a lemma, [line 74](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/ProbabilisticTheory/State/Basic.lean#L74).

```lean
lemma comap_apply (ω : Q.State) (f : Channel P Q) (x : P.Observables) :
    ω.comap f x = ω (f x)
```

## Depends on

- [Channels between observable spaces](../channel/basic.md)

## Sources

- [Physlib/ProbabilisticTheory/State/Basic.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/ProbabilisticTheory/State/Basic.lean)
