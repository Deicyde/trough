---
declaration: module
origin: cited
lean: ProbabilisticTheory.QuantumMechanics.Essential.essSpectrum, ProbabilisticTheory.QuantumMechanics.Essential.mem_essSpectrum_of_seq
statement: formalized
proof: formalized
---

# The essential spectrum

The module `PhyslibAlpha.ProbabilisticTheory.HilbertSpace.Unbounded.EssentialSpectrum.Defs`, [PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/EssentialSpectrum/Defs.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/EssentialSpectrum/Defs.lean): 2 declarations, 2 with a docstring.

> The essential spectrum of a self-adjoint operator, defined by singular sequences.

## i. Overview

> A real number `λ` is in the essential spectrum of a self-adjoint operator `A` when there is a
> singular sequence for `λ`: vectors `ψₙ` in the domain of `A` with `‖ψₙ‖ → 1`, `⟪g, ψₙ⟫ → 0` for
> every `g`, and `‖A ψₙ - λ ψₙ‖ → 0`. Orthonormal approximate eigenvectors are singular sequences.

## ii. Key results

> - `essSpectrum` : the essential spectrum of a self-adjoint operator.
> - `mem_essSpectrum_of_seq` : membership from a singular sequence.

## iv. References

> - Adapted from `adambornemann-glitch/Spectra`, `SpectralTheory/Essential/Defs.lean` (Apache 2.0).

## A. Singular sequences and the essential spectrum

**`ProbabilisticTheory.QuantumMechanics.Essential.essSpectrum`**, a def, [line 59](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/EssentialSpectrum/Defs.lean#L59).

> The **essential spectrum** of a self-adjoint operator `A`, defined by singular (Weyl)
> sequences: `λ ∈ essSpectrum hA` iff there is `ψ : ℕ → A.domain` with `‖ψ n‖ → 1`, `ψ` weakly null,
> and `‖A ψ n − λ ψ n‖ → 0`. (`hA` is carried for discoverability; the set depends only on `A`.)

```lean
def essSpectrum {A : H →ₗ.[ℂ] H} (_hA : IsSelfAdjoint A) : Set ℝ
```

**`ProbabilisticTheory.QuantumMechanics.Essential.mem_essSpectrum_of_seq`**, a lemma, [line 67](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/EssentialSpectrum/Defs.lean#L67).

> Membership in `essSpectrum` from an `H`-valued Weyl sequence together with a domain-membership
> witness. This packages the `ℕ → A.domain` data so callers can work with plain vectors.

```lean
lemma mem_essSpectrum_of_seq {A : H →ₗ.[ℂ] H} (hA : IsSelfAdjoint A) (lam : ℝ)
    (φ : ℕ → H) (hmem : ∀ n, φ n ∈ A.domain)
    (hnorm : Tendsto (fun n => ‖φ n‖) atTop (𝓝 1))
    (hweak : ∀ g : H, Tendsto (fun n => ⟪g, φ n⟫_ℂ) atTop (𝓝 0))
    (heig : Tendsto (fun n => ‖A ⟨φ n, hmem n⟩ - (lam : ℂ) • φ n‖) atTop (𝓝 0)) :
    lam ∈ essSpectrum hA
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/EssentialSpectrum/Defs.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/EssentialSpectrum/Defs.lean)
