---
declaration: lemma
origin: cited
lean: MIPRE.Pipeline.eps1, MIPRE.Pipeline.intro_margin, MIPRE.Pipeline.exists_mu, MIPRE.Pipeline.eps2, MIPRE.Pipeline.ar_margin
statement: formalized
proof: formalized
---

# The margin claim

Given the ambient contracts of Definitions [Ambient introspection contract](../part-06/def-introspection-contract.md) and [Ambient answer-reduction contract](def-answer-reduction-contract.md), write $(a_1,b_1)$ and $(a_2,b_2)$ for their respective soundness constants, with $a_1,a_2\geq1$, and $x = \lambda n$. Put $\varepsilon_1 = \bigl( 8 a_1 x^{a_1} \bigr)^{-1/b_1}$.

1. $\delta_1(\varepsilon_1, n) < \frac12$ for all $x \geq (4 a_1)^{1/b_1}$.

2. For every $K$ and $C$ there are a universal $\mu \geq C$ and a threshold $N$ such that, for all $x \geq N$ and all $1 \leq \sigma \leq x^K$,

    $$
    \sigma^{a_2} x^{-b_2 \mu} \;\lt \; \frac{\varepsilon_1}{2}\;;
    $$

    and then, with $\varepsilon_2 = \bigl( \varepsilon_1 / (3 \sigma^{a_2} x^{\mu a_2}) \bigr)^{1/b_2}$, $\delta_2(\varepsilon_2, n) < \varepsilon_1$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof

The first term of $\delta_1(\varepsilon_1, n)$ is exactly $\frac18$ and the second is at most $\frac14$ once $x^{b_1} \geq 4 a_1$. For the second item take $\mu$ with $\mu b_2 \geq K a_2 + a_1 / b_1 + 1$: then $\sigma^{a_2} x^{-b_2 \mu} \leq x^{-a_1/b_1 - 1}$, which is below $\varepsilon_1 / 2 = (8 a_1)^{-1/b_1} x^{-a_1/b_1} / 2$ as soon as $x > 2 (8 a_1)^{1/b_1}$; and the first term of $\delta_2(\varepsilon_2, n)$ is exactly $\varepsilon_1 / 3$. The paper fixes $\sigma = \lceil C_{\mathrm{intro}} \lambda^{C_{\mathrm{intro}}} \rceil$ and $\mu = \lceil \max\{ C_{\mathrm{intro}}, (9 a_1 + 2 a_2 C_{\mathrm{intro}}) / (b_1 b_2) \} \rceil$ and has the bound for all $n \geq 2$; the formalization takes $\sigma$ any polynomial in $\lambda$ dominating $C_{\mathrm{intro}} (\lambda + 1)^{C_{\mathrm{intro}}}$ and the size of the introspective sampler, hence $\sigma \leq x^K$ for a universal $K$, and a threshold on $n$ that $C_0$ absorbs.

## Lean

Formalized as [`MIPRE.Pipeline.eps1`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Pipeline.eps1), [`MIPRE.Pipeline.intro_margin`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Pipeline.intro_margin), [`MIPRE.Pipeline.exists_mu`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Pipeline.exists_mu), [`MIPRE.Pipeline.eps2`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Pipeline.eps2), [`MIPRE.Pipeline.ar_margin`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Pipeline.ar_margin).

## Sources

- [MIP* = RE blueprint: content/06_proof_structure.tex, line 6477](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/06_proof_structure.tex#L6477)
