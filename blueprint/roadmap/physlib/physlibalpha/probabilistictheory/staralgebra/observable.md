---
declaration: module
origin: cited
lean: ProbabilisticTheory.Observable, ProbabilisticTheory.PositiveObservable, ProbabilisticTheory.UnitalPositiveLinearMap.onObservables, ProbabilisticTheory.UnitalPositiveLinearMap.coe_onObservables_apply
statement: formalized
proof: formalized
---

# Observables

The module `PhyslibAlpha.ProbabilisticTheory.StarAlgebra.Observable`, [PhyslibAlpha/ProbabilisticTheory/StarAlgebra/Observable.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/Observable.lean): 4 declarations, 4 with a docstring.

> Observables as self-adjoint elements, and the real state on observables of a complex state.

## i. Overview

> An observable is a self-adjoint element of a space with an involution. A complex state on the space
> restricts to a real state on its observables, the expectation-value functional.

## ii. Key results

> - `Observable`, `PositiveObservable` : observables and positive observables.
> - `UnitalPositiveLinearMap.onObservables` : the real state on observables of a complex state.

## iv. References

> * None.

## A. Observables

**`ProbabilisticTheory.Observable`**, an abbrev, [line 46](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/Observable.lean#L46).

> An observable in a space with an additive involution.

```lean
abbrev Observable (A : Type*) [AddGroup A] [StarAddMonoid A]
```

**`ProbabilisticTheory.PositiveObservable`**, an abbrev, [line 49](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/Observable.lean#L49).

> A positive observable in an ordered space with an additive involution.

```lean
abbrev PositiveObservable (A : Type*) [AddGroup A] [StarAddMonoid A] [PartialOrder A]
```

## B. The real state on observables

**`ProbabilisticTheory.UnitalPositiveLinearMap.onObservables`**, a def, [line 62](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/Observable.lean#L62).

> The real state on observables induced by a complex state on the ambient starred space.

```lean
noncomputable def onObservables (ω : 𝓢[ℂ, A]) : 𝓢[ℝ, Observable A]
```

**`ProbabilisticTheory.UnitalPositiveLinearMap.coe_onObservables_apply`**, a lemma, [line 68](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/Observable.lean#L68).

> Restricting a state to observables does not change its values, after regarding the real
> expectation value as a complex number.

```lean
lemma coe_onObservables_apply (ω : 𝓢[ℂ, A]) (a : Observable A) :
    ((ω.onObservables a : ℝ) : ℂ) = ω (a : A)
```

## C. Examples: states on observables

## Depends on

- [Restricting positive maps](restrict.md)

## Sources

- [PhyslibAlpha/ProbabilisticTheory/StarAlgebra/Observable.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/StarAlgebra/Observable.lean)
