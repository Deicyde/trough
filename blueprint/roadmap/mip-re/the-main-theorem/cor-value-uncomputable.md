---
declaration: corollary
origin: cited
lean: MIPRE.Halting.gameValue_uncomputable, MIPRE.Halting.quantumValue_uncomputable
statement: formalized
proof: formalized
---

# Uncomputability of the game value

There is no algorithm that, given a game description $g$ with the promise that ${\mathrm{val}^{s}}(\mathfrak{G}_g) = 1$ or ${\mathrm{val}^{s}}(\mathfrak{G}_g) \leq \frac12$, decides which is the case; the same holds with $\mathrm{val}^*$ in place of ${\mathrm{val}^{s}}$ (Corollary [Halting reduces to the quantum value](cor-main-quantum.md)).

## Depends on

- [Turing](../background-results/part-03/thm-halting-undecidable.md)

## Proof depends on

- [Compression, and $\mathrm{MIP}^* = \mathrm{RE}$, from answer reduction alone](../structure-of-the-proof/part-09/cor-compression-from-answer-reduction.md)
- [Answer reduction](../structure-of-the-proof/part-09/thm-answer-reduction.md)

## Proof

A computable $f$ answering *true* on every description of value $1$ and *false* on every description of value at most $\frac12$, composed with the map of Theorem [Halting reduces to the game value; Theorem 12.2 of (JNVWY20), synchronous form](thm-main.md) (respectively Corollary [Halting reduces to the quantum value](cor-main-quantum.md)), would decide whether a machine halts on the empty input, against Theorem [Turing](../background-results/part-03/thm-halting-undecidable.md). In Lean the algorithm is a Mathlib-computable Boolean function (`Halting/Corollaries.lean`), at the compression of Theorem [Ambient compression inhabitation target](../structure-of-the-proof/part-09/thm-compression-target.md).

## Lean

Formalized as [`MIPRE.Halting.gameValue_uncomputable`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Halting.gameValue_uncomputable), [`MIPRE.Halting.quantumValue_uncomputable`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Halting.quantumValue_uncomputable).

## Sources

- [MIP* = RE blueprint: content/07_main_theorem.tex, line 136](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/07_main_theorem.tex#L136)
