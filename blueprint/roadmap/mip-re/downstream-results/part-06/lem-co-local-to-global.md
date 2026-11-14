---
declaration: lemma
origin: cited
lean: MIPRE.LIDT.Co.ExpansionHypercubeGraph.localVariance, MIPRE.LIDT.Co.ExpansionHypercubeGraph.globalVariance, MIPRE.LIDT.Co.ExpansionHypercubeGraph.re_combinedTraceForm_nonneg, MIPRE.LIDT.Co.ExpansionHypercubeGraph.traceForm_localToGlobal, MIPRE.LIDT.Co.ExpansionHypercubeGraph.localToGlobal, MIPRE.LIDT.Co.ExpansionHypercubeGraph.localToGlobalBipartite
statement: formalized
proof: formalized
---

# Local-to-global variance on the hypercube, for any vector state

Let $\Psi$ be a vector state on a Hilbert space $K$ (Definition [Symmetric models](../part-05/def-sym-model.md)), and let $(A^u)_{u \in \mathbb{F}_q^m}$ be bounded operators on $K$ indexed by the points. Then

$$
\frac12 \mathop{\mathbb{E}}_{u, v} \bigl\| (A^u - A^v) \Psi \bigr\|^2 \leq m \cdot \frac12 \mathop{\mathbb{E}}_{(u, v)}
\bigl\| (A^u - A^v) \Psi \bigr\|^2 ,
$$

where on the left $u$ and $v$ are independent uniformly random points, and on the right $u$ is a uniformly random point and $v$ is $u$ with a uniformly random coordinate replaced by a uniformly random element of $\mathbb{F}_q$. In particular, in a symmetric model over $\mathcal{P}$, the same holds for the family $L(A^u)$ for any $A^u \in \mathcal{P}$.

## Depends on

- [Symmetric models](../part-05/def-sym-model.md)

## Proof depends on

- [Bipartite model](../part-02/def-bipartite-model.md)

## Proof

The vendored proof, `MIPStarRE.LDT.ExpansionHypercubeGraph.localToGlobal`, realizes the family as a block matrix and traces the scalar inequality $g P_\perp \leq \Delta$ against the state's density, where $\Delta$ is the Laplacian of the hypercube graph, $P_\perp$ the projection onto the vectors of mean zero and $g = 1/(m q^m)$ its spectral gap. A vector state has no density; here the inequality is read through Gram positivity instead. For a positive semidefinite scalar matrix $Q$ indexed by the points, $\mathrm{Re} \sum_{u, v} Q_{u v} \langle A^v \Psi, A^u \Psi \rangle \geq 0$, because $Q$ is a sum of matrices $s^* s$, for which the sum is $\sum_k \| \sum_u s_{k u} A^u \Psi \|^2$. At $Q = \Delta - g P_\perp$, which is positive semidefinite (the scalar spectral estimate, imported from the vendored development), this reads $g \cdot q^m V_{\mathrm{glob}} \leq V_{\mathrm{loc}}$: the sum at $\Delta$ is the local variance $V_{\mathrm{loc}}$, the sum at $P_\perp$ is $\sum_u \| (A^u - \mathop{\mathbb{E}}_v A^v) \Psi \|^2 = q^m V_{\mathrm{glob}}$, and $g q^m = 1/m$ (`planning/c6b-plan.md`, milestone M5). The expectations are those of the vector state read as a state model (Definition [Bipartite model](../part-02/def-bipartite-model.md)). The matrix realization of the vendored development is not ported.

## Lean

Formalized as [`MIPRE.LIDT.Co.ExpansionHypercubeGraph.localVariance`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LIDT.Co.ExpansionHypercubeGraph.localVariance), [`MIPRE.LIDT.Co.ExpansionHypercubeGraph.globalVariance`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LIDT.Co.ExpansionHypercubeGraph.globalVariance), [`MIPRE.LIDT.Co.ExpansionHypercubeGraph.re_combinedTraceForm_nonneg`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LIDT.Co.ExpansionHypercubeGraph.re_combinedTraceForm_nonneg), [`MIPRE.LIDT.Co.ExpansionHypercubeGraph.traceForm_localToGlobal`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LIDT.Co.ExpansionHypercubeGraph.traceForm_localToGlobal), [`MIPRE.LIDT.Co.ExpansionHypercubeGraph.localToGlobal`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LIDT.Co.ExpansionHypercubeGraph.localToGlobal), [`MIPRE.LIDT.Co.ExpansionHypercubeGraph.localToGlobalBipartite`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LIDT.Co.ExpansionHypercubeGraph.localToGlobalBipartite).

## Sources

- [MIP* = RE blueprint: content/08_downstream.tex, line 3734](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/08_downstream.tex#L3734)
