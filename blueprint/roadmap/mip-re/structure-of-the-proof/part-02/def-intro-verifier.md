---
declaration: definition
origin: cited
lean: MIPRE.Introspection.QuestionType, MIPRE.Introspection.TypeGraph.adj, MIPRE.Introspection.DecisionCompiler.typedDecider, MIPRE.Introspection.DecisionCompiler.output
statement: formalized
---

# The introspective verifier

Fix $\ell$ and an $\ell$-level verifier $\mathsf{V}$ satisfying the paper's absolute $\lambda$-bound, as distinguished in Remark [Runtime normalization obligation](../README.md). The *introspective verifier* $\mathsf{V}^{\textsc{Intro}}$ is the typed verifier whose players sample the conditionally linear question distribution of $\mathsf{V}_{2^n}$ *themselves*: the question $y \in V = \mathbb{F}_q^s$ is not sent to them, but obtained by each player measuring its half of $Q$ shared EPR pairs in a Pauli basis, and reported back. Its decider runs three kinds of test.

1. a **Pauli test**, which is the game of Theorem [Pauli basis test / quantum low individual degree test](../../background-results/part-01/thm-qld.md) on the same EPR pairs, so that the measurements the players use to sample are forced to be genuine Pauli measurements in the low-degree-encoded basis;
2. a **sampling test**, which forces the reported $y$ to be distributed as the conditionally linear distribution of $\mathsf{V}_{2^n}$ rather than as anything else the players might prefer;
3. a **hiding test**, which forces each player not to learn the parts of the question that the conditional sampling should have hidden from it — the types $\mathtt{Hide}_1, \ldots, \mathtt{Hide}_\ell$ exist for this, one per level.

It is a $3$-level *typed* verifier, hence $5$-level once detyped (Remark [Typed verifiers and the exterior transformation boundaries](../README.md)), and that $5$ is what the compression pipeline consumes. The Lean verifier is the ambient one, built for $7$-level inputs (Definition [Ambient introspection contract](../part-06/def-introspection-contract.md)); its question types include the `Introspect` and `Read` types of the source.

## Depends on

- [Normal form verifier in the ambient model](../../foundations/part-03/def-normal-verifier.md)
- [Conditionally linear function](../part-01/def-cl-function.md)
- [Effective unary prime-power decomposition](../../background-results/part-04/lem-binary-degree-decomposition.md)
- [Uniform deterministic binary irreducible polynomials](../../background-results/part-05/lem-binary-uniform-irreducible.md)
- [Effective polynomial-basis field arithmetic](../../background-results/part-05/lem-effective-binary-field-arithmetic.md)
- [Effective binary matrix arithmetic and elimination](../../background-results/part-05/lem-effective-binary-linear-algebra.md)
- [Effective inversion, Frobenius iteration and trace](../../background-results/part-05/lem-effective-field-inverse-trace.md)
- [Effective Frobenius, trace Gram matrices and table transport](../../background-results/part-05/lem-effective-field-matrices.md)
- [Deterministic self-dual normal basis](../../background-results/part-04/lem-self-dual-basis.md)
- [Uniform executable cross-introspection compiler](../part-03/lem-intro-dynamic-source-compiler.md)
- [Pauli basis test](../../background-results/part-01/def-qld-game.md)
- [Register embeddings and detyped query routing](../part-01/lem-detype-queries.md)

## Lean

Formalized as [`MIPRE.Introspection.QuestionType`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.QuestionType), [`MIPRE.Introspection.TypeGraph.adj`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.TypeGraph.adj), [`MIPRE.Introspection.DecisionCompiler.typedDecider`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.DecisionCompiler.typedDecider), [`MIPRE.Introspection.DecisionCompiler.output`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.DecisionCompiler.output).

## Sources

- [MIP* = RE blueprint: content/06_proof_structure.tex, line 1013](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/06_proof_structure.tex#L1013)
