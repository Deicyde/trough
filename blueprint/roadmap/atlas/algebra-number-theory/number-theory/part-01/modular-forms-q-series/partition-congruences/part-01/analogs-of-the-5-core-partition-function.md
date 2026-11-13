---
declaration: section
origin: cited
lean: MetaMathlibExt.ramanujanThetaPow, MetaMathlibExt.fiveCoreCount, MetaMathlibExt.phiFiveCoreAnalog, MetaMathlibExt.psiFiveCoreAnalog, MetaMathlibExt.constantCoeff_ramanujanThetaPow, MetaMathlibExt.mk_fiveCoreCount_mul, MetaMathlibExt.mk_phiFiveCoreAnalog_mul, MetaMathlibExt.mk_psiFiveCoreAnalog_mul
statement: formalized
---

# Analogs of the 5-core partition function

20 results, 8 proved and 12 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/analogs-of-the-5-core-partition-function/index.html).

## Ramanujan's general theta function at powers of q

For positive integers $i$ and $j$,
$f(q^i, q^j)$ is the integer power series $\sum_{n \in \mathbb{Z}} q^{i n(n+1)/2 + j n(n-1)/2}$,
that is, Ramanujan's $f(a, b) = \sum_{n \in \mathbb{Z}} a^{n(n+1)/2} b^{n(n-1)/2}$ at $a = q^i$
and $b = q^j$.

Since $i, j \ge 1$, only integers $n$ with $|n| \le m$ contribute to the coefficient of $q^m$, so
each coefficient is a finite count.

## Sources

- Subhajit Bandyopadhyay and Nayandeep Deka Baruah, *Arithmetic Identities for Some Analogs of the 5-Core Partition Function*, Journal of Integer Sequences 27 (2024), Article 24.4.5, Section 1 (definition of `f(a, b)`).

