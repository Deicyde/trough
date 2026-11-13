---
declaration: section
origin: cited
lean: Real.tendsto_pow_mul_sub_bernoulli_sum_of_log_diff, tendsto_pow_mul_log_catalan_sub_bernoulli_sum, MetaMathlibExt.catalan_stirling_asymptotic_expansions, MetaMathlibExt.catalan_odd_terms_shift_unique
statement: formalized
proof: formalized
---

# Asymptotic expansion of the Catalan numbers

4 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/asymptotic-analysis/asymptotic-expansion-of-the-catalan-numbers/index.html).

## Bernoulli-polynomial expansion from a logarithmic difference equation

Let $\alpha$, $\beta$
and $c$ be real numbers and let $(u_n)$ be a real sequence with $u_n \to 0$ such that, for all
sufficiently large $n$,
$u_{n+1} - u_n = \log(1 + \alpha/(n + c)) - \log(1 + \beta/(n + c)) +
(\beta - \alpha) \log(1 + 1/(n + c))$.
Let $B_k(x)$ be the $k$-th Bernoulli polynomial and, for $j \ge 0$, put
$a_j = (-1)^j \left(B_{j+2}(\alpha) - B_{j+2}(\beta)\right) / ((j + 1)(j + 2))$. Then for every
natural number $M$, $(n + c)^M \left(u_n - \sum_{j=0}^{M-1} a_j (n + c)^{-(j+1)}\right) \to 0$
as $n \to \infty$.

The normalization $u_n \to 0$ fixes the otherwise undetermined additive constant.

Formalized by `Real.tendsto_pow_mul_sub_bernoulli_sum_of_log_diff`, a theorem declared in [MathlibExt/Analysis/Asymptotics/CatalanAsymptoticExpansion.lean, line 1222](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Asymptotics/CatalanAsymptoticExpansion.lean#L1222). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/asymptotic-analysis/asymptotic-expansion-of-the-catalan-numbers/index.html#tendsto-pow-mul-sub-bernoulli-sum-of-log).

## All-orders logarithmic expansion of the Catalan numbers at a real shift

Let $c$ be a real
number, let $C_n$ be the $n$-th Catalan number and $B_k(x)$ the $k$-th Bernoulli polynomial, and
for $j \ge 0$ put
$a_j = (-1)^j \left(B_{j+2}(1/2 - c) - B_{j+2}(2 - c)\right) / ((j + 1)(j + 2))$.
Then for every natural number $M$,
$(n + c)^M \left(\log\left(C_n \sqrt{\pi (n + c)^3} / 4^n\right) -
\sum_{j=0}^{M-1} a_j (n + c)^{-(j+1)}\right) \to 0$ as $n \to \infty$.

Formalized by `tendsto_pow_mul_log_catalan_sub_bernoulli_sum`, a theorem declared in [MathlibExt/Analysis/Asymptotics/CatalanAsymptoticExpansion.lean, line 1469](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Asymptotics/CatalanAsymptoticExpansion.lean#L1469). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/asymptotic-analysis/asymptotic-expansion-of-the-catalan-numbers/index.html#tendsto-pow-mul-log-catalan-sub-bernoull).

## Stirling-type asymptotic expansions of the Catalan numbers

Let $C_n$ be the $n$-th Catalan
number and $B_k$ the $k$-th Bernoulli number, and let $(E_k)$ be a sequence of integers with
$E_0 = 1$ and $\sum_{j=0}^{\lfloor n/2 \rfloor} \binom{n}{2j} E_{n-2j} = 0$ for every $n > 0$
(these are the Euler numbers $1, 0, -1, 0, 5, \dots$). For $k \ge 1$ put
$c_k = (-1)^{k+1} \left((2^{-k} - 2) B_{k+1} - k - 1\right) / (k (k + 1))$ and
$d_k = 2^{-4k-2} (4 - E_{2k}) / k$. Then for every $m \ge 0$, as $n \to \infty$,
$\log\left(C_n \, n \sqrt{\pi n} / 4^n\right) = \sum_{k=1}^{m} c_k n^{-k} + o(n^{-m})$ and,
writing $x = n + 3/4$,
$\log\left(C_n \sqrt{\pi x^3} / 4^n\right) = \sum_{k=1}^{m} d_k x^{-2k} + o(x^{-2m})$.

The first coefficient is $c_1 = -9/8$, matching the classical expansion
$C_n = \frac{4^n}{\sqrt{\pi} \, n^{3/2}} \left(1 - \frac{9}{8n} + \dots\right)$.

Proof: The Catalan recurrence gives a logarithmic first-difference equation.
Telescoping its Bernoulli-polynomial expansion yields both all-orders formulas.

## Sources

- Neven Elezović, "Asymptotic Expansions of Central Binomial Coefficients and Catalan Numbers," Journal of Integer Sequences 17 (2014), Article 14.2.1, Catalan Stirling-type theorem (unlabeled, equation 42), lines 626–637, https://cs.uwaterloo.ca/journals/JIS/VOL17/Elezovic/elezovic5.tex

Formalized by `MetaMathlibExt.catalan_stirling_asymptotic_expansions`, a theorem declared in [MathlibExt/Analysis/Asymptotics/CatalanAsymptoticExpansion.lean, line 1582](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Asymptotics/CatalanAsymptoticExpansion.lean#L1582). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/asymptotic-analysis/asymptotic-expansion-of-the-catalan-numbers/index.html#catalan-stirling-asymptotic-expansions).

## Uniqueness of the even-power shift in Catalan asymptotics

Let
$C_n = \binom{2n}{n} / (n + 1)$ be the $n$-th Catalan number. For a real number $\alpha$, there is
a real sequence $(a_k)_{k \ge 0}$ with $a_{2k+1} = 0$ for every $k$ such that, for every
$N \ge 0$, the difference
$C_n \sqrt{\pi} \, (n + \alpha)^{3/2} / 4^n - \sum_{k=0}^{N} a_k (n + \alpha)^{-k}$ is
$o\left((n + \alpha)^{-N}\right)$ as $n \to \infty$, if and only if $\alpha = 3/4$.

Elezović phrases this as the expansion "containing only odd terms"; the condition meant is that
the odd-indexed coefficients vanish: his displayed series for $\alpha = 3/4$ has only even powers,
and his proof obtains $\alpha = 3/4$ by setting the first odd coefficient to zero.

Proof: The reverse implication exponentiates the all-orders logarithmic expansion of the Catalan
numbers and uses the reflection symmetry of the Bernoulli polynomials to eliminate odd powers. The
first logarithmic coefficient gives uniqueness, following Elezović.

## Sources

- Neven Elezović, "Asymptotic Expansions of Central Binomial Coefficients and Catalan Numbers," Journal of Integer Sequences 17 (2014), Article 14.2.1, Corollary, lines 568–578, https://cs.uwaterloo.ca/journals/JIS/VOL17/Elezovic/elezovic5.tex

Formalized by `MetaMathlibExt.catalan_odd_terms_shift_unique`, a theorem declared in [MathlibExt/Analysis/Asymptotics/CatalanOddTermsShift.lean, line 586](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Asymptotics/CatalanOddTermsShift.lean#L586). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/asymptotic-analysis/asymptotic-expansion-of-the-catalan-numbers/index.html#catalan-odd-terms-shift-unique).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Asymptotic expansion of the Catalan numbers](https://deicyde.github.io/atlas-lean/roadmap/Analysis/asymptotic-analysis/asymptotic-expansion-of-the-catalan-numbers/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Analysis/asymptotic-analysis/asymptotic-expansion-of-the-catalan-numbers)
