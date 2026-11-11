---
declaration: section
origin: cited
lean: MetaMathlibExt.padicValNat_factorial_div_factorial_le, MetaMathlibExt.exists_density_one_padicValNat_centralBinom_bounds, MetaMathlibExt.factorial_div_factorial_dvd_centralBinom_density_one, MetaMathlibExt.max_padicValNat_add_le_density_one, MetaMathlibExt.card_padicValNat_centralBinom_le_isLittleO, MetaMathlibExt.card_max_padicValNat_add_gt_isLittleO, MetaMathlibExt.choose_dvd_centralBinom_density_one
statement: formalized
---

# Divisors of the middle binomial coefficient

7 results, 7 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/binomial-coefficients/divisors-of-the-middle-binomial-coefficient/index.html).

## Valuation of a product of consecutive integers

Let $m$ and $k$ be natural numbers and
$p$ a prime, and write $v_p(n)$ for the exponent of $p$ in a positive integer $n$. Then
$v_p\bigl((m+k)!/m!\bigr) \le v_p(k!) + \max \{ v_p(m + i) : 1 \le i \le k \}$, where the
maximum is $0$ when $k = 0$.

The quotient $(m+k)!/m! = (m+1) \cdots (m+k)$ is an integer. Unlike the source, the inequality
is stated also for $m = 0$ and $k = 0$.

## Sources

- Carl Pomerance, *Remarks on the Middle Binomial Coefficient*, INTEGERS 26 (2026), Article A47, Lemma 3.

