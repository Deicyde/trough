---
declaration: lemma
origin: cited
lean: MIPRE.Tailored.TailoredVerifier.ofTNFV_accepts_iff, MIPRE.Tailored.TailoredVerifier.ofTNFV_game_D, MIPRE.Tailored.TailoredVerifier.valStar_ofTNFV, MIPRE.Tailored.TailoredVerifier.hasPerfectPCC_ofTNFV
statement: formalized
proof: formalized
---

# A tailored verifier and its normal form verifier have the same games

At the questions of the $n$-th game, the normal form verifier of $\mathsf{V}$ accepts exactly what $\mathsf{V}_n$ accepts. Let $T$ be at least the answer lengths of $\mathsf{V}_n$. Then its game $\mathsf{V}_{n,T}$ has the quantum value of $\mathsf{V}_n$, and if $\mathsf{V}$ has a perfect ZPC strategy at $n$, the doubled game of $\mathsf{V}_{n,T}$ has a PCC strategy of value $1$ (Definition [PCC strategy](../../foundations/part-01/def-pcc.md)).

## Depends on

- [A tailored verifier as a normal form verifier; II:1757–1787](def-of-tnfv.md)
- [The canonical decider decides the $n$-th game](lem-canonical-decider.md)
- [ZPC strategies are PCC strategies](lem-zpc-pcc.md)
- [Value models](../../downstream-results/part-01/def-value-model.md)

## Proof

The question-length check passes at the questions of index $n$, so acceptance is the canonical decider's, which is that of $\mathsf{V}_n$ by Lemma [The canonical decider decides the $n$-th game](lem-canonical-decider.md). The two games have the same distribution and accept the same answer pairs, and every answer pair that $\mathsf{V}_{n,T}$ accepts has the lengths of $\mathsf{V}_n$, so is one of the answer pairs of the game of $\mathsf{V}_n$: enlarging the answer sets by rejected answers changes no value. A perfect ZPC strategy for the doubled game of $\mathsf{V}_n$ is a perfect PCC strategy for the doubled bipartite game (Lemma [ZPC strategies are PCC strategies](lem-zpc-pcc.md)), which, extended by zero to the answers of length at most $T$, is one for the doubled game of $\mathsf{V}_{n,T}$.

## Lean

Formalized as [`MIPRE.Tailored.TailoredVerifier.ofTNFV_accepts_iff`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.TailoredVerifier.ofTNFV_accepts_iff), [`MIPRE.Tailored.TailoredVerifier.ofTNFV_game_D`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.TailoredVerifier.ofTNFV_game_D), [`MIPRE.Tailored.TailoredVerifier.valStar_ofTNFV`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.TailoredVerifier.valStar_ofTNFV), [`MIPRE.Tailored.TailoredVerifier.hasPerfectPCC_ofTNFV`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.TailoredVerifier.hasPerfectPCC_ofTNFV).

## Sources

- [MIP* = RE blueprint: content/09_tailored.tex, line 418](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/09_tailored.tex#L418)
