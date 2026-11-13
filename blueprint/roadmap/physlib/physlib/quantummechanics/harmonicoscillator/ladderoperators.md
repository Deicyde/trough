---
declaration: module
origin: cited
lean: QuantumMechanics.HarmonicOscillator.loweringCLM, QuantumMechanics.HarmonicOscillator.raisingCLM, QuantumMechanics.HarmonicOscillator.loweringCLM_eq, QuantumMechanics.HarmonicOscillator.raisingCLM_eq, QuantumMechanics.HarmonicOscillator.sqrt_two_sq_ofReal, QuantumMechanics.HarmonicOscillator.lowering_commutation_raising, QuantumMechanics.HarmonicOscillator.lowering_commutation_lowering, QuantumMechanics.HarmonicOscillator.raising_commutation_raising
statement: formalized
proof: formalized
---

# Ladder operators

The module `Physlib.QuantumMechanics.HarmonicOscillator.LadderOperators`, [Physlib/QuantumMechanics/HarmonicOscillator/LadderOperators.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HarmonicOscillator/LadderOperators.lean): 18 declarations, 14 with a docstring.

## i. Overview

> The ladder operators of the `d`-dimensional quantum harmonic oscillator, acting on Schwartz maps:
> the lowering (annihilation) operators `aᵢ = (xᵢ/ξᵢ + i ξᵢ pᵢ/ℏ)/√2` and the raising (creation)
> operators `aᵢ† = (xᵢ/ξᵢ - i ξᵢ pᵢ/ℏ)/√2`, together with
> their commutation relations, which all follow from the canonical commutation relations
> `position_commutation_momentum`. The ladder operators are then lifted to unbounded operators on the
> Hilbert space with the Schwartz submodule as domain (like `momentumOperator`), `aᵢ†` being the
> formal adjoint of `aᵢ`. The number operators `Nᵢ = aᵢ† aᵢ` and the Hamiltonian written through them
> are in `NumberOperator.lean`.

## ii. Key results

> - `lowering_commutation_raising`: `[aᵢ, aⱼ†] = δᵢⱼ 𝟙`; `lowering_commutation_lowering`,
>   `raising_commutation_raising`: `[aᵢ, aⱼ] = 0`, `[aᵢ†, aⱼ†] = 0`.
> - `position_eq_lowering_add_raising`, `momentum_eq_raising_sub_lowering`: the position and
>   momentum operators in terms of the ladder operators.
> - `loweringOperator_isFormalAdjoint_raisingOperator`: `aᵢ†` is the formal adjoint of `aᵢ`.

## iv. References

> * None.

## A. Ladder operators

### A.1. Definitions

