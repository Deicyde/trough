---
declaration: definition
origin: cited
lean: Verifier.rbrKnowledgeSoundness
statement: formalized
---

# Round-by-Round Knowledge Soundness

A protocol with verifier $\mathcal{V}$ satisfies **round-by-round knowledge soundness** with respect to input relation $R_{\text{in}}$, output relation $R_{\text{out}}$, and error function $\epsilon: \text{ChallengeIdx} \to \mathbb{R}_{\geq 0}$ if:

- there exist a family of intermediate witness types, a round-by-round extractor, and a knowledge state function for the verifier and the input/output relations, such that
- for all initial statements,
- for all challenge rounds $i$,
- for all transcript prefixes $\tau$ up to round $i$,

the probability, over the next challenge $c$ chosen uniformly at random, that some intermediate witness $w$ satisfies:

- the knowledge state function is true for $w$ at $\tau$ extended by $c$, and
- it is false at $\tau$ for the witness extracted back from $w$

is at most $\epsilon(i)$. As for round-by-round soundness, the bound holds at every fixed transcript prefix. As in [Extraction cost](../README.md), the extractor is unconstrained.

## Depends on

- [Type Signature of a Verifier](../part-01/def-verifier.md)
- [Knowledge State Function](def-knowledge-state-function.md)
- [Round-by-Round Extractor](def-rbr-extractor.md)

## Lean

Formalized as [`Verifier.rbrKnowledgeSoundness`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/Verifier.rbrKnowledgeSoundness).

## Sources

- [ArkLib blueprint: oracle_reductions/defs.tex, line 692](https://github.com/Verified-zkEVM/ArkLib/blob/e1c185ba001d225d1f3ea84071d67a8c6c56d6a0/blueprint/src/oracle_reductions/defs.tex#L692)
