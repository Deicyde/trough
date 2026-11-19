# Definitions

In this section, we give the basic definitions of a public-coin interactive oracle reduction (henceforth called an oracle reduction or IOR). We will define its building blocks, and various security properties.

## Format

An **(interactive) oracle reduction (IOR)** is an interactive protocol between two parties, a *prover* $\mathcal{P}$ and a *verifier* $\mathcal{V}$. In ArkLib, IORs are defined in the following setting:

1. We work in an ambient dependent type theory (in our case, Lean).

2. The protocol flow is fixed and defined by a given *type signature*, which describes in each round which party sends a message to the other, and the type of that message.

3. The prover and verifier has access to some inputs (called the *(oracle) context*) at the beginning of the protocol. These inputs are classified as follows:

    - *Public inputs* (or *statement*) $\mathbb{x}$: available to both parties;
    - *Private inputs* (or *witness*) $\mathbb{w}$: available only to the prover;
    - *Oracle inputs* (or *oracle statement*) $\mathbb{ox}$: the underlying data is available to the prover, but it's only exposed as an oracle to the verifier. See [Oracle Interface](part-01/def-oracle-interface.md) for more information.
    - *Shared oracle* $\mathcal{O}$: the oracle is available to both parties via an interface; in most cases, it is either empty, a probabilistic sampling oracle, a random oracle, or a group oracle (for the Algebraic Group Model). See [The VCVio Library](../../supporting-theories/the-vcvio-library/README.md) for more information on oracle computations.

