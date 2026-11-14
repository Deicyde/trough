---
navigation: transparent
---

# The polynomial measurements to The answer-length calculator

- [The polynomial measurements](def-ar-sound-extract.md)
- [The polynomial measurements](lem-ar-sound-extract.md)
- [The point relations](lem-ar-sound-relations.md)
- [The polynomials of the roles agree](lem-ar-sound-poly.md)
- [Shifting a polynomial along an axis](lem-ar-sound-shift.md)
- [Indifference, at two points of a line](lem-ar-sound-indifference.md)
- [The proof check, on the polynomials](lem-ar-sound-check.md)
- [The decoded strategy](def-ar-decoded-strategy.md)
- [The checks of the decoded strategy](lem-ar-decoded-accepts.md)
- [The failure of the decoded strategy](lem-ar-decoded-value.md)
- [Soundness of the answer-reduced game](thm-ar-sound.md)

## The output verifier's programs

The output tailored verifier of the answer reduction has the answer-reduced sampler and two programs which, at index $n$, output at every detyped question the lengths of the presented answer-reduced game and at every pair its constraints. Once they do, the output's $n$-th game extends the presented one, and both items of prop:completeness\_soundness\_combi\_ans\_red carry over to it (Theorem [Completeness and soundness of an output verifier meeting the presented game](thm-ar-meets.md)). The output's parameters at $n$ grow like a power of $(\lambda n + 1)^\mu$ and its programs read them in unary, which no polynomial-time function of the binary index can write: a closed program computes them and the programs run it as a stage (Definition [The parameter routine of the answer-reduced verifier](def-ar-routine.md)), as in the MIP\* answer reduction. Every check of the game is a list of field equations in the answer bits, whose constraints are computed from a program of the equations' values (Lemma [Field equations as constraints, and field arithmetic, as programs](../part-08/lem-ar-field-cons.md)). The output verifier meets the presented game (Theorem [Completeness and soundness of the output verifier](../part-08/thm-ar-output.md)), and its programs run within the contract's output budget as soon as the routine's parameter program runs in polynomial time (Theorem [The complexity clause of the answer reduction](../part-08/thm-ar-output-within.md)).

- [A tailored verifier meeting a tailored game](def-tailored-meets.md)
- [A tailored verifier meeting a game extends it](lem-tailored-meets.md)
- [The presented answer-reduced game, and meeting it](def-ar-meets.md)
- [Completeness and soundness of an output verifier meeting the presented game](thm-ar-meets.md)
- [The low-degree half of the answer-reduced sampler, directly answered](lem-ar-ld-direct.md)
- [The answer-reduced sampler](def-ar-sampler.md)
- [The distribution of the answer-reduced sampler](lem-ar-sampler-dist.md)
- [The parameter routine of the answer-reduced verifier](def-ar-routine.md)
- [The answer-length calculator](lem-ar-len.md)
