---
declaration: module
origin: cited
lean: QuantumMechanics.OneDimension.momentumOperator, QuantumMechanics.OneDimension.momentumOperator_eq_smul, QuantumMechanics.OneDimension.continuous_momentumOperator, QuantumMechanics.OneDimension.momentumOperator_smul, QuantumMechanics.OneDimension.momentumOperator_add, QuantumMechanics.OneDimension.momentumOperatorSchwartz, QuantumMechanics.OneDimension.momentumOperatorSchwartz_apply, QuantumMechanics.OneDimension.momentumOperatorUnbounded
statement: formalized
proof: formalized
---

# Momentum operator

The module `Physlib.QuantumMechanics.Operators.OneDimension.Momentum`, [Physlib/QuantumMechanics/Operators/OneDimension/Momentum.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/OneDimension/Momentum.lean): 10 declarations, 3 with a docstring.

> In this module we define:
> - The momentum operator on functions `ℝ → ℂ`
> - The momentum operator on Schwartz maps as an unbounded operator on the Hilbert space.
>
> We show that plane waves are generalized eigenvectors of the momentum operator.

## The momentum operator on functions `ℝ → ℂ`

**`QuantumMechanics.OneDimension.momentumOperator`**, a def, [line 43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/OneDimension/Momentum.lean#L43).

> The momentum operator is defined as the map from `ℝ → ℂ` to `ℝ → ℂ` taking
> `ψ` to `- i ℏ ψ'`.

```lean
def momentumOperator (ψ : ℝ → ℂ) : ℝ → ℂ
```

**`QuantumMechanics.OneDimension.momentumOperator_eq_smul`**, a lemma, [line 45](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/OneDimension/Momentum.lean#L45).

```lean
lemma momentumOperator_eq_smul (ψ : ℝ → ℂ) :
    momentumOperator ψ = fun x => (- Complex.I * ℏ) • deriv ψ x
```

**`QuantumMechanics.OneDimension.continuous_momentumOperator`**, a lemma, [line 50](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/OneDimension/Momentum.lean#L50).

```lean
lemma continuous_momentumOperator (ψ : ℝ → ℂ) (hψ : ContDiff ℝ 1 ψ) :
    Continuous (momentumOperator ψ)
```

**`QuantumMechanics.OneDimension.momentumOperator_smul`**, a lemma, [line 55](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/OneDimension/Momentum.lean#L55).

```lean
lemma momentumOperator_smul {ψ : ℝ → ℂ} (hψ : Differentiable ℝ ψ) (c : ℂ) :
    momentumOperator (c • ψ) = c • momentumOperator ψ
```

**`QuantumMechanics.OneDimension.momentumOperator_add`**, a lemma, [line 61](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/OneDimension/Momentum.lean#L61).

```lean
lemma momentumOperator_add {ψ1 ψ2 : ℝ → ℂ}
    (hψ1 : Differentiable ℝ ψ1) (hψ2 : Differentiable ℝ ψ2) :
    momentumOperator (ψ1 + ψ2) = momentumOperator ψ1 + momentumOperator ψ2
```

## The momentum operator on Schwartz maps

**`QuantumMechanics.OneDimension.momentumOperatorSchwartz`**, a def, [line 77](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/OneDimension/Momentum.lean#L77).

> The parity operator on the Schwartz maps is defined as the linear map from
> `𝓢(ℝ, ℂ)` to itself, such that `ψ` is taken to `fun x => - I ℏ * ψ' x`.

```lean
def momentumOperatorSchwartz : 𝓢(ℝ, ℂ) →L[ℂ] 𝓢(ℝ, ℂ)
```

**`QuantumMechanics.OneDimension.momentumOperatorSchwartz_apply`**, a lemma, [line 85](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/OneDimension/Momentum.lean#L85).

```lean
lemma momentumOperatorSchwartz_apply (ψ : 𝓢(ℝ, ℂ))
    (x : ℝ) : (momentumOperatorSchwartz ψ) x = (- Complex.I * ℏ) * (deriv ψ x)
```

**`QuantumMechanics.OneDimension.momentumOperatorUnbounded`**, a def, [line 91](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/OneDimension/Momentum.lean#L91).

> The unbounded momentum operator, whose domain is Schwartz maps.

```lean
def momentumOperatorUnbounded : UnboundedOperator schwartzIncl schwartzIncl_injective
```

## Generalized eigenvectors of the momentum operator

**`QuantumMechanics.OneDimension.planeWaveFunctional_generalized_eigenvector_momentumOperatorUnbounded`**, a lemma, [line 100](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/OneDimension/Momentum.lean#L100).

```lean
lemma planeWaveFunctional_generalized_eigenvector_momentumOperatorUnbounded (k : ℝ) :
    momentumOperatorUnbounded.IsGeneralizedEigenvector
      (planewaveFunctional k) (2 * Real.pi * ℏ * k)
```

## The momentum operator is symmetric

**`QuantumMechanics.OneDimension.momentumOperatorUnbounded_isSymmetric`**, a lemma, [line 125](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/OneDimension/Momentum.lean#L125).

```lean
lemma momentumOperatorUnbounded_isSymmetric : momentumOperatorUnbounded.IsSymmetric
```

## Depends on

- [Plane waves](../hilbertspaces/onedimension-planewaves.md)
- [Schwartz submodule of the Hilbert space](../hilbertspaces/onedimension-schwartzsubmodule.md)
- [Unbounded operators (OneDimension/Unbounded)](onedimension-unbounded.md)
- [Planck's constant](../planckconstant.md)

## Sources

- [Physlib/QuantumMechanics/Operators/OneDimension/Momentum.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/OneDimension/Momentum.lean)
