---
declaration: proposition
origin: cited
lean: MIPRE.Tailored.Sofic.Cq, MIPRE.Tailored.Sofic.ZStrat.rej_le_sum_viol, MIPRE.Tailored.Sofic.rej_quotStrat_le, MIPRE.Tailored.Sofic.gameValue_ge_of_checks
statement: formalized
proof: formalized
---

# Game value of an action passing Checks 1–3; Proposition I:2279

An action passing Checks 1–3 everywhere with value $1 - \varepsilon$ against the associated test gives the game a synchronous value at least $1 - 2 \cdot 2^{2(\Lambda + 1)} \varepsilon$.

## Depends on

- [The trace identity](lem-trace-identity.md)
- [The quotient by $J$](lem-j-quotient.md)
- [Passing a challenge under Checks 1–3](lem-assoc-passes.md)
- [The associated subgroup test; I:2086](def-assoc-test.md)
- [Subgroup tests and their sofic value; I:439–520](def-subgroup-test.md)
- [The Fourier transform; II:974–1006](../../the-aldous-lyons-track-tmip-re/part-01/lem-fourier-pvm.md)

## Proof

By the trace identity, the game's rejection mass at $(x, y)$ is at most the sum over the distinct constraint words of the fraction of representatives they do not fix, hence at most the number of constraint words, twice, times the test's failure probability at $(x, y)$; there are at most $2^{2(\Lambda + 1)}$ of them. This replaces the paper's Fourier bases and orbit decompositions.

## Lean

Formalized as [`MIPRE.Tailored.Sofic.Cq`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Sofic.Cq), [`MIPRE.Tailored.Sofic.ZStrat.rej_le_sum_viol`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Sofic.ZStrat.rej_le_sum_viol), [`MIPRE.Tailored.Sofic.rej_quotStrat_le`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Sofic.rej_quotStrat_le), [`MIPRE.Tailored.Sofic.gameValue_ge_of_checks`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Sofic.gameValue_ge_of_checks).

## Sources

- [MIP* = RE blueprint: content/10_subgroup_tests.tex, line 301](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/10_subgroup_tests.tex#L301)
