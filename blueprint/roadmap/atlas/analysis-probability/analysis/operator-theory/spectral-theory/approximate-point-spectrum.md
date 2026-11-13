---
declaration: section
origin: cited
lean: MathlibExt.Analysis.InnerProductSpace.NormalApproximateSpectrum.IsApproximateEigenvalue, MathlibExt.Analysis.InnerProductSpace.NormalApproximateSpectrum.isApproximateEigenvalue_iff_forall_eps, MathlibExt.Analysis.InnerProductSpace.NormalApproximateSpectrum.isStarNormal_smul_one_sub, MathlibExt.Analysis.InnerProductSpace.NormalApproximateSpectrum.isApproximateEigenvalue_of_mem_spectrum, MathlibExt.Analysis.InnerProductSpace.NormalApproximateSpectrum.mem_spectrum_of_isApproximateEigenvalue, MathlibExt.Analysis.InnerProductSpace.NormalApproximateSpectrum.mem_spectrum_iff_isApproximateEigenvalue, MathlibExt.Analysis.InnerProductSpace.NormalApproximateSpectrum.mem_spectrum_iff_isApproximateEigenvalue_of_isSelfAdjoint, MathlibExt.Analysis.InnerProductSpace.NormalApproximateSpectrum.isApproximateEigenvalue_of_hasEigenvalue
statement: formalized
proof: formalized
---

# Approximate point spectrum

9 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/spectral-theory/approximate-point-spectrum/index.html).

## Approximate eigenvalue of an operator

`μ` is an **approximate eigenvalue** of `T` if there is a sequence of
unit vectors `xₙ` with `(μ • 1 - T) xₙ → 0`.

Formalized by `MathlibExt.Analysis.InnerProductSpace.NormalApproximateSpectrum.IsApproximateEigenvalue`, a definition declared in [MathlibExt/Analysis/InnerProductSpace/NormalApproximateSpectrum.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/NormalApproximateSpectrum.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/spectral-theory/approximate-point-spectrum/index.html#is-approximate-eigenvalue).

## Epsilon characterization of approximate eigenvalues

The `∀ ε > 0` characterization of approximate eigenvalues.

Formalized by `MathlibExt.Analysis.InnerProductSpace.NormalApproximateSpectrum.isApproximateEigenvalue_iff_forall_eps`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/NormalApproximateSpectrum.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/NormalApproximateSpectrum.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/spectral-theory/approximate-point-spectrum/index.html#is-approximate-eigenvalue-iff-forall-eps).

## Scalar shifts of a normal operator are normal

Shifting by a scalar preserves normality.

Formalized by `MathlibExt.Analysis.InnerProductSpace.NormalApproximateSpectrum.isStarNormal_smul_one_sub`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/NormalApproximateSpectrum.lean, line 103](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/NormalApproximateSpectrum.lean#L103). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/spectral-theory/approximate-point-spectrum/index.html#is-star-normal-smul-one-sub).

## Spectral values of a normal operator are approximate eigenvalues

Every spectral value of a normal operator is an approximate eigenvalue.

Formalized by `MathlibExt.Analysis.InnerProductSpace.NormalApproximateSpectrum.isApproximateEigenvalue_of_mem_spectrum`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/NormalApproximateSpectrum.lean, line 115](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/NormalApproximateSpectrum.lean#L115). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/spectral-theory/approximate-point-spectrum/index.html#is-approximate-eigenvalue-of-mem-spectru).

## Approximate eigenvalues lie in the spectrum

Every approximate eigenvalue is a spectral value (no normality needed).

Formalized by `MathlibExt.Analysis.InnerProductSpace.NormalApproximateSpectrum.mem_spectrum_of_isApproximateEigenvalue`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/NormalApproximateSpectrum.lean, line 167](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/NormalApproximateSpectrum.lean#L167). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/spectral-theory/approximate-point-spectrum/index.html#mem-spectrum-of-is-approximate-eigenvalu).

## Spectrum of a normal operator equals its approximate point spectrum

For a normal operator, the spectrum is exactly the approximate point
spectrum.

Formalized by `MathlibExt.Analysis.InnerProductSpace.NormalApproximateSpectrum.mem_spectrum_iff_isApproximateEigenvalue`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/NormalApproximateSpectrum.lean, line 203](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/NormalApproximateSpectrum.lean#L203). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/spectral-theory/approximate-point-spectrum/index.html#mem-spectrum-iff-is-approximate-eigenval).

## Weyl's criterion for self-adjoint operators

Weyl's criterion: for a self-adjoint operator, the spectrum is exactly
the approximate point spectrum.

Formalized by `MathlibExt.Analysis.InnerProductSpace.NormalApproximateSpectrum.mem_spectrum_iff_isApproximateEigenvalue_of_isSelfAdjoint`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/NormalApproximateSpectrum.lean, line 210](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/NormalApproximateSpectrum.lean#L210). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/spectral-theory/approximate-point-spectrum/index.html#mem-spectrum-iff-is-approximate-eigenval-2).

## Eigenvalues are approximate eigenvalues

Exact eigenvalues are approximate eigenvalues.

Formalized by `MathlibExt.Analysis.InnerProductSpace.NormalApproximateSpectrum.isApproximateEigenvalue_of_hasEigenvalue`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/NormalApproximateSpectrum.lean, line 217](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/NormalApproximateSpectrum.lean#L217). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/spectral-theory/approximate-point-spectrum/index.html#is-approximate-eigenvalue-of-has-eigenva).

## Normal operator with trivial kernel has dense range

A normal operator with trivial kernel has dense range: the residual
spectrum of a normal operator is empty.

Formalized by `MathlibExt.Analysis.InnerProductSpace.NormalApproximateSpectrum.denseRange_of_isStarNormal_of_ker_eq_bot`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/NormalApproximateSpectrum.lean, line 243](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/NormalApproximateSpectrum.lean#L243). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/spectral-theory/approximate-point-spectrum/index.html#dense-range-of-is-star-normal-of-ker-eq).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Approximate point spectrum](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/spectral-theory/approximate-point-spectrum/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Analysis/operator-theory/spectral-theory/approximate-point-spectrum)
