---
declaration: section
origin: cited
lean: MetaMathlibExt.dirichletLFunction_mod_four_fourth_moment_le, MetaMathlibExt.dedekindZetaCoeff, MetaMathlibExt.dedekindZetaCoeff_one, MetaMathlibExt.sixSquaresDedekindMoment, MetaMathlibExt.sixSquaresDedekindMoment_of_lt_one, MetaMathlibExt.dedekindSixSquaresA0, MetaMathlibExt.dedekindSixSquaresA3, MetaMathlibExt.dedekindSixSquaresA0_A3_small
statement: formalized
---

# Moments of Dedekind zeta coefficients over sums of six squares

10 results, 7 proved and 3 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/dirichlet-l-functions/moments-of-dedekind-zeta-coefficients-over-sums/index.html).

## Fourth moment of the $L$-function modulo $4$

Let $\chi$ be a nontrivial Dirichlet
character modulo $4$ and let $\varepsilon > 0$. Then there is a real constant $C$ such that for
every real $T \ge 1$, $\int_1^T |L(1/2 + it, \chi)|^4 \, dt \le C\, T^{1 + \varepsilon}$.

## Sources

- Naveen K. Godara and Prashant Tiwari, *The Higher Power Moments of the Coefficients of the Dedekind Zeta Function over a Polynomial in Six Variables*, INTEGERS 25 (2025), Article A101, Lemma 5, third display.

