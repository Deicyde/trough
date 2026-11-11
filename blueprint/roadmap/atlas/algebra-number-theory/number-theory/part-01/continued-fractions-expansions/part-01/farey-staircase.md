---
declaration: section
origin: cited
lean: MetaMathlibExt.fareyStaircase, MetaMathlibExt.fareyStaircase_zero, MetaMathlibExt.fareyStaircase_one, MetaMathlibExt.fareyZoom, MetaMathlibExt.fareyZoom_eq_sum, MetaMathlibExt.fareyZoom_one, MetaMathlibExt.tendsto_fareyZoom, MetaMathlibExt.tendsto_fareyZoom_sub_at_rational
statement: formalized
---

# Farey staircase

16 results, 6 proved and 10 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/farey-staircase/index.html).

## Farey staircase

For a natural number $n$ and a real number $x$, the Farey staircase of
order $n$ is $A_n(x) = \frac{1}{n} \sum_{k=1}^{n} \lfloor kx \rfloor / k$, the average of the
first $n$ lower rational approximations $\lfloor kx \rfloor / k$ of $x$. For $n = 0$ the sum is
empty and $A_0(x) = 0$.

## Sources

- David Harry Richman, *Lower Rational Approximations and Farey Staircases*, INTEGERS 24 (2024), Article A37, Section 1, equation (2).

