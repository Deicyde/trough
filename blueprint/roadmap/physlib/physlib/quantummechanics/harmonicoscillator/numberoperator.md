---
declaration: module
origin: cited
lean: QuantumMechanics.HarmonicOscillator.numberCLM, QuantumMechanics.HarmonicOscillator.numberCLM_eq, QuantumMechanics.HarmonicOscillator.number_commutation_lowering, QuantumMechanics.HarmonicOscillator.number_commutation_raising, QuantumMechanics.HarmonicOscillator.number_commutation_number, QuantumMechanics.HarmonicOscillator.lowering_comp_raising, QuantumMechanics.HarmonicOscillator.numberCLM_inner, QuantumMechanics.HarmonicOscillator.sum_number_commutation_lowering
statement: formalized
proof: formalized
---

# Number operators

The module `Physlib.QuantumMechanics.HarmonicOscillator.NumberOperator`, [Physlib/QuantumMechanics/HarmonicOscillator/NumberOperator.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HarmonicOscillator/NumberOperator.lean): 17 declarations, 15 with a docstring.

## i. Overview

> The number operators `Nᵢ = aᵢ† aᵢ` of the `d`-dimensional quantum harmonic oscillator, built from
> the ladder operators of `LadderOperators.lean` and acting on Schwartz maps: their commutation
> relations with the ladder operators and with each other, and the Hamiltonian of `Basic.lean`, which
> on Schwartz maps acts as `H_N = ∑ᵢ ℏ ωᵢ (Nᵢ + ½)`, commutes with the number operators and lowers
> and raises energies by `ℏ ωᵢ`. The number operators are then lifted to unbounded operators on the
> Hilbert space with the Schwartz submodule as domain (like `momentumOperator`), where they are
> symmetric, as is the Hamiltonian.

## ii. Key results

> - `number_commutation_number`: `[Nᵢ, Nⱼ] = 0`; `number_commutation_lowering`,
>   `number_commutation_raising`: `[Nᵢ, aⱼ] = -δᵢⱼ aⱼ`, `[Nᵢ, aⱼ†] = δᵢⱼ aⱼ†`.
> - `lowering_comp_raising`: `aᵢ aᵢ† = Nᵢ + 𝟙`; `numberCLM_inner`:
>   `⟪ Nᵢ f, g⟫ = ⟪ f, Nᵢ g⟫` for Schwartz maps.
> - `sum_number_commutation_lowering`, `sum_number_commutation_raising`,
>   `sum_number_commutation_number`: with `H_N = ∑ⱼ ℏ ωⱼ (Nⱼ + ½)`, `[H_N, aᵢ] = -ℏ ωᵢ aᵢ`,
>   `[H_N, aᵢ†] = ℏ ωᵢ aᵢ†`, `[H_N, Nᵢ] = 0`.
> - `sum_number_apply`: `H_N ψ = (1/2m) ∑ᵢ pᵢ (pᵢ ψ) + V ψ` on Schwartz maps;
>   `hamiltonian_apply_schwartz`: the Hamiltonian of `Basic.lean` acts on Schwartz maps as `H_N`;
>   `hamiltonian_inner_schwartz`: it is symmetric on the Schwartz submodule.
> - `numberOperator_isSymmetric`: the number operators are symmetric.

## iv. References

> * None.

## A. Number operators

### A.1. Definition

