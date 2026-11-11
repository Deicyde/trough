---
declaration: section
origin: cited
lean: MetaMathlibExt.centralBinom_add_eq_centralBinom_mul_choose_iff, MetaMathlibExt.centralBinom_add_le_centralBinom_mul_choose_of_le, MetaMathlibExt.centralBinom_add_eq_centralBinom_mul_choose_iff_of_le_ten, MetaMathlibExt.centralBinom_add_ne_centralBinom_mul_choose_sub_one, MetaMathlibExt.centralBinom_add_ne_centralBinom_mul_choose_sub_two, MetaMathlibExt.centralBinom_add_ne_centralBinom_mul_choose_sub_three, MetaMathlibExt.exists_prime_dvd_prod_consecutive_gt_three_halves_iff, MetaMathlibExt.choose_mul_mul_bounds
statement: formalized
---

# Equations in central binomial coefficients

17 results, 17 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/binomial-coefficients/equations-in-central-binomial-coefficients/index.html).

## Allen's theorem on central binomial products

Let $x$ and $b$ be positive integers and
let $a$ be a nonnegative integer. Then $\binom{2(a+b)}{a+b} = \binom{2a}{a}\binom{x+2b}{b}$ if
and only if $x = 1$ and $a = 1$.

## Sources

- Meaghan Allen, *Solvability of $\binom{2k}{k} = \binom{2a}{a}\binom{x+2b}{b}$*, INTEGERS 26 (2026), Article A26, Theorem 1.

