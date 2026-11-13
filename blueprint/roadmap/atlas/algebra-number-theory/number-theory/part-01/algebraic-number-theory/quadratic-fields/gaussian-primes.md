---
declaration: section
origin: cited
lean: GaussianInt.gaussianInt_isUnit_iff, GaussianInt.gaussianInt_prime_of_natAbs_norm_prime, GaussianInt.gaussianInt_prime_one_add_I, GaussianInt.gaussianInt_two_eq, GaussianInt.unitVal, GaussianInt.unitVal_inj, GaussianInt.unitVal_complete, GaussianInt.unitValInv
statement: formalized
proof: formalized
---

# Gaussian primes

15 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/quadratic-fields/gaussian-primes/index.html).

## Units of the Gaussian integers

A Gaussian integer $x \in \mathbb{Z}[i]$ is a unit if
and only if $x$ is one of $1$, $-1$, $i$ and $-i$.

Formalized by `GaussianInt.gaussianInt_isUnit_iff`, a theorem declared in [MathlibExt/NumberTheory/GaussianIntPrimeBasics.lean, line 29](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/GaussianIntPrimeBasics.lean#L29). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/quadratic-fields/gaussian-primes/index.html#gaussian-int-is-unit-iff).

## Gaussian integers of prime norm are prime

Let $\pi = a + bi \in \mathbb{Z}[i]$ and
let $N(\pi) = a^2 + b^2$ be its norm. If the absolute value of $N(\pi)$ is a prime number,
then $\pi$ is a prime element of $\mathbb{Z}[i]$.

Formalized by `GaussianInt.gaussianInt_prime_of_natAbs_norm_prime`, a theorem declared in [MathlibExt/NumberTheory/GaussianIntPrimeBasics.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/GaussianIntPrimeBasics.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/quadratic-fields/gaussian-primes/index.html#gaussian-int-prime-of-nat-abs-norm-prime).

## 1 + i is a Gaussian prime

The Gaussian integer $1 + i$ is a prime element of
$\mathbb{Z}[i]$; its norm is $2$.

Formalized by `GaussianInt.gaussianInt_prime_one_add_I`, a theorem declared in [MathlibExt/NumberTheory/GaussianIntPrimeBasics.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/GaussianIntPrimeBasics.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/quadratic-fields/gaussian-primes/index.html#gaussian-int-prime-one-add-i).

## Factorization of 2 in the Gaussian integers

In $\mathbb{Z}[i]$ we have
$2 = -i \cdot (1 + i)^2$, where $-i$ is a unit with inverse $i$.

Formalized by `GaussianInt.gaussianInt_two_eq`, a theorem declared in [MathlibExt/NumberTheory/GaussianIntPrimeBasics.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/GaussianIntPrimeBasics.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/quadratic-fields/gaussian-primes/index.html#gaussian-int-two-eq).

## Enumeration of the Gaussian units

The map $u$ on $\{0, 1, 2, 3\}$ with $u_0 = 1$,
$u_1 = -1$, $u_2 = i$ and $u_3 = -i$ in $\mathbb{Z}[i]$, listing the four units of
$\mathbb{Z}[i]$.

Formalized by `GaussianInt.unitVal`, a definition declared in [MathlibExt/NumberTheory/GaussianIntPrimeBasics.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/GaussianIntPrimeBasics.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/quadratic-fields/gaussian-primes/index.html#unit-val).

## The four Gaussian units are distinct

Let $u_0 = 1$, $u_1 = -1$, $u_2 = i$ and
$u_3 = -i$ in $\mathbb{Z}[i]$. For $j, k \in \{0, 1, 2, 3\}$, if $u_j = u_k$ then $j = k$.

Formalized by `GaussianInt.unitVal_inj`, a theorem declared in [MathlibExt/NumberTheory/GaussianIntPrimeBasics.lean, line 88](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/GaussianIntPrimeBasics.lean#L88). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/quadratic-fields/gaussian-primes/index.html#unit-val-inj).

## The enumeration of the Gaussian units is complete

Let $u_0 = 1$, $u_1 = -1$, $u_2 = i$
and $u_3 = -i$. Every unit $u$ of $\mathbb{Z}[i]$ equals $u_j$ for some $j \in \{0, 1, 2, 3\}$.

Formalized by `GaussianInt.unitVal_complete`, a theorem declared in [MathlibExt/NumberTheory/GaussianIntPrimeBasics.lean, line 93](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/GaussianIntPrimeBasics.lean#L93). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/quadratic-fields/gaussian-primes/index.html#unit-val-complete).

## Inverses of the Gaussian units

The map $v$ on $\{0, 1, 2, 3\}$ with $v_0 = 1$,
$v_1 = -1$, $v_2 = -i$ and $v_3 = i$ in $\mathbb{Z}[i]$, listing the inverses of the units
$1$, $-1$, $i$ and $-i$ in that order.

Formalized by `GaussianInt.unitValInv`, a definition declared in [MathlibExt/NumberTheory/GaussianIntPrimeBasics.lean, line 102](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/GaussianIntPrimeBasics.lean#L102). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/quadratic-fields/gaussian-primes/index.html#unit-val-inv).

## Each Gaussian unit times its listed inverse is one

Let $u_0 = 1$, $u_1 = -1$,
$u_2 = i$, $u_3 = -i$ and $v_0 = 1$, $v_1 = -1$, $v_2 = -i$, $v_3 = i$ in $\mathbb{Z}[i]$.
Then $u_j v_j = 1$ for every $j \in \{0, 1, 2, 3\}$.

Formalized by `GaussianInt.unitVal_mul_unitValInv`, a theorem declared in [MathlibExt/NumberTheory/GaussianIntPrimeBasics.lean, line 107](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/GaussianIntPrimeBasics.lean#L107). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/quadratic-fields/gaussian-primes/index.html#unit-val-mul-unit-val-inv).

## Explicit Gaussian prime factors of a prime congruent to 1 mod 4

Let $p$ be a prime with
$p \equiv 1 \pmod 4$. Then there are natural numbers $a$ and $b$ with $a^2 + b^2 = p$ such that
both $a + bi$ and $a - bi$ are prime elements of the Gaussian integers $\mathbb{Z}[i]$.

Formalized by `GaussianInt.gaussianInt_split_prime_sq_add_sq`, a theorem declared in [MathlibExt/NumberTheory/GaussianIntPrimeClassification.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/GaussianIntPrimeClassification.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/quadratic-fields/gaussian-primes/index.html#gaussian-int-split-prime-sq-add-sq).

## Classification of the Gaussian primes

Every prime element $z$ of the Gaussian integers
$\mathbb{Z}[i]$ is associated to one of the following: a rational prime $p$ with
$p \equiv 3 \pmod 4$; one of $a + bi$ and $a - bi$, where $a$ and $b$ are natural numbers with
$a^2 + b^2 = p$ for some rational prime $p \equiv 1 \pmod 4$; or $1 + i$.

Formalized by `GaussianInt.gaussianInt_prime_associated`, a theorem declared in [MathlibExt/NumberTheory/GaussianIntPrimeClassification.lean, line 102](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/GaussianIntPrimeClassification.lean#L102). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/quadratic-fields/gaussian-primes/index.html#gaussian-int-prime-associated).

## Primes congruent to 1 mod 4 split in the Gaussian integers

Let $p$ be a prime with
$p \equiv 1 \pmod 4$. Then there is a prime element $\pi = a + bi$ of $\mathbb{Z}[i]$ whose norm
$N(\pi) = a^2 + b^2$ equals $p$.

Formalized by `GaussianInt.gaussianInt_split_prime`, a theorem declared in [MathlibExt/NumberTheory/GaussianIntSplitPrimes.lean, line 35](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/GaussianIntSplitPrimes.lean#L35). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/quadratic-fields/gaussian-primes/index.html#gaussian-int-split-prime).

## Factoring a prime as a Gaussian integer times its conjugate

Let $p$ be a prime, write
$N(a + bi) = a^2 + b^2$ for the norm on $\mathbb{Z}[i]$, and let $\pi \in \mathbb{Z}[i]$ satisfy
$N(\pi) = p$. Then $p = \pi \bar{\pi}$ in $\mathbb{Z}[i]$, where $\bar{\pi}$ is the complex
conjugate of $\pi$, and $\bar{\pi}$ is a prime element of $\mathbb{Z}[i]$.

Formalized by `GaussianInt.gaussianInt_split_conj`, a theorem declared in [MathlibExt/NumberTheory/GaussianIntSplitPrimes.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/GaussianIntSplitPrimes.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/quadratic-fields/gaussian-primes/index.html#gaussian-int-split-conj).

## Gaussian integers of split prime norm are not associate to their conjugates

Write
$N(a + bi) = a^2 + b^2$ for the norm on $\mathbb{Z}[i]$. Let $p$ be a prime with
$p \equiv 1 \pmod 4$ and let $\pi \in \mathbb{Z}[i]$ satisfy $N(\pi) = p$. Then the complex
conjugate $\bar{\pi}$ is not associated to $\pi$: there is no unit $u$ of $\mathbb{Z}[i]$ with
$\bar{\pi} u = \pi$.

Formalized by `GaussianInt.gaussianInt_split_nonassociated`, a theorem declared in [MathlibExt/NumberTheory/GaussianIntSplitPrimes.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/GaussianIntSplitPrimes.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/quadratic-fields/gaussian-primes/index.html#gaussian-int-split-nonassociated).

## Number of Gaussian integers of norm a power of a split prime

Write
$N(a + bi) = a^2 + b^2$ for the norm on $\mathbb{Z}[i]$. Let $p$ be a prime with
$p \equiv 1 \pmod 4$, let $e$ be a natural number, and suppose $\pi \in \mathbb{Z}[i]$ is a prime
element with $N(\pi) = p$. Then exactly $4(e + 1)$ Gaussian integers $\alpha$ satisfy
$|N(\alpha)| = p^e$.

Formalized by `GaussianInt.gaussianInt_card_repr_prime_pow`, a theorem declared in [MathlibExt/NumberTheory/GaussianIntSplitPrimes.lean, line 176](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/GaussianIntSplitPrimes.lean#L176). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/quadratic-fields/gaussian-primes/index.html#gaussian-int-card-repr-prime-pow).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Gaussian primes](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/quadratic-fields/gaussian-primes/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/algebraic-number-theory/quadratic-fields/gaussian-primes)
