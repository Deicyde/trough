---
declaration: lemma
origin: cited
lean: MIPRE.CL.CLFun.eval_ident, MIPRE.CL.CLFun.exactlyOn_ident, MIPRE.exactlyOn_roleFamily, MIPRE.SeededGame.typedGame_mu, MIPRE.SeededGame.quantumValue_typedGame_le, MIPRE.SyncStrategy.pushTo, MIPRE.SyncStrategy.value_le_pushTo, MIPRE.SyncStrategy.isPCC_pushTo, MIPRE.Verifier.valStar_ge_of_typed, MIPRE.Verifier.exists_typed_perfectPCC, MIPRE.pairDec_pairEnc, MIPRE.parseAns_encAns, MIPRE.oaccepts_of_oraclePred, MIPRE.oraclePred_encAns, MIPRE.Verifier.valStar_ge_of_oraclePred, MIPRE.Verifier.exists_oraclePred_perfectPCC
statement: formalized
proof: formalized
---

# Value transfers of the typed oracularized game

In the setting of Definition [The typed oracularized game](def-oracular-typed-game.md):

1. (**Soundness**) for every $\varepsilon > 0$ and every answer cut $T$, if the quantum value of the typed oracularized game exceeds $1 - \varepsilon$, then $\mathrm{val}^*(\mathsf{V}_n) \geq 1 - 24\sqrt\varepsilon$ with answers of length at most $B$;
2. (**Completeness**) if $\mathsf{V}_n$ has a value-$1$ PCC strategy with answers of length at most $B$, then for every $T \geq 8B + 3$ the doubled typed oracularized game has a value-$1$ PCC synchronous strategy.

The same holds for any typed predicate whose acceptance implies the oracularized predicate after a reading of the answers, for soundness, and for any typed predicate that accepts an encoding of every answer pair the oracularized predicate accepts, for completeness.

## Depends on

- [The typed oracularized game](def-oracular-typed-game.md)
- [Completeness of oracularization, at the level of games](lem-oracular-completeness.md)
- [Soundness of oracularization, for bipartite strategies](lem-oracular-soundness-tensor.md)
- [PCC strategy](../../foundations/part-01/def-pcc.md)

## Proof depends on

- [Full-seed indexing for answer reduction](../part-08/def-ar-seed-index.md)

## Proof

The typed game samples a uniform ordered pair of types and one common uniform seed, and the identity gives the oracle the seed itself, so its question distribution is exactly that of the oracularization. For soundness, a tensor-product strategy of the typed game, played through the parse on the same state, is a strategy of the oracularization that loses nothing, because the typed predicate accepts only what the oracularized one accepts after parsing; then Lemma [Soundness of oracularization, for bipartite strategies](lem-oracular-soundness-tensor.md) applies. For completeness, the strategy of Lemma [Completeness of oracularization, at the level of games](lem-oracular-completeness.md), whose two players use identical operators, is doubled and its outcomes pushed forward along the honest encoding: the serialization for an oracle's pair, the string itself for an isolated player's answer. Summing a projective measurement over the fibres of a map keeps it projective and keeps commutation, and the pushed-forward strategy wins whenever the original does, because an accepted answer has the shape its type asks for and parses back from its encoding. The serialization of two strings of length at most $B$ has length at most $8B + 3$. In the ambient model the input witness already answers with strings of length at most $B$; in the source model that is what the truncation of Lemma [Timeout-compatible oracle PCC completeness](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/06_proof_structure.tex#L5391) provides.

## Lean

Formalized as [`MIPRE.CL.CLFun.eval_ident`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.CL.CLFun.eval_ident), [`MIPRE.CL.CLFun.exactlyOn_ident`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.CL.CLFun.exactlyOn_ident), [`MIPRE.exactlyOn_roleFamily`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.exactlyOn_roleFamily), [`MIPRE.SeededGame.typedGame_mu`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.SeededGame.typedGame_mu), [`MIPRE.SeededGame.quantumValue_typedGame_le`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.SeededGame.quantumValue_typedGame_le), [`MIPRE.SyncStrategy.pushTo`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.SyncStrategy.pushTo), [`MIPRE.SyncStrategy.value_le_pushTo`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.SyncStrategy.value_le_pushTo), [`MIPRE.SyncStrategy.isPCC_pushTo`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.SyncStrategy.isPCC_pushTo), [`MIPRE.Verifier.valStar_ge_of_typed`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Verifier.valStar_ge_of_typed), [`MIPRE.Verifier.exists_typed_perfectPCC`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Verifier.exists_typed_perfectPCC), [`MIPRE.pairDec_pairEnc`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.pairDec_pairEnc), [`MIPRE.parseAns_encAns`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.parseAns_encAns), [`MIPRE.oaccepts_of_oraclePred`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.oaccepts_of_oraclePred), [`MIPRE.oraclePred_encAns`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.oraclePred_encAns), [`MIPRE.Verifier.valStar_ge_of_oraclePred`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Verifier.valStar_ge_of_oraclePred), [`MIPRE.Verifier.exists_oraclePred_perfectPCC`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Verifier.exists_oraclePred_perfectPCC).

## Sources

- [MIP* = RE blueprint: content/06_proof_structure.tex, line 4377](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/06_proof_structure.tex#L4377)
