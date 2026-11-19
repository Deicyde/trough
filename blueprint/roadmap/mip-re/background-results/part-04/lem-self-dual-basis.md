---
declaration: lemma
origin: cited
lean: MIPRE.SAT.shoupSelfDualNormalBasis_selfDual, MIPRE.SAT.shoupSelfDualNormalBasis_normal, MIPRE.SAT.shoupSelfDualNormalBasisProg, MIPRE.SAT.shoupSelfDualNormalBasisProg_correct, MIPRE.SAT.shoupSelfDualNormalDataProg, MIPRE.SAT.shoupSelfDualNormalDataProg_correct, MIPRE.SAT.shoupSelfDualNormalDataProg_time_le, MIPRE.SAT.effective_selfDualNormalBasis
statement: formalized
proof: formalized
---

# Deterministic self-dual normal basis

There is a deterministic algorithm that, given an odd integer $k > 0$, outputs in time $\mathrm{poly}(k)$ a self-dual normal basis of $\mathbb{F}_{2^k}$ over $\mathbb{F}_2$ together with its multiplication tables.

## Depends on

- [Self-dual and normal bases](def-self-dual-basis.md)
- [Uniform deterministic binary irreducible polynomials](../part-05/lem-binary-uniform-irreducible.md)
- [Effective polynomial-basis field arithmetic](../part-05/lem-effective-binary-field-arithmetic.md)
- [Effective Frobenius, trace Gram matrices and table transport](../part-05/lem-effective-field-matrices.md)
- [Effective normal element by fixed-space projections](../part-05/lem-effective-normal-element.md)
- [Effective self-dualization of a supplied normal basis](../part-05/lem-effective-normal-selfdualization.md)
- [The bespoke PCP for deciders](../../structure-of-the-proof/part-07/thm-pcp-decider.md)

## Proof depends on

- [Effective binary matrix arithmetic and elimination](../part-05/lem-effective-binary-linear-algebra.md)
- [Effective inversion, Frobenius iteration and trace](../part-05/lem-effective-field-inverse-trace.md)
- [Effective circuit polynomial evaluation](../../structure-of-the-proof/part-07/lem-pcp-circuit-evaluator.md)

## Proof

Construct the normal basis by Lemma [Effective normal element by fixed-space projections](../part-05/lem-effective-normal-element.md), apply Lemma [Effective self-dualization of a supplied normal basis](../part-05/lem-effective-normal-selfdualization.md), and transport the multiplication table by Lemma [Effective Frobenius, trace Gram matrices and table transport](../part-05/lem-effective-field-matrices.md). The composed ambient program has unary degree as its only input and prints both the basis vectors and all table coefficients. Its source runtime is bounded by a fixed polynomial in $k$.

## Lean

Formalized as [`MIPRE.SAT.shoupSelfDualNormalBasis_selfDual`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.SAT.shoupSelfDualNormalBasis_selfDual), [`MIPRE.SAT.shoupSelfDualNormalBasis_normal`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.SAT.shoupSelfDualNormalBasis_normal), [`MIPRE.SAT.shoupSelfDualNormalBasisProg`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.SAT.shoupSelfDualNormalBasisProg), [`MIPRE.SAT.shoupSelfDualNormalBasisProg_correct`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.SAT.shoupSelfDualNormalBasisProg_correct), [`MIPRE.SAT.shoupSelfDualNormalDataProg`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.SAT.shoupSelfDualNormalDataProg), [`MIPRE.SAT.shoupSelfDualNormalDataProg_correct`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.SAT.shoupSelfDualNormalDataProg_correct), [`MIPRE.SAT.shoupSelfDualNormalDataProg_time_le`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.SAT.shoupSelfDualNormalDataProg_time_le), [`MIPRE.SAT.effective_selfDualNormalBasis`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.SAT.effective_selfDualNormalBasis).

## Sources

- [MIP* = RE blueprint: content/03_background_results.tex, line 6323](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/03_background_results.tex#L6323)
