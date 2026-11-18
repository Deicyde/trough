---
declaration: module
origin: cited
lean: QuantumMechanics.SpaceDHilbertSpace.positionState, QuantumMechanics.SpaceDHilbertSpace.positionState_apply, QuantumMechanics.SpaceDHilbertSpace.eq_of_eq_positionState, QuantumMechanics.SpaceDHilbertSpace.positionState_comp_positionCLM
statement: formalized
proof: formalized
---

# Position states (SpaceD/PositionStates)

The module `Physlib.QuantumMechanics.HilbertSpaces.SpaceD.PositionStates`, [Physlib/QuantumMechanics/HilbertSpaces/SpaceD/PositionStates.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/SpaceD/PositionStates.lean): 4 declarations, 4 with a docstring.

## i. Overview

> Informally, the position "state" at `x : Space d` has a non-normalizable wavefunction which is
> a Dirac-delta function centered at `x`. More precisely, the position "state" lives in the \_rigged\_
> Hilbert space `𝓢(Space d, ℂ) < SpaceDHilbertSpace d μ < StrongDual ℂ 𝓢(Space d, ℂ)` as the element
> of the dual of `𝓢(Space d, ℂ)` defined by evaluation at `x`.

## ii. Key results

> - `positionState` : the position state as a member of the strong dual of the Schwartz space.
> - `positionState_comp_positionCLM` : the position state `positionState x` is a generalized
>   eigenvector of `𝐱 i` with eigenvalue `xᵢ`.

## iv. References

> * https://en.wikipedia.org/wiki/Rigged\_Hilbert\_space. [ref: wiki\_rigged\_hilbert\_space]

## A. Position states

**`QuantumMechanics.SpaceDHilbertSpace.positionState`**, a def, [line 58](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/SpaceD/PositionStates.lean#L58).

> Position state as a member of the strong dual of the Schwartz space.
>
> For a given `x` this corresponds to the non-normalizable wavefunction `ψ(y) = δᵈ(y - x)

```lean
def positionState (x : Space d) : StrongDual ℂ 𝓢(Space d, ℂ)
```

**`QuantumMechanics.SpaceDHilbertSpace.positionState_apply`**, a lemma, [line 62](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/SpaceD/PositionStates.lean#L62).

> The defining property of position states.

```lean
lemma positionState_apply (x : Space d) (f : 𝓢(Space d, ℂ)) : positionState x f = f x
```

**`QuantumMechanics.SpaceDHilbertSpace.eq_of_eq_positionState`**, a lemma, [line 65](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/SpaceD/PositionStates.lean#L65).

> Two Schwartz maps are equal if they are equal on all position states.

```lean
lemma eq_of_eq_positionState {f g : 𝓢(Space d, ℂ)}
    (h : ∀ x, positionState x f = positionState x g) : f = g
```

## B. Position states as generalized eigenvectors

**`QuantumMechanics.SpaceDHilbertSpace.positionState_comp_positionCLM`**, a lemma, [line 79](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/SpaceD/PositionStates.lean#L79).

> The position state `positionState x` is a generalized eigenvector of `𝐱 i` with eigenvalue
> `xᵢ`, in the bra form `⟨x| 𝐱ᵢ = xᵢ ⟨x|` as functionals on Schwartz space. Since `𝐱 i` is
> symmetric and `xᵢ` is real, this is equivalent to the ket form `𝐱ᵢ |x⟩ = xᵢ |x⟩`.

```lean
lemma positionState_comp_positionCLM (x : Space d) (i : Fin d) :
    positionState x ∘L 𝐱 i = (x i : ℂ) • positionState x
```

## Depends on

- [Position operators](../../operators/position.md)

## Sources

- [Physlib/QuantumMechanics/HilbertSpaces/SpaceD/PositionStates.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HilbertSpaces/SpaceD/PositionStates.lean)
