---
declaration: section
origin: cited
lean: MathlibExt.NumberTheory.PrimeCounting.SiegelWalfiszWanted.siegel_walfisz, MathlibExt.NumberTheory.PrimeCounting.UniformPrimeCountingWanted.uniform_prime_counting_arithmetic_progression
statement: formalized
---

# Siegel–Walfisz theorem

2 results, 2 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/primes-in-progressions/siegel-walfisz-theorem/index.html).

## Siegel–Walfisz theorem for Chebyshev's function in residue classes

For every real $N > 0$
there are real constants $c > 0$, $C > 0$ and $X_0 > 1$ such that for every real $x \ge X_0$, every
positive integer $q$ with $q \le (\log x)^N$ and every unit $a$ of $\mathbb{Z}/q\mathbb{Z}$,

$$\left|\psi(x; q, a) - \frac{x}{\varphi(q)}\right| \le C x \exp\left(-c \sqrt{\log x}\right),$$

where $\psi(x; q, a)$ is Chebyshev's function in the residue class $a$ modulo $q$ and $\varphi$ is
Euler's totient function.

The constants may depend on $N$, but not on $x$, $q$, or $a$.

## Sources

- P. Holdridge, *Random Diophantine Equations in the Primes*, arXiv:2305.06306v2, Theorem 4.2, citing H. Davenport, *Multiplicative Number Theory*, 2nd ed., revised by H. L. Montgomery, Springer, 1980, Chapter 22.

Stated but not proved: `MathlibExt.NumberTheory.PrimeCounting.SiegelWalfiszWanted.siegel_walfisz` is written with `theorem_wanted` in [WantedExt/NumberTheory/PrimeCounting/SiegelWalfiszWanted.lean, line 33](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/PrimeCounting/SiegelWalfiszWanted.lean#L33). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/primes-in-progressions/siegel-walfisz-theorem/index.html#siegel-walfisz).

## Siegel–Walfisz theorem for primes in arithmetic progressions

Let $\varphi$ be Euler's
totient function and let $\mathrm{Li}(x) = \int_2^x du / \log u$. For every real $B > 0$ there are
real constants $c > 0$, $C > 0$ and $X_0 \ge 2$ such that for every real $x \ge X_0$ and all
natural numbers $q > 0$ and $b$ with $\gcd(b, q) = 1$ and $q \le (\log x)^B$, the number
$\pi(x; q, b)$ of primes $p \le x$ with $p \equiv b \pmod q$ satisfies

$$\left|\pi(x; q, b) - \frac{\mathrm{Li}(x)}{\varphi(q)}\right| \le C x e^{-c \sqrt{\log x}}.$$

The constants may depend on $B$, but not on $x$, $q$, or $b$. The logarithmic integral is taken
from $2$, as in the source, rather than as the principal value from $0$.

## Sources

- A. Guo, *Exceptional sets for compositions involving Euler's function, the divisor-sum function and Dedekind's function*, arXiv:2608.19972v1, Lemma `siegel`, `main.tex` lines 289–295.

Stated but not proved: `MathlibExt.NumberTheory.PrimeCounting.UniformPrimeCountingWanted.uniform_prime_counting_arithmetic_progression` is written with `theorem_wanted` in [WantedExt/NumberTheory/PrimeCounting/UniformPrimeCountingWanted.lean, line 38](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/PrimeCounting/UniformPrimeCountingWanted.lean#L38). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/primes-in-progressions/siegel-walfisz-theorem/index.html#uniform-prime-counting-arithmetic-progre).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Siegel–Walfisz theorem](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/primes-in-progressions/siegel-walfisz-theorem/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/distribution-of-primes/primes-in-progressions/siegel-walfisz-theorem)
