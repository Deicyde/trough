---
declaration: module
origin: cited
lean: QuantumMechanics.angularMomentumCLM, QuantumMechanics.angularMomentumCLM_apply_fun, QuantumMechanics.angularMomentumCLM_apply, QuantumMechanics.angularMomentumCLM_antisymm, QuantumMechanics.angularMomentumCLM_eq_zero, QuantumMechanics.angularMomentumOperatorSqr, QuantumMechanics.angularMomentumOperatorSqr_apply_fun, QuantumMechanics.angularMomentumOperatorSqr_apply
statement: formalized
proof: formalized
---

# Angular momentum operator

The module `Physlib.QuantumMechanics.Operators.AngularMomentum`, [Physlib/QuantumMechanics/Operators/AngularMomentum.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/AngularMomentum.lean): 46 declarations, 19 with a docstring.

## i. Overview

> In this module we introduce several angular momentum operators for quantum mechanics on `Space d`.
> Each component also acts symmetrically on `SpaceDHilbertSpace d` with domain `SchwartzSubmodule d`.
> We prove its symmetry and commutation relations.

## ii. Key results

> Definitions:
> - `angularMomentumCLM` : (components of) the angular momentum operator acting on Schwartz maps
>     `𝓢(Space d, ℂ)` as `𝐱ᵢ∘𝐩ⱼ - 𝐱ⱼ∘𝐩ᵢ`.
> - `angularMomentumOperatorSqr` : the operator acting on Schwartz maps `𝓢(Space d, ℂ)`
>     as `½ ∑ᵢⱼ 𝐋ᵢⱼ∘𝐋ᵢⱼ`.
> - `angularMomentumOperator2D` : the (pseudo)scalar angular momentum operator for `d = 2`.
> - `angularMomentumOperator3D` : the (pseudo)vector angular momentum operator for `d = 3`.
> - `angularMomentumOperator` : each component as a partially defined operator on
>     `SpaceDHilbertSpace d`, preserving the dense Schwartz submodule.
> - `angularMomentumSqOperator` : angular momentum squared on the same Schwartz domain.
>
> Lemmas:
> - `angularMomentumOperator_isSymmetric` : angular momentum is symmetric on the Schwartz domain.
> - `angularMomentumSqOperator_isSymmetric` : its sum of component squares is also symmetric.
> - `angularMomentum_commutation_angularMomentum` : angular momenta generate an `𝔰𝔬(d)` algebra.
>
> Notation:
> - `𝐋` for `angularMomentumCLM`
> - `𝐋²` for `angularMomentumOperatorSqr`

## iv. References

> * None.

## A. Angular momentum operator

