---
declaration: module
origin: cited
lean: ProbabilisticTheory.QuasiLocal.LocalStateFamily, ProbabilisticTheory.QuasiLocal.LocalStateFamily.lift, ProbabilisticTheory.QuasiLocal.LocalStateFamily.lift_of, ProbabilisticTheory.QuasiLocal.LocalStateFamily.toAlgState, ProbabilisticTheory.QuasiLocal.LocalStateFamily.toAlgState_of
statement: formalized
proof: formalized
---

# States of the quasi-local algebra from compatible local states

The module `PhyslibAlpha.ProbabilisticTheory.QuasiLocal.State`, [PhyslibAlpha/ProbabilisticTheory/QuasiLocal/State.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/QuasiLocal/State.lean): 5 declarations, 4 with a docstring.

> A family of local states, each the restriction of the next, is a state of the quasi-local algebra.

## i. Overview

> A state of an infinite system is determined by the expectation values of the local observables.
> A *compatible family* assigns to each finite region `X` a state of its algebra `A X` such that the
> state of a larger region restricts to the state of the smaller: `ω_Y (incl a) = ω_X (a)`. Such a
> family defines a linear functional on the quasi-local algebra, which is a state: normalized,
> Hermitian and positive. Every element of the quasi-local algebra is local, and positivity of
> `a* a` is positivity of local states.

## ii. Key results

> - `LocalStateFamily` : a compatible family of local states.
> - `LocalStateFamily.toAlgState` : the state of the quasi-local algebra.
> - `LocalStateFamily.toAlgState_of` : its value on a local observable is the local expectation.

## iv. References

> * O. Bratteli & D. Robinson, Operator Algebras and Quantum Statistical Mechanics 1,
>   Section 2.6.

## A. Compatible families

**`ProbabilisticTheory.QuasiLocal.LocalStateFamily`**, a structure, [line 59](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/QuasiLocal/State.lean#L59).

> A compatible family of local states of a net of algebras.

```lean
structure LocalStateFamily where
  /-- The local functionals. -/
  state : ∀ X : Finset S, N.A X →ₗ[ℂ] ℂ
  /-- The functional of a larger region restricts to that of a smaller one. -/
  compat : ∀ {X Y : Finset S} (h : X ≤ Y) (a : N.A X), state Y (N.incl h a) = state X a
  /-- The local functionals are normalized. -/
  map_one : ∀ X, state X 1 = 1
  /-- The local functionals are Hermitian. -/
  map_star : ∀ X (a : N.A X), state X (star a) = star (state X a)
  /-- The local functionals are positive. -/
  nonneg : ∀ X (a : N.A X), 0 ≤ state X (star a * a)
```

## B. The state of the quasi-local algebra

**`ProbabilisticTheory.QuasiLocal.LocalStateFamily.lift`**, a def, [line 76](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/QuasiLocal/State.lean#L76).

> The linear functional on the quasi-local algebra defined by a compatible family.

```lean
def LocalStateFamily.lift (ω : LocalStateFamily N) : N.Quasilocal →ₗ[ℂ] ℂ
```

**`ProbabilisticTheory.QuasiLocal.LocalStateFamily.lift_of`**, a lemma, [line 81](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/QuasiLocal/State.lean#L81).

```lean
lemma LocalStateFamily.lift_of (ω : LocalStateFamily N) (X : Finset S) (a : N.A X) :
    ω.lift (N.of X a) = ω.state X a
```

**`ProbabilisticTheory.QuasiLocal.LocalStateFamily.toAlgState`**, a def, [line 85](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/QuasiLocal/State.lean#L85).

> **The state of the quasi-local algebra** defined by a compatible family.

```lean
def LocalStateFamily.toAlgState (ω : LocalStateFamily N) : AlgState N.Quasilocal
```

**`ProbabilisticTheory.QuasiLocal.LocalStateFamily.toAlgState_of`**, a lemma, [line 101](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/QuasiLocal/State.lean#L101).

> The state of a compatible family on a local observable is the local expectation.

```lean
lemma LocalStateFamily.toAlgState_of (ω : LocalStateFamily N) (X : Finset S) (a : N.A X) :
    ω.toAlgState (N.of X a) = ω.state X a
```

## Depends on

- [Nets of algebras over the finite regions of a lattice and their quasi-local algebra](algebranet.md)
- [The GNS representation of a state on a unital `*`-algebra](../staralgebra/gns.md)

## Sources

- [PhyslibAlpha/ProbabilisticTheory/QuasiLocal/State.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/QuasiLocal/State.lean)
