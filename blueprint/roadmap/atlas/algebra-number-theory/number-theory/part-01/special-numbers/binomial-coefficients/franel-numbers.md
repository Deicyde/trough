---
declaration: section
origin: cited
lean: MathlibExt.NumberTheory.OeisA265233Wanted.a265233, MathlibExt.NumberTheory.OeisA265233Wanted.a265233_eq_sum_franel, MathlibExt.NumberTheory.OeisA265233Wanted.coeff_pow_eq_franel, MathlibExt.NumberTheory.OeisA265233Wanted.tsum_a265233_eq, MathlibExt.NumberTheory.OeisA265233Wanted.a265233_isEquivalent
statement: formalized
---

# Franel numbers

5 results, 1 proved and 4 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/binomial-coefficients/franel-numbers/index.html).

## The sequence A265233

The sequence $(a_n)_{n \ge 0}$ of rational numbers is given by
$a_0 = 1$, $a_1 = 1$, $a_2 = 7$, $a_3 = 56$ and, for every integer $N \ge 4$,

$$N^2 a_N = (19N^2 - 19N + 6)\, a_{N-1} - 96 (N-1)^2 a_{N-2} + 144 (N-1)(N-2)\, a_{N-3}.$$

## Sources

- Juntao Jin, "An Explicit Formula and a Recurrence for OEIS A265233", Theorem 1(2).

Formalized by `MathlibExt.NumberTheory.OeisA265233Wanted.a265233`, a definition declared in [WantedExt/NumberTheory/OeisA265233Wanted.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/OeisA265233Wanted.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/binomial-coefficients/franel-numbers/index.html#a265233).

## Explicit formula for A265233 in terms of Franel numbers

Let $(a_n)_{n \ge 0}$ be the
sequence A265233 and let $f_m = \sum_{k=0}^{m} \binom{m}{k}^3$ be the $m$-th Franel number. For
every integer $n \ge 1$,

$$a_n = \frac{1}{6} \sum_{m=0}^{n} \binom{n}{m} 4^{n-m} f_m.$$

## Sources

- Juntao Jin, "An Explicit Formula and a Recurrence for OEIS A265233", Theorem 1.

Stated but not proved: `MathlibExt.NumberTheory.OeisA265233Wanted.a265233_eq_sum_franel` is written with `theorem_wanted` in [WantedExt/NumberTheory/OeisA265233Wanted.lean, line 81](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/OeisA265233Wanted.lean#L81). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/binomial-coefficients/franel-numbers/index.html#a265233-eq-sum-franel).

## Franel numbers as diagonal coefficients

For every natural number $m$, the coefficient of
$x^m y^m z^m$ in the polynomial $\bigl((x + y)(y + z)(z + x)\bigr)^m \in \mathbb{Q}[x, y, z]$
is the Franel number $f_m = \sum_{k=0}^{m} \binom{m}{k}^3$.

## Sources

- Juntao Jin, "An Explicit Formula and a Recurrence for OEIS A265233", Lemma 3.

Stated but not proved: `MathlibExt.NumberTheory.OeisA265233Wanted.coeff_pow_eq_franel` is written with `theorem_wanted` in [WantedExt/NumberTheory/OeisA265233Wanted.lean, line 93](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/OeisA265233Wanted.lean#L93). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/binomial-coefficients/franel-numbers/index.html#coeff-pow-eq-franel).

## Generating function of A265233

Let $(a_n)_{n \ge 0}$ be the sequence A265233 and let
${}_2F_1$ be the Gauss hypergeometric function. For every real number $x$ with $|x| < 1/12$ and
$|27x(1 - 4x)^2| < 1$,

$$\sum_{n \ge 0} a_n x^n = \frac{{}_2F_1\bigl(\tfrac13, \tfrac23; 1; 27x(1 - 4x)^2\bigr) + 5}{6}.$$

## Sources

- Juntao Jin, "An Explicit Formula and a Recurrence for OEIS A265233", Corollary 2.

Stated but not proved: `MathlibExt.NumberTheory.OeisA265233Wanted.tsum_a265233_eq` is written with `theorem_wanted` in [WantedExt/NumberTheory/OeisA265233Wanted.lean, line 110](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/OeisA265233Wanted.lean#L110). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/binomial-coefficients/franel-numbers/index.html#tsum-a265233-eq).

## Asymptotics of A265233

The sequence $(a_n)_{n \ge 0}$ A265233 satisfies

$$a_n \sim \frac{\sqrt{3}}{6\pi} \cdot \frac{12^n}{n} \quad \text{as } n \to \infty.$$

## Sources

- Juntao Jin, "An Explicit Formula and a Recurrence for OEIS A265233", Corollary 2.

Stated but not proved: `MathlibExt.NumberTheory.OeisA265233Wanted.a265233_isEquivalent` is written with `theorem_wanted` in [WantedExt/NumberTheory/OeisA265233Wanted.lean, line 121](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/OeisA265233Wanted.lean#L121). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/binomial-coefficients/franel-numbers/index.html#a265233-is-equivalent).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Franel numbers](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/binomial-coefficients/franel-numbers/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/special-numbers/binomial-coefficients/franel-numbers)
