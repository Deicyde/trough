---
declaration: section
origin: cited
lean: MetaMathlibExt.centralBinomPowSum, MetaMathlibExt.centralBinomPowSum_zero, MetaMathlibExt.centralBinomPowSum_succ, MetaMathlibExt.centralBinomPowSum_oddHarmonic_recursion, MetaMathlibExt.centralBinomPowSum_harmonic_recursion, MetaMathlibExt.centralBinomPowSum_harmonic_two_mul_recursion, MetaMathlibExt.centralBinomPowSum_oddHarmonic_one_two_three, MetaMathlibExt.centralBinomPowSum_harmonic_one_two_three
statement: formalized
---

# Central binomial sums with harmonic numbers

19 results, 3 proved and 16 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/central-binomial-harmonic-sums/central-binomial-sums-with-harmonic-numbers/index.html).

## Weighted central binomial sum

For a sequence $a = (a_k)_{k \ge 0}$ of rational numbers
and natural numbers $r$ and $n$, the weighted central binomial sum is the rational number

$$S_r^a(n) = \sum_{k=0}^{n} \binom{2k}{k} 4^{-k} k^r a_k,$$

with the convention $0^0 = 1$.

Taking $a_k = 1$, $a_k = O_k$ (the odd harmonic numbers), $a_k = H_k$ and $a_k = H_{2k}$ (the
harmonic numbers) gives the paper's sums $S_r(n)$, $S_r^O(n)$, $S_r^H(n)$ and $S_r^{2H}(n)$.

## Sources

- Kunle Adegoke and Robert Frontczak, *Three Classes of Combinatorial Sums Involving Central Binomial Coefficients and Harmonic Numbers*, INTEGERS 26 (2026), Article A109, equations (1), (8), (9), (10).

