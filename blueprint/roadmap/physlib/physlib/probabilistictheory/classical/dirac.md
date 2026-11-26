---
declaration: module
origin: cited
lean: ProbabilisticTheory.Classical.eval, ProbabilisticTheory.Classical.dirac, ProbabilisticTheory.Classical.dirac_apply, ProbabilisticTheory.Classical.sq_apply_le_apply_sq, ProbabilisticTheory.Classical.eq_dirac_iff, ProbabilisticTheory.Classical.isPure_dirac
statement: formalized
proof: formalized
---

# Dirac states

The module `Physlib.ProbabilisticTheory.Classical.Dirac`, [Physlib/ProbabilisticTheory/Classical/Dirac.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/ProbabilisticTheory/Classical/Dirac.lean): 6 declarations, 6 with a docstring.

> A classical system in a definite configuration is in a pure state.

## i. Overview

> The Dirac state at a configuration `x` assigns to each observable its value at `x`. It describes
> a classical system whose configuration is known exactly, so every observable has vanishing
> variance. Conversely, a state in which every observable has vanishing variance around its value
> at `x` is the Dirac state at `x`. Dirac states are therefore pure.

## ii. Key results

> - `ProbabilisticTheory.Classical.dirac` : the Dirac state at a configuration.
> - `ProbabilisticTheory.Classical.eq_dirac_iff` : the Dirac state is the state in which every
>   observable has a sharp value.
> - `ProbabilisticTheory.Classical.isPure_dirac` : Dirac states are pure.

## iv. References

## A. Dirac states

**`ProbabilisticTheory.Classical.eval`**, a def, [line 55](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/ProbabilisticTheory/Classical/Dirac.lean#L55).

> Reading off the value of each quantity in the configuration `x`.

```lean
noncomputable def eval (x : X) : S →ₚ[ℂ] ℂ
```

**`ProbabilisticTheory.Classical.dirac`**, a def, [line 63](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/ProbabilisticTheory/Classical/Dirac.lean#L63).

> The Dirac state at a configuration `x` evaluates observables at `x`.

```lean
noncomputable def dirac (x : X) : State (classical S)
```

**`ProbabilisticTheory.Classical.dirac_apply`**, a lemma, [line 68](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/ProbabilisticTheory/Classical/Dirac.lean#L68).

> The Dirac state at `x` assigns each observable its value at `x`.

```lean
lemma dirac_apply (x : X) (f : Observables (classical S)) : dirac S x f = f x
```

## B. Sharp values

**`ProbabilisticTheory.Classical.sq_apply_le_apply_sq`**, a lemma, [line 75](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/ProbabilisticTheory/Classical/Dirac.lean#L75).

> The square of the mean is at most the mean of the square.

```lean
lemma sq_apply_le_apply_sq (ω : State (classical S)) (f : Observables (classical S)) :
    ω f ^ 2 ≤ ω (f ^ 2)
```

**`ProbabilisticTheory.Classical.eq_dirac_iff`**, a lemma, [line 85](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/ProbabilisticTheory/Classical/Dirac.lean#L85).

> The Dirac state at `x` is the state in which every observable has the sharp value it takes
> at `x`.

```lean
lemma eq_dirac_iff {ω : State (classical S)} {x : X} :
    ω = dirac S x ↔ ∀ f, ω ((f - f x • 1) ^ 2) = 0
```

## C. Purity

**`ProbabilisticTheory.Classical.isPure_dirac`**, a lemma, [line 94](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/ProbabilisticTheory/Classical/Dirac.lean#L94).

> A classical system in a definite configuration is in a pure state.

```lean
lemma isPure_dirac (x : X) : (dirac S x).IsPure
```

## Depends on

- [Classical probabilistic theories](basic.md)
- [Channels of C⋆-algebras](../cstaralgebra/channel.md)
- [Convex state spaces (Physlib)](../state/convex.md)

## Sources

- [Physlib/ProbabilisticTheory/Classical/Dirac.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/ProbabilisticTheory/Classical/Dirac.lean)
