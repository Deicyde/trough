---
declaration: module
origin: cited
lean: CondensedMatter.QuasiLocal.matrix_exists_sumSq, CondensedMatter.QuasiLocal.quantumNet_isLocallyBounded, CondensedMatter.QuasiLocal.Interaction.canonicalLimitState, CondensedMatter.QuasiLocal.Interaction.grandCanonicalLimitState, CondensedMatter.QuasiLocal.Interaction.canonicalLimitState_of
statement: formalized
proof: formalized
---

# Thermodynamic limit states of an interaction

The module `PhyslibAlpha.CondensedMatter.QuasiLocal.LimitState`, [PhyslibAlpha/CondensedMatter/QuasiLocal/LimitState.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/QuasiLocal/LimitState.lean): 5 declarations, 5 with a docstring.

> The Gibbs states of the finite boxes have limit points, which are states of the infinite system.

## i. Overview

> Every local operator of a quantum lattice system is bounded, `a* a ≤ ‖a‖² · 1`, so the net of
> box expectations of a fixed local observable is bounded. By compactness the canonical or grand
> canonical Gibbs states of the boxes `Λ` converge, along any ultrafilter finer than the filter of
> large boxes, to a state of the quasi-local algebra. This is the *thermodynamic limit state*. It is
> a state of the infinite crystal, not a number attached to it.

## ii. Key results

> - `matrix_exists_sumSq` : in a matrix algebra `a* a + p = c · 1` for a sum of squares `p`.
> - `quantumNet_isLocallyBounded` : the net of operators is locally bounded.
> - `Interaction.canonicalLimitState` : the thermodynamic limit state of the canonical ensemble.
> - `Interaction.grandCanonicalLimitState` : that of the grand canonical ensemble.

## iv. References

> * O. Bratteli & D. Robinson, Operator Algebras and Quantum Statistical Mechanics 2,
>   Section 6.2.3.

## A. Local boundedness of the net of operators

**`CondensedMatter.QuasiLocal.matrix_exists_sumSq`**, a lemma, [line 65](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/QuasiLocal/LimitState.lean#L65).

> In a matrix algebra every `a* a` lies below a multiple of the identity by a sum of
> squares.

```lean
lemma matrix_exists_sumSq {n : Type*} [Fintype n] [DecidableEq n] (a : Matrix n n ℂ) :
    ∃ c : ℝ, ∃ p ∈ sumSq (Matrix n n ℂ), star a * a + p = (c : ℂ) • (1 : Matrix n n ℂ)
```

**`CondensedMatter.QuasiLocal.quantumNet_isLocallyBounded`**, a lemma, [line 78](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/QuasiLocal/LimitState.lean#L78).

> **The net of operators is locally bounded.**

```lean
lemma quantumNet_isLocallyBounded : (quantumNet Ω).IsLocallyBounded
```

## B. Limit states of the ensembles

**`CondensedMatter.QuasiLocal.Interaction.canonicalLimitState`**, a def, [line 87](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/QuasiLocal/LimitState.lean#L87).

> **The thermodynamic limit state of the canonical ensemble** along an ultrafilter of boxes:
> a state of the infinite system.

```lean
def Interaction.canonicalLimitState (I : Interaction Ω) (β : ℝ) (𝒰 : Ultrafilter (Finset S))
    (h𝒰 : (𝒰 : Filter (Finset S)) ≤ atTop) : AlgState (quantumNet Ω).Quasilocal
```

**`CondensedMatter.QuasiLocal.Interaction.grandCanonicalLimitState`**, a def, [line 93](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/QuasiLocal/LimitState.lean#L93).

> **The thermodynamic limit state of the grand canonical ensemble** along an ultrafilter of
> boxes.

```lean
def Interaction.grandCanonicalLimitState (I : Interaction Ω) (q : Charge Ω) (β μ : ℝ)
    (𝒰 : Ultrafilter (Finset S)) (h𝒰 : (𝒰 : Filter (Finset S)) ≤ atTop) :
    AlgState (quantumNet Ω).Quasilocal
```

**`CondensedMatter.QuasiLocal.Interaction.canonicalLimitState_of`**, a lemma, [line 101](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/QuasiLocal/LimitState.lean#L101).

> The limit state of the canonical ensemble on a local observable is the limit of the box
> expectations.

```lean
lemma Interaction.canonicalLimitState_of (I : Interaction Ω) (β : ℝ) (𝒰 : Ultrafilter (Finset S))
    (h𝒰 : (𝒰 : Filter (Finset S)) ≤ atTop) (X : Finset S) (a : Alg Ω X) :
    Tendsto (localSeq (N := quantumNet Ω) (fun Λ => I.canonicalState β Λ) X a) 𝒰
      (nhds (I.canonicalLimitState β 𝒰 h𝒰 ((quantumNet Ω).of X a)))
```

## Depends on

- [The quantum and classical nets of a system with finite site spaces](instances.md)
- [Interactions, finite-volume Hamiltonians and ensembles of a lattice system](interaction.md)
- [Limit states of the quasi-local algebra](../../probabilistictheory/quasilocal/limit.md)

## Sources

- [PhyslibAlpha/CondensedMatter/QuasiLocal/LimitState.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/QuasiLocal/LimitState.lean)
