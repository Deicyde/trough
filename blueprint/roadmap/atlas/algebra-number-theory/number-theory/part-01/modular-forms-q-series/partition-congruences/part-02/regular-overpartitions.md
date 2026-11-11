---
declaration: section
origin: cited
lean: MetaMathlibExt.regularOverpartitionCount, MetaMathlibExt.regularOverpartitionCount_zero, MetaMathlibExt.regularOverpartitionCount_one, MetaMathlibExt.regularOverpartitionCount_eq_coeff_truncatedProduct, MetaMathlibExt.regularOverpartition_prime_power_two_density, MetaMathlibExt.regularOverpartition_three_mul_prime_power_two_density, MetaMathlibExt.regularOverpartition_three_mul_two_power_density, MetaMathlibExt.regularOverpartition_three_mul_two_power_many_primes
statement: formalized
---

# ℓ-regular overpartitions

15 results, 3 proved and 12 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/regular-overpartitions/index.html).

## Number of $\ell$-regular overpartitions

For natural numbers $\ell$ and $n$, $A_\ell(n)$ is
the number of overpartitions of $n$ in which no part is divisible by $\ell$.

No positivity restriction is placed on $\ell$; for $\ell = 0$ every overpartition of $n$ is
counted, since parts are positive.

## Sources

- Murugan P and Fathima S. N, *Arithmetic Density of Certain ℓ-Regular Overpartitions*, INTEGERS 25 (2025), Article A3, Identity (1).

