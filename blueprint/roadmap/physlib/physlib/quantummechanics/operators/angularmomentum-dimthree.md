---
declaration: module
origin: cited
lean: QuantumMechanics.angularMomentumDimThreeOperator, QuantumMechanics.angularMomentumDimThreeCLM_zero_eq, QuantumMechanics.angularMomentumDimThreeCLM_one_eq, QuantumMechanics.angularMomentumDimThreeCLM_two_eq, QuantumMechanics.angularMomentumDimThreeOperator_domain_eq, QuantumMechanics.angularMomentumDimThreeOperator_apply, QuantumMechanics.angularMomentumDimThreeOperator_apply_ae, QuantumMechanics.angularMomentumDimThreeOperator_range
statement: formalized
proof: formalized
---

# Three-dimensional angular momentum

The module `Physlib.QuantumMechanics.Operators.AngularMomentum.DimThree`, [Physlib/QuantumMechanics/Operators/AngularMomentum/DimThree.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/AngularMomentum/DimThree.lean): 45 declarations, 23 with a docstring.

> Cartesian components, commutation relations, and ladder operators on the Schwartz domain.

## i. Overview

> The Cartesian components use the right-handed convention
> `Lx = L₁₂`, `Ly = L₂₀`, `Lz = L₀₁`, with coordinate indices `0, 1, 2`.
> The Schwartz operators are the existing `angularMomentumOperator3D`; the Hilbert-space
> operators have the common invariant domain `SchwartzSubmodule 3`.
> Their commutation algebra and the raising/lowering operators are proved first on Schwartz maps
> and then transported to this Hilbert-space domain. In particular, a zero commutator means zero
> on that domain; it is not an equality with the everywhere-defined zero `LinearPMap`.

## ii. Key results

> - `angularMomentumDimThreeOperator`: the Hilbert-space Cartesian components.
> - `angularMomentumOperatorSqr_eq_sum_dimThree`: `L² = Lx² + Ly² + Lz²` on Schwartz maps.
> - `angularMomentumDimThreeOperator_isSymmetric`: symmetry of each Cartesian component.
> - `angularMomentumDimThree_commutation`: `[Li, Lj] = iℏ ∑k εijk Lk`.
> - `angularMomentumRaisingCLM`, `angularMomentumLoweringCLM`: `Lx ± i Ly` on Schwartz maps.
> - `angularMomentumRaisingOperator`, `angularMomentumLoweringOperator`: their Hilbert-space lifts.
> - `angularMomentumZOperator_commutation_raising`, `angularMomentumZOperator_commutation_lowering`:
>   `[Lz, L±] = ±ℏ L±` on the Schwartz domain.
> - `angularMomentumSqOperator_commutation_raising`, `angularMomentumSqOperator_commutation_lowering`:
>   `[L², L±] = 0` on that domain.
>
> Open the `AngularMomentum` scope for `𝐋₃ i` on Schwartz maps and `𝓛₃ i` on the Hilbert space,
> where `i : Fin 3` and indices `0`, `1`, `2` correspond to `x`, `y`, `z`.
> The notation `𝓛²` denotes the Hilbert-space square.
> The same scope provides `𝐋⁺`, `𝐋⁻` and `𝓛⁺`, `𝓛⁻` for the ladder operators.

## iv. References

> * None.

## A. Cartesian components

