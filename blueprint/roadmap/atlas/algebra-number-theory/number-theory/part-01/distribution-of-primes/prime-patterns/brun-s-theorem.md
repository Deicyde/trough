---
declaration: section
origin: cited
lean: MathlibExt.NumberTheory.PrimeCounting.BrunTwinPrimeReciprocalsWanted.brun_twin_prime_reciprocal_series_summable, MathlibExt.NumberTheory.PrimeCounting.brunTwinPrimeReciprocalTerm, MathlibExt.NumberTheory.PrimeCounting.summable_brunTwinPrimeReciprocalTerm, MathlibExt.NumberTheory.PrimeCounting.brunConstant, MathlibExt.NumberTheory.PrimeCounting.hasSum_brunConstant, MathlibExt.NumberTheory.PrimeCounting.brunConstant_lower_bound, MathlibExt.NumberTheory.PrimeCounting.brunConstant_upper_bound
statement: formalized
---

# Brun's theorem

7 results, 5 proved and 2 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-patterns/brun-s-theorem/index.html).

## Brun's theorem on twin primes

The series
$\sum_{p} \left(\frac{1}{p} + \frac{1}{p + 2}\right)$, taken over all primes $p$ such that
$p + 2$ is also prime, converges in $\mathbb{R}$.

Each twin-prime pair $(p, p + 2)$ is indexed by its smaller member, so a prime lying in two
pairs, such as $5$ in $(3, 5)$ and $(5, 7)$, is counted once for each pair. The statement holds
trivially if there are only finitely many twin-prime pairs.

## Sources

- Alexei Kourbatov and Marek Wolf, "On the First Occurrences of Gaps Between Primes in a Residue Class," Journal of Integer Sequences 23 (2020), <https://cs.uwaterloo.ca/journals/JIS/VOL23/Wolf/wolf2.tex>, lines 684–705. Corroboration: Prapanpong Pongsriiam and Kota Saito, "Palindromes and Antipalindromes in Short Intervals," Journal of Integer Sequences 26 (2023), <https://cs.uwaterloo.ca/journals/JIS/VOL26/Saito/saito1.tex>, lines 205–210. The sources attribute the theorem to V. Brun's 1919 paper on convergence or finiteness of the reciprocal twin-prime series.

Formalized by `MathlibExt.NumberTheory.PrimeCounting.BrunTwinPrimeReciprocalsWanted.brun_twin_prime_reciprocal_series_summable`, a theorem declared in [MathlibExt/NumberTheory/PrimeCounting/BrunTwinPrimeReciprocals.lean, line 1325](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/PrimeCounting/BrunTwinPrimeReciprocals.lean#L1325). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-patterns/brun-s-theorem/index.html#brun-twin-prime-reciprocal-series-summab).

## Twin-prime reciprocal term

For a natural number $p$, the twin-prime reciprocal term
$t(p)$ is the real number $\frac{1}{p} + \frac{1}{p + 2}$ when $p$ and $p + 2$ are both prime,
and $0$ otherwise.

## Sources

- teorth/optimizationproblems, “Brun's Constant,” `constants/81a.md`; the convention counts a prime once for every twin-prime pair containing it.

Formalized by `MathlibExt.NumberTheory.PrimeCounting.brunTwinPrimeReciprocalTerm`, a definition declared in [MathlibExt/NumberTheory/PrimeCounting/BrunConstant.lean, line 28](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/PrimeCounting/BrunConstant.lean#L28). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-patterns/brun-s-theorem/index.html#brun-twin-prime-reciprocal-term).

## Summability of the twin-prime reciprocal terms

For a natural number $p$, let $t(p)$ be
$\frac{1}{p} + \frac{1}{p + 2}$ when $p$ and $p + 2$ are both prime and $0$ otherwise. Then the
series $\sum_{p \ge 0} t(p)$ converges unconditionally in $\mathbb{R}$.

Formalized by `MathlibExt.NumberTheory.PrimeCounting.summable_brunTwinPrimeReciprocalTerm`, a theorem declared in [MathlibExt/NumberTheory/PrimeCounting/BrunConstant.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/PrimeCounting/BrunConstant.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-patterns/brun-s-theorem/index.html#summable-brun-twin-prime-reciprocal-term).

## Brun's constant

Brun's constant is the real number
$B = \sum_{p} \left(\frac{1}{p} + \frac{1}{p + 2}\right)$, the sum over all primes $p$ such that
$p + 2$ is also prime. A prime lying in two twin-prime pairs, such as $5$ in $(3, 5)$ and
$(5, 7)$, is counted once for each pair.

Formalized by `MathlibExt.NumberTheory.PrimeCounting.brunConstant`, a definition declared in [MathlibExt/NumberTheory/PrimeCounting/BrunConstant.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/PrimeCounting/BrunConstant.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-patterns/brun-s-theorem/index.html#brun-constant).

## Brun's constant is the sum of the twin-prime reciprocal series

For a natural number $p$,
let $t(p)$ be $\frac{1}{p} + \frac{1}{p + 2}$ when $p$ and $p + 2$ are both prime and $0$
otherwise. Then the series $\sum_{p \ge 0} t(p)$ over the natural numbers converges
unconditionally in $\mathbb{R}$, and its sum is Brun's constant.

Formalized by `MathlibExt.NumberTheory.PrimeCounting.hasSum_brunConstant`, a theorem declared in [MathlibExt/NumberTheory/PrimeCounting/BrunConstant.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/PrimeCounting/BrunConstant.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-patterns/brun-s-theorem/index.html#has-sum-brun-constant).

## Lower bound for Brun's constant

Brun's constant $B$, the sum of
$\frac{1}{p} + \frac{1}{p + 2}$ over all primes $p$ such that $p + 2$ is also prime, satisfies
$B > 1.840503$.

## Sources

- Dave Platt and Tim Trudgian, “Improved bounds on Brun's constant,” Experimental Mathematics 28 (2019), no. 2, 179–184; arXiv:1803.01925. The bound is also recorded in teorth/optimizationproblems, `constants/81a.md`.

Stated but not proved: `MathlibExt.NumberTheory.PrimeCounting.brunConstant_lower_bound` is written with `theorem_wanted` in [WantedExt/NumberTheory/PrimeCounting/BrunConstantBoundsWanted.lean, line 30](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/PrimeCounting/BrunConstantBoundsWanted.lean#L30). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-patterns/brun-s-theorem/index.html#brun-constant-lower-bound).

## Upper bound for Brun's constant

Brun's constant $B$, the sum of
$\frac{1}{p} + \frac{1}{p + 2}$ over all primes $p$ such that $p + 2$ is also prime, satisfies
$B < 2.288513$.

## Sources

- Dave Platt and Tim Trudgian, “Improved bounds on Brun's constant,” Experimental Mathematics 28 (2019), no. 2, 179–184; arXiv:1803.01925. The bound is also recorded in teorth/optimizationproblems, `constants/81a.md`.

Stated but not proved: `MathlibExt.NumberTheory.PrimeCounting.brunConstant_upper_bound` is written with `theorem_wanted` in [WantedExt/NumberTheory/PrimeCounting/BrunConstantBoundsWanted.lean, line 39](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/PrimeCounting/BrunConstantBoundsWanted.lean#L39). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-patterns/brun-s-theorem/index.html#brun-constant-upper-bound).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Brun's theorem](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-patterns/brun-s-theorem/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/distribution-of-primes/prime-patterns/brun-s-theorem)