Formalized by `MetaMathlibExt.regularOverpartitionCount`, a definition declared in [WantedExt/Combinatorics/Enumerative/RegularOverpartitionDensityWanted.lean, line 40](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/RegularOverpartitionDensityWanted.lean#L40). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/regular-overpartitions/index.html#regular-overpartition-count).

## One $\ell$-regular overpartition of zero

For every natural number $\ell$, the number
$A_\ell(0)$ of overpartitions of $0$ with no part divisible by $\ell$ equals $1$: the only one is
the empty overpartition.

The statement also covers $\ell = 0$, a harmless extension of the paper's positive regularity
parameter.

## Sources

- Murugan P and Fathima S. N, *Arithmetic Density of Certain ℓ-Regular Overpartitions*, INTEGERS 25 (2025), Article A3, Identity (1).

Formalized by `MetaMathlibExt.regularOverpartitionCount_zero`, a theorem declared in [WantedExt/Combinatorics/Enumerative/RegularOverpartitionDensityWanted.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/RegularOverpartitionDensityWanted.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/regular-overpartitions/index.html#regular-overpartition-count-zero).

## Two $\ell$-regular overpartitions of one

For every natural number $\ell \ge 2$, the number
$A_\ell(1)$ of overpartitions of $1$ with no part divisible by $\ell$ equals $2$: they are the
single part $1$, without and with an overline.

Among positive $\ell$, the hypothesis $\ell \ge 2$ says exactly that $\ell$ does not divide the
sole part $1$.

## Sources

- Murugan P and Fathima S. N, *Arithmetic Density of Certain ℓ-Regular Overpartitions*, INTEGERS 25 (2025), Article A3, Identity (1).

Formalized by `MetaMathlibExt.regularOverpartitionCount_one`, a theorem declared in [WantedExt/Combinatorics/Enumerative/RegularOverpartitionDensityWanted.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/RegularOverpartitionDensityWanted.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/regular-overpartitions/index.html#regular-overpartition-count-one).

## Truncated generating function for $\ell$-regular overpartitions

Let $\ell \ge 1$, $N$ and
$n \le N$ be natural numbers, and let $A_\ell(n)$ be the number of overpartitions of $n$ with no
part divisible by $\ell$. Then the coefficient of $X^n$ in the polynomial

$$\prod_{1 \le k \le N,\ \ell \nmid k} \Big((1 + X^k) \sum_{i=0}^{N} X^{ki}\Big) \in \mathbb{N}[X]$$

equals $A_\ell(n)$.

This is a finite-polynomial form of the generating function
$\sum_{n \ge 0} A_\ell(n) q^n = \prod_{k \ge 1,\ \ell \nmid k} (1 + q^k)/(1 - q^k)$: each
geometric series is cut off at $i = N$, and only coefficients up to degree $N$ are compared.

## Sources

- Murugan P and Fathima S. N, *Arithmetic Density of Certain ℓ-Regular Overpartitions*, INTEGERS 25 (2025), Article A3, Identity (1).

Stated but not proved: `MetaMathlibExt.regularOverpartitionCount_eq_coeff_truncatedProduct` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/RegularOverpartitionDensityWanted.lean, line 133](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/RegularOverpartitionDensityWanted.lean#L133). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/regular-overpartitions/index.html#regular-overpartition-count-eq-coeff-tru).

## $p$-regular overpartitions are almost always divisible by $2^j$

Let $p$ be an odd prime,
let $j \ge 1$, and let $A_p(n)$ be the number of overpartitions of $n$ with no part divisible by
$p$. Then

$$\lim_{X \to \infty} \frac{\#\{n : 0 \le n \le X,\ 2^j \mid A_p(n)\}}{X} = 1,$$

where $X$ runs over the natural numbers.

## Sources

- Murugan P and Fathima S. N, *Arithmetic Density of Certain ℓ-Regular Overpartitions*, INTEGERS 25 (2025), Article A3, Theorem 1.

Stated but not proved: `MetaMathlibExt.regularOverpartition_prime_power_two_density` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/RegularOverpartitionDensityWanted.lean, line 148](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/RegularOverpartitionDensityWanted.lean#L148). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/regular-overpartitions/index.html#regular-overpartition-prime-power-two-de).

## Almost all $3p$-regular overpartition counts are divisible by $2^j$

Write $A_\ell(m)$ for
the number of overpartitions of $m$ none of whose parts is divisible by $\ell$. Let $p$ be an
odd prime and let $j \ge 1$. Then the number of natural numbers $n$ with $0 \le n \le X$ and
$2^j \mid A_{3p}(n)$, divided by $X$, tends to $1$ as the natural number $X$ tends to infinity.

## Sources

- Murugan P and Fathima S. N, *Arithmetic Density of Certain ℓ-Regular Overpartitions*, INTEGERS 25 (2025), Article A3, Theorem 2.

Stated but not proved: `MetaMathlibExt.regularOverpartition_three_mul_prime_power_two_density` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/RegularOverpartitionDensityWanted.lean, line 164](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/RegularOverpartitionDensityWanted.lean#L164). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/regular-overpartitions/index.html#regular-overpartition-three-mul-prime-po).

## Almost all $3 \cdot 2^\alpha$-regular overpartition counts are divisible by $2^j$

Write
$A_\ell(m)$ for the number of overpartitions of $m$ none of whose parts is divisible by $\ell$.
Let $\alpha \ge 1$ and $j \ge \alpha + 1$ be natural numbers. Then the number of natural numbers
$n$ with $0 \le n \le X$ and $2^j \mid A_{3 \cdot 2^\alpha}(n)$, divided by $X$, tends to $1$ as
the natural number $X$ tends to infinity.

## Sources

- Murugan P and Fathima S. N, *Arithmetic Density of Certain ℓ-Regular Overpartitions*, INTEGERS 25 (2025), Article A3, Theorem 3.

Stated but not proved: `MetaMathlibExt.regularOverpartition_three_mul_two_power_density` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/RegularOverpartitionDensityWanted.lean, line 180](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/RegularOverpartitionDensityWanted.lean#L180). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/regular-overpartitions/index.html#regular-overpartition-three-mul-two-powe).

## Congruences modulo powers of two for $3 \cdot 2^\alpha$-regular overpartitions

Write
$A_\ell(m)$ for the number of overpartitions of $m$ none of whose parts is divisible by $\ell$.
For every natural number $\alpha \ge 1$ there is a natural number $c$ with the following
property. Let $d \ge 1$ be a natural number, let $p_1, \dots, p_{c+d}$ be distinct primes, each
coprime to $6$, and let $n$ be a natural number that is divisible by $24$ and coprime to every
$p_i$. Then $A_{3 \cdot 2^\alpha}(p_1 p_2 \cdots p_{c+d} \, n / 24) \equiv 0 \pmod{2^d}$.

The hypothesis that $24$ divides $n$ makes the argument an integer; the paper reads this value
off a series in $q^{24}$.

## Sources

- Murugan P and Fathima S. N, *Arithmetic Density of Certain ℓ-Regular Overpartitions*, INTEGERS 25 (2025), Article A3, Theorem 4.

Stated but not proved: `MetaMathlibExt.regularOverpartition_three_mul_two_power_many_primes` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/RegularOverpartitionDensityWanted.lean, line 201](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/RegularOverpartitionDensityWanted.lean#L201). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/regular-overpartitions/index.html#regular-overpartition-three-mul-two-powe-2).

## $\ell$-regular overpartitions vanish modulo $4$ along families of primes

For a natural
number $\ell$, let $A_\ell(m)$ be the number of overpartitions of $m$ with no part divisible by
$\ell$. Let $\ell \equiv 3 \pmod 4$, let $k$, $n$ and $j$ be natural numbers, and let
$p_1, \dots, p_{k+1}$ be primes, not necessarily distinct, each greater than $2$ and congruent
to $3$ modulo $4$. If $j \not\equiv 0 \pmod{p_{k+1}}$, then

$$A_\ell\big(p_1^2 \cdots p_k^2 \, p_{k+1} \, (p_{k+1}(4n + 1) + 4j)\big) \equiv 0 \pmod 4.$$

The paper takes $j$ to be an integer; here $j$ is a natural number.

## Sources

- Murugan P and Fathima S. N, *Arithmetic Density of Certain ℓ-Regular Overpartitions*, INTEGERS 25 (2025), Article A3, Theorem 5.

Stated but not proved: `MetaMathlibExt.regularOverpartition_mod_four_prime_family` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/RegularOverpartitionDensityWanted.lean, line 224](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/RegularOverpartitionDensityWanted.lean#L224). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/regular-overpartitions/index.html#regular-overpartition-mod-four-prime-fam).

## $\ell$-regular overpartitions vanish modulo $4$ along powers of one prime

For a natural
number $\ell$, let $A_\ell(m)$ be the number of overpartitions of $m$ with no part divisible by
$\ell$. Let $\ell \equiv 3 \pmod 4$, and let $p > 2$ be a prime with $p \not\equiv 1 \pmod 6$.
Then for all natural numbers $k$, $n$ and $j$ with $j \not\equiv 0 \pmod p$,

$$A_\ell\big(p^{2k+2}(4n + 1) + 4j \, p^{2k+1}\big) \equiv 0 \pmod 4.$$

The condition modulo $6$ is the one printed in the paper; it is not replaced by the condition
$p \equiv 3 \pmod 4$ of Theorem 5.

## Sources

- Murugan P and Fathima S. N, *Arithmetic Density of Certain ℓ-Regular Overpartitions*, INTEGERS 25 (2025), Article A3, Corollary 1.

Stated but not proved: `MetaMathlibExt.regularOverpartition_mod_four_single_prime` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/RegularOverpartitionDensityWanted.lean, line 245](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/RegularOverpartitionDensityWanted.lean#L245). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/regular-overpartitions/index.html#regular-overpartition-mod-four-single-pr).

## $\ell$-regular overpartitions vanish modulo $4$ on progressions modulo $4\ell$

For a
natural number $\ell$, let $A_\ell(m)$ be the number of overpartitions of $m$ with no part
divisible by $\ell$. Let $\ell \equiv 3 \pmod 4$, and let $n$ and $j$ be natural numbers with
$j \not\equiv (\ell - 3)/4 \pmod{\ell}$. Then $A_\ell(4\ell n + 4j + 3) \equiv 0 \pmod 4$.

## Sources

- Murugan P and Fathima S. N, *Arithmetic Density of Certain ℓ-Regular Overpartitions*, INTEGERS 25 (2025), Article A3, Theorem 6.

Stated but not proved: `MetaMathlibExt.regularOverpartition_mod_four_progression` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/RegularOverpartitionDensityWanted.lean, line 264](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/RegularOverpartitionDensityWanted.lean#L264). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/regular-overpartitions/index.html#regular-overpartition-mod-four-progressi).

## Self-similarity modulo 7 of 7-regular overpartition counts

Write $A_7(m)$ for the number
of overpartitions of $m$ none of whose parts is divisible by $7$. For all natural numbers $n$
and $k$, $A_7(7^{2k}(4n+3)) \equiv A_7(4n+3) \pmod 7$.

## Sources

- Murugan P and Fathima S. N, *Arithmetic Density of Certain ℓ-Regular Overpartitions*, INTEGERS 25 (2025), Article A3, Theorem 7.

Stated but not proved: `MetaMathlibExt.regularOverpartition_seven_self_similarity` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/RegularOverpartitionDensityWanted.lean, line 277](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/RegularOverpartitionDensityWanted.lean#L277). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/regular-overpartitions/index.html#regular-overpartition-seven-self-similar).

## Ramanujan-type congruences modulo 7 for 7-regular overpartitions

Write $A_7(m)$ for the
number of overpartitions of $m$ none of whose parts is divisible by $7$. For every natural number
$n$, we have $A_7(16n+4) \equiv 0 \pmod 7$; $A_7(64n+i) \equiv 0 \pmod 7$ for every natural
number $i < 64$ with $i \equiv 4 \pmod{32}$; $A_7(256n+i) \equiv 0 \pmod 7$ for every natural
number $i < 256$ with $i \equiv 4 \pmod{32}$; and $A_7(1024n+i) \equiv 0 \pmod 7$ for every
natural number $i < 1024$ with $i \equiv 4 \pmod{32}$.

## Sources

- Murugan P and Fathima S. N, *Arithmetic Density of Certain ℓ-Regular Overpartitions*, INTEGERS 25 (2025), Article A3, Theorem 8.

Stated but not proved: `MetaMathlibExt.regularOverpartition_seven_ramanujan_congruences` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/RegularOverpartitionDensityWanted.lean, line 293](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/RegularOverpartitionDensityWanted.lean#L293). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/regular-overpartitions/index.html#regular-overpartition-seven-ramanujan-co).

## Prime-power congruence for truncated Euler products

Let $s$ and $t$ be positive integers,
let $p$ be a prime and let $N$ be a natural number. Then every coefficient of the polynomial

$$\Big(\prod_{m=1}^{N} (1 - X^{sm})\Big)^{p^t} - \Big(\prod_{m=1}^{N} (1 - X^{spm})\Big)^{p^{t-1}}$$

in $\mathbb{Z}[X]$ is divisible by $p^t$.

Since the truncated products agree with the infinite products in all degrees up to $N$, letting
$N$ grow gives the congruence of formal power series
$\prod_{m \ge 1} (1 - q^{sm})^{p^t} \equiv \prod_{m \ge 1} (1 - q^{spm})^{p^{t-1}} \pmod{p^t}$.

## Sources

- Murugan P and Fathima S. N, *Arithmetic Density of Certain ℓ-Regular Overpartitions*, INTEGERS 25 (2025), Article A3, Lemma 1.

Stated but not proved: `MetaMathlibExt.finiteEulerProduct_primePower_congruence` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/RegularOverpartitionDensityWanted.lean, line 313](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/RegularOverpartitionDensityWanted.lean#L313). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/regular-overpartitions/index.html#finite-euler-product-prime-power-congrue).

## Double coset representatives for $\Gamma_0(N)$

Let $N$ be a natural number such that
either $N$ is squarefree, or $N$ is even and $N/2$ is squarefree. Write $\Gamma_0(N)$ for the
group of matrices in $\mathrm{SL}_2(\mathbb{Z})$ whose lower left entry is divisible by $N$, and
$T = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$. Then for every
$\gamma \in \mathrm{SL}_2(\mathbb{Z})$ there is exactly one natural number $\delta$ dividing $N$
for which there exist $A \in \Gamma_0(N)$ and an integer $h$ with

$$\gamma = A \begin{pmatrix} 1 & 0 \\ \delta & 1 \end{pmatrix} T^h.$$

Equivalently, the matrices $\begin{pmatrix} 1 & 0 \\ \delta & 1 \end{pmatrix}$ with
$\delta \mid N$ form a complete set of representatives, without repetition, of the double cosets
$\Gamma_0(N) \backslash \mathrm{SL}_2(\mathbb{Z}) / \Gamma_\infty$, where $\Gamma_\infty$ is
generated by $T$; adding $-I$ to $\Gamma_\infty$ changes nothing, as $-I \in \Gamma_0(N)$.

## Sources

- Murugan P and Fathima S. N, *Arithmetic Density of Certain ℓ-Regular Overpartitions*, INTEGERS 25 (2025), Article A3, Lemma 3, quoting Wang, Lemma 4.3. "`N / 2` is squarefree" is read with `2 ∣ N`.

Stated but not proved: `MetaMathlibExt.exists_gamma0_lowerUnipotent_T_zpow_decomposition` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/RegularOverpartitionDensityWanted.lean, line 330](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/RegularOverpartitionDensityWanted.lean#L330). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/regular-overpartitions/index.html#exists-gamma0-lower-unipotent-t-zpow-dec).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: ℓ-regular overpartitions](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/regular-overpartitions/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/regular-overpartitions)
