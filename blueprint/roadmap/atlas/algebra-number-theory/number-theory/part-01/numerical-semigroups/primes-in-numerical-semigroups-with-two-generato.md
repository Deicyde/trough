---
declaration: section
origin: cited
lean: MetaMathlibExt.twoGenerator_dvd_sub_of_eq, MetaMathlibExt.exists_eq_of_ncard_twoGeneratorReps, MetaMathlibExt.card_primes_ellNumericalSemigroup_eq, MetaMathlibExt.vonMangoldt_sum_ellNumericalSemigroup_asymptotic, MetaMathlibExt.card_primes_ellNumericalSemigroup_asymptotic
statement: formalized
---

# Primes in numerical semigroups with two generators

5 results, 5 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/numerical-semigroups/primes-in-numerical-semigroups-with-two-generato/index.html).

## Two representations by coprime generators

Let $c$ and $d$ be coprime natural numbers.
If natural numbers $x, y, x', y'$ satisfy $cx + dy = cx' + dy'$, then $c$ divides $y - y'$ and
$d$ divides $x - x'$ in the integers.

The paper's standing assumption $1 < c < d$ is not needed and is dropped.

## Sources

- Yuchen Ding and Takao Komatsu, *On a Conjecture of Ramírez Alfonsín and Skałba, III*, INTEGERS 25 (2025), Article A51, Lemma 1.

