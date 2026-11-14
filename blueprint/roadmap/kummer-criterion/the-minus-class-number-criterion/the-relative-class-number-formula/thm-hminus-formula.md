---
declaration: theorem
origin: cited
lean: KummerCriterion.hMinus_formula
statement: formalized
proof: formalized
---

# hminus-formula

For an odd prime cyclotomic field,

$$
h^-(K)
=
2p\prod_{\chi\ \mathrm{odd}}
\left(-\frac12 B_{1,\chi^{-1}}\right).
$$

## Depends on

- [hminus-formula-from-inputs](thm-hminus-formula-from-inputs.md)
- [hplus-even-lvalues](thm-hplus-even-lvalues.md)
- [cyclotomic-gauss-goal](thm-cyclotomic-gauss-goal.md)

## Proof

Supply the three inputs of [Theorem hminus-formula-from-inputs](thm-hminus-formula-from-inputs.md): the residue of $\zeta_K$ factors over the nontrivial characters into the even and odd $L$-value products; the even product is converted by [Theorem hplus-even-lvalues](thm-hplus-even-lvalues.md); and the Gauss hypothesis is [Theorem cyclotomic-gauss-goal](thm-cyclotomic-gauss-goal.md).

## Lean

Formalized as [`KummerCriterion.hMinus_formula`](https://riccardobrasca.github.io/KummerCriterion/docs/find/#doc/KummerCriterion.hMinus_formula).

## Sources

- [Kummer's criterion blueprint: subsections/hminus-formula.tex, line 213](https://github.com/riccardobrasca/KummerCriterion/blob/b96b2cde81e799bfe8364b6dd469abafd9a26bdf/blueprint/src/subsections/hminus-formula.tex#L213)
