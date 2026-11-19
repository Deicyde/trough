---
declaration: module
origin: cited
lean: ProbabilisticTheory.State.toWeight, ProbabilisticTheory.State.toWeight_apply, ProbabilisticTheory.State.toReal_toWeight_apply, ProbabilisticTheory.State.toWeight_isState
statement: formalized
proof: formalized
---

# States as weights

The module `Physlib.ProbabilisticTheory.State.Weight`, [Physlib/ProbabilisticTheory/State/Weight.lean](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/ProbabilisticTheory/State/Weight.lean): 4 declarations, 3 with a docstring.

> Restriction of a state to positive observables gives a finite normalized weight.

## i. Overview

> State values are nonnegative on the positive cone. Reading them as extended nonnegative
> reals produces a weight with value one on the certain outcome.

## ii. Key results

> - `ProbabilisticTheory.State.toWeight` : the weight induced by a state.
> - `ProbabilisticTheory.State.toWeight_isState` : finiteness and normalization.

## iv. References

## A. From a state to a weight

**`ProbabilisticTheory.State.toWeight`**, a def, [line 51](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/ProbabilisticTheory/State/Weight.lean#L51).

> The weight induced by a state: `ENNReal.ofReal` applied to the state's values on the positive
> cone, where they are automatically nonnegative.

```lean
noncomputable def toWeight (s : P.State) : Weight P
```

**`ProbabilisticTheory.State.toWeight_apply`**, a lemma, [line 59](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/ProbabilisticTheory/State/Weight.lean#L59).

```lean
lemma toWeight_apply (s : P.State) (A : PosCone P) :
    s.toWeight A = ENNReal.ofReal (s (A : P.Observables))
```

**`ProbabilisticTheory.State.toReal_toWeight_apply`**, a lemma, [line 64](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/ProbabilisticTheory/State/Weight.lean#L64).

> The weight induced by a state agrees with the state itself on the positive cone.

```lean
lemma toReal_toWeight_apply (s : P.State) (A : PosCone P) :
    (s.toWeight A).toReal = s (A : P.Observables)
```

**`ProbabilisticTheory.State.toWeight_isState`**, a lemma, [line 69](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/ProbabilisticTheory/State/Weight.lean#L69).

> The weight induced by a state is finite and normalized.

```lean
lemma toWeight_isState (s : P.State) : s.toWeight.IsState
```

## Depends on

- [States](basic.md)
- [Weights (Physlib)](../weight/basic.md)

## Sources

- [Physlib/ProbabilisticTheory/State/Weight.lean at 8c87bdfb](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/ProbabilisticTheory/State/Weight.lean)
