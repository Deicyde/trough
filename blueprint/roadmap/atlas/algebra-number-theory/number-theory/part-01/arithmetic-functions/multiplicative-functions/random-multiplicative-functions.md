---
declaration: section
origin: cited
lean: MetaMathlibExt.RandomMultiplicativeFunction.rademacherMeasure, MetaMathlibExt.RandomMultiplicativeFunction.rademacherMeasure_singleton, MetaMathlibExt.RandomMultiplicativeFunction.IsRademacherFamily, MetaMathlibExt.RandomMultiplicativeFunction.exists_rademacherFamily, MetaMathlibExt.RandomMultiplicativeFunction.primeSignNat, MetaMathlibExt.RandomMultiplicativeFunction.IsRademacherFamily.measurable_primeSignNat, MetaMathlibExt.RandomMultiplicativeFunction.rademacherFunction, MetaMathlibExt.RandomMultiplicativeFunction.rademacherFunction_apply
statement: formalized
---

# Random multiplicative functions

17 results, 16 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/random-multiplicative-functions/index.html).

## Rademacher measure on the integer units

The Rademacher measure is the uniform probability
measure on the two integer units $\{-1, 1\}$.

Formalized by `MetaMathlibExt.RandomMultiplicativeFunction.rademacherMeasure`, a definition declared in [MathlibExt/Probability/NumberTheory/RandomMultiplicativeFunction.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/NumberTheory/RandomMultiplicativeFunction.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/random-multiplicative-functions/index.html#rademacher-measure).

## Each Rademacher sign has probability one half

For each integer unit $x \in \{-1, 1\}$,
the Rademacher measure of the singleton $\{x\}$ is $1/2$.

Formalized by `MetaMathlibExt.RandomMultiplicativeFunction.rademacherMeasure_singleton`, a theorem declared in [MathlibExt/Probability/NumberTheory/RandomMultiplicativeFunction.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/NumberTheory/RandomMultiplicativeFunction.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/random-multiplicative-functions/index.html#rademacher-measure-singleton).

## Rademacher family

Let $\mu$ be a measure on a measurable space $\Omega$. A family
$(X_p)$, indexed by the primes $p$, of maps $X_p \colon \Omega \to \{-1, 1\}$ into the units of
$\mathbb{Z}$ is a Rademacher family for $\mu$ when every $X_p$ is measurable, every $X_p$ has
law the Rademacher measure (the uniform measure on $\{-1, 1\}$) under $\mu$, and the family
is mutually independent under $\mu$.

Formalized by `MetaMathlibExt.RandomMultiplicativeFunction.IsRademacherFamily`, a definition declared in [MathlibExt/Probability/NumberTheory/RandomMultiplicativeFunction.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/NumberTheory/RandomMultiplicativeFunction.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/random-multiplicative-functions/index.html#is-rademacher-family).

## Existence of a Rademacher family

There exist a measurable space $\Omega$, a probability
measure $\mu$ on $\Omega$ and a family $(X_p)$, indexed by the primes $p$, of maps
$X_p \colon \Omega \to \{-1, 1\}$ into the units of $\mathbb{Z}$ that is a Rademacher family
for $\mu$.

Formalized by `MetaMathlibExt.RandomMultiplicativeFunction.exists_rademacherFamily`, a theorem declared in [MathlibExt/Probability/NumberTheory/RandomMultiplicativeFunction.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/NumberTheory/RandomMultiplicativeFunction.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/random-multiplicative-functions/index.html#exists-rademacher-family).

## Prime sign of a natural number

Let $X = (X_p)$ be a family, indexed by the primes $p$,
of maps $X_p \colon \Omega \to \{-1, 1\}$ into the units of $\mathbb{Z}$. For a natural number
$n$ and $\omega \in \Omega$, the prime sign of $n$ at $\omega$ is the integer $X_n(\omega)$ if
$n$ is prime and $1$ otherwise.

Formalized by `MetaMathlibExt.RandomMultiplicativeFunction.primeSignNat`, a definition declared in [MathlibExt/Probability/NumberTheory/RandomMultiplicativeFunction.lean, line 91](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/NumberTheory/RandomMultiplicativeFunction.lean#L91). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/random-multiplicative-functions/index.html#prime-sign-nat).

## Measurability of the prime signs

Let $(X_p)$ be a Rademacher family for a measure
$\mu$ on a measurable space $\Omega$. For every natural number $n$, the map
$\omega \mapsto \varepsilon_n(\omega)$ from $\Omega$ to $\mathbb{Z}$ is measurable, where the
prime sign $\varepsilon_n(\omega)$ is $X_n(\omega)$ if $n$ is prime and $1$ otherwise.

Formalized by `MetaMathlibExt.RandomMultiplicativeFunction.IsRademacherFamily.measurable_primeSignNat`, a theorem declared in [MathlibExt/Probability/NumberTheory/RandomMultiplicativeFunction.lean, line 107](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/NumberTheory/RandomMultiplicativeFunction.lean#L107). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/random-multiplicative-functions/index.html#measurable-prime-sign-nat).

## Rademacher random multiplicative function

Let $(X_p)_p$ be a family of maps
$X_p : \Omega \to \{-1, 1\}$ indexed by the primes, and let $\omega \in \Omega$. The Rademacher
random multiplicative function at $\omega$ is the arithmetic function
$f : \mathbb{N} \to \mathbb{Z}$ with $f(0) = 0$ and

$$f(n) = \mu(n)^2 \prod_{p \mid n} X_p(\omega)$$

for $n \ge 1$, where $\mu$ is the Möbius function and the product runs over the distinct primes
$p$ dividing $n$.

Formalized by `MetaMathlibExt.RandomMultiplicativeFunction.rademacherFunction`, a definition declared in [MathlibExt/Probability/NumberTheory/RandomMultiplicativeFunction.lean, line 127](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/NumberTheory/RandomMultiplicativeFunction.lean#L127). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/random-multiplicative-functions/index.html#rademacher-function).

## Formula for the Rademacher random multiplicative function

Let $X = (X_p)$ be a family,
indexed by the primes $p$, of maps $X_p \colon \Omega \to \{-1, 1\}$, let $\omega \in \Omega$,
and let $f$ be the Rademacher random multiplicative function of $X$ at $\omega$. For every
natural number $n \neq 0$, $f(n) = \mu(n)^2 \prod_{p \mid n} \varepsilon_p(\omega)$, where
$\mu$ is the Möbius function, the product runs over the distinct primes $p$ dividing $n$, and
$\varepsilon_p(\omega)$ is the prime sign of $p$ at $\omega$.

Formalized by `MetaMathlibExt.RandomMultiplicativeFunction.rademacherFunction_apply`, a theorem declared in [MathlibExt/Probability/NumberTheory/RandomMultiplicativeFunction.lean, line 132](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/NumberTheory/RandomMultiplicativeFunction.lean#L132). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/random-multiplicative-functions/index.html#rademacher-function-apply).

## The Rademacher random multiplicative function on squarefree numbers

Let $X = (X_p)$ be
a family, indexed by the primes $p$, of maps $X_p \colon \Omega \to \{-1, 1\}$, let
$\omega \in \Omega$, and let $f$ be the Rademacher random multiplicative function of $X$ at
$\omega$. For every squarefree natural number $n$,
$f(n) = \prod_{p \mid n} \varepsilon_p(\omega)$, the product of the prime signs
$\varepsilon_p(\omega)$ at $\omega$ over the distinct primes $p$ dividing $n$.

Formalized by `MetaMathlibExt.RandomMultiplicativeFunction.rademacherFunction_eq_prod_of_squarefree`, a theorem declared in [MathlibExt/Probability/NumberTheory/RandomMultiplicativeFunction.lean, line 145](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/NumberTheory/RandomMultiplicativeFunction.lean#L145). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/random-multiplicative-functions/index.html#rademacher-function-eq-prod-of-squarefre).

## The Rademacher random multiplicative function vanishes off squarefree numbers

Let
$X = (X_p)$ be a family, indexed by the primes $p$, of maps $X_p \colon \Omega \to \{-1, 1\}$,
let $\omega \in \Omega$, and let $f$ be the Rademacher random multiplicative function of $X$ at
$\omega$. Then $f(n) = 0$ for every natural number $n$ that is not squarefree, including
$n = 0$.

Formalized by `MetaMathlibExt.RandomMultiplicativeFunction.rademacherFunction_eq_zero_of_not_squarefree`, a theorem declared in [MathlibExt/Probability/NumberTheory/RandomMultiplicativeFunction.lean, line 151](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/NumberTheory/RandomMultiplicativeFunction.lean#L151). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/random-multiplicative-functions/index.html#rademacher-function-eq-zero-of-not-squar).

## The Rademacher random multiplicative function is multiplicative

Let $X = (X_p)$ be a
family, indexed by the primes $p$, of maps $X_p \colon \Omega \to \{-1, 1\}$, and let
$\omega \in \Omega$. The Rademacher random multiplicative function $f$ of $X$ at $\omega$
satisfies $f(1) = 1$ and $f(mn) = f(m) f(n)$ for all coprime natural numbers $m$ and $n$.

Formalized by `MetaMathlibExt.RandomMultiplicativeFunction.isMultiplicative_rademacherFunction`, a theorem declared in [MathlibExt/Probability/NumberTheory/RandomMultiplicativeFunction.lean, line 159](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/NumberTheory/RandomMultiplicativeFunction.lean#L159). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/random-multiplicative-functions/index.html#is-multiplicative-rademacher-function).

## Value of the Rademacher function at a prime

Let $(X_p)_p$ be a family of maps
$X_p : \Omega \to \{-1, 1\}$ indexed by the primes, let $\omega \in \Omega$, and let $f$ be the
associated Rademacher random multiplicative function at $\omega$. For every prime $p$, the value
$f(p)$ is the sign assigned to $p$, that is, $f(p) = X_p(\omega)$.

Formalized by `MetaMathlibExt.RandomMultiplicativeFunction.rademacherFunction_prime`, a theorem declared in [MathlibExt/Probability/NumberTheory/RandomMultiplicativeFunction.lean, line 167](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/NumberTheory/RandomMultiplicativeFunction.lean#L167). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/random-multiplicative-functions/index.html#rademacher-function-prime).

## The Rademacher random multiplicative function vanishes at prime squares

Let
$X = (X_p)$ be a family, indexed by the primes $p$, of maps $X_p \colon \Omega \to \{-1, 1\}$,
let $\omega \in \Omega$, and let $f$ be the Rademacher random multiplicative function of $X$ at
$\omega$. Then $f(p^2) = 0$ for every prime $p$.

Formalized by `MetaMathlibExt.RandomMultiplicativeFunction.rademacherFunction_prime_sq`, a theorem declared in [MathlibExt/Probability/NumberTheory/RandomMultiplicativeFunction.lean, line 176](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/NumberTheory/RandomMultiplicativeFunction.lean#L176). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/random-multiplicative-functions/index.html#rademacher-function-prime-sq).

## Measurability of the Rademacher random multiplicative function

Let $(X_p)$ be a
Rademacher family for a measure $\mu$ on a measurable space $\Omega$, and for $\omega \in \Omega$
let $f_\omega$ be the Rademacher random multiplicative function of $(X_p)$ at $\omega$. For
every natural number $n$, the map $\omega \mapsto f_\omega(n)$ from $\Omega$ to $\mathbb{Z}$ is
measurable.

Formalized by `MetaMathlibExt.RandomMultiplicativeFunction.IsRademacherFamily.measurable_rademacherFunction`, a theorem declared in [MathlibExt/Probability/NumberTheory/RandomMultiplicativeFunction.lean, line 184](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/NumberTheory/RandomMultiplicativeFunction.lean#L184). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/random-multiplicative-functions/index.html#measurable-rademacher-function).

## Partial sums of the Rademacher multiplicative function

Given signs
$X_p(\omega) \in \{-1, 1\}$ indexed by the primes $p$ and a sample point $\omega$, and given
$N \in \mathbb{N}$, the partial sum $S_N(\omega)$ is the real number $\sum_{m=1}^{N} f_\omega(m)$,
where $f_\omega$ is the Rademacher multiplicative function of the signs $X_p(\omega)$:
$f_\omega(m) = \prod_{p \mid m} X_p(\omega)$ for squarefree $m$ and $f_\omega(m) = 0$ otherwise.

Formalized by `MathlibExt.NumberTheory.RademacherLILConstantWanted.partialSum`, a definition declared in [WantedExt/NumberTheory/RademacherLILConstantWanted.lean, line 31](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/RademacherLILConstantWanted.lean#L31). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/random-multiplicative-functions/index.html#partial-sum).

## Rademacher LIL constant conjecture

The statement that there is a real constant $c > 0$
such that, for every probability space $(\Omega, \mu)$ and every family $(X_p)_p$ of independent,
measurable random signs indexed by the primes, each uniform on $\{-1, 1\}$, for $\mu$-almost
every $\omega$ the limit superior as $N \to \infty$ of $S_N(\omega) / \sqrt{N \log \log N}$
equals $c$. Here $S_N(\omega) = \sum_{m=1}^{N} f_\omega(m)$ is the partial sum of the Rademacher
random multiplicative function $f_\omega$, given by $f_\omega(m) = \prod_{p \mid m} X_p(\omega)$
for squarefree $m$ and $f_\omega(m) = 0$ otherwise.

This is the question asked in Erdős Problem 520.

Formalized by `MathlibExt.NumberTheory.RademacherLILConstantWanted.conjecture`, a definition declared in [WantedExt/NumberTheory/RademacherLILConstantWanted.lean, line 37](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/RademacherLILConstantWanted.lean#L37). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/random-multiplicative-functions/index.html#conjecture).

## No iterated-logarithm constant for Rademacher multiplicative functions

The Rademacher
LIL constant conjecture is false: there is no real constant $c > 0$ such that, for every
probability space $(\Omega, \mu)$ and every family $(X_p)_p$ of independent, measurable random
signs indexed by the primes, each uniform on $\{-1, 1\}$, for $\mu$-almost every $\omega$ the
limit superior as $N \to \infty$ of $S_N(\omega) / \sqrt{N \log \log N}$ equals $c$. Here
$S_N(\omega) = \sum_{m=1}^{N} f_\omega(m)$, where $f_\omega$ is the Rademacher random
multiplicative function: $f_\omega(m) = \prod_{p \mid m} X_p(\omega)$ for squarefree $m$ and
$f_\omega(m) = 0$ otherwise.

Durkan and Pearce-Crump, and independently Verreault, proved that for every $\varepsilon > 0$,
almost surely $|\sum_{n \le x} f_\omega(n)| \ll \sqrt{x} (\log \log x)^{1/4 + \varepsilon}$ as
$x \to \infty$, so the normalized limit superior is almost surely $0$.

## Sources

- B. Durkan, A. Pearce-Crump, A sharp almost sure upper bound for partial sums of random multiplicative functions, arXiv preprint (2026), arXiv:2607.29429, https://arxiv.org/abs/2607.29429; W. Verreault, Almost sure upper bound for sums of random multiplicative functions and critical chaos, arXiv preprint (2026), arXiv:2608.21354, https://arxiv.org/abs/2608.21354.

Stated but not proved: `MathlibExt.NumberTheory.RademacherLILConstantWanted.conjecture_refuted` is written with `theorem_wanted` in [WantedExt/NumberTheory/RademacherLILConstantWanted.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/RademacherLILConstantWanted.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/random-multiplicative-functions/index.html#conjecture-refuted).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Random multiplicative functions](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/random-multiplicative-functions/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/random-multiplicative-functions)