Stated but not proved: `MetaMathlibExt.twoGenerator_dvd_sub_of_eq` is written with `theorem_wanted` in [WantedExt/NumberTheory/RamirezAlfonsinSkalbaWanted.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/RamirezAlfonsinSkalbaWanted.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/numerical-semigroups/primes-in-numerical-semigroups-with-two-generato/index.html#two-generator-dvd-sub-of-eq).

## Normal form of a number with exactly $\ell$ representations

Let $c$ and $d$ be coprime
positive integers, and let $n$ and $\ell$ be natural numbers such that the equation
$n = cx + dy$ has exactly $\ell$ solutions $(x, y)$ in natural numbers. Then there are natural
numbers $x_0 < d$ and $y_0 < c$ with $n = (\ell - 1)cd + cx_0 + dy_0$ in the integers.

The identity is stated over the integers, so $\ell = 0$ is included (then $\ell - 1 = -1$). The
paper's standing assumption $1 < c < d$ is weakened to $0 < c$, $0 < d$.

## Sources

- Yuchen Ding and Takao Komatsu, *On a Conjecture of Ramírez Alfonsín and Skałba, III*, INTEGERS 25 (2025), Article A51, Lemma 2.

Stated but not proved: `MetaMathlibExt.exists_eq_of_ncard_twoGeneratorReps` is written with `theorem_wanted` in [WantedExt/NumberTheory/RamirezAlfonsinSkalbaWanted.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/RamirezAlfonsinSkalbaWanted.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/numerical-semigroups/primes-in-numerical-semigroups-with-two-generato/index.html#exists-eq-of-ncard-two-generator-reps).

## Counting primes with more than $\ell$ representations

Let $c$ and $d$ be coprime
natural numbers with $1 < c < d$, let $\ell$ be a natural number, and put
$g_\ell(c, d) = (\ell + 1)cd - c - d$. Write $\pi_{\ell,c,d}$ for the number of primes
$n \le g_\ell(c, d)$ such that the equation $n = cx + dy$ has more than $\ell$ solutions
$(x, y)$ in natural numbers. Then $\pi_{\ell,c,d}$ equals the number of primes $n$ with
$\ell cd < n \le g_\ell(c, d)$ of the form $n = \ell cd + cx_0 + dy_0$ for some natural numbers
$x_0 \le d$ and $y_0 \le c$.

## Sources

- Yuchen Ding and Takao Komatsu, *On a Conjecture of Ramírez Alfonsín and Skałba, III*, INTEGERS 25 (2025), Article A51, Lemma 3, with `g_ℓ(c, d)` from equation (1).

Stated but not proved: `MetaMathlibExt.card_primes_ellNumericalSemigroup_eq` is written with `theorem_wanted` in [WantedExt/NumberTheory/RamirezAlfonsinSkalbaWanted.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/RamirezAlfonsinSkalbaWanted.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/numerical-semigroups/primes-in-numerical-semigroups-with-two-generato/index.html#card-primes-ell-numerical-semigroup-eq).

## Weighted count of primes in the $\ell$-numerical semigroup

For every natural number
$\ell$ and every $\varepsilon > 0$ there is a natural number $C$ such that the following holds
for all coprime natural numbers $c$ and $d$ with $C \le c < d$. For a natural number $k$ put
$g_k(c, d) = (k + 1)cd - c - d$, so that $g_0(c, d) = cd - c - d$, and let $\psi_{\ell,c,d}$ be
the sum of the von Mangoldt function $\Lambda(n)$ over the natural numbers $n$ with
$\ell cd < n \le g_\ell(c, d)$ of the form $n = \ell cd + cx_0 + dy_0$ for some natural numbers
$x_0 \le d$ and $y_0 \le c$. Then

$$
\left|\psi_{\ell,c,d} - \frac{g_0(c, d)}{2}\right| < \varepsilon \, \frac{g_0(c, d)}{2}.
$$

That is, $\psi_{\ell,c,d} \sim g_0(c, d)/2$ as $c \to \infty$, uniformly over coprime $d > c$.

## Sources

- Yuchen Ding and Takao Komatsu, *On a Conjecture of Ramírez Alfonsín and Skałba, III*, INTEGERS 25 (2025), Article A51, Proposition 1, with `g_ℓ(c, d)` from equation (1).

Stated but not proved: `MetaMathlibExt.vonMangoldt_sum_ellNumericalSemigroup_asymptotic` is written with `theorem_wanted` in [WantedExt/NumberTheory/RamirezAlfonsinSkalbaWanted.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/RamirezAlfonsinSkalbaWanted.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/numerical-semigroups/primes-in-numerical-semigroups-with-two-generato/index.html#von-mangoldt-sum-ell-numerical-semigroup).

## Asymptotic count of primes with more than $\ell$ representations

For every natural
number $\ell$ and every $\varepsilon > 0$ there is a natural number $C$ such that the following
holds for all coprime natural numbers $c$ and $d$ with $C \le c < d$. Put
$g_\ell(c, d) = (\ell + 1)cd - c - d$, and let $\pi_{\ell,c,d}$ be the number of primes
$n \le g_\ell(c, d)$ such that the equation $n = cx + dy$ has more than $\ell$ solutions
$(x, y)$ in natural numbers. Then, with $\pi$ the prime-counting function,

$$
\left|\pi_{\ell,c,d} - \frac{\pi(g_\ell(c, d))}{2\ell + 2}\right| <
\varepsilon \, \frac{\pi(g_\ell(c, d))}{2\ell + 2}.
$$

That is, $\pi_{\ell,c,d} \sim \pi(g_\ell(c, d))/(2\ell + 2)$ as $c \to \infty$, uniformly over
coprime $d > c$.

## Sources

- Yuchen Ding and Takao Komatsu, *On a Conjecture of Ramírez Alfonsín and Skałba, III*, INTEGERS 25 (2025), Article A51, Theorem 1, with `g_ℓ(c, d)` from equation (1).

Stated but not proved: `MetaMathlibExt.card_primes_ellNumericalSemigroup_asymptotic` is written with `theorem_wanted` in [WantedExt/NumberTheory/RamirezAlfonsinSkalbaWanted.lean, line 99](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/RamirezAlfonsinSkalbaWanted.lean#L99). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/numerical-semigroups/primes-in-numerical-semigroups-with-two-generato/index.html#card-primes-ell-numerical-semigroup-asym).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Primes in numerical semigroups with two generators](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/numerical-semigroups/primes-in-numerical-semigroups-with-two-generato/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/numerical-semigroups/primes-in-numerical-semigroups-with-two-generato)
