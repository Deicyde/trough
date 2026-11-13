---
declaration: section
origin: cited
lean: MetaMathlibExt.overpartitionSpt2Contribution, MetaMathlibExt.overpartitionSpt2, MetaMathlibExt.overpartitionSpt2_zero, MetaMathlibExt.overpartitionSpt2Contribution_eq_zero_of_odd, MetaMathlibExt.overpartitionSpt2_basic_congruences, MetaMathlibExt.overpartitionSpt2_dyadic_congruences, MetaMathlibExt.overpartitionSpt2_prime_congruence, MetaMathlibExt.qPochhammer_two_dissection_square
statement: formalized
---

# Smallest parts in overpartitions

15 results, 4 proved and 11 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/smallest-parts-in-overpartitions/index.html).

## Smallest-even-part contribution of an overpartition

For an overpartition $O$ of $n$,
let $s$ be the smallest part of $O$. The contribution of $O$ is the number of copies of $s$ in
$O$ if $s$ is even and not overlined, and $0$ otherwise; the empty overpartition, which has no
smallest part, contributes $0$.

## Sources

- Robson da Silva, *Extending Congruences for the Number of Smallest Parts in Overpartitions with Smallest Part Even*, INTEGERS 26 (2026), Article A62, Section 1 (definition of `spt2‾(n)`).

