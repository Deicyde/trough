---
declaration: section
origin: cited
lean: Nat.primeCountingMod, Nat.primeCountingMod_one, Nat.primeCountingMod_eq_card_filter_range, Chebyshev.psiResidueClass, Chebyshev.psiResidueClass_of_lt_one, Chebyshev.tendsto_psiResidueClass_div_self, Chebyshev.exists_abs_sum_residueClass_div_sub_log_le, Chebyshev.weakPNT_arithmeticProgression
statement: formalized
proof: formalized
---

# Prime number theorem for arithmetic progressions

10 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/primes-in-progressions/prime-number-theorem-for-arithmetic-progressions/index.html).

## Prime counting in a residue class

For natural numbers $X$, $q$ and $a$, $\pi(X; q, a)$ is
the number of primes $p \le X$ with $p \equiv a \pmod q$. The modulus $q = 1$ is allowed, and for
$q = 0$ the congruence means $p = a$.

Formalized by `Nat.primeCountingMod`, a definition declared in [MathlibExt/NumberTheory/PrimeCounting/ResidueClass.lean, line 28](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/PrimeCounting/ResidueClass.lean#L28). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/primes-in-progressions/prime-number-theorem-for-arithmetic-progressions/index.html#prime-counting-mod).

## Prime counting modulo one

For all natural numbers $X$ and $a$, the number $\pi(X; 1, a)$
of primes $p \le X$ with $p \equiv a \pmod 1$ equals $\pi(X)$, the number of primes $p \le X$.

Modulus one imposes no residue condition.

Formalized by `Nat.primeCountingMod_one`, a theorem declared in [MathlibExt/NumberTheory/PrimeCounting/ResidueClass.lean, line 33](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/PrimeCounting/ResidueClass.lean#L33). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/primes-in-progressions/prime-number-theorem-for-arithmetic-progressions/index.html#prime-counting-mod-one).

## Residue-class prime count as a filtered range

For all natural numbers $n$, $q$ and $a$,
the number $\pi(n; q, a)$ of primes $p \le n$ with $p \equiv a \pmod q$ equals the number of
integers $p$ with $0 \le p \le n$ such that $p$ is prime and $p \equiv a \pmod q$.

Formalized by `Nat.primeCountingMod_eq_card_filter_range`, a theorem declared in [MathlibExt/NumberTheory/PrimeCounting/ResidueClass.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/PrimeCounting/ResidueClass.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/primes-in-progressions/prime-number-theorem-for-arithmetic-progressions/index.html#prime-counting-mod-eq-card-filter-range).

## Chebyshev's function in a residue class

For a natural number $q$, a residue class
$a \in \mathbb{Z}/q\mathbb{Z}$ and a real number $x$, $\psi(x; q, a)$ is the sum of the von
Mangoldt function $\Lambda(n)$ over the positive integers $n \le x$ with $n \equiv a \pmod q$.

Formalized by `Chebyshev.psiResidueClass`, a definition declared in [MathlibExt/NumberTheory/PrimeCounting/ResidueClassPsi.lean, line 25](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/PrimeCounting/ResidueClassPsi.lean#L25). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/primes-in-progressions/prime-number-theorem-for-arithmetic-progressions/index.html#psi-residue-class).

## The residue-class Chebyshev function vanishes below one

For every natural number $q$,
every residue class $a \in \mathbb{Z}/q\mathbb{Z}$ and every real number $x < 1$, we have
$\psi(x; q, a) = 0$, where $\psi(x; q, a)$ is the sum of the von Mangoldt function $\Lambda(n)$
over the positive integers $n \le x$ with $n \equiv a \pmod q$.

Formalized by `Chebyshev.psiResidueClass_of_lt_one`, a theorem declared in [MathlibExt/NumberTheory/PrimeCounting/ResidueClassPsi.lean, line 29](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/PrimeCounting/ResidueClassPsi.lean#L29). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/primes-in-progressions/prime-number-theorem-for-arithmetic-progressions/index.html#psi-residue-class-of-lt-one).

## Prime number theorem for Chebyshev's function in a reduced residue class

Let $q \ge 1$
be an integer, let $b$ be a unit of $\mathbb{Z}/q\mathbb{Z}$, let $\Lambda$ be the von Mangoldt
function and let $\varphi$ be Euler's totient function. For real $x$ let $\psi(x; q, b)$ be the
sum of $\Lambda(n)$ over the integers $1 \le n \le x$ with $n \equiv b \pmod{q}$. Then
$\psi(x; q, b)/x \to 1/\varphi(q)$ as the real number $x$ tends to infinity.

Formalized by `Chebyshev.tendsto_psiResidueClass_div_self`, a lemma declared in [MathlibExt/NumberTheory/PrimeCounting/WeakPNTArithmeticProgression.lean, line 686](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/PrimeCounting/WeakPNTArithmeticProgression.lean#L686). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/primes-in-progressions/prime-number-theorem-for-arithmetic-progressions/index.html#tendsto-psi-residue-class-div-self).

## Mertens' theorem in arithmetic progressions

Let $q \ge 1$ be an integer, let $b$ be a
unit of $\mathbb{Z}/q\mathbb{Z}$, let $\Lambda$ be the von Mangoldt function and let $\varphi$ be
Euler's totient function. There is a real constant $C$ such that for every real $x \ge 1$,

$$
\left| \sum_{\substack{1 \le n \le x \\ n \equiv b \pmod{q}}} \frac{\Lambda(n)}{n} -
\frac{\log x}{\varphi(q)} \right| \le C.
$$

Formalized by `Chebyshev.exists_abs_sum_residueClass_div_sub_log_le`, a lemma declared in [MathlibExt/NumberTheory/PrimeCounting/WeakPNTArithmeticProgression.lean, line 723](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/PrimeCounting/WeakPNTArithmeticProgression.lean#L723). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/primes-in-progressions/prime-number-theorem-for-arithmetic-progressions/index.html#exists-abs-sum-residue-class-div-sub-log).

## Weak prime number theorem in arithmetic progressions

Let $q$ and $a$ be natural numbers with
$a < q$ and $\gcd(a, q) = 1$, let $\Lambda$ be the von Mangoldt function and let $\varphi$ be
Euler's totient function. Then, as $N \to \infty$ through the natural numbers,

$$
\frac{1}{N} \sum_{\substack{0 \le n < N \\ n \equiv a \pmod{q}}} \Lambda(n) \to
\frac{1}{\varphi(q)}.
$$

## Sources

- the proved theorem `PrimeNumberTheoremAnd.WeakPNT_AP` in [PrimeNumberTheoremAnd](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd), and its use in [arXiv:2608.24035](https://arxiv.org/abs/2608.24035). Lean preserves the source's natural representative and half-open `Finset.range` normalization, while omitting the redundant assumption `1 ≤ q`, which follows from `a < q`.

Formalized by `Chebyshev.weakPNT_arithmeticProgression`, a theorem declared in [MathlibExt/NumberTheory/PrimeCounting/WeakPNTArithmeticProgression.lean, line 1002](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/PrimeCounting/WeakPNTArithmeticProgression.lean#L1002). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/primes-in-progressions/prime-number-theorem-for-arithmetic-progressions/index.html#weak-pnt-arithmetic-progression).

## Prime number theorem in arithmetic progressions

Let $q \ge 2$ and $a$ be natural numbers
with $\gcd(a, q) = 1$, and for each natural number $n$ let $N(n)$ be the number of primes
$p \le n$ with $p \equiv a \pmod q$. Then $N(n) \log n / n \to 1 / \varphi(q)$ as $n \to \infty$,
where $\varphi$ is Euler's totient function and $\log$ is the natural logarithm.

## Sources

- G. L. Dirichlet 1837 existence, PNT for AP by de la Vallée Poussin and Hadamard 1896-1899 extensions; textbook in Montgomery-Vaughan, Multiplicative Number Theory I, Multiplicative Number Theory

Formalized by `MathlibExt.NumberTheory.PrimeNumberTheoremAPWanted.prime_number_theorem_arithmetic_progression`, a theorem declared in [MathlibExt/NumberTheory/PrimeNumberTheoremAP.lean, line 241](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/PrimeNumberTheoremAP.lean#L241). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/primes-in-progressions/prime-number-theorem-for-arithmetic-progressions/index.html#prime-number-theorem-arithmetic-progress).

## Prime number theorem for the residue-class prime count

Let $q \ge 2$ and $a$ be natural
numbers with $\gcd(a, q) = 1$, and let $\pi(n; q, a)$ be the number of primes $p \le n$ with
$p \equiv a \pmod q$. Then $\pi(n; q, a) \log n / n \to 1 / \varphi(q)$ as $n \to \infty$,
where $\varphi$ is Euler's totient function and $\log$ is the natural logarithm.

Formalized by `MathlibExt.NumberTheory.PrimeNumberTheoremAPWanted.tendsto_primeCountingMod_mul_log_div`, a theorem declared in [MathlibExt/NumberTheory/PrimeNumberTheoremAP.lean, line 273](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/PrimeNumberTheoremAP.lean#L273). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/primes-in-progressions/prime-number-theorem-for-arithmetic-progressions/index.html#tendsto-prime-counting-mod-mul-log-div).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Prime number theorem for arithmetic progressions](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/primes-in-progressions/prime-number-theorem-for-arithmetic-progressions/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/distribution-of-primes/primes-in-progressions/prime-number-theorem-for-arithmetic-progressions)
