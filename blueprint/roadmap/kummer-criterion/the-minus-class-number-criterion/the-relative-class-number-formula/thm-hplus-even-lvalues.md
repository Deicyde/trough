---
declaration: theorem
origin: cited
lean: KummerCriterion.hPlus_formula_of_evenLValues
statement: formalized
proof: formalized
---

# hplus-even-lvalues

The plus class number is given by the even part of the cyclotomic $L$-value product:

$$
h^+(K)=
c_{K^+}
\prod_{\substack{\chi\ \mathrm{even}\\ \chi\ne1}}
\left(
-\,\tau(\chi^{-1})^{-1}
\sum_{a \bmod p} \chi^{-1}(a)\,
\log\bigl|1-e^{2\pi i a/p}\bigr|
\right),
$$

where each factor of the product equals $L(1,\chi)$ and $c_{K^+}$ is the explicit constant of the analytic class-number formula of $K^+$ (built from the discriminant, the regulator and the roots of unity of $K^+$).

## Depends on

- [dirichlet-character](../characters-and-bernoulli-factors/def-dirichlet-character.md)
- [class-number-hplus](../../class-numbers-of-the-cyclotomic-cm-field/the-real-subfield-and-the-class-numbers/def-class-number-hplus.md)

## Proof

The analytic class-number formula for the totally real field $K^+$ expresses $h^+$ through the residue of the Dedekind zeta function $\zeta_{K^+}$. Factoring $\zeta_{K^+}(s) = \zeta(s)\prod_{\chi \text{ even},\ \chi\ne1} L(s,\chi)$ over the even characters and inserting the classical evaluation of $L(1,\chi)$ for even primitive $\chi$ — the displayed Gauss-sum-and-logarithm expression — gives the formula.

## Lean

Formalized as [`KummerCriterion.hPlus_formula_of_evenLValues`](https://riccardobrasca.github.io/KummerCriterion/docs/find/#doc/KummerCriterion.hPlus_formula_of_evenLValues).

## Sources

- [Kummer's criterion blueprint: subsections/hminus-formula.tex, line 121](https://github.com/riccardobrasca/KummerCriterion/blob/b96b2cde81e799bfe8364b6dd469abafd9a26bdf/blueprint/src/subsections/hminus-formula.tex#L121)
