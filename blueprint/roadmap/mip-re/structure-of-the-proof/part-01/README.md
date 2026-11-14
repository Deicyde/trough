---
navigation: transparent
---

# Conditionally linear function to Detyping PCC completeness

- [Conditionally linear function](def-cl-function.md)

Comments. This is the paper's definition (`linear.tex`, `def:cl-func`); the paraphrase this blueprint carried before started at level $1$ and let $V_1 \oplus V_{>1}$ be any direct sum decomposition, both departures from the paper. Two things about the formalization. Every consumer of the definition — the structure lemma below, the query interface of a sampler, the hiding tests of introspection — works with the decomposition data $(V_1, L_1, L_{>1,\cdot})$, which the function does not determine; so the Lean object is a *presentation*, `CLFun`, an inductive type indexed by the level, with `CLFun.eval` the function it presents and `IsCLFun` the paper's notion (some presentation on $V$ evaluates to the function). And presentations live on one ambient space $\mathbb{F}^\iota$ whose register subspaces are sets of coordinates; “a presentation on $V_T$” is the predicate `CLFun.SupportedOn`, under which the paper's $V_{>1}$ is the complement of $V_1$ inside $V_T$. The continuations $L_{>1,v}$ are indexed by all $v$ rather than by the range of $L_1$; the extra ones are never evaluated. The distribution is `clDist`, in the real-valued format of Definition [Nonlocal game](../../foundations/part-01/def-game.md).

- [Orthogonal and canonical complements](def-cl-canonical.md)

Source. `preliminaries.tex`: the orthogonal complement and `lem:perp_perp`; `def:canonical-complement` with `rk:cancomp`; `def:cl-canonical`; `def:Lperp` with `lem:L_perp_perp`. Among the facts ledger node $1.1.6$ lists as “subfield/trace facts as used”.

Comments. The paper defines the canonical complement through a canonical Gaussian elimination: reduce the matrix whose rows are a basis of $S$ to reduced row echelon form and take the standard basis vectors off the pivot columns. The formalization uses instead the equivalent characterization `rk:cancomp` credits to a referee — the dimension sequence $u_j$ above — and that choice is what makes the construction usable. It needs no echelon form, and, more importantly, it is manifestly a function of the *subspace* $S$: the paper has to argue that the echelon form does not depend on the chosen basis or on the order of its vectors, which is exactly what `rk:cancomp` spends its length on, whereas here there is nothing to argue. That the two agree is `card_pivots`: the pivot set has $\dim S$ elements.

This vocabulary is needed for the *lines* of the low-degree test, not for CL functions as such: a line $\ell(u_0, v)$ is presented by the canonical representative $u_0 = L^{\mathrm{Ln}}_v(u)$ of Definition [Seeded CL low individual degree test](../../background-results/part-01/def-lidt-cl.md), $L^{\mathrm{Ln}}_v$ being the canonical linear map with kernel $\mathrm{span}\{v\}$.

- [The two complements](lem-cl-canonical.md)
- [Structure of a CL function](lem-cl-structure.md)
- [Closure of CL functions](lem-cl-closure.md)
- [Direct sums of families, and their distributions](lem-cl-famsum.md)
- [Downsizing](lem-cl-downsize.md)

Comments. The paper states the lemma for admissible $q = 2^t$, $t$ odd, with the self-dual normal basis of Lemma [Deterministic self-dual normal basis](../../background-results/part-04/lem-self-dual-basis.md); the formalization proves it for any basis of any finite field over any subfield, the coordinates of $\mathbb{K}^{nt}$ being indexed by pairs $(i, k)$ and identified with $\{1, \ldots, nt\}$ by a reindexing (`CLFun.reindex`, the transport along any bijection of coordinates, which preserves everything above). The self-dual normal basis matters elsewhere: for the arithmetic of $\mathbb{F}_{2^t}$ to be computable from $\mathbb{F}_2$-data in polynomial time by the samplers and deciders that use it, a matter for the efficient-computability toolkit rather than for this lemma. The paper's downsized *sampler* (`def:downsize_sampler`, `lem:downsize_sampler`), a Turing machine wrapping a sampler over $\mathbb{F}_{2^t}$, has no counterpart here: samplers are over $\mathbb{F}_2$ by definition (Definition [Sampler](../../foundations/part-03/def-sampler.md)), and a construction native to $\mathbb{F}_{2^t}$, such as the introspection sampler, is to present the downsized CL functions directly, this lemma supplying their decomposition data.

