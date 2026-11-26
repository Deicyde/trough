---
declaration: module
origin: cited
lean: Weight.IsState.toState, Weight.IsState.toState_apply, Weight.stateEquiv
statement: formalized
proof: formalized
---

# States from normalized weights

The module `Physlib.ProbabilisticTheory.Weight.State`, [Physlib/ProbabilisticTheory/Weight/State.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/ProbabilisticTheory/Weight/State.lean): 3 declarations, 3 with a docstring.

> Finite normalized weights correspond exactly to states.

## i. Overview

> A finite normalized weight extends linearly to a state. Restriction to positive observables
> recovers the original weight, giving an equivalence.

## ii. Key results

> - `Weight.IsState.toState` : extend a finite normalized weight to a state.
> - `Weight.stateEquiv` : the correspondence with states.

## iv. References

## A. From a normalized weight to a state

**`Weight.IsState.toState`**, a def, [line 51](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/ProbabilisticTheory/Weight/State.lean#L51).

> A finite normalized weight extends to a state.

```lean
noncomputable def IsState.toState (hw : w.IsState) : P.State
```

**`Weight.IsState.toState_apply`**, a lemma, [line 58](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/ProbabilisticTheory/Weight/State.lean#L58).

> The extended state agrees with the weight on positive observables.

```lean
lemma IsState.toState_apply (hw : w.IsState) (A : PosCone P) : hw.toState A = (w A).toReal
```

## B. The equivalence

**`Weight.stateEquiv`**, a def, [line 68](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/ProbabilisticTheory/Weight/State.lean#L68).

> Finite normalized weights correspond exactly to states.

```lean
noncomputable def stateEquiv : {w : Weight P // w.IsState} ≃ P.State
```

## Depends on

- [States as weights](../state/weight.md)
- [Extending finite weights (Physlib)](extension.md)

## Sources

- [Physlib/ProbabilisticTheory/Weight/State.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/ProbabilisticTheory/Weight/State.lean)