Stated but not proved: `MetaMathlibExt.padicValNat_factorial_div_factorial_le` is written with `theorem_wanted` in [WantedExt/NumberTheory/MiddleBinomialCoefficientWanted.lean, line 31](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/MiddleBinomialCoefficientWanted.lean#L31). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/binomial-coefficients/divisors-of-the-middle-binomial-coefficient/index.html#padic-val-nat-factorial-div-factorial-le).

## Valuations of the middle binomial coefficient on a set of density one

Write $v_p(n)$ for
the exponent of a prime $p$ in a positive integer $n$, and for $m \ge 2$ let
$\alpha_p(m) = v_p\bigl(\binom{2m}{m}\bigr) / (\log m / \log p)$. There is a set $S$ of natural
numbers of natural density $1$ such that: $\alpha_2(m) \to 1/2$ as $m \to \infty$ within $S$; for
every $\varepsilon > 0$, $\alpha_3(m) \ge 34/81 - \varepsilon$ for all sufficiently large
$m \in S$; and $\alpha_p(m) \ge 0.39$ for every $m \in S$ and every prime $p$ with
$3 < p < 2 \log m$.

## Sources

- Carl Pomerance, *Remarks on the Middle Binomial Coefficient*, INTEGERS 26 (2026), Article A47, Lemma 1.

Stated but not proved: `MetaMathlibExt.exists_density_one_padicValNat_centralBinom_bounds` is written with `theorem_wanted` in [WantedExt/NumberTheory/MiddleBinomialCoefficientWanted.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/MiddleBinomialCoefficientWanted.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/binomial-coefficients/divisors-of-the-middle-binomial-coefficient/index.html#exists-density-one-padic-val-nat-central).

## Products of consecutive integers dividing the middle binomial coefficient

Let $\eta$ be
a real number with $\eta < 1 / \log 4$. The set of natural numbers $m$ such that
$(m+k)!/m! = (m+1)(m+2) \cdots (m+k)$ divides $\binom{2m}{m}$ for every integer $k$ with
$1 \le k \le \eta \log m$ has natural density $1$.

The constant $1 / \log 4$ is the threshold imposed by the prime $2$.

## Sources

- Carl Pomerance, *Remarks on the Middle Binomial Coefficient*, INTEGERS 26 (2026), Article A47, Theorem 1.

Stated but not proved: `MetaMathlibExt.factorial_div_factorial_dvd_centralBinom_density_one` is written with `theorem_wanted` in [WantedExt/NumberTheory/MiddleBinomialCoefficientWanted.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/MiddleBinomialCoefficientWanted.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/binomial-coefficients/divisors-of-the-middle-binomial-coefficient/index.html#factorial-div-factorial-dvd-central-bino).

## Short runs of consecutive integers have small valuations almost always

Write $v_p(n)$
for the exponent of a prime $p$ in a positive integer $n$. The set of natural numbers $m$ such
that $\max \{ v_p(m + i) : 1 \le i \le k \} \le 3 \log k / \log p$ for every integer $k$ with
$\frac{1}{2} \log m < k < \log m$ and every prime $p \le 2k$ has natural density $1$.

## Sources

- Carl Pomerance, *Remarks on the Middle Binomial Coefficient*, INTEGERS 26 (2026), Article A47, Lemma 2.

Stated but not proved: `MetaMathlibExt.max_padicValNat_add_le_density_one` is written with `theorem_wanted` in [WantedExt/NumberTheory/MiddleBinomialCoefficientWanted.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/MiddleBinomialCoefficientWanted.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/binomial-coefficients/divisors-of-the-middle-binomial-coefficient/index.html#max-padic-val-nat-add-le-density-one).

## Small valuations of the middle binomial coefficient are rare

For a natural number $x$
let $K = \lfloor \exp(0.8 \sqrt{\log x}) \rfloor$ and, for a prime $p$, let
$D_p = 1 + \lfloor \log x / \log p \rfloor$. Write $v_p(n)$ for the exponent of $p$ in a
positive integer $n$. Then the number of integers $m$ with $1 \le m \le x$ for which some prime
$p \le 2K$ satisfies $v_p\bigl(\binom{2m}{m}\bigr) \le D_p / \log D_p$ is $o(x)$ as $x \to \infty$.

For large $x$ every prime $p \le 2K$ is at most $x$, so $D_p \ge 2$ and $\log D_p > 0$.

## Sources

- Carl Pomerance, *Remarks on the Middle Binomial Coefficient*, INTEGERS 26 (2026), Article A47, Lemma 4.

Stated but not proved: `MetaMathlibExt.card_padicValNat_centralBinom_le_isLittleO` is written with `theorem_wanted` in [WantedExt/NumberTheory/MiddleBinomialCoefficientWanted.lean, line 82](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/MiddleBinomialCoefficientWanted.lean#L82). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/binomial-coefficients/divisors-of-the-middle-binomial-coefficient/index.html#card-padic-val-nat-central-binom-le-is-l).

## Large valuations in short runs of consecutive integers are rare

For a natural number
$x$ let $K = \lfloor \exp(0.8 \sqrt{\log x}) \rfloor$ and, for a prime $p$, let
$D_p = 1 + \lfloor \log x / \log p \rfloor$. Write $v_p(n)$ for the exponent of $p$ in a
positive integer $n$. Then the number of integers $m$ with $1 \le m \le x$ for which some prime
$p < 2K$ satisfies $\max \{ v_p(m + i) : 1 \le i \le K \} > D_p / \log D_p$ is $o(x)$ as
$x \to \infty$.

For large $x$ every prime $p < 2K$ is at most $x$, so $D_p \ge 2$ and $\log D_p > 0$.

## Sources

- Carl Pomerance, *Remarks on the Middle Binomial Coefficient*, INTEGERS 26 (2026), Article A47, Lemma 5.

Stated but not proved: `MetaMathlibExt.card_max_padicValNat_add_gt_isLittleO` is written with `theorem_wanted` in [WantedExt/NumberTheory/MiddleBinomialCoefficientWanted.lean, line 97](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/MiddleBinomialCoefficientWanted.lean#L97). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/binomial-coefficients/divisors-of-the-middle-binomial-coefficient/index.html#card-max-padic-val-nat-add-gt-is-little).

## Binomial coefficients dividing the middle binomial coefficient

The set of natural
numbers $m$ such that $\binom{m+k}{k}$ divides $\binom{2m}{m}$ for every integer $k$ with
$1 \le k \le \exp(0.8 \sqrt{\log m})$ has natural density $1$.

## Sources

- Carl Pomerance, *Remarks on the Middle Binomial Coefficient*, INTEGERS 26 (2026), Article A47, Theorem 2.

Stated but not proved: `MetaMathlibExt.choose_dvd_centralBinom_density_one` is written with `theorem_wanted` in [WantedExt/NumberTheory/MiddleBinomialCoefficientWanted.lean, line 112](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/MiddleBinomialCoefficientWanted.lean#L112). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/binomial-coefficients/divisors-of-the-middle-binomial-coefficient/index.html#choose-dvd-central-binom-density-one).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Divisors of the middle binomial coefficient](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/binomial-coefficients/divisors-of-the-middle-binomial-coefficient/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/special-numbers/binomial-coefficients/divisors-of-the-middle-binomial-coefficient)
