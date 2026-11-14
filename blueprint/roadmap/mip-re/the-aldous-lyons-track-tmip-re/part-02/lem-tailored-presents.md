---
declaration: lemma
origin: cited
lean: MIPRE.Tailored.Presents.quantumValue_eq, MIPRE.Tailored.Presents.hasPerfectZPC, MIPRE.Tailored.Presents.accepts_iff, MIPRE.Tailored.Presents.value_padStrategy, MIPRE.quantumValue_congr_support, MIPRE.quantumValue_eq_of_equiv_support, MIPRE.Tailored.TailoredGame.quantumValue_doubled_eq_valStar, MIPRE.Tailored.TailoredGame.doubled_μ_self, MIPRE.Tailored.fourierProj_castLE, MIPRE.Tailored.fourierProj_eq_zero_of_one
statement: formalized
proof: formalized
---

# A presentation of a game without weight on its loops

Let a tailored game description present a tailored game with no weight on its loops, such as a doubled game. Then the description has the game's quantum value, and a perfect ZPC strategy of the game, its observables padded with identities beyond a question's variables, is one of the description. A tailored game and its doubled game have the same quantum value.

## Depends on

- [Presentations](def-tailored-presents.md)
- [Tailored game descriptions as games of the foundations](lem-tailored-bridge.md)
- [The Fourier transform; II:974–1006](../part-01/lem-fourier-pvm.md)

## Proof depends on

- [Projective strategies in the two models](../../downstream-results/part-03/lem-model-proj-strategy-values.md)
- [Post-processing and detyping, in a model](../../downstream-results/part-02/lem-transports-model.md)

## Proof

The two read answers differently: the description reads bit vectors of the largest length that vanish beyond a vertex's variables, the game bit strings of exactly that length; and the description also rejects unequal answers at a loop. On well-formatted answers the two predicates agree up to the loop condition, and the quantum value sees a predicate only where the distribution has weight. Answers pass from vectors to strings by keeping a vertex's coordinates and back by padding with zeros, question by question, and decoding answers question by question can only raise a value; so the two values bound each other. For the strategies: an observable equal to the identity leaves the Fourier transform unchanged at an answer whose bit there is $0$ and annihilates it at the others, so the padded strategy's measurements are the strategy's on padded answers and vanish elsewhere, and it has the strategy's value.

## Lean

Formalized as [`MIPRE.Tailored.Presents.quantumValue_eq`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Presents.quantumValue_eq), [`MIPRE.Tailored.Presents.hasPerfectZPC`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Presents.hasPerfectZPC), [`MIPRE.Tailored.Presents.accepts_iff`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Presents.accepts_iff), [`MIPRE.Tailored.Presents.value_padStrategy`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Presents.value_padStrategy), [`MIPRE.quantumValue_congr_support`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.quantumValue_congr_support), [`MIPRE.quantumValue_eq_of_equiv_support`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.quantumValue_eq_of_equiv_support), [`MIPRE.Tailored.TailoredGame.quantumValue_doubled_eq_valStar`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.TailoredGame.quantumValue_doubled_eq_valStar), [`MIPRE.Tailored.TailoredGame.doubled_μ_self`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.TailoredGame.doubled_μ_self), [`MIPRE.Tailored.fourierProj_castLE`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.fourierProj_castLE), [`MIPRE.Tailored.fourierProj_eq_zero_of_one`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.fourierProj_eq_zero_of_one).

## Sources

- [MIP* = RE blueprint: content/09_tailored.tex, line 769](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/09_tailored.tex#L769)
