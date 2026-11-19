---
declaration: theorem
origin: cited
lean: MIPRE.Tailored.AnsRed.Typed.isPCC_arStrat, MIPRE.Tailored.AnsRed.Typed.value_arStrat, MIPRE.Tailored.AnsRed.Typed.arStrat_support, MIPRE.Tailored.AnsRed.Typed.isXBit_arStrat, MIPRE.Tailored.AnsRed.Typed.isZBit_arStrat, MIPRE.Tailored.AnsRed.Typed.hasPerfectZPC_ar
statement: formalized
proof: formalized
---

# ZPC completeness of the answer-reduced game

If the input's $n$-th game has a perfect Z-aligned permutation strategy, so does the answer-reduced game presented by the typed data on the typed game of an answer-reduced sampler, for a degree $d \geq 17$, an answer bound at least the types' lengths, and circuits under which the honest PCPs of accepted answers satisfy the checks.

## Depends on

- [The honest strategy of the answer-reduced game](def-ar-honest-strategy.md)
- [The checks hold of honest answers](lem-ar-honest-checks.md)
- [The answer bits of the honest answers](lem-ar-honest-bits.md)
- [Completeness of a presentation from a typed strategy](../part-04/lem-presentation-typed.md)

## Proof depends on

- [Reading the answer-reduced constraints](lem-ar-tailored-reading.md)

## Proof

The honest strategy is PCC because the oracularization is, its questions of positive weight having oracularized parts of positive weight. It is perfect because every outcome it produces at such a pair is accepted by the oracularized predicate, which Lemma [The checks hold of honest answers](lem-ar-honest-checks.md) turns into acceptance by the typed data. It charges only answers of the types' lengths, and its bit observables are those of the oracularized measurements along the honest answers, signed permutations diagonal at the readable bits by Lemma [The answer bits of the honest answers](lem-ar-honest-bits.md). Lemma [Completeness of a presentation from a typed strategy](../part-04/lem-presentation-typed.md) concludes.

## Lean

Formalized as [`MIPRE.Tailored.AnsRed.Typed.isPCC_arStrat`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.isPCC_arStrat), [`MIPRE.Tailored.AnsRed.Typed.value_arStrat`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.value_arStrat), [`MIPRE.Tailored.AnsRed.Typed.arStrat_support`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.arStrat_support), [`MIPRE.Tailored.AnsRed.Typed.isXBit_arStrat`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.isXBit_arStrat), [`MIPRE.Tailored.AnsRed.Typed.isZBit_arStrat`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.isZBit_arStrat), [`MIPRE.Tailored.AnsRed.Typed.hasPerfectZPC_ar`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.AnsRed.Typed.hasPerfectZPC_ar).

## Sources

- [MIP* = RE blueprint: content/09_tailored.tex, line 3087](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/09_tailored.tex#L3087)
