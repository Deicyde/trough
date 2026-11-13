---
declaration: module
origin: cited
lean: ProbabilisticTheory.QuasiLocal.sumSq, ProbabilisticTheory.AlgState.normSq_le, ProbabilisticTheory.QuasiLocal.AlgebraNet.IsLocallyBounded, ProbabilisticTheory.AlgState.nonneg_of_mem_sumSq, ProbabilisticTheory.QuasiLocal.AlgebraNet.norm_sq_le, ProbabilisticTheory.QuasiLocal.localSeq, ProbabilisticTheory.QuasiLocal.localSeq_eq, ProbabilisticTheory.QuasiLocal.exists_tendsto_localSeq
statement: formalized
proof: formalized
---

# Limit states of the quasi-local algebra

The module `PhyslibAlpha.ProbabilisticTheory.QuasiLocal.Limit`, [PhyslibAlpha/ProbabilisticTheory/QuasiLocal/Limit.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/QuasiLocal/Limit.lean): 13 declarations, 11 with a docstring.

> A net of local states, one for each finite region, has limit points that are states of the
> quasi-local algebra.

## i. Overview

> Let `ω_Λ` be a state of the algebra of the finite region `Λ`, for every `Λ`. The expectation value
> of a fixed local observable `a`, taken in the larger and larger regions `Λ`, is a net of complex
> numbers. If every local observable has a bounded such net, the net has a limit along every
> ultrafilter finer than the filter of large regions, by compactness of closed balls in `ℂ`. The
> limits are compatible, normalized, Hermitian and positive, so they form a `LocalStateFamily`, and
> hence a state of the quasi-local algebra.
>
> Boundedness is expressed without any norm: an observable `a` is *locally bounded* if some
> multiple `c · 1` of the identity exceeds `a* a` by a sum of squares. In a matrix algebra this
> holds with `c = ‖a‖²`. Each state then satisfies `|ω(a)|² ≤ ω(a* a) ≤ c`, by the Cauchy–Schwarz
> inequality for states.
>
> Nothing is assumed about the nature of the local states: they may be Gibbs states with any
> boundary condition. Different ultrafilters can give different limit states, which is how phase
> coexistence appears.

## ii. Key results

> - `AlgState.normSq_le` : the Cauchy–Schwarz inequality `|ω(a)|² ≤ ω(a* a)`.
> - `AlgebraNet.IsLocallyBounded` : every local observable is bounded by a multiple of the identity.
> - `limitFamily` : the ultrafilter limit of a net of local states, as a compatible family.
> - `limitState` : the limit state of the quasi-local algebra.
> - `limitState_of` : its value on a local observable is the limit of the local expectations.

## iv. References

> * O. Bratteli & D. Robinson, Operator Algebras and Quantum Statistical Mechanics 2,
>   Section 6.2.3 (existence of limit Gibbs states by weak-⋆ compactness).

## A. The Cauchy–Schwarz inequality and sums of squares