Formalized by `MetaMathlibExt.overpartitionSpt2Contribution`, a definition declared in [WantedExt/NumberTheory/OverpartitionSpt2CongruencesWanted.lean, line 35](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/OverpartitionSpt2CongruencesWanted.lean#L35). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/smallest-parts-in-overpartitions/index.html#overpartition-spt2-contribution).

## Number of smallest even parts in overpartitions

For a natural number $n$,
$\overline{\mathrm{spt2}}(n)$ is the number of smallest parts in the overpartitions of $n$ whose
smallest part is even and not overlined: the sum, over all overpartitions $O$ of $n$, of the
smallest-even-part contribution of $O$, which is the number of copies of the smallest part $s$
of $O$ when $s$ is even and not overlined, and $0$ otherwise (in particular when $O$ is empty).
For example $\overline{\mathrm{spt2}}(4) = 3$, from $4$ and $2 + 2$, while $\overline{2} + 2$
does not count; the values for $n = 0, \dots, 8$ are $0, 0, 1, 0, 3, 2, 6, 6, 15$.

## Sources

- Robson da Silva, *Extending Congruences for the Number of Smallest Parts in Overpartitions with Smallest Part Even*, INTEGERS 26 (2026), Article A62, Section 1.

Formalized by `MetaMathlibExt.overpartitionSpt2`, a definition declared in [WantedExt/NumberTheory/OverpartitionSpt2CongruencesWanted.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/OverpartitionSpt2CongruencesWanted.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/smallest-parts-in-overpartitions/index.html#overpartition-spt2).

## $\overline{\mathrm{spt2}}$ vanishes at zero

Let $\overline{\mathrm{spt2}}(n)$ be the
number of smallest parts in the overpartitions of $n$ whose smallest part is even and not
overlined. Then $\overline{\mathrm{spt2}}(0) = 0$: the only overpartition of $0$ is empty and has
no smallest part.

## Sources

- Robson da Silva, *Extending Congruences for the Number of Smallest Parts in Overpartitions with Smallest Part Even*, INTEGERS 26 (2026), Article A62, Section 1.

Formalized by `MetaMathlibExt.overpartitionSpt2_zero`, a theorem declared in [WantedExt/NumberTheory/OverpartitionSpt2CongruencesWanted.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/OverpartitionSpt2CongruencesWanted.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/smallest-parts-in-overpartitions/index.html#overpartition-spt2-zero).

## Overpartitions with odd smallest part contribute nothing

If $O$ is an overpartition of
$n$ with at least one part and the smallest part of $O$ is odd, then the smallest-even-part
contribution of $O$ is $0$.

## Sources

- Robson da Silva, *Extending Congruences for the Number of Smallest Parts in Overpartitions with Smallest Part Even*, INTEGERS 26 (2026), Article A62, Section 1.

Formalized by `MetaMathlibExt.overpartitionSpt2Contribution_eq_zero_of_odd`, a theorem declared in [WantedExt/NumberTheory/OverpartitionSpt2CongruencesWanted.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/OverpartitionSpt2CongruencesWanted.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/smallest-parts-in-overpartitions/index.html#overpartition-spt2-contribution-eq-zero).

## Three congruences modulo 4 for $\overline{\mathrm{spt2}}$

Let $\overline{\mathrm{spt2}}(n)$
be the number of smallest parts in the overpartitions of $n$ whose smallest part is even and not
overlined. For every natural number $n$, each of $\overline{\mathrm{spt2}}(36n + 30)$,
$\overline{\mathrm{spt2}}(48n + 34)$ and $\overline{\mathrm{spt2}}(72n + 42)$ is divisible by $4$.

## Sources

- Robson da Silva, *Extending Congruences for the Number of Smallest Parts in Overpartitions with Smallest Part Even*, INTEGERS 26 (2026), Article A62, Theorem 1.

Stated but not proved: `MetaMathlibExt.overpartitionSpt2_basic_congruences` is written with `theorem_wanted` in [WantedExt/NumberTheory/OverpartitionSpt2CongruencesWanted.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/OverpartitionSpt2CongruencesWanted.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/smallest-parts-in-overpartitions/index.html#overpartition-spt2-basic-congruences).

## Congruences modulo 4 for $\overline{\mathrm{spt2}}$ along powers of 2

Let
$\overline{\mathrm{spt2}}(N)$ be the number of smallest parts in the overpartitions of $N$ whose
smallest part is even and not overlined. For all natural numbers $j$ and $n$,
$\overline{\mathrm{spt2}}(N)$ is divisible by $4$ for each of the six values
$N = 2^{j+4} n + 7 \cdot 2^{j+1}$, $N = 2^{j+2} \cdot 9 n + 15 \cdot 2^{j+1}$,
$N = 2^{j+4} \cdot 3 n + 17 \cdot 2^{j+1}$, $N = 2^{j+3} \cdot 9 n + 21 \cdot 2^{j+1}$,
$N = 2^{j+4} \cdot 5 n + 17 \cdot 2^{j+1}$ and $N = 2^{j+4} \cdot 5 n + 33 \cdot 2^{j+1}$.

## Sources

- Robson da Silva, *Extending Congruences for the Number of Smallest Parts in Overpartitions with Smallest Part Even*, INTEGERS 26 (2026), Article A62, Theorem 2.

Stated but not proved: `MetaMathlibExt.overpartitionSpt2_dyadic_congruences` is written with `theorem_wanted` in [WantedExt/NumberTheory/OverpartitionSpt2CongruencesWanted.lean, line 93](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/OverpartitionSpt2CongruencesWanted.lean#L93). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/smallest-parts-in-overpartitions/index.html#overpartition-spt2-dyadic-congruences).

## Congruences modulo 4 for $\overline{\mathrm{spt2}}$ at primes $p \equiv 5, 7 \pmod 8$

Let
$\overline{\mathrm{spt2}}(N)$ be the number of smallest parts in the overpartitions of $N$ whose
smallest part is even and not overlined. Let $p > 3$ be a prime with $p \equiv 5 \pmod 8$ or
$p \equiv 7 \pmod 8$. Then for all natural numbers $k$ and $m$ with $p \nmid m$, the number
$\overline{\mathrm{spt2}}(32 p^{2k+1} m + 24 p^{2k+2})$ is divisible by $4$.

## Sources

- Robson da Silva, *Extending Congruences for the Number of Smallest Parts in Overpartitions with Smallest Part Even*, INTEGERS 26 (2026), Article A62, Theorem 3.

Stated but not proved: `MetaMathlibExt.overpartitionSpt2_prime_congruence` is written with `theorem_wanted` in [WantedExt/NumberTheory/OverpartitionSpt2CongruencesWanted.lean, line 110](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/OverpartitionSpt2CongruencesWanted.lean#L110). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/smallest-parts-in-overpartitions/index.html#overpartition-spt2-prime-congruence).

## 2-dissection of the square of Euler's product

Let $q$ be a complex number with $|q| < 1$,
and for $k \ge 1$ let $f_k = (q^k; q^k)_\infty = \prod_{n=0}^{\infty} (1 - q^k (q^k)^n)$ be the
raw infinite q-Pochhammer product. Then

$$f_1^2 = \frac{f_2 f_8^5}{f_4^2 f_{16}^2} - 2q \frac{f_2 f_{16}^2}{f_8}.$$

## Sources

- Robson da Silva, *Extending Congruences for the Number of Smallest Parts in Overpartitions with Smallest Part Even*, INTEGERS 26 (2026), Article A62, Lemma 1.

Stated but not proved: `MetaMathlibExt.qPochhammer_two_dissection_square` is written with `theorem_wanted` in [WantedExt/NumberTheory/OverpartitionSpt2CongruencesWanted.lean, line 122](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/OverpartitionSpt2CongruencesWanted.lean#L122). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/smallest-parts-in-overpartitions/index.html#q-pochhammer-two-dissection-square).

## 2-dissection of the reciprocal square of Euler's product

Let $q$ be a complex number with
$|q| < 1$, and for $k \ge 1$ let $f_k = (q^k; q^k)_\infty = \prod_{n=0}^{\infty} (1 - q^k (q^k)^n)$
be the raw infinite q-Pochhammer product. Then

$$\frac{1}{f_1^2} = \frac{f_8^5}{f_2^5 f_{16}^2} + 2q \frac{f_4^2 f_{16}^2}{f_2^5 f_8}.$$

## Sources

- Robson da Silva, *Extending Congruences for the Number of Smallest Parts in Overpartitions with Smallest Part Even*, INTEGERS 26 (2026), Article A62, Lemma 1.

Stated but not proved: `MetaMathlibExt.qPochhammer_two_dissection_inverse_square` is written with `theorem_wanted` in [WantedExt/NumberTheory/OverpartitionSpt2CongruencesWanted.lean, line 139](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/OverpartitionSpt2CongruencesWanted.lean#L139). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/smallest-parts-in-overpartitions/index.html#q-pochhammer-two-dissection-inverse-squa).

## The 3-dissection of $f_1^3$ for complex $q$

Let $q$ be a complex number with $|q| < 1$, and
for $k \ge 1$ let $f_k = (q^k; q^k)_\infty = \prod_{m \ge 1} (1 - q^{km})$ be the raw infinite
q-Pochhammer product with $a = q^k$ and base $q^k$. Then

$$
f_1^3 = \frac{f_6 f_9^6}{f_3 f_{18}^3} + 4 q^3 \frac{f_3^2 f_{18}^6}{f_6^2 f_9^3} - 3 q f_9^3.
$$

## Sources

- Robson da Silva, *Extending Congruences for the Number of Smallest Parts in Overpartitions with Smallest Part Even*, INTEGERS 26 (2026), Article A62, Lemma 2.

Stated but not proved: `MetaMathlibExt.qPochhammer_three_dissection_cube` is written with `theorem_wanted` in [WantedExt/NumberTheory/OverpartitionSpt2CongruencesWanted.lean, line 156](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/OverpartitionSpt2CongruencesWanted.lean#L156). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/smallest-parts-in-overpartitions/index.html#q-pochhammer-three-dissection-cube).

## The 3-dissection of $f_4/f_1$ for complex $q$

Let $q$ be a complex number with $|q| < 1$,
and for $k \ge 1$ let $f_k = (q^k; q^k)_\infty = \prod_{m \ge 1} (1 - q^{km})$ be the raw
infinite q-Pochhammer product with $a = q^k$ and base $q^k$. Then

$$
\frac{f_4}{f_1} = \frac{f_{12} f_{18}^4}{f_3^3 f_{36}^2} +
q \frac{f_6^2 f_9^3 f_{36}}{f_3^4 f_{18}^2} + 2 q^2 \frac{f_6 f_{18} f_{36}}{f_3^3}.
$$

## Sources

- Robson da Silva, *Extending Congruences for the Number of Smallest Parts in Overpartitions with Smallest Part Even*, INTEGERS 26 (2026), Article A62, Lemma 2.

Stated but not proved: `MetaMathlibExt.qPochhammer_three_dissection_ratio_four_one` is written with `theorem_wanted` in [WantedExt/NumberTheory/OverpartitionSpt2CongruencesWanted.lean, line 176](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/OverpartitionSpt2CongruencesWanted.lean#L176). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/smallest-parts-in-overpartitions/index.html#q-pochhammer-three-dissection-ratio-four).

## The 3-dissection of $f_1 f_2$ for complex $q$

Let $q$ be a complex number with $|q| < 1$,
and for $k \ge 1$ let $f_k = (q^k; q^k)_\infty = \prod_{m \ge 1} (1 - q^{km})$ be the raw
infinite q-Pochhammer product with $a = q^k$ and base $q^k$. Then

$$
f_1 f_2 = \frac{f_6 f_9^4}{f_3 f_{18}^2} - q f_9 f_{18} - 2 q^2 \frac{f_3 f_{18}^4}{f_6 f_9^2}.
$$

## Sources

- Robson da Silva, *Extending Congruences for the Number of Smallest Parts in Overpartitions with Smallest Part Even*, INTEGERS 26 (2026), Article A62, Lemma 2.

Stated but not proved: `MetaMathlibExt.qPochhammer_three_dissection_product_one_two` is written with `theorem_wanted` in [WantedExt/NumberTheory/OverpartitionSpt2CongruencesWanted.lean, line 199](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/OverpartitionSpt2CongruencesWanted.lean#L199). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/smallest-parts-in-overpartitions/index.html#q-pochhammer-three-dissection-product-on).

## 3-dissection of the product form of Ramanujan's psi function

Let $q$ be a complex number
with $|q| < 1$, and for $k \ge 1$ let
$f_k = (q^k; q^k)_\infty = \prod_{n=0}^{\infty} (1 - q^k (q^k)^n)$ be the raw infinite
q-Pochhammer product. Then

$$\frac{f_2^2}{f_1} = \frac{f_6 f_9^2}{f_3 f_{18}} + q \frac{f_{18}^2}{f_9}.$$

Here $f_2^2/f_1$ is the product form of Ramanujan's theta function
$\psi(q) = \sum_{n \ge 0} q^{n(n+1)/2}$.

## Sources

- Robson da Silva, *Extending Congruences for the Number of Smallest Parts in Overpartitions with Smallest Part Even*, INTEGERS 26 (2026), Article A62, Lemma 3.

Stated but not proved: `MetaMathlibExt.ramanujanPsi_three_dissection` is written with `theorem_wanted` in [WantedExt/NumberTheory/OverpartitionSpt2CongruencesWanted.lean, line 220](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/OverpartitionSpt2CongruencesWanted.lean#L220). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/smallest-parts-in-overpartitions/index.html#ramanujan-psi-three-dissection).

## 3-dissection of the product form of Ramanujan's psi function at negated argument

Let $q$ be
a complex number with $|q| < 1$, and for $k \ge 1$ let
$f_k = (q^k; q^k)_\infty = \prod_{n=0}^{\infty} (1 - q^k (q^k)^n)$ be the raw infinite
q-Pochhammer product. Then

$$\frac{f_1 f_4}{f_2} = \frac{f_3 f_{12} f_{18}^5}{f_6^2 f_9^2 f_{36}^2} -
q \frac{f_9 f_{36}}{f_{18}}.$$

Here $f_1 f_4/f_2$ is the product form of $\psi(-q)$, where
$\psi(q) = \sum_{n \ge 0} q^{n(n+1)/2}$ is Ramanujan's theta function.

## Sources

- Robson da Silva, *Extending Congruences for the Number of Smallest Parts in Overpartitions with Smallest Part Even*, INTEGERS 26 (2026), Article A62, Lemma 4.

Stated but not proved: `MetaMathlibExt.ramanujanPsi_neg_dissection` is written with `theorem_wanted` in [WantedExt/NumberTheory/OverpartitionSpt2CongruencesWanted.lean, line 237](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/OverpartitionSpt2CongruencesWanted.lean#L237). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/smallest-parts-in-overpartitions/index.html#ramanujan-psi-neg-dissection).

## 3-dissection of the product form of Ramanujan's phi function at negated argument

Let $q$ be
a complex number with $|q| < 1$, and for $k \ge 1$ let
$f_k = (q^k; q^k)_\infty = \prod_{n=0}^{\infty} (1 - q^k (q^k)^n)$ be the raw infinite
q-Pochhammer product. Then

$$\frac{f_1^2}{f_2} = \frac{f_9^2}{f_{18}} - 2q \frac{f_3 f_{18}^2}{f_6 f_9}.$$

Here $f_1^2/f_2$ is the product form of $\varphi(-q)$, where
$\varphi(q) = \sum_{n \in \mathbb{Z}} q^{n^2}$ is Ramanujan's theta function.

## Sources

- Robson da Silva, *Extending Congruences for the Number of Smallest Parts in Overpartitions with Smallest Part Even*, INTEGERS 26 (2026), Article A62, Lemma 5.

Stated but not proved: `MetaMathlibExt.ramanujanPhi_neg_dissection` is written with `theorem_wanted` in [WantedExt/NumberTheory/OverpartitionSpt2CongruencesWanted.lean, line 257](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/OverpartitionSpt2CongruencesWanted.lean#L257). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/smallest-parts-in-overpartitions/index.html#ramanujan-phi-neg-dissection).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Smallest parts in overpartitions](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/smallest-parts-in-overpartitions/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/smallest-parts-in-overpartitions)
