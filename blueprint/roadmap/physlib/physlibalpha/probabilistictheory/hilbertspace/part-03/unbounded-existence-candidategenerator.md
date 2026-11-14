---
declaration: module
origin: cited
lean: ProbabilisticTheory.QuantumMechanics.stoneCandidateDomainPred, ProbabilisticTheory.QuantumMechanics.stoneCandidateDomainPred_add, ProbabilisticTheory.QuantumMechanics.stoneCandidateDomainPred_smul, ProbabilisticTheory.QuantumMechanics.stoneCandidateDomainPred_zero, ProbabilisticTheory.QuantumMechanics.stoneCandidateDomain, ProbabilisticTheory.QuantumMechanics.stoneCandidateDeriv, ProbabilisticTheory.QuantumMechanics.stoneCandidateDeriv_spec, ProbabilisticTheory.QuantumMechanics.stoneCandidateDeriv_add
statement: formalized
proof: formalized
---

# The candidate generator of a unitary group

The module `PhyslibAlpha.ProbabilisticTheory.HilbertSpace.Unbounded.Existence.CandidateGenerator`, [PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Existence/CandidateGenerator.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Existence/CandidateGenerator.lean): 13 declarations, 8 with a docstring.

> The candidate generator of a strongly continuous unitary group, and its symmetry.

## i. Overview

> For a strongly continuous one-parameter unitary group `U`, the candidate generator is defined on the
> vectors whose orbit `t ↦ U t ψ` is differentiable at `0`, and sends such a vector to `-i` times the
> derivative. It is a symmetric operator.

## ii. Key results

> - `stoneCandidateDomain` : the vectors whose orbit is differentiable at `0`.
> - `stoneCandidateGenerator` : the candidate generator.
> - `stoneCandidateGenerator_isSymmetric` : the candidate generator is symmetric.

## iv. References

> * None.

## A. The candidate domain

