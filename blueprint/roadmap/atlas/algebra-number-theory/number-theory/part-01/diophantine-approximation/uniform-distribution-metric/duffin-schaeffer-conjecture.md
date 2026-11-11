---
declaration: section
origin: cited
lean: MathlibExt.NumberTheory.DuffinSchaefferConjectureWanted.DuffinSchaefferConjecture.inequality_1_7, MathlibExt.NumberTheory.DuffinSchaefferConjectureWanted.DuffinSchaefferConjecture.𝒜, MathlibExt.NumberTheory.DuffinSchaefferConjectureWanted.DuffinSchaefferConjecture.theorem_1, MathlibExt.NumberTheory.DuffinSchaefferConjectureWanted.DuffinSchaefferConjecture.𝒦, MathlibExt.NumberTheory.DuffinSchaefferConjectureWanted.DuffinSchaefferConjecture.ψ_star, MathlibExt.NumberTheory.DuffinSchaefferConjectureWanted.DuffinSchaefferConjecture.theorem_2_a, MathlibExt.NumberTheory.DuffinSchaefferConjectureWanted.DuffinSchaefferConjecture.theorem_2_b, MathlibExt.NumberTheory.DuffinSchaefferConjectureWanted.DuffinSchaefferConjecture.s_inf
statement: formalized
---

# Duffin–Schaeffer conjecture

10 results, 5 proved and 5 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/uniform-distribution-metric/duffin-schaeffer-conjecture/index.html).

## The approximation inequality (1.7)

For a function $\psi$ from the positive integers to
the nonnegative reals, a real number $\alpha$, a natural number $a$ and a positive integer $q$,
inequality (1.7) is the condition $|\alpha - a/q| \le \psi(q)/q$.

