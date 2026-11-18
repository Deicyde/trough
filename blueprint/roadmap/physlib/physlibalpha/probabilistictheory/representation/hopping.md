---
declaration: module
origin: cited
lean: ProbabilisticTheory.QuantumMechanics.UnitaryRep.hopping, ProbabilisticTheory.QuantumMechanics.UnitaryRep.blochMatrix, ProbabilisticTheory.QuantumMechanics.UnitaryRep.blochMatrix_apply, ProbabilisticTheory.QuantumMechanics.UnitaryRep.blochHom_blochMatrix, ProbabilisticTheory.QuantumMechanics.UnitaryRep.spectrum_hopping_subset, ProbabilisticTheory.QuantumMechanics.UnitaryRep.symmetrize, ProbabilisticTheory.QuantumMechanics.UnitaryRep.symmetrize_apply, ProbabilisticTheory.QuantumMechanics.UnitaryRep.conjTranspose_symmetrize
statement: formalized
proof: formalized
---

# Hopping operators and their Bloch matrices

The module `PhyslibAlpha.ProbabilisticTheory.Representation.Hopping`, [PhyslibAlpha/ProbabilisticTheory/Representation/Hopping.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Representation/Hopping.lean): 9 declarations, 7 with a docstring.

> The finite-range translation-invariant operators are the operators whose symbol is a trigonometric
> polynomial.

## i. Overview

> An operator `∑_r π(r) ι(A_r)` with finitely many matrices `A_r` couples each point to finitely many
> other points through the matrices `A_r`. The general theory of `BlochFloquet` applies to it: its
> symbol is the Bloch matrix `b(χ) = ∑_r χ(r) A_r`, a trigonometric polynomial, and the operator is
> the integral of its Bloch matrix. This covers tight-binding Hamiltonians, the dynamical matrices of
> harmonic lattices, adjacency operators of periodic graphs, and the transfer operators of
> translation-invariant classical lattice models alike.

## ii. Key results

> - `UnitaryRep.hopping` : the finite-range translation-invariant operator with matrices `A_r`.
> - `UnitaryRep.blochMatrix` : its Bloch matrix.
> - `UnitaryRep.blochHom_blochMatrix` : the operator is the integral of its Bloch matrix.
> - `UnitaryRep.spectrum_hopping_subset` : the spectrum is contained in the union of the bands.
> - `UnitaryRep.symmetrize` : the Hermitian completion of a family of hopping matrices.
> - `UnitaryRep.isHermitian_blochMatrix` : the Bloch matrix of a Hermitian hopping family is
>   Hermitian at every crystal momentum.

## iv. References

> * None.

## A. The hopping operator and its Bloch matrix

**`ProbabilisticTheory.QuantumMechanics.UnitaryRep.hopping`**, a def, [line 74](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Representation/Hopping.lean#L74).

> A translation-invariant hopping operator `∑_r π(r) ι(A_r)` with finitely many matrices `A_r`,
> the amplitude of hopping by the lattice vector `r` between orbitals.

```lean
def hopping (A : G →₀ Matrix (Fin N) (Fin N) ℂ) : H →L[ℂ] H
```

**`ProbabilisticTheory.QuantumMechanics.UnitaryRep.blochMatrix`**, a def, [line 79](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Representation/Hopping.lean#L79).

> The Bloch matrix `b(χ) = ∑_r χ(r) A_r` of a hopping operator, a continuous matrix-valued
> function on the Brillouin zone.

```lean
def blochMatrix (A : G →₀ Matrix (Fin N) (Fin N) ℂ) :
    C(PontryaginDual (Multiplicative G), Matrix (Fin N) (Fin N) ℂ)
```

**`ProbabilisticTheory.QuantumMechanics.UnitaryRep.blochMatrix_apply`**, a lemma, [line 90](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Representation/Hopping.lean#L90).

```lean
lemma blochMatrix_apply (A : G →₀ Matrix (Fin N) (Fin N) ℂ)
    (χ : PontryaginDual (Multiplicative G)) :
    blochMatrix A χ = A.sum fun r M => ((χ (Multiplicative.ofAdd r) : Circle) : ℂ) • M
```

**`ProbabilisticTheory.QuantumMechanics.UnitaryRep.blochHom_blochMatrix`**, a lemma, [line 97](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Representation/Hopping.lean#L97).

> **The hopping operator is the integral of its Bloch matrix.**

```lean
lemma blochHom_blochMatrix (A : G →₀ Matrix (Fin N) (Fin N) ℂ) :
    blochHom π ι hι (blochMatrix A) = hopping π ι A
```

## B. The spectrum

**`ProbabilisticTheory.QuantumMechanics.UnitaryRep.spectrum_hopping_subset`**, a lemma, [line 141](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Representation/Hopping.lean#L141).

> The spectrum of a finite-range translation-invariant operator is contained in the union of the
> spectra of its Bloch matrices.

```lean
lemma spectrum_hopping_subset (A : G →₀ Matrix (Fin N) (Fin N) ℂ) :
    spectrum ℂ (hopping π ι A) ⊆
      ⋃ χ : PontryaginDual (Multiplicative G), spectrum ℂ (blochMatrix A χ)
```

## C. Hermitian hopping

**`ProbabilisticTheory.QuantumMechanics.UnitaryRep.symmetrize`**, a def, [line 156](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Representation/Hopping.lean#L156).

> The Hermitian completion of a family of hopping matrices: the amplitude for hopping by `r` is
> `A r` plus the adjoint of the amplitude for hopping back by `-r`.

```lean
def symmetrize (A : G →₀ Matrix (Fin N) (Fin N) ℂ) : G →₀ Matrix (Fin N) (Fin N) ℂ
```

**`ProbabilisticTheory.QuantumMechanics.UnitaryRep.symmetrize_apply`**, a lemma, [line 161](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Representation/Hopping.lean#L161).

```lean
lemma symmetrize_apply (A : G →₀ Matrix (Fin N) (Fin N) ℂ) (r : G) :
    symmetrize A r = A r + (A (-r))ᴴ
```

**`ProbabilisticTheory.QuantumMechanics.UnitaryRep.conjTranspose_symmetrize`**, a lemma, [line 168](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Representation/Hopping.lean#L168).

> A symmetrized family of hopping matrices satisfies `(A r)ᴴ = A (-r)`.

```lean
lemma conjTranspose_symmetrize (A : G →₀ Matrix (Fin N) (Fin N) ℂ) (r : G) :
    (symmetrize A r)ᴴ = symmetrize A (-r)
```

**`ProbabilisticTheory.QuantumMechanics.UnitaryRep.isHermitian_blochMatrix`**, a lemma, [line 178](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Representation/Hopping.lean#L178).

> **Hermitian hopping gives Hermitian Bloch matrices.** If `(A r)ᴴ = A (-r)` for every `r`, then
> the Bloch matrix `∑_r χ(r) A_r` is Hermitian at every crystal momentum `χ`.

```lean
lemma isHermitian_blochMatrix (A : G →₀ Matrix (Fin N) (Fin N) ℂ)
    (hA : ∀ r, (A r)ᴴ = A (-r)) (χ : PontryaginDual (Multiplicative G)) :
    (blochMatrix A χ).IsHermitian
```

## Depends on

- [Bloch–Floquet theory for representations with a finite-dimensional internal space](floquet.md)

## Sources

- [PhyslibAlpha/ProbabilisticTheory/Representation/Hopping.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Representation/Hopping.lean)
