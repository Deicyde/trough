---
declaration: lemma
origin: cited
lean: MIPRE.Tailored.PermStrategy.toSync, MIPRE.Tailored.PermStrategy.isPCC_toSync, MIPRE.Tailored.PermStrategy.value_toSync, MIPRE.Tailored.PermStrategy.double, MIPRE.Tailored.PermStrategy.value_double, MIPRE.Tailored.TailoredGame.HasPerfectZPC.doubled, MIPRE.Tailored.TailoredGame.HasPerfectZPC.exists_pcc, MIPRE.Tailored.TailoredGame.HasPerfectZPC.syncValue_eq_one, MIPRE.Tailored.TailoredGame.HasPerfectZPC.valStar_eq_one
statement: formalized
proof: formalized
---

# ZPC strategies are PCC strategies

Let $G$ be a tailored game. A permutation strategy for its doubled game defines a synchronous strategy (Definition [Synchronous strategy](../../foundations/part-01/def-sync-strategy.md)) for the doubled game of the bipartite game of $G$: at $(t, x)$ it measures an answer string of length $\ell(x)$ with $P^{(t, x)}$ of its bits, and gives every other string the operator $0$. It has the value of the permutation strategy, and it commutes on the support of the question distribution, the permutation strategy commuting along edges (Definition [PCC strategy](../../foundations/part-01/def-pcc.md)). A permutation strategy for $G$, played at both tags, is one for its doubled game, of the same value. In particular a tailored game with a perfect ZPC strategy has a perfect ZPC strategy for its doubled game, and then synchronous value $1$ on the doubled game and quantum value $1$.

## Depends on

- [When a permutation strategy is perfect](lem-perm-strategy-perfect.md)
- [PCC strategy](../../foundations/part-01/def-pcc.md)
- [Synchronous value](../../foundations/part-01/def-sync-value.md)
- [Synchronous value lower-bounds the quantum value](../../foundations/part-01/lem-sync-le-valstar.md)

## Proof

By Lemma [When a permutation strategy is perfect](lem-perm-strategy-perfect.md) the measurements are projective and commute along edges; the operators on strings of the wrong length are $0$, and summing over the strings of length $\ell(x)$ is summing over $\mathbb{F}_2^{\ell(x)}$, so the measurement sums to ${I}$ and the two values are the same sum, the bipartite decider agreeing with the canonical one on the edges. Doubling a strategy keeps the observables, and the doubled distribution is that of $G$ on the pairs $((\mathsf{false}, x), (\mathsf{true}, y))$ and zero elsewhere. The synchronous value bounds the quantum value of the doubled game (Lemma [Synchronous value lower-bounds the quantum value](../../foundations/part-01/lem-sync-le-valstar.md)), which is that of $G$.

## Lean

Formalized as [`MIPRE.Tailored.PermStrategy.toSync`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.PermStrategy.toSync), [`MIPRE.Tailored.PermStrategy.isPCC_toSync`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.PermStrategy.isPCC_toSync), [`MIPRE.Tailored.PermStrategy.value_toSync`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.PermStrategy.value_toSync), [`MIPRE.Tailored.PermStrategy.double`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.PermStrategy.double), [`MIPRE.Tailored.PermStrategy.value_double`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.PermStrategy.value_double), [`MIPRE.Tailored.TailoredGame.HasPerfectZPC.doubled`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.TailoredGame.HasPerfectZPC.doubled), [`MIPRE.Tailored.TailoredGame.HasPerfectZPC.exists_pcc`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.TailoredGame.HasPerfectZPC.exists_pcc), [`MIPRE.Tailored.TailoredGame.HasPerfectZPC.syncValue_eq_one`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.TailoredGame.HasPerfectZPC.syncValue_eq_one), [`MIPRE.Tailored.TailoredGame.HasPerfectZPC.valStar_eq_one`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.TailoredGame.HasPerfectZPC.valStar_eq_one).

## Sources

- [MIP* = RE blueprint: content/09_tailored.tex, line 256](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/09_tailored.tex#L256)
