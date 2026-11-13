---
declaration: section
origin: cited
lean: MetaMathlibExt.card_consecutivePrimePowerSums_length_le, MetaMathlibExt.maxConsecutivePrimePowerSumLength_isEquivalent, MetaMathlibExt.card_consecutivePrimePowerSums_le, MetaMathlibExt.card_consecutivePrimePowerSums_ge, MetaMathlibExt.maxChainLength_lt, MetaMathlibExt.le_maxChainLength, MetaMathlibExt.log_maxChainLength_bounds, MetaMathlibExt.gleefulRepCount_le
statement: formalized
---

# Sums of powers of consecutive primes

9 results, 9 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/additive-number-theory/sums-of-powers-of-consecutive-primes/index.html).

## Counting sums of a fixed number of consecutive prime powers

Let $p_1 < p_2 < \cdots$
be the primes. For natural numbers $k > 1$, $m > 0$ and $x$, the number of integers $n \le x$ of
the form $n = p_{\ell+1}^k + p_{\ell+2}^k + \cdots + p_{\ell+m}^k$ for some $\ell \ge 0$ is at
most $\pi(\lfloor (x/m)^{1/k} \rfloor)$, the number of primes up to $(x/m)^{1/k}$.

## Sources

- Cathal O'Sullivan, Jonathan P. Sorenson, and Aryn Stahl, *Algorithms and Bounds on the Sums of Powers of Consecutive Primes*, INTEGERS 24 (2024), Article A4, Lemma 1 (quoted from [6]).