Formalized by `MetaMathlibExt.centralBinomPowSum`, a definition declared in [WantedExt/Combinatorics/Enumerative/CentralBinomHarmonicSumsWanted.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/CentralBinomHarmonicSumsWanted.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/central-binomial-harmonic-sums/central-binomial-sums-with-harmonic-numbers/index.html#central-binom-pow-sum).

## The weighted central binomial sum at zero

For every sequence $a$ of rational numbers and
every natural number $r$, the weighted central binomial sum
$S_r^a(n) = \sum_{k=0}^{n} \binom{2k}{k} 4^{-k} k^r a_k$ satisfies $S_r^a(0) = 0^r a_0$, with
the convention $0^0 = 1$.

## Sources

- Kunle Adegoke and Robert Frontczak, *Three Classes of Combinatorial Sums Involving Central Binomial Coefficients and Harmonic Numbers*, INTEGERS 26 (2026), Article A109, equations (1), (8)-(10).

Formalized by `MetaMathlibExt.centralBinomPowSum_zero`, a theorem declared in [WantedExt/Combinatorics/Enumerative/CentralBinomHarmonicSumsWanted.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/CentralBinomHarmonicSumsWanted.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/central-binomial-harmonic-sums/central-binomial-sums-with-harmonic-numbers/index.html#central-binom-pow-sum-zero).

## Adding one term to the weighted central binomial sum

For every sequence $a$ of rational
numbers and all natural numbers $r$ and $n$, the weighted central binomial sum
$S_r^a(n) = \sum_{k=0}^{n} \binom{2k}{k} 4^{-k} k^r a_k$ (with $0^0 = 1$) satisfies

$$S_r^a(n+1) = S_r^a(n) + \binom{2n+2}{n+1} 4^{-(n+1)} (n+1)^r a_{n+1}.$$

## Sources

- Kunle Adegoke and Robert Frontczak, *Three Classes of Combinatorial Sums Involving Central Binomial Coefficients and Harmonic Numbers*, INTEGERS 26 (2026), Article A109, equations (1), (8)-(10).

Formalized by `MetaMathlibExt.centralBinomPowSum_succ`, a theorem declared in [WantedExt/Combinatorics/Enumerative/CentralBinomHarmonicSumsWanted.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/CentralBinomHarmonicSumsWanted.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/central-binomial-harmonic-sums/central-binomial-sums-with-harmonic-numbers/index.html#central-binom-pow-sum-succ).

## Recurrence for central binomial sums with odd harmonic numbers

For a natural number $n$,
let $O_m = \sum_{i=1}^{m} 1/(2i-1)$ be the odd harmonic numbers, $c_n = \binom{2n}{n}/4^n$, and
for natural $r$ let $S_r(n) = \sum_{k=0}^{n} \binom{2k}{k} 4^{-k} k^r$ and
$S_r^O(n) = \sum_{k=0}^{n} \binom{2k}{k} 4^{-k} k^r O_k$, with $0^0 = 1$. Then

$$S_0^O(n) = c_n \big((2n+1) O_n - 2n\big),$$

and for every $r \ge 1$

$$(2r+1) S_r^O(n) = n^r c_n \big((2n+1) O_n + 1\big) - S_r(n) +
2 \sum_{j=1}^{r-1} \binom{r}{j+1} (-1)^{j+1} S_{r-j}^O(n).$$

## Sources

- Kunle Adegoke and Robert Frontczak, *Three Classes of Combinatorial Sums Involving Central Binomial Coefficients and Harmonic Numbers*, INTEGERS 26 (2026), Article A109, Theorem 1.

Stated but not proved: `MetaMathlibExt.centralBinomPowSum_oddHarmonic_recursion` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/CentralBinomHarmonicSumsWanted.lean, line 87](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/CentralBinomHarmonicSumsWanted.lean#L87). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/central-binomial-harmonic-sums/central-binomial-sums-with-harmonic-numbers/index.html#central-binom-pow-sum-odd-harmonic-recur).

## Recurrence for central binomial sums with harmonic numbers

For a natural number $n$,
let $H_m = \sum_{i=1}^{m} 1/i$ be the harmonic numbers, $c_n = \binom{2n}{n}/4^n$, and for natural
$r$ let $S_r(n) = \sum_{k=0}^{n} \binom{2k}{k} 4^{-k} k^r$ and
$S_r^H(n) = \sum_{k=0}^{n} \binom{2k}{k} 4^{-k} k^r H_k$, with $0^0 = 1$. Then

$$S_0^H(n) = (2n+1)\, c_n (H_n - 2) + 2,$$

and for every $r \ge 1$

$$(2r+1) S_r^H(n) = n^r (2n+1)\, c_n (H_n + 1) + 2(-1)^r - S_r(n) +
2 \sum_{j=1}^{r-1} \binom{r}{j+1} (-1)^{j+1} S_{r-j}^H(n) -
2 \sum_{j=0}^{r} \binom{r+1}{j} (-1)^{r-j} S_j(n).$$

## Sources

- Kunle Adegoke and Robert Frontczak, *Three Classes of Combinatorial Sums Involving Central Binomial Coefficients and Harmonic Numbers*, INTEGERS 26 (2026), Article A109, Theorem 2.

Stated but not proved: `MetaMathlibExt.centralBinomPowSum_harmonic_recursion` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/CentralBinomHarmonicSumsWanted.lean, line 105](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/CentralBinomHarmonicSumsWanted.lean#L105). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/central-binomial-harmonic-sums/central-binomial-sums-with-harmonic-numbers/index.html#central-binom-pow-sum-harmonic-recursion).

## Recurrence for central binomial sums with harmonic numbers of even index

For a natural
number $n$, let $H_m = \sum_{i=1}^{m} 1/i$ be the harmonic numbers, $c_n = \binom{2n}{n}/4^n$,
and for natural $r$ let $S_r(n) = \sum_{k=0}^{n} \binom{2k}{k} 4^{-k} k^r$ and
$S_r^{2H}(n) = \sum_{k=0}^{n} \binom{2k}{k} 4^{-k} k^r H_{2k}$, with $0^0 = 1$. Then

$$S_0^{2H}(n) = c_n \big((2n+1) H_{2n} - (4n+1)\big) + 1;$$

for every $r \ge 1$

$$(2r+1) S_r^{2H}(n) = n^r c_n \Big((2n+1) H_{2n} + n + \frac{3}{2}\Big) + (-1)^r -
\frac{3}{2} S_r(n) + 2 \sum_{j=1}^{r-1} \binom{r}{j+1} (-1)^{j+1} S_{r-j}^{2H}(n) -
\sum_{j=0}^{r} \binom{r+1}{j} (-1)^{r-j} S_j(n);$$

and

$$S_1^{2H}(n) = \frac{1}{9} c_n \big(3n(2n+1) H_{2n} - 4n^2 + 7n + 3\big) - \frac{1}{3}.$$

## Sources

- Kunle Adegoke and Robert Frontczak, *Three Classes of Combinatorial Sums Involving Central Binomial Coefficients and Harmonic Numbers*, INTEGERS 26 (2026), Article A109, Theorem 3.

Stated but not proved: `MetaMathlibExt.centralBinomPowSum_harmonic_two_mul_recursion` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/CentralBinomHarmonicSumsWanted.lean, line 125](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/CentralBinomHarmonicSumsWanted.lean#L125). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/central-binomial-harmonic-sums/central-binomial-sums-with-harmonic-numbers/index.html#central-binom-pow-sum-harmonic-two-mul-r).

## Odd harmonic central binomial sums for powers one to three

For every natural number $n$,
let $O_m = \sum_{i=1}^{m} 1/(2i-1)$ be the odd harmonic numbers, $c_n = \binom{2n}{n}/4^n$, and
$S_r^O(n) = \sum_{k=0}^{n} \binom{2k}{k} 4^{-k} k^r O_k$. Then

$$S_1^O(n) = (2n+1)\, c_n \frac{n}{3} \Big(O_{n+1} - \frac{1}{3}\Big),$$



$$S_2^O(n) = (2n+1)\, c_n \frac{n}{15} \Big((3n+2) O_{n+1} - \frac{9n+16}{15}\Big),$$



$$S_3^O(n) = (2n+1)\, c_n \frac{n}{105} \Big((15n^2 + 18n + 2) O_{n+1} -
\frac{225n^2 + 648n + 352}{105}\Big).$$

## Sources

- Kunle Adegoke and Robert Frontczak, *Three Classes of Combinatorial Sums Involving Central Binomial Coefficients and Harmonic Numbers*, INTEGERS 26 (2026), Article A109, Corollary 1.

Stated but not proved: `MetaMathlibExt.centralBinomPowSum_oddHarmonic_one_two_three` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/CentralBinomHarmonicSumsWanted.lean, line 147](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/CentralBinomHarmonicSumsWanted.lean#L147). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/central-binomial-harmonic-sums/central-binomial-sums-with-harmonic-numbers/index.html#central-binom-pow-sum-odd-harmonic-one-t).

## Central binomial sums with harmonic numbers for powers one to three

For every natural
number $n$, let $H_m = \sum_{i=1}^{m} 1/i$ be the harmonic numbers, $c_n = \binom{2n}{n}/4^n$,
and $S_r^H(n) = \sum_{k=0}^{n} \binom{2k}{k} 4^{-k} k^r H_k$. Then

$$S_1^H(n) = \frac{1}{3} (2n+1)\, c_n \Big(n H_n - \frac{2n}{3} + 2\Big) - \frac{2}{3},$$



$$S_2^H(n) = \frac{1}{5} (2n+1)\, c_n \Big(\frac{n}{3} (3n+2) H_n -
\frac{2}{45} (9n^2 - 14n + 15)\Big) + \frac{2}{15},$$



$$S_3^H(n) = \frac{1}{7} (2n+1)\, c_n \Big(\frac{n}{15} (15n^2 + 18n + 2) H_n -
\frac{2}{1575} (225n^3 - 297n^2 + 37n + 105)\Big) + \frac{2}{105}.$$

## Sources

- Kunle Adegoke and Robert Frontczak, *Three Classes of Combinatorial Sums Involving Central Binomial Coefficients and Harmonic Numbers*, INTEGERS 26 (2026), Article A109, Corollary 2.

Stated but not proved: `MetaMathlibExt.centralBinomPowSum_harmonic_one_two_three` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/CentralBinomHarmonicSumsWanted.lean, line 163](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/CentralBinomHarmonicSumsWanted.lean#L163). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/central-binomial-harmonic-sums/central-binomial-sums-with-harmonic-numbers/index.html#central-binom-pow-sum-harmonic-one-two-t).

## Stirling numbers from derivatives of powers of one minus the exponential

For all natural
numbers $k$, $r$ and $v$, write ${a \brace b}$ for the Stirling numbers of the second kind and
${a \brace b}_v$ for the r-Stirling numbers of the second kind with parameter $v$, and use the
convention $0^0 = 1$. Then the real functions $x \mapsto (1 - e^x)^k$ and
$x \mapsto (1 - e^x)^k e^{vx}$ satisfy

$$\frac{d^r}{dx^r} (1 - e^x)^k \Big|_{x=0} = \sum_{p=0}^{k} (-1)^p \binom{k}{p} p^r =
(-1)^k k! {r \brace k}$$

and

$$\frac{d^r}{dx^r} (1 - e^x)^k e^{vx} \Big|_{x=0} = \sum_{p=0}^{k} (-1)^p \binom{k}{p} (v+p)^r =
(-1)^k k! {r+v \brace k+v}_v.$$

## Sources

- Kunle Adegoke and Robert Frontczak, *Three Classes of Combinatorial Sums Involving Central Binomial Coefficients and Harmonic Numbers*, INTEGERS 26 (2026), Article A109, Lemma 1.

Stated but not proved: `MetaMathlibExt.iteratedDeriv_one_sub_exp_pow` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/CentralBinomHarmonicSumsWanted.lean, line 183](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/CentralBinomHarmonicSumsWanted.lean#L183). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/central-binomial-harmonic-sums/central-binomial-sums-with-harmonic-numbers/index.html#iterated-deriv-one-sub-exp-pow).

## Power sums of $\binom{t}{k}(H_t - H_{t-k})$ in r-Stirling form

Let $t$ be a complex
number that is not an integer. For complex $x$ write $\binom{x}{k} = x(x-1)\cdots(x-k+1)/k!$,
and write $H_x = \psi(x+1) + \gamma$, where $\psi$ is the digamma function and $\gamma$ is the
Euler–Mascheroni constant (only differences $H_x - H_y = \psi(x+1) - \psi(y+1)$ occur below).
Let ${a \brace b}_c$ denote the r-Stirling numbers of the second kind. For all natural numbers
$n$ and $r$ (with $0^0 = 1$),

$$\sum_{k=0}^{n} (-1)^k k^r \binom{t}{k} (H_t - H_{t-k}) =
\sum_{k=0}^{\min(r,n)} (-1)^k k! {r+n-k \brace n}_{n-k} \binom{n-t}{n-k} (H_{k-t} - H_{n-t}).$$

## Sources

- Kunle Adegoke and Robert Frontczak, *Three Classes of Combinatorial Sums Involving Central Binomial Coefficients and Harmonic Numbers*, INTEGERS 26 (2026), Article A109, Theorem 4.

Stated but not proved: `MetaMathlibExt.sum_choose_harmonic_diff_rStirling` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/CentralBinomHarmonicSumsWanted.lean, line 201](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/CentralBinomHarmonicSumsWanted.lean#L201). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/central-binomial-harmonic-sums/central-binomial-sums-with-harmonic-numbers/index.html#sum-choose-harmonic-diff-r-stirling).

## Power sums of $\binom{t}{k}(H_t - H_{t-k})$ for exponents up to three

Let $n$ be a
natural number and $t$ a complex number that is not an integer. For complex $x$ write
$\binom{x}{k} = x(x-1)\cdots(x-k+1)/k!$, and write $H_x = \psi(x+1) + \gamma$, where $\psi$ is
the digamma function and $\gamma$ is the Euler–Mascheroni constant (only differences
$H_x - H_y = \psi(x+1) - \psi(y+1)$ occur below). For natural $r$ let
$L_r = \sum_{k=0}^{n} (-1)^k k^r \binom{t}{k} (H_t - H_{t-k})$ (with $0^0 = 1$), and for natural
$j$ let $A_j = \binom{n-t}{n-j} (H_{j-t} - H_{n-t})$ if $j \le n$ and $A_j = 0$ if $j > n$. Then
$L_0 = A_0$, $L_1 = -A_1 + n A_0$, $L_2 = 2 A_2 - (2n-1) A_1 + n^2 A_0$ and
$L_3 = -6 A_3 + 6(n-1) A_2 - (3n^2 - 3n + 1) A_1 + n^3 A_0$.

These are the cases $r = 0, 1, 2, 3$ of the paper's Theorem 4.

## Sources

- Kunle Adegoke and Robert Frontczak, *Three Classes of Combinatorial Sums Involving Central Binomial Coefficients and Harmonic Numbers*, INTEGERS 26 (2026), Article A109, Proposition 1.

Stated but not proved: `MetaMathlibExt.sum_choose_harmonic_diff_pow_le_three` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/CentralBinomHarmonicSumsWanted.lean, line 218](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/CentralBinomHarmonicSumsWanted.lean#L218). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/central-binomial-harmonic-sums/central-binomial-sums-with-harmonic-numbers/index.html#sum-choose-harmonic-diff-pow-le-three).

## Odd harmonic central binomial sums via r-Stirling numbers

For natural numbers $n$ and
$r$, let $O_m = \sum_{i=1}^{m} 1/(2i-1)$ be the odd harmonic numbers, ${a \brace b}_s$ the
r-Stirling numbers of the second kind, and $S_r^O(n) = \sum_{k=0}^{n} \binom{2k}{k} 4^{-k} k^r O_k$,
with $0^0 = 1$. Then

$$S_r^O(n) = \frac{1}{4^n} \sum_{k=0}^{\min(r,n)} (-1)^k k! {r+n-k \brace n}_{n-k} 4^k
\binom{2n+1}{2k+1} \binom{2(n-k)}{n-k} \binom{n}{k}^{-1} (O_{n+1} - O_{k+1}).$$

Moreover $S_0^O(n) = (2n+1) \binom{2n}{n} 4^{-n} (O_{n+1} - 1)$ and
$S_1^O(n) = \frac{n(2n+1)}{3} \binom{2n}{n} 4^{-n} \big(O_{n+1} - \frac{1}{3}\big)$.

## Sources

- Kunle Adegoke and Robert Frontczak, *Three Classes of Combinatorial Sums Involving Central Binomial Coefficients and Harmonic Numbers*, INTEGERS 26 (2026), Article A109, Proposition 2.

Stated but not proved: `MetaMathlibExt.centralBinomPowSum_oddHarmonic_eq_rStirling` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/CentralBinomHarmonicSumsWanted.lean, line 237](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/CentralBinomHarmonicSumsWanted.lean#L237). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/central-binomial-harmonic-sums/central-binomial-sums-with-harmonic-numbers/index.html#central-binom-pow-sum-odd-harmonic-eq-r).

## Central binomial sums weighted by $1 - O_{k-1}$, in r-Stirling form

Let
$O_m = \sum_{j=1}^{m} \frac{1}{2j-1}$ be the odd harmonic numbers (so $O_0 = 0$) and let
${a \brace b}_c$ denote the r-Stirling numbers of the second kind. For all natural numbers $n$ and
$r$,

$$\sum_{k=1}^{n} \frac{k^r \binom{2k}{k}}{4^k (2k-1)} (1 - O_{k-1}) =
\frac{\binom{2n}{n}}{4^n} \sum_{k=0}^{\min(r,n)} (-1)^k k! {r+n-k \brace n}_{n-k}
\binom{n}{k} \frac{4^k}{\binom{2k}{k}} (O_n - O_k),$$

and in particular

$$\sum_{k=1}^{n} \frac{\binom{2k}{k}}{4^k (2k-1)} (1 - O_{k-1}) = \frac{\binom{2n}{n}}{4^n} O_n.$$

## Sources

- Kunle Adegoke and Robert Frontczak, *Three Classes of Combinatorial Sums Involving Central Binomial Coefficients and Harmonic Numbers*, INTEGERS 26 (2026), Article A109, Proposition 3.

Stated but not proved: `MetaMathlibExt.sum_centralBinom_one_sub_oddHarmonic_eq_rStirling` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/CentralBinomHarmonicSumsWanted.lean, line 257](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/CentralBinomHarmonicSumsWanted.lean#L257). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/central-binomial-harmonic-sums/central-binomial-sums-with-harmonic-numbers/index.html#sum-central-binom-one-sub-odd-harmonic-e).

## Power-weighted convolution of $4^k$ with $\binom{2m}{m} O_m$

Let
$O_m = \sum_{j=1}^{m} \frac{1}{2j-1}$ be the odd harmonic numbers (so $O_0 = 0$) and let
${r \brace k}$ denote the Stirling numbers of the second kind. For all natural numbers $n$ and $r$
(with $0^0 = 1$),

$$\sum_{k=0}^{n} 4^k \binom{2(n-k)}{n-k} k^r O_{n-k} =
(2n+1) \binom{2n}{n} \sum_{k=0}^{r} \frac{4^k\, k!}{(2k+1) \binom{2k}{k}} {r \brace k}
\binom{n}{k} (O_{n+1} - O_{k+1}).$$

## Sources

- Kunle Adegoke and Robert Frontczak, *Three Classes of Combinatorial Sums Involving Central Binomial Coefficients and Harmonic Numbers*, INTEGERS 26 (2026), Article A109, Proposition 4.

Stated but not proved: `MetaMathlibExt.sum_four_pow_centralBinom_oddHarmonic_eq_stirling` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/CentralBinomHarmonicSumsWanted.lean, line 275](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/CentralBinomHarmonicSumsWanted.lean#L275). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/central-binomial-harmonic-sums/central-binomial-sums-with-harmonic-numbers/index.html#sum-four-pow-central-binom-odd-harmonic).

## Power-weighted convolution of $4^k$ with $\binom{2m}{m} (1 - O_{m-1})/(2m-1)$

Let
$O_m = \sum_{j=1}^{m} \frac{1}{2j-1}$ be the odd harmonic numbers (so $O_0 = 0$) and let
${r \brace k}$ denote the Stirling numbers of the second kind. For all natural numbers $n$ and $r$
(with $0^0 = 1$),

$$\sum_{k=0}^{n-1} \frac{4^k}{2(n-k)-1} \binom{2(n-k)}{n-k} k^r (1 - O_{n-k-1}) =
\binom{2n}{n} \sum_{k=0}^{r} \frac{4^k}{\binom{2k}{k}} k! {r \brace k} \binom{n}{k}
(O_n - O_k).$$

## Sources

- Kunle Adegoke and Robert Frontczak, *Three Classes of Combinatorial Sums Involving Central Binomial Coefficients and Harmonic Numbers*, INTEGERS 26 (2026), Article A109, Proposition 5.

Stated but not proved: `MetaMathlibExt.sum_four_pow_centralBinom_one_sub_oddHarmonic_eq_stirling` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/CentralBinomHarmonicSumsWanted.lean, line 288](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/CentralBinomHarmonicSumsWanted.lean#L288). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/central-binomial-harmonic-sums/central-binomial-sums-with-harmonic-numbers/index.html#sum-four-pow-central-binom-one-sub-odd-h).

## Alternating reciprocal central binomial sum with $O_{n+1} - O_{k+1}$

Let
$O_m = \sum_{j=1}^{m} \frac{1}{2j-1}$ be the odd harmonic numbers (so $O_0 = 0$) and let
${r \brace k}$ denote the Stirling numbers of the second kind. For all natural numbers $n$ and $r$
(with $0^0 = 1$),

$$\sum_{k=0}^{n} \frac{(-1)^k}{2k+1} \binom{n}{k} \frac{4^k}{\binom{2k}{k}} k^r
(O_{n+1} - O_{k+1}) =
\frac{1}{(2n+1)\binom{2n}{n}} \sum_{k=0}^{\min(r,n)} (-1)^k k! {r \brace k} 4^k
\binom{2(n-k)}{n-k} O_{n-k}.$$

## Sources

- Kunle Adegoke and Robert Frontczak, *Three Classes of Combinatorial Sums Involving Central Binomial Coefficients and Harmonic Numbers*, INTEGERS 26 (2026), Article A109, Proposition 6.

Stated but not proved: `MetaMathlibExt.sum_alternating_inv_centralBinom_oddHarmonic_eq_stirling` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/CentralBinomHarmonicSumsWanted.lean, line 303](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/CentralBinomHarmonicSumsWanted.lean#L303). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/central-binomial-harmonic-sums/central-binomial-sums-with-harmonic-numbers/index.html#sum-alternating-inv-central-binom-odd-ha).

## Alternating reciprocal central binomial sum with $O_n - O_k$

Let
$O_m = \sum_{j=1}^{m} \frac{1}{2j-1}$ be the odd harmonic numbers (so $O_0 = 0$) and let
${r \brace k}$ denote the Stirling numbers of the second kind. For all natural numbers $n$ and $r$
(with $0^0 = 1$),

$$\sum_{k=0}^{n} (-1)^k \binom{n}{k} \frac{4^k}{\binom{2k}{k}} k^r (O_n - O_k) =
\frac{1}{\binom{2n}{n}} \sum_{k=0}^{\min(r,\, n-1)} \frac{(-1)^k}{2(n-k)-1}\, k! {r \brace k}
4^k \binom{2(n-k)}{n-k} (1 - O_{n-k-1}),$$

where the right-hand sum is empty when $n = 0$.

The paper's right-hand sum runs over all $k \le r$; its term $k = n$ vanishes there because
$1 - O_{-1} = 0$, so it is dropped here.

## Sources

- Kunle Adegoke and Robert Frontczak, *Three Classes of Combinatorial Sums Involving Central Binomial Coefficients and Harmonic Numbers*, INTEGERS 26 (2026), Article A109, Proposition 7.

Stated but not proved: `MetaMathlibExt.sum_alternating_inv_centralBinom_oddHarmonic_sub_eq_stirling` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/CentralBinomHarmonicSumsWanted.lean, line 319](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/CentralBinomHarmonicSumsWanted.lean#L319). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/central-binomial-harmonic-sums/central-binomial-sums-with-harmonic-numbers/index.html#sum-alternating-inv-central-binom-odd-ha-2).

## Power sums of $\binom{t}{n-k}(H_t - H_{t-n+k})$ in Stirling form

Let $t$ be a complex
number that is not an integer. For complex $x$ write $\binom{x}{k} = x(x-1)\cdots(x-k+1)/k!$,
and write $H_x = \psi(x+1) + \gamma$, where $\psi$ is the digamma function and $\gamma$ is the
Euler–Mascheroni constant (only differences $H_x - H_y = \psi(x+1) - \psi(y+1)$ occur below).
Let ${r \brace k}$ denote the Stirling numbers of the second kind. For all natural numbers $n$
and $r$ (with $0^0 = 1$),

$$\sum_{k=0}^{n} (-1)^k \binom{t}{n-k} k^r (H_t - H_{t-n+k}) =
(-1)^n \sum_{k=0}^{\min(r,n)} k! {r \brace k} \binom{n-t}{n-k} (H_{k-t} - H_{n-t}).$$

## Sources

- Kunle Adegoke and Robert Frontczak, *Three Classes of Combinatorial Sums Involving Central Binomial Coefficients and Harmonic Numbers*, INTEGERS 26 (2026), Article A109, Theorem 5.

Stated but not proved: `MetaMathlibExt.sum_choose_sub_harmonic_diff_stirling` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/CentralBinomHarmonicSumsWanted.lean, line 334](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/CentralBinomHarmonicSumsWanted.lean#L334). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/central-binomial-harmonic-sums/central-binomial-sums-with-harmonic-numbers/index.html#sum-choose-sub-harmonic-diff-stirling).

## Power sums of $\binom{n-t}{n-k}(H_{k-t} - H_{n-t})$ in Stirling form

Let $t$ be a
complex number that is not an integer. For complex $x$ write
$\binom{x}{k} = x(x-1)\cdots(x-k+1)/k!$, and write $H_x = \psi(x+1) + \gamma$, where $\psi$ is
the digamma function and $\gamma$ is the Euler–Mascheroni constant (only differences
$H_x - H_y = \psi(x+1) - \psi(y+1)$ occur below). Let ${r \brace k}$ denote the Stirling numbers
of the second kind. For all natural numbers $n$ and $r$ (with $0^0 = 1$),

$$\sum_{k=0}^{n} (-1)^{n-k} \binom{n-t}{n-k} k^r (H_{k-t} - H_{n-t}) =
\sum_{k=0}^{\min(r,n)} k! {r \brace k} \binom{t}{n-k} (H_t - H_{t-n+k}).$$

## Sources

- Kunle Adegoke and Robert Frontczak, *Three Classes of Combinatorial Sums Involving Central Binomial Coefficients and Harmonic Numbers*, INTEGERS 26 (2026), Article A109, Theorem 6.

Stated but not proved: `MetaMathlibExt.sum_choose_sub_harmonic_diff_stirling_dual` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/CentralBinomHarmonicSumsWanted.lean, line 350](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/CentralBinomHarmonicSumsWanted.lean#L350). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/central-binomial-harmonic-sums/central-binomial-sums-with-harmonic-numbers/index.html#sum-choose-sub-harmonic-diff-stirling-du).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Central binomial sums with harmonic numbers](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/central-binomial-harmonic-sums/central-binomial-sums-with-harmonic-numbers/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Combinatorics/binomial-coefficients/central-binomial-harmonic-sums/central-binomial-sums-with-harmonic-numbers)
