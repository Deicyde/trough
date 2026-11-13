---
declaration: module
origin: cited
lean: QuantumMechanics.OneDimension.HilbertSpace.parityOperator, QuantumMechanics.OneDimension.HilbertSpace.parityOperatorSchwartz, QuantumMechanics.OneDimension.HilbertSpace.parityOperatorUnbounded, QuantumMechanics.OneDimension.HilbertSpace.parityOperatorSchwartz_parityOperatorSchwartz, QuantumMechanics.OneDimension.HilbertSpace.parityOperatorUnbounded_isSymmetric
statement: formalized
proof: formalized
---

# Parity operator

The module `Physlib.QuantumMechanics.Operators.OneDimension.Parity`, [Physlib/QuantumMechanics/Operators/OneDimension/Parity.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/OneDimension/Parity.lean): 5 declarations, 3 with a docstring.

## The parity operator on functions

**`QuantumMechanics.OneDimension.HilbertSpace.parityOperator`**, a def, [line 36](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/OneDimension/Parity.lean#L36).

> The parity operator is defined as linear map from `ℝ → ℂ` to itself, such that
> `ψ` is taken to `fun x => ψ (-x)`.

```lean
def parityOperator : (ℝ → ℂ) →ₗ[ℂ] (ℝ → ℂ)
```

## The parity operator on Schwartz maps

**`QuantumMechanics.OneDimension.HilbertSpace.parityOperatorSchwartz`**, a def, [line 53](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/OneDimension/Parity.lean#L53).

> The parity operator on the Schwartz maps is defined as the linear map from
> `𝓢(ℝ, ℂ)` to itself, such that `ψ` is taken to `fun x => ψ (-x)`.

```lean
def parityOperatorSchwartz : 𝓢(ℝ, ℂ) →L[ℂ] 𝓢(ℝ, ℂ)
```

**`QuantumMechanics.OneDimension.HilbertSpace.parityOperatorUnbounded`**, a def, [line 85](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/OneDimension/Parity.lean#L85).

> The unbounded parity operator, whose domain is Schwartz maps.

```lean
def parityOperatorUnbounded : UnboundedOperator schwartzIncl schwartzIncl_injective
```

**`QuantumMechanics.OneDimension.HilbertSpace.parityOperatorSchwartz_parityOperatorSchwartz`**, a lemma, [line 89](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/OneDimension/Parity.lean#L89).

```lean
lemma parityOperatorSchwartz_parityOperatorSchwartz (ψ : 𝓢(ℝ, ℂ)) :
    parityOperatorSchwartz (parityOperatorSchwartz ψ) = ψ
```

## Parity operator is symmetric

**`QuantumMechanics.OneDimension.HilbertSpace.parityOperatorUnbounded_isSymmetric`**, a lemma, [line 103](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/OneDimension/Parity.lean#L103).

```lean
lemma parityOperatorUnbounded_isSymmetric :
    parityOperatorUnbounded.IsSymmetric
```

## Depends on

- [Schwartz submodule of the Hilbert space](../hilbertspaces/onedimension-schwartzsubmodule.md)
- [Unbounded operators](onedimension-unbounded.md)

## Sources

- [Physlib/QuantumMechanics/Operators/OneDimension/Parity.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/OneDimension/Parity.lean)
