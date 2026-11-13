---
declaration: section
origin: cited
lean: MetaMathlibExt.norm_sum_exp_two_pi_I_le_of_iteratedDeriv_two, MetaMathlibExt.exists_sqrt_cubic_equidistributed_mod_one, MetaMathlibExt.squarePyramidalNumber, MetaMathlibExt.squarePyramidalSquareDistance, MetaMathlibExt.squarePyramidalSquareDistance_examples, MetaMathlibExt.squarePyramidalSquareDistance_average_asymptotic, MetaMathlibExt.squarePyramidalSquareDistance_moment_asymptotic, MetaMathlibExt.squarePyramidal_dist_nearest_square_root_equidistributed
statement: formalized
---

# Square roots of cubic polynomials modulo one

10 results, 3 proved and 7 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/uniform-distribution-metric/square-roots-of-cubic-polynomials-modulo-one/index.html).

## Second-derivative test for exponential sums

Let $a < b$ be integers, let $\rho > 0$,
and let $f : \mathbb{R} \to \mathbb{R}$ be twice continuously differentiable, with either
$f''(t) \ge \rho$ for every $t \in [a, b]$ or $f''(t) \le -\rho$ for every $t \in [a, b]$. Then

$$\Bigl|\sum_{n=a}^{b} e(f(n))\Bigr| \le \bigl(|f'(b) - f'(a)| + 2\bigr)
\Bigl(\frac{4}{\sqrt{\rho}} + 3\Bigr),$$

where $e(x) = e^{2\pi i x}$.

Here $f$ is $C^2$ on all of $\mathbb{R}$; every $C^2$ function on $[a, b]$ extends to one, so
this loses nothing.

## Sources

- Anji Dong, Katerina Saettone, Kendra Song and Alexandru Zaharescu, *An Equidistribution Result for Differences Associated with Square Pyramidal Numbers*, Journal of Integer Sequences 29 (2026), Article 26.5.5, Lemma 4 (`jis-2026-26.5.5-lem-4`), quoted there from Kuipers and Niederreiter, *Uniform Distribution of Sequences*, Thm. 2.7.

