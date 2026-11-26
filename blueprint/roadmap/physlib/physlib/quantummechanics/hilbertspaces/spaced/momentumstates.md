---
declaration: module
origin: cited
lean: QuantumMechanics.SpaceDHilbertSpace.momentumState, QuantumMechanics.SpaceDHilbertSpace.momentumState_apply, QuantumMechanics.SpaceDHilbertSpace.momentumState_oneEquiv_symm_apply, QuantumMechanics.SpaceDHilbertSpace.eq_of_eq_momentumState, QuantumMechanics.SpaceDHilbertSpace.momentumState_comp_momentumCLM
statement: formalized
proof: formalized
---

# Momentum states

The module `Physlib.QuantumMechanics.HilbertSpaces.SpaceD.MomentumStates`, [Physlib/QuantumMechanics/HilbertSpaces/SpaceD/MomentumStates.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/HilbertSpaces/SpaceD/MomentumStates.lean): 5 declarations, 5 with a docstring.

## i. Overview

> Informally, the momentum "state" corresponding to the wave vector `p`, of momentum `ℏ p`, is the
> non-normalizable plane wave `exp (I p ⬝ᵥ x)`. More precisely, the momentum "state" lives in the
> \_rigged\_ Hilbert space `𝓢(Space d, ℂ) < SpaceDHilbertSpace d μ < StrongDual ℂ 𝓢(Space d, ℂ)`
> as the bra `⟨p|`. This is the linear functional `ψ ↦ ⟨exp (I p ⬝ᵥ x), ψ⟩ = 𝓕 ψ ((2π)⁻¹ • p)`.
>
> An operator `A` acts on `momentumState p` by precomposition, `⟨p| A = momentumState p ∘L A`.

## ii. Key results

> - `momentumState` : the momentum state as a member of the strong dual of the Schwartz space.
> - `momentumState_comp_momentumCLM` : the momentum state `momentumState p` is a generalized
>   eigenvector of `𝐩 i` with eigenvalue `ℏ pᵢ`.

## iv. References

> * https://en.wikipedia.org/wiki/Rigged\_Hilbert\_space. [ref: wiki\_rigged\_hilbert\_space]

## A. Momentum states

**`QuantumMechanics.SpaceDHilbertSpace.momentumState`**, a def, [line 63](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/HilbertSpaces/SpaceD/MomentumStates.lean#L63).

> Momentum state as a member of the strong dual of the Schwartz space.
>
> For a given wave vector `p` this is the bra `⟨p|` of the non-normalizable plane wave
> `exp (I p ⬝ᵥ x)`, that is `ψ ↦ ⟨exp (I p ⬝ᵥ x), ψ⟩`.

```lean
def momentumState (p : Space d) : StrongDual ℂ 𝓢(Space d, ℂ)
```

**`QuantumMechanics.SpaceDHilbertSpace.momentumState_apply`**, a lemma, [line 68](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/HilbertSpaces/SpaceD/MomentumStates.lean#L68).

> The defining property of momentum states.

```lean
lemma momentumState_apply (p : Space d) (ψ : 𝓢(Space d, ℂ)) :
    momentumState p ψ = 𝓕 ψ ((2 * π)⁻¹ • p)
```

**`QuantumMechanics.SpaceDHilbertSpace.momentumState_oneEquiv_symm_apply`**, a lemma, [line 74](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/HilbertSpaces/SpaceD/MomentumStates.lean#L74).

> In one dimension the momentum state with wavenumber `k` pairs `ψ` with the plane wave
> `exp (I k x)`.

```lean
lemma momentumState_oneEquiv_symm_apply (k : ℝ) (ψ : 𝓢(Space 1, ℂ)) :
    momentumState (oneEquiv.symm k) ψ = ∫ x : Space 1, exp (-(k * (x 0 : ℝ) * I)) * ψ x
```

**`QuantumMechanics.SpaceDHilbertSpace.eq_of_eq_momentumState`**, a lemma, [line 88](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/HilbertSpaces/SpaceD/MomentumStates.lean#L88).

> Two Schwartz maps are equal if they are equal on all momentum states.

```lean
lemma eq_of_eq_momentumState {ψ φ : 𝓢(Space d, ℂ)}
    (h : ∀ p, momentumState p ψ = momentumState p φ) : ψ = φ
```

## B. Momentum states as generalized eigenvectors

**`QuantumMechanics.SpaceDHilbertSpace.momentumState_comp_momentumCLM`**, a lemma, [line 103](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/HilbertSpaces/SpaceD/MomentumStates.lean#L103).

> The momentum state `momentumState p` is a generalized eigenvector of `𝐩 i` with eigenvalue
> `ℏ pᵢ`, in the bra form `⟨p| 𝐩ᵢ = ℏ pᵢ ⟨p|` as functionals on Schwartz space. Since `𝐩 i` is
> symmetric and `ℏ pᵢ` is real, this is equivalent to the ket form `𝐩ᵢ |p⟩ = ℏ pᵢ |p⟩`.

```lean
lemma momentumState_comp_momentumCLM (p : Space d) (i : Fin d) :
    momentumState p ∘L 𝐩 i = (ℏ * p i : ℂ) • momentumState p
```

## Depends on

- [Momentum operators](../../operators/spaced-momentum.md)

## Sources

- [Physlib/QuantumMechanics/HilbertSpaces/SpaceD/MomentumStates.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/HilbertSpaces/SpaceD/MomentumStates.lean)
