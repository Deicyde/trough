---
declaration: module
origin: cited
lean: Weight.IsState.toState, Weight.IsState.toState_apply, UnitalPositiveLinearMap.toWeight, UnitalPositiveLinearMap.toWeight_apply, UnitalPositiveLinearMap.toReal_toWeight_apply, UnitalPositiveLinearMap.toWeight_isState, Weight.stateEquiv
statement: formalized
proof: formalized
---

# Equivalence between states and finite normalized weights

The module `Physlib.ProbabilisticTheory.State.WeightEquivalence`, [Physlib/ProbabilisticTheory/State/WeightEquivalence.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/State/WeightEquivalence.lean): 7 declarations, 6 with a docstring.

> Finite normalized weights correspond exactly to positive unital linear functionals.

## i. Overview

> A state is, on its own terms, a normalized positive linear functional — `𝓢[ℝ, E]`, already fully
> built in `State/Basic.lean`. It is not *defined* as a weight; the two are independent notions, and
> the correspondence between them is a genuine theorem.

## ii. Key results

> - `Weight.stateEquiv` : finite normalized weights correspond exactly to states.

## iv. References

## A. From a normalized weight to a state

**`Weight.IsState.toState`**, a def, [line 56](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/State/WeightEquivalence.lean#L56).

> A finite normalized weight extends to a state.

```lean
noncomputable def toState (hw : w.IsState) : 𝓢[ℝ, E]
```

**`Weight.IsState.toState_apply`**, a lemma, [line 63](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/State/WeightEquivalence.lean#L63).

> The extended state agrees with the weight on positive observables.

```lean
lemma toState_apply (hw : w.IsState) (A : PosCone E) : hw.toState A = (w A).toReal
```

## B. From a state to a weight

**`UnitalPositiveLinearMap.toWeight`**, a def, [line 80](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/State/WeightEquivalence.lean#L80).

> The weight induced by a state: `ENNReal.ofReal` applied to the state's values on the positive
> cone, where they are automatically nonnegative.

```lean
noncomputable def toWeight (s : 𝓢[ℝ, E]) : Weight E
```

**`UnitalPositiveLinearMap.toWeight_apply`**, a lemma, [line 88](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/State/WeightEquivalence.lean#L88).

```lean
lemma toWeight_apply (s : 𝓢[ℝ, E]) (A : PosCone E) : s.toWeight A = ENNReal.ofReal (s (A : E))
```

**`UnitalPositiveLinearMap.toReal_toWeight_apply`**, a lemma, [line 92](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/State/WeightEquivalence.lean#L92).

> The weight induced by a state agrees with the state itself on the positive cone.

```lean
lemma toReal_toWeight_apply (s : 𝓢[ℝ, E]) (A : PosCone E) :
    (s.toWeight A).toReal = s (A : E)
```

**`UnitalPositiveLinearMap.toWeight_isState`**, a lemma, [line 97](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/State/WeightEquivalence.lean#L97).

> The weight induced by a state is finite and normalized.

```lean
lemma toWeight_isState (s : 𝓢[ℝ, E]) : s.toWeight.IsState
```

## C. The equivalence

**`Weight.stateEquiv`**, a def, [line 112](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/State/WeightEquivalence.lean#L112).

> Finite normalized weights correspond exactly to states.

```lean
noncomputable def stateEquiv : {w : Weight E // w.IsState} ≃ 𝓢[ℝ, E]
```

## Depends on

- [Positive unital maps](../channel/basic.md)
- [Extending finite weights (Physlib)](../weight/extension.md)

## Sources

- [Physlib/ProbabilisticTheory/State/WeightEquivalence.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/State/WeightEquivalence.lean)
