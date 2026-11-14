---
declaration: lemma
origin: cited
lean: MIPRE.CL.CLFun.famSum, MIPRE.CL.IsCLFun.famSum, MIPRE.CL.CLFun.exactlyOn_famSum, MIPRE.CL.CLFun.eval_famSum, MIPRE.CL.CLFun.eval_truncate_famSum, MIPRE.CL.CLFun.factorOfPrefix_famSum, MIPRE.CL.CLFun.mapOfPrefix_famSum, MIPRE.CL.clDist_famSum
statement: formalized
proof: formalized
---

# Direct sums of families, and their distributions

Let $V = \bigoplus_{i=1}^{k} V^{(i)}$ with every $V^{(i)}$ a copy of $F^s$, and let $L^{(i)}$ be an $\ell$-level CL function on $V^{(i)}$ for each $i$. Then $x \mapsto (L^{(i)}(x^{(i)}))_i$ is an $\ell$-level CL function on $V$, exact if every $L^{(i)}$ is, whose marginals, factor spaces and stage maps read off a prefix are those of the $L^{(i)}$ on the blocks. For two such families $(L^{(i)})$, $(R^{(i)})$, the conditionally linear distribution of the pair of direct sums is the product of the distributions of the pairs $(L^{(i)}, R^{(i)})$.

## Depends on

- [Structure of a CL function](lem-cl-structure.md)

## Proof

Item (3) of Lemma [Closure of CL functions](lem-cl-closure.md) iterated over the $k$ summands, done in one induction on the level with the $k$ presentations side by side: at every stage the register subspace is the union of the blocks' and the map their direct sum, and the continuations are selected blockwise. The Lean presentation lives on any $F^\kappa$ with $\kappa \cong \{1, \ldots, k\} \times \{1, \ldots, s\}$, so that $\kappa = \{1, \ldots, ks\}$ needs no reindexing. For the distribution: a uniform vector of $V$ is a $k$-tuple of independent uniform vectors of the blocks, and the event that the direct sums take prescribed values is the conjunction of the blockwise events.

## Lean

Formalized as [`MIPRE.CL.CLFun.famSum`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.CL.CLFun.famSum), [`MIPRE.CL.IsCLFun.famSum`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.CL.IsCLFun.famSum), [`MIPRE.CL.CLFun.exactlyOn_famSum`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.CL.CLFun.exactlyOn_famSum), [`MIPRE.CL.CLFun.eval_famSum`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.CL.CLFun.eval_famSum), [`MIPRE.CL.CLFun.eval_truncate_famSum`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.CL.CLFun.eval_truncate_famSum), [`MIPRE.CL.CLFun.factorOfPrefix_famSum`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.CL.CLFun.factorOfPrefix_famSum), [`MIPRE.CL.CLFun.mapOfPrefix_famSum`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.CL.CLFun.mapOfPrefix_famSum), [`MIPRE.CL.clDist_famSum`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.CL.clDist_famSum).

## Sources

- [MIP* = RE blueprint: content/06_proof_structure.tex, line 216](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/06_proof_structure.tex#L216)
