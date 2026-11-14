---
declaration: lemma
origin: cited
lean: MIPRE.CL.Detyping.decodeView_view, MIPRE.CL.Detyping.decodeQuestion_output, MIPRE.CL.Detyping.complete, MIPRE.CL.Detyping.complete_state, MIPRE.CL.Detyping.complete_player_independent, MIPRE.CL.Detyping.complete_isPCC, MIPRE.CL.Detyping.complete_value, MIPRE.CL.Detyping.exists_perfectPCC
statement: formalized
proof: formalized
---

# Finite-game detyping PCC completeness

For positive-level partitioned typed CL presentations and a symmetric nonempty graph, every perfect PCC witness for the doubled typed finite game gives a perfect PCC witness for the doubled detyped finite game. The construction keeps the local dimension and tracial state and uses one player-independent measurement rule. This is a construction inside the ambient PCC representation.

## Depends on

- [Finite-game detyping soundness](../part-02/lem-detype-game-soundness.md)
- [PCC strategy](../../foundations/part-01/def-pcc.md)
- [Synchronous value](../../foundations/part-01/def-sync-value.md)

## Proof

Decode the Alice-view pattern, then the disjoint Bob-view pattern, and use a fixed deterministic answer otherwise. On a common seed, either both decoded views identify an actual ordered edge or one side uses the deterministic measurement and the predicate accepts. On an edge the original measurements and predicate are recovered. Positive support transfers commutation and zero failure from the original perfect PCC witness.

## Lean

Formalized as [`MIPRE.CL.Detyping.decodeView_view`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.CL.Detyping.decodeView_view), [`MIPRE.CL.Detyping.decodeQuestion_output`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.CL.Detyping.decodeQuestion_output), [`MIPRE.CL.Detyping.complete`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.CL.Detyping.complete), [`MIPRE.CL.Detyping.complete_state`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.CL.Detyping.complete_state), [`MIPRE.CL.Detyping.complete_player_independent`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.CL.Detyping.complete_player_independent), [`MIPRE.CL.Detyping.complete_isPCC`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.CL.Detyping.complete_isPCC), [`MIPRE.CL.Detyping.complete_value`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.CL.Detyping.complete_value), [`MIPRE.CL.Detyping.exists_perfectPCC`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.CL.Detyping.exists_perfectPCC).

## Sources

- [MIP* = RE blueprint: content/06_proof_structure.tex, line 547](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/06_proof_structure.tex#L547)
