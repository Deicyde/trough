---
declaration: section
origin: cited
lean: MetaMathlibExt.strideAlternatingSum, MetaMathlibExt.strideSignedSum, MetaMathlibExt.strideAlternatingSum_of_le, MetaMathlibExt.strideSignedSum_of_le, MetaMathlibExt.strideAlternatingSum_add, MetaMathlibExt.strideSignedSum_add, MetaMathlibExt.tendsto_strideAlternatingSum_riemannZeta, MetaMathlibExt.tendsto_strideSignedSum_digamma
statement: formalized
---

# Stride series for zeta and eta values

15 results, 6 proved and 9 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/riemann-zeta/stride-series-for-zeta-and-eta-values/index.html).

## Alternating stride sum

For natural numbers $q$, $t$ and $n$, let
$K = \lfloor (n + q - 1)/q \rfloor$ if $q \ge 1$ and $K = 0$ if $q = 0$. The alternating stride
sum is the real number

$$
S_{q,t}(n) = \sum_{i=0}^{K-1} \frac{(-1)^i}{(n - qi)^t}.
$$

For $q \ge 1$ this is the alternating sum of $m^{-t}$ over $m = n, n - q, n - 2q, \dots$ with
$m \ge 1$; with $j = i + 1$ it reads $\sum_{j=1}^{K} (-1)^{j+1}/(n + q - qj)^t$.

## Sources

- Anthony Sofo and Junesang Choi, *New Series Representations for the Riemann Zeta Function and Its Associated Functions*, INTEGERS 24 (2024), Article A45, Theorem 1, equation (9).

