---
declaration: section
origin: cited
lean: MetaMathlibExt.average_cardFactors_over_h_free, MetaMathlibExt.IsConsecutivePolynomialFamily, Nat.SamePrimeSupport
statement: formalized
proof: formalized
---

# Integers with restricted factorization: its own results

3 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/special-integer-classes/index.html).

Squarefree, k-free, k-full and powerful, smooth and rough numbers, highly composite numbers, integers with prescribed prime factors.

## Average number of prime factors of h-free integers

Let $h \ge 2$ be an integer. Call a
positive integer $n$ $h$-free if every prime occurs in the factorization of $n$ with exponent less
than $h$, and write $\Omega(n)$ for the number of prime factors of $n$ counted with multiplicity
and $\zeta$ for the Riemann zeta function. Then, as the real number $x$ tends to infinity,

$$
\sum_{\substack{1 \le n \le x \\ n \ h\text{-free}}} \Omega(n)
= \frac{x \log\log x}{\zeta(h)} + O(x).
$$

## Sources

- Rafael Jakimczuk and Matilde Lalín, "The Number of Prime Factors on Average in Certain Integer Sequences," Journal of Integer Sequences 25 (2022), Article 22.2.3, Theorem, lines 110–117, https://cs.uwaterloo.ca/journals/JIS/VOL25/Lalin/lalin2.tex

Formalized by `MetaMathlibExt.average_cardFactors_over_h_free`, a theorem declared in [MathlibExt/NumberTheory/PrimeCounting/AverageOmegaHFree.lean, line 2357](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PrimeCounting/AverageOmegaHFree.lean#L2357). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/special-integer-classes/index.html#average-card-factors-over-h-free).

## Consecutive polynomial family

Let $k$ be a natural number. A family
$L_0, \dots, L_{k-1}$ of polynomials in $\mathbb{Z}[X]$ is consecutive when
$L_{i+1} - L_i = 1$ for every $i$ with $i + 1 < k$.

Formalized by `MetaMathlibExt.IsConsecutivePolynomialFamily`, a definition declared in [MathlibExt/NumberTheory/ConsecutivePolynomial.lean, line 32](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/ConsecutivePolynomial.lean#L32). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/special-integer-classes/index.html#is-consecutive-polynomial-family).

## Natural numbers with the same prime divisors

Natural numbers $a$ and $b$ have the same
prime support when every prime $p$ divides $a$ if and only if it divides $b$.

Formalized by `Nat.SamePrimeSupport`, a definition declared in [MathlibExt/NumberTheory/PrimeSupport.lean, line 19](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PrimeSupport.lean#L19). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/special-integer-classes/index.html#same-prime-support).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Integers with restricted factorization](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/special-integer-classes/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/arithmetic-functions/special-integer-classes)
