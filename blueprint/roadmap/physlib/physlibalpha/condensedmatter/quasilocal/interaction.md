---
declaration: module
origin: cited
lean: CondensedMatter.QuasiLocal.Interaction, CondensedMatter.QuasiLocal.Interaction.hamiltonian, CondensedMatter.QuasiLocal.Interaction.hamiltonian_isHermitian, CondensedMatter.QuasiLocal.inclMat_exp, CondensedMatter.QuasiLocal.inclMat_gibbsWeight, CondensedMatter.QuasiLocal.Charge, CondensedMatter.QuasiLocal.chargeOp, CondensedMatter.QuasiLocal.chargeOp_isHermitian
statement: formalized
proof: formalized
---

# Interactions, finite-volume Hamiltonians and ensembles of a lattice system

The module `PhyslibAlpha.CondensedMatter.QuasiLocal.Interaction`, [PhyslibAlpha/CondensedMatter/QuasiLocal/Interaction.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/QuasiLocal/Interaction.lean): 12 declarations, 10 with a docstring.

> An interaction assigns an operator to each finite region of a lattice, and the finite-volume
> Hamiltonian is the sum of the lifts to a box of the terms it contains.

## i. Overview

> An *interaction* `Φ` assigns to each finite region `X` of the sites a Hermitian operator `Φ X` of
> the algebra of `X`. The Ising chain has `Φ {x} = h σᶻ_x` and `Φ {x, y} = - J σᶻ_x σᶻ_y` for
> neighbours. The *Hamiltonian of a finite box* `Λ` is
> `H_Λ = ∑_{X ⊆ Λ} (Φ X ⊗ 1)`: every term supported inside the box, lifted to the box by `M ↦ M ⊗ 1`
> and summed. A *charge* is a function `q_x` on the configuration space of each site, such as the
> occupation number, and the total charge `N_Λ = ∑_{x ∈ Λ} q_x` of a box is the diagonal operator
> with value `∑ q_x(c_x)` on the configuration `c`.
>
> The lifts commute with the exponential: for a unital `*`-homomorphism `φ`, `φ (e^a) = e^{φ a}`, so
> the Gibbs weight of a lifted operator is the lift of its Gibbs weight. The canonical and grand
> canonical states of a box are the Gibbs states of `H_Λ` and `H_Λ - μ N_Λ` at inverse temperature
> `β`, as in `Gibbs`. If the interaction conserves the charge, they factorize.

## ii. Key results

> - `Interaction` : a family of Hermitian operators indexed by finite regions.
> - `Interaction.hamiltonian` : the Hamiltonian of a finite box.
> - `inclMat_exp` : the lift of an exponential is the exponential of the lift.
> - `chargeOp` : the total charge of a box.
> - `Interaction.canonicalState`, `Interaction.grandCanonicalState` : the ensembles of a box.

## iv. References

> * O. Bratteli & D. Robinson, Operator Algebras and Quantum Statistical Mechanics 2,
>   Section 6.2.

## A. Interactions and the Hamiltonian of a box

