---
declaration: module
origin: cited
lean: QuantumMechanics.HydrogenAtom, QuantumMechanics.HydrogenAtom.potential_eq, QuantumMechanics.HydrogenAtom.potential_AESM, QuantumMechanics.HydrogenAtom.potential_AEM, QuantumMechanics.HydrogenAtom.hamiltonianRegCLM, QuantumMechanics.HydrogenAtom.hamiltonianRegCLM_eq, QuantumMechanics.HydrogenAtom.polyBddSchwartzSubmodule_le_hamiltonianOperator_domain, QuantumMechanics.HydrogenAtom.hamiltonianOperator_hasDenseDomain
statement: formalized
proof: formalized
---

# Hydrogen atom

The module `Physlib.QuantumMechanics.Hydrogen.Basic`, [Physlib/QuantumMechanics/Hydrogen/Basic.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Hydrogen/Basic.lean): 8 declarations, 4 with a docstring.

> This module introduces the `d`-dimensional hydrogen atom with `1/r` potential.
>
> In addition to the dimension `d`, the quantum mechanical system is characterized by
> a mass `m > 0` and constant `k` appearing in the potential `V = -k/r`.
> The standard hydrogen atom has `d=3`, `m = mₑmₚ/(mₑ + mₚ) ≈ mₑ` and `k = e²/4πε₀`.
>
> The potential `V = -k/r` is singular at the origin. To address this we define a regularized
> Hamiltonian in which the potential is replaced by `-k·r(ε)⁻¹`, where `r(ε)² = ‖x‖² + ε²`.
> This goes by several names including "soft-core" and "truncated" Coulomb potential.
>
> The (unregularized) Hamiltonian is densely defined in any dimension: its domain contains the
> dense submodule of polynomially-bounded Schwartz maps (`hamiltonianOperator_hasDenseDomain`).

## References

> * https://doi.org/10.1103/PhysRevA.80.032507. [ref: doi\_physreva\_80\_032507]
> * https://doi.org/10.1063/1.3290740. [ref: doi\_1063\_1\_3290740]

**`QuantumMechanics.HydrogenAtom`**, a structure, [line 56](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Hydrogen/Basic.lean#L56).

> A hydrogen atom is characterized by the number of spatial dimensions `d`,
> the mass `m` and the coefficient `k` for the `1/r` potential.

```lean
structure HydrogenAtom (d : ℕ) extends SpaceDQuantumSystem d where
  /-- Coefficient in the Coulomb potential (positive for attractive) -/
  k : ℝ
  coulomb_potential : potential = fun x ↦ -k * ‖x‖⁻¹
```

## A. Basic

**`QuantumMechanics.HydrogenAtom.potential_eq`**, a lemma, [line 71](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Hydrogen/Basic.lean#L71).

```lean
lemma potential_eq : H.potential = fun x ↦ -H.k * ‖x‖⁻¹
```

**`QuantumMechanics.HydrogenAtom.potential_AESM`**, a lemma, [line 74](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Hydrogen/Basic.lean#L74).

```lean
lemma potential_AESM : AEStronglyMeasurable H.potential
```

**`QuantumMechanics.HydrogenAtom.potential_AEM`**, a lemma, [line 79](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Hydrogen/Basic.lean#L79).

```lean
lemma potential_AEM : AEMeasurable H.potential
```

## B. Regularization

**`QuantumMechanics.HydrogenAtom.hamiltonianRegCLM`**, a def, [line 87](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Hydrogen/Basic.lean#L87).

> The hydrogen atom Hamiltonian regularized by `ε ≠ 0` is defined to be
> `𝐇(ε) ≔ (2m)⁻¹𝐩² - k·𝐫(ε)⁻¹`.

```lean
def hamiltonianRegCLM (ε : ℝˣ) : 𝓢(Space d, ℂ) →L[ℂ] 𝓢(Space d, ℂ)
```

**`QuantumMechanics.HydrogenAtom.hamiltonianRegCLM_eq`**, a lemma, [line 90](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Hydrogen/Basic.lean#L90).

```lean
lemma hamiltonianRegCLM_eq (ε : ℝˣ) :
    H.hamiltonianRegCLM ε = (2 * H.m)⁻¹ • (𝐩 ⬝ᵥ 𝐩) - H.k • 𝐫₀ ε (-1)
```

## C. Domain of the Hamiltonian

**`QuantumMechanics.HydrogenAtom.polyBddSchwartzSubmodule_le_hamiltonianOperator_domain`**, a lemma, [line 101](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Hydrogen/Basic.lean#L101).

> Polynomially-bounded Schwartz maps `f` with `‖x‖ ^ (-k) * ‖f x‖ ≤ Cₖ` for all `k ≤ ⌊2 - d/2⌋`
> lie in the domain of the Hamiltonian. For `d ≥ 3` these are all Schwartz maps.

```lean
lemma polyBddSchwartzSubmodule_le_hamiltonianOperator_domain :
    PolyBddSchwartzSubmodule d ⌊1 - d / 2 - (-1 : ℝ)⌋.toNat ≤
      H.hamiltonianOperator.domain
```

**`QuantumMechanics.HydrogenAtom.hamiltonianOperator_hasDenseDomain`**, a lemma, [line 116](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Hydrogen/Basic.lean#L116).

> The Hamiltonian of the hydrogen atom is densely defined, in any dimension.

```lean
lemma hamiltonianOperator_hasDenseDomain : H.hamiltonianOperator.HasDenseDomain
```

## Depends on

- [Position operators](../operators/position.md)
- [Single-particle quantum system on `Space d`](../spacedquantumsystem.md)

## Sources

- [Physlib/QuantumMechanics/Hydrogen/Basic.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Hydrogen/Basic.lean)
