---
declaration: module
origin: cited
lean: ProbabilisticTheory.State.instMulActionReversible, ProbabilisticTheory.State.reversible_smul_apply, ProbabilisticTheory.State.IsInvariant, ProbabilisticTheory.State.IsInvariant.comap
statement: formalized
proof: formalized
---

# States under symmetries

The module `Physlib.ProbabilisticTheory.State.Symmetry`, [Physlib/ProbabilisticTheory/State/Symmetry.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/ProbabilisticTheory/State/Symmetry.lean): 4 declarations, 3 with a docstring.

> Reversible changes of observables act on states by inverse pullback.

## i. Overview

> A state is invariant under a group action when every transformation leaves it fixed.
> Pullback along an intertwining channel preserves this invariance.

## ii. Key results

> - `ProbabilisticTheory.State.reversible_smul_apply` : evaluation after a reversible action.
> - `ProbabilisticTheory.State.IsInvariant` : states fixed by a group action.
> - `ProbabilisticTheory.State.IsInvariant.comap` : pullback preserves invariant states.

## iv. References

## A. Reversible action

**`ProbabilisticTheory.State.instMulActionReversible`**, an instance, [line 47](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/ProbabilisticTheory/State/Symmetry.lean#L47).

> The action on states induced by the inverse of a reversible transformation.

```lean
instance instMulActionReversible : MulAction (Reversible P P) P.State
```

**`ProbabilisticTheory.State.reversible_smul_apply`**, a lemma, [line 52](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/ProbabilisticTheory/State/Symmetry.lean#L52).

```lean
lemma reversible_smul_apply (φ : Reversible P P) (ω : P.State) (x : P.Observables) :
    (φ • ω) x = ω (φ.symm x)
```

## B. Invariant states

**`ProbabilisticTheory.State.IsInvariant`**, a def, [line 58](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/ProbabilisticTheory/State/Symmetry.lean#L58).

> A state is invariant when every transformation of the group action fixes it.

```lean
def IsInvariant (ω : P.State) (ρ : G →* Reversible P P) : Prop
```

**`ProbabilisticTheory.State.IsInvariant.comap`**, a lemma, [line 61](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/ProbabilisticTheory/State/Symmetry.lean#L61).

> Pulling back an invariant state along an intertwining channel preserves invariance.

```lean
lemma IsInvariant.comap {ρ : G →* Reversible P P} {σ : G →* Reversible Q Q}
    {Φ : Channel P Q} {ω : Q.State} (hω : ω.IsInvariant σ)
    (h : Φ.IsIntertwining ρ σ) : (ω.comap Φ).IsInvariant ρ
```

## Depends on

- [Covariant channels](../channel/covariant.md)
- [States](basic.md)

## Sources

- [Physlib/ProbabilisticTheory/State/Symmetry.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/ProbabilisticTheory/State/Symmetry.lean)
