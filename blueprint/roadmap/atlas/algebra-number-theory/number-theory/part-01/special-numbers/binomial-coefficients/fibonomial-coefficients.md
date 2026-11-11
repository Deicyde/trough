---
declaration: section
origin: cited
lean: MetaMathlibExt.padicValNat_fib_mul, MetaMathlibExt.fibonomial_primePower_padicVal_eq_zero, MetaMathlibExt.fibonomial_prime_cube_congr
statement: formalized
proof: formalized
---

# Fibonomial coefficients

3 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/binomial-coefficients/fibonomial-coefficients/index.html).

## Lifting the exponent for Fibonacci numbers

Let $p$ be an odd prime and $m \ge 1$ an
integer such that $p$ divides the Fibonacci number $F_m$, and write $v_p$ for the $p$-adic
valuation. Then $v_p(F_{mj}) = v_p(F_m) + v_p(j)$ for every integer $j \ge 1$.

Formalized by `MetaMathlibExt.padicValNat_fib_mul`, a theorem declared in [MathlibExt/NumberTheory/Padics/FibonomialPrimePowerValuation.lean, line 367](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/Padics/FibonomialPrimePowerValuation.lean#L367). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/binomial-coefficients/fibonomial-coefficients/index.html#padic-val-nat-fib-mul).

## Vanishing $p$-adic valuation of Fibonomial coefficients at prime powers

Let $p$ be a
prime with $p \ne 2$ and $p \ne 5$, and let $a, b$ be integers with $0 < a \le b$ such that
$p \equiv \pm 1 \pmod 5$ or $a \equiv b \pmod 2$. Write $F_n$ for the $n$-th Fibonacci number
and $F_n! = F_1 F_2 \cdots F_n$ for the Fibonacci factorial, with $F_0! = 1$. Then the $p$-adic
valuation of the Fibonomial coefficient

$$\binom{p^b}{p^a}_F = \frac{F_{p^b}!}{F_{p^a}! \, F_{p^b - p^a}!},$$

where the quotient is taken by division of natural numbers, is $0$.

## Sources

- Phunphayap–Pongsriiam, Example `rem18`, equation `eq1remark2`.

Formalized by `MetaMathlibExt.fibonomial_primePower_padicVal_eq_zero`, a theorem declared in [MathlibExt/NumberTheory/Padics/FibonomialPrimePowerValuation.lean, line 594](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/Padics/FibonomialPrimePowerValuation.lean#L594). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/binomial-coefficients/fibonomial-coefficients/index.html#fibonomial-prime-power-padic-val-eq-zero).

## Kimball–Webb congruence for Fibonomial coefficients modulo $p^3$

Let $F_n$ be the
Fibonacci numbers, with $F_1 = F_2 = 1$, and write $F_n! = F_1 F_2 \cdots F_n$, with $F_0! = 1$.
Let $p \ge 7$ be a prime and $\varepsilon \in \{1, -1\}$, and suppose that $\rho = p - \varepsilon$
is the rank of appearance of $p$, that is, $p \mid F_\rho$ and $p \nmid F_m$ for $0 < m < \rho$.
Then for every natural number $k$ the Fibonomial coefficient

$$\binom{(k+1)\rho - 1}{\rho - 1}_F = \frac{F_{(k+1)\rho - 1}!}{F_{\rho - 1}!\, F_{k\rho}!}$$

is congruent to $\varepsilon^k$ modulo $p^3$.

The quotient is taken in the natural numbers; it is exact because Fibonomial coefficients are
integers. This is the Fibonacci case only, not Ballot's general theorem for Lucasnomial
coefficients.

## Sources

- Christian Ballot, *The Congruence of Wolstenholme for Generalized Binomial Coefficients Related to Lucas Sequences*, Journal of Integer Sequences 18 (2015), Article 15.5.4, <https://cs.uwaterloo.ca/journals/JIS/VOL18/Ballot/ballot14.tex>, Theorem `thm:KW` (rewriting Lemma 3 of Kimball and Webb), equation `eq:Fib`, lines 144-150.

Formalized by `MetaMathlibExt.fibonomial_prime_cube_congr`, a theorem declared in [MathlibExt/NumberTheory/Padics/KimballWebbFibonomialCongruence.lean, line 1942](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/Padics/KimballWebbFibonomialCongruence.lean#L1942). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/binomial-coefficients/fibonomial-coefficients/index.html#fibonomial-prime-cube-congr).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Fibonomial coefficients](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/binomial-coefficients/fibonomial-coefficients/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/special-numbers/binomial-coefficients/fibonomial-coefficients)
