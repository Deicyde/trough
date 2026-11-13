---
declaration: section
origin: cited
lean: MetaMathlibExt.cotangentPowerCoeff, MetaMathlibExt.cotangentPowerCoeff_one_one, MetaMathlibExt.cotangentPowerCoeff_two_two, MetaMathlibExt.I_mul_cot_pow_eq_sum_iteratedDeriv_cot, MetaMathlibExt.cotangentPowerCoeff_eq_zero_of_mod_two_ne, MetaMathlibExt.sum_conj_dirichletCharacter_mul_I_mul_cot_pow_of_odd, MetaMathlibExt.sum_conj_dirichletCharacter_mul_I_mul_cot_pow_of_even, MetaMathlibExt.cotangentPowerCoeff_eq_bernoulli_tuple_sum
statement: formalized
---

# Cotangent power sums

8 results, 3 proved and 5 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/exponential-sums/cotangent-power-sums/index.html).

## Girstmair's cotangent power coefficients

For natural numbers $r$ and $j$, the rational
number $c_{r,j}$ is

$$c_{r,j} = (-1)^{r-1} \sum_{k=j}^{r} \frac{(-2)^{k-j}}{(k-1)!} \binom{r}{k} S(k, j),$$

where $S(k, j)$ is the unsigned Stirling number of the first kind, the number of permutations
of $k$ elements with exactly $j$ cycles. Subtraction of natural numbers is truncated at $0$: for
$r = 0$ the exponent $r - 1$ is read as $0$, and for $j = 0$ the factor $(k-1)!$ of the term
$k = 0$ is read as $0! = 1$.

These coefficients express $(i \cot)^r$ in terms of the derivatives $i^j \cot^{(j-1)}$.

## Sources

- Kurt Girstmair, *Cotangent Power Sums and Character Coordinates*, INTEGERS 25 (2025), Article A63, Equation (8). The equation is not in the journal record; it is read from the arXiv version, arXiv:2504.08330, Section 3, where it also follows from the displayed derivation.

