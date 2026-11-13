---
declaration: section
origin: cited
lean: MetaMathlibExt.squareful_two_pow_omega_LSeries_eq_zeta_quotient_fifteen, MetaMathlibExt.squareful_two_pow_omega_LSeries_eq_zeta_quotient_five, MetaMathlibExt.zeta_fourth_moment_le_uniform, MetaMathlibExt.inv_zeta_le_vinogradov_korobov, MetaMathlibExt.zeta_ne_zero_vinogradov_korobov, MetaMathlibExt.zeta_le_rpow_of_riemannHypothesis, MetaMathlibExt.inv_zeta_le_rpow_of_riemannHypothesis, MetaMathlibExt.squareful_two_pow_omega_sum_asymptotic
statement: formalized
---

# Mean value of 2^ω(n) over squareful numbers

8 results, 8 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/special-integer-classes/mean-value-of-2-n-over-squareful-numbers/index.html).

## Fine zeta factorization of the squareful $2^{\omega(n)}$ Dirichlet series

Let
$\omega(n)$ be the number of distinct prime factors of $n$, call $n$ squareful when $n \ne 0$ and
$p^2 \mid n$ for every prime $p \mid n$ (that is, $n$ is $2$-full), and let
$F(s) = \sum_{n \text{ squareful}} 2^{\omega(n)} n^{-s}$. There is a sequence
$h : \mathbb{N} \to \mathbb{C}$ whose Dirichlet series $H(s) = \sum_{n \ge 1} h(n) n^{-s}$
converges absolutely for $\operatorname{Re} s > 1/15$, such that for every complex $s$ with
$\operatorname{Re} s > 1/2$,

$$F(s) = \frac{\zeta(2s)^2 \zeta(3s)^2 \zeta(7s)^2 \zeta(8s)^4 \zeta(12s)^5 \zeta(13s)^{14}
\zeta(14s)^5}{\zeta(4s) \zeta(5s)^2 \zeta(6s)^3 \zeta(10s)^5 \zeta(11s)^6} H(s).$$

## Sources

- Kampamolla Venkatasubbareddy and Ayyadurai Sankaranarayanan, *On the Distribution of the Restricted Sequence of Integers 2^{ω(n)}*, INTEGERS 24 (2024), Article A110, Lemma 1.

