---
declaration: lemma
origin: cited
lean: MIPRE.SyncStrategy.isPVMIn, MIPRE.SyncStrategy.mul_eq_zero_of_value_eq_one, MIPRE.Tailored.valStar_le_of_dec, MIPRE.Tailored.permOfSync, MIPRE.Tailored.permOfSync_proj, MIPRE.Tailored.value_permOfSync, MIPRE.Tailored.hasPerfectZPC_of_sync
statement: formalized
proof: formalized
---

# Presenting a game as a tailored game

Let $\mathfrak{G}$ be a tailored game and $\mathfrak{G}'$ a game with the same questions and question distribution. If a map $\mathrm{dec}$ of answers sends every pair that $\mathfrak{G}$ accepts to one that $\mathfrak{G}'$ accepts, then $\mathrm{val}^*(\mathfrak{G}) \le \mathrm{val}^*(\mathfrak{G}')$. Conversely, let $\mathrm{enc}$ send the answers of $\mathfrak{G}'$ at $x$ to $\mathbb{F}_2^{\mathrm{len}(x)}$, sending every accepted pair of answers in a set $\mathrm{ok}$ to a pair $\mathfrak{G}$ accepts, and let $S$ be a perfect PCC strategy of the doubled game of $\mathfrak{G}'$ that charges only answers in $\mathrm{ok}$, whose bit observables along $\mathrm{enc}$ are signed permutations, diagonal at the readable bits. Then these bit observables are a perfect Z-aligned permutation strategy of the doubled tailored game commuting along edges.

## Depends on

- [Z-aligned permutation strategies commuting along edges; II:1043–1057, II:1279–1283](../part-01/def-zpc-strategy.md)
- [When a permutation strategy is perfect](../part-01/lem-perm-strategy-perfect.md)
- [The bit observables of an encoded measurement](lem-encoded-pvm-obs.md)
- [PCC strategy](../../foundations/part-01/def-pcc.md)
- [Synchronous value](../../foundations/part-01/def-sync-value.md)
- [A perfect strategy rejects nothing on the support](../../foundations/part-01/lem-perfect-rejects-nothing.md)
- [Post-processing and detyping, in a model](../../downstream-results/part-02/lem-transports-model.md)

## Proof

The first claim is post-processing of the answers. For the second, the bit observables are commuting involutions commuting along edges (Lemma [The bit observables of an encoded measurement](lem-encoded-pvm-obs.md), from PCC), and their measurement at $x$ is the push-forward of $S$ along $\mathrm{enc}$. A perfect PCC strategy has $M^x_a M^y_b = 0$ for every rejected pair at an edge: the product is a projection, as the two commute, of trace zero. So a pair $(a, b)$ that $\mathfrak{G}$ rejects has $P^x_a P^y_b = \sum M^x_{a'} M^y_{b'}$ over the $a', b'$ encoding to it, each term zero — $a'$ or $b'$ outside $\mathrm{ok}$ carries zero, and otherwise $(a', b')$ is rejected by $\mathfrak{G}'$, or its encoding would be accepted — and the strategy is perfect by Lemma [When a permutation strategy is perfect](../part-01/lem-perm-strategy-perfect.md).

## Lean

Formalized as [`MIPRE.SyncStrategy.isPVMIn`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.SyncStrategy.isPVMIn), [`MIPRE.SyncStrategy.mul_eq_zero_of_value_eq_one`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.SyncStrategy.mul_eq_zero_of_value_eq_one), [`MIPRE.Tailored.valStar_le_of_dec`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.valStar_le_of_dec), [`MIPRE.Tailored.permOfSync`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.permOfSync), [`MIPRE.Tailored.permOfSync_proj`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.permOfSync_proj), [`MIPRE.Tailored.value_permOfSync`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.value_permOfSync), [`MIPRE.Tailored.hasPerfectZPC_of_sync`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.hasPerfectZPC_of_sync).

## Sources

- [MIP* = RE blueprint: content/09_tailored.tex, line 1477](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/09_tailored.tex#L1477)