Stated but not proved: `MetaMathlibExt.norm_sum_exp_two_pi_I_le_of_iteratedDeriv_two` is written with `theorem_wanted` in [WantedExt/NumberTheory/DiophantineApproximation/SqrtCubicEquidistributionWanted.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/DiophantineApproximation/SqrtCubicEquidistributionWanted.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/uniform-distribution-metric/square-roots-of-cubic-polynomials-modulo-one/index.html#norm-sum-exp-two-pi-i-le-of-iterated-der).

## Square roots of cubics with positive leading coefficient are uniformly distributed modulo one

**Square roots of cubics with positive leading coefficient are uniformly distributed modulo
one.** Let $q(t) = a t^3 + b t^2 + c t + d$ with real coefficients $a, b, c, d$ and $a > 0$,
write $\{x\} = x - \lfloor x \rfloor$ for the fractional part of a real $x$, and let
$e(x) = e^{2\pi i x}$. Then there is an integer $T \ge 1$ with three properties. First,
$q(t) > 0$ for every real $t \ge T$. Second, the sequence $\sqrt{q(T)}, \sqrt{q(T + 1)}, \dots$
is uniformly distributed modulo one: for all real $\alpha, \beta$ with $0 \le \alpha < \beta \le 1$,

$$\lim_{N \to \infty} \frac{1}{N}
\#\bigl\{0 \le n < N : \alpha \le \{\sqrt{q(T + n)}\} < \beta\bigr\} = \beta - \alpha.$$

Third, there is a real constant $C$ such that for every integer $N \ge T$ and every nonzero
integer $\gamma$,

$$\Bigl|\sum_{n=T}^{N} e\bigl(\gamma \sqrt{q(n)}\bigr)\Bigr| \le
C \bigl(|\gamma|^{1/2} N^{3/4} + |\gamma| N^{1/2} + |\gamma|^{-1/2} N^{1/4} + 1\bigr).$$

## Sources

- Anji Dong, Katerina Saettone, Kendra Song and Alexandru Zaharescu, *An Equidistribution Result for Differences Associated with Square Pyramidal Numbers*, Journal of Integer Sequences 29 (2026), Article 26.5.5, Proposition 6 (`jis-2026-26.5.5-prop-6`).

Stated but not proved: `MetaMathlibExt.exists_sqrt_cubic_equidistributed_mod_one` is written with `theorem_wanted` in [WantedExt/NumberTheory/DiophantineApproximation/SqrtCubicEquidistributionWanted.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/DiophantineApproximation/SqrtCubicEquidistributionWanted.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/uniform-distribution-metric/square-roots-of-cubic-polynomials-modulo-one/index.html#exists-sqrt-cubic-equidistributed-mod-on).

## Square pyramidal number

For a natural number $n$, the $n$-th square pyramidal number
is $P_n = 1^2 + 2^2 + \dots + n^2 = \sum_{i=1}^{n} i^2$ (so $P_0 = 0$).

## Sources

- Anji Dong, Katerina Saettone, Kendra Song and Alexandru Zaharescu, *An Equidistribution Result for Differences Associated with Square Pyramidal Numbers*, Journal of Integer Sequences 29 (2026), Article 26.5.5, equation (defn: square pyramidal number) of arXiv:2412.10097v2.

Formalized by `MetaMathlibExt.squarePyramidalNumber`, a definition declared in [WantedExt/NumberTheory/DiophantineApproximation/SqrtCubicEquidistributionWanted.lean, line 90](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/DiophantineApproximation/SqrtCubicEquidistributionWanted.lean#L90). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/uniform-distribution-metric/square-roots-of-cubic-polynomials-modulo-one/index.html#square-pyramidal-number).

## Distance from a square pyramidal number to the nearest square

For a natural number
$n$, let $P_n$ be the $n$-th square pyramidal number and $s = \lfloor \sqrt{P_n} \rfloor$. The
distance from $P_n$ to the nearest square is

$$a_n = \min\bigl(P_n - s^2, (s + 1)^2 - P_n\bigr).$$

Since $s^2 \le P_n < (s + 1)^2$, this is $a_n = |P_n - y_n^2|$, where $y_n^2$ is the square
nearest to $P_n$.

No ties occur, since the midpoint $m^2 + m + 1/2$ of two consecutive squares is never an integer.

## Sources

- Anji Dong, Katerina Saettone, Kendra Song and Alexandru Zaharescu, *An Equidistribution Result for Differences Associated with Square Pyramidal Numbers*, Journal of Integer Sequences 29 (2026), Article 26.5.5, equation (a_n first definition) of arXiv:2412.10097v2 (OEIS A351830).

Formalized by `MetaMathlibExt.squarePyramidalSquareDistance`, a definition declared in [WantedExt/NumberTheory/DiophantineApproximation/SqrtCubicEquidistributionWanted.lean, line 100](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/DiophantineApproximation/SqrtCubicEquidistributionWanted.lean#L100). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/uniform-distribution-metric/square-roots-of-cubic-polynomials-modulo-one/index.html#square-pyramidal-square-distance).

## Small square pyramidal numbers and their distances to squares

Let $P_n$ be the $n$-th
square pyramidal number and $a_n$ the distance from $P_n$ to the nearest square. Then
$P_1, P_2, P_3, P_4$ are $1, 5, 14, 30$; $a_2 = 1$ (since $P_2 = 5$ and the nearest square is
$4$); $P_{24} = 4900 = 70^2$; and $a_{24} = 0$ (the cannonball solution).

## Sources

- Anji Dong, Katerina Saettone, Kendra Song and Alexandru Zaharescu, *An Equidistribution Result for Differences Associated with Square Pyramidal Numbers*, Journal of Integer Sequences 29 (2026), Article 26.5.5, Introduction.

Formalized by `MetaMathlibExt.squarePyramidalSquareDistance_examples`, a theorem declared in [WantedExt/NumberTheory/DiophantineApproximation/SqrtCubicEquidistributionWanted.lean, line 110](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/DiophantineApproximation/SqrtCubicEquidistributionWanted.lean#L110). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/uniform-distribution-metric/square-roots-of-cubic-polynomials-modulo-one/index.html#square-pyramidal-square-distance-example).

## Average distance from square pyramidal numbers to the nearest square

Let $a_n$ be the
distance from the $n$-th square pyramidal number to the nearest square, and for real $x \ge 1$
let $A(x) = \frac{1}{x} \sum_{1 \le n \le x} a_n$. There is a real constant $C$ such that for
every real $x \ge 1$,

$$\Bigl|A(x) - \frac{x^{3/2}}{5\sqrt{3}}\Bigr| \le C x^{5/4},$$

that is, $A(x) = x^{3/2} / (5\sqrt{3}) + O(x^{5/4})$ with an absolute implied constant.

## Sources

- Anji Dong, Katerina Saettone, Kendra Song and Alexandru Zaharescu, *An Equidistribution Result for Differences Associated with Square Pyramidal Numbers*, Journal of Integer Sequences 29 (2026), Article 26.5.5, Theorem 1 (`jis-2026-26.5.5-thm-1`); arXiv:2412.10097v2 states the error `O(x^{17/12})`.

Stated but not proved: `MetaMathlibExt.squarePyramidalSquareDistance_average_asymptotic` is written with `theorem_wanted` in [WantedExt/NumberTheory/DiophantineApproximation/SqrtCubicEquidistributionWanted.lean, line 128](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/DiophantineApproximation/SqrtCubicEquidistributionWanted.lean#L128). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/uniform-distribution-metric/square-roots-of-cubic-polynomials-modulo-one/index.html#square-pyramidal-square-distance-average).

## Moments of the distance from square pyramidal numbers to the nearest square

Let $a_n$
be the distance from the $n$-th square pyramidal number to the nearest square, and for a
positive integer $k$ and real $x \ge 1$ let $M_k(x) = \sum_{1 \le n \le x} a_n^k$. For every
positive integer $k$ there is a real constant $C_k$ such that for every real $x \ge 1$,

$$\Bigl|M_k(x) - \frac{x^{3k/2 + 1}}{3^{k/2} (3k/2 + 1)(k + 1)}\Bigr| \le C_k x^{3k/2 + 3/4}.$$

## Sources

- Anji Dong, Katerina Saettone, Kendra Song and Alexandru Zaharescu, *An Equidistribution Result for Differences Associated with Square Pyramidal Numbers*, Journal of Integer Sequences 29 (2026), Article 26.5.5, Theorem 3 (`jis-2026-26.5.5-thm-3`); arXiv:2412.10097v2 states the error `O_k(x^{3k/2 + 11/12})`.

Stated but not proved: `MetaMathlibExt.squarePyramidalSquareDistance_moment_asymptotic` is written with `theorem_wanted` in [WantedExt/NumberTheory/DiophantineApproximation/SqrtCubicEquidistributionWanted.lean, line 140](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/DiophantineApproximation/SqrtCubicEquidistributionWanted.lean#L140). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/uniform-distribution-metric/square-roots-of-cubic-polynomials-modulo-one/index.html#square-pyramidal-square-distance-moment).

## The distance from the square root of a square pyramidal number to the nearest integer is uniformly distributed

**The distance from the square root of a square pyramidal number to the nearest integer is
uniformly distributed.** Let $P_n$ be the $n$-th square pyramidal number, write
$\|x\| = |x - \operatorname{round}(x)|$ for the distance from a real $x$ to the nearest integer,
and let $(y_n)_{n \ge 0}$ be natural numbers such that $|P_n - y_n^2| \le |P_n - z^2|$ for all
natural numbers $n$ and $z$ (so $y_n^2$ is a square nearest to $P_n$). Put
$d_n = |\sqrt{P_n} - y_n|$. Then $d_n = \|\sqrt{P_n}\|$ and $d_n \le 1/2$ for every $n \ge 0$,
and $(d_n)_{n \ge 1}$ is uniformly distributed in $[0, 1/2]$: for all real $\alpha, \beta$ with
$0 \le \alpha < \beta \le 1/2$,

$$\lim_{N \to \infty} \frac{1}{N}
\#\{1 \le n \le N : \alpha \le d_n \le \beta\} = 2(\beta - \alpha).$$

The source shows that $y_n$ is unique, and takes the limit over real $x \to \infty$, which is
equivalent to the limit along integers $N$.

## Sources

- Anji Dong, Katerina Saettone, Kendra Song and Alexandru Zaharescu, *An Equidistribution Result for Differences Associated with Square Pyramidal Numbers*, Journal of Integer Sequences 29 (2026), Article 26.5.5, Proposition 9 (`jis-2026-26.5.5-prop-9`).

Stated but not proved: `MetaMathlibExt.squarePyramidal_dist_nearest_square_root_equidistributed` is written with `theorem_wanted` in [WantedExt/NumberTheory/DiophantineApproximation/SqrtCubicEquidistributionWanted.lean, line 158](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/DiophantineApproximation/SqrtCubicEquidistributionWanted.lean#L158). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/uniform-distribution-metric/square-roots-of-cubic-polynomials-modulo-one/index.html#square-pyramidal-dist-nearest-square-roo).

## Fourier expansion of a power of the distance to the nearest integer

Let $k$ be a
positive integer, let $g(u) = |u - \operatorname{round}(u)|^k$ be the $k$-th power of the
distance from a real $u$ to the nearest integer, let $e(x) = e^{2\pi i x}$, and for every
integer $m$ let $c(m) = \int_0^1 g(u)\, e(-mu)\, du$. Then $c(0) = 1/(2^k (k + 1))$, the mean of
$g$ over a period; there is a real constant $C$ with $|c(m)| \le C / m^2$ for every integer
$m \ne 0$; the series $\sum_{m \in \mathbb{Z}} |c(m)|$ converges; the symmetric partial sums
$\sum_{|m| \le H} c(m)\, e(mu)$ converge to $g(u)$ uniformly in real $u$ as $H \to \infty$; and
there is a real constant $C'$ such that for every integer $H \ge 1$ and every real $u$,

$$\Bigl|g(u) - c(0) - \sum_{0 < |m| \le H} c(m)\, e(mu)\Bigr| \le \frac{C'}{H}.$$

## Sources

- Anji Dong, Katerina Saettone, Kendra Song and Alexandru Zaharescu, *An Equidistribution Result for Differences Associated with Square Pyramidal Numbers*, Journal of Integer Sequences 29 (2026), Article 26.5.5, Lemma 10 (`jis-2026-26.5.5-lem-10`).

Stated but not proved: `MetaMathlibExt.dist_round_pow_fourier_expansion` is written with `theorem_wanted` in [WantedExt/NumberTheory/DiophantineApproximation/SqrtCubicEquidistributionWanted.lean, line 181](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/DiophantineApproximation/SqrtCubicEquidistributionWanted.lean#L181). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/uniform-distribution-metric/square-roots-of-cubic-polynomials-modulo-one/index.html#dist-round-pow-fourier-expansion).

## Power sums of the distance from the square root of a square pyramidal number to the nearest integer

**Power sums of the distance from the square root of a square pyramidal number to the nearest
integer.** Let $P_n$ be the $n$-th square pyramidal number and write
$\|x\| = |x - \operatorname{round}(x)|$ for the distance from a real $x$ to the nearest integer.
For every positive integer $k$ there is a real constant $C_k$ such that for every real $t \ge 1$,

$$\Bigl|\sum_{1 \le n \le t} \|\sqrt{P_n}\|^k - \frac{t}{2^k (k + 1)}\Bigr| \le C_k t^{3/4},$$

that is, with $\mu_k = 1/(2^k (k + 1))$ and $G_k(t) = \sum_{1 \le n \le t} \|\sqrt{P_n}\|^k$,
one has $G_k(t) = \mu_k t + O_k(t^{3/4})$.

The source writes $h(n) = \sqrt{n(n+1)(2n+1)/6}$, which is $\sqrt{P_n}$.

## Sources

- Anji Dong, Katerina Saettone, Kendra Song and Alexandru Zaharescu, *An Equidistribution Result for Differences Associated with Square Pyramidal Numbers*, Journal of Integer Sequences 29 (2026), Article 26.5.5, Lemma 11 (`jis-2026-26.5.5-lem-11`).

Stated but not proved: `MetaMathlibExt.sum_dist_round_sqrt_squarePyramidal_pow` is written with `theorem_wanted` in [WantedExt/NumberTheory/DiophantineApproximation/SqrtCubicEquidistributionWanted.lean, line 204](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/DiophantineApproximation/SqrtCubicEquidistributionWanted.lean#L204). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/uniform-distribution-metric/square-roots-of-cubic-polynomials-modulo-one/index.html#sum-dist-round-sqrt-square-pyramidal-pow).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Square roots of cubic polynomials modulo one](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/uniform-distribution-metric/square-roots-of-cubic-polynomials-modulo-one/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/diophantine-approximation/uniform-distribution-metric/square-roots-of-cubic-polynomials-modulo-one)
