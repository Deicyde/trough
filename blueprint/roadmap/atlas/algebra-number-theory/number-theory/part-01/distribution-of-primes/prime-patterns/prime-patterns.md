---
declaration: section
origin: cited
lean: MetaMathlibExt.clement_twin_prime_criterion, MathlibExt.NumberTheory.FriedlanderIwaniecWanted.NumberTheory.FriedlanderIwaniec.friedlander_iwaniec, MetaMathlibExt.lemoine_of_le_ten_pow_thirteen
statement: formalized
---

# Prime patterns and conjectures: its own results

3 results, 1 proved and 2 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-patterns/index.html).

Twin primes and Brun's constant, Hardy–Littlewood tuples, Goldbach/Lemoine-type statements, primes represented by polynomials (Friedlander–Iwaniec).

## Clement's criterion for twin primes

For every natural number $p \ge 2$, the numbers
$p$ and $p + 2$ are both prime if and only if

$$4\bigl((p-1)! + 1\bigr) + p \equiv 0 \pmod{p(p+2)}.$$

The hypothesis $p \ge 2$ is needed: the unqualified restatement in the Journal of Integer
Sequences is false at $p = 1$.

Sources:
* JIS restatement: https://cs.uwaterloo.ca/journals/JIS/VOL13/Schmidt/multifact.tex,
  lines 3295-3306.
* Corrected domain: M. Chaves, `Twin Primes and a Primality Test by Indivisibility`,
  arXiv:math/0211034v3, source lines 110-121, citing P. A. Clement,
  `Congruences for Sets of Primes`, Amer. Math. Monthly 56 (1949), 23.

Formalized by `MetaMathlibExt.clement_twin_prime_criterion`, a theorem declared in [MathlibExt/NumberTheory/ClementTwinPrimes.lean, line 223](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/ClementTwinPrimes.lean#L223). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-patterns/index.html#clement-twin-prime-criterion).

## Friedlander–Iwaniec theorem

There are infinitely many primes $p$ of the form
$p = a^2 + b^4$ with $a$ and $b$ natural numbers.

## Sources

- Friedlander, John, and Henryk Iwaniec. “The Polynomial X² + Y⁴ Captures Its Primes.” Annals of Mathematics, vol. 148, no. 3, 1998, pp. 945–1040. JSTOR, https://doi.org/10.2307/121034. Problem `friedlander_iwaniec` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.NumberTheory.FriedlanderIwaniecWanted.NumberTheory.FriedlanderIwaniec.friedlander_iwaniec` is written with `theorem_wanted` in [WantedExt/NumberTheory/FriedlanderIwaniecWanted.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/FriedlanderIwaniecWanted.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-patterns/index.html#friedlander-iwaniec).

## Lemoine's conjecture up to $10^{13}$

Every odd natural number $n$ with
$5 < n \le 10^{13}$ can be written as $n = p + 2q$ with $p$ and $q$ prime.

## Sources

- Zsófia Juhász, Máté Bartalos, Péter Magyar, and Gábor Farkas, *Empirical Verification of a Generalization of Goldbach's Conjecture*, Journal of Integer Sequences 27 (2024), Article 24.4.3, abstract (`jis-2024-24.4.3-abstract-main`).

Stated but not proved: `MetaMathlibExt.lemoine_of_le_ten_pow_thirteen` is written with `theorem_wanted` in [WantedExt/NumberTheory/LemoineVerificationWanted.lean, line 37](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/LemoineVerificationWanted.lean#L37). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-patterns/index.html#lemoine-of-le-ten-pow-thirteen).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Prime patterns and conjectures](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-patterns/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/distribution-of-primes/prime-patterns)