Formalized by `MetaMathlibExt.strideAlternatingSum`, a definition declared in [WantedExt/NumberTheory/ZetaStrideSeriesWanted.lean, line 28](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ZetaStrideSeriesWanted.lean#L28). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/riemann-zeta/stride-series-for-zeta-and-eta-values/index.html#stride-alternating-sum).

## Signed stride sum

For natural numbers $q$, $t$ and $n$, let
$K = \lfloor (n + q - 1)/q \rfloor$ if $q \ge 1$ and $K = 0$ if $q = 0$. The signed stride sum is
the real number

$$
T_{q,t}(n) = \sum_{i=0}^{K-1} \frac{(-1)^{(q+1)i}}{(n - qi)^t}.
$$

With $j = i + 1$ it reads $\sum_{j=1}^{K} (-1)^{(q+1)(j+1)}/(n + q - qj)^t$. For odd $q$ every
sign is $+$, and for even $q$ the signs alternate.

## Sources

- Anthony Sofo and Junesang Choi, *New Series Representations for the Riemann Zeta Function and Its Associated Functions*, INTEGERS 24 (2024), Article A45, Theorem 2, equation (25).

Formalized by `MetaMathlibExt.strideSignedSum`, a definition declared in [WantedExt/NumberTheory/ZetaStrideSeriesWanted.lean, line 37](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ZetaStrideSeriesWanted.lean#L37). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/riemann-zeta/stride-series-for-zeta-and-eta-values/index.html#stride-signed-sum).

## Alternating stride sum with a single term

For natural numbers $q$, $t$ and $n$ with
$1 \le n \le q$, the alternating stride sum satisfies $S_{q,t}(n) = 1/n^t$.

## Sources

- Anthony Sofo and Junesang Choi, *New Series Representations for the Riemann Zeta Function and Its Associated Functions*, INTEGERS 24 (2024), Article A45, equation (9).

Formalized by `MetaMathlibExt.strideAlternatingSum_of_le`, a theorem declared in [WantedExt/NumberTheory/ZetaStrideSeriesWanted.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ZetaStrideSeriesWanted.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/riemann-zeta/stride-series-for-zeta-and-eta-values/index.html#stride-alternating-sum-of-le).

## Signed stride sum with a single term

For natural numbers $q$, $t$ and $n$ with
$1 \le n \le q$, the signed stride sum satisfies $T_{q,t}(n) = 1/n^t$.

## Sources

- Anthony Sofo and Junesang Choi, *New Series Representations for the Riemann Zeta Function and Its Associated Functions*, INTEGERS 24 (2024), Article A45, equation (25).

Formalized by `MetaMathlibExt.strideSignedSum_of_le`, a theorem declared in [WantedExt/NumberTheory/ZetaStrideSeriesWanted.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ZetaStrideSeriesWanted.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/riemann-zeta/stride-series-for-zeta-and-eta-values/index.html#stride-signed-sum-of-le).

## Recurrence for the alternating stride sum

Let $q \ge 1$, $n \ge 1$ and $t \ge 0$ be
integers and let $S_{q,t}$ denote the alternating stride sum. Then
$S_{q,t}(n + q) = 1/(n + q)^t - S_{q,t}(n)$.

## Sources

- Anthony Sofo and Junesang Choi, *New Series Representations for the Riemann Zeta Function and Its Associated Functions*, INTEGERS 24 (2024), Article A45, equation (9).

Formalized by `MetaMathlibExt.strideAlternatingSum_add`, a theorem declared in [WantedExt/NumberTheory/ZetaStrideSeriesWanted.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ZetaStrideSeriesWanted.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/riemann-zeta/stride-series-for-zeta-and-eta-values/index.html#stride-alternating-sum-add).

## Recurrence for the signed stride sum

Let $q \ge 1$, $n \ge 1$ and $t \ge 0$ be integers
and let $T_{q,t}$ denote the signed stride sum. Then
$T_{q,t}(n + q) = 1/(n + q)^t + (-1)^{q+1} T_{q,t}(n)$.

## Sources

- Anthony Sofo and Junesang Choi, *New Series Representations for the Riemann Zeta Function and Its Associated Functions*, INTEGERS 24 (2024), Article A45, equation (25).

Formalized by `MetaMathlibExt.strideSignedSum_add`, a theorem declared in [WantedExt/NumberTheory/ZetaStrideSeriesWanted.lean, line 82](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ZetaStrideSeriesWanted.lean#L82). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/riemann-zeta/stride-series-for-zeta-and-eta-values/index.html#stride-signed-sum-add).

## Alternating stride sum series for $\zeta(t + 1)$

Let $q \ge 1$ and $t \ge 1$ be integers
and let $S_{q,t}$ denote the alternating stride sum. Then the partial sums

$$
\sum_{n=1}^{N} \frac{2n + q}{n(n + q)} \, S_{q,t}(n)
$$

converge to $\zeta(t + 1)$ as $N \to \infty$, where $\zeta$ is the Riemann zeta function.

The series converges only conditionally, since $S_{q,t}(n)$ does not tend to $0$, which is why
it is stated through its partial sums. The second expression in equation (9) and the general
identity (8) use a quantity $A^{(t)}$ that the record does not define and are not stated here.

## Sources

- Anthony Sofo and Junesang Choi, *New Series Representations for the Riemann Zeta Function and Its Associated Functions*, INTEGERS 24 (2024), Article A45, Theorem 1, equation (9).

Stated but not proved: `MetaMathlibExt.tendsto_strideAlternatingSum_riemannZeta` is written with `theorem_wanted` in [WantedExt/NumberTheory/ZetaStrideSeriesWanted.lean, line 102](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ZetaStrideSeriesWanted.lean#L102). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/riemann-zeta/stride-series-for-zeta-and-eta-values/index.html#tendsto-stride-alternating-sum-riemann-z).

## Digamma series for the signed stride sum

Let $q \ge 1$ and $t \ge 1$ be integers, let
$a$ be a real number with $-1 \le a < 1$, let $T_{q,t}$ denote the signed stride sum and $\psi$
the digamma function. As $N \to \infty$, the partial sums

$$
\sum_{n=1}^{N} (-1)^{n+1} \frac{2n + q}{(n + a + 1)(n - a - 1 + q)} \, T_{q,t}(n)
$$

converge to

$$
\frac{1}{2q} \sum_{n=1}^{\infty} \frac{(-1)^{n+1}}{n^t}
\left[\psi\left(\frac{n+a+1+q}{2q}\right) - \psi\left(\frac{n+a+1}{2q}\right)\right] +
\frac{1}{2q} \sum_{n=1}^{\infty} \frac{(-1)^{n+1}}{n^t}
\left[\psi\left(\frac{n-a-1+2q}{2q}\right) - \psi\left(\frac{n-a-1+q}{2q}\right)\right].
$$

The first series converges only conditionally, while the two digamma series converge
absolutely.

## Sources

- Anthony Sofo and Junesang Choi, *New Series Representations for the Riemann Zeta Function and Its Associated Functions*, INTEGERS 24 (2024), Article A45, Theorem 2, equation (24).

Stated but not proved: `MetaMathlibExt.tendsto_strideSignedSum_digamma` is written with `theorem_wanted` in [WantedExt/NumberTheory/ZetaStrideSeriesWanted.lean, line 119](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ZetaStrideSeriesWanted.lean#L119). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/riemann-zeta/stride-series-for-zeta-and-eta-values/index.html#tendsto-stride-signed-sum-digamma).

## Stride series for the Dirichlet eta function

Let $q, t \ge 1$ be integers and let
$T_{q,t}(n)$ denote the signed stride sum. Then the partial sums

$$\sum_{n=1}^{N} (-1)^{n+1} \frac{2n+q}{n(n+q)} T_{q,t}(n)$$

converge, as $N \to \infty$, to $\eta(t+1)$, where $\eta(s) = \sum_{n \ge 1} (-1)^{n+1} n^{-s}$ is
the Dirichlet eta function.

## Sources

- Anthony Sofo and Junesang Choi, *New Series Representations for the Riemann Zeta Function and Its Associated Functions*, INTEGERS 24 (2024), Article A45, Theorem 2, equation (25).

Stated but not proved: `MetaMathlibExt.tendsto_strideSignedSum_dirichletEta` is written with `theorem_wanted` in [WantedExt/NumberTheory/ZetaStrideSeriesWanted.lean, line 139](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ZetaStrideSeriesWanted.lean#L139). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/riemann-zeta/stride-series-for-zeta-and-eta-values/index.html#tendsto-stride-signed-sum-dirichlet-eta).

## Digamma identity for stride sums over odd indices

Let $q, t \ge 1$ be integers, let
$a$ be a real number with $-1 \le a < 1$, let $S_{q,t}(n)$ denote the alternating stride sum and
$T_{q,t}(n)$ the signed stride sum, and let $\psi$ be the digamma function. Then the partial sums

$$\sum_{n=1}^{N} \frac{2n+q}{2(n+a+1)(n-a-1+q)} \bigl(S_{q,t}(n) + (-1)^{n+1} T_{q,t}(n)\bigr)$$

converge, as $N \to \infty$, to

$$\frac{1}{2q} \sum_{n \ge 1} \frac{1}{(2n-1)^t}
\Bigl[\psi\Bigl(\frac{2n+a+q}{2q}\Bigr) - \psi\Bigl(\frac{2n+a}{2q}\Bigr)\Bigr] +
\frac{1}{2q} \sum_{n \ge 1} \frac{1}{(2n-1)^t}
\Bigl[\psi\Bigl(\frac{2n-a-2+2q}{2q}\Bigr) - \psi\Bigl(\frac{2n-a-2+q}{2q}\Bigr)\Bigr].$$

Deviation: the paper prints the factor $2$ where this statement has $1/2$; as printed the
series sums to four times this limit (for $q = t = 1$ and $a = -1$: $4\lambda(2) \approx 4.935$
against $\lambda(2) = \pi^2/8 \approx 1.234$, where $\lambda(s) = \sum_{n \ge 0} (2n+1)^{-s}$
is the Dirichlet lambda function). With $1/2$ the identity checks numerically for several
$(a, q, t)$, and at $a = -1$ it is the stride series for $\lambda(t+1)$, half the sum of the
paper's series (9) for $\zeta(t+1)$ and (25) for $\eta(t+1)$.

## Sources

- Anthony Sofo and Junesang Choi, *New Series Representations for the Riemann Zeta Function and Its Associated Functions*, INTEGERS 24 (2024), Article A45, Theorem 3, equation (27).

Stated but not proved: `MetaMathlibExt.tendsto_strideSums_digamma_odd` is written with `theorem_wanted` in [WantedExt/NumberTheory/ZetaStrideSeriesWanted.lean, line 161](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ZetaStrideSeriesWanted.lean#L161). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/riemann-zeta/stride-series-for-zeta-and-eta-values/index.html#tendsto-stride-sums-digamma-odd).

## Stride series for the Dirichlet lambda function

Let $q, t \ge 1$ be integers, and let
$S_{q,t}(n)$ denote the alternating stride sum and $T_{q,t}(n)$ the signed stride sum. Then the
partial sums

$$\sum_{n=1}^{N} \frac{2n+q}{2n(n+q)} \bigl(S_{q,t}(n) + (-1)^{n+1} T_{q,t}(n)\bigr)$$

converge, as $N \to \infty$, to $\lambda(t+1)$, where $\lambda(s) = \sum_{n \ge 0} (2n+1)^{-s}$ is
the Dirichlet lambda function. The series is half the sum of the paper's series (9) for
$\zeta(t+1)$ and (25) for $\eta(t+1)$.

Deviation: the paper prints the factor $2$ where this statement has $1/2$; as printed the
series sums to $4\lambda(t+1)$ (for $q = t = 1$: about $4.935$ against
$\lambda(2) = \pi^2/8 \approx 1.234$).

## Sources

- Anthony Sofo and Junesang Choi, *New Series Representations for the Riemann Zeta Function and Its Associated Functions*, INTEGERS 24 (2024), Article A45, Theorem 3, equation (28).

Stated but not proved: `MetaMathlibExt.tendsto_strideSums_dirichletLambda` is written with `theorem_wanted` in [WantedExt/NumberTheory/ZetaStrideSeriesWanted.lean, line 186](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ZetaStrideSeriesWanted.lean#L186). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/riemann-zeta/stride-series-for-zeta-and-eta-values/index.html#tendsto-stride-sums-dirichlet-lambda).

## Alternating stride sum series for $\zeta(p + t + 1)$

Let $q \ge 1$ and $t \ge 1$ be
integers, let $p \ge 0$ be an even integer and let $S_{q,t}$ denote the alternating stride sum.
Then the partial sums

$$
\sum_{n=1}^{N} \frac{n^{p+1} + (n + q)^{p+1}}{(n(n + q))^{p+1}} \, S_{q,t}(n)
$$

converge to $\zeta(p + t + 1)$ as $N \to \infty$, where $\zeta$ is the Riemann zeta function.

Only the first equality of equation (32) is stated; its second expression uses a quantity
$A^{(t)}$ that the record does not define.

## Sources

- Anthony Sofo and Junesang Choi, *New Series Representations for the Riemann Zeta Function and Its Associated Functions*, INTEGERS 24 (2024), Article A45, Theorem 4, equation (32).

Stated but not proved: `MetaMathlibExt.tendsto_strideAlternatingSum_riemannZeta_add` is written with `theorem_wanted` in [WantedExt/NumberTheory/ZetaStrideSeriesWanted.lean, line 200](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ZetaStrideSeriesWanted.lean#L200). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/riemann-zeta/stride-series-for-zeta-and-eta-values/index.html#tendsto-stride-alternating-sum-riemann-z-2).

## Higher-power stride series for the Dirichlet eta function

Let $q, t \ge 1$ be integers,
let $p \ge 0$ be an even integer, and let $T_{q,t}(n)$ denote the signed stride sum. Then the
partial sums

$$\sum_{n=1}^{N} (-1)^{n+1} \frac{n^{p+1} + (n+q)^{p+1}}{(n(n+q))^{p+1}} T_{q,t}(n)$$

converge, as $N \to \infty$, to $\eta(p+t+1)$, where $\eta(s) = \sum_{n \ge 1} (-1)^{n+1} n^{-s}$
is the Dirichlet eta function.

## Sources

- Anthony Sofo and Junesang Choi, *New Series Representations for the Riemann Zeta Function and Its Associated Functions*, INTEGERS 24 (2024), Article A45, Theorem 5, equation (40).

Stated but not proved: `MetaMathlibExt.tendsto_strideSignedSum_dirichletEta_add` is written with `theorem_wanted` in [WantedExt/NumberTheory/ZetaStrideSeriesWanted.lean, line 215](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ZetaStrideSeriesWanted.lean#L215). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/riemann-zeta/stride-series-for-zeta-and-eta-values/index.html#tendsto-stride-signed-sum-dirichlet-eta-2).

## Digamma series for the alternating stride sum

Let $q \ge 1$ and $t \ge 1$ be integers,
let $S_{q,t}$ denote the alternating stride sum and $\psi$ the digamma function. As
$N \to \infty$, the partial sums

$$
\sum_{n=1}^{N} \frac{2n + q}{(n + \frac12)(n - \frac12 + q)} \, S_{q,t}(n)
$$

converge to

$$
\frac{1}{2q} \sum_{n=1}^{\infty} \frac{1}{n^t}
\left[\psi\left(\frac{n+\frac12+q}{2q}\right) - \psi\left(\frac{n+\frac12}{2q}\right)\right] +
\frac{1}{2q} \sum_{n=1}^{\infty} \frac{1}{n^t}
\left[\psi\left(\frac{n-\frac12+2q}{2q}\right) - \psi\left(\frac{n-\frac12+q}{2q}\right)\right].
$$

## Sources

- Anthony Sofo and Junesang Choi, *New Series Representations for the Riemann Zeta Function and Its Associated Functions*, INTEGERS 24 (2024), Article A45, Corollary 1, equation (20).

Stated but not proved: `MetaMathlibExt.tendsto_strideAlternatingSum_digamma_half` is written with `theorem_wanted` in [WantedExt/NumberTheory/ZetaStrideSeriesWanted.lean, line 230](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ZetaStrideSeriesWanted.lean#L230). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/riemann-zeta/stride-series-for-zeta-and-eta-values/index.html#tendsto-stride-alternating-sum-digamma-h).

## Closed form of $\sum_{n \ge 1} 1/(n^t(2n-1))$

For every integer $t \ge 1$,

$$\sum_{n \ge 1} \frac{1}{n^t (2n-1)} = 2^t \log 2 - \sum_{j=1}^{t-1} 2^{t-1-j} \zeta(j+1),$$

where $\zeta$ is the Riemann zeta function.

## Sources

- Anthony Sofo and Junesang Choi, *New Series Representations for the Riemann Zeta Function and Its Associated Functions*, INTEGERS 24 (2024), Article A45, Corollary 1, equation (22).

Stated but not proved: `MetaMathlibExt.tsum_inv_pow_mul_two_mul_sub_one` is written with `theorem_wanted` in [WantedExt/NumberTheory/ZetaStrideSeriesWanted.lean, line 247](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ZetaStrideSeriesWanted.lean#L247). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/riemann-zeta/stride-series-for-zeta-and-eta-values/index.html#tsum-inv-pow-mul-two-mul-sub-one).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Stride series for zeta and eta values](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/riemann-zeta/stride-series-for-zeta-and-eta-values/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/zeta-l-functions/riemann-zeta/stride-series-for-zeta-and-eta-values)
