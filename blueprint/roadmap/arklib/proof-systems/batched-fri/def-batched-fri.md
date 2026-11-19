---
declaration: definition
origin: cited
lean: BatchedFri.Spec.BatchingRound.inputRelation, BatchedFri.Spec.BatchingRound.batchOracleReduction, BatchedFri.Spec.batchedFRIreduction
statement: formalized
---

# Batched FRI relation and reduction

The input statement is $m+1$ oracle words $f_0,\ldots,f_m:D\to\mathbb{F}$; the witness is $m+1$ polynomials $p_0,\ldots,p_m$ of degree less than $d_0$. For $\delta\geq 0$, the input relation holds when some set $T\subseteq D$ with $|T|\geq(1-\delta)2^n$ satisfies $f_i(x)=p_i(x)$ for every $i$ and every $x\in T$. In the batching round the verifier sends one seed $c\in S$ and the prover sends nothing. The output is the virtual oracle $\sum_{i\leq m}G(c)_i f_i$, which feeds the initial FRI relation at the same radius. Batched FRI is the append of this round with the FRI reduction of the previous section.

## Depends on

- [proximity_generator](../whir/def-proximity-generator.md)
- [Reed-Solomon Code](../../supporting-theories/coding-theory/def-reed-solomon-code.md)

## Lean

Formalized as [`BatchedFri.Spec.BatchingRound.inputRelation`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/BatchedFri.Spec.BatchingRound.inputRelation), [`BatchedFri.Spec.BatchingRound.batchOracleReduction`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/BatchedFri.Spec.BatchingRound.batchOracleReduction), [`BatchedFri.Spec.batchedFRIreduction`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/BatchedFri.Spec.batchedFRIreduction).

## Sources

- [ArkLib blueprint: proof_systems/fri.tex, line 287](https://github.com/Verified-zkEVM/ArkLib/blob/e1c185ba001d225d1f3ea84071d67a8c6c56d6a0/blueprint/src/proof_systems/fri.tex#L287)
