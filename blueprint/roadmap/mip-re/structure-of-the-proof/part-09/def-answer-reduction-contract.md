---
declaration: definition
origin: cited
lean: MIPRE.AnswerReduction
statement: formalized
---

# Ambient answer-reduction contract

The structure `MIPRE.AnswerReduction` is an ambient contract, parametrized by $\ell$, its output at $\max\{\ell + 2, 5\}$ levels. The hypotheses on the input are the budget `AnswerReduction.inBudget`: sampler and decider runtime coefficients at most $(\lambda n + 1)^\mu$ and $2^{(\lambda n + 1)^\mu}$, respectively, both at input-size degree $\mu$, questions of dimension at most the sampler's bound and answers rejected beyond the decider's, together with $\left\vert {\mathcal{D}} \right\vert \leq \sigma$. The complexity clause asks $\left\vert {\mathcal{S}} \right\vert \leq \sigma$ as well: the output runs the input sampler through the universal machine, whose overhead is polynomial in the size of the program it simulates, and the source's $\mathrm{poly}((\lambda n)^\mu, \sigma)$ bounds are silent on that size (the introspective sampler that compression supplies has size polynomial in $\log \lambda$). For a universal base polynomial $P$ and base degree $d$, the output is within $P((\lambda n+1)^\mu+\sigma+\lambda+n)^{\mu+1}$ at input-size degree $d(\mu+1)$, and rejects longer answers. The terms $\lambda+n$ change nothing for $\lambda,\mu\geq1$ and $n\geq2$, where they are at most $2(\lambda n)^\mu$; they cover the indices where $(\lambda n+1)^\mu$ does not grow with $n$, at which the output still computes the PCP's parameters from $n$ and $\lambda$. The extra power retains the input sampler's degree; fixing $\mu$ in compression leaves a polynomial bound. Its threshold $C_{\mathrm{ar}}$ plays the role of the source threshold (`thm:ar` in `ld_compiler.tex`); an earlier statement here had the value clauses for all $n$. Its soundness field also explicitly requires $n\geq2$, $\lambda\geq1$ and $\varepsilon>0$. Completeness transfers ambient `HasPerfectPCC` from input answer cut $2^{(\lambda n+1)^\mu}$ to the output budget's answer cut, for $\lambda,\mu\geq1$: the source's regime, and the one in which $(\lambda n+1)^\mu\geq n+1$, which the PCP's validity hypothesis $2\lceil\log n\rceil\leq T$ needs. At $\lambda=0$ or $\mu=0$ the PCP's time bound is a constant and the clause would be false for large $n$; compression's $\lambda$ is at least $2$ and its $\mu$ at least $1$ (Lemma [Answer-reduction completeness](../part-08/lem-ar-completeness.md)). Soundness transfers output value greater than $1-\varepsilon$ to input value at least $1-\delta(\varepsilon,n)$ at those cuts, with $\delta(\varepsilon,n)=\sigma^a((\lambda n)^{\mu a}\varepsilon^b+(\lambda n)^{-\mu b})$, $a\geq1$ and $0\lt b\leq1$. Sampler and decider descriptions are computable in polynomial time; the sampler depends only on the input sampler and the parameters. The composition consumes an instance at $\ell=5$, which Lemma [Supplying ambient answer reduction](lem-answer-reduction-supply.md) constructs.

## Depends on

- [Normal form verifier in the ambient model](../../foundations/part-03/def-normal-verifier.md)
- [PCC strategy](../../foundations/part-01/def-pcc.md)
- [Synchronous value](../../foundations/part-01/def-sync-value.md)
- [Quantum value](../../foundations/part-01/def-q-value.md)

## Lean

Formalized as [`MIPRE.AnswerReduction`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.AnswerReduction).

## Sources

- [MIP* = RE blueprint: content/06_proof_structure.tex, line 6065](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/06_proof_structure.tex#L6065)
