---
declaration: section
origin: cited
lean: MetaMathlibExt.watsonCosSum, MetaMathlibExt.watsonAlternatingCosecantSum, MetaMathlibExt.watsonCosSum_two_one, MetaMathlibExt.watsonAlternatingCosecantSum_two, MetaMathlibExt.watsonOddCotangentDeriv, MetaMathlibExt.watson_cosh_integral_digamma, MetaMathlibExt.watsonExpansionTerm, MetaMathlibExt.watson_cos_sum_almost_asymptotic
statement: formalized
---

# Watson's cosecant and cosine sums

15 results, 7 proved and 8 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/exponential-sums/watson-s-cosecant-and-cosine-sums/index.html).

## Generalized Watson trigonometric sum

For natural numbers $n$ and $\nu$, $C_n(\nu)$ is the real
number

$$
C_n(\nu) = \sum_{l=1}^{n-1} \frac{\cos(2\pi\nu l/n)}{\sin(\pi l/n)}.
$$

For $n \le 1$ the sum is empty and $C_n(\nu) = 0$.

## Sources

- Iaroslav V. Blagouchine, *On a Generalization of Watson’s Trigonometric Sum (On Dowker’s Sum of Order One Half)*, INTEGERS 25 (2025), Article A30, definition of `C_n(ν)`.

