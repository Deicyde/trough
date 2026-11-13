---
declaration: module
origin: cited
lean: QuantumMechanics.leibniz_lie, QuantumMechanics.lie_leibniz, QuantumMechanics.comp_eq_comp_add_commute, QuantumMechanics.id_commutation, QuantumMechanics.comp_eq_comp_sub_commute, QuantumMechanics.position_commutation_position, QuantumMechanics.position_comp_commute, QuantumMechanics.position_commutation_radiusRegPow
statement: formalized
proof: formalized
---

# Commutation relations

The module `Physlib.QuantumMechanics.Operators.Commutation`, [Physlib/QuantumMechanics/Operators/Commutation.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Commutation.lean): 23 declarations, 5 with a docstring.

## i. Overview

> In this module we compute the commutators of position and momentum operators on Schwartz maps
> on `Space d`, including regularized powers of the radius.
>
> Commutator lemmas come in three flavors:
>   - 1. `a_commutation_b` lemmas are of the form `⁅a, b⁆ = (⋯)`.
>   - 2. `a_comp_b_commute` and `a_comp_commute` lemmas are of the form `a ∘ b = b ∘ a`.
>   - 3. `a_comp_b_eq` lemmas are of the form `a ∘ b = b ∘ a + (⋯)`.

## ii. Key results

> - `position_commutation_momentum` : The canonical commutation relations.

## iv. References

> * None.

## A. General

