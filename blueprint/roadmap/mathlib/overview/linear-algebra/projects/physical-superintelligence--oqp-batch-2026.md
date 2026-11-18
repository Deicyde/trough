---
declaration: theorem
origin: cited
lean: ThreeCopyQutritWerner.x2_qutritEndpointInequality, ThreeCopyQutritWerner.qutritEndpointInequality_of_certificate, ThreeCopyQutritWerner.x2_qutritEndpointInequality_of_facts', ThreeCopyQutritWerner.x2SourceM_posSemidef, ThreeCopyQutritWerner.x2SourceA_posSemidef, ThreeCopyQutritWerner.X2.InGS1.hT0, ThreeCopyQutritWerner.X2.InGA1.hT0, ThreeCopyQutritWerner.X2.InGA2.hT0
statement: formalized
proof: formalized
---

# Open Quantum Problems: a PSI batch, October 2026

[physical-superintelligence/oqp-batch-2026](https://github.com/physical-superintelligence/oqp-batch-2026) at commit [e5dd29ca](https://github.com/physical-superintelligence/oqp-batch-2026/tree/e5dd29ca987a15c883f3a19a97372acf155b617c), 2026-11-13.

> Five results on [Open Quantum Problems](https://oqp.iqoqi.oeaw.ac.at/). Each result folder contains a paper and a Lean 4 formalization. Start with a paper below, or open its result guide for the main theorem statements and supporting files.

*Quoted from [README.md](https://github.com/physical-superintelligence/oqp-batch-2026/blob/e5dd29ca987a15c883f3a19a97372acf155b617c/README.md), Apache-2.0.*

## Depends on

- [Ring-valued matrix](../matrices/ring-valued-matrix.md)
- [Permutation group of a type](../../general-algebra/group-theory/part-02/permutation-group-of-a-type.md)

## Proof depends on

- [Gershgorin circle theorem](../../../thousand-plus/algebra/15-linear-and-multilinear-algebra-matrix-theory/gershgorin-circle-theorem.md)
- [Eigenvector](../structure-theory-of-endomorphisms/eigenvector.md)
- [Rank of a matrix](../../../undergraduate/linear-algebra/matrices/rank-of-a-matrix.md)
- [Range of a linear map](../../../undergraduate/linear-algebra/fundamentals/range-of-a-linear-map.md)
- [Unitary group](../../../undergraduate/group-theory/classical-automorphism-groups/unitary-group.md)
- [Determinant](../matrices/determinant.md)
- [List](../../data-structures/list-like-structures/list.md)
- [Existence of orthonormal basis](../finite-dimensional-inner-product-spaces-see-also/existence-of-orthonormal-basis.md)

## Main results

Its Lean names are 8 of the 19 theorems its README names in code:

- [`ThreeCopyQutritWerner.x2_qutritEndpointInequality`](https://github.com/physical-superintelligence/oqp-batch-2026/blob/e5dd29ca987a15c883f3a19a97372acf155b617c/oqp02-three-copy-werner/lean/ThreeCopyQutritWerner/CertificateX2FinalProof.lean#L24) (theorem)
- [`ThreeCopyQutritWerner.qutritEndpointInequality_of_certificate`](https://github.com/physical-superintelligence/oqp-batch-2026/blob/e5dd29ca987a15c883f3a19a97372acf155b617c/oqp02-three-copy-werner/lean/ThreeCopyQutritWerner/CertificateReduction.lean#L247) (theorem)
- [`ThreeCopyQutritWerner.x2_qutritEndpointInequality_of_facts'`](https://github.com/physical-superintelligence/oqp-batch-2026/blob/e5dd29ca987a15c883f3a19a97372acf155b617c/oqp02-three-copy-werner/lean/ThreeCopyQutritWerner/CertificateX2BridgeTriple.lean#L637) (theorem)
- [`ThreeCopyQutritWerner.x2SourceM_posSemidef`](https://github.com/physical-superintelligence/oqp-batch-2026/blob/e5dd29ca987a15c883f3a19a97372acf155b617c/oqp02-three-copy-werner/lean/ThreeCopyQutritWerner/CertificateX2IntegrationSources.lean#L278) (theorem)
- [`ThreeCopyQutritWerner.x2SourceA_posSemidef`](https://github.com/physical-superintelligence/oqp-batch-2026/blob/e5dd29ca987a15c883f3a19a97372acf155b617c/oqp02-three-copy-werner/lean/ThreeCopyQutritWerner/CertificateX2IntegrationSources.lean#L318) (theorem)
- [`ThreeCopyQutritWerner.X2.InGS1.hT0`](https://github.com/physical-superintelligence/oqp-batch-2026/blob/e5dd29ca987a15c883f3a19a97372acf155b617c/oqp02-three-copy-werner/lean/ThreeCopyQutritWerner/CertificateX2InputGlueS1.lean#L196) (theorem)
- [`ThreeCopyQutritWerner.X2.InGA1.hT0`](https://github.com/physical-superintelligence/oqp-batch-2026/blob/e5dd29ca987a15c883f3a19a97372acf155b617c/oqp02-three-copy-werner/lean/ThreeCopyQutritWerner/CertificateX2InputGlueA1.lean#L196) (theorem)
- [`ThreeCopyQutritWerner.X2.InGA2.hT0`](https://github.com/physical-superintelligence/oqp-batch-2026/blob/e5dd29ca987a15c883f3a19a97372acf155b617c/oqp02-three-copy-werner/lean/ThreeCopyQutritWerner/CertificateX2InputGlueA2.lean#L59) (theorem)

No file its headlines import, directly or not (3326 files), holds `sorry`, `admit` or an axiom.

## Project

- Lean v4.35.0-rc4, Mathlib at [1b3c4196](https://github.com/leanprover-community/mathlib4/tree/1b3c41969602424bd2f04b3d4f731734e5b00cde).
- 5,230 .lean files; its Lean libraries `ThreeCopyQutritWerner`, `Challenge`, `Solution` hold 3,619, declaring 119,138 names, with `sorry` in 1 file and 0 axioms, read without Lean.
- License: Apache-2.0 ([LICENSE](https://github.com/physical-superintelligence/oqp-batch-2026/blob/e5dd29ca987a15c883f3a19a97372acf155b617c/LICENSE)).

## Builds on

- Mathlib, at [1b3c4196](https://github.com/leanprover-community/mathlib4/tree/1b3c41969602424bd2f04b3d4f731734e5b00cde).

## Placement

Of its imports of Mathlib modules in an overview area, 496 of 1826 are in Linear algebra, 4.6 times the average project's share, the most of the areas holding a tenth of its imports.

## Mathlib use

Areas of its Mathlib imports by lift over the average project: Linear algebra (496 of 1826 imports, 4.6×), General algebra (982 of 1826 imports, 1.5×), Data structures (219 of 1826 imports, 0.8×). *Proof depends on* names 8 of the 24 Mathlib concepts its files name, those named most often relative to the other projects.

## Sources

- [physical-superintelligence/oqp-batch-2026 at e5dd29ca](https://github.com/physical-superintelligence/oqp-batch-2026/tree/e5dd29ca987a15c883f3a19a97372acf155b617c)