**`CondensedMatter.QuasiLocal.Interaction`**, a structure, [line 72](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/QuasiLocal/Interaction.lean#L72).

> **An interaction**: a Hermitian operator of each finite region.

```lean
structure Interaction where
  /-- The term of the interaction supported in a region. -/
  Φ : ∀ X : Finset S, Alg Ω X
  /-- Every term is Hermitian. -/
  isHermitian : ∀ X, (Φ X).IsHermitian
```

**`CondensedMatter.QuasiLocal.Interaction.hamiltonian`**, a def, [line 82](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/QuasiLocal/Interaction.lean#L82).

> **The Hamiltonian of a finite box**: the sum of the lifts to the box of the terms of the
> interaction supported inside it.

```lean
def Interaction.hamiltonian (I : Interaction Ω) (Λ : Finset S) : Alg Ω Λ
```

**`CondensedMatter.QuasiLocal.Interaction.hamiltonian_isHermitian`**, a lemma, [line 86](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/QuasiLocal/Interaction.lean#L86).

```lean
lemma Interaction.hamiltonian_isHermitian (I : Interaction Ω) (Λ : Finset S) :
    (I.hamiltonian Λ).IsHermitian
```

## B. Lifts and the exponential

**`CondensedMatter.QuasiLocal.inclMat_exp`**, a lemma, [line 96](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/QuasiLocal/Interaction.lean#L96).

> The lift `M ↦ M ⊗ 1` commutes with the exponential.

```lean
lemma inclMat_exp {X Y : Finset S} (h : X ≤ Y) (a : Alg Ω X) :
    inclMat h (NormedSpace.exp a) = NormedSpace.exp (inclMat h a)
```

**`CondensedMatter.QuasiLocal.inclMat_gibbsWeight`**, a lemma, [line 102](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/QuasiLocal/Interaction.lean#L102).

> **The lift of a Gibbs weight is the Gibbs weight of the lift.**

```lean
lemma inclMat_gibbsWeight {X Y : Finset S} (h : X ≤ Y) (a : Alg Ω X) :
    inclMat h (gibbsWeight a) = gibbsWeight (inclMat h a)
```

## C. Charges and the ensembles of a box

**`CondensedMatter.QuasiLocal.Charge`**, an abbrev, [line 112](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/QuasiLocal/Interaction.lean#L112).

> A charge: a real number attached to each value of the configuration space of each site, such
> as the occupation number of a mode.

```lean
abbrev Charge (Ω : S → Type*)
```

**`CondensedMatter.QuasiLocal.chargeOp`**, a def, [line 116](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/QuasiLocal/Interaction.lean#L116).

> **The total charge of a box**: the diagonal operator with the value `∑_{x ∈ Λ} q_x(c_x)` on
> the configuration `c`.

```lean
def chargeOp (q : Charge Ω) (Λ : Finset S) : Alg Ω Λ
```

**`CondensedMatter.QuasiLocal.chargeOp_isHermitian`**, a lemma, [line 120](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/QuasiLocal/Interaction.lean#L120).

```lean
lemma chargeOp_isHermitian (q : Charge Ω) (Λ : Finset S) : (chargeOp q Λ).IsHermitian
```

**`CondensedMatter.QuasiLocal.Interaction.canonicalState`**, a def, [line 129](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/QuasiLocal/Interaction.lean#L129).

> **The canonical ensemble of a box** at inverse temperature `β`.

```lean
def Interaction.canonicalState (I : Interaction Ω) (β : ℝ) (Λ : Finset S) :
    AlgState (Alg Ω Λ)
```

**`CondensedMatter.QuasiLocal.Interaction.grandCanonicalState`**, a def, [line 135](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/QuasiLocal/Interaction.lean#L135).

> **The grand canonical ensemble of a box** at inverse temperature `β` and chemical potential
> `μ` for the charge `q`.

```lean
def Interaction.grandCanonicalState (I : Interaction Ω) (q : Charge Ω) (β μ : ℝ)
    (Λ : Finset S) : AlgState (Alg Ω Λ)
```

**`CondensedMatter.QuasiLocal.Interaction.Conserves`**, a def, [line 142](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/QuasiLocal/Interaction.lean#L142).

> The interaction conserves the charge: the Hamiltonian of every box commutes with its
> total charge.

```lean
def Interaction.Conserves (I : Interaction Ω) (q : Charge Ω) : Prop
```

**`CondensedMatter.QuasiLocal.Interaction.grandCanonicalWeight_of_conserves`**, a lemma, [line 148](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/QuasiLocal/Interaction.lean#L148).

> **For a conserved charge the grand canonical weight of a box is its canonical weight times a
> fugacity.**

```lean
lemma Interaction.grandCanonicalWeight_of_conserves (I : Interaction Ω) {q : Charge Ω}
    (hq : I.Conserves q) (β μ : ℝ) (Λ : Finset S) :
    gibbsWeight (grandCanonicalOp β μ (I.hamiltonian Λ) (chargeOp q Λ)) =
      gibbsWeight ((β : ℂ) • I.hamiltonian Λ) *
        NormedSpace.exp (((β * μ : ℝ) : ℂ) • chargeOp q Λ)
```

## Depends on

- [Gibbs weights and states of a finite-dimensional system](gibbs.md)
- [Local algebras of a system with a finite configuration space at each site](local.md)

## Sources

- [PhyslibAlpha/CondensedMatter/QuasiLocal/Interaction.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/QuasiLocal/Interaction.lean)
