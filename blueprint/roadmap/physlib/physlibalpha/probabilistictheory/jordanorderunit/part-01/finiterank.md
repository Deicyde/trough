---
declaration: module
origin: cited
lean: ProbabilisticTheory.JordanAlgebra.TraceDeterminant, ProbabilisticTheory.JordanAlgebra.TraceDeterminant.states, ProbabilisticTheory.JordanAlgebra.TraceDeterminant.pureStates, ProbabilisticTheory.JordanAlgebra.TraceDeterminant.expectation, ProbabilisticTheory.JordanAlgebra.TraceDeterminant.expectation_apply, ProbabilisticTheory.JordanAlgebra.TraceDeterminant.sq_smul_isSumSq, ProbabilisticTheory.JordanAlgebra.TraceDeterminant.sq_smul_add_sq_smul_mem_states, ProbabilisticTheory.JordanAlgebra.TraceDeterminant.expectation_sq_smul_add_sq_smul
statement: formalized
proof: formalized
---

# Trace and determinant of finite-rank Jordan algebras

The module `PhyslibAlpha.ProbabilisticTheory.JordanOrderUnit.FiniteRank`, [PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/FiniteRank.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/FiniteRank.lean): 8 declarations, 7 with a docstring.

> Traces on formally real Jordan algebras, their density observables and expectations.

## i. Overview

> A trace on a formally real Jordan algebra gives density observables: sums of squares with trace one,
> each defining the expectation `a ↦ tr(ρ ∘ a)`.

## ii. Key results

> - `JordanAlgebra.TraceDeterminant` : a trace and determinant on a Jordan algebra.
> - `JordanAlgebra.TraceDeterminant.states` : the density observables.
> - `JordanAlgebra.TraceDeterminant.expectation` : the expectation of a density observable.
> - `JordanAlgebra.TraceDeterminant.pureStates` : the idempotent density observables.
> - `JordanAlgebra.TraceDeterminant.sq_smul_add_sq_smul_mem_states` : square-weighted mixtures of
>   density observables are density observables.

## iv. References

> * None.

## A. Trace and determinant

**`ProbabilisticTheory.JordanAlgebra.TraceDeterminant`**, a structure, [line 58](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/FiniteRank.lean#L58).

> A trace and a determinant on a formally real Jordan algebra.

```lean
structure TraceDeterminant (E : Type*) [NonAssocCommRing E] [Module ℝ E] where
  /-- Jordan rank, i.e. determinant degree and trace of the unit. -/
  rank : ℕ
  /-- The generic trace. -/
  trace : E →ₗ[ℝ] ℝ
  /-- The generic determinant. -/
  determinant : E → ℝ
  determinant_smul : ∀ (r : ℝ) (x : E), determinant (r • x) = r ^ rank * determinant x
  trace_one : trace 1 = rank
  determinant_one : determinant 1 = 1
```

## B. Density observables and expectations

**`ProbabilisticTheory.JordanAlgebra.TraceDeterminant.states`**, a def, [line 78](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/FiniteRank.lean#L78).

> The finite-rank density-observable base: sums of Jordan squares with trace one.

```lean
def states (τ : TraceDeterminant E) : Set E
```

**`ProbabilisticTheory.JordanAlgebra.TraceDeterminant.pureStates`**, a def, [line 82](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/FiniteRank.lean#L82).

> A pure finite-rank density observable is an idempotent density observable.

```lean
def pureStates (τ : TraceDeterminant E) : Set E
```

**`ProbabilisticTheory.JordanAlgebra.TraceDeterminant.expectation`**, a def, [line 86](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/FiniteRank.lean#L86).

> Expectation in a finite-rank density observable.

```lean
def expectation (τ : TraceDeterminant E) (ρ : τ.states) : E →ₗ[ℝ] ℝ
```

**`ProbabilisticTheory.JordanAlgebra.TraceDeterminant.expectation_apply`**, a lemma, [line 92](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/FiniteRank.lean#L92).

```lean
lemma expectation_apply (τ : TraceDeterminant E) (ρ : τ.states) (a : E) :
    τ.expectation ρ a = τ.trace ((ρ : E) * a)
```

**`ProbabilisticTheory.JordanAlgebra.TraceDeterminant.sq_smul_isSumSq`**, a lemma, [line 97](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/FiniteRank.lean#L97).

> Square scalar weights preserve the sum-of-squares cone.

```lean
lemma sq_smul_isSumSq {x : E} (hx : IsSumSq x) (r : ℝ) : IsSumSq ((r * r) • x)
```

**`ProbabilisticTheory.JordanAlgebra.TraceDeterminant.sq_smul_add_sq_smul_mem_states`**, a lemma, [line 109](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/FiniteRank.lean#L109).

> Square-weighted mixtures remain finite-rank density observables.

```lean
lemma sq_smul_add_sq_smul_mem_states (τ : TraceDeterminant E)
    {ρ σ : E} (hρ : ρ ∈ τ.states) (hσ : σ ∈ τ.states)
    {r s : ℝ} (hrs : r * r + s * s = 1) :
    (r * r) • ρ + (s * s) • σ ∈ τ.states
```

**`ProbabilisticTheory.JordanAlgebra.TraceDeterminant.expectation_sq_smul_add_sq_smul`**, a lemma, [line 119](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/FiniteRank.lean#L119).

> Expectations respect square-weighted finite-rank mixtures.

```lean
lemma expectation_sq_smul_add_sq_smul (τ : TraceDeterminant E)
    {ρ σ : E} (hρ : ρ ∈ τ.states) (hσ : σ ∈ τ.states)
    {r s : ℝ} (hrs : r * r + s * s = 1) (a : E) :
    τ.expectation ⟨(r * r) • ρ + (s * s) • σ,
      τ.sq_smul_add_sq_smul_mem_states hρ hσ hrs⟩ a =
      (r * r) * τ.expectation ⟨ρ, hρ⟩ a + (s * s) * τ.expectation ⟨σ, hσ⟩ a
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/FiniteRank.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/FiniteRank.lean)
