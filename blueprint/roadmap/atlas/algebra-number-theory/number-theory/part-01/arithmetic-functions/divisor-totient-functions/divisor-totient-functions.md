---
declaration: section
origin: cited
lean: MetaMathlibExt.ford_totient_multiplicity, MathlibExt.NumberTheory.ArithmeticFunction.GronwallSigmaLimsupWanted.gronwall_sigma_limsup, MetaMathlibExt.mobius_formula_relatively_prime_subset_counts_interval
statement: formalized
---

# Divisor and totient functions: its own results

3 results, 2 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/divisor-totient-functions/index.html).

σ, τ, φ, Jordan and Dedekind ψ, unitary and biunitary divisors, gcd-sums, Ramanujan sums, totient multiplicities and values.

## Ford's theorem on totient multiplicities

For every natural number $k \ge 2$ there is a
natural number $m$ such that exactly $k$ natural numbers $x$ satisfy $\varphi(x) = m$, where
$\varphi$ is Euler's totient function.

## Sources

- Kevin Ford, *The Number of Solutions of phi(x) = m*, Annals of Mathematics 150 (1999), DOI 10.2307/121103. Also: https://en.wikipedia.org/wiki/Euler%27s_totient_function

Stated but not proved: `MetaMathlibExt.ford_totient_multiplicity` is written with `theorem_wanted` in [WantedExt/NumberTheory/FordTotientMultiplicityWanted.lean, line 24](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/FordTotientMultiplicityWanted.lean#L24). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/divisor-totient-functions/part-01/index.html#ford-totient-multiplicity).

## Gronwall's theorem

Let $\sigma(n)$ be the sum of the positive divisors of $n$ and let
$\gamma$ be the Euler–Mascheroni constant. Then, as $n$ runs over the natural numbers,
$\limsup_{n \to \infty} \sigma(n) / (n \log \log n) = e^{\gamma}$.

The quotient is read with the conventions $\log 0 = 0$ and $x/0 = 0$, so it is defined for every
natural number $n$; the finitely many $n \le 2$ with $n \log \log n \le 0$ do not affect the
limit superior.

## Sources

- S. Nazardonyavi and S. Yakubovich, "Extremely Abundant Numbers and the Riemann Hypothesis," Journal of Integer Sequences 17 (2014), Article 14.2.8, lines 98–111, https://cs.uwaterloo.ca/journals/JIS/VOL17/Nazar/nazar4.tex; original attribution: T. H. Gronwall, "Some asymptotic expressions in the theory of numbers," Transactions of the AMS 14 (1913), 113–122.

Formalized by `MathlibExt.NumberTheory.ArithmeticFunction.GronwallSigmaLimsupWanted.gronwall_sigma_limsup`, a theorem declared in [MathlibExt/NumberTheory/ArithmeticFunction/GronwallSigmaLimsup.lean, line 3219](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/ArithmeticFunction/GronwallSigmaLimsup.lean#L3219). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/divisor-totient-functions/part-02/index.html#gronwall-sigma-limsup).

## Relatively prime subset counts

Let $\ell < m$ and $k \ge 1$ be natural numbers, and let
$\mu$ be the Möbius function. The number of nonempty subsets of $\{\ell + 1, \dots, m\}$ whose
elements have greatest common divisor $1$ is

$$\sum_{d=1}^{m} \mu(d) \left(2^{\lfloor m/d \rfloor - \lfloor \ell/d \rfloor} - 1\right),$$

and the number of $k$-element subsets of $\{\ell + 1, \dots, m\}$ whose elements have greatest
common divisor $1$ is

$$\sum_{d=1}^{m} \mu(d) \binom{\lfloor m/d \rfloor - \lfloor \ell/d \rfloor}{k}.$$

## Sources

- M. Ayad, V. Coia, and O. Kihel, “The Number of Relatively Prime Subsets of a Finite Union of Sets of Consecutive Integers”, Journal of Integer Sequences 17 (2014), Article 14.3.7, Theorem 1, lines 138-151, <https://cs.uwaterloo.ca/journals/JIS/VOL17/Kihel/kihel10.tex>.

Formalized by `MetaMathlibExt.mobius_formula_relatively_prime_subset_counts_interval`, a theorem declared in [MathlibExt/NumberTheory/ArithmeticFunction/RelativelyPrimeSubsetCounts.lean, line 121](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/ArithmeticFunction/RelativelyPrimeSubsetCounts.lean#L121). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/divisor-totient-functions/part-02/index.html#mobius-formula-relatively-prime-subset-c).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Divisor and totient functions](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/divisor-totient-functions/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/arithmetic-functions/divisor-totient-functions)
