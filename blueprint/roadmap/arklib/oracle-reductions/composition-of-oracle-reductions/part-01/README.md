---
navigation: transparent
---

# Protocol Specification Append to Statement Lens

- [Protocol Specification Append](def-protocol-spec-append.md)
- [Full Transcript Append](def-transcript-append.md)

### Composition of Provers and Verifiers

- [Prover Append](def-prover-append.md)
- [Verifier Append](def-verifier-append.md)
- [Reduction Append](def-reduction-append.md)
- [Oracle Reduction Append](def-oracle-reduction-append.md)

### General Sequential Composition

For composing an arbitrary number of reductions, we provide a general composition operation.

- [General Protocol Specification Composition](def-protocol-spec-compose.md)
- [General Prover Composition](def-prover-compose.md)
- [General Verifier Composition](def-verifier-compose.md)
- [General Reduction Composition](def-reduction-compose.md)

### Security Properties of Sequential Composition

Completeness composition requires control of the prover execution order and of the shared oracle state. Fix one stateful oracle implementation on a state space $\Sigma$ and an initial state distribution $\mu$. The second component receives the state left by the first component. A guarantee for the second component initialized separately from $\mu$ does not cover this state.

The composition theorems below are proved under their stated hypotheses. Soundness and knowledge soundness require guarded verifiers (Definition [Guarded Verifier](../../definitions/part-02/def-guarded-verifier.md)): the first verifier for binary composition, and every verifier for finite chains. Bounds for later components must hold from every deterministic shared oracle state, and knowledge soundness composes extractors that are pure functions of the input statement, the output witness and the transcript.

- [Completeness Preservation under Append](thm-completeness-append.md)
- [Perfect Completeness Preservation under Append](thm-perfect-completeness-append.md)
- [Soundness Preservation under Append](thm-soundness-append.md)
- [Knowledge Soundness Preservation under Append](thm-knowledge-soundness-append.md)

Round-by-round guarantees and a guarded first verifier give the following composition theorem.

- [Round-by-Round Knowledge Soundness under a Guarded First Verifier](thm-rbr-knowledge-soundness-append-guarded.md)

Finite-chain completeness likewise requires guarantees from every shared state. Finite-chain soundness and knowledge soundness hold for guarded chains, and so does round-by-round knowledge soundness.

- [General Completeness Preservation](thm-completeness-compose.md)
- [General Soundness Preservation](thm-soundness-compose.md)
- [General Knowledge Soundness Preservation](thm-knowledge-soundness-compose.md)
- [Round-by-Round Knowledge Soundness of a Guarded Chain](thm-rbr-knowledge-soundness-compose-guarded.md)

## Lifting Contexts

Another essential tool for modular oracle reductions is the ability to adapt reductions from one context to another. This allows us to apply reductions designed for simple contexts to more complex scenarios.

### Context Lenses

The fundamental abstraction for context adaptation is a *lens*, a pair of maps between an outer and an inner context: one projects inputs inward, the other lifts outputs back outward.

- [Statement Lens](def-statement-lens.md)
