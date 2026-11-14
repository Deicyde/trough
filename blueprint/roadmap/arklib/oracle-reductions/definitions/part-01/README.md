---
navigation: transparent
---

# Oracle Interface to Straightline Extractor

- [Oracle Interface](def-oracle-interface.md)

See `OracleInterface.lean` for common instances of $\mathsf{OracleInterface}$.

- [Protocol Specification](def-protocol-spec.md)

We define some supporting definitions for a protocol specification.

- [Protocol Specification Components](def-protocol-spec-components.md)
- [Protocol Transcript](def-transcript.md)

**Remark (Design Decision).** We do not enforce a particular interaction flow in the definition of an interactive (oracle) reduction. This is done so that we can capture all protocols in the most generality. Also, we want to allow the prover to send multiple messages in a row, since each message may have a different oracle representation (for instance, in the Plonk protocol, the prover's first message is a 3-tuple of polynomial commitments.)

- [Type Signature of a Prover](def-prover.md)
- [Type Signature of an Oracle Prover](def-oracle-prover.md)

After the interaction phase, the verifier may then run some verification procedure to check the validity of the prover's responses. In this procedure, the verifier gets access to the public part of the context, and oracle access to either the shared oracle, or the oracle inputs.

- [Type Signature of a Verifier](def-verifier.md)
- [Type Signature of an Oracle Verifier](def-oracle-verifier.md)
- [Oracle Verifier to Verifier Conversion](def-oracle-verifier-to-verifier.md)

An oracle reduction then consists of a type signature for the interaction, and a pair of prover and verifier for that type signature.

- [Interactive Reduction](def-reduction.md)
- [Interactive Oracle Reduction](def-oracle-reduction.md)

## Execution Semantics

We now define what it means to execute an oracle reduction. This is essentially achieved by first executing the prover, interspersed with oracle queries to get the verifier's challenges (these will be given uniform random probability semantics later on), and then executing the verifier's checks. Any message exchanged in the protocol will be added to the context. We may also log information about the execution, such as the log of oracle queries for the shared oracles, for analysis purposes (i.e. feeding information into the extractor).

- [Prover Execution to Round](def-prover-run-to-round.md)
- [Complete Prover Execution](def-prover-run.md)
- [Verifier Execution](def-verifier-run.md)
- [Oracle Verifier Execution](def-oracle-verifier-run.md)
- [Interactive Reduction Execution](def-reduction-run.md)
- [Oracle Reduction Execution](def-oracle-reduction-run.md)

## Security Properties

We can now define properties of interactive reductions. The two main properties we consider in this project are completeness and various notions of soundness. Zero-knowledge is not yet formalized.

First, for completeness, this is essentially probabilistic Hoare-style conditions on the execution of the oracle reduction (with the honest prover and verifier). In other words, given a predicate on the initial context, and a predicate on the final context, we require that if the initial predicate holds, then the final predicate holds with high probability (except for some *completeness* error).

- [Completeness](def-completeness.md)
- [Perfect Completeness](def-perfect-completeness.md)

Almost all oracle reductions we consider actually satisfy *perfect completeness*, which simplifies the proof obligation. In particular, this means we only need to show that no matter what challenges are chosen, the verifier will always accept given messages from the honest prover.

### Extractors

For knowledge soundness, we need to consider different types of extractors that can recover witnesses from malicious provers.

- [Straightline Extractor](def-straightline-extractor.md)
