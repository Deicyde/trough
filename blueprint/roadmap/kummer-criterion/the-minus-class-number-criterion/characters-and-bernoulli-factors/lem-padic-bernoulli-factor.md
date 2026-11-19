---
declaration: lemma
origin: cited
lean: KummerCriterion.exists_padicInt_bernoulli_factor
statement: formalized
proof: formalized
---

# padic-bernoulli-factor

For $0\lt n\lt p-1$, the quotient $B_n/n$ lies in $\mathbb{Z}_p$, and it is a $p$-adic unit if and only if $p$ does not divide the numerator of $B_n$.

## Depends on

- [bernoulli-den-coprime](thm-bernoulli-den-coprime.md)

## Proof

The denominator of $B_n$ is prime to $p$ by [Theorem bernoulli-den-coprime](thm-bernoulli-den-coprime.md), and $n < p-1 < p$ is also prime to $p$, so $B_n/n \in \mathbb{Z}_p$. In $\mathbb{Z}_p$ the non-units are exactly the elements of $p\mathbb{Z}_p$; since the denominator and $n$ are $p$-adic units, $B_n/n \in p\mathbb{Z}_p$ holds precisely when $p$ divides the numerator of $B_n$.

## Lean

Formalized as [`KummerCriterion.exists_padicInt_bernoulli_factor`](https://riccardobrasca.github.io/KummerCriterion/docs/find/#doc/KummerCriterion.exists_padicInt_bernoulli_factor).

## Sources

- [Kummer's criterion blueprint: subsections/hminus-formula.tex, line 84](https://github.com/riccardobrasca/KummerCriterion/blob/b96b2cde81e799bfe8364b6dd469abafd9a26bdf/blueprint/src/subsections/hminus-formula.tex#L84)
