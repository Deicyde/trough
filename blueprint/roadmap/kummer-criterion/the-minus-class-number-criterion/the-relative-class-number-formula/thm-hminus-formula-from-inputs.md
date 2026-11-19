---
declaration: theorem
origin: cited
lean: KummerCriterion.hMinus_formula_of_residue_and_hPlus_cyclotomic_and_gauss
statement: formalized
proof: formalized
---

# hminus-formula-from-inputs

Assume the factorisation of the Dedekind zeta residue of $K$ into the even and odd $L$-value products, the $h^+$ formula of [Theorem hplus-even-lvalues](thm-hplus-even-lvalues.md), and the packaged Gauss-product identity. Then

$$
h^-(K)
=
2p\prod_{\chi\ \mathrm{odd}}
\left(-\frac12 B_{1,\chi^{-1}}\right).
$$

## Depends on

- [class-number-hminus](../../class-numbers-of-the-cyclotomic-cm-field/the-relative-class-number/def-class-number-hminus.md)
- [generalized-bernoulli](../characters-and-bernoulli-factors/def-generalized-bernoulli.md)
- [hplus-even-lvalues](thm-hplus-even-lvalues.md)
- [cyclotomic-gauss-goal](thm-cyclotomic-gauss-goal.md)

## Proof

Divide the analytic class-number formula of $K$ (in residue form) by that of $K^+$. Using $h = h^+ h^-$, the quotient expresses $h^-$ times the ratio of the analytic constants as the product of the odd $L$-values $L(1,\chi)$. Substituting the odd $L$-value formula

$$
L(1,\chi) = \frac{\pi i\,\tau(\chi)}{p}\,B_{1,\chi^{-1}}
$$

for each odd $\chi$ and cancelling the powers of $\pi$, $i$ and the Gauss sums against the analytic constants — this is exactly what the packaged Gauss-product identity provides — leaves the displayed product of generalised Bernoulli factors with the prefactor $2p$.

## Lean

Formalized as [`KummerCriterion.hMinus_formula_of_residue_and_hPlus_cyclotomic_and_gauss`](https://riccardobrasca.github.io/KummerCriterion/docs/find/#doc/KummerCriterion.hMinus_formula_of_residue_and_hPlus_cyclotomic_and_gauss).

## Sources

- [Kummer's criterion blueprint: subsections/hminus-formula.tex, line 184](https://github.com/riccardobrasca/KummerCriterion/blob/b96b2cde81e799bfe8364b6dd469abafd9a26bdf/blueprint/src/subsections/hminus-formula.tex#L184)
