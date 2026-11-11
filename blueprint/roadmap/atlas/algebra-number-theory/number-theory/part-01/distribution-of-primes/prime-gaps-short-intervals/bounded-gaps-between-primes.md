---
declaration: section
origin: cited
lean: WantedExt.NumberTheory.Polymath8b.SubpowerBound, WantedExt.NumberTheory.Polymath8b.DyadicSupport, WantedExt.NumberTheory.Polymath8b.DivisorLogBound, WantedExt.NumberTheory.Polymath8b.SiegelWalfisz, WantedExt.NumberTheory.Polymath8b.ElliottHalberstamAt, WantedExt.NumberTheory.Polymath8b.GeneralizedElliottHalberstamAt, WantedExt.NumberTheory.Polymath8b.ElliottHalberstam, WantedExt.NumberTheory.Polymath8b.GeneralizedElliottHalberstam
statement: formalized
---

# Bounded gaps between primes

25 results, 14 proved and 11 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/bounded-gaps-between-primes/index.html).

## Subpower bound

For functions $f, g : \mathbb{R} \to \mathbb{R}$, $f$ is bounded by $g$ up
to subpower losses if for every real $\delta > 0$ we have $f(x) = O(x^{\delta} g(x))$ as
$x \to \infty$.

## Sources

- Polymath8b, arXiv:1407.4897v4, Definition 1.6.

