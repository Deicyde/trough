---
declaration: module
origin: cited
lean: ProbabilisticTheory.FiniteClassicalSystem, ProbabilisticTheory.FiniteClassicalSystem.eval, ProbabilisticTheory.FiniteClassicalSystem.eval_apply, ProbabilisticTheory.FiniteClassicalSystem.apply_eq_sum, ProbabilisticTheory.FiniteClassicalSystem.dualEquiv, ProbabilisticTheory.FiniteClassicalSystem.dualEquiv_apply, ProbabilisticTheory.FiniteClassicalSystem.dualEquiv_symm_apply, ProbabilisticTheory.FiniteClassicalSystem.ofProbs
statement: formalized
proof: formalized
---

# Finite classical systems

The module `PhyslibAlpha.ProbabilisticTheory.Classical.FiniteSystem`, [PhyslibAlpha/ProbabilisticTheory/Classical/FiniteSystem.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/FiniteSystem.lean): 18 declarations (2 instances with no name), 10 with a docstring.

> The classical system with finitely many outcomes: states are probability vectors.

## i. Overview

> A classical system with finitely many outcomes `ι` has as observables the real functions on `ι`,
> ordered pointwise, with the constant function `1` as order unit. A state is then a probability
> distribution on the outcomes: it gives outcome `i` the probability `ω (Pi.single i 1)`. So the
> state space is the standard simplex, its pure states are the deterministic states reading off a
> single outcome, and every state is a mixture of them in exactly one way. This is what makes the
> system classical. The classical bit is `ι = Fin 2`.

## ii. Key results

> - `FiniteClassicalSystem ι` : the classical system with outcomes `ι`.
> - `FiniteClassicalSystem.stateEquiv` : the states are the probability vectors.
> - `FiniteClassicalSystem.isPure_iff` : the pure states are the point evaluations.
> - `FiniteClassicalSystem.isSimplex_algebraicStateSpace` : the state space is a simplex.

## iv. References

> * None.

## A. The order-unit space

