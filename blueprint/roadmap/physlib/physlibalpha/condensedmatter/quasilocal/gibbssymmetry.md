---
declaration: module
origin: cited
lean: CondensedMatter.QuasiLocal.quantumIso_exp, CondensedMatter.QuasiLocal.quantumIso_trace, CondensedMatter.QuasiLocal.quantumIso_gibbsWeight, CondensedMatter.QuasiLocal.quantumIso_partition, CondensedMatter.QuasiLocal.gibbsFunctional_quantumIso, CondensedMatter.QuasiLocal.Interaction.IsInvariant, CondensedMatter.QuasiLocal.powersetSmul, CondensedMatter.QuasiLocal.Interaction.hamiltonian_smul
statement: formalized
proof: formalized
---

# Covariance of the finite-volume ensembles under site symmetries

The module `PhyslibAlpha.CondensedMatter.QuasiLocal.GibbsSymmetry`, [PhyslibAlpha/CondensedMatter/QuasiLocal/GibbsSymmetry.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/QuasiLocal/GibbsSymmetry.lean): 13 declarations, 11 with a docstring.

> A symmetry of an interaction carries the Hamiltonian and the ensembles of a box to those of the
> moved box.

## i. Overview

> Let a group `Γ` act on the sites, all of which carry the same finite configuration space. An
> interaction is *invariant* if moving a term moves the term of the moved region:
> `quantumIso γ X (Φ X) = Φ (γ • X)`. Then the Hamiltonian of a box `Λ` is carried to the Hamiltonian
> of `γ • Λ`, because moving commutes with lifting and with the sum over the regions inside the box.
> Moving is a `*`-isomorphism preserving the trace, so it commutes with the exponential and carries
> the Gibbs weight to the Gibbs weight and the Gibbs state to the Gibbs state: the expectation of the
> moved observable in the ensemble of the moved box equals the expectation in the ensemble of the box.

## ii. Key results

> - `quantumIso_exp` : moving commutes with the exponential.
> - `Interaction.hamiltonian_smul` : the Hamiltonian of a moved box.
> - `Interaction.canonicalState_smul`, `Interaction.grandCanonicalState_smul` : covariance of the
>   canonical and grand canonical ensembles.

## iv. References

> * None.

## A. Moving the Gibbs weight

