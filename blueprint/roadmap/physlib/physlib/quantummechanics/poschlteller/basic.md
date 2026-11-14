---
declaration: module
origin: cited
lean: QuantumMechanics.PoschlTeller, QuantumMechanics.PoschlTeller.potential, QuantumMechanics.PoschlTeller.depth, QuantumMechanics.PoschlTeller.depth_pos, QuantumMechanics.PoschlTeller.potential_eq, QuantumMechanics.PoschlTeller.potential_eq_tanh, QuantumMechanics.PoschlTeller.potential_neg, QuantumMechanics.PoschlTeller.neg_depth_le_potential
statement: formalized
proof: formalized
---

# 1d Pöschl-Teller

The module `Physlib.QuantumMechanics.PoschlTeller.Basic`, [Physlib/QuantumMechanics/PoschlTeller/Basic.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/PoschlTeller/Basic.lean): 35 declarations, 33 with a docstring.

## i. Overview

> The Pöschl-Teller potential, `$V(x) \propto -\mathrm{sech}^2{(\kappa x)}$`, gives rise
> to a one-dimensional quantum system for which the energy eigenvalues, energy eigenstates and
> scattering data can be computed exactly. Notably, the potential is \_reflectionless\_ when
> the parameter controlling its depth is a positive integer.

## ii. Key results

> - `potential` is the Pöschl-Teller potential `-(ℏ² κ² N (N + 1)) / (2 m cosh² (κ x))`, of depth
>   `depth = ℏ² κ² N (N + 1) / (2 m)`; it is negative, bounded below by `-depth`, even, of temperate
>   growth (`potential_hasTemperateGrowth`) and continuous.
> - `toSpaceDQuantumSystem` realises the Pöschl-Teller system as a `SpaceDQuantumSystem` of
>   dimension `1`; its kinetic, potential and Hamiltonian operators are the generic ones of
>   `SpaceDQuantumSystem`, for which this file gives the pointwise formulas in dimension one
>   (`toSpaceDQuantumSystem_kineticCLM_apply`, `toSpaceDQuantumSystem_hamiltonianCLM_apply`) and the
>   self-adjointness of the potential operator
>   (`toSpaceDQuantumSystem_potentialOperator_isSelfAdjoint`).
> - `creationCLM_apply`, `annihilationCLM_apply` give the pointwise action of the ladder operators;
>   their sum and difference are `(2 / √(2m)) 𝐩` and `(2 i ℏ κ / √(2m)) tanh (κ X)`.

## iv. References

> * https://arxiv.org/pdf/2411.14941. [ref: arxiv\_2411\_14941]

