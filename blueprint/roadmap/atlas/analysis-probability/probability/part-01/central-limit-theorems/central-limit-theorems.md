---
declaration: section
origin: cited
lean: MathlibExt.Probability.ScottishBook17Wanted.urnConversePoisson, MathlibExt.Probability.ScottishBook126Wanted.khintchine_infinite_variance_limit, MetaMathlibExt.stirling_edgeworth_expansion, MathlibExt.MeasureTheory.CubeAbsSumIntegralAsymptoticWanted.tendsto_integral_abs_sum_cube_div_sqrt
statement: formalized
---

# Central limit theorems and Poisson approximation: its own results

4 results, 4 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/central-limit-theorems/index.html).

Convergence in law of normalized sums and their error terms: central limit theorems (Lindeberg–Feller, lacunary and infinite-variance variants), Berry–Esseen bounds and constants, global and local de Moivre–Laplace theorems, Edgeworth expansions, Donsker's invariance principle, and Poisson limit theorems for binomial and urn models.

## Converse of Poisson's theorem for urns

Let $(\Omega, \mu)$ be a probability space, let
$(p_n)_{n \ge 0}$ be real numbers in $[0, 1]$, and let $(X_n)_{n \ge 0}$ be pairwise independent
measurable real random variables on $\Omega$ such that each $X_n$ almost surely takes only the
values $0$ and $1$, and $\mu(X_n = 1) = p_n$. Then for every real number $L$ and almost every
$\omega \in \Omega$: if $\frac{1}{n} \sum_{i=0}^{n-1} X_i(\omega) \to L$ as $n \to \infty$, then
$\frac{1}{n} \sum_{i=0}^{n-1} p_i \to L$ as $n \to \infty$.

Here $X_n$ records one draw from the $n$-th of a sequence of urns of unknown composition, a white
ball as $1$ and a black ball as $0$, and $p_n$ is the probability of drawing a white ball from the
$n$-th urn. Only pairwise independence is assumed: for uncorrelated variables with uniformly
bounded variances the strong law of large numbers still holds.

## Sources

- S. Ulam, Problem 17 of the Scottish Book. The proof is Kolmogorov's strong law of large numbers for independent bounded variables (1933).

Stated but not proved: `MathlibExt.Probability.ScottishBook17Wanted.urnConversePoisson` is written with `theorem_wanted` in [WantedExt/Probability/ScottishBook17Wanted.lean, line 36](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Probability/ScottishBook17Wanted.lean#L36). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/central-limit-theorems/index.html#urn-converse-poisson).

## Kac's Scottish Book Problem 126

Let $f : \mathbb{R} \to \mathbb{R}$ be a measurable function
that is integrable on $[0, 1]$ and satisfies $\int_0^1 f(x)\,dx = 0$ and
$\int_0^1 f(x)^2\,dx = \infty$. Then the complex numbers
$\left(\int_0^1 \exp\left(i f(x) / \sqrt{n}\right) dx\right)^n$ tend to $0$ as $n \to \infty$
through the natural numbers.

## Sources

- M. Kac, Problem 126 of the Scottish Book; solved affirmatively by A. Khintchine, fourth communique on dependent functions, Studia Mathematicae 6 or 7, as cited in the typescript addendum Ad 126. The typescript parenthetical states the finite-variance case as `e ^ (-1 / 2)` where `e ^ (-A / 2)` for `A = ∫_0^1 f^2` would be expected; that parenthetical is not used here.

Stated but not proved: `MathlibExt.Probability.ScottishBook126Wanted.khintchine_infinite_variance_limit` is written with `theorem_wanted` in [WantedExt/Probability/ScottishBook126Wanted.lean, line 33](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Probability/ScottishBook126Wanted.lean#L33). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/central-limit-theorems/index.html#khintchine-infinite-variance-limit).

## Local Edgeworth expansion for the Ewens distribution

Let $r \ge 0$ be an integer and let
$L \subseteq (0, \infty)$ be compact. For $\theta > 0$ and integers $n \ge 2$ and $1 \le k \le n$,
let $s(n, k)$ be the unsigned Stirling number of the first kind (the number of permutations of
$n$ elements with exactly $k$ cycles), let
$p_n(k; \theta) = \theta^k s(n, k) / (\theta (\theta + 1) \cdots (\theta + n - 1))$ be the
probability that an Ewens permutation with parameter $\theta$ has exactly $k$ cycles, and let
$x_n(k; \theta) = (k - \theta \log n) / \sqrt{\theta \log n}$. Then there are functions
$H_0, H_1, \dots : \mathbb{R} \times \mathbb{R} \to \mathbb{R}$ such that for every
$\varepsilon > 0$ there is an $N \ge 2$ with the following property: for all $n \ge N$, all
$\theta \in L$ and all integers $1 \le k \le n$, writing $x = x_n(k; \theta)$,

$$(\log n)^{(r+1)/2} \left| p_n(k; \theta) - \frac{e^{-x^2/2}}{\sqrt{2 \pi \theta \log n}}
\sum_{j=0}^{r} \frac{H_j(x, \theta)}{(\theta \log n)^{j/2}} \right| < \varepsilon.$$

The functions $H_j$ are bound existentially and may depend on both $r$ and $L$; nothing requires
them to be polynomials.

## Sources

- Zakhar Kabluchko, Alexander Marynych, and Henning Sulzbach, "Mode and Edgeworth Expansion for the Ewens Distribution and the Stirling Numbers," Journal of Integer Sequences 19 (2016), Article 16.8.8, Theorem, lines 207–226 (Ewens probability mass function at lines 143–146), https://cs.uwaterloo.ca/journals/JIS/VOL19/Kabluchko/kabl2.tex

Stated but not proved: `MetaMathlibExt.stirling_edgeworth_expansion` is written with `theorem_wanted` in [WantedExt/Probability/StirlingEdgeworthExpansionWanted.lean, line 39](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Probability/StirlingEdgeworthExpansionWanted.lean#L39). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/central-limit-theorems/index.html#stirling-edgeworth-expansion).

## Mean absolute sum over the unit cube

For $n \in \mathbb{N}$ let

$$
I_n = \int_{[-1/2,\, 1/2]^n} \left| \sum_{i=1}^n x_i \right| dx.
$$

Then $I_n / \sqrt{n} \to 1 / \sqrt{6\pi}$ as $n \to \infty$.

## Sources

- MA-ProofBench (L. Pu et al., arXiv:2606.13782), Level II (Measure and integration; Classical measure theory), problem `ma_proofbench_l2_95`.

Stated but not proved: `MathlibExt.MeasureTheory.CubeAbsSumIntegralAsymptoticWanted.tendsto_integral_abs_sum_cube_div_sqrt` is written with `theorem_wanted` in [WantedExt/MeasureTheory/CubeAbsSumIntegralAsymptoticWanted.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/MeasureTheory/CubeAbsSumIntegralAsymptoticWanted.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/central-limit-theorems/index.html#tendsto-integral-abs-sum-cube-div-sqrt).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Central limit theorems and Poisson approximation](https://deicyde.github.io/atlas-lean/roadmap/Probability/central-limit-theorems/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Probability/central-limit-theorems)