**`QuantumMechanics.leibniz_lie`**, a lemma, [line 60](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Commutation.lean#L60).

```lean
lemma leibniz_lie (A B C : 𝓢(Space d, ℂ) →L[ℂ] 𝓢(Space d, ℂ)) :
    ⁅A ∘L B, C⁆ = A ∘L ⁅B, C⁆ + ⁅A, C⁆ ∘L B
```

**`QuantumMechanics.lie_leibniz`**, a lemma, [line 65](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Commutation.lean#L65).

```lean
lemma lie_leibniz (A B C : 𝓢(Space d, ℂ) →L[ℂ] 𝓢(Space d, ℂ)) :
    ⁅A, B ∘L C⁆ = B ∘L ⁅A, C⁆ + ⁅A, B⁆ ∘L C
```

**`QuantumMechanics.comp_eq_comp_add_commute`**, a lemma, [line 70](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Commutation.lean#L70).

```lean
lemma comp_eq_comp_add_commute (A B : 𝓢(Space d, ℂ) →L[ℂ] 𝓢(Space d, ℂ)) :
    A ∘L B = B ∘L A + ⁅A, B⁆
```

**`QuantumMechanics.id_commutation`**, a lemma, [line 76](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Commutation.lean#L76).

> The identity commutes with everything.

```lean
lemma id_commutation (A : 𝓢(Space d, ℂ) →L[ℂ] 𝓢(Space d, ℂ)) :
    ⁅ContinuousLinearMap.id ℂ 𝓢(Space d, ℂ), A⁆ = 0
```

**`QuantumMechanics.comp_eq_comp_sub_commute`**, a lemma, [line 80](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Commutation.lean#L80).

```lean
lemma comp_eq_comp_sub_commute (A B : 𝓢(Space d, ℂ) →L[ℂ] 𝓢(Space d, ℂ)) :
    A ∘L B = B ∘L A - ⁅B, A⁆
```

## B. Commutators

### B.1. Position / position

**`QuantumMechanics.position_commutation_position`**, a lemma, [line 99](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Commutation.lean#L99).

> Position operators commute: `[xᵢ, xⱼ] = 0`.

```lean
lemma position_commutation_position : ⁅𝐱 i, 𝐱 j⁆ = 0
```

**`QuantumMechanics.position_comp_commute`**, a lemma, [line 103](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Commutation.lean#L103).

```lean
lemma position_comp_commute : 𝐱 i ∘L 𝐱 j = 𝐱 j ∘L 𝐱 i
```

**`QuantumMechanics.position_commutation_radiusRegPow`**, a lemma, [line 107](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Commutation.lean#L107).

```lean
lemma position_commutation_radiusRegPow : ⁅𝐱 i, 𝐫₀[d] ε s⁆ = 0
```

**`QuantumMechanics.position_comp_radiusRegPow_commute`**, a lemma, [line 111](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Commutation.lean#L111).

```lean
lemma position_comp_radiusRegPow_commute : 𝐱 i ∘L 𝐫₀ ε s = 𝐫₀ ε s ∘L 𝐱 i
```

**`QuantumMechanics.radiusRegPow_commutation_radiusRegPow`**, a lemma, [line 115](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Commutation.lean#L115).

```lean
lemma radiusRegPow_commutation_radiusRegPow : ⁅𝐫₀[d] ε s, 𝐫₀[d] ε t⁆ = 0
```

### B.2. Momentum / momentum

**`QuantumMechanics.momentum_commutation_momentum`**, a lemma, [line 126](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Commutation.lean#L126).

> Momentum operators commute: `[pᵢ, pⱼ] = 0`.

```lean
lemma momentum_commutation_momentum : ⁅𝐩 i, 𝐩 j⁆ = 0
```

**`QuantumMechanics.momentum_comp_commute`**, a lemma, [line 133](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Commutation.lean#L133).

```lean
lemma momentum_comp_commute : 𝐩 i ∘L 𝐩 j = 𝐩 j ∘L 𝐩 i
```

**`QuantumMechanics.momentumSqr_commutation_momentum`**, a lemma, [line 139](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Commutation.lean#L139).

```lean
lemma momentumSqr_commutation_momentum : ⁅𝐩[d] ⬝ᵥ 𝐩, 𝐩 i⁆ = 0
```

**`QuantumMechanics.momentumSqr_comp_momentum_commute`**, a lemma, [line 142](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Commutation.lean#L142).

```lean
lemma momentumSqr_comp_momentum_commute : (𝐩 ⬝ᵥ 𝐩) ∘L 𝐩 i = 𝐩 i ∘L (𝐩 ⬝ᵥ 𝐩)
```

### B.3. Position / momentum

**`QuantumMechanics.position_commutation_momentum`**, a lemma, [line 152](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Commutation.lean#L152).

> The canonical commutation relations: `[xᵢ, pⱼ] = iℏ δᵢⱼ𝟙`.

```lean
lemma position_commutation_momentum : ⁅𝐱 i, 𝐩 j⁆ =
    (I * ℏ) • δ[i,j] • ContinuousLinearMap.id ℂ 𝓢(Space d, ℂ)
```

**`QuantumMechanics.position_commutation_momentum_apply`**, a lemma, [line 166](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Commutation.lean#L166).

> The canonical commutation relations, pointwise: `xᵢ (pᵢ ψ)(x) - (pᵢ (xᵢ ψ))(x) = iℏ ψ(x)`.

```lean
lemma position_commutation_momentum_apply (ψ : 𝓢(Space d, ℂ)) (x : Space d) :
    ((x i : ℝ) : ℂ) * 𝐩 i ψ x - 𝐩 i (𝐱 i ψ) x = I * ℏ * ψ x
```

**`QuantumMechanics.momentum_comp_position_eq`**, a lemma, [line 172](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Commutation.lean#L172).

```lean
lemma momentum_comp_position_eq : 𝐩 j ∘L 𝐱 i =
    𝐱 i ∘L 𝐩 j - (I * ℏ) • δ[i,j] • ContinuousLinearMap.id ℂ 𝓢(Space d, ℂ)
```

**`QuantumMechanics.position_position_commutation_momentum`**, a lemma, [line 176](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Commutation.lean#L176).

```lean
lemma position_position_commutation_momentum : ⁅𝐱 i ∘L 𝐱 j, 𝐩 k⁆ =
    (I * ℏ) • (δ[i,k] • 𝐱 j + δ[j,k] • 𝐱 i)
```

**`QuantumMechanics.position_commutation_momentum_momentum`**, a lemma, [line 181](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Commutation.lean#L181).

```lean
lemma position_commutation_momentum_momentum : ⁅𝐱 i, 𝐩 j ∘L 𝐩 k⁆ =
    (I * ℏ) • (δ[i,k] • 𝐩 j + δ[i,j] • 𝐩 k)
```

**`QuantumMechanics.position_commutation_momentumSqr`**, a lemma, [line 186](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Commutation.lean#L186).

```lean
lemma position_commutation_momentumSqr : ⁅𝐱 i, 𝐩 ⬝ᵥ 𝐩⁆ = (2 * I * ℏ) • 𝐩 i
```

**`QuantumMechanics.radiusRegPow_commutation_momentum`**, a lemma, [line 190](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Commutation.lean#L190).

```lean
lemma radiusRegPow_commutation_momentum :
    ⁅𝐫₀[d] ε s, 𝐩 i⁆ = (s * I * ℏ) • 𝐫₀ ε (s-2) ∘L 𝐱 i
```

**`QuantumMechanics.momentum_comp_radiusRegPow_eq`**, a lemma, [line 211](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Commutation.lean#L211).

```lean
lemma momentum_comp_radiusRegPow_eq :
    𝐩 i ∘L 𝐫₀ ε s = 𝐫₀ ε s ∘L 𝐩 i - (s * I * ℏ) • 𝐫₀ ε (s-2) ∘L 𝐱 i
```

**`QuantumMechanics.radiusRegPow_commutation_momentumSqr`**, a lemma, [line 215](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Commutation.lean#L215).

```lean
lemma radiusRegPow_commutation_momentumSqr :
    ⁅𝐫₀[d] ε s, 𝐩[d] ⬝ᵥ 𝐩⁆ = (2 * s * I * ℏ) • 𝐫₀ ε (s-2) ∘L (𝐱 ⬝ᵥ 𝐩)
    + (s * (d + s - 2) * ℏ ^ 2) • 𝐫₀ ε (s-2) - (ε ^ 2 * s * (s - 2) * ℏ ^ 2) • 𝐫₀ ε (s-4)
```

## Depends on

- [Kronecker delta](../../mathematics/kroneckerdelta/basic.md)
- [Momentum operators](momentum.md)
- [Position operators](position.md)

## Sources

- [Physlib/QuantumMechanics/Operators/Commutation.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Commutation.lean)