Formalized by `WantedExt.NumberTheory.Polymath8b.SubpowerBound`, a definition declared in [WantedExt/NumberTheory/PrimeGapBoundsHypotheses.lean, line 34](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/PrimeGapBoundsHypotheses.lean#L34). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/bounded-gaps-between-primes/index.html#subpower-bound).

## Support in a dyadic interval

A finitely supported sequence
$\alpha : \mathbb{N} \to \mathbb{R}$ is supported in the dyadic interval at scale
$N \in \mathbb{R}$ if every $n$ with $\alpha(n) \ne 0$ satisfies $n \ge 1$ and $N \le n \le 2N$.

## Sources

- Polymath8b v4, Claim 2.6.

Formalized by `WantedExt.NumberTheory.Polymath8b.DyadicSupport`, a definition declared in [WantedExt/NumberTheory/PrimeGapBoundsHypotheses.lean, line 39](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/PrimeGapBoundsHypotheses.lean#L39). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/bounded-gaps-between-primes/index.html#dyadic-support).

## Divisor–logarithm bound for a family of sequences

A family $(\alpha_x)_{x \in \mathbb{R}}$
of finitely supported sequences $\alpha_x : \mathbb{N} \to \mathbb{R}$ satisfies the
divisor–logarithm bound if there are a real number $C > 0$ and natural numbers $k$ and $l$ such
that for all sufficiently large real $x$ and all integers $n \ge 1$,

$$|\alpha_x(n)| \le C \, \tau(n)^k (\log x)^l,$$

where $\tau(n)$ is the number of positive divisors of $n$. The constants $C$, $k$ and $l$ depend
neither on $x$ nor on $n$.

## Sources

- Polymath8b v4, Claim 2.6.

Formalized by `WantedExt.NumberTheory.Polymath8b.DivisorLogBound`, a definition declared in [WantedExt/NumberTheory/PrimeGapBoundsHypotheses.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/PrimeGapBoundsHypotheses.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/bounded-gaps-between-primes/index.html#divisor-log-bound).

## Siegel–Walfisz hypothesis for a family of sequences

Let $(\beta_x)_{x \in \mathbb{R}}$
be a family of finitely supported sequences $\beta_x : \mathbb{N} \to \mathbb{R}$ and let
$M : \mathbb{R} \to \mathbb{R}$. The family satisfies the Siegel–Walfisz hypothesis at scale $M$
if for every real $A \ge 1$ there are a real number $C > 0$ and a natural number $k$ such that,
for all sufficiently large real $x$ and all natural numbers $q \ge 1$, $r \ge 1$ and $a$ with
$\gcd(a, q) = 1$,

$$|\Delta(\beta_x^{(r)}; a \bmod q)| \le C \, \tau(qr)^k \, M(x) / (\log x)^A.$$

Here $\beta_x^{(r)}$ is the sequence equal to $\beta_x(n)$ when $\gcd(n, r) = 1$ and to $0$
otherwise, $\Delta(\cdot\,; a \bmod q)$ is the discrepancy in the residue class of $a$ modulo $q$,
and $\tau(m)$ is the number of positive divisors of $m$.

## Sources

- Polymath8b v4, Claim 2.6 and its uniformity footnote.

Formalized by `WantedExt.NumberTheory.Polymath8b.SiegelWalfisz`, a definition declared in [WantedExt/NumberTheory/PrimeGapBoundsHypotheses.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/PrimeGapBoundsHypotheses.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/bounded-gaps-between-primes/index.html#siegel-walfisz).

## Elliott–Halberstam estimate at level $\theta$

For a real number $\theta$, the
Elliott–Halberstam estimate at level $\theta$ is the following statement. Let
$Q : \mathbb{R} \to \mathbb{N}$ be such that $Q(x) = O(x^{\delta} x^{\theta})$ as $x \to \infty$
for every real $\delta > 0$, and let $A \ge 1$ be real. Then there is a real number $C > 0$ such
that for all sufficiently large real $x$, the averaged discrepancy of $\Lambda_x$ up to $Q(x)$ is
at most $C x / (\log x)^A$. Here $\Lambda_x$ is the sequence equal to the von Mangoldt function
$\Lambda(n)$ for integers $n \ge 1$ with $x \le n \le 2x$ and to $0$ otherwise, and the averaged
discrepancy of a sequence $\alpha$ up to $Q$ is $\sum_{q=1}^{Q} \Delta^*(\alpha; q)$, where
$\Delta^*(\alpha; q)$ is the largest absolute value of the discrepancy of $\alpha$ in a residue
class modulo $q$ coprime to $q$.

## Sources

- Polymath8b v4, Claim 2.2.

Formalized by `WantedExt.NumberTheory.Polymath8b.ElliottHalberstamAt`, a definition declared in [WantedExt/NumberTheory/PrimeGapBoundsHypotheses.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/PrimeGapBoundsHypotheses.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/bounded-gaps-between-primes/index.html#elliott-halberstam-at).

## Generalized Elliott–Halberstam estimate at level $\theta$

For a real number $\theta$,
the generalized Elliott–Halberstam estimate at level $\theta$ is the following statement. Let
$\varepsilon > 0$ be real, let $N, M : \mathbb{R} \to \mathbb{R}$, and let
$(\alpha_x)_{x \in \mathbb{R}}$ and $(\beta_x)_{x \in \mathbb{R}}$ be families of finitely
supported sequences $\mathbb{N} \to \mathbb{R}$. Assume that for all sufficiently large real $x$
we have $N(x) > 0$ and $M(x) > 0$, $\alpha_x$ is supported in the dyadic interval at scale
$N(x)$ and $\beta_x$ is supported in the dyadic interval at scale $M(x)$; that for every real
$\delta > 0$, as $x \to \infty$, $x^{\varepsilon} = O(x^{\delta} N(x))$,
$N(x) = O(x^{\delta} x^{1 - \varepsilon})$, $x^{\varepsilon} = O(x^{\delta} M(x))$ and
$M(x) = O(x^{\delta} x^{1 - \varepsilon})$; that $N(x) M(x) = O(x)$ and $x = O(N(x) M(x))$ as
$x \to \infty$; that both families satisfy the divisor–logarithm bound; and that
$(\beta_x)$ satisfies the Siegel–Walfisz hypothesis at scale $M$. Let
$Q : \mathbb{R} \to \mathbb{N}$ be such that $Q(x) = O(x^{\delta} x^{\theta})$ as $x \to \infty$
for every real $\delta > 0$, and let $A \ge 1$ be real. Then there is a real number $C > 0$ such
that for all sufficiently large real $x$, the averaged discrepancy of the multiplicative
convolution $\alpha_x \star \beta_x$ up to $Q(x)$ is at most $C x / (\log x)^A$.

## Sources

- Polymath8b v4, Claim 2.6.

Formalized by `WantedExt.NumberTheory.Polymath8b.GeneralizedElliottHalberstamAt`, a definition declared in [WantedExt/NumberTheory/PrimeGapBoundsHypotheses.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/PrimeGapBoundsHypotheses.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/bounded-gaps-between-primes/index.html#generalized-elliott-halberstam-at).

## Elliott–Halberstam conjecture (dyadic form)

The Elliott–Halberstam estimate at level
$\theta$ holds for every real number $\theta$ with $0 < \theta < 1$.

## Sources

- Polymath8b v4, Theorems 1.1 and 1.3 and Claim 2.2.

Formalized by `WantedExt.NumberTheory.Polymath8b.ElliottHalberstam`, a definition declared in [WantedExt/NumberTheory/PrimeGapBoundsHypotheses.lean, line 82](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/PrimeGapBoundsHypotheses.lean#L82). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/bounded-gaps-between-primes/index.html#elliott-halberstam).

## Generalized Elliott–Halberstam conjecture (dyadic form)

The generalized
Elliott–Halberstam estimate at level $\theta$ holds for every real number $\theta$ with
$0 < \theta < 1$.

## Sources

- Polymath8b v4, Theorem 1.4 and Claim 2.6.

Formalized by `WantedExt.NumberTheory.Polymath8b.GeneralizedElliottHalberstam`, a definition declared in [WantedExt/NumberTheory/PrimeGapBoundsHypotheses.lean, line 87](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/PrimeGapBoundsHypotheses.lean#L87). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/bounded-gaps-between-primes/index.html#generalized-elliott-halberstam).

## Zhang's 2014 bound on prime gaps

Let $p_0 < p_1 < p_2 < \cdots$ be the primes in
increasing order. Then $\liminf_{n \to \infty} (p_{n+1} - p_n) \le 70\,000\,000$, where the
liminf is taken in $\mathbb{N} \cup \{\infty\}$.

## Sources

- Zhang, Annals of Mathematics 179 (2014), 1121-1174; Polymath8b v4, Theorem 1.2.

Stated but not proved: `WantedExt.NumberTheory.PrimeGapBounds.zhang2014UpperBound` is written with `theorem_wanted` in [WantedExt/NumberTheory/PrimeGapBoundsWanted.lean, line 34](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/PrimeGapBoundsWanted.lean#L34). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/bounded-gaps-between-primes/index.html#zhang2014-upper-bound).

## Polymath8a bound 4680 on small prime gaps

Let $p_0 < p_1 < p_2 < \cdots$ be the primes
in increasing order. Then $\liminf_{n \to \infty} (p_{n+1} - p_n) \le 4680$, where the liminf is
taken in $\mathbb{N} \cup \{\infty\}$.

## Sources

- Polymath, Algebra & Number Theory 8 (2014), 2067-2199; Polymath8b v4, Introduction.

Stated but not proved: `WantedExt.NumberTheory.PrimeGapBounds.polymath8a2014UpperBound` is written with `theorem_wanted` in [WantedExt/NumberTheory/PrimeGapBoundsWanted.lean, line 38](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/PrimeGapBoundsWanted.lean#L38). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/bounded-gaps-between-primes/index.html#polymath8a2014-upper-bound).

## Maynard's bound 600 on small prime gaps

Let $p_0 < p_1 < p_2 < \cdots$ be the primes in
increasing order. Then $\liminf_{n \to \infty} (p_{n+1} - p_n) \le 600$, where the liminf is
taken in $\mathbb{N} \cup \{\infty\}$.

The bound was also obtained independently by Tao.

## Sources

- Maynard, Annals of Mathematics 181 (2015), 383-413; Polymath8b v4, Theorem 1.3(i).

Stated but not proved: `WantedExt.NumberTheory.PrimeGapBounds.maynard2015UpperBound` is written with `theorem_wanted` in [WantedExt/NumberTheory/PrimeGapBoundsWanted.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/PrimeGapBoundsWanted.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/bounded-gaps-between-primes/index.html#maynard2015-upper-bound).

## Polymath8b bound 246 on small prime gaps

Let $p_0 < p_1 < p_2 < \cdots$ be the primes in
increasing order. Then $\liminf_{n \to \infty} (p_{n+1} - p_n) \le 246$, where the liminf is
taken in $\mathbb{N} \cup \{\infty\}$.

The bound is the one stated in the original arXiv version v4; whether the 2015 erratum affects it
is unresolved.

## Sources

- Polymath8b, arXiv:1407.4897v4, Theorem 1.4(i), DOI 10.1186/s40687-014-0012-7.

Stated but not proved: `WantedExt.NumberTheory.PrimeGapBounds.polymath8b2014UpperBound` is written with `theorem_wanted` in [WantedExt/NumberTheory/PrimeGapBoundsWanted.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/PrimeGapBoundsWanted.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/bounded-gaps-between-primes/index.html#polymath8b2014-upper-bound).

## Zhang's 2026 bound of 240 on prime gaps

Let $p_0 < p_1 < p_2 < \cdots$ be the primes in
increasing order. Then $\liminf_{n \to \infty} (p_{n+1} - p_n) \le 240$, where the liminf is
taken in $\mathbb{N} \cup \{\infty\}$.

## Sources

- Zhang, Zenodo 10.5281/zenodo.22135842, 28 August 2026, as quoted in constants/88a.md.

Stated but not proved: `WantedExt.NumberTheory.PrimeGapBounds.zhang2026UpperBound` is written with `theorem_wanted` in [WantedExt/NumberTheory/PrimeGapBoundsWanted.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/PrimeGapBoundsWanted.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/bounded-gaps-between-primes/index.html#zhang2026-upper-bound).

## OpenAI's bound 186 on small prime gaps

Let $p_0 < p_1 < p_2 < \cdots$ be the primes in
increasing order. Then $\liminf_{n \to \infty} (p_{n+1} - p_n) \le 186$, where the liminf is
taken in $\mathbb{N} \cup \{\infty\}$.

## Sources

- OpenAI, Improved short gaps between primes, 30 August 2026, quoted in constants/88a.md.

Stated but not proved: `WantedExt.NumberTheory.PrimeGapBounds.openai2026UpperBound` is written with `theorem_wanted` in [WantedExt/NumberTheory/PrimeGapBoundsWanted.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/PrimeGapBoundsWanted.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/bounded-gaps-between-primes/index.html#openai2026-upper-bound).

## Stadlmann's bound 240 on small prime gaps

Let $p_0 < p_1 < p_2 < \cdots$ be the primes
in increasing order. Then $\liminf_{n \to \infty} (p_{n+1} - p_n) \le 240$, where the liminf is
taken in $\mathbb{N} \cup \{\infty\}$.

## Sources

- Stadlmann, arXiv:2608.31126, 31 August 2026, as quoted in constants/88a.md.

Stated but not proved: `WantedExt.NumberTheory.PrimeGapBounds.stadlmann2026UpperBound` is written with `theorem_wanted` in [WantedExt/NumberTheory/PrimeGapBoundsWanted.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/PrimeGapBoundsWanted.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/bounded-gaps-between-primes/index.html#stadlmann2026-upper-bound).

## Maynard's bound under Elliott–Halberstam

Let $p_0 < p_1 < p_2 < \cdots$ be the primes in
increasing order. If the Elliott–Halberstam conjecture holds at every level $\theta$ with
$0 < \theta < 1$, in Polymath8b's dyadic form, then $\liminf_{n \to \infty} (p_{n+1} - p_n) \le 12$,
where the liminf is taken in $\mathbb{N} \cup \{\infty\}$.

## Sources

- Maynard (2015); Polymath8b v4, Theorem 1.3(iii).

Stated but not proved: `WantedExt.NumberTheory.PrimeGapBounds.maynardElliottHalberstamUpperBound` is written with `theorem_wanted` in [WantedExt/NumberTheory/PrimeGapBoundsWanted.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/PrimeGapBoundsWanted.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/bounded-gaps-between-primes/index.html#maynard-elliott-halberstam-upper-bound).

## Goldston–Pintz–Yıldırım bound under Elliott–Halberstam

Let $p_0 < p_1 < p_2 < \cdots$
be the primes in increasing order. If the Elliott–Halberstam conjecture holds at every level
$\theta$ with $0 < \theta < 1$, in Polymath8b's dyadic form, then
$\liminf_{n \to \infty} (p_{n+1} - p_n) \le 16$, where the liminf is taken in
$\mathbb{N} \cup \{\infty\}$.

## Sources

- Goldston-Pintz-Yıldırım (2009); Polymath8b v4, Theorem 1.1.

Stated but not proved: `WantedExt.NumberTheory.PrimeGapBounds.gpyElliottHalberstamUpperBound` is written with `theorem_wanted` in [WantedExt/NumberTheory/PrimeGapBoundsWanted.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/PrimeGapBoundsWanted.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/bounded-gaps-between-primes/index.html#gpy-elliott-halberstam-upper-bound).

## Polymath8b bound under the generalized Elliott–Halberstam conjecture

Let
$p_0 < p_1 < p_2 < \cdots$ be the primes in increasing order. If the generalized
Elliott–Halberstam conjecture holds at every level $\theta$ with $0 < \theta < 1$, in Polymath8b's
dyadic form, then $\liminf_{n \to \infty} (p_{n+1} - p_n) \le 6$, where the liminf is taken in
$\mathbb{N} \cup \{\infty\}$.

## Sources

- Polymath8b v4, Theorem 1.4(xii); the 2015 erratum correction is unavailable.

Stated but not proved: `WantedExt.NumberTheory.PrimeGapBounds.polymath8bGeneralizedElliottHalberstamUpperBound` is written with `theorem_wanted` in [WantedExt/NumberTheory/PrimeGapBoundsWanted.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/PrimeGapBoundsWanted.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/bounded-gaps-between-primes/index.html#polymath8b-generalized-elliott-halbersta).

## Two primes in infinitely many translates of an admissible 40-tuple

Let
$h_1, \dots, h_{40}$ be distinct integers forming an admissible tuple: for every prime $p$, some
residue class modulo $p$ contains none of the $h_i$. Then there are infinitely many natural
numbers $n$ such that at least two of the integers $n + h_1, \dots, n + h_{40}$ are prime.

A negative integer or zero is never counted as prime.

## Sources

- OpenAI (2026), Theorem 1.1, as quoted in the 186 row of constants/88a.md.

Stated but not proved: `WantedExt.NumberTheory.PrimeGapBounds.openai2026DHL` is written with `theorem_wanted` in [WantedExt/NumberTheory/PrimeGapBoundsWanted.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/PrimeGapBoundsWanted.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/bounded-gaps-between-primes/index.html#openai2026-dhl).

## The forty shifts behind the bound 186

The list of the forty integers
$0, 2, 6, 12, 20, 26, 30, 32, 36, 42, 48, 50, 56, 60, 68, 72, 78, 86, 90, 92, 98, 102, 110,
116, 120, 126, 132, 138, 140, 146, 152, 156, 158, 162, 168, 170, 176, 180, 182, 186$, in this
order.

## Sources

- OpenAI (2026), equation (1.3).

Formalized by `WantedExt.NumberTheory.PrimeGapBounds.shifts186`, a definition declared in [WantedExt/NumberTheory/PrimeGapBoundsWanted.lean, line 86](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/PrimeGapBoundsWanted.lean#L86). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/bounded-gaps-between-primes/index.html#shifts186).

## The explicit 40-tuple for the gap bound 186

The $40$-tuple of integers
$h = (h_0, \dots, h_{39})$ whose entries, in order, are $0, 2, 6, 12, 20, 26, 30, 32, 36, 42,
48, 50, 56, 60, 68, 72, 78, 86, 90, 92, 98, 102, 110, 116, 120, 126, 132, 138, 140, 146, 152,
156, 158, 162, 168, 170, 176, 180, 182, 186$.

## Sources

- OpenAI (2026), equation (1.3), and the 186 row of constants/88a.md.

Formalized by `WantedExt.NumberTheory.PrimeGapBounds.tuple186`, a definition declared in [WantedExt/NumberTheory/PrimeGapBoundsWanted.lean, line 93](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/PrimeGapBoundsWanted.lean#L93). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/bounded-gaps-between-primes/index.html#tuple186).

## The explicit 40-tuple has distinct entries

Let $h = (h_0, \dots, h_{39})$ be the
explicit $40$-tuple of integers $(0, 2, 6, \dots, 182, 186)$. Then the entries of $h$ are
pairwise distinct: $h_i = h_j$ implies $i = j$.

## Sources

- the explicit tuple in OpenAI (2026), equation (1.3).

Formalized by `WantedExt.NumberTheory.PrimeGapBounds.tuple186_injective`, a theorem declared in [WantedExt/NumberTheory/PrimeGapBoundsWanted.lean, line 97](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/PrimeGapBoundsWanted.lean#L97). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/bounded-gaps-between-primes/index.html#tuple186-injective).

## The entries of the explicit 40-tuple lie between 0 and 186

Let
$h = (h_0, \dots, h_{39})$ be the explicit $40$-tuple of integers $(0, 2, 6, \dots, 182, 186)$.
Then $0 \le h_i \le 186$ for every $i \in \{0, \dots, 39\}$.

## Sources

- the explicit tuple in OpenAI (2026), equation (1.3).

Formalized by `WantedExt.NumberTheory.PrimeGapBounds.tuple186_bounds`, a theorem declared in [WantedExt/NumberTheory/PrimeGapBoundsWanted.lean, line 101](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/PrimeGapBoundsWanted.lean#L101). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/bounded-gaps-between-primes/index.html#tuple186-bounds).

## The explicit 40-tuple has diameter 186

Let $h = (h_0, \dots, h_{39})$ be the explicit
$40$-tuple of integers $(0, 2, 6, \dots, 182, 186)$. The largest value in the set
$\{h_0, \dots, h_{39}\}$ minus the smallest value in it equals $186$.

## Sources

- OpenAI (2026), equation (1.3), as quoted in constants/88a.md.

Formalized by `WantedExt.NumberTheory.PrimeGapBounds.tuple186_diameter`, a theorem declared in [WantedExt/NumberTheory/PrimeGapBoundsWanted.lean, line 105](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/PrimeGapBoundsWanted.lean#L105). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/bounded-gaps-between-primes/index.html#tuple186-diameter).

## The explicit 40-tuple is admissible

Let $h = (h_0, \dots, h_{39})$ be the explicit
$40$-tuple of integers $(0, 2, 6, \dots, 182, 186)$. Then $h$ is Hardy–Littlewood admissible:
for every prime $p$, the number of residue classes modulo $p$ that contain an entry of $h$ is
not $p$.

## Sources

- OpenAI (2026), equation (1.3).

Formalized by `WantedExt.NumberTheory.PrimeGapBounds.tuple186_admissible`, a theorem declared in [WantedExt/NumberTheory/PrimeGapBoundsWanted.lean, line 130](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/PrimeGapBoundsWanted.lean#L130). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/bounded-gaps-between-primes/index.html#tuple186-admissible).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Bounded gaps between primes](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/bounded-gaps-between-primes/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/distribution-of-primes/prime-gaps-short-intervals/bounded-gaps-between-primes)