**`QuantumMechanics.PoschlTeller`**, a structure, [line 68](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/PoschlTeller/Basic.lean#L68).

> A Pöschl-Teller system is specified by the particle mass `m`, the width parameter `κ`,
> and family number `N` (all positive). -

```lean
structure PoschlTeller where
  /-- mass of the particle -/
  m : ℝ
  /-- width parameter of the potential -/
  κ : ℝ
  /-- family number, positive integer -/
  N : ℕ
  m_pos : 0 < m -- mass of the particle is positive
  κ_pos : 0 < κ -- width parameter of the potential is positive
  N_pos : 0 < N -- family number is positive
```

## A. Potential function

### A.1. Definition and depth

**`QuantumMechanics.PoschlTeller.potential`**, a def, [line 92](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/PoschlTeller/Basic.lean#L92).

> The Pöschl-Teller potential is `-(ℏ^2 * κ^2 * N * (N + 1)) / (2 * m * (cosh (κ * x)) ^ 2)`. -

```lean
def potential (x : Space 1) : ℝ
```

**`QuantumMechanics.PoschlTeller.depth`**, a def, [line 97](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/PoschlTeller/Basic.lean#L97).

> The depth `ℏ^2 * κ^2 * N * (N + 1) / (2 * m)` of the potential well, so that
> `potential x = -depth / cosh (κ * x) ^ 2`.

```lean
def depth : ℝ
```

**`QuantumMechanics.PoschlTeller.depth_pos`**, a lemma, [line 100](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/PoschlTeller/Basic.lean#L100).

> The depth of the well is positive.

```lean
lemma depth_pos : 0 < Q.depth
```

**`QuantumMechanics.PoschlTeller.potential_eq`**, a lemma, [line 109](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/PoschlTeller/Basic.lean#L109).

> The potential in terms of the depth, `potential x = -depth / cosh (κ * x) ^ 2`.

```lean
lemma potential_eq (x : Space 1) : Q.potential x = -Q.depth / Real.cosh (Q.κ * x 0) ^ 2
```

**`QuantumMechanics.PoschlTeller.potential_eq_tanh`**, a lemma, [line 115](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/PoschlTeller/Basic.lean#L115).

> The potential in terms of `tanh`, `potential x = -depth * (1 - tanh (κ * x) ^ 2)`.

```lean
lemma potential_eq_tanh (x : Space 1) :
    Q.potential x = -Q.depth * (1 - Real.tanh (Q.κ * x 0) ^ 2)
```

### A.2. Sign, bounds and parity

**`QuantumMechanics.PoschlTeller.potential_neg`**, a lemma, [line 126](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/PoschlTeller/Basic.lean#L126).

> The potential is negative.

```lean
lemma potential_neg (x : Space 1) : Q.potential x < 0
```

**`QuantumMechanics.PoschlTeller.neg_depth_le_potential`**, a lemma, [line 131](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/PoschlTeller/Basic.lean#L131).

> The potential is bounded below by `-depth`.

```lean
lemma neg_depth_le_potential (x : Space 1) : -Q.depth ≤ Q.potential x
```

**`QuantumMechanics.PoschlTeller.potential_zero`**, a lemma, [line 136](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/PoschlTeller/Basic.lean#L136).

> The minimum `-depth` of the potential is attained at the origin.

```lean
lemma potential_zero : Q.potential 0 = -Q.depth
```

**`QuantumMechanics.PoschlTeller.potential_neg_eq`**, a lemma, [line 141](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/PoschlTeller/Basic.lean#L141).

> The potential is even.

```lean
lemma potential_neg_eq (x : Space 1) : Q.potential (-x) = Q.potential x
```

### A.3. Regularity

**`QuantumMechanics.PoschlTeller.tanh_hasTemperateGrowth`**, a lemma, [line 150](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/PoschlTeller/Basic.lean#L150).

> The function `tanh (κ * x)` on `Space 1` has temperate growth.

```lean
lemma tanh_hasTemperateGrowth :
    (fun x : Space 1 => Real.tanh (Q.κ * x 0)).HasTemperateGrowth
```

**`QuantumMechanics.PoschlTeller.ofReal_comp_tanh_hasTemperateGrowth`**, a lemma, [line 155](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/PoschlTeller/Basic.lean#L155).

> The complexified function `ofReal ∘ tanh (κ * x)` has temperate growth.

```lean
lemma ofReal_comp_tanh_hasTemperateGrowth :
    (ofReal ∘ fun x : Space 1 => Real.tanh (Q.κ * x 0)).HasTemperateGrowth
```

**`QuantumMechanics.PoschlTeller.potential_hasTemperateGrowth`**, a lemma, [line 160](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/PoschlTeller/Basic.lean#L160).

> The potential has temperate growth.

```lean
lemma potential_hasTemperateGrowth : Q.potential.HasTemperateGrowth
```

**`QuantumMechanics.PoschlTeller.ofReal_comp_potential_hasTemperateGrowth`**, a lemma, [line 167](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/PoschlTeller/Basic.lean#L167).

> The complexified potential `ofReal ∘ potential` has temperate growth.

```lean
lemma ofReal_comp_potential_hasTemperateGrowth : (ofReal ∘ Q.potential).HasTemperateGrowth
```

**`QuantumMechanics.PoschlTeller.potential_continuous`**, a lemma, [line 171](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/PoschlTeller/Basic.lean#L171).

> The potential is continuous.

```lean
lemma potential_continuous : Continuous Q.potential
```

## B. As a quantum system

**`QuantumMechanics.PoschlTeller.toSpaceDQuantumSystem`**, an abbrev, [line 180](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/PoschlTeller/Basic.lean#L180).

> The Pöschl-Teller system as a `SpaceDQuantumSystem` of dimension `1`. Its kinetic, potential
> and Hamiltonian operators are those of `SpaceDQuantumSystem`.

```lean
abbrev toSpaceDQuantumSystem : SpaceDQuantumSystem 1
```

**`QuantumMechanics.PoschlTeller.toSpaceDQuantumSystem_m`**, a lemma, [line 182](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/PoschlTeller/Basic.lean#L182).

```lean
lemma toSpaceDQuantumSystem_m : Q.toSpaceDQuantumSystem.m = Q.m
```

**`QuantumMechanics.PoschlTeller.toSpaceDQuantumSystem_potential`**, a lemma, [line 184](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/PoschlTeller/Basic.lean#L184).

```lean
lemma toSpaceDQuantumSystem_potential : Q.toSpaceDQuantumSystem.potential = Q.potential
```

**`QuantumMechanics.PoschlTeller.HS`**, an abbrev, [line 188](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/PoschlTeller/Basic.lean#L188).

> The Hilbert space for the Pöschl-Teller system is `SpaceDHilbertSpace 1`.

```lean
abbrev HS (_ : PoschlTeller) : Type _
```

## C. Operators

### C.1. Kinetic energy, potential energy and Hamiltonian

**`QuantumMechanics.PoschlTeller.toSpaceDQuantumSystem_kineticCLM_apply`**, a lemma, [line 199](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/PoschlTeller/Basic.lean#L199).

> In dimension one the kinetic operator is `(2m)⁻¹ 𝐩 0 ∘ 𝐩 0`.

```lean
lemma toSpaceDQuantumSystem_kineticCLM_apply (ψ : 𝓢(Space 1, ℂ)) :
    Q.toSpaceDQuantumSystem.kineticCLM ψ = (2 * Q.m)⁻¹ • momentumCLM 0 (momentumCLM 0 ψ)
```

**`QuantumMechanics.PoschlTeller.toSpaceDQuantumSystem_potentialCLM_apply`**, a lemma, [line 204](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/PoschlTeller/Basic.lean#L204).

> The potential operator acts by pointwise multiplication by the potential.

```lean
lemma toSpaceDQuantumSystem_potentialCLM_apply (ψ : 𝓢(Space 1, ℂ)) (x : Space 1) :
    Q.toSpaceDQuantumSystem.potentialCLM ψ x = Q.potential x • ψ x
```

**`QuantumMechanics.PoschlTeller.toSpaceDQuantumSystem_potentialOperator_isSelfAdjoint`**, a lemma, [line 210](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/PoschlTeller/Basic.lean#L210).

> The potential operator is self-adjoint.

```lean
lemma toSpaceDQuantumSystem_potentialOperator_isSelfAdjoint :
    IsSelfAdjoint Q.toSpaceDQuantumSystem.potentialOperator
```

**`QuantumMechanics.PoschlTeller.toSpaceDQuantumSystem_potentialOperator_domain_ge`**, a lemma, [line 216](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/PoschlTeller/Basic.lean#L216).

> Schwartz functions lie in the domain of the potential operator.

```lean
lemma toSpaceDQuantumSystem_potentialOperator_domain_ge :
    SchwartzSubmodule 1 ≤ Q.toSpaceDQuantumSystem.potentialOperator.domain
```

**`QuantumMechanics.PoschlTeller.toSpaceDQuantumSystem_hamiltonianCLM_apply`**, a lemma, [line 222](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/PoschlTeller/Basic.lean#L222).

> The pointwise action of the Hamiltonian on a Schwartz function.

```lean
lemma toSpaceDQuantumSystem_hamiltonianCLM_apply (ψ : 𝓢(Space 1, ℂ)) (x : Space 1) :
    Q.toSpaceDQuantumSystem.hamiltonianCLM ψ x =
      (2 * Q.m)⁻¹ • momentumCLM 0 (momentumCLM 0 ψ) x + Q.potential x • ψ x
```

### C.2. Creation and annihilation operators

#### C.2.1. On Schwartz functions

**`QuantumMechanics.PoschlTeller.tanhCLM`**, a def, [line 238](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/PoschlTeller/Basic.lean#L238).

> Pointwise multiplication of Schwartz maps by `tanh(κx)`.

```lean
def tanhCLM : 𝓢(Space 1, ℂ) →L[ℂ] 𝓢(Space 1, ℂ)
```

**`QuantumMechanics.PoschlTeller.tanhCLM_apply`**, a lemma, [line 242](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/PoschlTeller/Basic.lean#L242).

> Multiplication by `tanh (κ * x)` acts pointwise.

```lean
lemma tanhCLM_apply (ψ : 𝓢(Space 1, ℂ)) (x : Space 1) :
    Q.tanhCLM ψ x = Real.tanh (Q.κ * x 0) • ψ x
```

**`QuantumMechanics.PoschlTeller.creationCLM`**, a def, [line 248](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/PoschlTeller/Basic.lean#L248).

> The creation operator, `1/√(2m) (P + iℏκ tanh(κX))`

```lean
def creationCLM : 𝓢(Space 1, ℂ) →L[ℂ] 𝓢(Space 1, ℂ)
```

**`QuantumMechanics.PoschlTeller.annihilationCLM`**, a def, [line 252](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/PoschlTeller/Basic.lean#L252).

> The annihilation operator, `1/√(2m) (P - iℏκ tanh(κX))`

```lean
def annihilationCLM : 𝓢(Space 1, ℂ) →L[ℂ] 𝓢(Space 1, ℂ)
```

**`QuantumMechanics.PoschlTeller.creationCLM_apply`**, a lemma, [line 256](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/PoschlTeller/Basic.lean#L256).

> The pointwise action of the creation operator.

```lean
lemma creationCLM_apply (ψ : 𝓢(Space 1, ℂ)) (x : Space 1) :
    Q.creationCLM ψ x = (1 / √(2 * Q.m)) • momentumCLM 0 ψ x
      + (I * ℏ * Q.κ / √(2 * Q.m)) * (Real.tanh (Q.κ * x 0) • ψ x)
```

**`QuantumMechanics.PoschlTeller.annihilationCLM_apply`**, a lemma, [line 263](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/PoschlTeller/Basic.lean#L263).

> The pointwise action of the annihilation operator.

```lean
lemma annihilationCLM_apply (ψ : 𝓢(Space 1, ℂ)) (x : Space 1) :
    Q.annihilationCLM ψ x = (1 / √(2 * Q.m)) • momentumCLM 0 ψ x
      + (-I * ℏ * Q.κ / √(2 * Q.m)) * (Real.tanh (Q.κ * x 0) • ψ x)
```

**`QuantumMechanics.PoschlTeller.creationCLM_add_annihilationCLM`**, a lemma, [line 270](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/PoschlTeller/Basic.lean#L270).

> The sum of the ladder operators is `(2 / √(2m)) 𝐩`.

```lean
lemma creationCLM_add_annihilationCLM :
    Q.creationCLM + Q.annihilationCLM = (2 / √(2 * Q.m)) • momentumCLM 0
```

**`QuantumMechanics.PoschlTeller.creationCLM_sub_annihilationCLM`**, a lemma, [line 280](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/PoschlTeller/Basic.lean#L280).

> The difference of the ladder operators is `(2 i ℏ κ / √(2m)) tanh (κ X)`.

```lean
lemma creationCLM_sub_annihilationCLM :
    Q.creationCLM - Q.annihilationCLM = (2 * I * ℏ * Q.κ / √(2 * Q.m)) • Q.tanhCLM
```

#### C.2.2. As unbounded operators

**`QuantumMechanics.PoschlTeller.tanhOperator`**, a def, [line 292](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/PoschlTeller/Basic.lean#L292).

> The unbounded operator defined by pointwise multiplication by `tanh(κx)`.

```lean
def tanhOperator : Q.HS →ₗ.[ℂ] Q.HS
```

**`QuantumMechanics.PoschlTeller.creationOperator`**, a def, [line 295](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/PoschlTeller/Basic.lean#L295).

> The creation unbounded operator, `1/√(2m) (P + iℏκ tanh(κX))`

```lean
def creationOperator : Q.HS →ₗ.[ℂ] Q.HS
```

**`QuantumMechanics.PoschlTeller.annihilationOperator`**, a def, [line 299](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/PoschlTeller/Basic.lean#L299).

> The annihilation unbounded operator, `1/√(2m) (P - iℏκ tanh(κX))`

```lean
def annihilationOperator : Q.HS →ₗ.[ℂ] Q.HS
```

## Depends on

- [Single-particle quantum system on `Space d`](../spacedquantumsystem.md)

## Proof depends on

- [Properties of Tanh](../../mathematics/formathlib/trigonometry-tanh.md)

## Sources

- [Physlib/QuantumMechanics/PoschlTeller/Basic.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/PoschlTeller/Basic.lean)
