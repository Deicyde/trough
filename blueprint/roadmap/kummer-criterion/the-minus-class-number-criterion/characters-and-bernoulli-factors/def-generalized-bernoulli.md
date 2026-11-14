---
declaration: definition
origin: cited
lean: KummerCriterion.BernoulliGen
statement: formalized
---

# generalized-bernoulli

For a Dirichlet character $\chi$ modulo $N$ and $n \ge 0$, the *generalised Bernoulli number* is

$$
B_{n,\chi}
\;=\;
N^{\,n-1} \sum_{a \bmod N} \chi(a)\, B_n\!\left(\frac{a}{N}\right),
$$

where $B_n(X)$ is the $n$th Bernoulli polynomial. For nontrivial $\chi$ the case $n = 1$ simplifies to

$$
B_{1,\chi} = \frac{1}{N}\sum_{a=1}^{N} \chi(a)\,a ,
$$

because $\sum_a \chi(a) = 0$ kills the constant term of $B_1(X) = X - \tfrac12$. The class-number formula only uses the values $B_{1,\chi^{-1}}$ for odd $\chi$.

## Depends on

- [dirichlet-character](def-dirichlet-character.md)

## Lean

Formalized as [`KummerCriterion.BernoulliGen`](https://riccardobrasca.github.io/KummerCriterion/docs/find/#doc/KummerCriterion.BernoulliGen).

## Sources

- [Kummer's criterion blueprint: subsections/hminus-formula.tex, line 26](https://github.com/riccardobrasca/KummerCriterion/blob/b96b2cde81e799bfe8364b6dd469abafd9a26bdf/blueprint/src/subsections/hminus-formula.tex#L26)