Stated but not proved: `MetaMathlibExt.dirichletLFunction_mod_four_fourth_moment_le` is written with `theorem_wanted` in [WantedExt/NumberTheory/DedekindZetaSixSquaresMomentsWanted.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/DedekindZetaSixSquaresMomentsWanted.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/dirichlet-l-functions/moments-of-dedekind-zeta-coefficients-over-sums/index.html#dirichlet-lfunction-mod-four-fourth-mome).

## Coefficients of the Dedekind zeta function

For a number field $K$ with ring of integers
$\mathcal{O}_K$ and a natural number $n$, $a_K(n)$ is the number of ideals of $\mathcal{O}_K$ of
absolute norm $n$. These are the coefficients of $\zeta_K(s) = \sum_{n \ge 1} a_K(n)\, n^{-s}$.

## Sources

- Naveen K. Godara and Prashant Tiwari, *The Higher Power Moments of the Coefficients of the Dedekind Zeta Function over a Polynomial in Six Variables*, INTEGERS 25 (2025), Article A101, Section 1, equation (2).

Formalized by `MetaMathlibExt.dedekindZetaCoeff`, a definition declared in [WantedExt/NumberTheory/DedekindZetaSixSquaresMomentsWanted.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/DedekindZetaSixSquaresMomentsWanted.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/dirichlet-l-functions/moments-of-dedekind-zeta-coefficients-over-sums/index.html#dedekind-zeta-coeff).

## The Dedekind zeta coefficient at $1$

For every number field $K$, $a_K(1) = 1$, where
$a_K(n)$ is the number of ideals of the ring of integers of $K$ of absolute norm $n$: the unit
ideal is the only ideal of norm $1$.

## Sources

- Naveen K. Godara and Prashant Tiwari, *The Higher Power Moments of the Coefficients of the Dedekind Zeta Function over a Polynomial in Six Variables*, INTEGERS 25 (2025), Article A101, Section 1, equation (2).

Formalized by `MetaMathlibExt.dedekindZetaCoeff_one`, a theorem declared in [WantedExt/NumberTheory/DedekindZetaSixSquaresMomentsWanted.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/DedekindZetaSixSquaresMomentsWanted.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/dirichlet-l-functions/moments-of-dedekind-zeta-coefficients-over-sums/index.html#dedekind-zeta-coeff-one).

## Six-squares moments of Dedekind zeta coefficients

For a number field $K$, a natural
number $\ell$ and a real number $x$, the moment is the real number
$S_\ell(x) = \sum_{1 \le n \le x} r_6(n)\, a_K(n)^\ell$, where $n$ runs over the integers in
$[1, x]$, $a_K(n)$ is the number of ideals of the ring of integers of $K$ of absolute norm $n$,
and $r_6(n)$ is the coefficient of $q^n$ in $\theta(q)^6$, with
$\theta(q) = \sum_{m \in \mathbb{Z}} q^{m^2}$; that is, $r_6(n)$ is the number of representations
of $n$ as a sum of six squares of integers.

## Sources

- Naveen K. Godara and Prashant Tiwari, *The Higher Power Moments of the Coefficients of the Dedekind Zeta Function over a Polynomial in Six Variables*, INTEGERS 25 (2025), Article A101, Section 1, equation (4), and Section 2, equation (12).

Formalized by `MetaMathlibExt.sixSquaresDedekindMoment`, a definition declared in [WantedExt/NumberTheory/DedekindZetaSixSquaresMomentsWanted.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/DedekindZetaSixSquaresMomentsWanted.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/dirichlet-l-functions/moments-of-dedekind-zeta-coefficients-over-sums/index.html#six-squares-dedekind-moment).

## The six-squares moment vanishes below $1$

For every number field $K$, every natural
number $\ell$ and every real $x < 1$, the six-squares moment
$S_\ell(x) = \sum_{1 \le n \le x} r_6(n)\, a_K(n)^\ell$ equals $0$, where $r_6(n)$ is the number
of representations of $n$ as a sum of six squares of integers and $a_K(n)$ is the number of
ideals of the ring of integers of $K$ of absolute norm $n$.

## Sources

- Naveen K. Godara and Prashant Tiwari, *The Higher Power Moments of the Coefficients of the Dedekind Zeta Function over a Polynomial in Six Variables*, INTEGERS 25 (2025), Article A101, Section 1, equation (4).

Formalized by `MetaMathlibExt.sixSquaresDedekindMoment_of_lt_one`, a theorem declared in [WantedExt/NumberTheory/DedekindZetaSixSquaresMomentsWanted.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/DedekindZetaSixSquaresMomentsWanted.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/dirichlet-l-functions/moments-of-dedekind-zeta-coefficients-over-sums/index.html#six-squares-dedekind-moment-of-lt-one).

## The exponent $a_{0,\ell}$

For a natural number $\ell$, define

$$a_{0,\ell} = 1 + \sum_{i=1}^{\lfloor \ell/2 \rfloor} \binom{\ell}{2i} C_i,$$

where $C_i = (2i)!/(i!\,(i+1)!)$ is the $i$-th Catalan number.

## Sources

- Naveen K. Godara and Prashant Tiwari, *The Higher Power Moments of the Coefficients of the Dedekind Zeta Function over a Polynomial in Six Variables*, INTEGERS 25 (2025), Article A101, Theorem 2 and equation (19).

Formalized by `MetaMathlibExt.dedekindSixSquaresA0`, a definition declared in [WantedExt/NumberTheory/DedekindZetaSixSquaresMomentsWanted.lean, line 93](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/DedekindZetaSixSquaresMomentsWanted.lean#L93). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/dirichlet-l-functions/moments-of-dedekind-zeta-coefficients-over-sums/index.html#dedekind-six-squares-a0).

## The exponent $a_{3,\ell}$

For a natural number $\ell$, $a_{3,\ell}$ is the sum over the
integers $1 \le i \le \lfloor (\ell - 1)/2 \rfloor$ of $\binom{\ell}{2i+1} q_i$, where $q_i$ is the
integer part of $4\,(2i+1)!/((i-1)!\,(i+3)!)$.

Each quotient $4\,(2i+1)!/((i-1)!\,(i+3)!)$ is in fact an integer, and the upper limit
$\lfloor (\ell - 1)/2 \rfloor$ equals the source's $\lceil \ell/2 - 1 \rceil$.

## Sources

- Naveen K. Godara and Prashant Tiwari, *The Higher Power Moments of the Coefficients of the Dedekind Zeta Function over a Polynomial in Six Variables*, INTEGERS 25 (2025), Article A101, Theorem 2.

Formalized by `MetaMathlibExt.dedekindSixSquaresA3`, a definition declared in [WantedExt/NumberTheory/DedekindZetaSixSquaresMomentsWanted.lean, line 102](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/DedekindZetaSixSquaresMomentsWanted.lean#L102). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/dirichlet-l-functions/moments-of-dedekind-zeta-coefficients-over-sums/index.html#dedekind-six-squares-a3).

## Values of $a_{0,\ell}$ and $a_{3,\ell}$ for $\ell = 3, 4, 5$

For a natural number $\ell$
let $a_{0,\ell} = 1 + \sum_{i=1}^{\lfloor \ell/2 \rfloor} \binom{\ell}{2i} C_i$, with $C_i$ the
$i$-th Catalan number, and let $a_{3,\ell}$ be the sum over the integers
$1 \le i \le \lfloor (\ell - 1)/2 \rfloor$ of $\binom{\ell}{2i+1}$ times the integer part of
$4\,(2i+1)!/((i-1)!\,(i+3)!)$. Then $(a_{0,3}, a_{3,3}) = (4, 1)$, $(a_{0,4}, a_{3,4}) = (9, 4)$
and $(a_{0,5}, a_{3,5}) = (21, 14)$.

## Sources

- Naveen K. Godara and Prashant Tiwari, *The Higher Power Moments of the Coefficients of the Dedekind Zeta Function over a Polynomial in Six Variables*, INTEGERS 25 (2025), Article A101, Table 1.

Formalized by `MetaMathlibExt.dedekindSixSquaresA0_A3_small`, a theorem declared in [WantedExt/NumberTheory/DedekindZetaSixSquaresMomentsWanted.lean, line 111](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/DedekindZetaSixSquaresMomentsWanted.lean#L111). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/dirichlet-l-functions/moments-of-dedekind-zeta-coefficients-over-sums/index.html#dedekind-six-squares-a0-a3-small).

## Second and third six-squares moments over a cubic field of negative discriminant

Let
$K$ be a number field of degree $3$ over $\mathbb{Q}$ with negative discriminant. For $n \ge 1$
let $a_K(n)$ be the number of ideals of the ring of integers of $K$ of absolute norm $n$ and
$r_6(n)$ the number of representations of $n$ as a sum of six squares of integers, and for real
$x$ and natural $\ell$ let $S_\ell(x) = \sum_{1 \le n \le x} r_6(n)\, a_K(n)^\ell$. Then there
are real constants $c_1, c_2$ such that for every $\varepsilon > 0$,
$S_2(x) = c_1 x^3 + c_2 x^3 \log x + O(x^{25/9 + \varepsilon})$ as $x \to \infty$, and there is
a real polynomial $P$ of degree $4$ such that for every $\varepsilon > 0$,
$S_3(x) = x^3 P(\log x) + O(x^{79/27 + \varepsilon})$ as $x \to \infty$.

A cubic field of negative discriminant is not normal over $\mathbb{Q}$.

## Sources

- Naveen K. Godara and Prashant Tiwari, *The Higher Power Moments of the Coefficients of the Dedekind Zeta Function over a Polynomial in Six Variables*, INTEGERS 25 (2025), Article A101, Theorem 1.

Stated but not proved: `MetaMathlibExt.sixSquaresDedekindMoment_two_three` is written with `theorem_wanted` in [WantedExt/NumberTheory/DedekindZetaSixSquaresMomentsWanted.lean, line 124](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/DedekindZetaSixSquaresMomentsWanted.lean#L124). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/dirichlet-l-functions/moments-of-dedekind-zeta-coefficients-over-sums/index.html#six-squares-dedekind-moment-two-three).

## Higher six-squares moments over a non-normal cubic field

Let $K$ be a number field of
degree $3$ over $\mathbb{Q}$ with negative discriminant and let $\ell \ge 4$. For $n \ge 1$ let
$a_K(n)$ be the number of ideals of the ring of integers of $K$ of absolute norm $n$ and $r_6(n)$
the number of representations of $n$ as a sum of six squares of integers, and for real $x$ let
$S_\ell(x) = \sum_{1 \le n \le x} r_6(n)\, a_K(n)^\ell$. Let
$a_{0,\ell} = 1 + \sum_{i=1}^{\lfloor \ell/2 \rfloor} \binom{\ell}{2i} C_i$, with $C_i$ the
$i$-th Catalan number, and let $a_{3,\ell}$ be the sum over the integers
$1 \le i \le \lfloor (\ell - 1)/2 \rfloor$ of $\binom{\ell}{2i+1}$ times the integer part of
$4\,(2i+1)!/((i-1)!\,(i+3)!)$. Then there is a real polynomial $P$ of degree
$a_{0,\ell} + a_{3,\ell} - 1$ such that for every $\varepsilon > 0$,
$S_\ell(x) - x^3 P(\log x) = O(x^{3 - 2/3^\ell + \varepsilon})$ as $x \to \infty$.

Such a field is not normal over $\mathbb{Q}$. The polynomial is called $P_\ell$ for even $\ell$
and $Q_\ell$ for odd $\ell$ in the source.

## Sources

- Naveen K. Godara and Prashant Tiwari, *The Higher Power Moments of the Coefficients of the Dedekind Zeta Function over a Polynomial in Six Variables*, INTEGERS 25 (2025), Article A101, Theorem 2.

Stated but not proved: `MetaMathlibExt.sixSquaresDedekindMoment_ge_four` is written with `theorem_wanted` in [WantedExt/NumberTheory/DedekindZetaSixSquaresMomentsWanted.lean, line 140](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/DedekindZetaSixSquaresMomentsWanted.lean#L140). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/dirichlet-l-functions/moments-of-dedekind-zeta-coefficients-over-sums/index.html#six-squares-dedekind-moment-ge-four).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Moments of Dedekind zeta coefficients over sums of six squares](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/dirichlet-l-functions/moments-of-dedekind-zeta-coefficients-over-sums/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/zeta-l-functions/dirichlet-l-functions/moments-of-dedekind-zeta-coefficients-over-sums)
