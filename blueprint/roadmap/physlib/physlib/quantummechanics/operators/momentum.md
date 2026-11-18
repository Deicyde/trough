---
declaration: module
origin: cited
lean: QuantumMechanics.momentumCLM, QuantumMechanics.momentumCLM_apply_fun, QuantumMechanics.momentumCLM_apply, QuantumMechanics.momentumOperator, QuantumMechanics.momentumOperator_apply, QuantumMechanics.momentumOperator_apply_ae, QuantumMechanics.momentumOperator_range, QuantumMechanics.momentumOperator_hasDenseDomain
statement: formalized
proof: formalized
---

# Momentum operators

The module `Physlib.QuantumMechanics.Operators.Momentum`, [Physlib/QuantumMechanics/Operators/Momentum.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Momentum.lean): 14 declarations, 4 with a docstring.

## i. Overview

> In this module we introduce several momentum operators for quantum mechanics on `Space d`.

## ii. Key results

> Definitions:
> - `momentumCLM` : (components of) the momentum vector operator acting on Schwartz maps
>     `𝓢(Space d, ℂ)` as `-iℏ∂ᵢ`.
> - `momentumOperator` : a symmetric unbounded operator acting on the Schwartz submodule
>     of the Hilbert space `SpaceDHilbertSpace d`.
>
> Notation:
> - `𝐩` for `momentumOperator`

## iv. References

> * None.

## A. Momentum vector operator

**`QuantumMechanics.momentumCLM`**, a def, [line 64](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Momentum.lean#L64).

> Component `i` of the momentum operator is the continuous linear map
> from `𝓢(Space d, ℂ)` to itself which maps `ψ` to `-iℏ ∂ᵢψ`.

```lean
def momentumCLM : 𝓢(Space d, ℂ) →L[ℂ] 𝓢(Space d, ℂ)
```

**`QuantumMechanics.momentumCLM_apply_fun`**, a lemma, [line 74](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Momentum.lean#L74).

```lean
lemma momentumCLM_apply_fun (ψ : 𝓢(Space d, ℂ)) : 𝐩 i ψ = (-I * ℏ) • ∂[i] ψ
```

**`QuantumMechanics.momentumCLM_apply`**, a lemma, [line 77](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Momentum.lean#L77).

```lean
lemma momentumCLM_apply (ψ : 𝓢(Space d, ℂ)) (x : Space d) : 𝐩 i ψ x = -I * ℏ * ∂[i] ψ x
```

## B. Unbounded momentum vector operator

**`QuantumMechanics.momentumOperator`**, a def, [line 92](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Momentum.lean#L92).

> The momentum operator as a LinearPMap with domain the Schwartz submodule.

```lean
def momentumOperator : SpaceDHilbertSpace d →ₗ.[ℂ] SpaceDHilbertSpace d
```

**`QuantumMechanics.momentumOperator_apply`**, a lemma, [line 99](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Momentum.lean#L99).

```lean
lemma momentumOperator_apply (ψ : SchwartzSubmodule d) :
    𝓟 i ψ = schwartzEquiv volume (𝐩 i ((schwartzEquiv volume).symm ψ))
```

**`QuantumMechanics.momentumOperator_apply_ae`**, a lemma, [line 102](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Momentum.lean#L102).

```lean
lemma momentumOperator_apply_ae (ψ : SchwartzSubmodule d) :
    𝓟 i ψ =ᵐ[volume] 𝐩 i ((schwartzEquiv volume).symm ψ)
```

**`QuantumMechanics.momentumOperator_range`**, a lemma, [line 106](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Momentum.lean#L106).

```lean
lemma momentumOperator_range (ψ : SchwartzSubmodule d) : 𝓟 i ψ ∈ SchwartzSubmodule d
```

**`QuantumMechanics.momentumOperator_hasDenseDomain`**, a lemma, [line 109](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Momentum.lean#L109).

```lean
lemma momentumOperator_hasDenseDomain : (𝓟 i).HasDenseDomain
```

**`QuantumMechanics.momentumOperator_isSymmetric`**, a lemma, [line 111](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Momentum.lean#L111).

```lean
lemma momentumOperator_isSymmetric : (𝓟 i).IsSymmetric
```

**`QuantumMechanics.momentumCLM_inner`**, a lemma, [line 142](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Momentum.lean#L142).

> The momentum operator is symmetric on Schwartz maps, in terms of `momentumCLM`.

```lean
lemma momentumCLM_inner (f g : 𝓢(Space d, ℂ)) :
    ⟪(schwartzEquiv volume (𝐩 i f) : SpaceDHilbertSpace d), schwartzEquiv volume g⟫_ℂ
      = ⟪(schwartzEquiv volume f : SpaceDHilbertSpace d), schwartzEquiv volume (𝐩 i g)⟫_ℂ
```

**`QuantumMechanics.momentumOperator_isUnbounded`**, a lemma, [line 149](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Momentum.lean#L149).

```lean
lemma momentumOperator_isUnbounded : (𝓟 i).IsUnbounded
```

**`QuantumMechanics.momentumSqOperator`**, a def, [line 155](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Momentum.lean#L155).

> The square of the momentum operator.

```lean
def momentumSqOperator : SpaceDHilbertSpace d →ₗ.[ℂ] SpaceDHilbertSpace d
```

**`QuantumMechanics.momentumSqOperator_eq`**, a lemma, [line 158](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Momentum.lean#L158).

```lean
lemma momentumSqOperator_eq :
    momentumSqOperator (d := d) = sum fun i ↦ (𝓟 i).comp (𝓟 i) (momentumOperator_range i)
```

**`QuantumMechanics.momentumSqOperator_domain_eq`**, a lemma, [line 161](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Momentum.lean#L161).

```lean
lemma momentumSqOperator_domain_eq : momentumSqOperator.domain = SchwartzSubmodule d
```

## Depends on

- [Schwartz submodule](../hilbertspaces/spaced/schwartzsubmodule.md)
- [Unbounded operators (Operators/Unbounded)](unbounded.md)
- [Planck's constant](../planckconstant.md)
- [Derivatives on Space](../../spaceandtime/space/part-01/derivatives-basic.md)

## Sources

- [Physlib/QuantumMechanics/Operators/Momentum.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Momentum.lean)
