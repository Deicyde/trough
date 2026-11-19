---
navigation: transparent
---

# Monotone Straightline Extractor to RBR Knowledge Soundness Implies…

- [Monotone Straightline Extractor](def-monotone-straightline-extractor.md)
- [Round-by-Round Extractor](def-rbr-extractor.md)
- [Rewinding Extractor](def-rewinding-extractor.md)

### Soundness Definitions

For soundness, we need to consider different notions. These notions differ in two main aspects:

- Whether we consider the plain soundness, or knowledge soundness. The latter relies on the notion of an *extractor*.
- Whether we consider plain, state-restoration, round-by-round, or tree-based (special) soundness.

State-restoration knowledge soundness is necessary for the security of the SNARK obtained from an oracle reduction after composing with a commitment scheme and applying the Fiat–Shamir transform. Round-by-round knowledge certificates in the interaction layer imply it (State-Restoration Security). Special soundness is the other classical source of knowledge soundness, via a rewinding extractor; its tree-based definitions are given in Tree-Based Special Soundness, but the rewinding argument from them to knowledge soundness is not yet formalized.

- [Soundness](def-soundness.md)
- [Knowledge Soundness](def-knowledge-soundness.md)

**Remark (Extraction cost).** The extractor in [Knowledge Soundness](def-knowledge-soundness.md) is unconstrained: it may be noncomputable and may pick a witness by classical choice. With that extractor, knowledge soundness is equivalent to *relation soundness*, which bounds the probability that the prover outputs a valid output pair from an input statement with no valid input witness ([Unbounded Knowledge Soundness is Relation Soundness](thm-knowledge-soundness-iff-relation-soundness.md)). Knowledge soundness in the cryptographic sense is the game for a named extractor together with a cost bound for that extractor. The measured contract $\mathsf{knowledgeSoundnessWithResources}$ adds this bound: the extractor's run is the execution of a named measured program, without querying the shared oracle, and every execution path of the program costs at most a stated budget.

- [Unbounded Knowledge Soundness is Relation Soundness](thm-knowledge-soundness-iff-relation-soundness.md)
- [Knowledge Soundness with Measured Extraction](def-knowledge-soundness-with-resources.md)

### Round-by-Round Security

To define round-by-round (knowledge) soundness, we need to define the notion of a *state function*. This is a (possibly inefficient) function $\mathsf{StateF}$ that, for every challenge sent by the verifier, takes in the transcript of the protocol so far and outputs whether the state is doomed or not. Roughly speaking, the requirement of round-by-round soundness is that, for any (possibly malicious) prover $P$, if the state function outputs that the state is doomed on some partial transcript of the protocol, then the verifier will reject with high probability.

- [State Function](def-state-function.md)
- [Knowledge State Function](def-knowledge-state-function.md)

Both round-by-round notions below bound a bad transition at every *fixed* transcript prefix, with the probability taken over the fresh challenge alone. This fixed-prefix form is the only round-by-round notion in the library. Bounds averaged over prefixes reached with honestly sampled earlier challenges follow from it with the same error, but they do not survive Fiat–Shamir or state restoration, where the adversary chooses the prefix to extend.

- [Round-by-Round Soundness](def-round-by-round-soundness.md)
- [Round-by-Round Knowledge Soundness](def-round-by-round-knowledge-soundness.md)
- [Round-by-Round Knowledge Soundness with a Named Extractor](def-round-by-round-knowledge-soundness-with.md)

### Tree-Based Special Soundness

Special soundness and its relatives extract a witness from a tree of accepting transcripts that share every message before the round where their challenges diverge.

- [Challenge Tree](def-challenge-tree.md)
- [Tree Special Soundness](def-tree-special-soundness.md)
- [Coordinate-Wise Special Soundness Generalizes Special Soundness](thm-cwss-of-special-sound-iff.md)

### Implications Between Security Notions

- [Guarded Verifier](def-guarded-verifier.md)

Round-by-round soundness implies soundness, and round-by-round knowledge soundness implies knowledge soundness, for guarded verifiers. A state function's terminal condition is checked from a fresh oracle state, while the ordinary games run the verifier from whatever oracle state the prover left behind, so without the guard the implications fail. The library states no implication from knowledge soundness to soundness: the knowledge game fixes the output witness before a randomized verifier runs, so the usual argument does not apply.

- [RBR Soundness Implies Soundness](thm-rbr-soundness-implies-soundness.md)
- [RBR Knowledge Soundness Implies RBR Soundness](thm-rbr-knowledge-soundness-implies-rbr-soundnes.md)
- [RBR Soundness and RBR Knowledge Soundness Coincide](thm-rbr-soundness-iff-rbr-knowledge-soundness.md)
- [RBR Knowledge Soundness Implies Knowledge Soundness](thm-rbr-knowledge-soundness-implies-knowledge-so.md)
