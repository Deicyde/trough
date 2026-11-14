---
declaration: theorem
origin: cited
lean: MIPRE.AnswerReduction.answerReduction
statement: formalized
proof: formalized
---

# Answer reduction

In the source model there is a polynomial-time Turing machine ${\mathsf{ComputeAnsRedVerifier}}$ that on input $(\mathsf{V}, \lambda, \ell, \mu, \sigma)$, for $\mathsf{V}$ an $\ell$-level normal form verifier whose decider is in standard timeout-counter form, with $\left\vert {\mathcal{D}} \right\vert \leq \sigma$, $\mathsf{TIME}_\mathcal{S}(n) \leq (\lambda n)^\mu$ and $\mathsf{TIME}_\mathcal{D}(n) \leq (2^{\lambda n})^\mu$ for $n \geq 2$, outputs a $\max\{\ell + 2, 5\}$-level normal form verifier $\mathsf{V}^{\mathsf{ar}}$ whose decider is in standard timeout-counter form with $B_{\mathcal{D}^{\mathsf{ar}}}(n)=\mathrm{poly}(\sigma,(\lambda n)^\mu)$, with $\mathsf{TIME}_{\mathcal{S}^{\mathsf{ar}}}(n), \mathsf{TIME}_{\mathcal{D}^{\mathsf{ar}}}(n) = \mathrm{poly}\bigl( (\lambda n)^\mu, \sigma \bigr)$, whose sampler depends only on $(\mathcal{S}, \lambda, \ell, \mu, \sigma)$, and such that for some $\delta(\varepsilon, n) = \sigma^a \bigl( (\lambda n)^{\mu a} \varepsilon^b + (\lambda n)^{-\mu b} \bigr)$ (universal constants $a, b$) and a universal constant $C_{\mathrm{ar}}$, for all $n \geq C_{\mathrm{ar}}$:

1. (**Completeness**) If $\mathsf{V}_n$ has a value-$1$ PCC strategy then $\mathsf{V}^{\mathsf{ar}}_n$ has a value-$1$ PCC strategy.
2. (**Soundness**) If $\mathrm{val}^*(\mathsf{V}^{\mathsf{ar}}_n) > 1 - \varepsilon$ then $\mathrm{val}^*(\mathsf{V}_n) \geq 1 - \delta(\varepsilon, n)$.

## Depends on

- [Normal form verifier in the ambient model](../../foundations/part-03/def-normal-verifier.md)
- [PCC strategy](../../foundations/part-01/def-pcc.md)
- [Answer-reduction construction](../part-08/lem-ar-construction.md)
- [Answer-reduction completeness](../part-08/lem-ar-completeness.md)
- [Answer-reduction quantitative assembly](../part-08/lem-ar-error-assembly.md)

## Proof depends on

- [Supplying ambient answer reduction](lem-answer-reduction-supply.md)
- [Ambient answer-reduction contract](def-answer-reduction-contract.md)
- [PCP complexity](../part-08/lem-pcp-complexity.md)

## Proof

In the ambient form of Definition [Ambient answer-reduction contract](def-answer-reduction-contract.md), at $\ell=5$, this is Lemma [Supplying ambient answer reduction](lem-answer-reduction-supply.md).

## Lean

Formalized as [`MIPRE.AnswerReduction.answerReduction`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.AnswerReduction.answerReduction).

## Sources

- [MIP* = RE blueprint: content/06_proof_structure.tex, line 6032](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/06_proof_structure.tex#L6032)