**`ProbabilisticTheory.QuasiLocal.sumSq`**, a def, [line 74](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/QuasiLocal/Limit.lean#L74).

> The sums of squares `∑ s_i* s_i` of a `*`-algebra.

```lean
def sumSq (A : Type*) [Ring A] [StarRing A] : AddSubmonoid A
```

**`ProbabilisticTheory.AlgState.normSq_le`**, a lemma, [line 78](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/QuasiLocal/Limit.lean#L78).

> **The Cauchy–Schwarz inequality for states**: `|ω(a)|² ≤ ω(a* a)`.

```lean
lemma _root_.ProbabilisticTheory.AlgState.normSq_le (ω : AlgState A) (a : A) :
    ((‖ω a‖ ^ 2 : ℝ) : ℂ) ≤ ω (star a * a)
```

## B. Local boundedness

**`ProbabilisticTheory.QuasiLocal.AlgebraNet.IsLocallyBounded`**, a def, [line 111](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/QuasiLocal/Limit.lean#L111).

> **Local boundedness**: for every local observable `a` some multiple `c · 1` of the identity
> exceeds `a* a` by a sum of squares.

```lean
def AlgebraNet.IsLocallyBounded : Prop
```

**`ProbabilisticTheory.AlgState.nonneg_of_mem_sumSq`**, a lemma, [line 118](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/QuasiLocal/Limit.lean#L118).

> A state is nonnegative on sums of squares.

```lean
lemma _root_.ProbabilisticTheory.AlgState.nonneg_of_mem_sumSq
    {A : Type*} [Ring A] [Algebra ℂ A] [StarRing A] [StarModule ℂ A] (ω : AlgState A)
    {p : A} (hp : p ∈ sumSq A) : 0 ≤ ω p
```

**`ProbabilisticTheory.QuasiLocal.AlgebraNet.norm_sq_le`**, a lemma, [line 128](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/QuasiLocal/Limit.lean#L128).

> **The expectation of a locally bounded observable in any larger region is bounded.**

```lean
lemma AlgebraNet.norm_sq_le (hb : N.IsLocallyBounded) {X Λ : Finset S} (h : X ≤ Λ)
    (ω : AlgState (N.A Λ)) (a : N.A X) :
    ∃ c : ℝ, ‖ω (N.incl h a)‖ ^ 2 ≤ c ∧ ∀ Λ' (h' : X ≤ Λ') (ω' : AlgState (N.A Λ')),
      ‖ω' (N.incl h' a)‖ ^ 2 ≤ c
```

## C. The ultrafilter limit

**`ProbabilisticTheory.QuasiLocal.localSeq`**, a def, [line 165](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/QuasiLocal/Limit.lean#L165).

> The expectation of a local observable `a` of the region `X` in the region `Λ`, zero if `Λ`
> does not contain `X`.

```lean
def localSeq (X : Finset S) (a : N.A X) (Λ : Finset S) : ℂ
```

**`ProbabilisticTheory.QuasiLocal.localSeq_eq`**, a lemma, [line 168](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/QuasiLocal/Limit.lean#L168).

```lean
lemma localSeq_eq (X : Finset S) (a : N.A X) {Λ : Finset S} (h : X ≤ Λ) :
    localSeq ω X a Λ = ω Λ (N.incl h a)
```

**`ProbabilisticTheory.QuasiLocal.exists_tendsto_localSeq`**, a lemma, [line 174](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/QuasiLocal/Limit.lean#L174).

> The expectations of a local observable have a limit along a fine ultrafilter.

```lean
lemma exists_tendsto_localSeq (hb : N.IsLocallyBounded) (h𝒰 : (𝒰 : Filter (Finset S)) ≤ atTop)
    (X : Finset S) (a : N.A X) : ∃ z, Tendsto (localSeq ω X a) 𝒰 (𝓝 z)
```

**`ProbabilisticTheory.QuasiLocal.limitValue`**, a def, [line 191](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/QuasiLocal/Limit.lean#L191).

> The limit along the ultrafilter of the expectations of a local observable.

```lean
def limitValue (X : Finset S) (a : N.A X) : ℂ
```

**`ProbabilisticTheory.QuasiLocal.tendsto_limitValue`**, a lemma, [line 194](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/QuasiLocal/Limit.lean#L194).

```lean
lemma tendsto_limitValue (X : Finset S) (a : N.A X) :
    Tendsto (localSeq ω X a) 𝒰 (𝓝 (limitValue ω hb h𝒰 X a))
```

**`ProbabilisticTheory.QuasiLocal.limitFamily`**, a def, [line 200](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/QuasiLocal/Limit.lean#L200).

> **The limit of a net of local states along an ultrafilter** is a compatible family of local
> states.

```lean
def limitFamily : LocalStateFamily N
```

**`ProbabilisticTheory.QuasiLocal.limitState`**, a def, [line 242](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/QuasiLocal/Limit.lean#L242).

> **The limit state** of a net of local states along an ultrafilter: a state of the
> quasi-local algebra.

```lean
def limitState : AlgState N.Quasilocal
```

**`ProbabilisticTheory.QuasiLocal.limitState_of`**, a lemma, [line 245](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/QuasiLocal/Limit.lean#L245).

> The limit state on a local observable is the limit of the local expectations.

```lean
lemma limitState_of (X : Finset S) (a : N.A X) :
    Tendsto (fun Λ => localSeq ω X a Λ) 𝒰 (𝓝 (limitState ω hb h𝒰 (N.of X a)))
```

## Depends on

- [States of the quasi-local algebra from compatible local states](state.md)

## Sources

- [PhyslibAlpha/ProbabilisticTheory/QuasiLocal/Limit.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/QuasiLocal/Limit.lean)
