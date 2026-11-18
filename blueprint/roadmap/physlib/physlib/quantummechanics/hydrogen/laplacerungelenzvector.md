---
declaration: module
origin: cited
lean: QuantumMechanics.HydrogenAtom.lrlOperator, QuantumMechanics.HydrogenAtom.lrlOperator_eq, QuantumMechanics.HydrogenAtom.lrlOperator_eq', QuantumMechanics.HydrogenAtom.lrlOperator_eq'', QuantumMechanics.HydrogenAtom.angularMomentum_commutation_Ldot_p, QuantumMechanics.HydrogenAtom.angularMomentum_commutation_lrl, QuantumMechanics.HydrogenAtom.angularMomentum_commutation_lrlSqr, QuantumMechanics.HydrogenAtom.angularMomentumSqr_commutation_lrlSqr
statement: formalized
proof: formalized
---

# Laplace-Runge-Lenz vector

The module `Physlib.QuantumMechanics.Hydrogen.LaplaceRungeLenzVector`, [Physlib/QuantumMechanics/Hydrogen/LaplaceRungeLenzVector.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Hydrogen/LaplaceRungeLenzVector.lean): 13 declarations, 13 with a docstring; 29 private, not shown.

> In this file we define
> - The (regularized) LRL vector operator for the quantum mechanical hydrogen atom,
>   `𝐀(ε)ᵢ ≔ ½(𝐩ⱼ𝐋ᵢⱼ + 𝐋ᵢⱼ𝐩ⱼ) - mk·𝐫(ε)⁻¹𝐱ᵢ`.
>
> The main results are
> - The commutators `⁅𝐋ᵢⱼ, 𝐀(ε)ₖ⁆ = iℏ(δᵢₖ𝐀(ε)ⱼ - δⱼₖ𝐀(ε)ᵢ)` in `angularMomentum_commutation_lrl`
> - The cyclic relation `𝐋ᵢⱼ𝐀(ε)ₖ + 𝐋ⱼₖ𝐀(ε)ᵢ + 𝐋ₖᵢ𝐀(ε)ⱼ = 0` (in `d = 3`: `𝐋 · 𝐀(ε) = 0`) in
>   `angularMomentum_cyclic_lrl`, and with `𝐀(ε)` on the left in `lrl_cyclic_angularMomentum`
> - The commutators `⁅𝐀(ε)ᵢ, 𝐀(ε)ⱼ⁆ = (-2iℏm·𝐇(ε) + iℏmkε²·𝐫(ε)⁻³))𝐋ᵢⱼ` in `lrl_commutation_lrl`
> - The commutators `⁅𝐇(ε), 𝐀(ε)ᵢ⁆ = iℏε²(⋯)` in `hamiltonianReg_commutation_lrl`
> - The relation `𝐀(ε)² = 2m 𝐇(ε)(𝐋² + ¼ℏ²(d-1)²) + m²k² + ε²(⋯)` in `lrlOperatorSqr_eq`

