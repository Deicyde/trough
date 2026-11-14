---
declaration: lemma
origin: cited
lean: MIPRE.tensorFamily, MIPRE.SyncStrategy.tensorPow, MIPRE.SyncStrategy.value_tensorPow, MIPRE.SyncStrategy.isPCC_tensorPow, MIPRE.SyncStrategy.tensorPowDoubled, MIPRE.exists_perfectPCC_repeat_doubled
statement: formalized
proof: formalized
---

# Tensor powers of synchronous strategies

Let $\mathfrak{G}$ be a synchronous game and $\mathscr{S} = (d, M)$ a synchronous strategy for it. The $k$-fold tensor power $\mathscr{S}^{\otimes k} = (d^k, M^{\otimes k})$, with $M^{\bar{x}}_{\bar{a}} = \bigotimes_{i=1}^{k} M^{x_i}_{a_i}$, is a synchronous strategy for the direct repetition $\mathfrak{G}^{k}$ whose value is the $k$-th power of the value of $\mathscr{S}$, and it is PCC if $\mathscr{S}$ is. In particular a value-$1$ PCC strategy for the doubled game of a game $\mathfrak{G}$ gives one for the doubled game of $\mathfrak{G}^{k}$, for every $k$, the tag being read on every coordinate.

## Depends on

- [Direct repetition](def-direct-repetition.md)
- [Synchronous strategy](../foundations/part-01/def-sync-strategy.md)
- [PCC strategy](../foundations/part-01/def-pcc.md)
- [Synchronous value](../foundations/part-01/def-sync-value.md)

## Proof

The normalized trace on $\mathbb{C}^{d^k}$ of a tensor product is the product of the normalized traces on $\mathbb{C}^d$ (the trace of a product of two projections being real), and the distribution and predicate of $\mathfrak{G}^{k}$ are products, so each summand of the value of $\mathscr{S}^{\otimes k}$ is the product over the coordinates of the corresponding summands of the value of $\mathscr{S}$, and the sum over $k$-tuples of questions and answers is the $k$-th power of the sum. Commutation is coordinatewise, on the support of the product distribution, which is the product of the supports. For the doubled reading, the strategy on the doubled repetition is the tensor power relabeled along $(t, \bar{x}) \mapsto ((t, x_i))_i$, which is injective and covers the support of the doubled repeated distribution.

## Lean

Formalized as [`MIPRE.tensorFamily`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.tensorFamily), [`MIPRE.SyncStrategy.tensorPow`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.SyncStrategy.tensorPow), [`MIPRE.SyncStrategy.value_tensorPow`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.SyncStrategy.value_tensorPow), [`MIPRE.SyncStrategy.isPCC_tensorPow`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.SyncStrategy.isPCC_tensorPow), [`MIPRE.SyncStrategy.tensorPowDoubled`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.SyncStrategy.tensorPowDoubled), [`MIPRE.exists_perfectPCC_repeat_doubled`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.exists_perfectPCC_repeat_doubled).

## Sources

- [MIP* = RE blueprint: content/05_parallel_repetition.tex, line 247](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/05_parallel_repetition.tex#L247)
