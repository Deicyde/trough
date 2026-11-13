---
declaration: module
origin: cited
lean: QuantumMechanics.OneDimension.HilbertSpace.positionState, QuantumMechanics.OneDimension.HilbertSpace.positionState_apply, QuantumMechanics.OneDimension.HilbertSpace.eq_of_eq_positionState
statement: formalized
proof: formalized
---

# Position states

The module `Physlib.QuantumMechanics.HilbertSpaces.OneDimension.PositionStates`, [Physlib/QuantumMechanics/HilbertSpaces/OneDimension/PositionStates.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/OneDimension/PositionStates.lean): 3 declarations, 2 with a docstring.

> We define position state as a member of the dual of the Schwartz submodule of the 1d Hilbert space.
>
> This module has been generalized to d-dimensions in
> `QuantumMechanics/HilbertSpaces/SpaceD/PositionStates.lean` and will be removed in the near future.

**`QuantumMechanics.OneDimension.HilbertSpace.positionState`**, a def, [line 32](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/OneDimension/PositionStates.lean#L32).

> Position state as a member of the dual of the
> Schwartz submodule of the Hilbert space.

```lean
def positionState (x : ℝ) : 𝓢(ℝ, ℂ) →L[ℂ] ℂ
```

**`QuantumMechanics.OneDimension.HilbertSpace.positionState_apply`**, a lemma, [line 34](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/OneDimension/PositionStates.lean#L34).

```lean
lemma positionState_apply (x : ℝ) (ψ : 𝓢(ℝ, ℂ)) :
    positionState x ψ = ψ x
```

**`QuantumMechanics.OneDimension.HilbertSpace.eq_of_eq_positionState`**, a lemma, [line 39](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/OneDimension/PositionStates.lean#L39).

> Two elements of the `𝓢(ℝ, ℂ)` are equal if they
> are equal on all position states.

```lean
lemma eq_of_eq_positionState {ψ1 ψ2 : 𝓢(ℝ, ℂ)}
    (h : ∀ x, positionState x ψ1 = positionState x ψ2) :
    ψ1 = ψ2
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [Physlib/QuantumMechanics/HilbertSpaces/OneDimension/PositionStates.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/OneDimension/PositionStates.lean)