**`QuantumMechanics.HydrogenAtom.lrlOperator`**, a def, [line 43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Hydrogen/LaplaceRungeLenzVector.lean#L43).

> The (regularized) Laplace-Runge-Lenz vector operator for the `d`-dimensional hydrogen atom,
> `𝐀(ε)ᵢ ≔ ½(𝐩ⱼ𝐋ᵢⱼ + 𝐋ᵢⱼ𝐩ⱼ) - mk·𝐫(ε)⁻¹𝐱ᵢ`.

```lean
def lrlOperator (ε : ℝˣ) (i : Fin d) : 𝓢(Space d, ℂ) →L[ℂ] 𝓢(Space d, ℂ)
```

**`QuantumMechanics.HydrogenAtom.lrlOperator_eq`**, a lemma, [line 47](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Hydrogen/LaplaceRungeLenzVector.lean#L47).

> `𝐀(ε)ᵢ = 𝐱ᵢ𝐩² - (𝐱ⱼ𝐩ⱼ)𝐩ᵢ + ½iℏ(d-1)𝐩ᵢ - mk·𝐫(ε)⁻¹𝐱ᵢ`

```lean
lemma lrlOperator_eq (ε : ℝˣ) (i : Fin d) : H.lrlOperator ε i = 𝐱 i ∘L (𝐩 ⬝ᵥ 𝐩)
    - (𝐱 ⬝ᵥ 𝐩) ∘L 𝐩 i + (2⁻¹ * I * ℏ * (d - 1)) • 𝐩 i - (H.m * H.k) • 𝐫₀ ε (-1) ∘L 𝐱 i
```

**`QuantumMechanics.HydrogenAtom.lrlOperator_eq'`**, a lemma, [line 72](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Hydrogen/LaplaceRungeLenzVector.lean#L72).

> `𝐀(ε)ᵢ = 𝐋ᵢⱼ𝐩ⱼ + ½iℏ(d-1)𝐩ᵢ - mk·𝐫(ε)⁻¹𝐱ᵢ`

```lean
lemma lrlOperator_eq' (ε : ℝˣ) (i : Fin d) : H.lrlOperator ε i =
    𝐋 i ⬝ᵥ 𝐩 + (2⁻¹ * I * ℏ * (d - 1)) • 𝐩 i - (H.m * H.k) • 𝐫₀ ε (-1) ∘L 𝐱 i
```

**`QuantumMechanics.HydrogenAtom.lrlOperator_eq''`**, a lemma, [line 81](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Hydrogen/LaplaceRungeLenzVector.lean#L81).

> `𝐀(ε)ᵢ = 𝐩ⱼ𝐋ᵢⱼ - ½iℏ(d-1)𝐩ᵢ - mk·𝐫(ε)⁻¹𝐱ᵢ`

```lean
lemma lrlOperator_eq'' (ε : ℝˣ) (i : Fin d) : H.lrlOperator ε i =
    𝐩 ⬝ᵥ 𝐋 i - (2⁻¹ * I * ℏ * (d - 1)) • 𝐩 i - (H.m * H.k) • 𝐫₀ ε (-1) ∘L 𝐱 i
```

**`QuantumMechanics.HydrogenAtom.angularMomentum_commutation_Ldot_p`**, a lemma, [line 100](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Hydrogen/LaplaceRungeLenzVector.lean#L100).

> A supporting piece of `angularMomentum_commutation_lrl`: how `𝐋ᵢⱼ` commutes with the
> dot-product term `𝐋ₖ⬝ᵥ𝐩` appearing in `H.lrlOperator`'s expanded form (`lrlOperator_eq'`).

```lean
lemma angularMomentum_commutation_Ldot_p (i j k : Fin d) :
    ⁅𝐋[d] i j, 𝐋 k ⬝ᵥ 𝐩⁆ =
      (I * ℏ) • (δ[i,k] • (𝐋 j ⬝ᵥ 𝐩) - δ[j,k] • (𝐋 i ⬝ᵥ 𝐩))
```

**`QuantumMechanics.HydrogenAtom.angularMomentum_commutation_lrl`**, a lemma, [line 113](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Hydrogen/LaplaceRungeLenzVector.lean#L113).

> `⁅𝐋ᵢⱼ, 𝐀(ε)ₖ⁆ = iℏ(δᵢₖ𝐀(ε)ⱼ - δⱼₖ𝐀(ε)ᵢ)`

```lean
lemma angularMomentum_commutation_lrl (ε : ℝˣ) (i j k : Fin d) : ⁅𝐋 i j, H.lrlOperator ε k⁆ =
    (I * ℏ) • (δ[i,k] • H.lrlOperator ε j - δ[j,k] • H.lrlOperator ε i)
```

**`QuantumMechanics.HydrogenAtom.angularMomentum_commutation_lrlSqr`**, a lemma, [line 124](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Hydrogen/LaplaceRungeLenzVector.lean#L124).

> `⁅𝐋ᵢⱼ, 𝐀(ε)²⁆ = 0`

```lean
lemma angularMomentum_commutation_lrlSqr (ε : ℝˣ) (i j : Fin d) :
    ⁅𝐋 i j, H.lrlOperator ε ⬝ᵥ H.lrlOperator ε⁆ = 0
```

**`QuantumMechanics.HydrogenAtom.angularMomentumSqr_commutation_lrlSqr`**, a lemma, [line 132](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Hydrogen/LaplaceRungeLenzVector.lean#L132).

> `⁅𝐋², 𝐀(ε)²⁆ = 0`

```lean
lemma angularMomentumSqr_commutation_lrlSqr (ε : ℝˣ) :
    ⁅𝐋²[d], H.lrlOperator ε ⬝ᵥ H.lrlOperator ε⁆ = 0
```

**`QuantumMechanics.HydrogenAtom.angularMomentum_cyclic_lrl`**, a lemma, [line 139](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Hydrogen/LaplaceRungeLenzVector.lean#L139).

> `𝐋ᵢⱼ𝐀(ε)ₖ + 𝐋ⱼₖ𝐀(ε)ᵢ + 𝐋ₖᵢ𝐀(ε)ⱼ = 0`; in three dimensions this is `𝐋 · 𝐀(ε) = 0`.
> The identity is trivial unless `i`, `j`, `k` are pairwise distinct, so it has no content in
> fewer than three dimensions.

```lean
lemma angularMomentum_cyclic_lrl (ε : ℝˣ) (i j k : Fin d) :
    𝐋 i j ∘L H.lrlOperator ε k + 𝐋 j k ∘L H.lrlOperator ε i + 𝐋 k i ∘L H.lrlOperator ε j = 0
```

**`QuantumMechanics.HydrogenAtom.lrl_cyclic_angularMomentum`**, a lemma, [line 157](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Hydrogen/LaplaceRungeLenzVector.lean#L157).

> `𝐀(ε)ₖ𝐋ᵢⱼ + 𝐀(ε)ᵢ𝐋ⱼₖ + 𝐀(ε)ⱼ𝐋ₖᵢ = 0`; in three dimensions this is `𝐀(ε) · 𝐋 = 0`.
> The identity is trivial unless `i`, `j`, `k` are pairwise distinct, so it has no content in
> fewer than three dimensions.

```lean
lemma lrl_cyclic_angularMomentum (ε : ℝˣ) (i j k : Fin d) :
    H.lrlOperator ε k ∘L 𝐋 i j + H.lrlOperator ε i ∘L 𝐋 j k + H.lrlOperator ε j ∘L 𝐋 k i = 0
```

**`QuantumMechanics.HydrogenAtom.lrl_commutation_lrl`**, a lemma, [line 317](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Hydrogen/LaplaceRungeLenzVector.lean#L317).

> `⁅𝐀(ε)ᵢ, 𝐀(ε)ⱼ⁆ = (-2iℏm·𝐇(ε) + iℏmkε²·𝐫(ε)⁻³)𝐋ᵢⱼ`

```lean
lemma lrl_commutation_lrl (ε : ℝˣ) (i j : Fin d) :
    ⁅H.lrlOperator ε i, H.lrlOperator ε j⁆ = ((-2 * I * ℏ * H.m) • H.hamiltonianRegCLM ε
    + (I * ℏ * H.m * H.k * ε.1 ^ 2) • 𝐫₀ ε (-3)) ∘L 𝐋 i j
```

**`QuantumMechanics.HydrogenAtom.hamiltonianReg_commutation_lrl`**, a lemma, [line 414](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Hydrogen/LaplaceRungeLenzVector.lean#L414).

> `⁅𝐇(ε), 𝐀(ε)ᵢ⁆ = iℏk·ε²𝐫(ε)⁻³𝐩ᵢ - 3ℏ²k/2·ε²𝐫(ε)⁻⁵𝐱ᵢ`

```lean
lemma hamiltonianReg_commutation_lrl (ε : ℝˣ) (i : Fin d) :
    ⁅H.hamiltonianRegCLM ε, H.lrlOperator ε i⁆ = (I * ℏ * H.k * ε.1 ^ 2) • 𝐫₀ ε (-3) ∘L 𝐩 i
    - (3 / 2 * ℏ ^ 2 * H.k * ε.1 ^ 2) • 𝐫₀ ε (-5) ∘L 𝐱 i
```

**`QuantumMechanics.HydrogenAtom.lrlOperatorSqr_eq`**, a lemma, [line 550](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Hydrogen/LaplaceRungeLenzVector.lean#L550).

> The square of the (regularized) LRL vector operator is related to the (regularized) Hamiltonian
> `𝐇(ε)` of the hydrogen atom, square of the angular momentum `𝐋²` and powers of `𝐫(ε)` as
> `𝐀(ε)² = 2m·𝐇(ε)(𝐋² + ¼ℏ²(d-1)²) + m²k²(𝟙 - ε²·𝐫(ε)⁻²) - ½(d-1)mkℏ²ε²𝐫(ε)⁻³`.

```lean
lemma lrlOperatorSqr_eq (ε : ℝˣ) : H.lrlOperator ε ⬝ᵥ H.lrlOperator ε =
    (2 * H.m) • (H.hamiltonianRegCLM ε) ∘L
      (𝐋² + (4⁻¹ * ℏ ^ 2 * (d - 1) ^ 2 : ℝ) • ContinuousLinearMap.id ℂ 𝓢(Space d, ℂ))
    + (H.m ^ 2 * H.k ^ 2) • (ContinuousLinearMap.id ℂ 𝓢(Space d, ℂ) - ε.1 ^ 2 • 𝐫₀ ε (-2))
    - (2⁻¹ * ℏ^2 * H.m * H.k * (d - 1) * ε.1 ^ 2) • 𝐫₀ ε (-3)
```

## Depends on

- [Hydrogen atom](basic.md)
- [Angular momentum operator](../operators/angularmomentum.md)

## Sources

- [Physlib/QuantumMechanics/Hydrogen/LaplaceRungeLenzVector.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Hydrogen/LaplaceRungeLenzVector.lean)
