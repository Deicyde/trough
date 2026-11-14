---
declaration: lemma
origin: cited
lean: MIPRE.Tailored.PermStrategy.encObs_ansProj, MIPRE.Tailored.PermStrategy.encObs_ansProj_bit, MIPRE.Tailored.PermStrategy.encObs_ansProj_const
statement: formalized
proof: formalized
---

# The input strategy's answer bits

Read a permutation strategy as the synchronous strategy measuring answer strings, as in Lemma [ZPC strategies are PCC strategies](../part-01/lem-zpc-pcc.md). An answer bit that copies the $j$-th bit of the answers at $x$ has observable $U(x, j)$, and a constant answer bit has observable $\pm {I}$.

## Depends on

- [The bit observables of an encoded measurement](lem-encoded-pvm-obs.md)
- [The Fourier transform; II:974–1006](../part-01/lem-fourier-pvm.md)
- [Normal form verifier in the ambient model](../../foundations/part-03/def-normal-verifier.md)
- [Signed permutations; II:1008–1069](../part-01/def-signed-perm.md)
- [Tailored game; II:1243](../part-01/def-tailored-game.md)
- [Z-aligned permutation strategies commuting along edges; II:1043–1057, II:1279–1283](../part-01/def-zpc-strategy.md)
- [When a permutation strategy is perfect](../part-01/lem-perm-strategy-perfect.md)
- [Signed permutation matrices](../part-01/lem-signed-perm.md)

## Proof

The synchronous strategy charges only the strings of length $\mathrm{len}(x)$, with the Fourier transform of the observables at $x$; on them the bit observable is $\sum_v (-1)^{v_j} P^x_v = U(x, j)$ (Lemma [The Fourier transform; II:974–1006](../part-01/lem-fourier-pvm.md)), resp. $\pm \sum_v P^x_v = \pm {I}$.

## Lean

Formalized as [`MIPRE.Tailored.PermStrategy.encObs_ansProj`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.PermStrategy.encObs_ansProj), [`MIPRE.Tailored.PermStrategy.encObs_ansProj_bit`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.PermStrategy.encObs_ansProj_bit), [`MIPRE.Tailored.PermStrategy.encObs_ansProj_const`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.PermStrategy.encObs_ansProj_const).

## Sources

- [MIP* = RE blueprint: content/09_tailored.tex, line 1458](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/09_tailored.tex#L1458)