Stated but not proved: `MetaMathlibExt.centralBinom_add_eq_centralBinom_mul_choose_iff` is written with `theorem_wanted` in [WantedExt/NumberTheory/CentralBinomProductEquationWanted.lean, line 37](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/CentralBinomProductEquationWanted.lean#L37). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/binomial-coefficients/equations-in-central-binomial-coefficients/index.html#central-binom-add-eq-central-binom-mul-c).

## Allen's inequality for central binomial products

Let $x$ and $b$ be positive integers
and let $a$ be a nonnegative integer with $a \le x$. Then
$\binom{2(a+b)}{a+b} \le \binom{2a}{a}\binom{x+2b}{b}$, and equality holds if and only if
$x = 1$ and $a = 1$.

## Sources

- Meaghan Allen, *Solvability of $\binom{2k}{k} = \binom{2a}{a}\binom{x+2b}{b}$*, INTEGERS 26 (2026), Article A26, Proposition 1.

Stated but not proved: `MetaMathlibExt.centralBinom_add_le_centralBinom_mul_choose_of_le` is written with `theorem_wanted` in [WantedExt/NumberTheory/CentralBinomProductEquationWanted.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/CentralBinomProductEquationWanted.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/binomial-coefficients/equations-in-central-binomial-coefficients/index.html#central-binom-add-le-central-binom-mul-c).

## Central binomial products with $a + b \le 10$

Let $x$, $a$, $b$ be positive integers
with $a + b \le 10$. Then $\binom{2(a+b)}{a+b} = \binom{2a}{a}\binom{x+2b}{b}$ if and only if
$x = 1$ and $a = 1$.

## Sources

- Meaghan Allen, *Solvability of $\binom{2k}{k} = \binom{2a}{a}\binom{x+2b}{b}$*, INTEGERS 26 (2026), Article A26, Lemma 1.

Stated but not proved: `MetaMathlibExt.centralBinom_add_eq_centralBinom_mul_choose_iff_of_le_ten` is written with `theorem_wanted` in [WantedExt/NumberTheory/CentralBinomProductEquationWanted.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/CentralBinomProductEquationWanted.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/binomial-coefficients/equations-in-central-binomial-coefficients/index.html#central-binom-add-eq-central-binom-mul-c-2).

## Central binomial products in the case $x = a - 1$

Let $a$ and $b$ be natural numbers
with $4 < 2a \le a + b$. Then $\binom{2(a+b)}{a+b} \ne \binom{2a}{a}\binom{a+2b-1}{b}$, so the
equation $\binom{2(a+b)}{a+b} = \binom{2a}{a}\binom{x+2b}{b}$ has no solution with $x = a - 1$.

## Sources

- Meaghan Allen, *Solvability of $\binom{2k}{k} = \binom{2a}{a}\binom{x+2b}{b}$*, INTEGERS 26 (2026), Article A26, Lemma 2.

Stated but not proved: `MetaMathlibExt.centralBinom_add_ne_centralBinom_mul_choose_sub_one` is written with `theorem_wanted` in [WantedExt/NumberTheory/CentralBinomProductEquationWanted.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/CentralBinomProductEquationWanted.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/binomial-coefficients/equations-in-central-binomial-coefficients/index.html#central-binom-add-ne-central-binom-mul-c).

## Central binomial products in the case $x = a - 2$

Let $a$ and $b$ be natural numbers
with $4 < 2a \le a + b$. Then $\binom{2(a+b)}{a+b} \ne \binom{2a}{a}\binom{a+2b-2}{b}$, so the
equation $\binom{2(a+b)}{a+b} = \binom{2a}{a}\binom{x+2b}{b}$ has no solution with $x = a - 2$.

## Sources

- Meaghan Allen, *Solvability of $\binom{2k}{k} = \binom{2a}{a}\binom{x+2b}{b}$*, INTEGERS 26 (2026), Article A26, Lemma 3.

Stated but not proved: `MetaMathlibExt.centralBinom_add_ne_centralBinom_mul_choose_sub_two` is written with `theorem_wanted` in [WantedExt/NumberTheory/CentralBinomProductEquationWanted.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/CentralBinomProductEquationWanted.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/binomial-coefficients/equations-in-central-binomial-coefficients/index.html#central-binom-add-ne-central-binom-mul-c-2).

## Central binomial products in the case $x = a - 3$

Let $a$ and $b$ be natural numbers
with $4 < 2a \le a + b$. Then $\binom{2(a+b)}{a+b} \ne \binom{2a}{a}\binom{a+2b-3}{b}$, so the
equation $\binom{2(a+b)}{a+b} = \binom{2a}{a}\binom{x+2b}{b}$ has no solution with $x = a - 3$.

## Sources

- Meaghan Allen, *Solvability of $\binom{2k}{k} = \binom{2a}{a}\binom{x+2b}{b}$*, INTEGERS 26 (2026), Article A26, Lemma 4.

Stated but not proved: `MetaMathlibExt.centralBinom_add_ne_centralBinom_mul_choose_sub_three` is written with `theorem_wanted` in [WantedExt/NumberTheory/CentralBinomProductEquationWanted.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/CentralBinomProductEquationWanted.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/binomial-coefficients/equations-in-central-binomial-coefficients/index.html#central-binom-add-ne-central-binom-mul-c-3).

## Hanson's theorem on a prime factor above $3m/2$ in consecutive integers

Let $m$ and $n$
be natural numbers with $0 < m < n$. The product $n(n+1)\cdots(n+m-1)$ has a prime divisor $p$
with $p > 3m/2$ if and only if $(n, m)$ is none of the pairs $(3, 2)$, $(8, 2)$ and $(6, 5)$
(the products $3 \cdot 4$, $8 \cdot 9$ and $6 \cdot 7 \cdot 8 \cdot 9 \cdot 10$).

## Sources

- Meaghan Allen, *Solvability of $\binom{2k}{k} = \binom{2a}{a}\binom{x+2b}{b}$*, INTEGERS 26 (2026), Article A26, Lemma 5, quoting Hanson.

Stated but not proved: `MetaMathlibExt.exists_prime_dvd_prod_consecutive_gt_three_halves_iff` is written with `theorem_wanted` in [WantedExt/NumberTheory/CentralBinomProductEquationWanted.lean, line 93](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/CentralBinomProductEquationWanted.lean#L93). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/binomial-coefficients/equations-in-central-binomial-coefficients/index.html#exists-prime-dvd-prod-consecutive-gt-thr).

## Stănică's bounds for the binomial coefficient $\binom{mn}{rn}$

Let $m$, $n$ and $r$ be
natural numbers with $1 \le r < m$ and $n \ge 1$, and put

$$B = \frac{m^{mn + 1/2}}{(m-r)^{(m-r)n + 1/2}\, r^{rn + 1/2}}.$$

Then

$$\frac{e^{-1/(8n)}}{\sqrt{2\pi}\,\sqrt{n}}\, B < \binom{mn}{rn} <
\frac{1}{\sqrt{2\pi}\,\sqrt{n}}\, B.$$

## Sources

- Meaghan Allen, *Solvability of $\binom{2k}{k} = \binom{2a}{a}\binom{x+2b}{b}$*, INTEGERS 26 (2026), Article A26, Lemma 6, quoting Stănică.

Stated but not proved: `MetaMathlibExt.choose_mul_mul_bounds` is written with `theorem_wanted` in [WantedExt/NumberTheory/CentralBinomProductEquationWanted.lean, line 104](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/CentralBinomProductEquationWanted.lean#L104). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/binomial-coefficients/equations-in-central-binomial-coefficients/index.html#choose-mul-mul-bounds).

## Central binomial products with $a \ge b \ge 3$

Let $x$, $a$, $b$ be natural numbers with
$x \ge 1$ and $3 \le b \le a$. Then $\binom{2(a+b)}{a+b} \ne \binom{2a}{a}\binom{x+2b}{b}$.

## Sources

- Meaghan Allen, *Solvability of $\binom{2k}{k} = \binom{2a}{a}\binom{x+2b}{b}$*, INTEGERS 26 (2026), Article A26, Lemma 7.

Stated but not proved: `MetaMathlibExt.centralBinom_add_ne_of_half_le_of_three_le` is written with `theorem_wanted` in [WantedExt/NumberTheory/CentralBinomProductEquationWanted.lean, line 122](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/CentralBinomProductEquationWanted.lean#L122). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/binomial-coefficients/equations-in-central-binomial-coefficients/index.html#central-binom-add-ne-of-half-le-of-three).

## Central binomial products with $x \ge 2$ and $a \ge b$

Let $x$, $a$, $b$ be natural
numbers with $x \ge 2$ and $1 \le b \le a$. Then
$\binom{2(a+b)}{a+b} \ne \binom{2a}{a}\binom{x+2b}{b}$.

## Sources

- Meaghan Allen, *Solvability of $\binom{2k}{k} = \binom{2a}{a}\binom{x+2b}{b}$*, INTEGERS 26 (2026), Article A26, Lemma 8.

Stated but not proved: `MetaMathlibExt.centralBinom_add_ne_of_half_le_of_two_le` is written with `theorem_wanted` in [WantedExt/NumberTheory/CentralBinomProductEquationWanted.lean, line 131](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/CentralBinomProductEquationWanted.lean#L131). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/binomial-coefficients/equations-in-central-binomial-coefficients/index.html#central-binom-add-ne-of-half-le-of-two-l).

## A prime factor above $9m/5$ in a product of consecutive integers

Let $m$ and $n$ be
natural numbers with $2 < m < n$ and $n + m \ge 150$. Then the product $n(n+1)\cdots(n+m-1)$ has
a prime divisor $p$ with $p > 9m/5$.

## Sources

- Meaghan Allen, *Solvability of $\binom{2k}{k} = \binom{2a}{a}\binom{x+2b}{b}$*, INTEGERS 26 (2026), Article A26, Lemma 9, quoting Shanta and Shorey.

Stated but not proved: `MetaMathlibExt.exists_prime_dvd_prod_consecutive_gt_nine_fifths` is written with `theorem_wanted` in [WantedExt/NumberTheory/CentralBinomProductEquationWanted.lean, line 141](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/CentralBinomProductEquationWanted.lean#L141). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/binomial-coefficients/equations-in-central-binomial-coefficients/index.html#exists-prime-dvd-prod-consecutive-gt-nin).

## A prime factor above $4.42m$ in a product of consecutive integers

Let $m$ and $n$ be
natural numbers with $m > 3$, $n > 4m$ and $n + m \ge 150$. Then the product
$n(n+1)\cdots(n+m-1)$ has a prime divisor $p$ with $p > 4.42\,m$.

## Sources

- Meaghan Allen, *Solvability of $\binom{2k}{k} = \binom{2a}{a}\binom{x+2b}{b}$*, INTEGERS 26 (2026), Article A26, Lemma 10, quoting Nair and Shorey.

Stated but not proved: `MetaMathlibExt.exists_prime_dvd_prod_consecutive_gt_four_point_four_two` is written with `theorem_wanted` in [WantedExt/NumberTheory/CentralBinomProductEquationWanted.lean, line 151](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/CentralBinomProductEquationWanted.lean#L151). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/binomial-coefficients/equations-in-central-binomial-coefficients/index.html#exists-prime-dvd-prod-consecutive-gt-fou).

## Central binomial products in the balanced range

Let $a$ and $b$ be positive integers,
let $x \ge 2$ be an integer, and put $k = a + b$. If $k \ge 75$, $a \le \tfrac{9}{10}k$ and
$b \le \tfrac{4}{5}k$, then $\binom{2k}{k} \ne \binom{2a}{a}\binom{x+2b}{b}$.

## Sources

- Meaghan Allen, *Solvability of $\binom{2k}{k} = \binom{2a}{a}\binom{x+2b}{b}$*, INTEGERS 26 (2026), Article A26, Lemma 11.

Stated but not proved: `MetaMathlibExt.centralBinom_add_ne_of_balanced` is written with `theorem_wanted` in [WantedExt/NumberTheory/CentralBinomProductEquationWanted.lean, line 160](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/CentralBinomProductEquationWanted.lean#L160). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/binomial-coefficients/equations-in-central-binomial-coefficients/index.html#central-binom-add-ne-of-balanced).

## No large solutions of the central binomial product equation with a dominant central factor

For natural numbers $a$, $b$, $x$ with $b \ge 1$, $x \ge 2$, $a + b \ge 150$ and
$a \ge \frac{171}{121} x$, we have
$\binom{2(a+b)}{a+b} \ne \binom{2a}{a}\binom{x+2b}{b}$.

## Sources

- Meaghan Allen, *Solvability of $\binom{2k}{k} = \binom{2a}{a}\binom{x+2b}{b}$*, INTEGERS 26 (2026), Article A26, Lemma 12.

Stated but not proved: `MetaMathlibExt.centralBinom_add_ne_of_large_a` is written with `theorem_wanted` in [WantedExt/NumberTheory/CentralBinomProductEquationWanted.lean, line 169](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/CentralBinomProductEquationWanted.lean#L169). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/binomial-coefficients/equations-in-central-binomial-coefficients/index.html#central-binom-add-ne-of-large-a).

## Central binomial products with $x = 1$

Let $a$ and $b$ be positive integers. Then
$\binom{2(a+b)}{a+b} = \binom{2a}{a}\binom{1+2b}{b}$ if and only if $a = 1$.

## Sources

- Meaghan Allen, *Solvability of $\binom{2k}{k} = \binom{2a}{a}\binom{x+2b}{b}$*, INTEGERS 26 (2026), Article A26, Proposition 2.

Stated but not proved: `MetaMathlibExt.centralBinom_add_eq_centralBinom_mul_choose_one_iff` is written with `theorem_wanted` in [WantedExt/NumberTheory/CentralBinomProductEquationWanted.lean, line 178](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/CentralBinomProductEquationWanted.lean#L178). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/binomial-coefficients/equations-in-central-binomial-coefficients/index.html#central-binom-add-eq-central-binom-mul-c-3).

## No large solutions of the central binomial product equation with shift at least two

For natural numbers $a$, $b$, $x$ with $a \ge 1$, $b \ge 1$, $x \ge 2$ and $a + b \ge 150$, we have
$\binom{2(a+b)}{a+b} \ne \binom{2a}{a}\binom{x+2b}{b}$.

## Sources

- Meaghan Allen, *Solvability of $\binom{2k}{k} = \binom{2a}{a}\binom{x+2b}{b}$*, INTEGERS 26 (2026), Article A26, Proposition 3.

Stated but not proved: `MetaMathlibExt.centralBinom_add_ne_of_two_le_of_large` is written with `theorem_wanted` in [WantedExt/NumberTheory/CentralBinomProductEquationWanted.lean, line 187](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/CentralBinomProductEquationWanted.lean#L187). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/binomial-coefficients/equations-in-central-binomial-coefficients/index.html#central-binom-add-ne-of-two-le-of-large).

## Central binomial products with $x \ge 2$ and $a + b < 150$

Let $x$, $a$, $b$ be natural
numbers with $a \ge 1$, $b \ge 1$, $x \ge 2$ and $x < a + b < 150$. Then
$\binom{2(a+b)}{a+b} \ne \binom{2a}{a}\binom{x+2b}{b}$.

## Sources

- Meaghan Allen, *Solvability of $\binom{2k}{k} = \binom{2a}{a}\binom{x+2b}{b}$*, INTEGERS 26 (2026), Article A26, Proposition 4.

Stated but not proved: `MetaMathlibExt.centralBinom_add_ne_of_two_le_of_small` is written with `theorem_wanted` in [WantedExt/NumberTheory/CentralBinomProductEquationWanted.lean, line 196](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/CentralBinomProductEquationWanted.lean#L196). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/binomial-coefficients/equations-in-central-binomial-coefficients/index.html#central-binom-add-ne-of-two-le-of-small).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Equations in central binomial coefficients](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/binomial-coefficients/equations-in-central-binomial-coefficients/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/special-numbers/binomial-coefficients/equations-in-central-binomial-coefficients)