**`QuantumMechanics.angularMomentumCLM`**, a def, [line 76](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/AngularMomentum.lean#L76).

> Component `i j` of the angular momentum operator is the continuous linear map
> from `𝓢(Space d, ℂ)` to itself defined by `𝐋ᵢⱼ ≔ 𝐱ᵢ∘𝐩ⱼ - 𝐱ⱼ∘𝐩ᵢ`.

```lean
def angularMomentumCLM {d : ℕ} (i j : Fin d) : 𝓢(Space d, ℂ) →L[ℂ] 𝓢(Space d, ℂ)
```

**`QuantumMechanics.angularMomentumCLM_apply_fun`**, a lemma, [line 85](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/AngularMomentum.lean#L85).

```lean
lemma angularMomentumCLM_apply_fun {d : ℕ} (i j : Fin d) (ψ : 𝓢(Space d, ℂ)) :
    𝐋 i j ψ = 𝐱 i (𝐩 j ψ) - 𝐱 j (𝐩 i ψ)
```

**`QuantumMechanics.angularMomentumCLM_apply`**, a lemma, [line 88](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/AngularMomentum.lean#L88).

```lean
lemma angularMomentumCLM_apply {d : ℕ} (i j : Fin d) (ψ : 𝓢(Space d, ℂ)) (x : Space d) :
    𝐋 i j ψ x = 𝐱 i (𝐩 j ψ) x - 𝐱 j (𝐩 i ψ) x
```

### A.1 Antisymmetry

**`QuantumMechanics.angularMomentumCLM_antisymm`**, a lemma, [line 98](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/AngularMomentum.lean#L98).

> The angular momentum operator is antisymmetric, `𝐋ᵢⱼ = -𝐋ⱼᵢ`

```lean
lemma angularMomentumCLM_antisymm {d : ℕ} (i j : Fin d) : 𝐋 i j = -𝐋 j i
```

**`QuantumMechanics.angularMomentumCLM_eq_zero`**, a lemma, [line 102](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/AngularMomentum.lean#L102).

> Angular momentum operator components with repeated index vanish, `𝐋ᵢᵢ = 0`.

```lean
lemma angularMomentumCLM_eq_zero {d : ℕ} (i : Fin d) : 𝐋 i i = 0
```

## B. Angular momentum squared operator

**`QuantumMechanics.angularMomentumOperatorSqr`**, a def, [line 111](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/AngularMomentum.lean#L111).

> The square of the angular momentum operator, `𝐋² ≔ ½ ∑ᵢⱼ 𝐋ᵢⱼ∘𝐋ᵢⱼ`.

```lean
def angularMomentumOperatorSqr {d : ℕ} : 𝓢(Space d, ℂ) →L[ℂ] 𝓢(Space d, ℂ)
```

**`QuantumMechanics.angularMomentumOperatorSqr_apply_fun`**, a lemma, [line 120](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/AngularMomentum.lean#L120).

```lean
lemma angularMomentumOperatorSqr_apply_fun {d : ℕ} (ψ : 𝓢(Space d, ℂ)) :
    𝐋² ψ = (2 : ℂ)⁻¹ • ∑ i, ∑ j, 𝐋 i j (𝐋 i j ψ)
```

**`QuantumMechanics.angularMomentumOperatorSqr_apply`**, a lemma, [line 125](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/AngularMomentum.lean#L125).

```lean
lemma angularMomentumOperatorSqr_apply {d : ℕ} (ψ : 𝓢(Space d, ℂ)) (x : Space d) :
    𝐋² ψ x = (2 : ℂ)⁻¹ * ∑ i, ∑ j, 𝐋 i j (𝐋 i j ψ) x
```

## C. Special cases in low dimensions

> • d = 1 : The angular momentum operator is trivial.
>
>   • d = 2 : The angular momentum operator has only one independent component, 𝐋₀₁, which may
>             be thought of as a (pseudo)scalar operator.
>
>   • d = 3 : The angular momentum operator has three independent components, 𝐋₀₁, 𝐋₁₂ and 𝐋₂₀.
>             Dualizing using the Levi-Civita symbol produces the familiar (pseudo)vector angular
>             momentum operator with components 𝐋₀ = 𝐋₁₂, 𝐋₁ = 𝐋₂₀ and 𝐋₂ = 𝐋₀₁.

**`QuantumMechanics.angularMomentumOperator1D_trivial`**, a lemma, [line 145](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/AngularMomentum.lean#L145).

> In one dimension the angular momentum operator is trivial.

```lean
lemma angularMomentumOperator1D_trivial : 𝐋[1] = 0
```

**`QuantumMechanics.angularMomentumOperator2D`**, a def, [line 150](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/AngularMomentum.lean#L150).

> The angular momentum (pseudo)scalar operator in two dimensions, `𝐋 ≔ 𝐋₀₁`.

```lean
def angularMomentumOperator2D : 𝓢(Space 2, ℂ) →L[ℂ] 𝓢(Space 2, ℂ)
```

**`QuantumMechanics.angularMomentumOperator3D`**, a def, [line 154](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/AngularMomentum.lean#L154).

> The angular momentum (pseudo)vector operator in three dimensions, `𝐋ᵢ ≔ ½ ∑ⱼₖ εᵢⱼₖ 𝐋ⱼₖ`.
> The transpose matches the convention of `Matrix.crossProductVee`, giving `(𝐋₁₂, 𝐋₂₀, 𝐋₀₁)`.

```lean
def angularMomentumOperator3D (i : Fin 3) : 𝓢(Space 3, ℂ) →L[ℂ] 𝓢(Space 3, ℂ)
```

## D. Hilbert-space angular momentum operator

**`QuantumMechanics.angularMomentumOperator`**, a def, [line 168](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/AngularMomentum.lean#L168).

> Component `i j` of angular momentum on the Hilbert space, with Schwartz domain.
> This transports the existing Schwartz-space operator `𝐋 i j`.

```lean
def angularMomentumOperator : SpaceDHilbertSpace d →ₗ.[ℂ] SpaceDHilbertSpace d
```

**`QuantumMechanics.angularMomentumOperator_domain_eq`**, a lemma, [line 172](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/AngularMomentum.lean#L172).

```lean
lemma angularMomentumOperator_domain_eq :
    (angularMomentumOperator i j).domain = SchwartzSubmodule d
```

**`QuantumMechanics.angularMomentumOperator_apply`**, a lemma, [line 175](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/AngularMomentum.lean#L175).

```lean
lemma angularMomentumOperator_apply (ψ : SchwartzSubmodule d) :
    angularMomentumOperator i j ψ =
      schwartzEquiv volume (𝐋 i j ((schwartzEquiv volume).symm ψ))
```

**`QuantumMechanics.angularMomentumOperator_apply_ae`**, a lemma, [line 179](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/AngularMomentum.lean#L179).

```lean
lemma angularMomentumOperator_apply_ae (ψ : SchwartzSubmodule d) :
    angularMomentumOperator i j ψ =ᵐ[volume] 𝐋 i j ((schwartzEquiv volume).symm ψ)
```

**`QuantumMechanics.angularMomentumOperator_range`**, a lemma, [line 183](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/AngularMomentum.lean#L183).

```lean
lemma angularMomentumOperator_range (ψ : SchwartzSubmodule d) :
    angularMomentumOperator i j ψ ∈ SchwartzSubmodule d
```

**`QuantumMechanics.angularMomentumOperator_hasDenseDomain`**, a lemma, [line 187](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/AngularMomentum.lean#L187).

```lean
lemma angularMomentumOperator_hasDenseDomain :
    (angularMomentumOperator i j).HasDenseDomain
```

**`QuantumMechanics.angularMomentumCLM_eq_momentum_position`**, a lemma, [line 191](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/AngularMomentum.lean#L191).

> Reversing the order of position and momentum leaves angular momentum unchanged.

```lean
lemma angularMomentumCLM_eq_momentum_position :
    𝐋 i j = 𝐩 j ∘L 𝐱 i - 𝐩 i ∘L 𝐱 j
```

**`QuantumMechanics.angularMomentumOperator_isSymmetric`**, a lemma, [line 197](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/AngularMomentum.lean#L197).

> Each angular momentum component is symmetric on the Schwartz domain.

```lean
lemma angularMomentumOperator_isSymmetric :
    (angularMomentumOperator i j).IsSymmetric
```

**`QuantumMechanics.angularMomentumOperator_isUnbounded`**, a lemma, [line 209](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/AngularMomentum.lean#L209).

> Angular momentum on the Schwartz domain is densely defined and closable.

```lean
lemma angularMomentumOperator_isUnbounded :
    (angularMomentumOperator i j).IsUnbounded
```

**`QuantumMechanics.angularMomentumCLM_inner`**, a lemma, [line 215](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/AngularMomentum.lean#L215).

> The component symmetry identity, expressed directly on Schwartz maps.

```lean
lemma angularMomentumCLM_inner (f g : 𝓢(Space d, ℂ)) :
    ⟪(schwartzEquiv volume (𝐋 i j f) : SpaceDHilbertSpace d), schwartzEquiv volume g⟫_ℂ =
      ⟪(schwartzEquiv volume f : SpaceDHilbertSpace d), schwartzEquiv volume (𝐋 i j g)⟫_ℂ
```

### D.1. Angular momentum squared on the Hilbert space

**`QuantumMechanics.angularMomentumSqOperator`**, a def, [line 227](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/AngularMomentum.lean#L227).

> Angular momentum squared on the Hilbert space, with the invariant Schwartz domain.
> This transports the existing Schwartz operator `𝐋²`, including its factor `1/2`.

```lean
def angularMomentumSqOperator : SpaceDHilbertSpace d →ₗ.[ℂ] SpaceDHilbertSpace d
```

**`QuantumMechanics.angularMomentumSqOperator_domain_eq`**, a lemma, [line 234](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/AngularMomentum.lean#L234).

```lean
lemma angularMomentumSqOperator_domain_eq :
    (angularMomentumSqOperator (d := d)).domain = SchwartzSubmodule d
```

**`QuantumMechanics.angularMomentumSqOperator_apply`**, a lemma, [line 237](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/AngularMomentum.lean#L237).

```lean
lemma angularMomentumSqOperator_apply (ψ : SchwartzSubmodule d) : angularMomentumSqOperator ψ =
    schwartzEquiv volume (𝐋² ((schwartzEquiv volume).symm ψ))
```

**`QuantumMechanics.angularMomentumSqOperator_apply_ae`**, a lemma, [line 240](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/AngularMomentum.lean#L240).

```lean
lemma angularMomentumSqOperator_apply_ae (ψ : SchwartzSubmodule d) :
    angularMomentumSqOperator ψ =ᵐ[volume] 𝐋² ((schwartzEquiv volume).symm ψ)
```

**`QuantumMechanics.angularMomentumSqOperator_range`**, a lemma, [line 244](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/AngularMomentum.lean#L244).

```lean
lemma angularMomentumSqOperator_range (ψ : SchwartzSubmodule d) :
    angularMomentumSqOperator ψ ∈ SchwartzSubmodule d
```

**`QuantumMechanics.angularMomentumSqOperator_apply_eq_sum`**, a lemma, [line 251](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/AngularMomentum.lean#L251).

> The squared operator is the sum of squares of Hilbert-space components on their
> common invariant domain. The inner applications land in Schwartz by `angularMomentumOperator_range`.

```lean
lemma angularMomentumSqOperator_apply_eq_sum (ψ : SchwartzSubmodule d) :
    angularMomentumSqOperator ψ = (2 : ℂ)⁻¹ • ∑ i, ∑ j,
      angularMomentumOperator i j
        ⟨angularMomentumOperator i j ψ, angularMomentumOperator_range i j ψ⟩
```

**`QuantumMechanics.angularMomentumSqOperator_hasDenseDomain`**, a lemma, [line 269](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/AngularMomentum.lean#L269).

```lean
lemma angularMomentumSqOperator_hasDenseDomain :
    (angularMomentumSqOperator (d := d)).HasDenseDomain
```

**`QuantumMechanics.angularMomentumSqr_inner`**, a lemma, [line 273](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/AngularMomentum.lean#L273).

> Symmetry of `𝐋²` follows by moving each component across the inner product twice.

```lean
lemma angularMomentumSqr_inner (f g : 𝓢(Space d, ℂ)) :
    ⟪(schwartzEquiv volume (𝐋² f) : SpaceDHilbertSpace d), schwartzEquiv volume g⟫_ℂ =
      ⟪(schwartzEquiv volume f : SpaceDHilbertSpace d), schwartzEquiv volume (𝐋² g)⟫_ℂ
```

**`QuantumMechanics.angularMomentumSqOperator_isSymmetric`**, a lemma, [line 281](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/AngularMomentum.lean#L281).

> Angular momentum squared is symmetric on the Schwartz domain.

```lean
lemma angularMomentumSqOperator_isSymmetric : (angularMomentumSqOperator (d := d)).IsSymmetric
```

**`QuantumMechanics.angularMomentumSqOperator_isUnbounded`**, a lemma, [line 289](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/AngularMomentum.lean#L289).

> In Physlib terminology, the squared operator is densely defined and closable.

```lean
lemma angularMomentumSqOperator_isUnbounded : (angularMomentumSqOperator (d := d)).IsUnbounded
```

## E. Algebraic relations

### E.1. Angular momentum / position

**`QuantumMechanics.angularMomentum_commutation_position`**, a lemma, [line 309](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/AngularMomentum.lean#L309).

```lean
lemma angularMomentum_commutation_position :
    ⁅𝐋 i j, 𝐱 k⁆ = (I * ℏ) • (δ[i,k] • 𝐱 j - δ[j,k] • 𝐱 i)
```

**`QuantumMechanics.angularMomentum_commutation_radiusRegPow`**, a lemma, [line 317](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/AngularMomentum.lean#L317).

```lean
lemma angularMomentum_commutation_radiusRegPow : ⁅𝐋 i j, 𝐫₀[d] ε s⁆ = 0
```

**`QuantumMechanics.angularMomentum_comp_radiusRegPow_commute`**, a lemma, [line 323](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/AngularMomentum.lean#L323).

```lean
lemma angularMomentum_comp_radiusRegPow_commute : 𝐋 i j ∘L 𝐫₀ ε s = 𝐫₀ ε s ∘L 𝐋 i j
```

**`QuantumMechanics.angularMomentumSqr_commutation_radiusRegPow`**, a lemma, [line 327](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/AngularMomentum.lean#L327).

```lean
lemma angularMomentumSqr_commutation_radiusRegPow : ⁅𝐋²[d], 𝐫₀[d] ε s⁆ = 0
```

**`QuantumMechanics.angularMomentumSqr_comp_radiusRegPow_commute`**, a lemma, [line 330](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/AngularMomentum.lean#L330).

```lean
lemma angularMomentumSqr_comp_radiusRegPow_commute : 𝐋² ∘L 𝐫₀[d] ε s = 𝐫₀ ε s ∘L 𝐋²
```

**`QuantumMechanics.angularMomentum_cyclic_position`**, a lemma, [line 336](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/AngularMomentum.lean#L336).

> `𝐋ᵢⱼ𝐱ₖ + 𝐋ⱼₖ𝐱ᵢ + 𝐋ₖᵢ𝐱ⱼ = 0`; in three dimensions this is `𝐋 · 𝐱 = 0`.
> The identity is trivial unless `i`, `j`, `k` are pairwise distinct, so it has no content in
> fewer than three dimensions.

```lean
lemma angularMomentum_cyclic_position :
    𝐋 i j ∘L 𝐱 k + 𝐋 j k ∘L 𝐱 i + 𝐋 k i ∘L 𝐱 j = 0
```

### E.2. Angular momentum / momentum

**`QuantumMechanics.angularMomentum_commutation_momentum`**, a lemma, [line 351](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/AngularMomentum.lean#L351).

```lean
lemma angularMomentum_commutation_momentum :
    ⁅𝐋 i j, 𝐩 k⁆ = (I * ℏ) • (δ[i,k] • 𝐩 j - δ[j,k] • 𝐩 i)
```

**`QuantumMechanics.momentum_comp_angularMomentum_eq`**, a lemma, [line 357](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/AngularMomentum.lean#L357).

```lean
lemma momentum_comp_angularMomentum_eq :
    𝐩 k ∘L 𝐋 i j = 𝐋 i j ∘L 𝐩 k - (I * ℏ) • (δ[i,k] • 𝐩 j - δ[j,k] • 𝐩 i)
```

**`QuantumMechanics.angularMomentum_commutation_momentumSqr`**, a lemma, [line 362](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/AngularMomentum.lean#L362).

```lean
lemma angularMomentum_commutation_momentumSqr : ⁅𝐋 i j, 𝐩[d] ⬝ᵥ 𝐩⁆ = 0
```

**`QuantumMechanics.momentumSqr_comp_angularMomentum_commute`**, a lemma, [line 367](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/AngularMomentum.lean#L367).

```lean
lemma momentumSqr_comp_angularMomentum_commute : (𝐩 ⬝ᵥ 𝐩) ∘L 𝐋 i j = 𝐋 i j ∘L (𝐩 ⬝ᵥ 𝐩)
```

**`QuantumMechanics.angularMomentumSqr_commutation_momentumSqr`**, a lemma, [line 371](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/AngularMomentum.lean#L371).

```lean
lemma angularMomentumSqr_commutation_momentumSqr : ⁅𝐋²[d], 𝐩[d] ⬝ᵥ 𝐩⁆ = 0
```

**`QuantumMechanics.angularMomentum_cyclic_momentum`**, a lemma, [line 377](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/AngularMomentum.lean#L377).

> `𝐋ᵢⱼ𝐩ₖ + 𝐋ⱼₖ𝐩ᵢ + 𝐋ₖᵢ𝐩ⱼ = 0`; in three dimensions this is `𝐋 · 𝐩 = 0`.
> The identity is trivial unless `i`, `j`, `k` are pairwise distinct, so it has no content in
> fewer than three dimensions.

```lean
lemma angularMomentum_cyclic_momentum :
    𝐋 i j ∘L 𝐩 k + 𝐋 j k ∘L 𝐩 i + 𝐋 k i ∘L 𝐩 j = 0
```

### E.3. Angular momentum / angular momentum

**`QuantumMechanics.angularMomentum_commutation_angularMomentum`**, a lemma, [line 389](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/AngularMomentum.lean#L389).

```lean
lemma angularMomentum_commutation_angularMomentum : ⁅𝐋 i j, 𝐋 k l⁆ =
    (I * ℏ) • (δ[i,k] • 𝐋 j l - δ[i,l] • 𝐋 j k - δ[j,k] • 𝐋 i l + δ[j,l] • 𝐋 i k)
```

**`QuantumMechanics.angularMomentumSqr_commutation_angularMomentum`**, a lemma, [line 398](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/AngularMomentum.lean#L398).

```lean
lemma angularMomentumSqr_commutation_angularMomentum : ⁅𝐋²[d], 𝐋 i j⁆ = 0
```

### E.4. Angular momentum / dilation operator

> Angular momentum commutes with the dilation operator `𝐱 · 𝐩`.

**`QuantumMechanics.angularMomentum_commutation_positionDotMomentum`**, a lemma, [line 415](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/AngularMomentum.lean#L415).

```lean
lemma angularMomentum_commutation_positionDotMomentum : ⁅𝐋 i j, 𝐱[d] ⬝ᵥ 𝐩⁆ = 0
```

## Depends on

- [Kronecker delta](../../mathematics/kroneckerdelta/basic.md)
- [The hat map on three-dimensional vectors](../../mathematics/modules/crossproductmatrix.md)
- [Momentum operators](momentum.md)
- [Position operators](position.md)

## Proof depends on

- [Commutation relations (Operators/Commutation)](commutation.md)

## Sources

- [Physlib/QuantumMechanics/Operators/AngularMomentum.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/AngularMomentum.lean)
