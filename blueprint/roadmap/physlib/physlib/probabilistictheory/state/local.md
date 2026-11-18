---
declaration: module
origin: cited
lean: ProbabilisticTheory.LocalNet.restrict, ProbabilisticTheory.LocalNet.restrict_apply, ProbabilisticTheory.LocalNet.restrict_refl, ProbabilisticTheory.LocalNet.restrict_restrict, ProbabilisticTheory.LocalNet.CompatibleStates, ProbabilisticTheory.LocalNet.CompatibleStates.compat_apply, ProbabilisticTheory.LocalNet.Quasilocal.lift, ProbabilisticTheory.LocalNet.Quasilocal.lift_apply
statement: formalized
proof: formalized
---

# States of a local net

The module `Physlib.ProbabilisticTheory.State.Local`, [Physlib/ProbabilisticTheory/State/Local.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/State/Local.lean): 12 declarations (1 instance with no name), 12 with a docstring.

> Compatible subsystem states and states of the whole system.

## i. Overview

> An observable of a smaller subsystem can also be measured in a larger one. A state of the larger
> subsystem therefore determines a state of the smaller one: assign each smaller observable the
> expectation it has when viewed in the larger system. This operation is called restriction.
> Observable inclusions point from smaller to larger subsystems, state restrictions point the other
> way.
>
> In a tensor product system, including an observable means letting it act as the identity on the
> additional factors. Restricting a density-matrix state then amounts to tracing out those factors.
> A `LocalNet.CompatibleStates` assigns a state to every subsystem, with the requirement that a
> smaller subsystem's state agrees with the restriction of any larger subsystem's state. Thus the
> expectation of an observable does not depend on which containing subsystem is used to evaluate
> it.
>
> For a nonempty directed family, local positivity defines an order on the quasilocal observables.
> Every compatible family then defines a unique state of the whole system. Conversely, a quasilocal
> state restricts to a compatible family of subsystem states.

## ii. Key results

> - `LocalNet.restrict`: precomposition with the observable inclusion map.
> - `LocalNet.CompatibleStates`: a compatible family of states on the subsystems.
> - `LocalNet.CompatibleStates.compat_apply`: compatible states agree on included observables.
> - `LocalNet.Quasilocal.toState`: the quasilocal state defined by a compatible family.
> - `LocalNet.Quasilocal.stateEquiv`: quasilocal states correspond to compatible local states.

## iv. References

## A. Restriction of states

**`ProbabilisticTheory.LocalNet.restrict`**, a def, [line 68](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/State/Local.lean#L68).

> Restrict a state of `Y` to `X` by pulling it back along the observable inclusion channel.

```lean
def restrict (h : X ≤ Y) (ω : 𝓢[ℝ, A Y]) : 𝓢[ℝ, A X]
```

**`ProbabilisticTheory.LocalNet.restrict_apply`**, a lemma, [line 72](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/State/Local.lean#L72).

> Restriction evaluates an observable through its inclusion into the larger subsystem.

```lean
lemma restrict_apply (h : X ≤ Y) (ω : 𝓢[ℝ, A Y]) (a : A X) :
    N.restrict h ω a = ω (N.incl h a)
```

**`ProbabilisticTheory.LocalNet.restrict_refl`**, a lemma, [line 77](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/State/Local.lean#L77).

> Restriction to the same subsystem is the identity.

```lean
lemma restrict_refl (ω : 𝓢[ℝ, A X]) : N.restrict (le_refl X) ω = ω
```

**`ProbabilisticTheory.LocalNet.restrict_restrict`**, a lemma, [line 82](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/State/Local.lean#L82).

> Successive restrictions agree with direct restriction.

```lean
lemma restrict_restrict (h₁ : X ≤ Y) (h₂ : Y ≤ Z) (h₃ : X ≤ Z) (ω : 𝓢[ℝ, A Z]) :
    N.restrict h₁ (N.restrict h₂ ω) = N.restrict h₃ ω
```

## B. Compatible local states

> A compatible family assigns a state to every local subsystem. Whenever one subsystem is contained
> in another, its state must agree with the restriction of the larger subsystem's state. This
> ensures that local observables have consistent expectation values, even in infinite systems with
> correlations and entanglement.

**`ProbabilisticTheory.LocalNet.CompatibleStates`**, a structure, [line 98](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/State/Local.lean#L98).

> A state on each subsystem whose restrictions agree with the states of smaller subsystems.

```lean
structure CompatibleStates (N : LocalNet R A) where
  /-- The state of the subsystem `X`. -/
  state : ∀ X, 𝓢[ℝ, A X]
  /-- The state of `X` is the restriction of the state of any larger subsystem `Y`. -/
  compat : ∀ {X Y : R} (h : X ≤ Y), N.restrict h (state Y) = state X
```

**`ProbabilisticTheory.LocalNet.CompatibleStates.compat_apply`**, a lemma, [line 105](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/State/Local.lean#L105).

> An observable has the same expectation in every subsystem containing it.

```lean
lemma CompatibleStates.compat_apply {N : LocalNet R A} (ω : N.CompatibleStates)
    {X Y : R} (h : X ≤ Y) (a : A X) :
    ω.state Y (N.incl h a) = ω.state X a
```

**An instance with no name**, [line 116](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/State/Local.lean#L116).

> Decidable equality used internally by the direct-limit construction.

```lean
noncomputable local instance : DecidableEq R
```

## C. States of the whole system

> A quasilocal observable has a local representative. A compatible family evaluates that
> representative in its subsystem; compatibility makes the result independent of the representative.

**`ProbabilisticTheory.LocalNet.Quasilocal.lift`**, a def, [line 126](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/State/Local.lean#L126).

> The expectation functional of `LocalNet.CompatibleStates` on the whole system.

```lean
noncomputable def lift (σ : N.CompatibleStates) : N.Quasilocal →ₗ[ℝ] ℝ
```

**`ProbabilisticTheory.LocalNet.Quasilocal.lift_apply`**, a lemma, [line 136](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/State/Local.lean#L136).

> The expectation functional of `LocalNet.CompatibleStates` evaluates a quasilocal observable
> in any subsystem representing it.

```lean
lemma lift_apply (σ : N.CompatibleStates) (i : R) (a : A i) :
    lift σ (toQuasilocal N i a) = σ.state i a
```

**`ProbabilisticTheory.LocalNet.Quasilocal.toState`**, a def, [line 144](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/State/Local.lean#L144).

> The state of the whole system defined by `LocalNet.CompatibleStates`.

```lean
noncomputable def toState (σ : N.CompatibleStates) : 𝓢[ℝ, N.Quasilocal]
```

**`ProbabilisticTheory.LocalNet.Quasilocal.toState_apply`**, a lemma, [line 155](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/State/Local.lean#L155).

> On a quasilocal observable represented in the subsystem `i`, `toState σ` is the state of `i`.

```lean
lemma toState_apply (σ : N.CompatibleStates) (i : R) (a : A i) :
    toState σ (toQuasilocal N i a) = σ.state i a
```

**`ProbabilisticTheory.LocalNet.Quasilocal.stateEquiv`**, a def, [line 160](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/State/Local.lean#L160).

> A state of the whole system is the same as `LocalNet.CompatibleStates`.

```lean
noncomputable def stateEquiv : 𝓢[ℝ, N.Quasilocal] ≃ N.CompatibleStates
```

## Depends on

- [Order-unit structure on quasilocal observables](../localnet/quasilocalorder.md)
- [States](basic.md)

## Sources

- [Physlib/ProbabilisticTheory/State/Local.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/State/Local.lean)
