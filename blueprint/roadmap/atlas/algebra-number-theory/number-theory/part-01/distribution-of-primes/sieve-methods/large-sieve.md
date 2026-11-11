---
declaration: section
origin: cited
lean: MathlibExt.NumberTheory.PrimeCounting.weightedHilbertCosecant, MathlibExt.NumberTheory.PrimeCounting.weightedLargeSieve, MathlibExt.NumberTheory.PrimeCounting.arithmeticLargeSieve_progression
statement: formalized
proof: formalized
---

# Large sieve

3 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/sieve-methods/large-sieve/index.html).

## The Montgomery–Vaughan weighted Hilbert inequality

Let $\iota$ be a finite index set and
for $r \in \iota$ let $x_r$ and $\delta_r > 0$ be real numbers and $z_r$ a complex number. Write
$\|t\|$ for the distance from a real number $t$ to the nearest integer, and suppose that
$\delta_r \le \|x_r - x_s\|$ for all $r \ne s$. Then

$$
\left| \sum_{r} \sum_{s \ne r} \frac{z_r \overline{z_s}}{\sin(\pi (x_r - x_s))} \right| \le
\frac{3}{2} \sum_{r} \frac{|z_r|^2}{\delta_r}.
$$

## Sources

- Montgomery–Vaughan (1974), Theorem 1, in its weighted circle form. The proof follows Yangjit, arXiv:2203.14950, lines 166–205, 209–462, and 596–640: Selberg's eigenvector identity, the Hermitian spectral theorem, and convex circle packing estimates for the one-pole and two-pole cosecant-square sums.

Formalized by `MathlibExt.NumberTheory.PrimeCounting.weightedHilbertCosecant`, a theorem declared in [MathlibExt/NumberTheory/PrimeCounting/WeightedHilbert.lean, line 2131](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/PrimeCounting/WeightedHilbert.lean#L2131). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/sieve-methods/large-sieve/index.html#weighted-hilbert-cosecant).

## The Montgomery–Vaughan weighted large sieve

Let $N$ be a natural number, let $a_n$ be complex
numbers, let $\iota$ be a finite index set and for $r \in \iota$ let $x_r$ and $\delta_r > 0$ be
real numbers. Write $\|t\|$ for the distance from a real number $t$ to the nearest integer, and
suppose that $\delta_r \le \|x_r - x_s\|$ for all $r \ne s$. Then

$$
\sum_{r} \left( N + \frac{3}{2 \delta_r} \right)^{-1}
\left| \sum_{n=0}^{N-1} a_n e^{2 \pi i n x_r} \right|^2 \le \sum_{n=0}^{N-1} |a_n|^2.
$$

## Sources

- Montgomery–Vaughan, *The large sieve* (1973), Theorem 1, equations (1.5)–(1.6) and (2.4), lines 227–321. The proof uses duality, the exact geometric sum, and `weightedHilbertCosecant`.

Formalized by `MathlibExt.NumberTheory.PrimeCounting.weightedLargeSieve`, a theorem declared in [MathlibExt/NumberTheory/PrimeCounting/WeightedLargeSieve.lean, line 381](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/PrimeCounting/WeightedLargeSieve.lean#L381). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/sieve-methods/large-sieve/index.html#weighted-large-sieve).

## Arithmetic large sieve for primes in a progression

Let $N$, $z$, $q$ and $a$ be natural
numbers with $z > 0$ and $q > 0$, and let $S$ be a finite set of natural numbers less than $N$
such that for every $n \in S$ the number $qn + a$ is prime and greater than $z$. Write $\mu$ for
the Möbius function and $\varphi$ for Euler's totient function. Then

$$
\left(\sum_{r=1}^{z} \frac{\mu(r)^2}{\varphi(r)\,(N + 3rz/2)}\right) |S|^2
\le \frac{q}{\varphi(q)}\,|S|.
$$

## Sources

- Montgomery–Vaughan, *The large sieve* (1973), Corollary 1 and Lemma 3, equations (2.7) and (3.2), lines 322–461. The Farey fractions are weighted by the denominator-dependent spacing from `weightedLargeSieve`.

Formalized by `MathlibExt.NumberTheory.PrimeCounting.arithmeticLargeSieve_progression`, a theorem declared in [MathlibExt/NumberTheory/PrimeCounting/ArithmeticLargeSieve.lean, line 1079](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/PrimeCounting/ArithmeticLargeSieve.lean#L1079). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/sieve-methods/large-sieve/index.html#arithmetic-large-sieve-progression).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Large sieve](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/sieve-methods/large-sieve/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/distribution-of-primes/sieve-methods/large-sieve)
