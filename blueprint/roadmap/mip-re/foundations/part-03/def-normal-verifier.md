---
declaration: definition
origin: cited
lean: MIPRE.Verifier, MIPRE.Verifier.game, MIPRE.Verifier.Answers, MIPRE.Verifier.size, MIPRE.Verifier.IsSynchronousAt, MIPRE.Verifier.syncGame
statement: formalized
---

# Normal form verifier in the ambient model

An ambient *normal form verifier* is a pair $\mathsf{V}=(\mathcal{S},\mathcal{D})$ of a sampler over $\mathbb{F}_2$ and a decider satisfying the extensional condition

$$
\mathcal{D}(n,x,y,a,b)\text{ accepts}\;\Rightarrow\;
\left\vert {x} \right\vert=\left\vert {y} \right\vert=s(n).
$$

This is `Verifier.accepts_length`; no particular sequence of preliminary checks is part of the structure. For each index $n$ and independently chosen answer cut $T\in\mathbb{N}$, the game $\mathsf{V}_{n,T}$ (`Verifier.game n T`) has question sets ${\mathcal{X}}={\mathcal{Y}}=\{0,1\}^{s(n)}$, answer sets consisting of the bit strings of length at most $T$, the sampler distribution at index $n$, and decision predicate equal to the decider's acceptance predicate. Its definition imposes no time-bound hypothesis. We write $\mathsf{V}_n$ when the answer cut is specified by the surrounding statement.

The condition `Verifier.IsSynchronousAt n` says that the decider rejects unequal answers to equal questions at index $n$. Under this condition, `Verifier.syncGame n T` is the same game as a synchronous game, so its synchronous value is defined (Remark [The synchronization invariant](../README.md)). The description length is $\left\vert {\mathsf{V}} \right\vert = \max\{\left\vert {\mathcal{S}} \right\vert, \left\vert {\mathcal{D}} \right\vert\}$, and the number of levels of $\mathsf{V}$ is that of $\mathcal{S}$.

## Depends on

- [Sampler](def-sampler.md)
- [Decider](def-decider.md)
- [Nonlocal game](../part-01/def-game.md)
- [Synchronous game](../part-01/def-sync-game.md)

## Lean

Formalized as [`MIPRE.Verifier`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Verifier), [`MIPRE.Verifier.game`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Verifier.game), [`MIPRE.Verifier.Answers`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Verifier.Answers), [`MIPRE.Verifier.size`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Verifier.size), [`MIPRE.Verifier.IsSynchronousAt`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Verifier.IsSynchronousAt), [`MIPRE.Verifier.syncGame`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Verifier.syncGame).

## Sources

- [MIP* = RE blueprint: content/02_foundations.tex, line 1476](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/02_foundations.tex#L1476)