**`ProbabilisticTheory.QuantumMechanics.stoneCandidateDomainPred`**, a def, [line 66](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Existence/CandidateGenerator.lean#L66).

> A vector is in the domain of the candidate generator when its orbit is differentiable at `0`.

```lean
def stoneCandidateDomainPred (ψ : H) : Prop
```

**`ProbabilisticTheory.QuantumMechanics.stoneCandidateDomainPred_add`**, a lemma, [line 71](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Existence/CandidateGenerator.lean#L71).

> The candidate domain is closed under addition. The group law is an argument so that the
> domain is attached to a unitary group.

```lean
lemma stoneCandidateDomainPred_add (_hUmul : ∀ s t, U (s + t) = U s * U t) {ψ₁ ψ₂ : H}
    (h₁ : stoneCandidateDomainPred (U := U) ψ₁) (h₂ : stoneCandidateDomainPred (U := U) ψ₂) :
    stoneCandidateDomainPred (U := U) (ψ₁ + ψ₂)
```

**`ProbabilisticTheory.QuantumMechanics.stoneCandidateDomainPred_smul`**, a lemma, [line 82](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Existence/CandidateGenerator.lean#L82).

> The candidate domain is closed under scalar multiplication, by the same linearity argument.

```lean
lemma stoneCandidateDomainPred_smul {ψ : H} (c : ℂ)
    (h : stoneCandidateDomainPred (U := U) ψ) :
    stoneCandidateDomainPred (U := U) (c • ψ)
```

**`ProbabilisticTheory.QuantumMechanics.stoneCandidateDomainPred_zero`**, a lemma, [line 91](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Existence/CandidateGenerator.lean#L91).

```lean
lemma stoneCandidateDomainPred_zero : stoneCandidateDomainPred (U := U) (0 : H)
```

**`ProbabilisticTheory.QuantumMechanics.stoneCandidateDomain`**, a def, [line 96](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Existence/CandidateGenerator.lean#L96).

> The domain of the candidate generator of the unitary group `U`, as a submodule.

```lean
def stoneCandidateDomain : Submodule ℂ H
```

## B. The candidate generator

**`ProbabilisticTheory.QuantumMechanics.stoneCandidateDeriv`**, a def, [line 110](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Existence/CandidateGenerator.lean#L110).

> The derivative witness for a vector in the candidate domain, chosen once and for all via
> choice; `-Complex.I` times this is the candidate generator's action.

```lean
def stoneCandidateDeriv (ψ : stoneCandidateDomain (U := U) hUmul) : H
```

**`ProbabilisticTheory.QuantumMechanics.stoneCandidateDeriv_spec`**, a lemma, [line 114](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Existence/CandidateGenerator.lean#L114).

```lean
lemma stoneCandidateDeriv_spec (ψ : stoneCandidateDomain (U := U) hUmul) :
    HasDerivAt (fun t : ℝ => U t (ψ : H)) (stoneCandidateDeriv hUmul ψ) 0
```

**`ProbabilisticTheory.QuantumMechanics.stoneCandidateDeriv_add`**, a lemma, [line 119](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Existence/CandidateGenerator.lean#L119).

```lean
lemma stoneCandidateDeriv_add (ψ₁ ψ₂ : stoneCandidateDomain (U := U) hUmul) :
    stoneCandidateDeriv hUmul (ψ₁ + ψ₂) =
      stoneCandidateDeriv hUmul ψ₁ + stoneCandidateDeriv hUmul ψ₂
```

**`ProbabilisticTheory.QuantumMechanics.stoneCandidateDeriv_smul`**, a lemma, [line 130](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Existence/CandidateGenerator.lean#L130).

```lean
lemma stoneCandidateDeriv_smul (c : ℂ) (ψ : stoneCandidateDomain (U := U) hUmul) :
    stoneCandidateDeriv hUmul (c • ψ) = c • stoneCandidateDeriv hUmul ψ
```

**`ProbabilisticTheory.QuantumMechanics.stoneCandidateLinearMap`**, a def, [line 139](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Existence/CandidateGenerator.lean#L139).

> The candidate generator as a linear map on its domain.

```lean
def stoneCandidateLinearMap :
    stoneCandidateDomain (U := U) hUmul →ₗ[ℂ] H
```

**`ProbabilisticTheory.QuantumMechanics.stoneCandidateGenerator`**, a def, [line 148](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Existence/CandidateGenerator.lean#L148).

> The candidate Stone generator: a `LinearPMap` whose domain is exactly the vectors along which
> `U`'s orbit is differentiable at `0`, sending such a vector to `-i` times that derivative.

```lean
def stoneCandidateGenerator : H →ₗ.[ℂ] H
```

**`ProbabilisticTheory.QuantumMechanics.stoneCandidateGenerator_apply`**, a lemma, [line 153](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Existence/CandidateGenerator.lean#L153).

```lean
lemma stoneCandidateGenerator_apply (ψ : (stoneCandidateGenerator (U := U) hUmul).domain) :
    stoneCandidateGenerator (U := U) hUmul ψ = (-Complex.I) • stoneCandidateDeriv hUmul ψ
```

## C. Symmetry of the candidate generator

**`ProbabilisticTheory.QuantumMechanics.stoneCandidateGenerator_isSymmetric`**, a lemma, [line 165](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Existence/CandidateGenerator.lean#L165).

> **The candidate generator is symmetric.** The inner product `⟪U t ψ₁, U t ψ₂⟫` is constant in
> `t`; differentiating at `0` gives the symmetry.

```lean
lemma stoneCandidateGenerator_isSymmetric :
    (stoneCandidateGenerator (U := U) hUmul).IsSymmetric
```

## Depends on

- [Unbounded operators (Operators/Unbounded)](../../../../physlib/quantummechanics/operators/unbounded.md)

## Sources

- [PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Existence/CandidateGenerator.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Existence/CandidateGenerator.lean)
