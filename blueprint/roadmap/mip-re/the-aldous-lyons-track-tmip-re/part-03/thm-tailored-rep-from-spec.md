---
declaration: theorem
origin: cited
lean: MIPRE.Tailored.TailoredVerifier.RepSpec.accepts_iff, MIPRE.Tailored.TailoredVerifier.RepSpec.accepts_of_accepts, MIPRE.Tailored.TailoredVerifier.RepSpec.hasPerfectZPC, MIPRE.Tailored.TailoredVerifier.RepSpec.valStar_le_repeat, MIPRE.Tailored.TailoredVerifier.RepSpec.valStar_le, MIPRE.quantumValue_le_of_coarse, MIPRE.Tailored.PermStrategy.exists_accepts
statement: formalized
proof: formalized
---

# Completeness and soundness of repeated tailored verifiers

Let the programs of the repeated verifier meet the specification at $n$. If $\mathsf{V}_n$ has a perfect ZPC strategy, so does the repeated verifier's $n$-th game. If the lengths of $\mathsf{V}$ at $n$ are at most $B$ and $\mathrm{val}^*(\mathsf{V}_n) \leq 1 - \varepsilon$, then

$$
\mathrm{val}^*\bigl(\mathsf{V}^{\mathrm{rep}}_n\bigr) \;\leq\; \exp\Bigl( - \frac{c\, \varepsilon^{13}\,
k(n)}{2(B + 1)} \Bigr)\;,
$$

with $c$ the constant of Lemma [The repetition bound for answers of bounded length](../../parallel-repetition/lem-repetition-sound-bound.md).

## Depends on

- [Repeated tailored verifiers and the specification of their programs](def-tailored-rep-spec.md)
- [Tensor powers of permutation strategies; II:3043](lem-tensor-power-zpc.md)
- [The canonical decider of the product](lem-tailored-product-accepts.md)
- [The repetition bound for answers of bounded length](../../parallel-repetition/lem-repetition-sound-bound.md)
- [Parallel repetition of normal form verifiers](../../structure-of-the-proof/part-09/thm-parallel-repetition.md)

## Proof

At good questions the repeated verifier's game has the lengths and the constraints of the product, up to the blocks of the questions; at any other question it accepts nothing, and neither does the product, a coordinate of whose constraint lists then rejects. For completeness, the doubled product has a perfect ZPC strategy (Lemma [Tensor powers of permutation strategies; II:3043](lem-tensor-power-zpc.md)); a perfect strategy is accepted somewhere on every edge, so the questions on an edge are good, and the strategy pulled back along the blocks of the questions, with identity observables at the questions that carry no edge, is perfect for the repeated verifier. For soundness, the repeated verifier's game accepts, read through the coordinates of its answers, only what the direct repetition of $\mathsf{V}_n$'s bipartite game accepts, so its value is at most that game's: a strategy merged at each question along the map from answers to their coordinates is a strategy of the repetition of at least the same value. The answers of $\mathsf{V}_n$ have length at most $2B$, and Lemma [The repetition bound for answers of bounded length](../../parallel-repetition/lem-repetition-sound-bound.md) at length $2B$ gives the bound, the factor $2$ absorbed into the constant.

## Lean

Formalized as [`MIPRE.Tailored.TailoredVerifier.RepSpec.accepts_iff`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.TailoredVerifier.RepSpec.accepts_iff), [`MIPRE.Tailored.TailoredVerifier.RepSpec.accepts_of_accepts`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.TailoredVerifier.RepSpec.accepts_of_accepts), [`MIPRE.Tailored.TailoredVerifier.RepSpec.hasPerfectZPC`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.TailoredVerifier.RepSpec.hasPerfectZPC), [`MIPRE.Tailored.TailoredVerifier.RepSpec.valStar_le_repeat`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.TailoredVerifier.RepSpec.valStar_le_repeat), [`MIPRE.Tailored.TailoredVerifier.RepSpec.valStar_le`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.TailoredVerifier.RepSpec.valStar_le), [`MIPRE.quantumValue_le_of_coarse`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.quantumValue_le_of_coarse), [`MIPRE.Tailored.PermStrategy.exists_accepts`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.PermStrategy.exists_accepts).

## Sources

- [MIP* = RE blueprint: content/09_tailored.tex, line 1213](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/09_tailored.tex#L1213)