Formalized by `MetaMathlibExt.ramanujanThetaPow`, a definition declared in [WantedExt/Combinatorics/Enumerative/Partition/FiveCoreAnalogsWanted.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/Partition/FiveCoreAnalogsWanted.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/analogs-of-the-5-core-partition-function/index.html#ramanujan-theta-pow).

## The 5-core counts

For a natural number $n$, $c_5(n)$ is the coefficient of $q^n$ in the
integer power series $f_5^5 / f_1$, where $f_k = \prod_{m \ge 1} (1 - q^{km})$ is the Euler
product. The series $f_5^5 / f_1$ is the generating function of 5-core partitions.

## Sources

- Subhajit Bandyopadhyay and Nayandeep Deka Baruah, *Arithmetic Identities for Some Analogs of the 5-Core Partition Function*, Journal of Integer Sequences 27 (2024), Article 24.4.5, Section 1, equation for `∑ c_t(n) q^n` with `t = 5` (OEIS A053723).

Formalized by `MetaMathlibExt.fiveCoreCount`, a definition declared in [WantedExt/Combinatorics/Enumerative/Partition/FiveCoreAnalogsWanted.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/Partition/FiveCoreAnalogsWanted.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/analogs-of-the-5-core-partition-function/index.html#five-core-count).

## The φ-analog of the 5-core partition function

Let
$\varphi(q) = \sum_{n \in \mathbb{Z}} q^{n^2}$ be Ramanujan's theta function. For a natural
number $n$, $\bar a_5(n)$ is the coefficient of $q^n$ in the integer power series
$\varphi^5(-q^5)/\varphi(-q)$ (the denominator has constant term $1$, so the quotient is a power
series).

## Sources

- Subhajit Bandyopadhyay and Nayandeep Deka Baruah, *Arithmetic Identities for Some Analogs of the 5-Core Partition Function*, Journal of Integer Sequences 27 (2024), Article 24.4.5, Section 1, equation (at) (OEIS A368490).

Formalized by `MetaMathlibExt.phiFiveCoreAnalog`, a definition declared in [WantedExt/Combinatorics/Enumerative/Partition/FiveCoreAnalogsWanted.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/Partition/FiveCoreAnalogsWanted.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/analogs-of-the-5-core-partition-function/index.html#phi-five-core-analog).

## The ψ-analog of the 5-core partition function

Let
$\psi(q) = \sum_{n \in \mathbb{Z}} q^{2n^2 - n} = \sum_{n \ge 0} q^{n(n+1)/2}$ be Ramanujan's theta
function. For a natural number $n$, $\bar b_5(n)$ is the coefficient of $q^n$ in the integer
power series $\psi^5(-q^5)/\psi(-q)$ (the denominator has constant term $1$, so the quotient is
a power series).

## Sources

- Subhajit Bandyopadhyay and Nayandeep Deka Baruah, *Arithmetic Identities for Some Analogs of the 5-Core Partition Function*, Journal of Integer Sequences 27 (2024), Article 24.4.5, Section 1, equation (bt) (OEIS A368495).

Formalized by `MetaMathlibExt.psiFiveCoreAnalog`, a definition declared in [WantedExt/Combinatorics/Enumerative/Partition/FiveCoreAnalogsWanted.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/Partition/FiveCoreAnalogsWanted.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/analogs-of-the-5-core-partition-function/index.html#psi-five-core-analog).

## Constant term of Ramanujan's theta function

For all positive integers $i$ and $j$, the
integer power series $f(q^i, q^j) = \sum_{n \in \mathbb{Z}} q^{i n(n+1)/2 + j n(n-1)/2}$ has
constant term $1$: only $n = 0$ contributes to $q^0$.

## Sources

- Subhajit Bandyopadhyay and Nayandeep Deka Baruah, *Arithmetic Identities for Some Analogs of the 5-Core Partition Function*, Journal of Integer Sequences 27 (2024), Article 24.4.5, Section 1.

Formalized by `MetaMathlibExt.constantCoeff_ramanujanThetaPow`, a theorem declared in [WantedExt/Combinatorics/Enumerative/Partition/FiveCoreAnalogsWanted.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/Partition/FiveCoreAnalogsWanted.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/analogs-of-the-5-core-partition-function/index.html#constant-coeff-ramanujan-theta-pow).

## Generating function of the 5-core counts

Let $f_k = \prod_{m \ge 1} (1 - q^{km})$ and
let $c_5(n)$ be the coefficient of $q^n$ in $f_5^5 / f_1$. Then, as integer power series,
$\left(\sum_{n \ge 0} c_5(n) q^n\right) f_1 = f_5^5$, where $f_1$ is written as the pentagonal
series $\sum_{j \in \mathbb{Z}} (-1)^j q^{j(3j-1)/2}$.

## Sources

- Subhajit Bandyopadhyay and Nayandeep Deka Baruah, *Arithmetic Identities for Some Analogs of the 5-Core Partition Function*, Journal of Integer Sequences 27 (2024), Article 24.4.5, Section 1.

Formalized by `MetaMathlibExt.mk_fiveCoreCount_mul`, a theorem declared in [WantedExt/Combinatorics/Enumerative/Partition/FiveCoreAnalogsWanted.lean, line 93](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/Partition/FiveCoreAnalogsWanted.lean#L93). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/analogs-of-the-5-core-partition-function/index.html#mk-five-core-count-mul).

## Generating function of the $\varphi$-analog of the 5-core counts

Let
$\varphi(q) = \sum_{n \in \mathbb{Z}} q^{n^2}$ and let $\bar a_5(n)$ be the coefficient of $q^n$
in $\varphi(-q^5)^5 / \varphi(-q)$. Then, as integer power series,
$\left(\sum_{n \ge 0} \bar a_5(n) q^n\right) \varphi(-q) = \varphi(-q^5)^5$.

## Sources

- Subhajit Bandyopadhyay and Nayandeep Deka Baruah, *Arithmetic Identities for Some Analogs of the 5-Core Partition Function*, Journal of Integer Sequences 27 (2024), Article 24.4.5, Section 1, equation (at).

Formalized by `MetaMathlibExt.mk_phiFiveCoreAnalog_mul`, a theorem declared in [WantedExt/Combinatorics/Enumerative/Partition/FiveCoreAnalogsWanted.lean, line 107](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/Partition/FiveCoreAnalogsWanted.lean#L107). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/analogs-of-the-5-core-partition-function/index.html#mk-phi-five-core-analog-mul).

## Generating function of the $\psi$-analog of the 5-core counts

Let
$\psi(q) = \sum_{n \in \mathbb{Z}} q^{n(2n-1)}$ and let $\bar b_5(n)$ be the coefficient of $q^n$
in $\psi(-q^5)^5 / \psi(-q)$. Then, as integer power series,
$\left(\sum_{n \ge 0} \bar b_5(n) q^n\right) \psi(-q) = \psi(-q^5)^5$.

## Sources

- Subhajit Bandyopadhyay and Nayandeep Deka Baruah, *Arithmetic Identities for Some Analogs of the 5-Core Partition Function*, Journal of Integer Sequences 27 (2024), Article 24.4.5, Section 1, equation (bt).

Formalized by `MetaMathlibExt.mk_psiFiveCoreAnalog_mul`, a theorem declared in [WantedExt/Combinatorics/Enumerative/Partition/FiveCoreAnalogsWanted.lean, line 125](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/Partition/FiveCoreAnalogsWanted.lean#L125). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/analogs-of-the-5-core-partition-function/index.html#mk-psi-five-core-analog-mul).

## The $\varphi$-analog of the 5-core counts in terms of the 5-core counts

Let
$f_k = \prod_{m \ge 1} (1 - q^{km})$, let $c_5(n)$ be the coefficient of $q^n$ in $f_5^5 / f_1$,
let $\varphi(q) = \sum_{n \in \mathbb{Z}} q^{n^2}$ and let $\bar a_5(n)$ be the coefficient of
$q^n$ in $\varphi(-q^5)^5 / \varphi(-q)$. For every natural number $n$,
$\bar a_5(5n+2) = 4\, c_5(5n+1)$, $\bar a_5(5n+3) = 4\, c_5(5n+2)$,
$\bar a_5(10n+1) = 2\, c_5(10n)$, $\bar a_5(10n+9) = 2\, c_5(10n+8)$,
$\bar a_5(20n+6) = 10\, c_5(10n+2)$ and $\bar a_5(20n+14) = 10\, c_5(10n+6)$.

## Sources

- Subhajit Bandyopadhyay and Nayandeep Deka Baruah, *Arithmetic Identities for Some Analogs of the 5-Core Partition Function*, Journal of Integer Sequences 27 (2024), Article 24.4.5, Theorem 2 (`jis-2024-24.4.5-thm-2`).

Stated but not proved: `MetaMathlibExt.phiFiveCoreAnalog_eq_fiveCoreCount` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/FiveCoreAnalogsWanted.lean, line 150](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/Partition/FiveCoreAnalogsWanted.lean#L150). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/analogs-of-the-5-core-partition-function/index.html#phi-five-core-analog-eq-five-core-count).

## Recurrence for the $\varphi$-analog of the 5-core counts along powers of 5

Let
$\varphi(q) = \sum_{n \in \mathbb{Z}} q^{n^2}$ and let $\bar a_5(n)$ be the coefficient of $q^n$
in $\varphi(-q^5)^5 / \varphi(-q)$. For every natural number $k \ge 2$ and every natural number
$n$, $\bar a_5(5^k n) = \frac{5^k - 1}{4}\, \bar a_5(5n) - \frac{5^k - 5}{4}\, \bar a_5(n)$.
Both quotients are integers.

## Sources

- Subhajit Bandyopadhyay and Nayandeep Deka Baruah, *Arithmetic Identities for Some Analogs of the 5-Core Partition Function*, Journal of Integer Sequences 27 (2024), Article 24.4.5, Theorem 2 (`jis-2024-24.4.5-thm-2`).

Stated but not proved: `MetaMathlibExt.phiFiveCoreAnalog_five_pow_mul` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/FiveCoreAnalogsWanted.lean, line 164](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/Partition/FiveCoreAnalogsWanted.lean#L164). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/analogs-of-the-5-core-partition-function/index.html#phi-five-core-analog-five-pow-mul).

## Congruences for the $\varphi$-analog of the 5-core counts

Let
$\varphi(q) = \sum_{n \in \mathbb{Z}} q^{n^2}$ and let $\bar a_5(n)$ be the coefficient of $q^n$
in $\varphi(-q^5)^5 / \varphi(-q)$. For every natural number $k \ge 2$ and every natural number
$n$, $\bar a_5(20n+6) \equiv 0 \pmod{10}$, $\bar a_5(20n+14) \equiv 0 \pmod{10}$ and
$4\, \bar a_5(5^k n) \equiv 5\, \bar a_5(n) - \bar a_5(5n) \pmod{5^k}$.

## Sources

- Subhajit Bandyopadhyay and Nayandeep Deka Baruah, *Arithmetic Identities for Some Analogs of the 5-Core Partition Function*, Journal of Integer Sequences 27 (2024), Article 24.4.5, Corollary 3 (`jis-2024-24.4.5-cor-3`).

Stated but not proved: `MetaMathlibExt.phiFiveCoreAnalog_congruences` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/FiveCoreAnalogsWanted.lean, line 175](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/Partition/FiveCoreAnalogsWanted.lean#L175). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/analogs-of-the-5-core-partition-function/index.html#phi-five-core-analog-congruences).

## A doubling identity for the ψ-analog of the 5-core partition function

Let
$\bar b_5(n)$ be the coefficient of $q^n$ in $\psi^5(-q^5)/\psi(-q)$, where
$\psi(q) = \sum_{n \ge 0} q^{n(n+1)/2}$. For every natural number $n$,
$\bar b_5(4n+3) = 2 \bar b_5(2n)$.

## Sources

- Subhajit Bandyopadhyay and Nayandeep Deka Baruah, *Arithmetic Identities for Some Analogs of the 5-Core Partition Function*, Journal of Integer Sequences 27 (2024), Article 24.4.5, Theorem 4 (`jis-2024-24.4.5-thm-4`).

Stated but not proved: `MetaMathlibExt.psiFiveCoreAnalog_four_mul_add_three` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/FiveCoreAnalogsWanted.lean, line 186](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/Partition/FiveCoreAnalogsWanted.lean#L186). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/analogs-of-the-5-core-partition-function/index.html#psi-five-core-analog-four-mul-add-three).

## A recurrence for the ψ-analog of the 5-core partition function along powers of 5

Let
$\bar b_5(n)$ be the coefficient of $q^n$ in $\psi^5(-q^5)/\psi(-q)$, where
$\psi(q) = \sum_{n \ge 0} q^{n(n+1)/2}$. For every integer $k \ge 2$ and every natural number
$n$, $\bar b_5(5^k(n+3) - 3) = \frac{5^k - 1}{4} \bar b_5(5n+12) - \frac{5^k - 5}{4} \bar b_5(n)$;
both quotients are integers.

## Sources

- Subhajit Bandyopadhyay and Nayandeep Deka Baruah, *Arithmetic Identities for Some Analogs of the 5-Core Partition Function*, Journal of Integer Sequences 27 (2024), Article 24.4.5, Theorem 4 (`jis-2024-24.4.5-thm-4`).

Stated but not proved: `MetaMathlibExt.psiFiveCoreAnalog_five_pow_mul` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/FiveCoreAnalogsWanted.lean, line 195](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/Partition/FiveCoreAnalogsWanted.lean#L195). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/analogs-of-the-5-core-partition-function/index.html#psi-five-core-analog-five-pow-mul).

## Identities relating the ψ-analog to the 5-core counts and the φ-analog

Let
$f_k = \prod_{m \ge 1} (1 - q^{km})$, $\varphi(q) = \sum_{n \in \mathbb{Z}} q^{n^2}$ and
$\psi(q) = \sum_{n \ge 0} q^{n(n+1)/2}$, and let $c_5(n)$, $\bar a_5(n)$ and $\bar b_5(n)$ be the
coefficients of $q^n$ in $f_5^5/f_1$, $\varphi^5(-q^5)/\varphi(-q)$ and $\psi^5(-q^5)/\psi(-q)$.
Then for every natural number $n$:
$\bar b_5(4n+1) = c_5(n) - 2 \bar b_5(2n-1)$, where the last term is read as $0$ for $n = 0$;
$2 \bar b_5(10n) = c_5(10n+2)$; $\bar b_5(10n+1) = c_5(5n+1)$;
$4 \bar b_5(10n+2) = \bar a_5(2n+1) + 2 c_5(2n)$; $\bar b_5(10n+3) = c_5(5n+2)$;
$2 \bar b_5(10n+4) = c_5(10n+6)$; $\bar b_5(10n+6) = \bar b_5(10n+8) = 0$;
$\bar b_5(20n+5) = -c_5(5n+1)$; $2 \bar b_5(20n+7) = \bar a_5(2n+1) + 2 c_5(2n)$;
$\bar b_5(20n+9) = -c_5(5n+2)$; and $\bar b_5(20n+15) = \bar b_5(20n+19) = 0$.

## Sources

- Subhajit Bandyopadhyay and Nayandeep Deka Baruah, *Arithmetic Identities for Some Analogs of the 5-Core Partition Function*, Journal of Integer Sequences 27 (2024), Article 24.4.5, Theorem 5 (`jis-2024-24.4.5-thm-5`).

Stated but not proved: `MetaMathlibExt.psiFiveCoreAnalog_identities` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/FiveCoreAnalogsWanted.lean, line 206](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/Partition/FiveCoreAnalogsWanted.lean#L206). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/analogs-of-the-5-core-partition-function/index.html#psi-five-core-analog-identities).

## Sign densities of the ψ-analog of the 5-core partition function

Let
$\bar b_5(n)$ be the coefficient of $q^n$ in $\psi^5(-q^5)/\psi(-q)$, where
$\psi(q) = \sum_{n \ge 0} q^{n(n+1)/2}$, and let the lower density of a set $S$ of natural numbers
be $\liminf_{N \to \infty} |S \cap \{0, \dots, N - 1\}|/N$. The set of positive integers $n$ with
$\bar b_5(n) = 0$ has lower density at least $3/10$, the set of positive $n$ with
$\bar b_5(n) > 0$ has lower density at least $52/100$, and the set of positive $n$ with
$\bar b_5(n) < 0$ has lower density at least $1/10$.

## Sources

- Subhajit Bandyopadhyay and Nayandeep Deka Baruah, *Arithmetic Identities for Some Analogs of the 5-Core Partition Function*, Journal of Integer Sequences 27 (2024), Article 24.4.5, Corollary 6 (`jis-2024-24.4.5-cor-6`).

Stated but not proved: `MetaMathlibExt.psiFiveCoreAnalog_sign_densities` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/FiveCoreAnalogsWanted.lean, line 231](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/Partition/FiveCoreAnalogsWanted.lean#L231). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/analogs-of-the-5-core-partition-function/index.html#psi-five-core-analog-sign-densities).

## The $\varphi$-analog in terms of the $\psi$-analog of the 5-core counts

Let
$\varphi(q) = \sum_{n \in \mathbb{Z}} q^{n^2}$ and $\psi(q) = \sum_{n \in \mathbb{Z}} q^{n(2n-1)}$,
and let $\bar a_5(n)$ and $\bar b_5(n)$ be the coefficients of $q^n$ in
$\varphi(-q^5)^5 / \varphi(-q)$ and $\psi(-q^5)^5 / \psi(-q)$ respectively. For every natural
number $n$, $\bar a_5(20n+6) = 20\, \bar b_5(10n)$ and
$\bar a_5(20n+14) = 20\, \bar b_5(10n+4)$.

## Sources

- Subhajit Bandyopadhyay and Nayandeep Deka Baruah, *Arithmetic Identities for Some Analogs of the 5-Core Partition Function*, Journal of Integer Sequences 27 (2024), Article 24.4.5, Corollary 7 (`jis-2024-24.4.5-cor-7`).

Stated but not proved: `MetaMathlibExt.phiFiveCoreAnalog_eq_twenty_mul_psiFiveCoreAnalog` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/FiveCoreAnalogsWanted.lean, line 241](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/Partition/FiveCoreAnalogsWanted.lean#L241). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/analogs-of-the-5-core-partition-function/index.html#phi-five-core-analog-eq-twenty-mul-psi-f).

## Congruences for the ψ-analog of the 5-core partition function

Let
$\bar b_5(n)$ be the coefficient of $q^n$ in $\psi^5(-q^5)/\psi(-q)$, where
$\psi(q) = \sum_{n \ge 0} q^{n(n+1)/2}$. For every integer $k \ge 2$ and every natural number
$n$, $4 \bar b_5(5^k(n+3) - 3) \equiv 5 \bar b_5(n) - \bar b_5(5n+12) \pmod{5^k}$, and both
$\bar b_5(5^k(20n+18) - 3)$ and $\bar b_5(5^k(20n+22) - 3)$ are divisible by $(5^k - 1)/4$.

## Sources

- Subhajit Bandyopadhyay and Nayandeep Deka Baruah, *Arithmetic Identities for Some Analogs of the 5-Core Partition Function*, Journal of Integer Sequences 27 (2024), Article 24.4.5, Corollary 8 (`jis-2024-24.4.5-cor-8`).

Stated but not proved: `MetaMathlibExt.psiFiveCoreAnalog_congruences` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/FiveCoreAnalogsWanted.lean, line 251](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/Partition/FiveCoreAnalogsWanted.lean#L251). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/analogs-of-the-5-core-partition-function/index.html#psi-five-core-analog-congruences).

## Theta-function identities of level 5

Let $f_k = \prod_{m \ge 1} (1 - q^{km})$,
$f(q) = \prod_{m \ge 1} (1 - (-q)^m)$ (so that $f(-q) = f_1$),
$\chi(-q) = \prod_{m \ge 0} (1 - q^{2m+1})$ and $\chi(q) = \prod_{m \ge 0} (1 + q^{2m+1})$. Let
$f(a, b) = \sum_{n \in \mathbb{Z}} a^{n(n+1)/2} b^{n(n-1)/2}$ be Ramanujan's general theta
function, $\varphi(q) = f(q, q)$ and $\psi(q) = f(q, q^3)$. Then, as integer power series in
$q$ (every denominator below has constant term $1$):
$\varphi^5(q^5)/\varphi(q) + 4q f^5(q^5)/f(q) = \varphi(q) \varphi^3(q^5)$;
$\varphi^2(q) - \varphi^2(q^5) = 4q \chi(q) f_5 f_{20}$;
$\psi^5(-q^5)/\psi(-q) - \psi^5(q^5)/\psi(q) = 4q^3 \psi^5(q^{10})/\psi(q^2) + 2q f_{20}^5/f_4$;
$\psi^2(q) - q \psi^2(q^5) = f_5 \varphi(-q^5)/\chi(-q) = f(q, q^4) f(q^2, q^3)$;
$f_5^5/f_1 - 4q^3 f_{20}^5/f_4 = f^5(q^5)/f(q) + 2q f_{10}^5/f_2$; and
$f_2^2/f_1^4 = f_{10}^2/f_5^4 + 4q f_2 f_{10}^5/(f_1^3 f_5^5)$.

## Sources

- Subhajit Bandyopadhyay and Nayandeep Deka Baruah, *Arithmetic Identities for Some Analogs of the 5-Core Partition Function*, Journal of Integer Sequences 27 (2024), Article 24.4.5, Lemma 9 (`jis-2024-24.4.5-lem-9`).

Stated but not proved: `MetaMathlibExt.theta_level_five_identities` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/FiveCoreAnalogsWanted.lean, line 268](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/Partition/FiveCoreAnalogsWanted.lean#L268). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/analogs-of-the-5-core-partition-function/index.html#theta-level-five-identities).

## 5-dissections of Ramanujan's theta functions φ and ψ

Let
$f(a, b) = \sum_{n \in \mathbb{Z}} a^{n(n+1)/2} b^{n(n-1)/2}$ be Ramanujan's general theta
function, $\varphi(q) = f(q, q)$ and $\psi(q) = f(q, q^3)$. As integer power series in $q$,
$\varphi(q) = \varphi(q^{25}) + 2q f(q^{15}, q^{35}) + 2q^4 f(q^5, q^{45})$ and
$\psi(q) = f(q^{10}, q^{15}) + q f(q^5, q^{20}) + q^3 \psi(q^{25})$.

Lemma 10 of the source also gives a 5-dissection of $\prod_{m \ge 1} (1 - q^m)^{-1}$ via the
Rogers–Ramanujan continued fraction; that part is not included.

## Sources

- Subhajit Bandyopadhyay and Nayandeep Deka Baruah, *Arithmetic Identities for Some Analogs of the 5-Core Partition Function*, Journal of Integer Sequences 27 (2024), Article 24.4.5, Lemma 10 (`jis-2024-24.4.5-lem-10`).

Stated but not proved: `MetaMathlibExt.theta_five_dissections` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/FiveCoreAnalogsWanted.lean, line 295](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/Partition/FiveCoreAnalogsWanted.lean#L295). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/analogs-of-the-5-core-partition-function/index.html#theta-five-dissections).

## Two identities for the 5-core counts

Let $f_k = \prod_{m \ge 1} (1 - q^{km})$ and let
$c_5(n)$ be the coefficient of $q^n$ in $f_5^5 / f_1$. For every natural number $n$,
$c_5(4n+1) = c_5(2n)$ and $c_5(5n+4) = 5\, c_5(n)$.

## Sources

- Subhajit Bandyopadhyay and Nayandeep Deka Baruah, *Arithmetic Identities for Some Analogs of the 5-Core Partition Function*, Journal of Integer Sequences 27 (2024), Article 24.4.5, Lemma 11 (`jis-2024-24.4.5-lem-11`).

Stated but not proved: `MetaMathlibExt.fiveCoreCount_identities` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/FiveCoreAnalogsWanted.lean, line 305](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/Partition/FiveCoreAnalogsWanted.lean#L305). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/analogs-of-the-5-core-partition-function/index.html#five-core-count-identities).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Analogs of the 5-core partition function](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/analogs-of-the-5-core-partition-function/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/analogs-of-the-5-core-partition-function)
