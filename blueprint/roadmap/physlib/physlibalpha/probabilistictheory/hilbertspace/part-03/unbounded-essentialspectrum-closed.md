---
declaration: module
origin: cited
lean: ProbabilisticTheory.QuantumMechanics.Essential.isClosed_essSpectrum
statement: formalized
proof: formalized
---

# The essential spectrum is closed

The module `PhyslibAlpha.ProbabilisticTheory.HilbertSpace.Unbounded.EssentialSpectrum.Closed`, [PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/EssentialSpectrum/Closed.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/EssentialSpectrum/Closed.lean): 1 declaration, 1 with a docstring.

> The essential spectrum of a self-adjoint operator is closed.

## i. Overview

> The essential spectrum of a self-adjoint operator is closed. For `λₖ → λ` in the essential spectrum,
> all singular sequences of the `λₖ` lie in a separable closed subspace. A diagonal choice, almost
> orthogonal to more and more vectors of a countable dense subset, is a singular sequence for `λ`.

## ii. Key results

> - `isClosed_essSpectrum` : the essential spectrum is closed.

## iv. References

> - Adapted from `adambornemann-glitch/Spectra`, `SpectralTheory/Essential/Closed.lean` (Apache 2.0).

## A. Closedness of the essential spectrum

**`ProbabilisticTheory.QuantumMechanics.Essential.isClosed_essSpectrum`**, a lemma, [line 56](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/EssentialSpectrum/Closed.lean#L56).

> The essential spectrum is closed.

```lean
lemma isClosed_essSpectrum {A : H →ₗ.[ℂ] H} (hA : IsSelfAdjoint A) :
    IsClosed (essSpectrum hA)
```

## Depends on

- [The essential spectrum](unbounded-essentialspectrum-defs.md)

## Sources

- [PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/EssentialSpectrum/Closed.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/EssentialSpectrum/Closed.lean)
