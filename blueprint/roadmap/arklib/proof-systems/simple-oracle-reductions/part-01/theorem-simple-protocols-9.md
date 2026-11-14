---
declaration: theorem
origin: cited
lean: RandomEvaluation.oracleVerifier_rbrKnowledgeSoundness, RandomEvaluation.oracleVerifier_rbrKnowledgeSoundness_of_degreeOf_le_one
statement: formalized
---

# RandomEvaluation Soundness

If every $P(x, \mathsf{o})$ has total degree at most $d$, the RandomEvaluation reduction satisfies fixed-prefix round-by-round knowledge soundness with error $\frac{d}{|\mathbb{F}|}$. This follows from the Schwartz–Zippel lemma: a nonzero polynomial of total degree at most $d$ vanishes at a uniformly random point of $\mathbb{F}^m$ with probability at most $\frac{d}{|\mathbb{F}|}$. For multilinear polynomials the error is $\frac{m}{|\mathbb{F}|}$.

## Depends on

- [RandomEvaluation Oracle Reduction](def-random-evaluation.md)

## Lean

Stated as [`RandomEvaluation.oracleVerifier_rbrKnowledgeSoundness`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/RandomEvaluation.oracleVerifier_rbrKnowledgeSoundness), [`RandomEvaluation.oracleVerifier_rbrKnowledgeSoundness_of_degreeOf_le_one`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/RandomEvaluation.oracleVerifier_rbrKnowledgeSoundness_of_degreeOf_le_one); the blueprint marks no proof of it as formalized.

## Sources

- [ArkLib blueprint: proof_systems/simple_protocols.tex, line 194](https://github.com/Verified-zkEVM/ArkLib/blob/e1c185ba001d225d1f3ea84071d67a8c6c56d6a0/blueprint/src/proof_systems/simple_protocols.tex#L194)
