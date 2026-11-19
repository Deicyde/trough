---
declaration: lemma
origin: cited
lean: MIPRE.Tailored.Sofic.sigBound, MIPRE.Tailored.Sofic.sig_le, MIPRE.Tailored.Sofic.mdeg, MIPRE.Tailored.Sofic.sum_mdeg, MIPRE.Tailored.Sofic.sig_genX_le
statement: formalized
proof: formalized
---

# Significance of the associated test; Proposition I:2283

In the associated test every generator has significance at most a bound $S(\Lambda)$ of order $\Lambda 4^{\Lambda}$, and the variables at a vertex $x$ at most $S(\Lambda)$ times the weight of the question pairs containing $x$.

## Depends on

- [The associated subgroup test; I:2086](def-assoc-test.md)
- [Robustness of the value; Claim I:1480](lem-test-robust.md)

## Proof

The words of the challenge at $(x, y)$ use only $J$ and the variables at $x$ and $y$; their number and lengths are bounded, the constraint words by deduplication.

## Lean

Formalized as [`MIPRE.Tailored.Sofic.sigBound`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Sofic.sigBound), [`MIPRE.Tailored.Sofic.sig_le`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Sofic.sig_le), [`MIPRE.Tailored.Sofic.mdeg`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Sofic.mdeg), [`MIPRE.Tailored.Sofic.sum_mdeg`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Sofic.sum_mdeg), [`MIPRE.Tailored.Sofic.sig_genX_le`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Sofic.sig_genX_le).

## Sources

- [MIP* = RE blueprint: content/10_subgroup_tests.tex, line 183](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/10_subgroup_tests.tex#L183)
