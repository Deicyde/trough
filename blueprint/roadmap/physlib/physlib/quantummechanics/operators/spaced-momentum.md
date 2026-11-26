---
declaration: module
origin: cited
lean: QuantumMechanics.momentumCLM, QuantumMechanics.momentumCLM_apply_fun, QuantumMechanics.momentumCLM_apply, QuantumMechanics.momentumOperator, QuantumMechanics.momentumOperator_apply, QuantumMechanics.momentumOperator_apply_ae, QuantumMechanics.momentumOperator_range, QuantumMechanics.momentumOperator_hasDenseDomain
statement: formalized
proof: formalized
---

# Momentum operators

The module `Physlib.QuantumMechanics.Operators.SpaceD.Momentum`, [Physlib/QuantumMechanics/Operators/SpaceD/Momentum.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/SpaceD/Momentum.lean): 15 declarations, 5 with a docstring.

## i. Overview

> In this module we introduce several momentum operators for quantum mechanics on `Space d`.

## ii. Key results

> Definitions:
> - `momentumCLM` : (components of) the momentum vector operator acting on Schwartz maps
>     `𝓢(Space d, ℂ)` as `-iℏ∂ᵢ`.
> - `momentumOperator` : a symmetric unbounded operator acting on the Schwartz submodule
>     of the Hilbert space `SpaceDHilbertSpace d`.
>
> Results:
> - `integral_mul_momentumCLM` : integration by parts of `momentumCLM` against a function of
>     temperate growth.
>
> Notation:
> - `𝐩` for `momentumOperator`

## iv. References

> * None.

## A. Momentum vector operator

**`QuantumMechanics.momentumCLM`**, a def, [line 70](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/SpaceD/Momentum.lean#L70).

> Component `i` of the momentum operator is the continuous linear map
> from `𝓢(Space d, ℂ)` to itself which maps `ψ` to `-iℏ ∂ᵢψ`.

```lean
def momentumCLM : 𝓢(Space d, ℂ) →L[ℂ] 𝓢(Space d, ℂ)
```

**`QuantumMechanics.momentumCLM_apply_fun`**, a lemma, [line 80](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/SpaceD/Momentum.lean#L80).

```lean
lemma momentumCLM_apply_fun (ψ : 𝓢(Space d, ℂ)) : 𝐩 i ψ = (-I * ℏ) • ∂[i] ψ
```

**`QuantumMechanics.momentumCLM_apply`**, a lemma, [line 83](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/SpaceD/Momentum.lean#L83).

```lean
lemma momentumCLM_apply (ψ : 𝓢(Space d, ℂ)) (x : Space d) : 𝐩 i ψ x = -I * ℏ * ∂[i] ψ x
```

## B. Unbounded momentum vector operator

**`QuantumMechanics.momentumOperator`**, a def, [line 98](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/SpaceD/Momentum.lean#L98).

> The momentum operator as a LinearPMap with domain the Schwartz submodule.

```lean
def momentumOperator : SpaceDHilbertSpace d →ₗ.[ℂ] SpaceDHilbertSpace d
```

**`QuantumMechanics.momentumOperator_apply`**, a lemma, [line 105](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/SpaceD/Momentum.lean#L105).

```lean
lemma momentumOperator_apply (ψ : SchwartzSubmodule d) :
    𝓟 i ψ = schwartzEquiv volume (𝐩 i ((schwartzEquiv volume).symm ψ))
```

**`QuantumMechanics.momentumOperator_apply_ae`**, a lemma, [line 108](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/SpaceD/Momentum.lean#L108).

```lean
lemma momentumOperator_apply_ae (ψ : SchwartzSubmodule d) :
    𝓟 i ψ =ᵐ[volume] 𝐩 i ((schwartzEquiv volume).symm ψ)
```

**`QuantumMechanics.momentumOperator_range`**, a lemma, [line 112](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/SpaceD/Momentum.lean#L112).

```lean
lemma momentumOperator_range (ψ : SchwartzSubmodule d) : 𝓟 i ψ ∈ SchwartzSubmodule d
```

**`QuantumMechanics.momentumOperator_hasDenseDomain`**, a lemma, [line 115](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/SpaceD/Momentum.lean#L115).

```lean
lemma momentumOperator_hasDenseDomain : (𝓟 i).HasDenseDomain
```

**`QuantumMechanics.momentumOperator_isSymmetric`**, a lemma, [line 117](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/SpaceD/Momentum.lean#L117).

```lean
lemma momentumOperator_isSymmetric : (𝓟 i).IsSymmetric
```

**`QuantumMechanics.momentumCLM_inner`**, a lemma, [line 148](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/SpaceD/Momentum.lean#L148).

> The momentum operator is symmetric on Schwartz maps, in terms of `momentumCLM`.

```lean
lemma momentumCLM_inner (f g : 𝓢(Space d, ℂ)) :
    ⟪(schwartzEquiv volume (𝐩 i f) : SpaceDHilbertSpace d), schwartzEquiv volume g⟫_ℂ
      = ⟪(schwartzEquiv volume f : SpaceDHilbertSpace d), schwartzEquiv volume (𝐩 i g)⟫_ℂ
```

**`QuantumMechanics.momentumOperator_isUnbounded`**, a lemma, [line 155](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/SpaceD/Momentum.lean#L155).

```lean
lemma momentumOperator_isUnbounded : (𝓟 i).IsUnbounded
```

**`QuantumMechanics.momentumSqOperator`**, a def, [line 161](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/SpaceD/Momentum.lean#L161).

> The square of the momentum operator.

```lean
def momentumSqOperator : SpaceDHilbertSpace d →ₗ.[ℂ] SpaceDHilbertSpace d
```

**`QuantumMechanics.momentumSqOperator_eq`**, a lemma, [line 164](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/SpaceD/Momentum.lean#L164).

```lean
lemma momentumSqOperator_eq :
    momentumSqOperator (d := d) = sum fun i ↦ (𝓟 i).comp (𝓟 i) (momentumOperator_range i)
```

**`QuantumMechanics.momentumSqOperator_domain_eq`**, a lemma, [line 167](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/SpaceD/Momentum.lean#L167).

```lean
lemma momentumSqOperator_domain_eq : momentumSqOperator.domain = SchwartzSubmodule d
```

## C. Integration by parts against functions of temperate growth

**`QuantumMechanics.integral_mul_momentumCLM`**, a lemma, [line 183](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/SpaceD/Momentum.lean#L183).

> For a function `g` of temperate growth and a Schwartz map `ψ`,
> `∫ g (𝐩ᵢ ψ) = iℏ ∫ (∂ᵢ g) ψ`.

```lean
lemma integral_mul_momentumCLM {g : Space d → ℂ} (hg : g.HasTemperateGrowth)
    (ψ : 𝓢(Space d, ℂ)) :
    ∫ x, g x * 𝐩 i ψ x = I * ℏ * ∫ x, ∂[i] g x * ψ x
```

## Depends on

- [Schwartz submodule](../hilbertspaces/spaced/schwartzsubmodule.md)
- [Unbounded operators (Basic)](basic.md)
- [Planck's constant](../planckconstant.md)
- [Derivatives on Space](../../spaceandtime/space/part-01/derivatives-basic.md)

## Proof depends on

- [Functions of temperate growth](../../mathematics/formathlib/part-01/hastemperategrowth.md)

## Sources

- [Physlib/QuantumMechanics/Operators/SpaceD/Momentum.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/SpaceD/Momentum.lean)