**`QuantumMechanics.angularMomentumDimThreeOperator`**, a def, [line 76](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/AngularMomentum/DimThree.lean#L76).

> The Cartesian Hilbert-space components, ordered as `x, y, z`.

```lean
def angularMomentumDimThreeOperator (i : Fin 3) :
    SpaceDHilbertSpace 3 →ₗ.[ℂ] SpaceDHilbertSpace 3
```

**`QuantumMechanics.angularMomentumDimThreeCLM_zero_eq`**, a lemma, [line 87](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/AngularMomentum/DimThree.lean#L87).

```lean
lemma angularMomentumDimThreeCLM_zero_eq : 𝐋₃ 0 = 𝐋 1 2
```

**`QuantumMechanics.angularMomentumDimThreeCLM_one_eq`**, a lemma, [line 89](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/AngularMomentum/DimThree.lean#L89).

```lean
lemma angularMomentumDimThreeCLM_one_eq : 𝐋₃ 1 = 𝐋 2 0
```

**`QuantumMechanics.angularMomentumDimThreeCLM_two_eq`**, a lemma, [line 91](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/AngularMomentum/DimThree.lean#L91).

```lean
lemma angularMomentumDimThreeCLM_two_eq : 𝐋₃ 2 = 𝐋 0 1
```

### A.1. Hilbert-space transport

**`QuantumMechanics.angularMomentumDimThreeOperator_domain_eq`**, a lemma, [line 99](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/AngularMomentum/DimThree.lean#L99).

```lean
lemma angularMomentumDimThreeOperator_domain_eq : (𝓛₃ i).domain = SchwartzSubmodule 3
```

**`QuantumMechanics.angularMomentumDimThreeOperator_apply`**, a lemma, [line 101](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/AngularMomentum/DimThree.lean#L101).

```lean
lemma angularMomentumDimThreeOperator_apply (ψ : SchwartzSubmodule 3) :
    𝓛₃ i ψ = schwartzEquiv volume (𝐋₃ i ((schwartzEquiv volume).symm ψ))
```

**`QuantumMechanics.angularMomentumDimThreeOperator_apply_ae`**, a lemma, [line 104](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/AngularMomentum/DimThree.lean#L104).

```lean
lemma angularMomentumDimThreeOperator_apply_ae (ψ : SchwartzSubmodule 3) :
    𝓛₃ i ψ =ᵐ[volume] 𝐋₃ i ((schwartzEquiv volume).symm ψ)
```

**`QuantumMechanics.angularMomentumDimThreeOperator_range`**, a lemma, [line 107](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/AngularMomentum/DimThree.lean#L107).

```lean
lemma angularMomentumDimThreeOperator_range (ψ : SchwartzSubmodule 3) :
    𝓛₃ i ψ ∈ SchwartzSubmodule 3
```

**`QuantumMechanics.angularMomentumDimThreeOperator_apply_apply`**, a lemma, [line 112](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/AngularMomentum/DimThree.lean#L112).

> Composing two components stays on the common Schwartz domain.

```lean
lemma angularMomentumDimThreeOperator_apply_apply (j : Fin 3) (ψ : SchwartzSubmodule 3) :
    𝓛₃ i ⟨𝓛₃ j ψ, angularMomentumDimThreeOperator_range j ψ⟩ =
      schwartzEquiv volume (𝐋₃ i (𝐋₃ j ((schwartzEquiv volume).symm ψ)))
```

**`QuantumMechanics.angularMomentumDimThreeOperator_hasDenseDomain`**, a lemma, [line 120](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/AngularMomentum/DimThree.lean#L120).

```lean
lemma angularMomentumDimThreeOperator_hasDenseDomain :
    (𝓛₃ i).HasDenseDomain
```

**`QuantumMechanics.angularMomentumDimThreeOperator_isSymmetric`**, a lemma, [line 123](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/AngularMomentum/DimThree.lean#L123).

```lean
lemma angularMomentumDimThreeOperator_isSymmetric : (𝓛₃ i).IsSymmetric
```

**`QuantumMechanics.angularMomentumDimThreeOperator_isUnbounded`**, a lemma, [line 126](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/AngularMomentum/DimThree.lean#L126).

```lean
lemma angularMomentumDimThreeOperator_isUnbounded : (𝓛₃ i).IsUnbounded
```

### A.2. Sum of the three squares

**`QuantumMechanics.angularMomentumOperatorSqr_eq_sum_dimThree`**, a lemma, [line 135](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/AngularMomentum/DimThree.lean#L135).

> The antisymmetric-index definition agrees with the Cartesian sum of squares.

```lean
lemma angularMomentumOperatorSqr_eq_sum_dimThree : 𝐋²[3] = ∑ i : Fin 3, 𝐋₃ i ∘L 𝐋₃ i
```

**`QuantumMechanics.angularMomentumSqOperator_apply_eq_sum_dimThree`**, a lemma, [line 145](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/AngularMomentum/DimThree.lean#L145).

> The same Cartesian sum of squares, evaluated on a Hilbert-space Schwartz vector.

```lean
lemma angularMomentumSqOperator_apply_eq_sum_dimThree (ψ : SchwartzSubmodule 3) :
    angularMomentumSqOperator ψ = ∑ i : Fin 3, 𝓛₃ i
      ⟨𝓛₃ i ψ, angularMomentumDimThreeOperator_range i ψ⟩
```

## B. Commutation algebra

> The bracket below is the existing commutator of continuous linear maps on Schwartz space.
> Hilbert-space statements are evaluated on `SchwartzSubmodule 3`, with explicit membership
> proofs for intermediate vectors. They make no claims about domains of closed extensions.

**`QuantumMechanics.angularMomentumDimThree_commutation`**, a lemma, [line 166](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/AngularMomentum/DimThree.lean#L166).

> The Cartesian angular momentum algebra, with the right-handed Levi-Civita symbol.

```lean
lemma angularMomentumDimThree_commutation (j : Fin 3) : ⁅𝐋₃ i, 𝐋₃ j⁆ =
    (I * ℏ) • ∑ k : Fin 3, (leviCivitaSymbol ![i, j, k] : ℂ) • 𝐋₃ k
```

**`QuantumMechanics.angularMomentumDimThree_commutation_xy`**, a lemma, [line 177](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/AngularMomentum/DimThree.lean#L177).

> `[Lx, Ly] = iℏ Lz`.

```lean
lemma angularMomentumDimThree_commutation_xy : ⁅𝐋₃ 0, 𝐋₃ 1⁆ = (I * ℏ) • 𝐋₃ 2
```

**`QuantumMechanics.angularMomentumDimThree_commutation_yz`**, a lemma, [line 184](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/AngularMomentum/DimThree.lean#L184).

> `[Ly, Lz] = iℏ Lx`.

```lean
lemma angularMomentumDimThree_commutation_yz : ⁅𝐋₃ 1, 𝐋₃ 2⁆ = (I * ℏ) • 𝐋₃ 0
```

**`QuantumMechanics.angularMomentumDimThree_commutation_zx`**, a lemma, [line 191](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/AngularMomentum/DimThree.lean#L191).

> `[Lz, Lx] = iℏ Ly`.

```lean
lemma angularMomentumDimThree_commutation_zx : ⁅𝐋₃ 2, 𝐋₃ 0⁆ = (I * ℏ) • 𝐋₃ 1
```

**`QuantumMechanics.angularMomentumSqr_commutation_dimThree`**, a lemma, [line 198](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/AngularMomentum/DimThree.lean#L198).

> Angular momentum squared commutes with every Cartesian component on Schwartz maps.

```lean
lemma angularMomentumSqr_commutation_dimThree : ⁅𝐋²[3], 𝐋₃ i⁆ = 0
```

**`QuantumMechanics.angularMomentumDimThreeOperator_commutation`**, a lemma, [line 202](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/AngularMomentum/DimThree.lean#L202).

> The Cartesian commutation algebra on the common Hilbert-space Schwartz domain.

```lean
lemma angularMomentumDimThreeOperator_commutation (j : Fin 3) (ψ : SchwartzSubmodule 3) :
    𝓛₃ i ⟨𝓛₃ j ψ, angularMomentumDimThreeOperator_range j ψ⟩ -
      𝓛₃ j ⟨𝓛₃ i ψ, angularMomentumDimThreeOperator_range i ψ⟩ =
      (I * ℏ) • ∑ k : Fin 3, (leviCivitaSymbol ![i, j, k] : ℂ) • 𝓛₃ k ψ
```

**`QuantumMechanics.angularMomentumSqOperator_commutation_dimThree`**, a lemma, [line 216](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/AngularMomentum/DimThree.lean#L216).

> `[L², Li] = 0` on the common invariant Hilbert-space domain.

```lean
lemma angularMomentumSqOperator_commutation_dimThree (ψ : SchwartzSubmodule 3) :
    angularMomentumSqOperator ⟨𝓛₃ i ψ, angularMomentumDimThreeOperator_range i ψ⟩ -
      𝓛₃ i ⟨angularMomentumSqOperator ψ, angularMomentumSqOperator_range ψ⟩ = 0
```

## C. Ladder operators

> These operators act on arbitrary Schwartz vectors. No eigenstate or spectral assumptions
> are used in their commutation relations.

**`QuantumMechanics.angularMomentumRaisingCLM`**, a def, [line 239](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/AngularMomentum/DimThree.lean#L239).

> The angular momentum raising operator `L₊ = Lx + i Ly` on Schwartz maps.

```lean
def angularMomentumRaisingCLM : 𝓢(Space 3, ℂ) →L[ℂ] 𝓢(Space 3, ℂ)
```

**`QuantumMechanics.angularMomentumLoweringCLM`**, a def, [line 242](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/AngularMomentum/DimThree.lean#L242).

> The angular momentum lowering operator `L₋ = Lx - i Ly` on Schwartz maps.

```lean
def angularMomentumLoweringCLM : 𝓢(Space 3, ℂ) →L[ℂ] 𝓢(Space 3, ℂ)
```

**`QuantumMechanics.angularMomentumZ_commutation_raising`**, a lemma, [line 251](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/AngularMomentum/DimThree.lean#L251).

> `[Lz, L₊] = ℏ L₊`.

```lean
lemma angularMomentumZ_commutation_raising : ⁅𝐋₃ 2, 𝐋⁺⁆ = (ℏ : ℂ) • 𝐋⁺
```

**`QuantumMechanics.angularMomentumZ_commutation_lowering`**, a lemma, [line 258](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/AngularMomentum/DimThree.lean#L258).

> `[Lz, L₋] = -ℏ L₋`.

```lean
lemma angularMomentumZ_commutation_lowering : ⁅𝐋₃ 2, 𝐋⁻⁆ = -(ℏ : ℂ) • 𝐋⁻
```

**`QuantumMechanics.angularMomentumSqr_commutation_raising`**, a lemma, [line 265](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/AngularMomentum/DimThree.lean#L265).

> Angular momentum squared commutes with the raising operator.

```lean
lemma angularMomentumSqr_commutation_raising : ⁅𝐋²[3], 𝐋⁺⁆ = 0
```

**`QuantumMechanics.angularMomentumSqr_commutation_lowering`**, a lemma, [line 269](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/AngularMomentum/DimThree.lean#L269).

> Angular momentum squared commutes with the lowering operator.

```lean
lemma angularMomentumSqr_commutation_lowering : ⁅𝐋²[3], 𝐋⁻⁆ = 0
```

### C.1. Hilbert-space ladder operators

**`QuantumMechanics.angularMomentumRaisingOperator`**, a def, [line 277](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/AngularMomentum/DimThree.lean#L277).

> The raising operator on the Hilbert space, with Schwartz domain.

```lean
def angularMomentumRaisingOperator : SpaceDHilbertSpace 3 →ₗ.[ℂ] SpaceDHilbertSpace 3
```

**`QuantumMechanics.angularMomentumLoweringOperator`**, a def, [line 282](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/AngularMomentum/DimThree.lean#L282).

> The lowering operator on the Hilbert space, with Schwartz domain.

```lean
def angularMomentumLoweringOperator : SpaceDHilbertSpace 3 →ₗ.[ℂ] SpaceDHilbertSpace 3
```

**`QuantumMechanics.angularMomentumRaisingOperator_domain_eq`**, a lemma, [line 292](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/AngularMomentum/DimThree.lean#L292).

```lean
lemma angularMomentumRaisingOperator_domain_eq : (𝓛⁺).domain = SchwartzSubmodule 3
```

**`QuantumMechanics.angularMomentumLoweringOperator_domain_eq`**, a lemma, [line 294](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/AngularMomentum/DimThree.lean#L294).

```lean
lemma angularMomentumLoweringOperator_domain_eq : (𝓛⁻).domain = SchwartzSubmodule 3
```

**`QuantumMechanics.angularMomentumRaisingOperator_apply`**, a lemma, [line 296](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/AngularMomentum/DimThree.lean#L296).

```lean
lemma angularMomentumRaisingOperator_apply (ψ : SchwartzSubmodule 3) :
    𝓛⁺ ψ = schwartzEquiv volume (𝐋⁺ ((schwartzEquiv volume).symm ψ))
```

**`QuantumMechanics.angularMomentumLoweringOperator_apply`**, a lemma, [line 299](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/AngularMomentum/DimThree.lean#L299).

```lean
lemma angularMomentumLoweringOperator_apply (ψ : SchwartzSubmodule 3) :
    𝓛⁻ ψ = schwartzEquiv volume (𝐋⁻ ((schwartzEquiv volume).symm ψ))
```

**`QuantumMechanics.angularMomentumRaisingOperator_apply_eq`**, a lemma, [line 302](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/AngularMomentum/DimThree.lean#L302).

```lean
lemma angularMomentumRaisingOperator_apply_eq (ψ : SchwartzSubmodule 3) :
    𝓛⁺ ψ = 𝓛₃ 0 ψ + I • 𝓛₃ 1 ψ
```

**`QuantumMechanics.angularMomentumLoweringOperator_apply_eq`**, a lemma, [line 307](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/AngularMomentum/DimThree.lean#L307).

```lean
lemma angularMomentumLoweringOperator_apply_eq (ψ : SchwartzSubmodule 3) :
    𝓛⁻ ψ = 𝓛₃ 0 ψ - I • 𝓛₃ 1 ψ
```

**`QuantumMechanics.angularMomentumRaisingOperator_apply_ae`**, a lemma, [line 312](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/AngularMomentum/DimThree.lean#L312).

```lean
lemma angularMomentumRaisingOperator_apply_ae (ψ : SchwartzSubmodule 3) :
    𝓛⁺ ψ =ᵐ[volume] 𝐋⁺ ((schwartzEquiv volume).symm ψ)
```

**`QuantumMechanics.angularMomentumLoweringOperator_apply_ae`**, a lemma, [line 315](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/AngularMomentum/DimThree.lean#L315).

```lean
lemma angularMomentumLoweringOperator_apply_ae (ψ : SchwartzSubmodule 3) :
    𝓛⁻ ψ =ᵐ[volume] 𝐋⁻ ((schwartzEquiv volume).symm ψ)
```

**`QuantumMechanics.angularMomentumRaisingOperator_range`**, a lemma, [line 318](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/AngularMomentum/DimThree.lean#L318).

```lean
lemma angularMomentumRaisingOperator_range (ψ : SchwartzSubmodule 3) :
    𝓛⁺ ψ ∈ SchwartzSubmodule 3
```

**`QuantumMechanics.angularMomentumLoweringOperator_range`**, a lemma, [line 322](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/AngularMomentum/DimThree.lean#L322).

```lean
lemma angularMomentumLoweringOperator_range (ψ : SchwartzSubmodule 3) :
    𝓛⁻ ψ ∈ SchwartzSubmodule 3
```

**`QuantumMechanics.angularMomentumRaisingOperator_hasDenseDomain`**, a lemma, [line 326](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/AngularMomentum/DimThree.lean#L326).

```lean
lemma angularMomentumRaisingOperator_hasDenseDomain : (𝓛⁺).HasDenseDomain
```

**`QuantumMechanics.angularMomentumLoweringOperator_hasDenseDomain`**, a lemma, [line 329](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/AngularMomentum/DimThree.lean#L329).

```lean
lemma angularMomentumLoweringOperator_hasDenseDomain : (𝓛⁻).HasDenseDomain
```

### C.2. Hilbert-space commutation relations on the invariant domain

**`QuantumMechanics.angularMomentumZOperator_commutation_raising`**, a lemma, [line 337](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/AngularMomentum/DimThree.lean#L337).

> `[Lz, L₊] ψ = ℏ L₊ ψ` for every Schwartz vector in the Hilbert space.

```lean
lemma angularMomentumZOperator_commutation_raising (ψ : SchwartzSubmodule 3) :
    𝓛₃ 2 ⟨𝓛⁺ ψ, angularMomentumRaisingOperator_range ψ⟩ -
      𝓛⁺ ⟨𝓛₃ 2 ψ, angularMomentumDimThreeOperator_range 2 ψ⟩ = (ℏ : ℂ) • 𝓛⁺ ψ
```

**`QuantumMechanics.angularMomentumZOperator_commutation_lowering`**, a lemma, [line 354](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/AngularMomentum/DimThree.lean#L354).

> `[Lz, L₋] ψ = -ℏ L₋ ψ` for every Schwartz vector in the Hilbert space.

```lean
lemma angularMomentumZOperator_commutation_lowering (ψ : SchwartzSubmodule 3) :
    𝓛₃ 2 ⟨𝓛⁻ ψ, angularMomentumLoweringOperator_range ψ⟩ -
      𝓛⁻ ⟨𝓛₃ 2 ψ, angularMomentumDimThreeOperator_range 2 ψ⟩ = -(ℏ : ℂ) • 𝓛⁻ ψ
```

**`QuantumMechanics.angularMomentumSqOperator_commutation_raising`**, a lemma, [line 371](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/AngularMomentum/DimThree.lean#L371).

> `[L², L₊] ψ = 0` on the common invariant Schwartz domain.

```lean
lemma angularMomentumSqOperator_commutation_raising (ψ : SchwartzSubmodule 3) :
    𝓛² ⟨𝓛⁺ ψ, angularMomentumRaisingOperator_range ψ⟩ -
      𝓛⁺ ⟨𝓛² ψ, angularMomentumSqOperator_range ψ⟩ = 0
```

**`QuantumMechanics.angularMomentumSqOperator_commutation_lowering`**, a lemma, [line 387](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/AngularMomentum/DimThree.lean#L387).

> `[L², L₋] ψ = 0` on the common invariant Schwartz domain.

```lean
lemma angularMomentumSqOperator_commutation_lowering (ψ : SchwartzSubmodule 3) :
    𝓛² ⟨𝓛⁻ ψ, angularMomentumLoweringOperator_range ψ⟩ -
      𝓛⁻ ⟨𝓛² ψ, angularMomentumSqOperator_range ψ⟩ = 0
```

## Depends on

- [The Levi-Civita symbol in general dimension](../../mathematics/levicivita/basic.md)
- [Angular momentum operator](angularmomentum.md)

## Sources

- [Physlib/QuantumMechanics/Operators/AngularMomentum/DimThree.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/AngularMomentum/DimThree.lean)
