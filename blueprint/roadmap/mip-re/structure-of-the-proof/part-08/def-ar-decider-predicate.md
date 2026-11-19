---
declaration: definition
origin: cited
lean: MIPRE.AnswerReduction.Ans, MIPRE.AnswerReduction.ansFmt, MIPRE.AnswerReduction.side, MIPRE.AnswerReduction.accepts
statement: formalized
---

# The answer-reduced decision predicate

A type of the answer-reduced verifier is a pair of an oracularization role and a PCP type. An answer is an answer of its copy's low-degree test, with one codeword for copies $1$ to $5$ and $m'+6$ codewords for copy $6$. The oracle answers of the input verifier are never sent. The predicate is the format preamble on both answers, then the five steps of the paper's decision procedure for both players:

1. equal types have equal answers;
2. the oracle's $\mathrm{Point}_6$ answer agrees with an isolated player $v$'s $\mathrm{Point}_v$ answer in component $v$;
3. an isolated player $v$'s input codeword passes the $m$-variable test on copy $v$;
4. between two oracles, copies $3$, $4$ and $5$ pass the consistency check against copy $6$ and the individual $m$-variable test, and copy $6$ passes the simultaneous test with $m'+6$ codewords;
5. on an oracle's $\mathrm{Point}_6$ question, the point and the answer form a PCP view that the PCP verifier accepts on the input question pair.

The PCP verifier's decision is a parameter of the predicate.

## Depends on

- [The PCP sampler of answer reduction](def-ar-pcp-sampler.md)
- [The oracularized game](../part-06/def-oracular-game.md)

## Lean

Formalized as [`MIPRE.AnswerReduction.Ans`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.AnswerReduction.Ans), [`MIPRE.AnswerReduction.ansFmt`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.AnswerReduction.ansFmt), [`MIPRE.AnswerReduction.side`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.AnswerReduction.side), [`MIPRE.AnswerReduction.accepts`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.AnswerReduction.accepts).

## Sources

- [MIP* = RE blueprint: content/06_proof_structure.tex, line 5451](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/06_proof_structure.tex#L5451)
