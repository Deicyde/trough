---
declaration: module
origin: cited
lean: ProbabilisticTheory.IsSchurBlock, ProbabilisticTheory.exists_scalar_of_isSchurBlock, ProbabilisticTheory.UnitalPositiveLinearMap.IsCovariant.exists_scalar_of_isSchurBlock
statement: formalized
proof: formalized
---

# Schur's lemma for covariant channels

The module `PhyslibAlpha.ProbabilisticTheory.Representation.Schur`, [PhyslibAlpha/ProbabilisticTheory/Representation/Schur.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Representation/Schur.lean): 3 declarations, 3 with a docstring.

> Schur's lemma as a hypothesis: equivariant maps and covariant channels are scalar on blocks.

## i. Overview

> If the observables split into invariant blocks `E = ⨁ᵢ Wᵢ` on each of which every equivariant map
> acts as a scalar, then every equivariant map preserving the blocks is determined by one real number
> per block. For the qubit, the Hermitian `2 × 2` matrices split into the scalars and the Pauli
> vectors, so a rotation-covariant channel is determined by one number.
>
> Mathlib's Schur lemma needs an algebraically closed field, while the observables are a real space.
> The Schur property of a block is therefore a hypothesis, `IsSchurBlock`.

## ii. Key results

> - `IsSchurBlock` : every equivariant map preserving the block acts on it as a scalar.
> - `exists_scalar_of_isSchurBlock` : an equivariant map is a scalar on each block.
> - `UnitalPositiveLinearMap.IsCovariant.exists_scalar_of_isSchurBlock` : the same for covariant
>   channels.

## iv. References

> * None.

## A. The Schur hypothesis on a single block

**`ProbabilisticTheory.IsSchurBlock`**, a def, [line 62](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Representation/Schur.lean#L62).

> The **Schur hypothesis** for a submodule `W`, relative to an action `smul : G → E → E`: every
> linear endomorphism of `E` that is `G`-equivariant on `W` (`f (smul g x) = smul g (f x)` for
> `x ∈ W`) and maps `W` into itself acts on all of `W` as a single scalar `c`. This is the abstract
> shape of "every `G`-equivariant self-map of an irreducible real representation is a scalar" — taken
> here as a hypothesis to be supplied per block (cited or proved separately), not derived from a
> general representation-theoretic classification (see the file docstring).

```lean
def IsSchurBlock (smul : G → E → E) (W : Submodule ℝ E) : Prop
```

## B. The multiplicity-free classification theorem

**`ProbabilisticTheory.exists_scalar_of_isSchurBlock`**, a lemma, [line 77](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Representation/Schur.lean#L77).

> **Equivariant maps are scalars on Schur blocks.** If `E = ⨁ᵢ Wᵢ` with invariant Schur blocks
> `Wᵢ`, every equivariant linear map preserving the blocks acts on each `Wᵢ` as a real scalar.

```lean
lemma exists_scalar_of_isSchurBlock (smul : G → E → E) (W : ι → Submodule ℝ E)
    (_hsum : DirectSum.IsInternal W) (_hW_inv : ∀ i g, ∀ x ∈ W i, smul g x ∈ W i)
    (hSchur : ∀ i, IsSchurBlock smul (W i)) (f : E →ₗ[ℝ] E)
    (hf_equiv : ∀ g x, f (smul g x) = smul g (f x)) (hf_block : ∀ i, ∀ x ∈ W i, f x ∈ W i) :
    ∃ c : ι → ℝ, ∀ i, ∀ x ∈ W i, f x = c i • x
```

## C. Covariant channels

> A channel intertwining a symmetry action with itself is a `G`-equivariant endomorphism.

**`ProbabilisticTheory.UnitalPositiveLinearMap.IsCovariant.exists_scalar_of_isSchurBlock`**, a lemma, [line 100](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Representation/Schur.lean#L100).

> **Schur's lemma for covariant channels.** A channel covariant for a symmetry action `ρ` acts as
> a real scalar on each block of a finite decomposition of `E` into invariant Schur blocks that it
> preserves.

```lean
lemma UnitalPositiveLinearMap.IsCovariant.exists_scalar_of_isSchurBlock
    {ρ : G →* Symmetry E} {φ : Channel E E} (hφ : φ.IsCovariant ρ ρ) (W : ι → Submodule ℝ E)
    (hsum : DirectSum.IsInternal W)
    (hW_inv : ∀ i g, ∀ x ∈ W i, (ρ g).1 x ∈ W i)
    (hSchur : ∀ i, IsSchurBlock (fun g x => (ρ g).1 x) (W i))
    (hφ_block : ∀ i, ∀ x ∈ W i, φ x ∈ W i) :
    ∃ c : ι → ℝ, ∀ i, ∀ x ∈ W i, φ x = c i • x
```

## Depends on

- [Covariant measurements and channels](covariance-basic.md)

## Sources

- [PhyslibAlpha/ProbabilisticTheory/Representation/Schur.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Representation/Schur.lean)
