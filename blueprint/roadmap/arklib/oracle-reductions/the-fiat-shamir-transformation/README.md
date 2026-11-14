# The Fiat-Shamir Transformation

The Fiat–Shamir transformation turns a public-coin interactive reduction into a non-interactive one. The prover computes all of its messages at once, and both parties derive each verifier challenge by querying a challenge oracle on the input statement and the prover messages sent before that challenge. In the security analysis this oracle is a random oracle.

ArkLib formalizes the basic (or slow) variant, which hashes the whole statement and message prefix for each challenge. The same challenge oracle serves as the state-restoration oracle, so the definitions below carry both names. Salted variants are covered by placing the salts in the input statement.

## The Challenge Oracle

Let $\mathsf{pSpec}$ be a protocol specification and $\mathsf{StmtIn}$ the input statement type. Write $\mathsf{pSpec}.\mathsf{MessagesUpTo}\ k$ for the prover messages among the first $k$ rounds.

- [Challenge Oracle Interface](def-fiat-shamir-challenge-oracle-interface.md)
- [Challenge Oracle Specification](def-fiat-shamir-spec.md)

## Fiat-Shamir Transformation for Provers

The transformed prover runs the interactive prover, answering its own challenges with oracle queries. All definitions in this section and the next run in the oracle specification $\mathsf{oSpec} \mathrel{+} \mathsf{srChallengeOracle}\ \mathsf{StmtIn}\ \mathsf{pSpec}$.

- [Fiat-Shamir Round Processing](def-prover-process-round-fs.md)
- [Fiat-Shamir Prover Execution](def-prover-run-to-round-fs.md)
- [Fiat-Shamir Prover Transformation](def-prover-fiat-shamir.md)

## Transcript Derivation and Verifier Transformation

- [Fiat-Shamir Transcript Derivation](def-derive-transcript-fs.md)
- [Fiat-Shamir Verifier Transformation](def-verifier-fiat-shamir.md)

## Fiat-Shamir Transformation for Reductions

- [Fiat-Shamir Reduction Transformation](def-reduction-fiat-shamir.md)

## Security Properties

- [Fiat-Shamir Preserves Completeness](thm-fiat-shamir-completeness.md)

**Remark (Soundness and zero-knowledge).** The expected route to soundness of the transform is the following:

- state-restoration knowledge soundness of the interactive reduction implies knowledge soundness of its Fiat–Shamir transform in the random oracle model;
- honest-verifier zero-knowledge of the interactive reduction implies zero-knowledge of the transform.

State-restoration knowledge soundness itself is proved for fixed-round oracle protocols in the interaction layer, from round-by-round knowledge certificates, with error $(Q + k)\cdot\epsilon$ ([State-Restoration Knowledge Soundness](../definitions/part-03/thm-sr-knowledge-soundness.md)). The two transfers above are not formalized, and zero-knowledge is not defined ([Simulator](../definitions/part-03/def-simulator.md)). `docs/design/00-current-status.md` records the status of this work.

**Remark (Implementation considerations).** Practical Fiat–Shamir implementations absorb transcript elements into a cryptographic sponge incrementally and squeeze challenges from it. ArkLib formalizes only the basic variant above; it has no sponge-based variant.
