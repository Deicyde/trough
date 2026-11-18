---
declaration: module
origin: cited
lean: ProbabilisticTheory.QuantumMechanics.bandOf, ProbabilisticTheory.QuantumMechanics.abs_bandOf_sub_le, ProbabilisticTheory.QuantumMechanics.continuous_bandOf, ProbabilisticTheory.QuantumMechanics.UnitaryRep.isSelfAdjoint_blochHom, ProbabilisticTheory.QuantumMechanics.UnitaryRep.exists_band_eq_of_mem_spectrum
statement: formalized
proof: formalized
---

# Bloch bands

The module `PhyslibAlpha.ProbabilisticTheory.Representation.Bands`, [PhyslibAlpha/ProbabilisticTheory/Representation/Bands.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Representation/Bands.lean): 5 declarations, 5 with a docstring.

> The ordered eigenvalues of a Hermitian Bloch matrix are continuous functions on the Brillouin zone,
> and they exhaust the spectrum of the translation-invariant operator.

## i. Overview

> The eigenvalues of a Hermitian `N × N` matrix, listed in decreasing order, are the bands
> `ε₁(χ) ≥ ⋯ ≥ ε_N(χ)` of a Hermitian Bloch matrix `b(χ)`. By Weyl's inequality the `k`-th
> eigenvalue moves by at most the operator norm of the change of the matrix, so each band `ε_k` is a
> continuous function of the matrix and hence of the crystal momentum `χ`. If the symbol of a
> translation-invariant operator is Hermitian the operator is self-adjoint, and its spectrum is
> contained in the union of the ranges of the bands.

## ii. Key results

> - `bandOf` : the `k`-th largest eigenvalue of a Hermitian matrix.
> - `abs_bandOf_sub_le` : Weyl's inequality for bands.
> - `continuous_bandOf` : bands are continuous functions of a continuous Hermitian family.
> - `UnitaryRep.isSelfAdjoint_blochHom` : the operator of a Hermitian symbol is self-adjoint.
> - `UnitaryRep.exists_band_eq_of_mem_spectrum` : every spectral value is a band value.

## iv. References

> * R. Bhatia, Matrix Analysis, Corollary III.2.6.

## A. Bands of Hermitian matrices

**`ProbabilisticTheory.QuantumMechanics.bandOf`**, a def, [line 60](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Representation/Bands.lean#L60).

> The `k`-th largest eigenvalue of a Hermitian matrix: its `k`-th band.

```lean
def bandOf {N : ℕ} {M : Matrix (Fin N) (Fin N) ℂ} (hM : M.IsHermitian)
    (k : Fin (Fintype.card (Fin N))) : ℝ
```

**`ProbabilisticTheory.QuantumMechanics.abs_bandOf_sub_le`**, a lemma, [line 66](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Representation/Bands.lean#L66).

> **Weyl's inequality for bands**: the `k`-th band of two Hermitian matrices differ by at most
> the operator norm of the difference.

```lean
lemma abs_bandOf_sub_le {N : ℕ} {M S : Matrix (Fin N) (Fin N) ℂ} (hM : M.IsHermitian)
    (hS : S.IsHermitian) (k : Fin (Fintype.card (Fin N))) :
    |bandOf hM k - bandOf hS k| ≤
      ‖LinearMap.toContinuousLinearMap (Matrix.toEuclideanLin (M - S))‖
```

**`ProbabilisticTheory.QuantumMechanics.continuous_bandOf`**, a lemma, [line 77](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Representation/Bands.lean#L77).

> **Bands are continuous**: the `k`-th band of a continuous family of Hermitian matrices is a
> continuous function.

```lean
lemma continuous_bandOf {X : Type*} [TopologicalSpace X] {N : ℕ}
    {b : X → Matrix (Fin N) (Fin N) ℂ} (hb : ∀ x, (b x).IsHermitian) (hc : Continuous b)
    (k : Fin (Fintype.card (Fin N))) : Continuous fun x => bandOf (hb x) k
```

## B. Bands of a translation-invariant operator

**`ProbabilisticTheory.QuantumMechanics.UnitaryRep.isSelfAdjoint_blochHom`**, a lemma, [line 112](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Representation/Bands.lean#L112).

> The operator of a Hermitian symbol is self-adjoint.

```lean
lemma isSelfAdjoint_blochHom
    (b : C(PontryaginDual (Multiplicative G), Matrix (Fin N) (Fin N) ℂ))
    (hb : ∀ χ, (b χ).IsHermitian) : IsSelfAdjoint (blochHom π ι hι b)
```

**`ProbabilisticTheory.QuantumMechanics.UnitaryRep.exists_band_eq_of_mem_spectrum`**, a lemma, [line 123](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Representation/Bands.lean#L123).

> **Every point of the spectrum of the operator of a Hermitian symbol is a band value**: it is
> the `k`-th band `ε_k(χ)` of some crystal momentum `χ`.

```lean
lemma exists_band_eq_of_mem_spectrum
    (b : C(PontryaginDual (Multiplicative G), Matrix (Fin N) (Fin N) ℂ))
    (hb : ∀ χ, (b χ).IsHermitian) {z : ℂ} (hz : z ∈ spectrum ℂ (blochHom π ι hι b)) :
    ∃ (χ : PontryaginDual (Multiplicative G)) (k : Fin (Fintype.card (Fin N))),
      z = ((bandOf (hb χ) k : ℝ) : ℂ)
```

## Depends on

- [Bloch–Floquet theory for representations with a finite-dimensional internal space](floquet.md)

## Proof depends on

- [Courant–Fischer min–max theorem and Weyl's inequality](../../mathematics/part-02/tauceti/part-01/analysis-innerproductspace-courantfischer.md)

## Sources

- [PhyslibAlpha/ProbabilisticTheory/Representation/Bands.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Representation/Bands.lean)
