---
declaration: lemma
origin: cited
lean: MIPRE.AnswerReduction.arVerifier_sampler
statement: formalized
proof: formalized
---

# Answer-reduction sampler independence

The output sampler is determined by $(S,\lambda,\ell,\mu,\sigma)$, independent of the input decider's code. The typed oracle sampler uses only $S$; PCP parameters use only the supplied numerical bounds; downsizing uses their explicit field routine; and detyping's sampler uses only its sampler and fixed graph. This supplies the source premise used by compression's sampler-independence argument (ledger node $1.5.1$). The already checked conditional compression theorem keeps its existing Lean proof and premises.

## Depends on

- [Answer-reduction construction](../part-08/lem-ar-construction.md)

## Proof

The output sampler is the detyping compiler's sampler of the typed sampler, which is built from the input sampler and $(\lambda,\mu,\sigma)$ only; its program is a polynomial-time function of the input sampler's program and $(\lambda,\mu,\sigma)$.

## Lean

Formalized as [`MIPRE.AnswerReduction.arVerifier_sampler`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.AnswerReduction.arVerifier_sampler).

## Sources

- [MIP* = RE blueprint: content/06_proof_structure.tex, line 6010](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/06_proof_structure.tex#L6010)