Formalized by `MetaMathlibExt.watsonCosSum`, a definition declared in [WantedExt/NumberTheory/DowkerHalfSumWanted.lean, line 31](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/DowkerHalfSumWanted.lean#L31). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/exponential-sums/watson-s-cosecant-and-cosine-sums/index.html#watson-cos-sum).

## Watson's alternating cosecant sum

For a natural number $n$, the alternating cosecant sum is
the real number

$$
C_n = \sum_{l=1}^{n-1} \frac{(-1)^{l+1}}{\sin(\pi l / n)}.
$$

For $n \le 1$ the sum is empty and $C_n = 0$.

## Sources

- Iaroslav V. Blagouchine, *On a Generalization of Watson’s Trigonometric Sum (On Dowker’s Sum of Order One Half)*, INTEGERS 25 (2025), Article A30, definition of `C_n`.

Formalized by `MetaMathlibExt.watsonAlternatingCosecantSum`, a definition declared in [WantedExt/NumberTheory/DowkerHalfSumWanted.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/DowkerHalfSumWanted.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/exponential-sums/watson-s-cosecant-and-cosine-sums/index.html#watson-alternating-cosecant-sum).

## Watson's cosine sum at $n = 2$, $\nu = 1$

The cosine sum
$C_n(\nu) = \sum_{l=1}^{n-1} \cos(2 \pi \nu l / n) / \sin(\pi l / n)$ satisfies $C_2(1) = -1$.

## Sources

- Iaroslav V. Blagouchine, *On a Generalization of Watson’s Trigonometric Sum (On Dowker’s Sum of Order One Half)*, INTEGERS 25 (2025), Article A30, definition of `C_n(ν)`.

Formalized by `MetaMathlibExt.watsonCosSum_two_one`, a theorem declared in [WantedExt/NumberTheory/DowkerHalfSumWanted.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/DowkerHalfSumWanted.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/exponential-sums/watson-s-cosecant-and-cosine-sums/index.html#watson-cos-sum-two-one).

## Watson's alternating cosecant sum at $n = 2$

The alternating cosecant sum
$C_2 = \sum_{l=1}^{1} (-1)^{l+1} / \sin(\pi l / 2)$ equals $1$.

## Sources

- Iaroslav V. Blagouchine, *On a Generalization of Watson’s Trigonometric Sum (On Dowker’s Sum of Order One Half)*, INTEGERS 25 (2025), Article A30, definition of `C_n`.

Formalized by `MetaMathlibExt.watsonAlternatingCosecantSum_two`, a theorem declared in [WantedExt/NumberTheory/DowkerHalfSumWanted.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/DowkerHalfSumWanted.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/exponential-sums/watson-s-cosecant-and-cosine-sums/index.html#watson-alternating-cosecant-sum-two).

## Odd cotangent derivatives

For natural numbers $r$, $n$ and $\nu$, $\mathcal{H}_{2r-1}(\nu/n)$
is the real number $\cot^{(2r-1)}(\pi\nu/n)$, the $(2r-1)$st derivative of the cotangent function
evaluated at $\pi\nu/n$. Here $2r - 1$ is computed in the natural numbers, so for $r = 0$ this is
$\cot(\pi\nu/n)$ itself.

The derivative is taken of the cotangent as a function on all of $\mathbb{R}$; the value is the
classical one whenever $\pi\nu/n$ is not a multiple of $\pi$.

## Sources

- Iaroslav V. Blagouchine, *On a Generalization of Watson’s Trigonometric Sum (On Dowker’s Sum of Order One Half)*, INTEGERS 25 (2025), Article A30, definition of `ℋ_{2r-1}`.

Formalized by `MetaMathlibExt.watsonOddCotangentDeriv`, a definition declared in [WantedExt/NumberTheory/DowkerHalfSumWanted.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/DowkerHalfSumWanted.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/exponential-sums/watson-s-cosecant-and-cosine-sums/index.html#watson-odd-cotangent-deriv).

## Digamma evaluation of a hyperbolic Laplace integral

Let $b > 0$ be a real number and let
$\alpha, \beta$ be complex numbers with $\operatorname{Re}(\alpha + b - \beta) > 0$ and
$\operatorname{Re}(\alpha + b + \beta) > 0$. Then the function
$x \mapsto e^{-\alpha x} \cosh(\beta x) / \cosh(bx)$ is integrable on $(0, \infty)$, and, writing
$\psi$ for the digamma function,

$$
\int_0^\infty \frac{e^{-\alpha x} \cosh(\beta x)}{\cosh(bx)} \, dx =
\frac{1}{4b} \Bigl[ \psi\bigl(\tfrac34 + \tfrac{\alpha+\beta}{4b}\bigr) -
\psi\bigl(\tfrac14 + \tfrac{\alpha-\beta}{4b}\bigr) +
\psi\bigl(\tfrac34 + \tfrac{\alpha-\beta}{4b}\bigr) -
\psi\bigl(\tfrac14 + \tfrac{\alpha+\beta}{4b}\bigr) \Bigr].
$$

The source prints only the condition $\operatorname{Re}(\alpha + b - \beta) > 0$; the condition
$\operatorname{Re}(\alpha + b + \beta) > 0$ is also needed, since the integrand is even in $\beta$.

## Sources

- Iaroslav V. Blagouchine, *On a Generalization of Watson’s Trigonometric Sum (On Dowker’s Sum of Order One Half)*, INTEGERS 25 (2025), Article A30, Lemma 1.

Stated but not proved: `MetaMathlibExt.watson_cosh_integral_digamma` is written with `theorem_wanted` in [WantedExt/NumberTheory/DowkerHalfSumWanted.lean, line 81](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/DowkerHalfSumWanted.lean#L81). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/exponential-sums/watson-s-cosecant-and-cosine-sums/index.html#watson-cosh-integral-digamma).

## Watson expansion terms

For natural numbers $r$, $n$ and $\nu$, let $B_{2r}$ be the $2r$th
Bernoulli number and let $\mathcal{H}_{2r-1}(\nu/n) = \cot^{(2r-1)}(\pi\nu/n)$ be the
$(2r-1)$st derivative of the cotangent evaluated at $\pi\nu/n$. The $r$th Watson expansion term is
the real number

$$
\Bigl(1 - \frac{1}{2^{2r-1}}\Bigr)
\frac{\pi^{2r-1} B_{2r} \, \mathcal{H}_{2r-1}(\nu/n)}{(2r)! \, n^{2r-1}}.
$$

Here $2r - 1$ is computed in the natural numbers, so for $r = 0$ the factor $1 - 1/2^{2r-1}$ is $0$
and the term vanishes.

## Sources

- Iaroslav V. Blagouchine, *On a Generalization of Watson’s Trigonometric Sum (On Dowker’s Sum of Order One Half)*, INTEGERS 25 (2025), Article A30, Theorem 3 (printed as Theorem 4).

Formalized by `MetaMathlibExt.watsonExpansionTerm`, a definition declared in [WantedExt/NumberTheory/DowkerHalfSumWanted.lean, line 106](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/DowkerHalfSumWanted.lean#L106). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/exponential-sums/watson-s-cosecant-and-cosine-sums/index.html#watson-expansion-term).

## Almost-asymptotic expansion of Watson's cosine sum

Let $n \ge 2$, $N \ge 2$ and $\nu$ be
natural numbers with $1 \le \nu \le n - 1$, and let

$$
C_n(\nu) = \sum_{l=1}^{n-1} \frac{\cos(2 \pi \nu l / n)}{\sin(\pi l / n)}.
$$

For $r \ge 1$ write

$$
T_r(n, \nu) = \frac{(1 - 2^{1-2r}) \, \pi^{2r-1} B_{2r} \, \cot^{(2r-1)}(\pi \nu / n)}
{(2r)! \, n^{2r-1}},
$$

where $B_{2r}$ is the $2r$-th Bernoulli number and $\cot^{(2r-1)}$ is the $(2r-1)$-st derivative
of the cotangent. Then there is a real number $\lambda$ with $0 < \lambda < 1$ such that

$$
C_n(\nu) = -\frac{2n}{\pi} \log\left(2 \sin\frac{\pi \nu}{n}\right) +
2 \sum_{r=1}^{N-1} T_r(n, \nu) + 2 \lambda \, T_N(n, \nu).
$$

## Sources

- Iaroslav V. Blagouchine, *On a Generalization of Watson’s Trigonometric Sum (On Dowker’s Sum of Order One Half)*, INTEGERS 25 (2025), Article A30, Theorem 3 (printed as Theorem 4).

Stated but not proved: `MetaMathlibExt.watson_cos_sum_almost_asymptotic` is written with `theorem_wanted` in [WantedExt/NumberTheory/DowkerHalfSumWanted.lean, line 120](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/DowkerHalfSumWanted.lean#L120). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/exponential-sums/watson-s-cosecant-and-cosine-sums/index.html#watson-cos-sum-almost-asymptotic).

## The odd cotangent derivatives in Watson's expansion are negative

Let $r$, $n$ and $\nu$ be
natural numbers with $r \ge 1$ and $1 \le \nu \le n - 1$. Then
$\mathcal{H}_{2r-1}(\nu/n) = \cot^{(2r-1)}(\pi\nu/n)$, the $(2r-1)$st derivative of the cotangent
evaluated at $\pi\nu/n$, is strictly negative.

## Sources

- Iaroslav V. Blagouchine, *On a Generalization of Watson’s Trigonometric Sum (On Dowker’s Sum of Order One Half)*, INTEGERS 25 (2025), Article A30, Theorem 3 (printed as Theorem 4).

Stated but not proved: `MetaMathlibExt.watson_odd_cotangent_deriv_neg` is written with `theorem_wanted` in [WantedExt/NumberTheory/DowkerHalfSumWanted.lean, line 136](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/DowkerHalfSumWanted.lean#L136). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/exponential-sums/watson-s-cosecant-and-cosine-sums/index.html#watson-odd-cotangent-deriv-neg).

## Main part of the asymptotic expansion of Watson's alternating cosecant sum

For natural numbers
$N$ and $n$, the main part is the real number

$$
M_N(n) = \frac{2 n \log 2}{\pi} + 2 \sum_{r=1}^{N-1}
\frac{(-1)^{r+1} (2^{2r-1} - 1)(2^{2r} - 1) \pi^{2r-1} B_{2r}^2}{r \, (2r)! \, n^{2r-1}},
$$

where $B_{2r}$ is the $2r$-th Bernoulli number. For $N \le 1$ the sum is empty.

## Sources

- Iaroslav V. Blagouchine, *On a Generalization of Watson’s Trigonometric Sum (On Dowker’s Sum of Order One Half)*, INTEGERS 25 (2025), Article A30, Corollary 2.

Formalized by `MetaMathlibExt.watsonAlternatingMain`, a definition declared in [WantedExt/NumberTheory/DowkerHalfSumWanted.lean, line 147](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/DowkerHalfSumWanted.lean#L147). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/exponential-sums/watson-s-cosecant-and-cosine-sums/index.html#watson-alternating-main).

## Complete asymptotic expansion of Watson's alternating cosecant sum

For natural numbers $N$
and $n$ let $C_n = \sum_{l=1}^{n-1} (-1)^{l+1} / \sin(\pi l / n)$ and

$$
M_N(n) = \frac{2 n \log 2}{\pi} + 2 \sum_{r=1}^{N-1}
\frac{(-1)^{r+1} (2^{2r-1} - 1)(2^{2r} - 1) \pi^{2r-1} B_{2r}^2}{r \, (2r)! \, n^{2r-1}},
$$

where $B_{2r}$ is the $2r$-th Bernoulli number. For every $N \ge 2$ there is a real constant
$K \ge 0$ such that for every even $n \ge 2$,

$$
|C_n - M_N(n)| \le \frac{K}{n^{2N-1}}.
$$

In other words, $C_n = M_N(n) + O(n^{1-2N})$ as $n \to \infty$ through even values.

## Sources

- Iaroslav V. Blagouchine, *On a Generalization of Watson’s Trigonometric Sum (On Dowker’s Sum of Order One Half)*, INTEGERS 25 (2025), Article A30, Corollary 2.

Stated but not proved: `MetaMathlibExt.watson_alternating_complete_asymptotic` is written with `theorem_wanted` in [WantedExt/NumberTheory/DowkerHalfSumWanted.lean, line 162](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/DowkerHalfSumWanted.lean#L162). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/exponential-sums/watson-s-cosecant-and-cosine-sums/index.html#watson-alternating-complete-asymptotic).

## Watson's alternating cosecant sum vanishes for odd $n$

For every odd natural number $n$,

$$
\sum_{l=1}^{n-1} \frac{(-1)^{l+1}}{\sin(\pi l / n)} = 0.
$$

## Sources

- Iaroslav V. Blagouchine, *On a Generalization of Watson’s Trigonometric Sum (On Dowker’s Sum of Order One Half)*, INTEGERS 25 (2025), Article A30, Corollary 2 and Theorem 6.

Stated but not proved: `MetaMathlibExt.watson_alternating_odd_zero` is written with `theorem_wanted` in [WantedExt/NumberTheory/DowkerHalfSumWanted.lean, line 173](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/DowkerHalfSumWanted.lean#L173). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/exponential-sums/watson-s-cosecant-and-cosine-sums/index.html#watson-alternating-odd-zero).

## Two-sided bounds for Watson's alternating cosecant sum

For every even natural number
$n \ge 2$, the alternating cosecant sum $C_n = \sum_{l=1}^{n-1} (-1)^{l+1} / \sin(\pi l / n)$
satisfies the strict inequalities

$$
\frac{2 n \log 2}{\pi} + \frac{\pi}{12 n} - \frac{7 \pi^3}{1440 n^3} < C_n <
\frac{2 n \log 2}{\pi} + \frac{\pi}{12 n}.
$$

The lower bound consists of the first three terms of the asymptotic expansion of $C_n$ and the
upper bound of the first two.

## Sources

- Iaroslav V. Blagouchine, *On a Generalization of Watson’s Trigonometric Sum (On Dowker’s Sum of Order One Half)*, INTEGERS 25 (2025), Article A30, Theorem 6 and Corollary 3.

Stated but not proved: `MetaMathlibExt.watson_alternating_sharp_bounds` is written with `theorem_wanted` in [WantedExt/NumberTheory/DowkerHalfSumWanted.lean, line 183](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/DowkerHalfSumWanted.lean#L183). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/exponential-sums/watson-s-cosecant-and-cosine-sums/index.html#watson-alternating-sharp-bounds).

## Decimal bounds for Watson's alternating cosecant sum

For every even natural number
$n \ge 4$, the alternating cosecant sum $C_n = \sum_{l=1}^{n-1} (-1)^{l+1} / \sin(\pi l / n)$
satisfies the strict inequalities

$$
\frac{2 n \log 2}{\pi} + \frac{0.252}{n} < C_n < \frac{2 n \log 2}{\pi} + \frac{0.262}{n}.
$$

## Sources

- Iaroslav V. Blagouchine, *On a Generalization of Watson’s Trigonometric Sum (On Dowker’s Sum of Order One Half)*, INTEGERS 25 (2025), Article A30, Corollary 3.

Stated but not proved: `MetaMathlibExt.watson_alternating_simple_bounds` is written with `theorem_wanted` in [WantedExt/NumberTheory/DowkerHalfSumWanted.lean, line 198](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/DowkerHalfSumWanted.lean#L198). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/exponential-sums/watson-s-cosecant-and-cosine-sums/index.html#watson-alternating-simple-bounds).

## Vanishing limits of Watson's cosine sum at one sixth and five sixths

For natural numbers
$n$ and $\nu$ let $C_n(\nu) = \sum_{l=1}^{n-1} \cos(2 \pi \nu l / n) / \sin(\pi l / n)$. As
$m \to \infty$ through the natural numbers, $C_{6m}(m) \to 0$ and $C_{6m}(5m) \to 0$.

## Sources

- Iaroslav V. Blagouchine, *On a Generalization of Watson’s Trigonometric Sum (On Dowker’s Sum of Order One Half)*, INTEGERS 25 (2025), Article A30, Corollary 4.

Stated but not proved: `MetaMathlibExt.watson_cos_sum_sixth_limits` is written with `theorem_wanted` in [WantedExt/NumberTheory/DowkerHalfSumWanted.lean, line 211](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/DowkerHalfSumWanted.lean#L211). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/exponential-sums/watson-s-cosecant-and-cosine-sums/index.html#watson-cos-sum-sixth-limits).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Watson's cosecant and cosine sums](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/exponential-sums/watson-s-cosecant-and-cosine-sums/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/exponential-sums/watson-s-cosecant-and-cosine-sums)