Formalized by `MetaMathlibExt.fareyStaircase`, a definition declared in [WantedExt/NumberTheory/FareyStaircaseWanted.lean, line 34](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/FareyStaircaseWanted.lean#L34). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/farey-staircase/index.html#farey-staircase).

## The Farey staircase of order zero vanishes

For every real number $x$, the Farey staircase
$A_0$ of order $0$ satisfies $A_0(x) = 0$.

## Sources

- David Harry Richman, *Lower Rational Approximations and Farey Staircases*, INTEGERS 24 (2024), Article A37, Section 1, equation (2).

Formalized by `MetaMathlibExt.fareyStaircase_zero`, a theorem declared in [WantedExt/NumberTheory/FareyStaircaseWanted.lean, line 41](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/FareyStaircaseWanted.lean#L41). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/farey-staircase/index.html#farey-staircase-zero).

## The Farey staircase of order one is the floor function

For every real number $x$, the
Farey staircase $A_1$ of order $1$ satisfies $A_1(x) = \lfloor x \rfloor$.

## Sources

- David Harry Richman, *Lower Rational Approximations and Farey Staircases*, INTEGERS 24 (2024), Article A37, Section 1, equation (2).

Formalized by `MetaMathlibExt.fareyStaircase_one`, a theorem declared in [WantedExt/NumberTheory/FareyStaircaseWanted.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/FareyStaircaseWanted.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/farey-staircase/index.html#farey-staircase-one).

## Zoomed Farey staircase

For a natural number $n$ and a real number $x$, the zoomed Farey
staircase of order $n$ is $B_0(x) = 0$ for $n = 0$ and $B_n(x) = n A_n(x/n)$ for $n \ge 1$, where
$A_n$ is the Farey staircase of order $n$. For $n \ge 1$ this equals
$\sum_{k=1}^{n} \lfloor (k/n) x \rfloor / k$.

## Sources

- David Harry Richman, *Lower Rational Approximations and Farey Staircases*, INTEGERS 24 (2024), Article A37, Section 1.1, equation (4).

Formalized by `MetaMathlibExt.fareyZoom`, a definition declared in [WantedExt/NumberTheory/FareyStaircaseWanted.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/FareyStaircaseWanted.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/farey-staircase/index.html#farey-zoom).

## The zoomed Farey staircase as a sum

For every natural number $n \ge 1$ and every real
number $x$, the zoomed Farey staircase $B_n$ of order $n$ satisfies
$B_n(x) = \sum_{k=1}^{n} \lfloor (k/n) x \rfloor / k$.

## Sources

- David Harry Richman, *Lower Rational Approximations and Farey Staircases*, INTEGERS 24 (2024), Article A37, Section 1.1, equation (4).

Formalized by `MetaMathlibExt.fareyZoom_eq_sum`, a theorem declared in [WantedExt/NumberTheory/FareyStaircaseWanted.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/FareyStaircaseWanted.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/farey-staircase/index.html#farey-zoom-eq-sum).

## The zoomed Farey staircase of order one is the floor function

For every real number $x$,
the zoomed Farey staircase $B_1$ of order $1$ satisfies $B_1(x) = \lfloor x \rfloor$.

## Sources

- David Harry Richman, *Lower Rational Approximations and Farey Staircases*, INTEGERS 24 (2024), Article A37, Section 1.1, equation (4).

Formalized by `MetaMathlibExt.fareyZoom_one`, a theorem declared in [WantedExt/NumberTheory/FareyStaircaseWanted.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/FareyStaircaseWanted.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/farey-staircase/index.html#farey-zoom-one).

## Limit of the Farey staircase zoomed at the origin

Let $B_n$ be the zoomed Farey staircase
of order $n$. For every real $x \ge 0$, $B_n(x) \to \sum_{k=1}^{\lfloor x \rfloor} \log(x/k)$ as
$n \to \infty$.

## Sources

- David Harry Richman, *Lower Rational Approximations and Farey Staircases*, INTEGERS 24 (2024), Article A37, Theorem 1.

Stated but not proved: `MetaMathlibExt.tendsto_fareyZoom` is written with `theorem_wanted` in [WantedExt/NumberTheory/FareyStaircaseWanted.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/FareyStaircaseWanted.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/farey-staircase/index.html#tendsto-farey-zoom).

## Limit of the Farey staircase zoomed at a rational point

Let $B_n$ be the zoomed Farey
staircase of order $n$, let $x \ge 0$ be real, and let $p$ and $q$ be coprime positive integers.
Then $B_n(x + pn/q) - B_n(pn/q) \to \frac{1}{q} \sum_{k=1}^{\lfloor qx \rfloor} \log(qx/k)$ as
$n \to \infty$.

## Sources

- David Harry Richman, *Lower Rational Approximations and Farey Staircases*, INTEGERS 24 (2024), Article A37, Theorem 3.

Stated but not proved: `MetaMathlibExt.tendsto_fareyZoom_sub_at_rational` is written with `theorem_wanted` in [WantedExt/NumberTheory/FareyStaircaseWanted.lean, line 89](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/FareyStaircaseWanted.lean#L89). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/farey-staircase/index.html#tendsto-farey-zoom-sub-at-rational).

## Limit of the rescaled Farey staircase increment

Let $A_n$ be the Farey staircase of order
$n$ and $D_n = A_n - A_{n-1}$. For every real $x \ge 0$,
$n^2 D_n(x/n) \to \sum_{k=1}^{\lfloor x \rfloor} (1 - \log(x/k))$ as $n \to \infty$.

## Sources

- David Harry Richman, *Lower Rational Approximations and Farey Staircases*, INTEGERS 24 (2024), Article A37, Theorem 4.

Stated but not proved: `MetaMathlibExt.tendsto_sq_mul_fareyStaircase_sub` is written with `theorem_wanted` in [WantedExt/NumberTheory/FareyStaircaseWanted.lean, line 101](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/FareyStaircaseWanted.lean#L101). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/farey-staircase/index.html#tendsto-sq-mul-farey-staircase-sub).

## Floor gaps of Farey staircases are dense above $1 - \log 2$

For $n \ge 1$ and
$x \in \mathbb{R}$ let $f_n(x) = \lfloor nx \rfloor - n A_n(x)$, where $A_n$ is the Farey staircase
of order $n$; thus $f_n(x) = \lfloor nx \rfloor - \sum_{k=1}^n \lfloor kx \rfloor / k$. Every real
number $y \ge 1 - \log 2$ lies in the closure of the set
$S = \{f_n(x) : n \ge 1,\ x \in \mathbb{R}\}$, that is, $S$ is dense in $[1 - \log 2, \infty)$.

## Sources

- David Harry Richman, *Lower Rational Approximations and Farey Staircases*, INTEGERS 24 (2024), Article A37, Theorem 5 (i), also Corollary 6.

Stated but not proved: `MetaMathlibExt.Ici_one_sub_log_two_subset_closure_floor_gaps` is written with `theorem_wanted` in [WantedExt/NumberTheory/FareyStaircaseWanted.lean, line 113](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/FareyStaircaseWanted.lean#L113). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/farey-staircase/index.html#ici-one-sub-log-two-subset-closure-floor).

## Finiteness of small floor gaps of the Farey staircase

For a natural number $n \ge 1$ and a
real number $x$, let $f_n(x) = \lfloor nx \rfloor - n A_n(x)$, where $A_n$ is the Farey staircase
of order $n$. Then for every real number $\varepsilon > 0$, only finitely many distinct real
numbers that are at most $1 - \log 2 - \varepsilon$ occur as a value $f_n(x)$ with $n \ge 1$ and
$x$ real; here $\log$ is the natural logarithm.

## Sources

- David Harry Richman, *Lower Rational Approximations and Farey Staircases*, INTEGERS 24 (2024), Article A37, Theorem 5 (ii).

Stated but not proved: `MetaMathlibExt.floor_gaps_inter_Iic_finite` is written with `theorem_wanted` in [WantedExt/NumberTheory/FareyStaircaseWanted.lean, line 122](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/FareyStaircaseWanted.lean#L122). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/farey-staircase/index.html#floor-gaps-inter-iic-finite).

## Recursion between consecutive Farey staircases

Let $n \ge 2$ be a natural number and $x$
a real number, write $A_m$ for the Farey staircase of order $m$, and let
$D_n(x) = A_n(x) - A_{n-1}(x)$. Then
$D_n(x) = \frac{1}{n} \left( \lfloor nx \rfloor / n - A_{n-1}(x) \right)$ and
$D_n(x) = \frac{1}{n-1} \left( \lfloor nx \rfloor / n - A_n(x) \right)$.

## Sources

- David Harry Richman, *Lower Rational Approximations and Farey Staircases*, INTEGERS 24 (2024), Article A37, Proposition 7.

Stated but not proved: `MetaMathlibExt.fareyStaircase_sub_eq` is written with `theorem_wanted` in [WantedExt/NumberTheory/FareyStaircaseWanted.lean, line 131](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/FareyStaircaseWanted.lean#L131). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/farey-staircase/index.html#farey-staircase-sub-eq).

## Bounds comparing the Farey staircase with $\lfloor nx \rfloor / n$

For every natural
number $n \ge 1$ and every real number $x$, the Farey staircase $A_n$ of order $n$ satisfies
$A_n(x) \le \lfloor nx \rfloor / n \le A_n(x) + (\log n)/n$, where $\log$ is the natural
logarithm.

## Sources

- David Harry Richman, *Lower Rational Approximations and Farey Staircases*, INTEGERS 24 (2024), Article A37, Lemma 8 (a).

Stated but not proved: `MetaMathlibExt.fareyStaircase_le_floor_div` is written with `theorem_wanted` in [WantedExt/NumberTheory/FareyStaircaseWanted.lean, line 141](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/FareyStaircaseWanted.lean#L141). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/farey-staircase/index.html#farey-staircase-le-floor-div).

## Bounds on the increment of the Farey staircase

Let $n \ge 2$ be a natural number and $x$
a real number, and write $A_m$ for the Farey staircase of order $m$. Then
$0 \le A_n(x) - A_{n-1}(x) \le \frac{\log n}{n(n-1)}$, where $\log$ is the natural logarithm.

## Sources

- David Harry Richman, *Lower Rational Approximations and Farey Staircases*, INTEGERS 24 (2024), Article A37, Lemma 8 (b).

Stated but not proved: `MetaMathlibExt.fareyStaircase_sub_mem_Icc` is written with `theorem_wanted` in [WantedExt/NumberTheory/FareyStaircaseWanted.lean, line 149](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/FareyStaircaseWanted.lean#L149). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/farey-staircase/index.html#farey-staircase-sub-mem-icc).

## Harmonic blocks versus the logarithmic integral

Let $(a_n)$ and $(b_n)$ be sequences of
natural numbers with $a_n \le b_n$ for every $n$ and $a_n \to \infty$. Then
$\sum_{k=a_n}^{b_n} 1/k - \int_{a_n}^{b_n} dt/t \to 0$ as $n \to \infty$.

In particular, if either $\sum_{k=a_n}^{b_n} 1/k$ or $\int_{a_n}^{b_n} dt/t$ converges, then so does
the other, with the same limit. Positivity of $a_n$ and $b_n$ and $b_n \to \infty$ need not be
assumed: they follow from the hypotheses (positivity for all large $n$).

## Sources

- David Harry Richman, *Lower Rational Approximations and Farey Staircases*, INTEGERS 24 (2024), Article A37, Lemma 9.

Stated but not proved: `MetaMathlibExt.tendsto_harmonic_block_sub_integral` is written with `theorem_wanted` in [WantedExt/NumberTheory/FareyStaircaseWanted.lean, line 159](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/FareyStaircaseWanted.lean#L159). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/farey-staircase/index.html#tendsto-harmonic-block-sub-integral).

## Dilation derivative of a differentiable function

Let $f : \mathbb{R} \to \mathbb{R}$ have
derivative $f'$ at the point $x \in \mathbb{R}$. Then the quotient
$(\lambda^{-1} f(\lambda x) - f(x))/(\lambda - 1)$ tends to $x f' - f(x)$ as $\lambda \to 1$ with
$\lambda \ne 1$; that is, the dilation derivative of $f$ at $x$ exists and equals $x f' - f(x)$.

## Sources

- David Harry Richman, *Lower Rational Approximations and Farey Staircases*, INTEGERS 24 (2024), Article A37, Proposition 12; dilation derivative as defined before it.

Stated but not proved: `MetaMathlibExt.tendsto_dilation_quotient` is written with `theorem_wanted` in [WantedExt/NumberTheory/FareyStaircaseWanted.lean, line 171](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/FareyStaircaseWanted.lean#L171). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/farey-staircase/index.html#tendsto-dilation-quotient).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Farey staircase](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/farey-staircase/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/continued-fractions-expansions/part-01/farey-staircase)
