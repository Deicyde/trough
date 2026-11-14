---
declaration: module
origin: cited
lean: CondensedMatter.Crystal.robertson_det_translationInvariantState, CondensedMatter.Crystal.covariance_translationInvariantState_eq_zero, CondensedMatter.Crystal.bracket_translationInvariantState_eq_zero
statement: formalized
proof: formalized
---

# Uncertainty relations in the invariant states of an infinite crystal

The module `PhyslibAlpha.CondensedMatter.Crystal.InvariantStateUncertainty`, [PhyslibAlpha/CondensedMatter/Crystal/InvariantStateUncertainty.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/InvariantStateUncertainty.lean): 3 declarations, 3 with a docstring.

> Robertson's relation for several observables holds in the translation invariant state of an
> interaction on the crystal `ℤ^d`, and the translations that fix the state fix entries of `Σ`
> and `Ω`.

## i. Overview

> The translation invariant state of the canonical ensemble of an interaction is a state on the
> quasi-local algebra of the crystal, so `AlgState.robertson_det` applies to it: for every finite
> family of observables, `|det Ω| ≤ det Σ`.
>
> The state is invariant under every translation `t_a`. If `t_a` fixes an observable `A` and
> reverses an observable `B`, as a translation by one site does for the uniform and the staggered
> magnetization of a finite block of an antiferromagnet, then `Σ_AB = Ω_AB = 0` by
> `AlgState.covariance_eq_zero_of_symm`. A state that breaks the translation by `a`, such as a
> Néel state, need not satisfy this.

## ii. Key results

> - `robertson_det_translationInvariantState` : `|det Ω| ≤ det Σ` in the translation invariant
>   state of an interaction.
> - `covariance_translationInvariantState_eq_zero`,
>   `bracket_translationInvariantState_eq_zero` : an observable fixed and one reversed by a
>   translation have `Σ_AB = Ω_AB = 0`.

## iv. References

> * O. Bratteli & D. Robinson, Operator Algebras and Quantum Statistical Mechanics 1,
>   Section 4.3.

## A. Uncertainty relations in the invariant state

**`CondensedMatter.Crystal.robertson_det_translationInvariantState`**, a lemma, [line 67](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/InvariantStateUncertainty.lean#L67).

> **Robertson's relation for several observables in the translation invariant state** of an
> interaction on the crystal `ℤ^d`.

```lean
lemma robertson_det_translationInvariantState {ι : Type*} [Fintype ι] [DecidableEq ι]
    (a : ι → selfAdjoint (crystalAlgebra Ω₀ (Fin d → ℤ) F)) :
    |((I.translationInvariantState β).bracketMatrix a).det| ≤
      ((I.translationInvariantState β).covarianceMatrix a).det
```

**`CondensedMatter.Crystal.covariance_translationInvariantState_eq_zero`**, a lemma, [line 82](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/InvariantStateUncertainty.lean#L82).

> In the translation invariant state, an observable fixed and one reversed by a translation
> are uncorrelated.

```lean
lemma covariance_translationInvariantState_eq_zero :
    (I.translationInvariantState β).covariance A B = 0
```

**`CondensedMatter.Crystal.bracket_translationInvariantState_eq_zero`**, a lemma, [line 88](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/InvariantStateUncertainty.lean#L88).

> In the translation invariant state, an observable fixed and one reversed by a translation
> have a bracket of expectation zero.

```lean
lemma bracket_translationInvariantState_eq_zero :
    (I.translationInvariantState β).bracket A B = 0
```

## Depends on

- [Translation invariant states of an infinite crystal](invariantstate.md)
- [Uncertainty relations for states on a `*`-algebra](../../../probabilistictheory/staralgebra/stateuncertainty.md)

## Sources

- [PhyslibAlpha/CondensedMatter/Crystal/InvariantStateUncertainty.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Crystal/InvariantStateUncertainty.lean)
