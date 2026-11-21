---
declaration: theorem
origin: cited
lean: KAM.Certificate.checkTorusCertificate_sound, KAM.CertificateSharp.checkTorusCertificateSharp_sound, KAM.Certificate.toyCert3_torus, KAM.EffectiveStability.checkOscChain_sound, KAM.EffectiveStability.certifiedTorus_confinement, KAM.Application.Confinement.hamiltonian_approxIntegrals_confinement, KAM.EffectiveStability.SJSU.sjsu_secular_confinement_proof
statement: formalized
---

# KAM-dev — campaign HQ

[scottnarmstrong/KAM-dev](https://github.com/scottnarmstrong/KAM-dev) at commit [1adf7cd3](https://github.com/scottnarmstrong/KAM-dev/tree/1adf7cd386d54900e28ab4ba81fbfe9f5b1ced5a), 2026-11-18.

> Lean 4 + Mathlib formalization of the **Kolmogorov–Arnold–Moser theorem** in its positive-measure form: for a nearly-integrable real-analytic Hamiltonian H(θ, I) = h(I) + f(θ, I) with a Kolmogorov-nondegenerate h, most of phase space is filled by invariant Lagrangian tori that carry quasi-periodic motion with Diophantine frequencies, as soon as f is small enough.

*Quoted from [README.md](https://github.com/scottnarmstrong/KAM-dev/blob/1adf7cd386d54900e28ab4ba81fbfe9f5b1ced5a/README.md), Apache-2.0.*

## Depends on

- [Associative algebra over a commutative ring](../../../general-algebra/algebras-over-a-ring/associative-algebra-over-a-commutative-ring.md)
- [Derivative at a point](../../../../undergraduate/single-variable-real-analysis/differentiability/derivative-at-a-point.md)
- [Set](../../../data-structures/sets/set.md)
- [Holomorphic functions](../../../../undergraduate/single-variable-complex-analysis/functions-on-one-complex-variable/holomorphic-functions.md)
- [Extended real number](../../../general-algebra/numbers/extended-real-number.md)
- [Compactness in terms of filters](../../../topology/general-topology/part-01/compactness-in-terms-of-filters.md)
- [Closure](../../../topology/general-topology/part-01/closure.md)
- [Differentials (linear tangent functions)](../../../../undergraduate/multivariable-calculus/differential-calculus/differentials-linear-tangent-functions.md)

## Proof depends on

- [Change of coordinates](../../../../undergraduate/bilinear-and-quadratic-forms-over-a-vector-space/bilinear-forms/change-of-coordinates.md)
- [Rational number](../../../general-algebra/numbers/rational-number.md)
- [Natural number](../../../general-algebra/numbers/natural-number.md)
- [Matrix representation](../../../linear-algebra/bilinear-and-quadratic-forms/matrix-representation.md)
- [Heine-Borel theorem (finite-dimensional normed spaces are proper)](../../normed-vector-spaces-banach-spaces/heine-borel-theorem-finite-dimensional-normed-sp.md)
- [Cos (extension of trigonometric functions to the complex plane)](../../../../undergraduate/single-variable-complex-analysis/complex-valued-series/extension-of-trigonometric-functions-to-the-comp/cos.md)
- [Equivalence of norms in finite dimension](../../normed-vector-spaces-banach-spaces/equivalence-of-norms-in-finite-dimension.md)
- [Sin (extension of trigonometric functions to the complex plane)](../../../../undergraduate/single-variable-complex-analysis/complex-valued-series/extension-of-trigonometric-functions-to-the-comp/sin.md)

## Main results

Its Lean names are the theorems its README names in code:

- [`KAM.Certificate.checkTorusCertificate_sound`](https://github.com/scottnarmstrong/KAM-dev/blob/1adf7cd386d54900e28ab4ba81fbfe9f5b1ced5a/KAM/Certificate/Soundness.lean#L62) (theorem)
- [`KAM.CertificateSharp.checkTorusCertificateSharp_sound`](https://github.com/scottnarmstrong/KAM-dev/blob/1adf7cd386d54900e28ab4ba81fbfe9f5b1ced5a/KAM/CertificateSharp/Sound.lean#L38) (theorem)
- [`KAM.Certificate.toyCert3_torus`](https://github.com/scottnarmstrong/KAM-dev/blob/1adf7cd386d54900e28ab4ba81fbfe9f5b1ced5a/KAM/Certificate/Tests/Toy3.lean#L53) (theorem)
- [`KAM.EffectiveStability.checkOscChain_sound`](https://github.com/scottnarmstrong/KAM-dev/blob/1adf7cd386d54900e28ab4ba81fbfe9f5b1ced5a/KAM/EffectiveStability/OscillatorChainCheck.lean#L120) (theorem)
- [`KAM.EffectiveStability.certifiedTorus_confinement`](https://github.com/scottnarmstrong/KAM-dev/blob/1adf7cd386d54900e28ab4ba81fbfe9f5b1ced5a/KAM/EffectiveStability/CertifiedTorusRoute.lean#L49) (theorem)
- [`KAM.Application.Confinement.hamiltonian_approxIntegrals_confinement`](https://github.com/scottnarmstrong/KAM-dev/blob/1adf7cd386d54900e28ab4ba81fbfe9f5b1ced5a/KAM/Application/Confinement/ApproxIntegral.lean#L295) (theorem)
- [`KAM.EffectiveStability.SJSU.sjsu_secular_confinement_proof`](https://github.com/scottnarmstrong/KAM-dev/blob/1adf7cd386d54900e28ab4ba81fbfe9f5b1ced5a/KAM/EffectiveStability/SJSU/Confinement/Proof.lean#L111) (theorem)

## Project

- Lean v4.35.0, Mathlib at [56a00585](https://github.com/leanprover-community/mathlib4/tree/56a005855ea17e0b0958f73ec801ae140b0a1679).
- 29,055 .lean files; its Lean libraries `KAM`, `KAMLunarBand`, `KAMLunarLock`, `KAMMagneticBarrier`, `KAMHenonHeiles`, `KAMSJSU` hold 5,000 (the first read), declaring 35,407 names, with `sorry` in 1 file and 0 axioms, read without Lean.
- License: Apache-2.0 ([LICENSE](https://github.com/scottnarmstrong/KAM-dev/blob/1adf7cd386d54900e28ab4ba81fbfe9f5b1ced5a/LICENSE)).

## Builds on

- Mathlib, at [56a00585](https://github.com/leanprover-community/mathlib4/tree/56a005855ea17e0b0958f73ec801ae140b0a1679).

## Placement

Of its imports of Mathlib modules in an overview area, 102 of 160 are in Analysis, 2.3 times the average project's share, the most of the areas holding a tenth of its imports.

## Mathlib use

Areas of its Mathlib imports by lift over the average project: Analysis (102 of 160 imports, 2.3×), General algebra (35 of 160 imports, 0.6×). *Proof depends on* lists 8 of the 58 Mathlib overview articles whose Lean names its files write, those written most often relative to the other projects; a name match, not an import.

## Sources

- [scottnarmstrong/KAM-dev at 1adf7cd3](https://github.com/scottnarmstrong/KAM-dev/tree/1adf7cd386d54900e28ab4ba81fbfe9f5b1ced5a)
