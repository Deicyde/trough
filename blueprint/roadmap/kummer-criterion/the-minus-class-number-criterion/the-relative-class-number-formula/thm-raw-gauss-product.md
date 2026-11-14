---
declaration: theorem
origin: cited
lean: KummerCriterion.rawGaussProduct
statement: formalized
proof: formalized
---

# raw-gauss-product

The product of the Gauss sums over the odd characters modulo $p$ is

$$
\prod_{\chi\ \mathrm{odd}} \tau(\chi)
\;=\;
i^{\,(p-1)/2}\,\sqrt{p^{\,(p-1)/2}} .
$$

## Depends on

- [dirichlet-character](../characters-and-bernoulli-factors/def-dirichlet-character.md)

## Proof

The proof splits into the cases $p\equiv1\pmod4$ and $p\equiv3\pmod4$. A non-quadratic odd character $\chi$ is paired with its distinct inverse $\chi^{-1}$ (also odd), and the identity $\tau(\chi)\tau(\chi^{-1}) = \chi(-1)\,p = -p$ evaluates each pair. When $p \equiv 3 \pmod 4$ the quadratic character is odd and unpaired; it contributes the classical quadratic Gauss sum $i\sqrt p$. Counting pairs in the two cases and collecting signs and powers of $i$ gives the stated value.

## Lean

Formalized as [`KummerCriterion.rawGaussProduct`](https://riccardobrasca.github.io/KummerCriterion/docs/find/#doc/KummerCriterion.rawGaussProduct).

## Sources

- [Kummer's criterion blueprint: subsections/hminus-formula.tex, line 149](https://github.com/riccardobrasca/KummerCriterion/blob/b96b2cde81e799bfe8364b6dd469abafd9a26bdf/blueprint/src/subsections/hminus-formula.tex#L149)