4. The messages sent from the prover may either: 1) be seen directly by the verifier, or 2) only available to a verifier through an *oracle interface* (which specifies the type for the query and response, and the oracle's behavior given the underlying message).

    Currently, in the oracle reduction setting, we *only* allow messages sent to be available through oracle interfaces. In the (non-oracle) reduction setting, all messages are available directly. Future extensions may allow for mixed visibility for prover's messages.

5. $\mathcal{V}$ is assumed to be *public-coin*, meaning that its challenges are chosen uniformly at random from the finite type corresponding to that round, and it uses no randomness otherwise, except from those coming from the shared oracle.

6. At the end of the protocol, the prover and verifier outputs a new (oracle) context, which consists of:

    - The verifier takes in the input statement and the challenges, performs an *oracle* computation on the input oracle statements and the oracle messages, and outputs a new output statement.

        The verifier also outputs the new oracle statements, in one of two representations. Either each output oracle is an embedded copy of an input oracle statement or an oracle message, or the output family is *virtual*: each query to it is answered by queries to the input oracle statements and oracle messages, and this answer is certified against an explicit map that materializes the output data. The virtual form covers derived outputs such as a linear combination of input polynomials.

    - The prover takes in some final private state (maintained during protocol execution), and outputs a new output statement, new output oracle statement, and new output witness.

**Remark (Literature Comparison).** In the literature, our definition corresponds to the notion of *functional* IORs. Historically, (vector) IOPs were the first notion to be introduced by (Ben-Sasson et al. 2016); these are IORs where the output statement is true/false, all oracle statements and messages are vectors over some alphabet $\Sigma$, and the oracle interfaces are for querying specific positions in the vector. More recent works have considered other oracle interfaces, e.g., polynomial oracles (Chiesa et al. 2020, Bünz et al. 2020), generalized proofs to reductions (Kothapalli and Parno 2023, Bünz et al. 2025, Bünz et al. 2024, Baweja et al. 2025), and considered general oracle interfaces (Arnon et al. 2025). Most of the IOP theory has been distilled in the textbook ([Chiesa and Yogev 2024](https://github.com/hash-based-snargs-book)).

We have not seen any work that considers our most general setting, of IORs with arbitrary oracle interfaces.

We now go into more details on these objects, and how they are represented in Lean. Our description will aim to be as close as possible to the Lean code, and hence may differ somewhat from “mainstream” mathematical & cryptographic notation.

## [Oracle Interface to Straightline Extractor](part-01/README.md)

- [Oracle Interface](part-01/def-oracle-interface.md)
- [Protocol Specification](part-01/def-protocol-spec.md)
- [Protocol Specification Components](part-01/def-protocol-spec-components.md)
- [Protocol Transcript](part-01/def-transcript.md)
- [Type Signature of a Prover](part-01/def-prover.md)
- [Type Signature of an Oracle Prover](part-01/def-oracle-prover.md)
- [Type Signature of a Verifier](part-01/def-verifier.md)
- [Type Signature of an Oracle Verifier](part-01/def-oracle-verifier.md)
- [Oracle Verifier to Verifier Conversion](part-01/def-oracle-verifier-to-verifier.md)
- [Interactive Reduction](part-01/def-reduction.md)
- [Interactive Oracle Reduction](part-01/def-oracle-reduction.md)
- [Prover Execution to Round](part-01/def-prover-run-to-round.md)
- [Complete Prover Execution](part-01/def-prover-run.md)
- [Verifier Execution](part-01/def-verifier-run.md)
- [Oracle Verifier Execution](part-01/def-oracle-verifier-run.md)
- [Interactive Reduction Execution](part-01/def-reduction-run.md)
- [Oracle Reduction Execution](part-01/def-oracle-reduction-run.md)
- [Completeness](part-01/def-completeness.md)
- [Perfect Completeness](part-01/def-perfect-completeness.md)
- [Straightline Extractor](part-01/def-straightline-extractor.md)

## [Monotone Straightline Extractor to RBR Knowledge Soundness Implies…](part-02/README.md)

- [Monotone Straightline Extractor](part-02/def-monotone-straightline-extractor.md)
- [Round-by-Round Extractor](part-02/def-rbr-extractor.md)
- [Rewinding Extractor](part-02/def-rewinding-extractor.md)
- [Soundness](part-02/def-soundness.md)
- [Knowledge Soundness](part-02/def-knowledge-soundness.md)
- [Unbounded Knowledge Soundness is Relation Soundness](part-02/thm-knowledge-soundness-iff-relation-soundness.md)
- [Knowledge Soundness with Measured Extraction](part-02/def-knowledge-soundness-with-resources.md)
- [State Function](part-02/def-state-function.md)
- [Knowledge State Function](part-02/def-knowledge-state-function.md)
- [Round-by-Round Soundness](part-02/def-round-by-round-soundness.md)
- [Round-by-Round Knowledge Soundness](part-02/def-round-by-round-knowledge-soundness.md)
- [Round-by-Round Knowledge Soundness with a Named Extractor](part-02/def-round-by-round-knowledge-soundness-with.md)
- [Challenge Tree](part-02/def-challenge-tree.md)
- [Tree Special Soundness](part-02/def-tree-special-soundness.md)
- [Coordinate-Wise Special Soundness Generalizes Special Soundness](part-02/thm-cwss-of-special-sound-iff.md)
- [Guarded Verifier](part-02/def-guarded-verifier.md)
- [RBR Soundness Implies Soundness](part-02/thm-rbr-soundness-implies-soundness.md)
- [RBR Knowledge Soundness Implies RBR Soundness](part-02/thm-rbr-knowledge-soundness-implies-rbr-soundnes.md)
- [RBR Soundness and RBR Knowledge Soundness Coincide](part-02/thm-rbr-soundness-iff-rbr-knowledge-soundness.md)
- [RBR Knowledge Soundness Implies Knowledge Soundness](part-02/thm-rbr-knowledge-soundness-implies-knowledge-so.md)

## [Simulator to State-Restoration Knowledge…](part-03/README.md)

- [Simulator](part-03/def-simulator.md)
- [Oracle Reduction Completeness](part-03/def-oracle-reduction-completeness.md)
- [Oracle Verifier Soundness](part-03/def-oracle-verifier-soundness.md)
- [Oracle Verifier Knowledge Soundness](part-03/def-oracle-verifier-knowledge-soundness.md)
- [Oracle Verifier RBR Soundness](part-03/def-oracle-verifier-rbr-soundness.md)
- [Oracle Verifier RBR Knowledge Soundness](part-03/def-oracle-verifier-rbr-knowledge-soundness.md)
- [State-Restoration Experiment](part-03/def-sr-experiment.md)
- [Round-by-Round Knowledge Certificate in the Interaction Layer](part-03/def-interaction-knowledge-certificate.md)
- [State-Restoration Knowledge Soundness](part-03/thm-sr-knowledge-soundness.md)
- [State-Restoration Knowledge Soundness with Per-Round Errors](part-03/thm-sr-knowledge-soundness-nonuniform.md)