**`QuantumMechanics.HarmonicOscillator.loweringCLM`**, a def, [line 75](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HarmonicOscillator/LadderOperators.lean#L75).

> The lowering (annihilation) operator `aᵢ = (xᵢ/ξᵢ + i ξᵢ pᵢ/ℏ)/√2`, as a continuous linear
> map on Schwartz maps.

```lean
def loweringCLM : 𝓢(Space d, ℂ) →L[ℂ] 𝓢(Space d, ℂ)
```

**`QuantumMechanics.HarmonicOscillator.raisingCLM`**, a def, [line 80](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HarmonicOscillator/LadderOperators.lean#L80).

> The raising (creation) operator `aᵢ† = (xᵢ/ξᵢ - i ξᵢ pᵢ/ℏ)/√2`, as a continuous linear
> map on Schwartz maps.

```lean
def raisingCLM : 𝓢(Space d, ℂ) →L[ℂ] 𝓢(Space d, ℂ)
```

**`QuantumMechanics.HarmonicOscillator.loweringCLM_eq`**, a lemma, [line 83](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HarmonicOscillator/LadderOperators.lean#L83).

```lean
lemma loweringCLM_eq : Q.loweringCLM i =
    (Real.sqrt 2 : ℂ)⁻¹ • (((Q.ξ i : ℝ) : ℂ)⁻¹ • 𝐱 i + (I * ((Q.ξ i : ℝ) : ℂ) / (ℏ : ℂ)) • 𝐩 i)
```

**`QuantumMechanics.HarmonicOscillator.raisingCLM_eq`**, a lemma, [line 87](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HarmonicOscillator/LadderOperators.lean#L87).

```lean
lemma raisingCLM_eq : Q.raisingCLM i =
    (Real.sqrt 2 : ℂ)⁻¹ • (((Q.ξ i : ℝ) : ℂ)⁻¹ • 𝐱 i - (I * ((Q.ξ i : ℝ) : ℂ) / (ℏ : ℂ)) • 𝐩 i)
```

**`QuantumMechanics.HarmonicOscillator.sqrt_two_sq_ofReal`**, a lemma, [line 92](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HarmonicOscillator/LadderOperators.lean#L92).

> `(√2)² = 2` as complex numbers.

```lean
lemma sqrt_two_sq_ofReal : ((Real.sqrt 2 : ℝ) : ℂ) ^ 2 = 2
```

### A.2. Commutation relations

**`QuantumMechanics.HarmonicOscillator.lowering_commutation_raising`**, a lemma, [line 103](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HarmonicOscillator/LadderOperators.lean#L103).

> `[aᵢ, aⱼ†] = δᵢⱼ 𝟙`.

```lean
lemma lowering_commutation_raising :
    ⁅Q.loweringCLM i, Q.raisingCLM j⁆ = δ[i,j] • ContinuousLinearMap.id ℂ 𝓢(Space d, ℂ)
```

**`QuantumMechanics.HarmonicOscillator.lowering_commutation_lowering`**, a lemma, [line 120](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HarmonicOscillator/LadderOperators.lean#L120).

> `[aᵢ, aⱼ] = 0`.

```lean
lemma lowering_commutation_lowering : ⁅Q.loweringCLM i, Q.loweringCLM j⁆ = 0
```

**`QuantumMechanics.HarmonicOscillator.raising_commutation_raising`**, a lemma, [line 135](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HarmonicOscillator/LadderOperators.lean#L135).

> `[aᵢ†, aⱼ†] = 0`.

```lean
lemma raising_commutation_raising : ⁅Q.raisingCLM i, Q.raisingCLM j⁆ = 0
```

**`QuantumMechanics.HarmonicOscillator.raising_commutation_lowering`**, a lemma, [line 151](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HarmonicOscillator/LadderOperators.lean#L151).

> `[aᵢ†, aⱼ] = -δᵢⱼ 𝟙`.

```lean
lemma raising_commutation_lowering :
    ⁅Q.raisingCLM i, Q.loweringCLM j⁆ = -(δ[i,j] • ContinuousLinearMap.id ℂ 𝓢(Space d, ℂ))
```

### A.3. Position and momentum in terms of the ladder operators

**`QuantumMechanics.HarmonicOscillator.position_eq_lowering_add_raising`**, a lemma, [line 162](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HarmonicOscillator/LadderOperators.lean#L162).

> `xᵢ = (ξᵢ/√2) (aᵢ + aᵢ†)`.

```lean
lemma position_eq_lowering_add_raising :
    𝐱 i = (((Q.ξ i : ℝ) : ℂ) / (Real.sqrt 2 : ℂ)) • (Q.loweringCLM i + Q.raisingCLM i)
```

**`QuantumMechanics.HarmonicOscillator.momentum_eq_raising_sub_lowering`**, a lemma, [line 173](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HarmonicOscillator/LadderOperators.lean#L173).

> `pᵢ = (i ℏ/(√2 ξᵢ)) (aᵢ† - aᵢ)`.

```lean
lemma momentum_eq_raising_sub_lowering :
    𝐩 i = (I * (ℏ : ℂ) / ((Real.sqrt 2 : ℂ) * ((Q.ξ i : ℝ) : ℂ))) •
      (Q.raisingCLM i - Q.loweringCLM i)
```

### A.4. The ladder operators as unbounded operators, adjointness

**`QuantumMechanics.HarmonicOscillator.loweringOperator`**, a def, [line 191](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HarmonicOscillator/LadderOperators.lean#L191).

> The lowering operator as an unbounded operator with domain the Schwartz submodule.

```lean
def loweringOperator : Q.HS →ₗ.[ℂ] Q.HS
```

**`QuantumMechanics.HarmonicOscillator.raisingOperator`**, a def, [line 196](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HarmonicOscillator/LadderOperators.lean#L196).

> The raising operator as an unbounded operator with domain the Schwartz submodule.

```lean
def raisingOperator : Q.HS →ₗ.[ℂ] Q.HS
```

**`QuantumMechanics.HarmonicOscillator.loweringOperator_apply`**, a lemma, [line 200](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HarmonicOscillator/LadderOperators.lean#L200).

```lean
lemma loweringOperator_apply (ψ : SchwartzSubmodule d) :
    Q.loweringOperator i ψ =
      schwartzEquiv volume (Q.loweringCLM i ((schwartzEquiv volume).symm ψ))
```

**`QuantumMechanics.HarmonicOscillator.raisingOperator_apply`**, a lemma, [line 205](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HarmonicOscillator/LadderOperators.lean#L205).

```lean
lemma raisingOperator_apply (ψ : SchwartzSubmodule d) :
    Q.raisingOperator i ψ =
      schwartzEquiv volume (Q.raisingCLM i ((schwartzEquiv volume).symm ψ))
```

**`QuantumMechanics.HarmonicOscillator.loweringCLM_inner`**, a lemma, [line 211](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HarmonicOscillator/LadderOperators.lean#L211).

> `⟪aᵢ f, g⟫ = ⟪f, aᵢ† g⟫` for Schwartz maps `f`, `g`.

```lean
lemma loweringCLM_inner (f g : 𝓢(Space d, ℂ)) :
    ⟪(schwartzEquiv volume (Q.loweringCLM i f) : Q.HS), schwartzEquiv volume g⟫_ℂ
      = ⟪(schwartzEquiv volume f : Q.HS), schwartzEquiv volume (Q.raisingCLM i g)⟫_ℂ
```

**`QuantumMechanics.HarmonicOscillator.raisingCLM_inner`**, a lemma, [line 221](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HarmonicOscillator/LadderOperators.lean#L221).

> `⟪aᵢ† f, g⟫ = ⟪f, aᵢ g⟫` for Schwartz maps `f`, `g`.

```lean
lemma raisingCLM_inner (f g : 𝓢(Space d, ℂ)) :
    ⟪(schwartzEquiv volume (Q.raisingCLM i f) : Q.HS), schwartzEquiv volume g⟫_ℂ
      = ⟪(schwartzEquiv volume f : Q.HS), schwartzEquiv volume (Q.loweringCLM i g)⟫_ℂ
```

**`QuantumMechanics.HarmonicOscillator.loweringOperator_isFormalAdjoint_raisingOperator`**, a lemma, [line 227](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HarmonicOscillator/LadderOperators.lean#L227).

> The raising operator is the formal adjoint of the lowering operator.

```lean
lemma loweringOperator_isFormalAdjoint_raisingOperator :
    (Q.loweringOperator i).IsFormalAdjoint (Q.raisingOperator i)
```

## Depends on

- [Kronecker delta](../../mathematics/kroneckerdelta/basic.md)
- [The quantum harmonic oscillator](basic.md)
- [Position operators](../operators/position.md)

## Proof depends on

- [Commutation relations](../operators/commutation.md)

## Sources

- [Physlib/QuantumMechanics/HarmonicOscillator/LadderOperators.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HarmonicOscillator/LadderOperators.lean)
