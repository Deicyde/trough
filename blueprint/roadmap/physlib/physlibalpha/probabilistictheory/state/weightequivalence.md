---
declaration: module
origin: cited
lean: PhyslibAlpha.ProbabilisticTheory.Weight.IsState.toState, PhyslibAlpha.ProbabilisticTheory.UnitalPositiveLinearMap.toWeight, PhyslibAlpha.ProbabilisticTheory.UnitalPositiveLinearMap.toWeight_apply, PhyslibAlpha.ProbabilisticTheory.UnitalPositiveLinearMap.toReal_toWeight_apply, PhyslibAlpha.ProbabilisticTheory.UnitalPositiveLinearMap.toWeight_isState, PhyslibAlpha.ProbabilisticTheory.Weight.stateEquiv
statement: formalized
proof: formalized
---

# States and finite normalized weights

The module `PhyslibAlpha.ProbabilisticTheory.State.WeightEquivalence`, [PhyslibAlpha/ProbabilisticTheory/State/WeightEquivalence.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ProbabilisticTheory/State/WeightEquivalence.lean): 6 declarations, 5 with a docstring.

> Finite normalized weights on an order unit space correspond bijectively to states.

## i. Overview

> A state is a normalized positive linear functional, a weight is a function on the positive cone.
> Restricting a state to the positive cone gives a finite normalized weight, and extending a finite
> normalized weight linearly gives a state. These are inverse to each other.

## ii. Key results

> - `Weight.stateEquiv` : finite normalized weights correspond to states.

## iv. References

> * None.

## A. From a normalized weight to a state

**`PhyslibAlpha.ProbabilisticTheory.Weight.IsState.toState`**, a def, [line 60](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ProbabilisticTheory/State/WeightEquivalence.lean#L60).

> A finite normalized weight extends to a state.

```lean
noncomputable def toState (hw : w.IsState) : 𝓢[ℝ, E]
```

## B. From a state to a weight

**`PhyslibAlpha.ProbabilisticTheory.UnitalPositiveLinearMap.toWeight`**, a def, [line 81](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ProbabilisticTheory/State/WeightEquivalence.lean#L81).

> The weight induced by a state: `ENNReal.ofReal` applied to the state's values on the positive
> cone, where they are automatically nonnegative.

```lean
noncomputable def toWeight (s : 𝓢[ℝ, E]) : Weight E
```

**`PhyslibAlpha.ProbabilisticTheory.UnitalPositiveLinearMap.toWeight_apply`**, a lemma, [line 91](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ProbabilisticTheory/State/WeightEquivalence.lean#L91).

```lean
lemma toWeight_apply (s : 𝓢[ℝ, E]) (A : PosCone E) : s.toWeight A = ENNReal.ofReal (s (A : E))
```

**`PhyslibAlpha.ProbabilisticTheory.UnitalPositiveLinearMap.toReal_toWeight_apply`**, a lemma, [line 95](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ProbabilisticTheory/State/WeightEquivalence.lean#L95).

> The weight induced by a state agrees with the state itself on the positive cone.

```lean
lemma toReal_toWeight_apply (s : 𝓢[ℝ, E]) (A : PosCone E) :
    (s.toWeight A).toReal = s (A : E)
```

**`PhyslibAlpha.ProbabilisticTheory.UnitalPositiveLinearMap.toWeight_isState`**, a lemma, [line 100](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ProbabilisticTheory/State/WeightEquivalence.lean#L100).

> The weight induced by a state is finite and normalized.

```lean
lemma toWeight_isState (s : 𝓢[ℝ, E]) : s.toWeight.IsState
```

## C. The equivalence

**`PhyslibAlpha.ProbabilisticTheory.Weight.stateEquiv`**, a def, [line 115](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ProbabilisticTheory/State/WeightEquivalence.lean#L115).

> Finite normalized weights correspond exactly to states.

```lean
noncomputable def stateEquiv : {w : Weight E // w.IsState} ≃ 𝓢[ℝ, E]
```

## Depends on

- [Channels](../channel/basic.md)
- [Extending finite weights (PhyslibAlpha)](../weight/extension.md)

## Sources

- [PhyslibAlpha/ProbabilisticTheory/State/WeightEquivalence.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ProbabilisticTheory/State/WeightEquivalence.lean)
