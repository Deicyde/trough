---
declaration: definition
origin: cited
lean: MIPRE.CL.CLFun.ident, MIPRE.roleFamily, MIPRE.roleGraph, MIPRE.SeededGame.ofCL, MIPRE.Verifier.seeded, MIPRE.pairEnc, MIPRE.pairDec, MIPRE.parseAns, MIPRE.oraclePred, MIPRE.encAns, MIPRE.Verifier.oracleTypedPred
statement: formalized
---

# The typed oracularized game

Let $\mathsf{V}$ be a normal form verifier with at least one level, $n$ an index, $B$ a parse cut and $T$ an answer cut, and let $L^\textsc{A}, L^\textsc{B}$ be the CL functions of its sampler at $n$. The *typed oracularized game* of $\mathsf{V}_n$ is the finite typed game, in the sense of Definition [Typed sampler and its distribution](../part-01/def-typed-sampler-interface.md), on the complete type graph with loops over ${\mathcal{T}}^\textsc{Orac} = \{\textsc{O}, \textsc{A}, \textsc{B}\}$. Its CL functions are the identity for the type $\textsc{O}$, as a CL function with the levels of $\mathsf{V}$, and $L^\textsc{A}$, $L^\textsc{B}$ for the types $\textsc{A}$, $\textsc{B}$, the same for both players; its answers are the bit strings of length at most $T$. Its predicate parses each answer by the type of the player who gave it: an oracle's must be the serialization of a pair of strings of length at most $B$, an isolated player's a single string of length at most $B$. It rejects when a parse fails, and otherwise decides as the oracularization (Definition [The oracularized game](def-oracular-game.md)) of the seeded game $(L^\textsc{A}, L^\textsc{B}, D)$, where $D$ is the predicate of $\mathsf{V}_n$ on answers of length at most $B$.

## Depends on

- [The oracularized game](def-oracular-game.md)
- [Normal form verifier in the ambient model](../../foundations/part-03/def-normal-verifier.md)

## Lean

Formalized as [`MIPRE.CL.CLFun.ident`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.CL.CLFun.ident), [`MIPRE.roleFamily`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.roleFamily), [`MIPRE.roleGraph`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.roleGraph), [`MIPRE.SeededGame.ofCL`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.SeededGame.ofCL), [`MIPRE.Verifier.seeded`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Verifier.seeded), [`MIPRE.pairEnc`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.pairEnc), [`MIPRE.pairDec`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.pairDec), [`MIPRE.parseAns`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.parseAns), [`MIPRE.oraclePred`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.oraclePred), [`MIPRE.encAns`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.encAns), [`MIPRE.Verifier.oracleTypedPred`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Verifier.oracleTypedPred).

## Sources

- [MIP* = RE blueprint: content/06_proof_structure.tex, line 4356](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/06_proof_structure.tex#L4356)
