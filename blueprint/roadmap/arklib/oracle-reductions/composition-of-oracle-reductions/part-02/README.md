---
navigation: transparent
---

# Witness Lens to State Function Lifting

- [Witness Lens](def-witness-lens.md)
- [Context Lens](def-context-lens.md)
- [Oracle Context Lens](def-oracle-context-lens.md)
- [Extractor Lens](def-extractor-lens.md)

### Lifting Reductions

Given a context lens, we can lift reductions from inner contexts to outer contexts.

- [Prover Context Lifting](def-prover-lift-context.md)
- [Verifier Context Lifting](def-verifier-lift-context.md)
- [Reduction Context Lifting](def-reduction-lift-context.md)

### Conditions for Security Preservation

For lifting to preserve security properties, the lens must satisfy conditions relative to the outer and inner relations. Each condition takes a compatibility predicate between the outer input and the inner output. The lifting theorems instantiate it with the outputs the inner reduction or verifier can actually produce on the projected input, for some transcript.

- [Completeness-Preserving Context Lens](def-context-lens-is-complete.md)
- [Soundness-Preserving Statement Lens](def-statement-lens-is-sound.md)
- [Knowledge-Soundness-Preserving Extractor Lens](def-context-lens-is-knowledge-sound.md)

### Security Preservation Theorems for Context Lifting

- [Completeness Preservation under Context Lifting](thm-lift-context-completeness.md)
- [Soundness Preservation under Context Lifting](thm-lift-context-soundness.md)
- [Knowledge Soundness Preservation under Context Lifting](thm-lift-context-knowledge-soundness.md)
- [RBR Soundness Preservation under Context Lifting](thm-lift-context-rbr-soundness.md)
- [RBR Knowledge Soundness Preservation under Context Lifting](thm-lift-context-rbr-knowledge-soundness.md)

### Extractors and State Functions

Context lifting also applies to extractors and state functions used in knowledge soundness and round-by-round soundness.

- [Straightline Extractor Lifting](def-straightline-extractor-lift-context.md)
- [Round-by-Round Extractor Lifting](def-rbr-extractor-lift-context.md)
- [State Function Lifting](def-state-function-lift-context.md)

These composition and lifting operators provide the essential building blocks for constructing complex oracle reductions from simpler components while preserving their security properties.
