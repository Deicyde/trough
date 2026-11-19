---
declaration: lemma
origin: cited
lean: MIPRE.Tailored.vecOf, MIPRE.Tailored.ofFn_vecOf, MIPRE.Tailored.presented, MIPRE.Tailored.okD, MIPRE.Tailored.encV, MIPRE.Tailored.length_encD_of_okD, MIPRE.Tailored.valStar_presented_le, MIPRE.Tailored.hasPerfectZPC_presented
statement: formalized
proof: formalized
---

# Presenting a detyped game by a detyped tailored game

Let $\mathfrak{G}'$ be a game on detyped questions whose predicate calls a typed predicate $D$ on the views of the edges and accepts off them, and let $\mathfrak{G}$ be the detyping of typed tailored data, on the question distribution of $\mathfrak{G}'$. If, on every edge, a pair the typed data accepts decodes to one $D$ accepts, then $\mathrm{val}^*(\mathfrak{G}) \le \mathrm{val}^*(\mathfrak{G}')$. If, on every edge, a pair of encodable answers that $D$ accepts encodes, with the typed lengths, to one the typed data accepts, then every perfect PCC strategy of the doubled $\mathfrak{G}'$ that charges only encodable answers, and whose bit observables along the encoding are signed permutations diagonal at the readable bits, gives a perfect Z-aligned permutation strategy of the doubled $\mathfrak{G}$ commuting along edges.

## Depends on

- [Presenting a game as a tailored game](../part-03/lem-presentation-transport.md)
- [Detyping tailored games](../part-03/lem-tailored-detyping.md)

## Proof

Lemma [Presenting a game as a tailored game](../part-03/lem-presentation-transport.md), its acceptance obligations reduced to the edges by Lemma [Detyping tailored games](../part-03/lem-tailored-detyping.md); the encoded lists have the question's length, so they are the vectors the permutation strategy reads.

## Lean

Formalized as [`MIPRE.Tailored.vecOf`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.vecOf), [`MIPRE.Tailored.ofFn_vecOf`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.ofFn_vecOf), [`MIPRE.Tailored.presented`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.presented), [`MIPRE.Tailored.okD`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.okD), [`MIPRE.Tailored.encV`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.encV), [`MIPRE.Tailored.length_encD_of_okD`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.length_encD_of_okD), [`MIPRE.Tailored.valStar_presented_le`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.valStar_presented_le), [`MIPRE.Tailored.hasPerfectZPC_presented`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.hasPerfectZPC_presented).

## Sources

- [MIP* = RE blueprint: content/09_tailored.tex, line 1615](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/09_tailored.tex#L1615)