Formalized by `MetaMathlibExt.cotangentPowerCoeff`, a definition declared in [WantedExt/NumberTheory/CotangentPowerSumsWanted.lean, line 30](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/CotangentPowerSumsWanted.lean#L30). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/exponential-sums/cotangent-power-sums/index.html#cotangent-power-coeff).

## Girstmair's coefficient at index (1, 1)

Girstmair's cotangent power coefficient
$c_{1,1}$ equals $1$, matching the identity $i \cot = i \cot$.

## Sources

- Kurt Girstmair, *Cotangent Power Sums and Character Coordinates*, INTEGERS 25 (2025), Article A63, characteristic value of Equation (8).

Formalized by `MetaMathlibExt.cotangentPowerCoeff_one_one`, a theorem declared in [WantedExt/NumberTheory/CotangentPowerSumsWanted.lean, line 38](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/CotangentPowerSumsWanted.lean#L38). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/exponential-sums/cotangent-power-sums/index.html#cotangent-power-coeff-one-one).

## Girstmair's coefficient at index (2, 2)

Girstmair's cotangent power coefficient
$c_{2,2}$ equals $-1$, matching the identity $(i \cot)^2 = 1 - i^2 \cot'$ with
$\cot' = -1 - \cot^2$.

## Sources

- Kurt Girstmair, *Cotangent Power Sums and Character Coordinates*, INTEGERS 25 (2025), Article A63, characteristic value of Equation (8).

Formalized by `MetaMathlibExt.cotangentPowerCoeff_two_two`, a theorem declared in [WantedExt/NumberTheory/CotangentPowerSumsWanted.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/CotangentPowerSumsWanted.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/exponential-sums/cotangent-power-sums/index.html#cotangent-power-coeff-two-two).

## Cotangent powers through cotangent derivatives

Let $c_{r,j}$ be Girstmair's cotangent
power coefficients and $\cot^{(m)}$ the $m$-th derivative of the real cotangent function. For
every natural number $r \ge 1$ and every real number $x$ with $\sin x \ne 0$,

$$(i \cot x)^r = \frac{(-1)^r + 1}{2} + \sum_{j=1}^{r} c_{r,j} \, i^j \cot^{(j-1)}(x).$$

## Sources

- Kurt Girstmair, *Cotangent Power Sums and Character Coordinates*, INTEGERS 25 (2025), Article A63, Proposition 1.

Stated but not proved: `MetaMathlibExt.I_mul_cot_pow_eq_sum_iteratedDeriv_cot` is written with `theorem_wanted` in [WantedExt/NumberTheory/CotangentPowerSumsWanted.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/CotangentPowerSumsWanted.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/exponential-sums/cotangent-power-sums/index.html#i-mul-cot-pow-eq-sum-iterated-deriv-cot).

## Parity of Girstmair's cotangent power coefficients

For natural numbers $j$ and $r$ with
$1 \le j \le r$ and $r \not\equiv j \pmod 2$, Girstmair's cotangent power coefficient $c_{r,j}$
is $0$.

The source deduces this from the $\mathbb{Q}$-linear independence of the functions
$i^j \cot^{(j-1)}$.

## Sources

- Kurt Girstmair, *Cotangent Power Sums and Character Coordinates*, INTEGERS 25 (2025), Article A63, Proposition 1, the sentence that follows it.

Stated but not proved: `MetaMathlibExt.cotangentPowerCoeff_eq_zero_of_mod_two_ne` is written with `theorem_wanted` in [WantedExt/NumberTheory/CotangentPowerSumsWanted.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/CotangentPowerSumsWanted.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/exponential-sums/cotangent-power-sums/index.html#cotangent-power-coeff-eq-zero-of-mod-two).

## Girstmair's cotangent power sums, odd case

Let $n \ge 2$, let $r$ be odd, and let $\chi$
be a complex Dirichlet character modulo $n$ with $\chi(-1) = -1$. Let $f$ be the conductor of
$\chi$, $\chi_f$ the primitive character modulo $f$ attached to $\chi$, and $c_{r,j}$
Girstmair's cotangent power coefficients. Write
$\tau(\overline{\chi_f}) = \sum_{k=1}^{f} \overline{\chi_f(k)} e^{2 \pi i k/f}$ for the Gauss sum
and $B_{j,\chi_f} = f^{j-1} \sum_{k=1}^{f} B_j(k/f) \chi_f(k)$, where $B_j$ is the $j$-th
Bernoulli polynomial. Then

$$\sum_{k} \overline{\chi(k)} \left(i \cot \frac{\pi k}{n}\right)^r = -\tau(\overline{\chi_f})
\sum_{j} \frac{c_{r,j} (2n)^j}{j f^j}
\prod_{p \mid n} \Bigl(1 - \frac{\overline{\chi_f(p)}}{p^j}\Bigr) B_{j,\chi_f},$$

where $k$ runs over $1 \le k \le n$ with $\gcd(k, n) = 1$, $j$ runs over the odd numbers with
$1 \le j \le r$, and $p$ runs over the primes dividing $n$.

The left side is $\tau(\overline{\chi_f})$ times the character coordinate
$y(\chi \mid i^r \cot^r(\pi/n))$ of the source, defined by Equation (3), since
$\sigma_k(i^r \cot^r(\pi/n)) = i^r \cot^r(\pi k/n)$ (Equation (4)).

## Sources

- Kurt Girstmair, *Cotangent Power Sums and Character Coordinates*, INTEGERS 25 (2025), Article A63, Theorem 1, first case.

Stated but not proved: `MetaMathlibExt.sum_conj_dirichletCharacter_mul_I_mul_cot_pow_of_odd` is written with `theorem_wanted` in [WantedExt/NumberTheory/CotangentPowerSumsWanted.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/CotangentPowerSumsWanted.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/exponential-sums/cotangent-power-sums/index.html#sum-conj-dirichlet-character-mul-i-mul-c).

## Girstmair's cotangent power sums, even case

Let $n \ge 2$, let $r \ge 2$ be even, and let
$\chi$ be a complex Dirichlet character modulo $n$ with $\chi(-1) = 1$. Let $f$ be the conductor
of $\chi$, $\chi_f$ the primitive character modulo $f$ attached to $\chi$, and $c_{r,j}$
Girstmair's cotangent power coefficients. Write
$\tau(\overline{\chi_f}) = \sum_{k=1}^{f} \overline{\chi_f(k)} e^{2 \pi i k/f}$ for the Gauss sum,
$B_{j,\chi_f} = f^{j-1} \sum_{k=1}^{f} B_j(k/f) \chi_f(k)$, where $B_j$ is the $j$-th Bernoulli
polynomial, and $\varepsilon_\chi = \varphi(n)$ if $\chi$ is the principal character modulo $n$
and $\varepsilon_\chi = 0$ otherwise. Then

$$\sum_{k} \overline{\chi(k)} \left(i \cot \frac{\pi k}{n}\right)^r = \tau(\overline{\chi_f}) \,
\Bigl(\varepsilon_\chi + \sum_{j} \frac{c_{r,j} (2n)^j}{j f^j}
\prod_{p \mid n} \Bigl(1 - \frac{\overline{\chi_f(p)}}{p^j}\Bigr) B_{j,\chi_f}\Bigr),$$

where $k$ runs over $1 \le k \le n$ with $\gcd(k, n) = 1$, $j$ runs over the even numbers with
$1 \le j \le r$, and $p$ runs over the primes dividing $n$.

The left side is $\tau(\overline{\chi_f})$ times the character coordinate
$y(\chi \mid i^r \cot^r(\pi/n))$ of the source (Equation (3)), and $\varepsilon_\chi$ is
$y(\chi \mid 1)$ (Equation (11)).

## Sources

- Kurt Girstmair, *Cotangent Power Sums and Character Coordinates*, INTEGERS 25 (2025), Article A63, Theorem 1, second case.

Stated but not proved: `MetaMathlibExt.sum_conj_dirichletCharacter_mul_I_mul_cot_pow_of_even` is written with `theorem_wanted` in [WantedExt/NumberTheory/CotangentPowerSumsWanted.lean, line 108](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/CotangentPowerSumsWanted.lean#L108). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/exponential-sums/cotangent-power-sums/index.html#sum-conj-dirichlet-character-mul-i-mul-c-2).

## Cotangent power coefficients through even Bernoulli numbers

Let $c_{r,j}$ be
Girstmair's cotangent power coefficients and $B_m$ the $m$-th Bernoulli number. For natural
numbers $j$ and $r$ with $1 \le j \le r$ and $j \equiv r \pmod 2$,

$$c_{r,j} = \frac{(-1)^{r+1} 2^{r-j}}{(j-1)!} \, d_{r,j},$$

where

$$d_{r,j} = \sum_{(j_1, \dots, j_r)} \prod_{t=1}^{r} \frac{B_{2 j_t}}{(2 j_t)!}$$

and the sum runs over all $r$-tuples $(j_1, \dots, j_r)$ of natural numbers with
$j + 2 j_1 + \dots + 2 j_r = r$. This is Theorem 2 of the source, relating $c_{r,j}$ to the
coefficients $d_{r,j}$ of the earlier literature (Equations (13) and (15)).

## Sources

- Kurt Girstmair, *Cotangent Power Sums and Character Coordinates*, INTEGERS 25 (2025), Article A63, Theorem 2 with Equations (13) and (15).

Stated but not proved: `MetaMathlibExt.cotangentPowerCoeff_eq_bernoulli_tuple_sum` is written with `theorem_wanted` in [WantedExt/NumberTheory/CotangentPowerSumsWanted.lean, line 131](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/CotangentPowerSumsWanted.lean#L131). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/exponential-sums/cotangent-power-sums/index.html#cotangent-power-coeff-eq-bernoulli-tuple).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Cotangent power sums](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/exponential-sums/cotangent-power-sums/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/exponential-sums/cotangent-power-sums)
