---
declaration: module
origin: cited
lean: ProbabilisticTheory.QuantumMechanics.Essential.isFormalAdjoint_smul_real, ProbabilisticTheory.QuantumMechanics.Essential.exists_apply_sub_smul_eq, ProbabilisticTheory.QuantumMechanics.Essential.smul_surjective_sub_smul, ProbabilisticTheory.QuantumMechanics.Essential.isSelfAdjoint_smul_real, ProbabilisticTheory.QuantumMechanics.Essential.mem_essSpectrum_smul_real, ProbabilisticTheory.QuantumMechanics.Essential.essSpectrum_congr_op, ProbabilisticTheory.QuantumMechanics.Essential.smul_inv_smul_pmap, ProbabilisticTheory.QuantumMechanics.Essential.essSpectrum_smul_real
statement: formalized
proof: formalized
---

# Scaling self-adjoint operators

The module `PhyslibAlpha.ProbabilisticTheory.HilbertSpace.Unbounded.EssentialSpectrum.Smul`, [PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/EssentialSpectrum/Smul.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/EssentialSpectrum/Smul.lean): 8 declarations, 8 with a docstring.

> Real scaling preserves self-adjointness and scales the essential spectrum.

## i. Overview

> For a self-adjoint operator `A` and a real `c ≠ 0`, `c • A` is self-adjoint and its essential
> spectrum is the essential spectrum of `A` scaled by `c`.

## ii. Key results

> - `isSelfAdjoint_smul_real` : `c • A` is self-adjoint.
> - `essSpectrum_smul_real` : the essential spectrum scales with `c`.

## iv. References

> - Adapted from `adambornemann-glitch/Spectra`, `SpectralTheory/Essential/Smul.lean` (Apache 2.0).

## A. L1: self-adjointness under real scaling

**`ProbabilisticTheory.QuantumMechanics.Essential.isFormalAdjoint_smul_real`**, a lemma, [line 54](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/EssentialSpectrum/Smul.lean#L54).

> For a real scalar `c`, `c • A` is formally self-adjoint when `A` is.

```lean
lemma isFormalAdjoint_smul_real {A : H →ₗ.[ℂ] H} (hsym : A.IsFormalAdjoint A)
    (c : ℝ) : (((c : ℂ)) • A).IsFormalAdjoint (((c : ℂ)) • A)
```

**`ProbabilisticTheory.QuantumMechanics.Essential.exists_apply_sub_smul_eq`**, a lemma, [line 62](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/EssentialSpectrum/Smul.lean#L62).

> For self-adjoint `A` and `z` off the real axis, every vector is `A ψ - z ψ` for some `ψ` in the
> domain of `A`.

```lean
lemma exists_apply_sub_smul_eq {A : H →ₗ.[ℂ] H} (hA : IsSelfAdjoint A) {z : ℂ} (hz : z.im ≠ 0)
    (φ : H) : ∃ ψ : A.domain, A ψ - z • (ψ : H) = φ
```

**`ProbabilisticTheory.QuantumMechanics.Essential.smul_surjective_sub_smul`**, a lemma, [line 72](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/EssentialSpectrum/Smul.lean#L72).

> Surjectivity of `c•A - w` reduces to surjectivity of `A - w/c` (real `c ≠ 0`).

```lean
lemma smul_surjective_sub_smul {A : H →ₗ.[ℂ] H} (hA : IsSelfAdjoint A)
    (c : ℝ) (hc : c ≠ 0) (w : ℂ) (hw : w.im ≠ 0) :
    ∀ φ : H, ∃ ψ : ((c : ℂ) • A).domain, ((c : ℂ) • A) ψ - w • (ψ : H) = φ
```

**`ProbabilisticTheory.QuantumMechanics.Essential.isSelfAdjoint_smul_real`**, a lemma, [line 94](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/EssentialSpectrum/Smul.lean#L94).

> **L1.** If `A` is self-adjoint and `c : ℝ` is nonzero, then `(c : ℂ) • A` is self-adjoint.

```lean
lemma isSelfAdjoint_smul_real {A : H →ₗ.[ℂ] H} (hA : IsSelfAdjoint A)
    (c : ℝ) (hc : c ≠ 0) : IsSelfAdjoint ((c : ℂ) • A)
```

## B. L2: essential spectrum under real scaling

**`ProbabilisticTheory.QuantumMechanics.Essential.mem_essSpectrum_smul_real`**, a lemma, [line 124](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/EssentialSpectrum/Smul.lean#L124).

> A Weyl sequence for `A` at `λ` is a Weyl sequence for `c • A` at `c·λ` (real `c`).

```lean
lemma mem_essSpectrum_smul_real {A : H →ₗ.[ℂ] H} (hA : IsSelfAdjoint A)
    (c : ℝ) (hc : c ≠ 0) {lam : ℝ} (hlam : lam ∈ essSpectrum hA) :
    c * lam ∈ essSpectrum (isSelfAdjoint_smul_real hA c hc)
```

**`ProbabilisticTheory.QuantumMechanics.Essential.essSpectrum_congr_op`**, a lemma, [line 150](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/EssentialSpectrum/Smul.lean#L150).

> `essSpectrum` depends only on the operator, not on the self-adjointness witness.

```lean
lemma essSpectrum_congr_op {A B : H →ₗ.[ℂ] H} (hA : IsSelfAdjoint A) (hB : IsSelfAdjoint B)
    (h : A = B) : essSpectrum hA = essSpectrum hB
```

**`ProbabilisticTheory.QuantumMechanics.Essential.smul_inv_smul_pmap`**, a lemma, [line 156](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/EssentialSpectrum/Smul.lean#L156).

> Scaling by `c` then by `c⁻¹` is the identity operator (real `c ≠ 0`).

```lean
lemma smul_inv_smul_pmap {A : H →ₗ.[ℂ] H} (c : ℝ) (hc : c ≠ 0) :
    ((c⁻¹ : ℝ) : ℂ) • (((c : ℂ)) • A) = A
```

**`ProbabilisticTheory.QuantumMechanics.Essential.essSpectrum_smul_real`**, a lemma, [line 165](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/EssentialSpectrum/Smul.lean#L165).

> **L2.** The essential spectrum scales by a real nonzero `c`:
> `essSpectrum (c • A) = (· * c) '' essSpectrum A`.

```lean
lemma essSpectrum_smul_real {A : H →ₗ.[ℂ] H} (hA : IsSelfAdjoint A)
    (c : ℝ) (hc : c ≠ 0) :
    essSpectrum (isSelfAdjoint_smul_real hA c hc) = (fun μ => c * μ) '' essSpectrum hA
```

## Depends on

- [The essential spectrum](unbounded-essentialspectrum-defs.md)

## Proof depends on

- [Spectral theory for self-adjoint operators](../../../../physlib/quantummechanics/operators/spectraltheory/selfadjoint.md)

## Sources

- [PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/EssentialSpectrum/Smul.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/EssentialSpectrum/Smul.lean)
