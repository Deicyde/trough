---
declaration: lemma
origin: cited
lean: MIPRE.Tailored.Sofic.ZStrat.rsgn, MIPRE.Tailored.Sofic.ZStrat.sum_trace_proj_mul_mul_proj, MIPRE.Tailored.Sofic.consBit, MIPRE.Tailored.Sofic.satisfies_iff_consBit, MIPRE.Tailored.Sofic.ZStrat.consMat, MIPRE.Tailored.Sofic.ZStrat.proj_mul_consMat_mul_proj
statement: formalized
proof: formalized
---

# The trace identity

For such a strategy, the sum over the answer pairs whose readable parts lie in a set $R$ of $\mathrm{Tr}(P_a\, X\, Q_b)$ is the sum of the diagonal entries $X_{jj}$ over the basis points $j$ whose readable signs lie in $R$. For a constraint $c$ with matrix $M_c = (-1)^{c_J} U^{\alpha} V^{\beta}$, the probability that the readable parts are $r$ and $c$ is violated is $\frac1m \sum_{j \in R_r} \frac{1 - (M_c)_{jj}}{2}$.

## Depends on

- [Z-aligned signed-permutation strategies without commutation along edges](def-zstrat.md)
- [Signed permutations; II:1008–1069](../../the-aldous-lyons-track-tmip-re/part-01/def-signed-perm.md)
- [Signed permutation matrices](../../the-aldous-lyons-track-tmip-re/part-01/lem-signed-perm.md)
- [The three forms of a measurement with outcomes in $\mathbb{F}_2^k$; II:972–1006](../../the-aldous-lyons-track-tmip-re/part-01/def-fourier-forms.md)
- [The Fourier transform; II:974–1006](../../the-aldous-lyons-track-tmip-re/part-01/lem-fourier-pvm.md)

## Proof

A basis point lies in the support of $P_a$ only if its readable signs are those of $a$, and the projections sum to the identity; the observable of a constraint is $(-1)^{\langle c, (a, b, 1) \rangle}$ on the range of $P_a \otimes Q_b$.

## Lean

Formalized as [`MIPRE.Tailored.Sofic.ZStrat.rsgn`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Sofic.ZStrat.rsgn), [`MIPRE.Tailored.Sofic.ZStrat.sum_trace_proj_mul_mul_proj`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Sofic.ZStrat.sum_trace_proj_mul_mul_proj), [`MIPRE.Tailored.Sofic.consBit`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Sofic.consBit), [`MIPRE.Tailored.Sofic.satisfies_iff_consBit`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Sofic.satisfies_iff_consBit), [`MIPRE.Tailored.Sofic.ZStrat.consMat`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Sofic.ZStrat.consMat), [`MIPRE.Tailored.Sofic.ZStrat.proj_mul_consMat_mul_proj`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Sofic.ZStrat.proj_mul_consMat_mul_proj).

## Sources

- [MIP* = RE blueprint: content/10_subgroup_tests.tex, line 242](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/10_subgroup_tests.tex#L242)