Stated but not proved: `MetaMathlibExt.card_consecutivePrimePowerSums_length_le` is written with `theorem_wanted` in [WantedExt/NumberTheory/ConsecutivePrimePowerSumsWanted.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ConsecutivePrimePowerSumsWanted.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/additive-number-theory/sums-of-powers-of-consecutive-primes/index.html#card-consecutive-prime-power-sums-length).

## Length of the longest sum of consecutive prime powers

Let $p_1 < p_2 < \cdots$ be the
primes, let $k > 1$ be a natural number, and for a natural number $x$ let $M(x, k)$ be the
largest $m \le x$ with $p_1^k + p_2^k + \cdots + p_m^k \le x$. Then
$M(x, k) \sim (k + 1)\, x^{1/(k+1)} / (\log x)^{k/(k+1)}$ (asymptotic equivalence) as $x \to \infty$
through the natural numbers.

## Sources

- Cathal O'Sullivan, Jonathan P. Sorenson, and Aryn Stahl, *Algorithms and Bounds on the Sums of Powers of Consecutive Primes*, INTEGERS 24 (2024), Article A4, Lemma 2.

Stated but not proved: `MetaMathlibExt.maxConsecutivePrimePowerSumLength_isEquivalent` is written with `theorem_wanted` in [WantedExt/NumberTheory/ConsecutivePrimePowerSumsWanted.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ConsecutivePrimePowerSumsWanted.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/additive-number-theory/sums-of-powers-of-consecutive-primes/index.html#max-consecutive-prime-power-sum-length-i).

## Upper bound for the number of sums of consecutive prime powers

Let $p_1 < p_2 < \cdots$
be the primes and let $k > 1$ be a natural number. For a natural number $x$ let $s_k(x)$ be the
number of pairs $(\ell, m)$ of integers with $0 \le \ell < x$ and $1 \le m \le x$ such that
$p_{\ell+1}^k + \cdots + p_{\ell+m}^k \le x$. Then for every real $\varepsilon > 0$, for all
sufficiently large $x$,
$s_k(x) \le (1 + \varepsilon)\, c_k\, x^{2/(k+1)} / (\log x)^{2k/(k+1)}$, where
$c_k = \frac{k^2}{k-1} (k + 1)^{1 - 1/k}$.

## Sources

- Cathal O'Sullivan, Jonathan P. Sorenson, and Aryn Stahl, *Algorithms and Bounds on the Sums of Powers of Consecutive Primes*, INTEGERS 24 (2024), Article A4, Theorem 1.

Stated but not proved: `MetaMathlibExt.card_consecutivePrimePowerSums_le` is written with `theorem_wanted` in [WantedExt/NumberTheory/ConsecutivePrimePowerSumsWanted.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ConsecutivePrimePowerSumsWanted.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/additive-number-theory/sums-of-powers-of-consecutive-primes/index.html#card-consecutive-prime-power-sums-le).

## Lower bound for the number of sums of consecutive prime powers

Let $p_1 < p_2 < \cdots$
be the primes and let $k > 1$ be a natural number. For a natural number $x$ let $s_k(x)$ be the
number of pairs $(\ell, m)$ of integers with $0 \le \ell < x$ and $1 \le m \le x$ such that
$p_{\ell+1}^k + \cdots + p_{\ell+m}^k \le x$, and let $M(x, k)$ be the largest $m \le x$ with
$p_1^k + \cdots + p_m^k \le x$. Then $M(x, k)^2 / 2 \le s_k(x)$ for every $x$, and for every
real $\varepsilon > 0$, for all sufficiently large $x$,
$(1 - \varepsilon) (k + 1)^2 x^{2/(k+1)} / \bigl(2 (\log x)^{2k/(k+1)}\bigr) \le M(x, k)^2 / 2$.

## Sources

- Cathal O'Sullivan, Jonathan P. Sorenson, and Aryn Stahl, *Algorithms and Bounds on the Sums of Powers of Consecutive Primes*, INTEGERS 24 (2024), Article A4, Theorem 2.

Stated but not proved: `MetaMathlibExt.card_consecutivePrimePowerSums_ge` is written with `theorem_wanted` in [WantedExt/NumberTheory/ConsecutivePrimePowerSumsWanted.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ConsecutivePrimePowerSumsWanted.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/additive-number-theory/sums-of-powers-of-consecutive-primes/index.html#card-consecutive-prime-power-sums-ge).

## Upper bound for the maximal gleeful chain length

Let $p_1 = 2, p_2 = 3, \dots$ be the
primes in increasing order. Let $k > 1$, $M_0 \ge 6$, $M \ge M_0$ and $x$ be natural numbers with
$p_1^k + \cdots + p_M^k \le x < p_1^k + \cdots + p_{M+1}^k$. Put $y = M_0$,

$$B = \frac{\log(y+1)}{\log y} + \frac{\log\log((y+1)^2)}{\log y} \cdot \frac{k}{k+1}$$

and $C = (y/(y-1))^{1/(k+1)} B^{k/(k+1)}$, where $\log$ is the natural logarithm. Then

$$M < 4^{1/(k+1)} \cdot \frac{(k+1)\, x^{1/(k+1)}}{(\log x)^{k/(k+1)}} \cdot C.$$

## Sources

- Sara Moore and Jonathan P. Sorenson, *Explicit Bounds and Parallel Algorithms for Counting Multiply Gleeful Numbers*, INTEGERS 26 (2026), Article A84, Lemma 1, with `B`, `C` from Section 2.

Stated but not proved: `MetaMathlibExt.maxChainLength_lt` is written with `theorem_wanted` in [WantedExt/NumberTheory/GleefulNumbersWanted.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GleefulNumbersWanted.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/additive-number-theory/sums-of-powers-of-consecutive-primes/index.html#max-chain-length-lt).

## Lower bound for the maximal gleeful chain length

Let $p_1 = 2, p_2 = 3, \dots$ be the
primes in increasing order. Let $k > 1$, $M_0 \ge 6$, $M \ge M_0$ and $x$ be natural numbers with
$p_1^k + \cdots + p_M^k \le x < p_1^k + \cdots + p_{M+1}^k$. Put $y = M_0$ and

$$D = \frac{y}{y+3} \Big(\frac{\log(y/2)}{\log y + 2 \log\log(y+2)}\Big)^{k/(k+1)},$$

where $\log$ is the natural logarithm. Then

$$\frac{(k+1)\, x^{1/(k+1)}}{(\log x)^{k/(k+1)}} \cdot D \le M.$$

## Sources

- Sara Moore and Jonathan P. Sorenson, *Explicit Bounds and Parallel Algorithms for Counting Multiply Gleeful Numbers*, INTEGERS 26 (2026), Article A84, Lemma 2, with `D` from Section 2.

Stated but not proved: `MetaMathlibExt.le_maxChainLength` is written with `theorem_wanted` in [WantedExt/NumberTheory/GleefulNumbersWanted.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GleefulNumbersWanted.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/additive-number-theory/sums-of-powers-of-consecutive-primes/index.html#le-max-chain-length).

## Bounds for the logarithm of the maximal gleeful chain length

Let
$p_1 = 2, p_2 = 3, \dots$ be the primes in increasing order. Let $k > 1$, $M_0 \ge 6$, $M \ge M_0$
and $x$ be natural numbers with $p_1^k + \cdots + p_M^k \le x < p_1^k + \cdots + p_{M+1}^k$.
Put $y = M_0$, let $\log$ be the natural logarithm, and set

$$A = \frac{\log(y/2)}{\log y},$$



$$B = \frac{\log(y+1)}{\log y} + \frac{\log\log((y+1)^2)}{\log y} \cdot \frac{k}{k+1}.$$

Then

$$\frac{\log x}{k+1} \cdot \frac{1}{B} \le \log M < \frac{\log x}{k+1} \cdot \frac{1}{A}.$$

## Sources

- Sara Moore and Jonathan P. Sorenson, *Explicit Bounds and Parallel Algorithms for Counting Multiply Gleeful Numbers*, INTEGERS 26 (2026), Article A84, Lemma 3, with `A`, `B` from Section 2.

Stated but not proved: `MetaMathlibExt.log_maxChainLength_bounds` is written with `theorem_wanted` in [WantedExt/NumberTheory/GleefulNumbersWanted.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GleefulNumbersWanted.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/additive-number-theory/sums-of-powers-of-consecutive-primes/index.html#log-max-chain-length-bounds).

## Upper bound for the number of gleeful representations

Let $p_1 = 2, p_2 = 3, \dots$ be
the primes in increasing order, and for natural numbers $k$ and $x$ let $s_k(x)$ be the number
of pairs $(n, m)$ of natural numbers with $m \ge 1$ and $p_{n+1}^k + \cdots + p_{n+m}^k \le x$.
Let $k > 1$, $M_0 \ge 6$ and $x$ be natural numbers with $p_1^k + \cdots + p_{M_0}^k \le x$. Put
$y = M_0$, let $\log$ be the natural logarithm, and set

$$A = \frac{\log(y/2)}{\log y},$$



$$B = \frac{\log(y+1)}{\log y} + \frac{\log\log((y+1)^2)}{\log y} \cdot \frac{k}{k+1},$$



$$C = \Big(\frac{y}{y-1}\Big)^{1/(k+1)} B^{k/(k+1)}, \qquad E = 1 + \frac{1}{(k+1)A - 1},$$



$$F = \Big(\frac{y+1}{y}\Big)^{(k-1)/k} 4^{(k-1)/(k(k+1))} C^{(k-1)/k} E,$$

$U = 1.25506\,F$ and $c_k = \frac{k^2}{k-1} (k+1)^{(k-1)/k}$. Then

$$s_k(x) \le c_k \cdot \frac{x^{2/(k+1)}}{(\log x)^{2k/(k+1)}} \cdot U.$$

The paper prints the exponent of $\log x$ as $k/(k+1)$; its proof ends with $2k/(k+1)$, which
is stated here and implies the printed bound because $\log x \ge 1$.

## Sources

- Sara Moore and Jonathan P. Sorenson, *Explicit Bounds and Parallel Algorithms for Counting Multiply Gleeful Numbers*, INTEGERS 26 (2026), Article A84, Theorem 1 and its proof, with `c_k, A, B, C, E, F, U` from Section 2.

Stated but not proved: `MetaMathlibExt.gleefulRepCount_le` is written with `theorem_wanted` in [WantedExt/NumberTheory/GleefulNumbersWanted.lean, line 94](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GleefulNumbersWanted.lean#L94). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/additive-number-theory/sums-of-powers-of-consecutive-primes/index.html#gleeful-rep-count-le).

## Lower bound for the number of gleeful representations

Let $p_1 = 2, p_2 = 3, \dots$ be
the primes in increasing order, and for natural numbers $k$ and $x$ let $s_k(x)$ be the number
of pairs $(n, m)$ of natural numbers with $m \ge 1$ and $p_{n+1}^k + \cdots + p_{n+m}^k \le x$.
Let $k > 1$, $M_0 \ge 6$ and $x$ be natural numbers with $p_1^k + \cdots + p_{M_0}^k \le x$. Put
$y = M_0$, let $\log$ be the natural logarithm, and set

$$D = \frac{y}{y+3} \Big(\frac{\log(y/2)}{\log y + 2 \log\log(y+2)}\Big)^{k/(k+1)}$$

and $L = \frac{y-1}{y} D^2$. Then

$$\frac{(k+1)^2}{2} \cdot \frac{x^{2/(k+1)}}{(\log x)^{2k/(k+1)}} \cdot L \le s_k(x).$$

The paper prints the exponent of $\log x$ as $k/(k+1)$; its proof gives $2k/(k+1)$, which is
stated here. The printed form contradicts the upper bound for $s_k(x)$ for large $x$.

## Sources

- Sara Moore and Jonathan P. Sorenson, *Explicit Bounds and Parallel Algorithms for Counting Multiply Gleeful Numbers*, INTEGERS 26 (2026), Article A84, Theorem 2 and its proof, with `D`, `L` from Section 2.

Stated but not proved: `MetaMathlibExt.le_gleefulRepCount` is written with `theorem_wanted` in [WantedExt/NumberTheory/GleefulNumbersWanted.lean, line 121](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GleefulNumbersWanted.lean#L121). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/additive-number-theory/sums-of-powers-of-consecutive-primes/index.html#le-gleeful-rep-count).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Sums of powers of consecutive primes](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/additive-number-theory/sums-of-powers-of-consecutive-primes/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/additive-number-theory/sums-of-powers-of-consecutive-primes)
