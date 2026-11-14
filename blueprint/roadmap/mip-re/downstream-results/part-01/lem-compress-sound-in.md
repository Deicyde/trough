---
declaration: lemma
origin: cited
lean: MIPRE.Pipeline.output_val_le
statement: formalized
proof: formalized
---

# The soundness chain of compression, in a value model

If the three stages are sound in the value model $\omega$ (Definition [The stages' soundness clauses in a value model](def-stage-sound-in.md)), then for every $\lambda$-bounded verifier $\mathsf{V}$ and every $n \geq C_0$, $\omega(\mathsf{V}_{2^n}) \leq \frac12$ implies $\omega(\mathsf{V}^{\textsc{Compr}}_n) \leq \frac12$, for the verifier $\mathsf{V}^{\textsc{Compr}}$ of Theorem [Gap-preserving compression from ambient stage contracts](../../structure-of-the-proof/part-09/thm-compression.md) at its answer bounds.

## Depends on

- [The stages' soundness clauses in a value model](def-stage-sound-in.md)
- [The margin claim](../../structure-of-the-proof/part-09/lem-compress-margin.md)
- [A universal repetition exponent](../../structure-of-the-proof/part-09/lem-compress-tau.md)

## Proof

The soundness chain of Theorem [Gap-preserving compression from ambient stage contracts](../../structure-of-the-proof/part-09/thm-compression.md) (Remark [How the value chain composes, and what it avoids](../../structure-of-the-proof/README.md)), read in $\omega$: the three clauses, used contrapositively, through the same margins (Lemmas [The margin claim](../../structure-of-the-proof/part-09/lem-compress-margin.md) and [A universal repetition exponent](../../structure-of-the-proof/part-09/lem-compress-tau.md)). Nothing else in the chain depends on the model: between the stages' answer bounds it passes by the value of a verifier whose decider rejects every answer beyond a bound, which is the same at every larger bound in every model. The soundness clause of Theorem [Gap-preserving compression from ambient stage contracts](../../structure-of-the-proof/part-09/thm-compression.md) is the case $\omega = \mathrm{val}^*$.

## Lean

Formalized as [`MIPRE.Pipeline.output_val_le`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Pipeline.output_val_le).

## Sources

- [MIP* = RE blueprint: content/08_downstream.tex, line 864](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/08_downstream.tex#L864)
