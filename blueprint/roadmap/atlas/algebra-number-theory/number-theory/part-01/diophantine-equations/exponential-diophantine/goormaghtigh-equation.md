---
declaration: section
origin: cited
lean: MetaMathlibExt.goormaghtigh_eq_of_gcd_sub_one_gt_one_of_le_fifty, MetaMathlibExt.goormaghtigh_prime_lt_ten_pow_seven_hundred, MetaMathlibExt.goormaghtigh_numbers_length_ge_five_finite_of_abc, MetaMathlibExt.goormaghtigh_primes_finite_of_abc
statement: formalized
---

# Goormaghtigh equation

4 results, 4 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/exponential-diophantine/goormaghtigh-equation/index.html).

## Goormaghtigh solutions with $\gcd(m - 1, n - 1) > 1$ and $m \le 50$

Let $x, y, m, n$ be
natural numbers with $2 \le x < y$, $n > 2$, $m \le 50$ and $\gcd(m - 1, n - 1) > 1$, and suppose

$$N = \sum_{i=0}^{m-1} x^i = \sum_{i=0}^{n-1} y^i,$$

that is, $N = (x^m - 1)/(x - 1) = (y^n - 1)/(y - 1)$. Then $N = 31$ or $N = 8191$.

The paper prints the side conditions of its Equation (1) as $y > x \ge 2$ and $n > m > 2$. Since
$y > x$, equal repunits force $m > n$ (the paper's own solution
$31 = 1 + 2 + 4 + 8 + 16 = 1 + 5 + 25$ has $m = 5 > n = 3$), so the printed $n > m$ is read as
$m > n$; that inequality follows from the other hypotheses and is not assumed. The paper quotes
this result as part of Theorem 4 of Bennett, Garbuz and Marten (2020).

## Sources

- Jon Grantham, *No New Goormaghtigh Primes up to 10^700*, INTEGERS 24 (2024), Article A98, Theorem 1.

Stated but not proved: `MetaMathlibExt.goormaghtigh_eq_of_gcd_sub_one_gt_one_of_le_fifty` is written with `theorem_wanted` in [WantedExt/NumberTheory/GoormaghtighPrimesWanted.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/GoormaghtighPrimesWanted.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/exponential-diophantine/goormaghtigh-equation/index.html#goormaghtigh-eq-of-gcd-sub-one-gt-one-of).

## No Goormaghtigh primes below $10^{700}$ besides $31$ and $8191$

Let $p$ be a prime with
$p < 10^{700}$, and let $x, y, m, n$ be natural numbers with $2 \le x < y$ and $n \ge 3$ such that

$$p = \sum_{i=0}^{m-1} x^i = \sum_{i=0}^{n-1} y^i,$$

that is, $p$ is a repunit of length $m$ in base $x$ and of length $n$ in base $y$. Then $p = 31$
or $p = 8191$.

## Sources

- Jon Grantham, *No New Goormaghtigh Primes up to 10^700*, INTEGERS 24 (2024), Article A98, Section 2, discussion following Theorem 1.

Stated but not proved: `MetaMathlibExt.goormaghtigh_prime_lt_ten_pow_seven_hundred` is written with `theorem_wanted` in [WantedExt/NumberTheory/GoormaghtighPrimesWanted.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/GoormaghtighPrimesWanted.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/exponential-diophantine/goormaghtigh-equation/index.html#goormaghtigh-prime-lt-ten-pow-seven-hund).

## Under abc, finitely many Goormaghtigh numbers have both lengths at least five

Assume the
abc conjecture in the following form: for every real $\varepsilon > 0$, there are only finitely
many triples $(a, b, c)$ of positive integers with $a + b = c$, $\gcd(a, b) = 1$ and
$\operatorname{rad}(abc)^{1 + \varepsilon} \le c$, where $\operatorname{rad}(k)$ is the product of
the distinct primes dividing $k$. Then there are only finitely many natural numbers $N$ for which
there exist natural numbers $x, y, m, n$ with $2 \le x < y$ and $n \ge 5$ such that

$$N = \sum_{i=0}^{m-1} x^i = \sum_{i=0}^{n-1} y^i.$$

Such an $N$ is a repunit of length $m$ in base $x$ and of length $n \ge 5$ in base $y$; since
$x < y$, equality forces $m > n$, so both lengths are at least five. The paper states the abc
conjecture for relatively prime integers; the positive-triple form used here is the standard
equivalent one.

## Sources

- Jon Grantham, *No New Goormaghtigh Primes up to 10^700*, INTEGERS 24 (2024), Article A98, Theorem 2.

Stated but not proved: `MetaMathlibExt.goormaghtigh_numbers_length_ge_five_finite_of_abc` is written with `theorem_wanted` in [WantedExt/NumberTheory/GoormaghtighPrimesWanted.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/GoormaghtighPrimesWanted.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/exponential-diophantine/goormaghtigh-equation/index.html#goormaghtigh-numbers-length-ge-five-fini).

## Under abc, there are only finitely many Goormaghtigh primes

Assume the abc conjecture in
the following form: for every real $\varepsilon > 0$, there are only finitely many triples
$(a, b, c)$ of positive integers with $a + b = c$, $\gcd(a, b) = 1$ and
$\operatorname{rad}(abc)^{1 + \varepsilon} \le c$, where $\operatorname{rad}(k)$ is the product of
the distinct primes dividing $k$. Then there are only finitely many primes $p$ for which there
exist natural numbers $x, y, m, n$ with $2 \le x < y$ and $n \ge 3$ such that

$$p = \sum_{i=0}^{m-1} x^i = \sum_{i=0}^{n-1} y^i.$$

## Sources

- Jon Grantham, *No New Goormaghtigh Primes up to 10^700*, INTEGERS 24 (2024), Article A98, Corollary 1.

Stated but not proved: `MetaMathlibExt.goormaghtigh_primes_finite_of_abc` is written with `theorem_wanted` in [WantedExt/NumberTheory/GoormaghtighPrimesWanted.lean, line 90](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/GoormaghtighPrimesWanted.lean#L90). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/exponential-diophantine/goormaghtigh-equation/index.html#goormaghtigh-primes-finite-of-abc).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Goormaghtigh equation](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/exponential-diophantine/goormaghtigh-equation/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/diophantine-equations/exponential-diophantine/goormaghtigh-equation)
