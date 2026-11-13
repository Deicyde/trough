---
declaration: module
origin: cited
lean: QuantumMechanics.OneDimension.positionOperatorSchwartz_commutation_momentumOperatorSchwartz, QuantumMechanics.OneDimension.positionOperatorSchwartz_momentumOperatorSchwartz_eq, QuantumMechanics.OneDimension.momentumOperatorSchwartz_positionOperatorSchwartz_eq
statement: formalized
proof: formalized
---

# Commutation relations (OneDimension/Commutation)

The module `Physlib.QuantumMechanics.Operators.OneDimension.Commutation`, [Physlib/QuantumMechanics/Operators/OneDimension/Commutation.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/OneDimension/Commutation.lean): 3 declarations, 0 with a docstring.

> The commutation relations between different operators.

## Commutation relation between position and momentum operators

**`QuantumMechanics.OneDimension.positionOperatorSchwartz_commutation_momentumOperatorSchwartz`**, a lemma, [line 34](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/OneDimension/Commutation.lean#L34).

```lean
lemma positionOperatorSchwartz_commutation_momentumOperatorSchwartz
    (ψ : 𝓢(ℝ, ℂ)) : positionOperatorSchwartz (momentumOperatorSchwartz ψ)
    - momentumOperatorSchwartz (positionOperatorSchwartz ψ)
    = (Complex.I * ℏ) • ψ
```

**`QuantumMechanics.OneDimension.positionOperatorSchwartz_momentumOperatorSchwartz_eq`**, a lemma, [line 47](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/OneDimension/Commutation.lean#L47).

```lean
lemma positionOperatorSchwartz_momentumOperatorSchwartz_eq (ψ : 𝓢(ℝ, ℂ)) :
    positionOperatorSchwartz (momentumOperatorSchwartz ψ)
    = momentumOperatorSchwartz (positionOperatorSchwartz ψ)
    + (Complex.I * ℏ) • ψ
```

**`QuantumMechanics.OneDimension.momentumOperatorSchwartz_positionOperatorSchwartz_eq`**, a lemma, [line 53](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/OneDimension/Commutation.lean#L53).

```lean
lemma momentumOperatorSchwartz_positionOperatorSchwartz_eq (ψ : 𝓢(ℝ, ℂ)) :
    momentumOperatorSchwartz (positionOperatorSchwartz ψ)
    = positionOperatorSchwartz (momentumOperatorSchwartz ψ)
    - (Complex.I * ℏ) • ψ
```

## Depends on

- [Momentum operator](onedimension-momentum.md)
- [Position operator](onedimension-position.md)

## Sources

- [Physlib/QuantumMechanics/Operators/OneDimension/Commutation.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/OneDimension/Commutation.lean)
