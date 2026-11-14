---
declaration: theorem
origin: cited
lean: MIPRE.GapCompression, MIPRE.GapCompression.ofPipeline
statement: formalized
proof: formalized
---

# Gap-preserving compression from ambient stage contracts

Assume $I : \texttt{MIPRE.Introspection 7}$ and $A : \texttt{MIPRE.AnswerReduction 5}$, the contracts of Definitions [Ambient introspection contract](../part-06/def-introspection-contract.md) and [Ambient answer-reduction contract](def-answer-reduction-contract.md). Using the supplied repetition construction of Theorem [Parallel repetition of normal form verifiers](thm-parallel-repetition.md), there is a universal constant $C_0 > 0$ and a polynomial-time procedure ${\mathsf{Compress}}$ that on input $(\mathsf{V}, \lambda)$ outputs a $7$-level normal form verifier $\mathsf{V}^{\textsc{Compr}} = (\mathcal{S}^{\textsc{Compr}}, \mathcal{D}^{\textsc{Compr}})$ with runtime coefficients bounded by $\mathrm{poly}(n,\lambda)$ at a fixed input-size degree, where $\mathcal{S}^{\textsc{Compr}}$ is independent of $\mathsf{V}$ and computable from $\lambda$ in time $\mathrm{polylog}(\lambda)$. If moreover $\mathsf{V}$ is a $\lambda$-bounded $7$-level normal form verifier, then for all $n \geq C_0$ and $N = 2^n$:

1. (**Completeness**) If $\mathsf{V}_N$ has a value-$1$ PCC strategy, then so does $\mathsf{V}^{\textsc{Compr}}_n$.
2. (**Soundness**) If $\mathrm{val}^*(\mathsf{V}_N) \leq \tfrac12$ then $\mathrm{val}^*(\mathsf{V}^{\textsc{Compr}}_n) \leq \tfrac12$: the class “$\mathrm{val}^* \leq \tfrac12$” is preserved, in the same value at both ends.

## Depends on

- [Ambient introspection contract](../part-06/def-introspection-contract.md)
- [Ambient answer-reduction contract](def-answer-reduction-contract.md)
- [Parallel repetition of normal form verifiers](thm-parallel-repetition.md)
- [$\lambda$-bounded verifier in the ambient model](../../foundations/part-03/def-lambda-bounded.md)
- [PCC strategy](../../foundations/part-01/def-pcc.md)
- [Normal form verifier in the ambient model](../../foundations/part-03/def-normal-verifier.md)
- [The compressed sampler does not depend on the verifier](lem-compress-sampler-indep.md)

## Proof depends on

- [The margin claim](lem-compress-margin.md)
- [A universal repetition exponent](lem-compress-tau.md)
- [Value models](../../downstream-results/part-01/def-value-model.md)
- [The soundness chain of compression, in a value model](../../downstream-results/part-01/lem-compress-sound-in.md)

## Proof

Let ${\mathsf{ComputeIntroVerifier}}$ and ${\mathsf{ComputeAnsRedVerifier}}$ denote the procedures provided by $I$ and $A$, respectively. These are assumed ambient procedures in this proof. ${\mathsf{Compress}}(\mathsf{V}, \lambda)$ is ${\mathsf{ComputeIntroVerifier}}(\mathsf{V}, \lambda, 7)$, then ${\mathsf{ComputeAnsRedVerifier}}(\cdot, \lambda, \mu, \sigma(\lambda))$, then ${\mathsf{ComputeRepeatedVerifier}}(\cdot, 7, \lambda, \tau, \beta)$, with $\mu$ from Lemma [The margin claim](lem-compress-margin.md), $\sigma(\lambda)$ a polynomial in $\lambda$ dominating $C_{\mathrm{intro}} (\lambda + 1)^{C_{\mathrm{intro}}}$, $\beta$ an exponent with $\mathrm{poly}\bigl((\lambda n + 1)^\mu + \sigma(\lambda)\bigr) \leq (\lambda n + 1)^\beta$, and $\tau$ from Lemma [A universal repetition exponent](lem-compress-tau.md); $C_0$ dominates $2$, $C_{\mathrm{ar}}$, the introspection and answer-reduction margin thresholds, the threshold for the lower bound on $\varepsilon_2$, and $\tau$, as recorded in `Pipeline/Compress.lean`. The complexity clauses chain the three complexity clauses through the budgets: every bound is a monotone polynomial expression in $n$, $\lambda$, $\sigma(\lambda)$ and the sizes of the programs along the chain, hence at most a polynomial in $n + \lambda$. The value clauses are Remark [How the value chain composes, and what it avoids](../README.md). In Lean this is `MIPRE.GapCompression.ofPipeline`: an `Introspection 7`, an `AnswerReduction 5` and a `Repetition 7` give a `GapCompression`. $\sigma(\lambda)$ is computed by iterating the program of $\lambda(n)$ of Lemma [The parameter of the halting verifier](lem-lambda.md), there being no polynomial-time arithmetic in the toolkit for the paper's $\lceil C_{\mathrm{intro}} \lambda^{C_{\mathrm{intro}}} \rceil$, which only has to be dominated; it also dominates the size of the introspective sampler, which the complexity clause of Definition [Ambient answer-reduction contract](def-answer-reduction-contract.md) bounds by $\sigma$. Oracularization is not a stage: it is the first step of the proof of Theorem [Answer reduction](thm-answer-reduction.md).

## Lean

Formalized as [`MIPRE.GapCompression`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.GapCompression), [`MIPRE.GapCompression.ofPipeline`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.GapCompression.ofPipeline).

## Sources

- [MIP* = RE blueprint: content/06_proof_structure.tex, line 6281](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/06_proof_structure.tex#L6281)
