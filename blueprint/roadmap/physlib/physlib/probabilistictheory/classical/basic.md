---
declaration: module
origin: cited
lean: ProbabilisticTheory.classical, ProbabilisticTheory.Classical.toSelfAdjoint, ProbabilisticTheory.Classical.instFunLike, ProbabilisticTheory.Classical.ofReal_apply, ProbabilisticTheory.Classical.zero_apply, ProbabilisticTheory.Classical.one_apply, ProbabilisticTheory.Classical.add_apply, ProbabilisticTheory.Classical.sub_apply
statement: formalized
proof: formalized
---

# Classical probabilistic theories

The module `Physlib.ProbabilisticTheory.Classical.Basic`, [Physlib/ProbabilisticTheory/Classical/Basic.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/ProbabilisticTheory/Classical/Basic.lean): 14 declarations (1 instance with no name), 8 with a docstring.

> In a classical system every observable has a definite value in each configuration.

## i. Overview

> An observable of a classical system with configurations `X` is a bounded real function on `X`.
> A closed algebra `S` of bounded functions fixes which functions count as observables. On a
> measurable space these are the bounded measurable functions.
>
> The observables in `S` form the probabilistic theory `classical S`. Observables add, multiply and
> compare value by value. Their algebra is commutative, which is characteristic of classical
> systems.

## ii. Key results

> - `ProbabilisticTheory.classical` : the classical theory of a closed algebra of bounded functions.
> - `ProbabilisticTheory.Classical.instFunLike` : the value of an observable in a configuration.
> - `ProbabilisticTheory.Classical.le_def` : observables are ordered by their values.

## iv. References

## A. The classical theory

**`ProbabilisticTheory.classical`**, a def, [line 51](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/ProbabilisticTheory/Classical/Basic.lean#L51).

> The classical theory whose observables are the real functions in a closed algebra `S` of
> bounded functions.

```lean
noncomputable def classical {X : Type*} (S : StarSubalgebra ℂ (lp (fun _ : X ↦ ℂ) ∞))
    [IsClosed (S : Set (lp (fun _ : X ↦ ℂ) ∞))] : ProbabilisticTheory
```

## B. Values of observables

**`ProbabilisticTheory.Classical.toSelfAdjoint`**, a def, [line 65](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/ProbabilisticTheory/Classical/Basic.lean#L65).

> An observable as a real function in `S`.

```lean
def toSelfAdjoint : Observables (classical S) ≃ selfAdjoint S
```

**An instance with no name**, [line 69](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/ProbabilisticTheory/Classical/Basic.lean#L69).

> Observables multiply value by value.

```lean
noncomputable instance : CommRing (Observables (classical S))
```

**`ProbabilisticTheory.Classical.instFunLike`**, an instance, [line 76](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/ProbabilisticTheory/Classical/Basic.lean#L76).

> The value of an observable in a configuration.

```lean
noncomputable instance instFunLike : FunLike (Observables (classical S)) X ℝ
```

**`ProbabilisticTheory.Classical.ofReal_apply`**, a lemma, [line 85](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/ProbabilisticTheory/Classical/Basic.lean#L85).

> The function of an observable takes real values.

```lean
lemma ofReal_apply (f : Observables (classical S)) (x : X) :
    (f x : ℂ) = ((toSelfAdjoint f).1 : lp (fun _ : X ↦ ℂ) ∞) x
```

**`ProbabilisticTheory.Classical.zero_apply`**, a lemma, [line 89](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/ProbabilisticTheory/Classical/Basic.lean#L89).

```lean
lemma zero_apply (x : X) : (0 : Observables (classical S)) x = 0
```

**`ProbabilisticTheory.Classical.one_apply`**, a lemma, [line 91](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/ProbabilisticTheory/Classical/Basic.lean#L91).

```lean
lemma one_apply (x : X) : (1 : Observables (classical S)) x = 1
```

**`ProbabilisticTheory.Classical.add_apply`**, a lemma, [line 93](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/ProbabilisticTheory/Classical/Basic.lean#L93).

```lean
lemma add_apply (f g : Observables (classical S)) (x : X) : (f + g) x = f x + g x
```

**`ProbabilisticTheory.Classical.sub_apply`**, a lemma, [line 95](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/ProbabilisticTheory/Classical/Basic.lean#L95).

```lean
lemma sub_apply (f g : Observables (classical S)) (x : X) : (f - g) x = f x - g x
```

**`ProbabilisticTheory.Classical.smul_apply`**, a lemma, [line 97](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/ProbabilisticTheory/Classical/Basic.lean#L97).

```lean
lemma smul_apply (c : ℝ) (f : Observables (classical S)) (x : X) :
    (c • f) x = c * f x
```

**`ProbabilisticTheory.Classical.mul_apply`**, a lemma, [line 102](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/ProbabilisticTheory/Classical/Basic.lean#L102).

> The product of two observables multiplies their values.

```lean
lemma mul_apply (f g : Observables (classical S)) (x : X) : (f * g) x = f x * g x
```

**`ProbabilisticTheory.Classical.pow_apply`**, a lemma, [line 106](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/ProbabilisticTheory/Classical/Basic.lean#L106).

```lean
lemma pow_apply (f : Observables (classical S)) (n : ℕ) (x : X) :
    (f ^ n) x = f x ^ n
```

**`ProbabilisticTheory.Classical.le_def`**, a lemma, [line 111](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/ProbabilisticTheory/Classical/Basic.lean#L111).

> Observables are ordered by their values.

```lean
lemma le_def {f g : Observables (classical S)} : f ≤ g ↔ ∀ x, f x ≤ g x
```

**`ProbabilisticTheory.Classical.sq_nonneg'`**, a lemma, [line 115](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/ProbabilisticTheory/Classical/Basic.lean#L115).

> The square of an observable is positive.

```lean
lemma sq_nonneg' (f : Observables (classical S)) : 0 ≤ f ^ 2
```

## Depends on

- [The pointwise star order on bounded functions](../../mathematics/formathlib/part-01/lpstarorder.md)
- [The observables of a C⋆-algebra (Physlib)](../cstaralgebra/basic.md)

## Sources

- [Physlib/ProbabilisticTheory/Classical/Basic.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/ProbabilisticTheory/Classical/Basic.lean)