Stated but not proved: `MetaMathlibExt.squareful_two_pow_omega_LSeries_eq_zeta_quotient_fifteen` is written with `theorem_wanted` in [WantedExt/NumberTheory/ArithmeticFunction/SquarefulTwoPowOmegaWanted.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ArithmeticFunction/SquarefulTwoPowOmegaWanted.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/special-integer-classes/mean-value-of-2-n-over-squareful-numbers/index.html#squareful-two-pow-omega-lseries-eq-zeta).

## Coarse zeta factorization of the squareful $2^{\omega(n)}$ Dirichlet series

Let
$\omega(n)$ be the number of distinct prime factors of $n$, call $n$ squareful when $n \ne 0$ and
$p^2 \mid n$ for every prime $p \mid n$ (that is, $n$ is $2$-full), and let
$F(s) = \sum_{n \text{ squareful}} 2^{\omega(n)} n^{-s}$. There is a sequence
$h : \mathbb{N} \to \mathbb{C}$ whose Dirichlet series $H(s) = \sum_{n \ge 1} h(n) n^{-s}$
converges absolutely for $\operatorname{Re} s > 1/5$, such that for every complex $s$ with
$\operatorname{Re} s > 1/2$,

$$F(s) = \frac{\zeta(2s)^2 \zeta(3s)^2}{\zeta(4s)} H(s).$$

## Sources

- Kampamolla Venkatasubbareddy and Ayyadurai Sankaranarayanan, *On the Distribution of the Restricted Sequence of Integers 2^{ω(n)}*, INTEGERS 24 (2024), Article A110, Lemma 2.

Stated but not proved: `MetaMathlibExt.squareful_two_pow_omega_LSeries_eq_zeta_quotient_five` is written with `theorem_wanted` in [WantedExt/NumberTheory/ArithmeticFunction/SquarefulTwoPowOmegaWanted.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ArithmeticFunction/SquarefulTwoPowOmegaWanted.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/special-integer-classes/mean-value-of-2-n-over-squareful-numbers/index.html#squareful-two-pow-omega-lseries-eq-zeta-2).

## Uniform fourth-moment bound for the Riemann zeta function

There are real constants $C$
and $T_0$ such that for every real $\sigma$ with $1/2 \le \sigma \le 1$ and every real
$T \ge T_0$,

$$\int_1^T |\zeta(\sigma + it)|^4 \, dt \le C T (\log T)^4.$$

## Sources

- Kampamolla Venkatasubbareddy and Ayyadurai Sankaranarayanan, *On the Distribution of the Restricted Sequence of Integers 2^{ω(n)}*, INTEGERS 24 (2024), Article A110, Lemma 4.

Stated but not proved: `MetaMathlibExt.zeta_fourth_moment_le_uniform` is written with `theorem_wanted` in [WantedExt/NumberTheory/ArithmeticFunction/SquarefulTwoPowOmegaWanted.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ArithmeticFunction/SquarefulTwoPowOmegaWanted.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/special-integer-classes/mean-value-of-2-n-over-squareful-numbers/index.html#zeta-fourth-moment-le-uniform).

## Vinogradov–Korobov bound for $1/\zeta$

Write $s = \sigma + it$ and
$g(T) = (\log T)^{2/3} (\log \log T)^{1/3}$. There are real constants $C > 0$, $K$ and
$T_0 \ge 3$ such that for every real $T$ and every complex $s$ with $T_0 < t \le T$ and
$\sigma \ge 1 - C / g(T)$, we have $\zeta(s) \ne 0$ and $|1/\zeta(s)| \le K g(T)$.

## Sources

- Kampamolla Venkatasubbareddy and Ayyadurai Sankaranarayanan, *On the Distribution of the Restricted Sequence of Integers 2^{ω(n)}*, INTEGERS 24 (2024), Article A110, Lemma 5.

Stated but not proved: `MetaMathlibExt.inv_zeta_le_vinogradov_korobov` is written with `theorem_wanted` in [WantedExt/NumberTheory/ArithmeticFunction/SquarefulTwoPowOmegaWanted.lean, line 90](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ArithmeticFunction/SquarefulTwoPowOmegaWanted.lean#L90). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/special-integer-classes/mean-value-of-2-n-over-squareful-numbers/index.html#inv-zeta-le-vinogradov-korobov).

## Vinogradov–Korobov zero-free region

There are real constants $C > 0$ and $t_0 \ge 3$
such that $\zeta(\sigma + it) \ne 0$ for all real $\sigma$ and $t$ with $|t| \ge t_0$ and
$\sigma \ge 1 - C / \bigl((\log |t|)^{2/3} (\log \log |t|)^{1/3}\bigr)$.

## Sources

- Kampamolla Venkatasubbareddy and Ayyadurai Sankaranarayanan, *On the Distribution of the Restricted Sequence of Integers 2^{ω(n)}*, INTEGERS 24 (2024), Article A110, Lemma 6.

Stated but not proved: `MetaMathlibExt.zeta_ne_zero_vinogradov_korobov` is written with `theorem_wanted` in [WantedExt/NumberTheory/ArithmeticFunction/SquarefulTwoPowOmegaWanted.lean, line 103](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ArithmeticFunction/SquarefulTwoPowOmegaWanted.lean#L103). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/special-integer-classes/mean-value-of-2-n-over-squareful-numbers/index.html#zeta-ne-zero-vinogradov-korobov).

## Lindelöf bound from the Riemann hypothesis

Assume the Riemann hypothesis, and let
$\varepsilon > 0$ be real. Then there are real constants $C$ and $t_0$ such that
$|\zeta(\sigma + it)| \le C |t|^{\varepsilon}$ for all real $\sigma$ and $t$ with
$1/2 \le \sigma \le 1$ and $|t| \ge t_0$.

## Sources

- Kampamolla Venkatasubbareddy and Ayyadurai Sankaranarayanan, *On the Distribution of the Restricted Sequence of Integers 2^{ω(n)}*, INTEGERS 24 (2024), Article A110, Lemma 8.

Stated but not proved: `MetaMathlibExt.zeta_le_rpow_of_riemannHypothesis` is written with `theorem_wanted` in [WantedExt/NumberTheory/ArithmeticFunction/SquarefulTwoPowOmegaWanted.lean, line 115](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ArithmeticFunction/SquarefulTwoPowOmegaWanted.lean#L115). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/special-integer-classes/mean-value-of-2-n-over-squareful-numbers/index.html#zeta-le-rpow-of-riemann-hypothesis).

## Bound for $1/\zeta$ from the Riemann hypothesis

Assume the Riemann hypothesis, and let
$1/2 < \sigma \le 1$ and $\varepsilon > 0$ be real. Then there are real constants $C$ and $t_0$,
depending on $\sigma$ and $\varepsilon$, such that $|1/\zeta(\sigma + it)| \le C |t|^{\varepsilon}$
for every real $t$ with $|t| \ge t_0$.

## Sources

- Kampamolla Venkatasubbareddy and Ayyadurai Sankaranarayanan, *On the Distribution of the Restricted Sequence of Integers 2^{ω(n)}*, INTEGERS 24 (2024), Article A110, Lemma 8.

Stated but not proved: `MetaMathlibExt.inv_zeta_le_rpow_of_riemannHypothesis` is written with `theorem_wanted` in [WantedExt/NumberTheory/ArithmeticFunction/SquarefulTwoPowOmegaWanted.lean, line 127](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ArithmeticFunction/SquarefulTwoPowOmegaWanted.lean#L127). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/special-integer-classes/mean-value-of-2-n-over-squareful-numbers/index.html#inv-zeta-le-rpow-of-riemann-hypothesis).

## Asymptotic for the sum of $2^{\omega(n)}$ over squareful $n$

Let $\omega(n)$ be the
number of distinct prime factors of $n$, and let $f(n) = 2^{\omega(n)}$ if $n$ is squareful
($n \ne 0$ and $p^2 \mid n$ for every prime $p \mid n$; so $f(1) = 1$) and $f(n) = 0$ otherwise.
There are real constants $C_1$, $C_2$, $C_3$, $C_4$, $c > 0$, $K$ and $x_0$ such that for every
real $x \ge x_0$,

$$\Bigl|\sum_{1 \le n \le x} f(n) - \bigl(C_1 x^{1/2} \log x + C_2 x^{1/2} +
C_3 x^{1/3} \log x + C_4 x^{1/3}\bigr)\Bigr| \le
K x^{1/4} \exp\Bigl(c \Bigl(\frac{\log x}{\log \log x}\Bigr)^{1/3}\Bigr).$$

The paper writes the coefficient as $c_\varepsilon$, "for some $c > 0$", after "let
$\varepsilon > 0$": a constant chosen after $\varepsilon$, not a product with an arbitrarily small
factor. Its proof (equations (28)–(30)) produces, with $T$ the height parameter of its contour,
the exponent $(4 + \varepsilon) c (\log T / \log \log T)^{1/3}$ with $\varepsilon$ small and
$c > 0$ the fixed constant of its contour shift to $\operatorname{Re} s = 1/4 - c/g(T)$, where
$g(T) = (\log T)^{2/3} (\log \log T)^{1/3}$, chosen in terms of the Vinogradov–Korobov
zero-free region and the bound for $1/\zeta$ there (its Lemmas 5 and 6), so the coefficient
stays bounded away from $0$ and the statement is one existential $c > 0$.

## Sources

- Kampamolla Venkatasubbareddy and Ayyadurai Sankaranarayanan, *On the Distribution of the Restricted Sequence of Integers 2^{ω(n)}*, INTEGERS 24 (2024), Article A110, Theorem 1.

Stated but not proved: `MetaMathlibExt.squareful_two_pow_omega_sum_asymptotic` is written with `theorem_wanted` in [WantedExt/NumberTheory/ArithmeticFunction/SquarefulTwoPowOmegaWanted.lean, line 146](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ArithmeticFunction/SquarefulTwoPowOmegaWanted.lean#L146). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/special-integer-classes/mean-value-of-2-n-over-squareful-numbers/index.html#squareful-two-pow-omega-sum-asymptotic).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Mean value of 2^ω(n) over squareful numbers](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/special-integer-classes/mean-value-of-2-n-over-squareful-numbers/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/arithmetic-functions/special-integer-classes/mean-value-of-2-n-over-squareful-numbers)
