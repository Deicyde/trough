---
declaration: definition
origin: cited
lean: MIPRE.Tailored.TailoredVerifier.ofTNFV
statement: formalized
---

# A tailored verifier as a normal form verifier; II:1757–1787

A tailored verifier $\mathsf{V}$ is the normal form verifier (Definition [Normal form verifier in the ambient model](../../foundations/part-03/def-normal-verifier.md)) with the sampler of $\mathsf{V}$ and the decider that checks that both questions have the length the sampler gives them and then runs the canonical decider of $\mathsf{V}$ through the universal machine (`Verifier.ofSamplerDecider`, Remark [Relation to the abstract compression lemma](../../structure-of-the-proof/README.md)).

## Depends on

- [The canonical decider, as a program; II:1757–1787](def-canonical-decider.md)
- [Normal form verifier in the ambient model](../../foundations/part-03/def-normal-verifier.md)

## Lean

Formalized as [`MIPRE.Tailored.TailoredVerifier.ofTNFV`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.TailoredVerifier.ofTNFV).

## Sources

- [MIP* = RE blueprint: content/09_tailored.tex, line 407](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/09_tailored.tex#L407)
