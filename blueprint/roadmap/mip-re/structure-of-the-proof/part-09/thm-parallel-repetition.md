---
declaration: theorem
origin: cited
lean: MIPRE.Repetition, MIPRE.Repetition.soundBound, MIPRE.repetition
statement: formalized
proof: formalized
---

# Parallel repetition of normal form verifiers

There are a universal constant $c > 0$ and a polynomial-time Turing machine ${\mathsf{ComputeRepeatedVerifier}}$ that on input $(\mathsf{V}, \ell, \lambda, \tau, \beta)$, for $\mathsf{V}$ an $\ell$-level normal form verifier, outputs an $\ell$-level normal form verifier $\mathsf{V}^{\textsc{Rep}}$ whose game $\mathsf{V}^{\textsc{Rep}}_n$ is the $k(n)$-fold direct repetition (Definition [Direct repetition](../../parallel-repetition/def-direct-repetition.md)) of $\mathsf{V}_n$ with answers of length at most $B(n) = 2^{\beta(|\lambda| + |n|)}$, with $|\cdot|$ the bit length — up to the encoding of answer tuples as strings, the decider parsing a self-delimiting $k(n)$-tuple, each coordinate against $B(n)$, and rejecting malformed answers — with $k(n) = 2^{\tau(|\lambda| + |n|)}$, $\mathsf{TIME}_{\mathcal{S}^{\textsc{Rep}}}(n) = \mathrm{poly}\bigl(k(n), \mathsf{TIME}_\mathcal{S}(n)\bigr)$ and $\mathsf{TIME}_{\mathcal{D}^{\textsc{Rep}}}(n) = \mathrm{poly}\bigl(k(n), B(n), \mathsf{TIME}_\mathcal{D}(n), \left\vert {\mathsf{V}} \right\vert\bigr)$, the sampler of $\mathsf{V}^{\textsc{Rep}}$ depending only on $(\mathcal{S}, \lambda, \ell, \tau)$, and for all $n$:

1. (**Completeness**) If $\mathsf{V}_n$ has a value-$1$ PCC strategy, then $\mathsf{V}^{\textsc{Rep}}_n$ has a value-$1$ PCC strategy.

2. (**Soundness**) For all $0 < \varepsilon \leq 1$, if $\mathrm{val}^*(\mathsf{V}_n) \leq 1 - \varepsilon$ then

    $$
    \mathrm{val}^*(\mathsf{V}^{\textsc{Rep}}_n) \;\leq\; \exp\Bigl( - \frac{c\, \varepsilon^{13}\, k(n)}{B(n) + 1} \Bigr)\;.
    $$

## Depends on

- [Normal form verifier in the ambient model](../../foundations/part-03/def-normal-verifier.md)
- [PCC strategy](../../foundations/part-01/def-pcc.md)
- [Direct repetition](../../parallel-repetition/def-direct-repetition.md)
- [Direct parallel repetition for entangled strategies](../../parallel-repetition/thm-direct-repetition-q.md)
- [Tensor powers of synchronous strategies](../../parallel-repetition/lem-tensor-power-pcc.md)
- [The repetition bound for answers of bounded length](../../parallel-repetition/lem-repetition-sound-bound.md)

## Proof depends on

- [Direct sums of families, and their distributions](../part-01/lem-cl-famsum.md)
- [Efficient s-m-n](../../computability/lem-smn.md)
- [Value models](../../downstream-results/part-01/def-value-model.md)

## Proof

The game $\mathsf{V}^{\textsc{Rep}}_n$ is $\mathsf{V}_n^{k(n)}$ at the truncated alphabet: its sampler runs $k(n)$ independent copies of $\mathcal{S}$ (a product of conditionally linear functions of the same level) and its decider runs $\mathcal{D}$ on every coordinate. Completeness: the $k(n)$-fold tensor power of a value-$1$ PCC strategy is a value-$1$ PCC strategy for the repeated game. Soundness is a direct application of Theorem [Direct parallel repetition for entangled strategies](../../parallel-repetition/thm-direct-repetition-q.md): the hypothesis is already a $\mathrm{val}^*$ bound, so nothing has to be transported first. That theorem bounds $\mathrm{val}^*(\mathsf{V}_n^{k(n)})$ by $\exp\bigl( -c\, k(n)\, \varepsilon^{13} / (\varepsilon + \log(\left\vert {{\mathcal{A}}} \right\vert\left\vert {{\mathcal{B}}} \right\vert)) \bigr)$, and the answer alphabets are the strings of length at most $B(n)$, so $\log(\left\vert {{\mathcal{A}}} \right\vert\left\vert {{\mathcal{B}}} \right\vert) \leq 2(B(n) + 1)$ and the denominator is at most $3(B(n) + 1)$, the factor absorbed into $c$. The exponent $13$ is the one of Theorem [Direct parallel repetition for entangled strategies](../../parallel-repetition/thm-direct-repetition-q.md) itself, with no further loss: carrying the hypothesis in $\mathrm{val}^*$ rather than ${\mathrm{val}^{s}}$ removes both the transport's polynomial loss and the factor $\kappa^{13}$ that its diagonal-weight hypothesis used to contribute. The conclusion is in $\mathrm{val}^*$, as is the hypothesis: that is the form Definition [The computable class](../../foundations/part-03/def-mipstar-computable.md) asks of the final game, and it is available at every step because nothing in the chain ever leaves $\mathrm{val}^*$ (Remark [Why the pipeline is bipartite throughout](../README.md)). In (JNVWY20) the answer length is the timeout bound $B_\mathcal{D}(n)$ read off the decider and $\tau$ is chosen against it; the ambient model has no timeout-counter form, so the parse length is the explicit parameter $\beta$, and the choice of $\tau$ against it is Lemma [A universal repetition exponent](lem-compress-tau.md). The counts are powers of two rather than the paper's $(\lambda n)^\tau$ because a program of the ambient model writes $2^{\tau(|\lambda| + |n|)}$ down by a walk over the bits of $\lambda$ and $n$, where $(\lambda n)^\tau$ would need multiplication; $(\lambda n + 1)^\tau \leq 2^{\tau(|\lambda| + |n|)} \leq (\lambda n + 1)^{6\tau}$ for $\lambda, n \geq 1$, so nothing downstream can tell the difference.

## Lean

Formalized as [`MIPRE.Repetition`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Repetition), [`MIPRE.Repetition.soundBound`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Repetition.soundBound), [`MIPRE.repetition`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.repetition).

## Sources

- [MIP* = RE blueprint: content/06_proof_structure.tex, line 6183](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/06_proof_structure.tex#L6183)
