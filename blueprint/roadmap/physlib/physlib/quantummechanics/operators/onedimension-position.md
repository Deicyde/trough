---
declaration: module
origin: cited
lean: QuantumMechanics.OneDimension.positionOperator, QuantumMechanics.OneDimension.positionOperatorSchwartz, QuantumMechanics.OneDimension.positionOperatorSchwartz_apply_fun, QuantumMechanics.OneDimension.positionOperatorSchwartz_apply, QuantumMechanics.OneDimension.positionOperatorUnbounded, QuantumMechanics.OneDimension.positionStates_generalized_eigenvector_positionOperatorUnbounded, QuantumMechanics.OneDimension.positionOperatorUnbounded_isSymmetric
statement: formalized
proof: formalized
---

# Position operator

The module `Physlib.QuantumMechanics.Operators.OneDimension.Position`, [Physlib/QuantumMechanics/Operators/OneDimension/Position.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/OneDimension/Position.lean): 7 declarations, 3 with a docstring.

> In this module we define:
> - The position operator on functions `ℝ → ℂ`
> - The position operator on Schwartz maps as an unbounded operator on the Hilbert space.
>
> We show that position wavefunctions are generalized eigenvectors of the position operator.

## The position operator on functions `ℝ → ℂ`

**`QuantumMechanics.OneDimension.positionOperator`**, a def, [line 42](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/OneDimension/Position.lean#L42).

> The position operator is defined as the linear map from `ℝ → ℂ` to `ℝ → ℂ` taking
> `ψ` to `x * ψ`.

```lean
def positionOperator : (ℝ → ℂ) →ₗ[ℂ] ℝ → ℂ
```

## The position operator on Schwartz maps

**`QuantumMechanics.OneDimension.positionOperatorSchwartz`**, a def, [line 64](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/OneDimension/Position.lean#L64).

> The position operator on the Schwartz maps is defined as the linear map from
> `𝓢(ℝ, ℂ)` to itself, such that `ψ` is taken to `fun x => x * ψ x`.

```lean
def positionOperatorSchwartz : 𝓢(ℝ, ℂ) →L[ℂ] 𝓢(ℝ, ℂ)
```

**`QuantumMechanics.OneDimension.positionOperatorSchwartz_apply_fun`**, a lemma, [line 66](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/OneDimension/Position.lean#L66).

```lean
lemma positionOperatorSchwartz_apply_fun (ψ : 𝓢(ℝ, ℂ)) :
    (positionOperatorSchwartz ψ) = fun x => x * ψ x
```

**`QuantumMechanics.OneDimension.positionOperatorSchwartz_apply`**, a lemma, [line 72](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/OneDimension/Position.lean#L72).

```lean
lemma positionOperatorSchwartz_apply (ψ : 𝓢(ℝ, ℂ)) (x : ℝ) :
    (positionOperatorSchwartz ψ) x = x * ψ x
```

**`QuantumMechanics.OneDimension.positionOperatorUnbounded`**, a def, [line 78](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/OneDimension/Position.lean#L78).

> The unbounded position operator, whose domain is Schwartz maps.

```lean
def positionOperatorUnbounded : UnboundedOperator schwartzIncl schwartzIncl_injective
```

## Generalized eigenvectors of the position operator

**`QuantumMechanics.OneDimension.positionStates_generalized_eigenvector_positionOperatorUnbounded`**, a lemma, [line 87](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/OneDimension/Position.lean#L87).

```lean
lemma positionStates_generalized_eigenvector_positionOperatorUnbounded (x : ℝ) :
    positionOperatorUnbounded.IsGeneralizedEigenvector (positionState x) x
```

## Position operator is symmetric

**`QuantumMechanics.OneDimension.positionOperatorUnbounded_isSymmetric`**, a lemma, [line 100](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/OneDimension/Position.lean#L100).

```lean
lemma positionOperatorUnbounded_isSymmetric :
    positionOperatorUnbounded.IsSymmetric
```

## Depends on

- [Physlib.Mathematics.Distribution.PowMul](../../mathematics/distribution/powmul.md)
- [Position states (OneDimension/PositionStates)](../hilbertspaces/onedimension-positionstates.md)
- [Schwartz submodule of the Hilbert space](../hilbertspaces/onedimension-schwartzsubmodule.md)
- [Unbounded operators (OneDimension/Unbounded)](onedimension-unbounded.md)

## Sources

- [Physlib/QuantumMechanics/Operators/OneDimension/Position.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/OneDimension/Position.lean)
