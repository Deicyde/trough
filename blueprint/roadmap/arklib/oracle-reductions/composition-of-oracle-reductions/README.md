# Composition of Oracle Reductions

In this section, we describe a suite of composition operators for building secure oracle reductions from simpler secure components. In other words, we define a number of definitions that govern how oracle reductions can be composed to form larger reductions, and how the resulting reduction inherits the security properties of the components.

## Sequential Composition

Sequential composition allows us to chain together oracle reductions where the output context of one reduction becomes the input context of the next reduction. This is fundamental for building complex protocols from simpler components.

### Composition of Protocol Specifications

We begin by defining how to compose protocol specifications and their associated structures.

## [Protocol Specification Append to Statement Lens](part-01/README.md)

- [Protocol Specification Append](part-01/def-protocol-spec-append.md)
- [Full Transcript Append](part-01/def-transcript-append.md)
- [Prover Append](part-01/def-prover-append.md)
- [Verifier Append](part-01/def-verifier-append.md)
- [Reduction Append](part-01/def-reduction-append.md)
- [Oracle Reduction Append](part-01/def-oracle-reduction-append.md)
- [General Protocol Specification Composition](part-01/def-protocol-spec-compose.md)
- [General Prover Composition](part-01/def-prover-compose.md)
- [General Verifier Composition](part-01/def-verifier-compose.md)
- [General Reduction Composition](part-01/def-reduction-compose.md)
- [Completeness Preservation under Append](part-01/thm-completeness-append.md)
- [Perfect Completeness Preservation under Append](part-01/thm-perfect-completeness-append.md)
- [Soundness Preservation under Append](part-01/thm-soundness-append.md)
- [Knowledge Soundness Preservation under Append](part-01/thm-knowledge-soundness-append.md)
- [Round-by-Round Knowledge Soundness under a Guarded First Verifier](part-01/thm-rbr-knowledge-soundness-append-guarded.md)
- [General Completeness Preservation](part-01/thm-completeness-compose.md)
- [General Soundness Preservation](part-01/thm-soundness-compose.md)
- [General Knowledge Soundness Preservation](part-01/thm-knowledge-soundness-compose.md)
- [Round-by-Round Knowledge Soundness of a Guarded Chain](part-01/thm-rbr-knowledge-soundness-compose-guarded.md)
- [Statement Lens](part-01/def-statement-lens.md)

## [Witness Lens to State Function Lifting](part-02/README.md)

- [Witness Lens](part-02/def-witness-lens.md)
- [Context Lens](part-02/def-context-lens.md)
- [Oracle Context Lens](part-02/def-oracle-context-lens.md)
- [Extractor Lens](part-02/def-extractor-lens.md)
- [Prover Context Lifting](part-02/def-prover-lift-context.md)
- [Verifier Context Lifting](part-02/def-verifier-lift-context.md)
- [Reduction Context Lifting](part-02/def-reduction-lift-context.md)
- [Completeness-Preserving Context Lens](part-02/def-context-lens-is-complete.md)
- [Soundness-Preserving Statement Lens](part-02/def-statement-lens-is-sound.md)
- [Knowledge-Soundness-Preserving Extractor Lens](part-02/def-context-lens-is-knowledge-sound.md)
- [Completeness Preservation under Context Lifting](part-02/thm-lift-context-completeness.md)
- [Soundness Preservation under Context Lifting](part-02/thm-lift-context-soundness.md)
- [Knowledge Soundness Preservation under Context Lifting](part-02/thm-lift-context-knowledge-soundness.md)
- [RBR Soundness Preservation under Context Lifting](part-02/thm-lift-context-rbr-soundness.md)
- [RBR Knowledge Soundness Preservation under Context Lifting](part-02/thm-lift-context-rbr-knowledge-soundness.md)
- [Straightline Extractor Lifting](part-02/def-straightline-extractor-lift-context.md)
- [Round-by-Round Extractor Lifting](part-02/def-rbr-extractor-lift-context.md)
- [State Function Lifting](part-02/def-state-function-lift-context.md)