**`CondensedMatter.QuasiLocal.quantumIso_exp`**, a lemma, [line 65](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/QuasiLocal/GibbsSymmetry.lean#L65).

> Moving commutes with the exponential.

```lean
lemma quantumIso_exp (γ : Γ) (X : Finset S) (a : Alg (fun _ : S => Ω₀) X) :
    quantumIso γ X (NormedSpace.exp a) = NormedSpace.exp (quantumIso γ X a)
```

**`CondensedMatter.QuasiLocal.quantumIso_trace`**, a lemma, [line 71](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/QuasiLocal/GibbsSymmetry.lean#L71).

> Moving preserves the trace.

```lean
lemma quantumIso_trace (γ : Γ) (X : Finset S) (a : Alg (fun _ : S => Ω₀) X) :
    (quantumIso γ X a).trace = a.trace
```

**`CondensedMatter.QuasiLocal.quantumIso_gibbsWeight`**, a lemma, [line 77](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/QuasiLocal/GibbsSymmetry.lean#L77).

```lean
lemma quantumIso_gibbsWeight (γ : Γ) (X : Finset S) (a : Alg (fun _ : S => Ω₀) X) :
    quantumIso γ X (gibbsWeight a) = gibbsWeight (quantumIso γ X a)
```

**`CondensedMatter.QuasiLocal.quantumIso_partition`**, a lemma, [line 81](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/QuasiLocal/GibbsSymmetry.lean#L81).

```lean
lemma quantumIso_partition (γ : Γ) (X : Finset S) (a : Alg (fun _ : S => Ω₀) X) :
    partition (quantumIso γ X a) = partition a
```

**`CondensedMatter.QuasiLocal.gibbsFunctional_quantumIso`**, a lemma, [line 86](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/QuasiLocal/GibbsSymmetry.lean#L86).

> **The Gibbs functional is covariant.**

```lean
lemma gibbsFunctional_quantumIso (γ : Γ) (X : Finset S) (h b : Alg (fun _ : S => Ω₀) X) :
    gibbsFunctional (quantumIso γ X h) (quantumIso γ X b) = gibbsFunctional h b
```

## B. Moving the Hamiltonian

**`CondensedMatter.QuasiLocal.Interaction.IsInvariant`**, a def, [line 94](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/QuasiLocal/GibbsSymmetry.lean#L94).

> An interaction is *invariant* under `γ` if moving a term gives the term of the moved region.

```lean
def Interaction.IsInvariant (I : Interaction (fun _ : S => Ω₀)) (γ : Γ) : Prop
```

**`CondensedMatter.QuasiLocal.powersetSmul`**, a def, [line 98](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/QuasiLocal/GibbsSymmetry.lean#L98).

> The bijection between the regions of a box and the regions of the moved box.

```lean
def powersetSmul (γ : Γ) (Λ : Finset S) : Λ.powerset ≃ (γ • Λ).powerset
```

**`CondensedMatter.QuasiLocal.Interaction.hamiltonian_smul`**, a lemma, [line 108](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/QuasiLocal/GibbsSymmetry.lean#L108).

> **The Hamiltonian of a moved box**: for an invariant interaction, moving the Hamiltonian of a
> box gives the Hamiltonian of the moved box.

```lean
lemma Interaction.hamiltonian_smul (I : Interaction (fun _ : S => Ω₀)) {γ : Γ}
    (hI : I.IsInvariant γ) (Λ : Finset S) :
    quantumIso γ Λ (I.hamiltonian Λ) = I.hamiltonian (γ • Λ)
```

## C. Moving the ensembles

**`CondensedMatter.QuasiLocal.Interaction.canonicalState_smul`**, a lemma, [line 122](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/QuasiLocal/GibbsSymmetry.lean#L122).

> **The canonical ensemble is covariant**: the expectation of a moved observable in the
> ensemble of the moved box is the expectation of the observable in the ensemble of the box.

```lean
lemma Interaction.canonicalState_smul (I : Interaction (fun _ : S => Ω₀)) {γ : Γ}
    (hI : I.IsInvariant γ) (β : ℝ) (Λ : Finset S) (a : Alg (fun _ : S => Ω₀) Λ) :
    I.canonicalState β (γ • Λ) (quantumIso γ Λ a) = I.canonicalState β Λ a
```

**`CondensedMatter.QuasiLocal.siteSmul`**, a def, [line 132](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/QuasiLocal/GibbsSymmetry.lean#L132).

> The bijection between the sites of a box and the sites of the moved box.

```lean
def siteSmul (γ : Γ) (Λ : Finset S) : ↥Λ ≃ ↥(γ • Λ)
```

**`CondensedMatter.QuasiLocal.chargeOp_smul`**, a lemma, [line 140](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/QuasiLocal/GibbsSymmetry.lean#L140).

> **A uniform charge is moved to the uniform charge of the moved box.**

```lean
lemma chargeOp_smul (q₀ : Ω₀ → ℝ) (γ : Γ) (Λ : Finset S) :
    quantumIso γ Λ (chargeOp (fun _ : S => q₀) Λ) = chargeOp (fun _ : S => q₀) (γ • Λ)
```

**`CondensedMatter.QuasiLocal.grandCanonicalOp_quantumIso`**, a lemma, [line 157](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/QuasiLocal/GibbsSymmetry.lean#L157).

> The charge of a moved box, as a statement about the operator whose weight is the grand
> canonical one.

```lean
lemma grandCanonicalOp_quantumIso (γ : Γ) (Λ : Finset S) (β μ : ℝ) (H N : Alg (fun _ : S => Ω₀) Λ) :
    quantumIso γ Λ (grandCanonicalOp β μ H N) =
      grandCanonicalOp β μ (quantumIso γ Λ H) (quantumIso γ Λ N)
```

**`CondensedMatter.QuasiLocal.Interaction.grandCanonicalState_smul`**, a lemma, [line 164](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/QuasiLocal/GibbsSymmetry.lean#L164).

> **The grand canonical ensemble is covariant**, for an invariant interaction and a uniform
> charge.

```lean
lemma Interaction.grandCanonicalState_smul (I : Interaction (fun _ : S => Ω₀)) {γ : Γ}
    (hI : I.IsInvariant γ) (q₀ : Ω₀ → ℝ) (β μ : ℝ) (Λ : Finset S)
    (a : Alg (fun _ : S => Ω₀) Λ) :
    I.grandCanonicalState (fun _ : S => q₀) β μ (γ • Λ) (quantumIso γ Λ a) =
      I.grandCanonicalState (fun _ : S => q₀) β μ Λ a
```

## Depends on

- [Interactions, finite-volume Hamiltonians and ensembles of a lattice system](interaction.md)
- [Symmetries of the quantum net](symmetry.md)

## Sources

- [PhyslibAlpha/CondensedMatter/QuasiLocal/GibbsSymmetry.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/QuasiLocal/GibbsSymmetry.lean)
