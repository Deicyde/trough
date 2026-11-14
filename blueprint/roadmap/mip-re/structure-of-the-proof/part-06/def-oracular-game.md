---
declaration: definition
origin: cited
lean: MIPRE.Role, MIPRE.SeededGame, MIPRE.SeededGame.toGame, MIPRE.OAns, MIPRE.SeededGame.oquestion, MIPRE.SeededGame.shapeOk, MIPRE.SeededGame.gameCheck, MIPRE.SeededGame.oracleVsPlayer, MIPRE.SeededGame.oaccepts, MIPRE.SeededGame.oDist, MIPRE.SeededGame.oracular
statement: formalized
---

# The oracularized game

A *seeded game* is a finite seed space $V$, two question maps $L^\textsc{A}, L^\textsc{B} : V \to V$ and a decision predicate $D$; the game it presents is the law of $(L^\textsc{A}(z), L^\textsc{B}(z))$ for a uniform seed $z$, with predicate $D$. Its *oracularization* is the synchronous game on questions ${\mathcal{T}}^\textsc{Orac} \times V$, ${\mathcal{T}}^\textsc{Orac} = \{\textsc{O}, \textsc{A}, \textsc{B}\}$, and answers either a pair (from an oracle) or a single answer (from an isolated player), in which the verifier draws the ordered pair of roles and the seed uniformly, gives an oracle the seed $z$ itself and an isolated player of role $v$ the question $L^v(z)$, and accepts when: each answer's shape matches its player's role; each oracle's pair of answers is accepted by $D$ at the pair of questions its seed determines; equal roles carry equal answers; and each oracle's component for the other player's role agrees with that player's answer.

## Depends on

- [Nonlocal game](../../foundations/part-01/def-game.md)
- [Synchronous game](../../foundations/part-01/def-sync-game.md)

## Lean

Formalized as [`MIPRE.Role`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Role), [`MIPRE.SeededGame`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.SeededGame), [`MIPRE.SeededGame.toGame`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.SeededGame.toGame), [`MIPRE.OAns`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.OAns), [`MIPRE.SeededGame.oquestion`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.SeededGame.oquestion), [`MIPRE.SeededGame.shapeOk`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.SeededGame.shapeOk), [`MIPRE.SeededGame.gameCheck`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.SeededGame.gameCheck), [`MIPRE.SeededGame.oracleVsPlayer`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.SeededGame.oracleVsPlayer), [`MIPRE.SeededGame.oaccepts`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.SeededGame.oaccepts), [`MIPRE.SeededGame.oDist`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.SeededGame.oDist), [`MIPRE.SeededGame.oracular`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.SeededGame.oracular).

## Sources

- [MIP* = RE blueprint: content/06_proof_structure.tex, line 4172](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/06_proof_structure.tex#L4172)