Formalized by `MathlibExt.NumberTheory.DuffinSchaefferConjectureWanted.DuffinSchaefferConjecture.inequality_1_7`, a definition declared in [WantedExt/NumberTheory/DuffinSchaefferConjectureWanted.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/DuffinSchaefferConjectureWanted.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/uniform-distribution-metric/duffin-schaeffer-conjecture/index.html#inequality-1-7).

## The set $\mathcal{A}$ of the Duffin–Schaeffer conjecture

For a function $\psi$ from the
positive integers to the nonnegative reals, $\mathcal{A}(\psi)$ is the set of real numbers
$\alpha \in [0, 1]$ for which inequality (1.7), $|\alpha - a/q| \le \psi(q)/q$, has infinitely
many solutions $(a, q)$ with $a$ a natural number, $q$ a positive integer and $\gcd(a, q) = 1$.

Formalized by `MathlibExt.NumberTheory.DuffinSchaefferConjectureWanted.DuffinSchaefferConjecture.𝒜`, a definition declared in [WantedExt/NumberTheory/DuffinSchaefferConjectureWanted.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/DuffinSchaefferConjectureWanted.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/uniform-distribution-metric/duffin-schaeffer-conjecture/index.html#untitled).

## Koukoulopoulos–Maynard Theorem 1 (Duffin–Schaeffer conjecture)

Let $\psi$ be a function
from the positive integers to the nonnegative reals such that the series
$\sum_{q \ge 1} \psi(q)\varphi(q)/q$ diverges, where $\varphi$ is Euler's totient function. Let
$\mathcal{A}(\psi)$ be the set of real numbers $\alpha \in [0, 1]$ for which
$|\alpha - a/q| \le \psi(q)/q$ has infinitely many solutions with $a$ a natural number, $q$ a
positive integer and $\gcd(a, q) = 1$. Then $\mathcal{A}(\psi)$ is a Borel set and has
Lebesgue measure $1$.

## Sources

- D. Koukoulopoulos and J. Maynard, `On the Duffin-Schaeffer conjecture`, Annals of Math, 192 (1) 2020. Statement taken from https://github.com/ImperialCollegeLondon/AnnalsChallenge. Problem `annals_duffin_schaeffer_conjecture` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.NumberTheory.DuffinSchaefferConjectureWanted.DuffinSchaefferConjecture.theorem_1` is written with `theorem_wanted` in [WantedExt/NumberTheory/DuffinSchaefferConjectureWanted.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/DuffinSchaefferConjectureWanted.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/uniform-distribution-metric/duffin-schaeffer-conjecture/index.html#theorem-1).

## The set $\mathcal{K}$ of Catlin's conjecture

For a function $\psi$ from the positive
integers to the nonnegative reals, $\mathcal{K}(\psi)$ is the set of real numbers
$\alpha \in [0, 1]$ for which inequality (1.7), $|\alpha - a/q| \le \psi(q)/q$, has infinitely
many solutions $(a, q)$ with $a$ a natural number and $q$ a positive integer such that $a \le q$.

The fractions $a/q$ need not be reduced.

Formalized by `MathlibExt.NumberTheory.DuffinSchaefferConjectureWanted.DuffinSchaefferConjecture.𝒦`, a definition declared in [WantedExt/NumberTheory/DuffinSchaefferConjectureWanted.lean, line 86](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/DuffinSchaefferConjectureWanted.lean#L86). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/uniform-distribution-metric/duffin-schaeffer-conjecture/index.html#untitled-2).

## The function $\psi^*$ of Catlin's conjecture

**The function $\psi^*$ of Catlin's conjecture.** For a function $\psi$ from the positive
integers to the nonnegative reals, $\psi^*$ sends each positive integer $q$ to
$\psi^*(q) = \varphi(q) \cdot \sup \{\psi(n)/n : n \text{ a positive integer with } q \mid n\}$,
where $\varphi$ is Euler's totient function and the supremum is taken in $[0, \infty]$.

Formalized by `MathlibExt.NumberTheory.DuffinSchaefferConjectureWanted.DuffinSchaefferConjecture.ψ_star`, a definition declared in [WantedExt/NumberTheory/DuffinSchaefferConjectureWanted.lean, line 91](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/DuffinSchaefferConjectureWanted.lean#L91). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/uniform-distribution-metric/duffin-schaeffer-conjecture/index.html#star).

## Koukoulopoulos–Maynard Theorem 2(a) (Catlin's conjecture, convergent case)

Let $\psi$
be a function from the positive integers to the nonnegative reals, and for each positive integer
$q$ let $\psi^*(q) = \varphi(q) \cdot \sup \{\psi(n)/n : n \text{ a positive integer with }
q \mid n\}$, where $\varphi$ is Euler's totient function and the supremum is taken in
$[0, \infty]$. Let $\mathcal{K}(\psi)$ be the set of real numbers $\alpha \in [0, 1]$ for which
$|\alpha - a/q| \le \psi(q)/q$ has infinitely many solutions with $a$ a natural number and $q$ a
positive integer such that $a \le q$. If $\sum_{q \ge 1} \psi^*(q) < \infty$, then
$\mathcal{K}(\psi)$ is a Borel set and has Lebesgue measure $0$.

## Sources

- D. Koukoulopoulos and J. Maynard, `On the Duffin-Schaeffer conjecture`, Annals of Math, 192 (1) 2020. Statement taken from https://github.com/ImperialCollegeLondon/AnnalsChallenge. Problem `annals_duffin_schaeffer_conjecture` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.NumberTheory.DuffinSchaefferConjectureWanted.DuffinSchaefferConjecture.theorem_2_a` is written with `theorem_wanted` in [WantedExt/NumberTheory/DuffinSchaefferConjectureWanted.lean, line 101](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/DuffinSchaefferConjectureWanted.lean#L101). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/uniform-distribution-metric/duffin-schaeffer-conjecture/index.html#theorem-2-a).

## Koukoulopoulos–Maynard Theorem 2(b) (Catlin's conjecture, divergent case)

Let $\psi$
be a function from the positive integers to the nonnegative reals, and for each positive integer
$q$ let $\psi^*(q) = \varphi(q) \cdot \sup \{\psi(n)/n : n \text{ a positive integer with }
q \mid n\}$, where $\varphi$ is Euler's totient function and the supremum is taken in
$[0, \infty]$. Let $\mathcal{K}(\psi)$ be the set of real numbers $\alpha \in [0, 1]$ for which
$|\alpha - a/q| \le \psi(q)/q$ has infinitely many solutions with $a$ a natural number and $q$ a
positive integer such that $a \le q$. If $\sum_{q \ge 1} \psi^*(q) = \infty$, then
$\mathcal{K}(\psi)$ is a Borel set and has Lebesgue measure $1$.

## Sources

- D. Koukoulopoulos and J. Maynard, `On the Duffin-Schaeffer conjecture`, Annals of Math, 192 (1) 2020. Statement taken from https://github.com/ImperialCollegeLondon/AnnalsChallenge. Problem `annals_duffin_schaeffer_conjecture` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.NumberTheory.DuffinSchaefferConjectureWanted.DuffinSchaefferConjecture.theorem_2_b` is written with `theorem_wanted` in [WantedExt/NumberTheory/DuffinSchaefferConjectureWanted.lean, line 111](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/DuffinSchaefferConjectureWanted.lean#L111). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/uniform-distribution-metric/duffin-schaeffer-conjecture/index.html#theorem-2-b).

## The convergence exponent $s(\psi)$

For a function $\psi$ from the positive integers to
the nonnegative reals, $s(\psi)$ is the infimum, taken in the nonnegative reals, of the set of
real numbers $\beta \ge 0$ for which the series $\sum_{q \ge 1} \varphi(q) (\psi(q)/q)^{\beta}$
converges, where $\varphi$ is Euler's totient function. If there is no such $\beta$, then
$s(\psi) = 0$.

Formalized by `MathlibExt.NumberTheory.DuffinSchaefferConjectureWanted.DuffinSchaefferConjecture.s_inf`, a definition declared in [WantedExt/NumberTheory/DuffinSchaefferConjectureWanted.lean, line 115](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/DuffinSchaefferConjectureWanted.lean#L115). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/uniform-distribution-metric/duffin-schaeffer-conjecture/index.html#s-inf).

## Koukoulopoulos–Maynard Corollary 3 (Hausdorff dimension of $\mathcal{A}$)

Let $\psi$
be a function from the positive integers to $[0, 1/2]$. Let $\mathcal{A}(\psi)$ be the set of
real numbers $\alpha \in [0, 1]$ for which $|\alpha - a/q| \le \psi(q)/q$ has infinitely many
solutions with $a$ a natural number, $q$ a positive integer and $\gcd(a, q) = 1$. Let $s(\psi)$
be the infimum, taken in the nonnegative reals (where the empty set has infimum $0$), of the
real numbers $\beta \ge 0$ for which the series $\sum_{q \ge 1} \varphi(q) (\psi(q)/q)^{\beta}$
converges, where $\varphi$ is Euler's totient function. Then the Hausdorff dimension of
$\mathcal{A}(\psi)$ equals $\min(s(\psi), 1)$.

## Sources

- D. Koukoulopoulos and J. Maynard, `On the Duffin-Schaeffer conjecture`, Annals of Math, 192 (1) 2020. Statement taken from https://github.com/ImperialCollegeLondon/AnnalsChallenge. Problem `annals_duffin_schaeffer_conjecture` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.NumberTheory.DuffinSchaefferConjectureWanted.DuffinSchaefferConjecture.corollary_3` is written with `theorem_wanted` in [WantedExt/NumberTheory/DuffinSchaefferConjectureWanted.lean, line 125](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/DuffinSchaefferConjectureWanted.lean#L125). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/uniform-distribution-metric/duffin-schaeffer-conjecture/index.html#corollary-3).

## Duffin–Schaeffer conjecture on the unit circle

Let $(\delta_n)_{n \in \mathbb{N}}$ be a
sequence of nonnegative real numbers. Let $W$ be the set of points $x$ of the circle
$\mathbb{R}/\mathbb{Z}$ such that, for infinitely many positive integers $n$, the distance from $x$
to some point of additive order exactly $n$ is less than $\delta_n$. Then $W$ has measure $1$ for
the Haar measure of total mass $1$ on $\mathbb{R}/\mathbb{Z}$ if and only if the series
$\sum_{n} \varphi(n)\,\delta_n$ diverges, where $\varphi$ is Euler's totient function.

The points of additive order exactly $n$ are the reduced fractions $a/n$ modulo $1$.

## Sources

- D. Koukoulopoulos and J. Maynard, 'On the Duffin-Schaeffer conjecture', Ann. of Math. 192 (2020), 251-307, https://doi.org/10.4007/annals.2020.192.1.5. Problem `duffin_schaeffer` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.NumberTheory.DuffinSchaefferWanted.NumberTheory.DuffinSchaeffer.duffin_schaeffer` is written with `theorem_wanted` in [WantedExt/NumberTheory/DuffinSchaefferWanted.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/DuffinSchaefferWanted.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/uniform-distribution-metric/duffin-schaeffer-conjecture/index.html#duffin-schaeffer).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Duffin–Schaeffer conjecture](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/uniform-distribution-metric/duffin-schaeffer-conjecture/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/diophantine-approximation/uniform-distribution-metric/duffin-schaeffer-conjecture)