**`ProbabilisticTheory.FiniteClassicalSystem`**, an abbrev, [line 57](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/FiniteSystem.lean#L57).

> The classical system with outcomes `ι`: real functions on `ι`, ordered pointwise.

```lean
abbrev FiniteClassicalSystem (ι : Type*) : Type _
```

**An instance with no name**, [line 63](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/FiniteSystem.lean#L63).

```lean
instance : OrderUnitSpace (FiniteClassicalSystem ι)
```

**An instance with no name**, [line 70](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/FiniteSystem.lean#L70).

```lean
instance : ArchimedeanOrderUnitSpace (FiniteClassicalSystem ι)
```

## B. States as probability vectors

**`ProbabilisticTheory.FiniteClassicalSystem.eval`**, a def, [line 83](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/FiniteSystem.lean#L83).

> The deterministic state reading off the outcome `i`.

```lean
def eval (i : ι) : 𝓢[ℝ, FiniteClassicalSystem ι]
```

**`ProbabilisticTheory.FiniteClassicalSystem.eval_apply`**, a lemma, [line 86](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/FiniteSystem.lean#L86).

```lean
lemma eval_apply (i : ι) (A : FiniteClassicalSystem ι) : eval i A = A i
```

**`ProbabilisticTheory.FiniteClassicalSystem.apply_eq_sum`**, a lemma, [line 91](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/FiniteSystem.lean#L91).

> A linear functional is determined by its values on the outcomes.

```lean
lemma apply_eq_sum (f : FiniteClassicalSystem ι →ₗ[ℝ] ℝ) (A : FiniteClassicalSystem ι) :
    f A = ∑ i, A i * f (Pi.single i 1)
```

**`ProbabilisticTheory.FiniteClassicalSystem.dualEquiv`**, a def, [line 100](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/FiniteSystem.lean#L100).

> A linear functional on a classical system is its vector of values on the outcomes.

```lean
def dualEquiv : (FiniteClassicalSystem ι →ₗ[ℝ] ℝ) ≃ₗ[ℝ] (ι → ℝ)
```

**`ProbabilisticTheory.FiniteClassicalSystem.dualEquiv_apply`**, a lemma, [line 109](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/FiniteSystem.lean#L109).

```lean
lemma dualEquiv_apply (f : FiniteClassicalSystem ι →ₗ[ℝ] ℝ) (i : ι) :
    dualEquiv f i = f (Pi.single i 1)
```

**`ProbabilisticTheory.FiniteClassicalSystem.dualEquiv_symm_apply`**, a lemma, [line 113](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/FiniteSystem.lean#L113).

```lean
lemma dualEquiv_symm_apply (p : ι → ℝ) (A : FiniteClassicalSystem ι) :
    dualEquiv.symm p A = ∑ i, p i * A i
```

**`ProbabilisticTheory.FiniteClassicalSystem.ofProbs`**, a def, [line 118](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/FiniteSystem.lean#L118).

> The state giving outcome `i` the probability `p i`.

```lean
def ofProbs (p : ι → ℝ) (hp : p ∈ stdSimplexSet ι) : 𝓢[ℝ, FiniteClassicalSystem ι]
```

**`ProbabilisticTheory.FiniteClassicalSystem.ofProbs_apply`**, a lemma, [line 124](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/FiniteSystem.lean#L124).

```lean
lemma ofProbs_apply (p : ι → ℝ) (hp : p ∈ stdSimplexSet ι) (A : FiniteClassicalSystem ι) :
    ofProbs p hp A = ∑ i, p i * A i
```

**`ProbabilisticTheory.FiniteClassicalSystem.image_algebraicStateSpace`**, a lemma, [line 129](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/FiniteSystem.lean#L129).

> The probability vectors are the images of the states.

```lean
lemma image_algebraicStateSpace :
    dualEquiv '' algebraicStateSpace (E := FiniteClassicalSystem ι) = stdSimplexSet ι
```

**`ProbabilisticTheory.FiniteClassicalSystem.stateEquiv`**, a def, [line 140](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/FiniteSystem.lean#L140).

> The states of a classical system are the probability vectors.

```lean
noncomputable def stateEquiv : 𝓢[ℝ, FiniteClassicalSystem ι] ≃ stdSimplexSet ι
```

**`ProbabilisticTheory.FiniteClassicalSystem.stateEquiv_apply`**, a lemma, [line 148](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/FiniteSystem.lean#L148).

```lean
lemma stateEquiv_apply (ω : 𝓢[ℝ, FiniteClassicalSystem ι]) (i : ι) :
    (stateEquiv ω : ι → ℝ) i = ω (Pi.single i 1)
```

## C. The simplex of states

**`ProbabilisticTheory.FiniteClassicalSystem.dualEquiv_eval`**, a lemma, [line 157](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/FiniteSystem.lean#L157).

```lean
lemma dualEquiv_eval (i : ι) : dualEquiv (eval i).toLinearMap = Pi.single i 1
```

**`ProbabilisticTheory.FiniteClassicalSystem.isPure_iff`**, a lemma, [line 163](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/FiniteSystem.lean#L163).

> The pure states are the deterministic states.

```lean
lemma isPure_iff {ω : 𝓢[ℝ, FiniteClassicalSystem ι]} : ω.IsPure ↔ ∃ i, ω = eval i
```

**`ProbabilisticTheory.FiniteClassicalSystem.isSimplex_algebraicStateSpace`**, a lemma, [line 171](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/FiniteSystem.lean#L171).

> **Classical systems are classical**: the state space is a simplex, so every state is a
> mixture of the deterministic states in exactly one way.

```lean
lemma isSimplex_algebraicStateSpace :
    IsSimplex (algebraicStateSpace (E := FiniteClassicalSystem ι))
```

## D. Effects of `ℝ`

**`ProbabilisticTheory.Effect.isSharp_iff_eq_zero_or_eq_one`**, a lemma, [line 184](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/FiniteSystem.lean#L184).

> The sharp effects of `ℝ` are `0` and `1`.

```lean
lemma Effect.isSharp_iff_eq_zero_or_eq_one {e : Effect ℝ} :
    Effect.IsSharp e ↔ (e : ℝ) = 0 ∨ (e : ℝ) = 1
```

## Depends on

- [Sharp effects](../../../physlib/probabilistictheory/effect/sharp.md)
- [Simplices](../../mathematics/part-02/geometry/simplex.md)
- [Convex state spaces](../state/convex.md)

## Sources

- [PhyslibAlpha/ProbabilisticTheory/Classical/FiniteSystem.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/FiniteSystem.lean)