**`QuantumMechanics.HarmonicOscillator.numberCLM`**, a def, [line 82](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HarmonicOscillator/NumberOperator.lean#L82).

> The number operator `Nᵢ = aᵢ† aᵢ`.

```lean
def numberCLM : 𝓢(Space d, ℂ) →L[ℂ] 𝓢(Space d, ℂ)
```

**`QuantumMechanics.HarmonicOscillator.numberCLM_eq`**, a lemma, [line 84](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HarmonicOscillator/NumberOperator.lean#L84).

```lean
lemma numberCLM_eq : Q.numberCLM i = Q.raisingCLM i ∘L Q.loweringCLM i
```

### A.2. Commutation relations

**`QuantumMechanics.HarmonicOscillator.number_commutation_lowering`**, a lemma, [line 93](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HarmonicOscillator/NumberOperator.lean#L93).

> `[Nᵢ, aⱼ] = -δᵢⱼ aⱼ`.

```lean
lemma number_commutation_lowering :
    ⁅Q.numberCLM i, Q.loweringCLM j⁆ = -(δ[i,j] • Q.loweringCLM j)
```

**`QuantumMechanics.HarmonicOscillator.number_commutation_raising`**, a lemma, [line 102](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HarmonicOscillator/NumberOperator.lean#L102).

> `[Nᵢ, aⱼ†] = δᵢⱼ aⱼ†`.

```lean
lemma number_commutation_raising :
    ⁅Q.numberCLM i, Q.raisingCLM j⁆ = δ[i,j] • Q.raisingCLM j
```

**`QuantumMechanics.HarmonicOscillator.number_commutation_number`**, a lemma, [line 111](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HarmonicOscillator/NumberOperator.lean#L111).

> `[Nᵢ, Nⱼ] = 0`.

```lean
lemma number_commutation_number : ⁅Q.numberCLM i, Q.numberCLM j⁆ = 0
```

**`QuantumMechanics.HarmonicOscillator.lowering_comp_raising`**, a lemma, [line 122](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HarmonicOscillator/NumberOperator.lean#L122).

> `aᵢ aᵢ† = Nᵢ + 𝟙`.

```lean
lemma lowering_comp_raising :
    Q.loweringCLM i ∘L Q.raisingCLM i =
      Q.numberCLM i + ContinuousLinearMap.id ℂ 𝓢(Space d, ℂ)
```

### A.3. Inner products

**`QuantumMechanics.HarmonicOscillator.numberCLM_inner`**, a lemma, [line 137](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HarmonicOscillator/NumberOperator.lean#L137).

> `⟪Nᵢ f, g⟫ = ⟪f, Nᵢ g⟫` for Schwartz maps `f`, `g`.

```lean
lemma numberCLM_inner (f g : 𝓢(Space d, ℂ)) :
    ⟪(schwartzEquiv volume (Q.numberCLM i f) : Q.HS), schwartzEquiv volume g⟫_ℂ
      = ⟪(schwartzEquiv volume f : Q.HS), schwartzEquiv volume (Q.numberCLM i g)⟫_ℂ
```

## B. Hamiltonian

> On Schwartz maps the Hamiltonian of `Basic.lean` acts as `H_N = ∑ⱼ ℏ ωⱼ (Nⱼ + ½)`
> (`hamiltonian_apply_schwartz`); the lemmas below are stated for this sum.

### B.1. Commutation relations with the ladder and number operators

**`QuantumMechanics.HarmonicOscillator.sum_number_commutation_lowering`**, a lemma, [line 158](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HarmonicOscillator/NumberOperator.lean#L158).

> `[∑ⱼ ℏ ωⱼ (Nⱼ + ½), aᵢ] = -ℏ ωᵢ aᵢ`.

```lean
lemma sum_number_commutation_lowering :
    ⁅∑ j, ((ℏ * Q.ω j : ℝ) : ℂ) •
        (Q.numberCLM j + (2⁻¹ : ℂ) • ContinuousLinearMap.id ℂ 𝓢(Space d, ℂ)),
      Q.loweringCLM i⁆ = -(((ℏ * Q.ω i : ℝ) : ℂ) • Q.loweringCLM i)
```

**`QuantumMechanics.HarmonicOscillator.sum_number_commutation_raising`**, a lemma, [line 168](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HarmonicOscillator/NumberOperator.lean#L168).

> `[∑ⱼ ℏ ωⱼ (Nⱼ + ½), aᵢ†] = ℏ ωᵢ aᵢ†`.

```lean
lemma sum_number_commutation_raising :
    ⁅∑ j, ((ℏ * Q.ω j : ℝ) : ℂ) •
        (Q.numberCLM j + (2⁻¹ : ℂ) • ContinuousLinearMap.id ℂ 𝓢(Space d, ℂ)),
      Q.raisingCLM i⁆ = ((ℏ * Q.ω i : ℝ) : ℂ) • Q.raisingCLM i
```

**`QuantumMechanics.HarmonicOscillator.sum_number_commutation_number`**, a lemma, [line 178](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HarmonicOscillator/NumberOperator.lean#L178).

> `[∑ⱼ ℏ ωⱼ (Nⱼ + ½), Nᵢ] = 0`.

```lean
lemma sum_number_commutation_number :
    ⁅∑ j, ((ℏ * Q.ω j : ℝ) : ℂ) •
        (Q.numberCLM j + (2⁻¹ : ℂ) • ContinuousLinearMap.id ℂ 𝓢(Space d, ℂ)),
      Q.numberCLM i⁆ = 0
```

### B.2. The Hamiltonian on Schwartz maps

**`QuantumMechanics.HarmonicOscillator.sum_number_apply`**, a lemma, [line 191](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HarmonicOscillator/NumberOperator.lean#L191).

> On Schwartz maps, `∑ᵢ ℏ ωᵢ (Nᵢ + ½) ψ = (1/2m) ∑ᵢ pᵢ (pᵢ ψ) + V ψ`.

```lean
lemma sum_number_apply (ψ : 𝓢(Space d, ℂ)) (x : Space d) :
    (∑ j, ((ℏ * Q.ω j : ℝ) : ℂ) •
      (Q.numberCLM j + (2⁻¹ : ℂ) • ContinuousLinearMap.id ℂ 𝓢(Space d, ℂ))) ψ x =
      ((2 * Q.m : ℝ) : ℂ)⁻¹ * ∑ i, 𝐩 i (𝐩 i ψ) x + (Q.potentialFunction x : ℂ) * ψ x
```

**`QuantumMechanics.HarmonicOscillator.schwartzSubmodule_le_hamiltonian_domain`**, a lemma, [line 220](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HarmonicOscillator/NumberOperator.lean#L220).

> The Schwartz submodule is contained in the domain of the Hamiltonian.

```lean
lemma schwartzSubmodule_le_hamiltonian_domain : SchwartzSubmodule d ≤ Q.hamiltonian.domain
```

**`QuantumMechanics.HarmonicOscillator.hamiltonian_apply_schwartz`**, a lemma, [line 228](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HarmonicOscillator/NumberOperator.lean#L228).

> On a Schwartz map, the Hamiltonian `kineticOperator + potentialOperator` of `Basic.lean` acts as
> `∑ᵢ ℏ ωᵢ (Nᵢ + ½)`.

```lean
lemma hamiltonian_apply_schwartz (f : 𝓢(Space d, ℂ))
    (h : (schwartzEquiv volume f : Q.HS) ∈ Q.hamiltonian.domain) :
    Q.hamiltonian ⟨schwartzEquiv volume f, h⟩ = schwartzEquiv volume
      ((∑ j, ((ℏ * Q.ω j : ℝ) : ℂ) •
        (Q.numberCLM j + (2⁻¹ : ℂ) • ContinuousLinearMap.id ℂ 𝓢(Space d, ℂ))) f)
```

**`QuantumMechanics.HarmonicOscillator.hamiltonian_inner_schwartz`**, a lemma, [line 257](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HarmonicOscillator/NumberOperator.lean#L257).

> `⟪H f, g⟫ = ⟪f, H g⟫` for Schwartz maps `f`, `g`: the Hamiltonian is symmetric on the Schwartz
> submodule.

```lean
lemma hamiltonian_inner_schwartz (f g : 𝓢(Space d, ℂ))
    (hf : (schwartzEquiv volume f : Q.HS) ∈ Q.hamiltonian.domain)
    (hg : (schwartzEquiv volume g : Q.HS) ∈ Q.hamiltonian.domain) :
    ⟪Q.hamiltonian ⟨schwartzEquiv volume f, hf⟩, (schwartzEquiv volume g : Q.HS)⟫_ℂ
      = ⟪(schwartzEquiv volume f : Q.HS), Q.hamiltonian ⟨schwartzEquiv volume g, hg⟩⟫_ℂ
```

## C. The number operators as unbounded operators

**`QuantumMechanics.HarmonicOscillator.numberOperator`**, a def, [line 275](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HarmonicOscillator/NumberOperator.lean#L275).

> The number operator as an unbounded operator with domain the Schwartz submodule.

```lean
def numberOperator : Q.HS →ₗ.[ℂ] Q.HS
```

**`QuantumMechanics.HarmonicOscillator.numberOperator_apply`**, a lemma, [line 279](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HarmonicOscillator/NumberOperator.lean#L279).

```lean
lemma numberOperator_apply (ψ : SchwartzSubmodule d) :
    Q.numberOperator i ψ =
      schwartzEquiv volume (Q.numberCLM i ((schwartzEquiv volume).symm ψ))
```

## D. Symmetry

**`QuantumMechanics.HarmonicOscillator.numberOperator_isSymmetric`**, a lemma, [line 291](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HarmonicOscillator/NumberOperator.lean#L291).

> The number operator is symmetric.

```lean
lemma numberOperator_isSymmetric : (Q.numberOperator i).IsSymmetric
```

## Depends on

- [Ladder operators](ladderoperators.md)

## Sources

- [Physlib/QuantumMechanics/HarmonicOscillator/NumberOperator.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HarmonicOscillator/NumberOperator.lean)