**Remark (Why the pipeline is bipartite throughout).** Every soundness clause of this chapter is stated in $\mathrm{val}^*$ and none in ${\mathrm{val}^{s}}$. The choice follows the source transformation contracts and the direct repetition theorem (Theorem [Direct parallel repetition for entangled strategies](../../parallel-repetition/thm-direct-repetition-q.md)), all of which already concern $\mathrm{val}^*$. No scalar transport from a synchronous value bound is needed. In particular, neither the synchronization statement of Theorem [Almost-synchronous strategies are near synchronous strategies](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/03_background_results.tex#L137) nor the additional hypotheses discussed in Remark [The diagonal-weight hypothesis cannot be dropped](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/03_background_results.tex#L180) enter the composition. The source rigidity analyses can therefore be formalized in their bipartite setting, without the synchronization invariant of Remark [The synchronization invariant](../../foundations/README.md). Lemma [Synchronous value lower-bounds the quantum value](../../foundations/part-01/lem-sync-le-valstar.md) is used only to read a $\mathrm{val}^*$ conclusion in ${\mathrm{val}^{s}}$ when a synchronous statement is wanted (Theorem [Halting reduction](../part-09/thm-halting.md), Theorem [Halting reduces to the game value; Theorem 12.2 of (JNVWY20), synchronous form](../../the-main-theorem/thm-main.md)), never in the other direction.

What this costs in turn is that the rigidity and approximate-measurement lemmas the inner analyses consume must be stated bipartitely, as their sources state them, rather than tracially. That is the arrangement of (JNVWY20) and of the companion repository's paper, so it is the arrangement with the least to prove.

## Question reduction: introspection

Introspection removes the verifier's cost of sampling questions: instead of receiving questions for $\mathsf{V}_{2^n}$, the players *sample the questions themselves* by measuring shared EPR pairs, and the new verifier uses the Pauli basis test (Theorem [Pauli basis test / quantum low individual degree test](../../background-results/part-01/thm-qld.md)) to force honest sampling. The CL structure of the sampler is what makes commitment to each stage of the sampled question enforceable (the “hiding” directions of the CL decomposition). The result is a verifier whose questions are exponentially smaller, at the price of a fixed number of levels.

**Remark (Typed verifiers and the exterior transformation boundaries).** Introspection is detyped at its exterior boundary. Oracularization stays typed inside answer reduction; the final answer-reduced verifier is then detyped. The exterior levels are $5\to7\to7$ for introspection, answer reduction and repetition. Detyping adds two levels and gives $\mathrm{failure}_{\mathrm{typed}}\leq16^{|T|} \mathrm{failure}_{\mathrm{detyped}}$ via a same-state strategy conversion. This is a bound on failure, not a multiplicative comparison of values. The graph must have an edge. The following interfaces retain the effective and timeout hypotheses of the current source (AuditSync26).

- [Typed sampler and its distribution](def-typed-sampler-interface.md)
- [Typed decider and normal verifier](def-typed-normal-interface.md)
- [Graph rejection sampling](lem-detype-graph.md)
- [Detyped conditionally linear functions](lem-detype-cl.md)
- [Register embeddings and detyped query routing](lem-detype-queries.md)
- [Executable fixed CL samplers](lem-fixed-cl-sampler.md)
- [Finite-game detyping PCC completeness](lem-detype-game-completeness.md)
- [Executable detyping sampler](lem-detype-functional-sampler.md)
- [Detyping with answer coarse-graining](lem-detype-game-answers.md)
- [Executable detyping decider with two answer cuts](lem-detype-executable-decider.md)
- [Strategy transfer for the executable detyping verifier](lem-detype-program-strategies.md)
- [Total clocking of arbitrary typed decision programs](lem-detype-total-clock.md)
- [Detyping PCC completeness](lem-detype-completeness.md)
