---
declaration: section
origin: cited
lean: MetaMathlibExt.pattern3, MetaMathlibExt.twoPatternAvoiderCount, MetaMathlibExt.twoPatternAvoiderCount_three_123_132, MetaMathlibExt.twoPatternAvoiderCount_four_132_321, MetaMathlibExt.twoPatternAvoiderCount_length_three, MetaMathlibExt.permAscents, MetaMathlibExt.permDescents, MetaMathlibExt.permAscents_permDescents_small
statement: formalized
---

# Permutations avoiding two patterns of length three

20 results, 12 proved and 8 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/permutations-avoiding-two-patterns-of-length-thr/index.html).

## Length-three pattern from one-line values

Given a bijection $v$ from $\{0, 1, 2\}$ to
itself, this is the permutation of $\{0, 1, 2\}$ that sends $i$ to $v(i)$. The values are listed
zero-based, so $v = (0, 2, 1)$ gives the pattern $132$ in the usual one-based one-line notation.

## Sources

- Han, *Joint Distributions of 10 Classical Statistics over Permutations Avoiding Two Patterns of Length 3*, INTEGERS 26 (2026), Article A18, Section 1.

Formalized by `MetaMathlibExt.pattern3`, a definition declared in [WantedExt/Combinatorics/Enumerative/TwoPatternAvoidanceCountsWanted.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/TwoPatternAvoidanceCountsWanted.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/permutations-avoiding-two-patterns-of-length-thr/index.html#pattern3).

## Number of permutations avoiding two patterns of length three

For a natural number $n$
and permutations $\tau$ and $\rho$ of $\{0, 1, 2\}$, $A_n(\tau, \rho)$ is the number of
permutations of $\{0, 1, \dots, n - 1\}$ that contain neither $\tau$ nor $\rho$ as a classical
pattern.

## Sources

- Han, *Joint Distributions of 10 Classical Statistics over Permutations Avoiding Two Patterns of Length 3*, INTEGERS 26 (2026), Article A18, Theorem 1.

Formalized by `MetaMathlibExt.twoPatternAvoiderCount`, a definition declared in [WantedExt/Combinatorics/Enumerative/TwoPatternAvoidanceCountsWanted.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/TwoPatternAvoidanceCountsWanted.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/permutations-avoiding-two-patterns-of-length-thr/index.html#two-pattern-avoider-count).

## Permutations of length three avoiding $123$ and $132$

Exactly $4$ permutations of
$\{0, 1, 2\}$ avoid both patterns $123$ and $132$, that is, $A_3(123, 132) = 4$: of the six
permutations of length $3$, only $123$ and $132$ themselves are excluded.

## Sources

- Han, *Joint Distributions of 10 Classical Statistics over Permutations Avoiding Two Patterns of Length 3*, INTEGERS 26 (2026), Article A18, Theorem 1.

Formalized by `MetaMathlibExt.twoPatternAvoiderCount_three_123_132`, a theorem declared in [WantedExt/Combinatorics/Enumerative/TwoPatternAvoidanceCountsWanted.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/TwoPatternAvoidanceCountsWanted.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/permutations-avoiding-two-patterns-of-length-thr/index.html#two-pattern-avoider-count-three-123-132).

## Permutations of length four avoiding $132$ and $321$

Exactly $7$ permutations of
$\{0, 1, 2, 3\}$ avoid both patterns $132$ and $321$, that is,
$A_4(132, 321) = 7 = 1 + \binom{4}{2}$.

## Sources

- Han, *Joint Distributions of 10 Classical Statistics over Permutations Avoiding Two Patterns of Length 3*, INTEGERS 26 (2026), Article A18, Theorem 1.

Formalized by `MetaMathlibExt.twoPatternAvoiderCount_four_132_321`, a theorem declared in [WantedExt/Combinatorics/Enumerative/TwoPatternAvoidanceCountsWanted.lean, line 87](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/TwoPatternAvoidanceCountsWanted.lean#L87). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/permutations-avoiding-two-patterns-of-length-thr/index.html#two-pattern-avoider-count-four-132-321).

## Simion–Schmidt enumeration of permutations avoiding two patterns of length three

For
every $n \ge 1$, writing $A_n(\tau, \rho)$ for the number of permutations of
$\{0, 1, \dots, n - 1\}$ avoiding both patterns $\tau$ and $\rho$:
(a) $A_n(123, 132) = A_n(123, 213) = A_n(321, 231) = A_n(321, 312) = 2^{n-1}$;
(b) $A_n(231, 312) = A_n(132, 213) = 2^{n-1}$;
(c) $A_n(213, 312) = A_n(132, 231) = 2^{n-1}$;
(d) $A_n(213, 231) = A_n(132, 312) = 2^{n-1}$;
(e) $A_n(132, 321) = A_n(123, 231) = A_n(123, 312) = A_n(213, 321) = 1 + \binom{n}{2}$;
(f) $A_n(123, 321)$ equals $n$ if $n \le 2$, equals $4$ if $n \in \{3, 4\}$, and equals $0$ if
$n \ge 5$.

## Sources

- Han, *Joint Distributions of 10 Classical Statistics over Permutations Avoiding Two Patterns of Length 3*, INTEGERS 26 (2026), Article A18, Theorem 1, citing Simion and Schmidt.

Stated but not proved: `MetaMathlibExt.twoPatternAvoiderCount_length_three` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/TwoPatternAvoidanceCountsWanted.lean, line 102](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/TwoPatternAvoidanceCountsWanted.lean#L102). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/permutations-avoiding-two-patterns-of-length-thr/index.html#two-pattern-avoider-count-length-three).

## Ascent number of a permutation

For a permutation $\sigma$ of $\{0, 1, \dots, n - 1\}$,
$\operatorname{asc}(\sigma)$ is the number of positions $i$ with $i + 1 < n$ and
$\sigma(i) < \sigma(i + 1)$.

## Sources

- Han, *Joint Distributions of 10 Classical Statistics over Permutations Avoiding Two Patterns of Length 3*, INTEGERS 26 (2026), Article A18, Section 1 (`asc`, `des`).

Formalized by `MetaMathlibExt.permAscents`, a definition declared in [WantedExt/Combinatorics/Enumerative/TwoPatternAvoidanceCountsWanted.lean, line 124](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/TwoPatternAvoidanceCountsWanted.lean#L124). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/permutations-avoiding-two-patterns-of-length-thr/index.html#perm-ascents).

## Descent number of a permutation

For a permutation $\sigma$ of $\{0, 1, \dots, n - 1\}$,
$\operatorname{des}(\sigma)$ is the number of positions $i$ with $i + 1 < n$ and
$\sigma(i + 1) < \sigma(i)$.

## Sources

- Han, *Joint Distributions of 10 Classical Statistics over Permutations Avoiding Two Patterns of Length 3*, INTEGERS 26 (2026), Article A18, Section 1 (`asc`, `des`).

Formalized by `MetaMathlibExt.permDescents`, a definition declared in [WantedExt/Combinatorics/Enumerative/TwoPatternAvoidanceCountsWanted.lean, line 132](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/TwoPatternAvoidanceCountsWanted.lean#L132). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/permutations-avoiding-two-patterns-of-length-thr/index.html#perm-descents).

## Ascents and descents of $123$ and $132$

Writing permutations of $\{0, 1, 2\}$ in
one-based one-line notation, the identity $123$ has two ascents and no descents,
$\operatorname{asc}(123) = 2$ and $\operatorname{des}(123) = 0$, and $132$ has one of each,
$\operatorname{asc}(132) = \operatorname{des}(132) = 1$.

## Sources

- Han, *Joint Distributions of 10 Classical Statistics over Permutations Avoiding Two Patterns of Length 3*, INTEGERS 26 (2026), Article A18, Section 1 (`asc`, `des`).

Formalized by `MetaMathlibExt.permAscents_permDescents_small`, a theorem declared in [WantedExt/Combinatorics/Enumerative/TwoPatternAvoidanceCountsWanted.lean, line 139](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/TwoPatternAvoidanceCountsWanted.lean#L139). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/permutations-avoiding-two-patterns-of-length-thr/index.html#perm-ascents-perm-descents-small).

## Ascent–descent generating function of a pair of patterns

For permutations $\tau$ and
$\rho$ of $\{0, 1, 2\}$, let $S_n(\tau, \rho)$ be the set of permutations of
$\{0, 1, \dots, n-1\}$ that contain neither $\tau$ nor $\rho$ as a classical pattern. The
ascent–descent generating function of $(\tau, \rho)$ is the formal power series

$$\sum_{n \ge 0} \sum_{\sigma \in S_n(\tau, \rho)}
x^n p^{\mathrm{asc}(\sigma)} q^{\mathrm{des}(\sigma)}$$

in $x$ with coefficients in the polynomial ring $\mathbb{Q}[p, q]$, where $\mathrm{asc}(\sigma)$
and $\mathrm{des}(\sigma)$ are the numbers of ascents and descents of $\sigma$. The empty
permutation ($n = 0$) contributes the constant term $1$.

## Sources

- Han, *Joint Distributions of 10 Classical Statistics over Permutations Avoiding Two Patterns of Length 3*, INTEGERS 26 (2026), Article A18, Section 1 (`asc`, `des`).

Formalized by `MetaMathlibExt.ascDesGF`, a definition declared in [WantedExt/Combinatorics/Enumerative/TwoPatternAvoidanceCountsWanted.lean, line 149](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/TwoPatternAvoidanceCountsWanted.lean#L149). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/permutations-avoiding-two-patterns-of-length-thr/index.html#asc-des-gf).

## Ascents and descents over permutations avoiding $123$ and $132$

Let

$$G = \sum_{n \ge 0} \sum_{\sigma} x^n p^{\mathrm{asc}(\sigma)} q^{\mathrm{des}(\sigma)},$$

where $\sigma$ runs over the permutations of $\{0, 1, \dots, n-1\}$ that avoid both patterns
$123$ and $132$, and $\mathrm{asc}(\sigma)$ and $\mathrm{des}(\sigma)$ are the numbers of ascents
and descents of $\sigma$; $G$ is a formal power series in $x$ with coefficients in
$\mathbb{Q}[p, q]$. Then

$$(1 - 2qx - pqx^2 + q^2x^2)\, G = 1 + x - 2qx + px^2 - qx^2 - pqx^2 + q^2x^2.$$

## Sources

- Han, *Joint Distributions of 10 Classical Statistics over Permutations Avoiding Two Patterns of Length 3*, INTEGERS 26 (2026), Article A18, Corollary 1.

Stated but not proved: `MetaMathlibExt.ascDesGF_123_132` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/TwoPatternAvoidanceCountsWanted.lean, line 163](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/TwoPatternAvoidanceCountsWanted.lean#L163). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/permutations-avoiding-two-patterns-of-length-thr/index.html#asc-des-gf-123-132).

## Ascents and descents over permutations avoiding $132$ and $321$

Let

$$G = \sum_{n \ge 0} \sum_{\sigma} x^n p^{\mathrm{asc}(\sigma)} q^{\mathrm{des}(\sigma)},$$

where $\sigma$ runs over the permutations of $\{0, 1, \dots, n-1\}$ that avoid both patterns
$132$ and $321$, and $\mathrm{asc}(\sigma)$ and $\mathrm{des}(\sigma)$ are the numbers of ascents
and descents of $\sigma$; $G$ is a formal power series in $x$ with coefficients in
$\mathbb{Q}[p, q]$. Then

$$(1 - px)^3\, G = 1 + x - 3px - 2px^2 + 3p^2x^2 + qx^2 + p^2x^3 - p^3x^3.$$

## Sources

- Han, *Joint Distributions of 10 Classical Statistics over Permutations Avoiding Two Patterns of Length 3*, INTEGERS 26 (2026), Article A18, Corollary 2.

Stated but not proved: `MetaMathlibExt.ascDesGF_132_321` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/TwoPatternAvoidanceCountsWanted.lean, line 178](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/TwoPatternAvoidanceCountsWanted.lean#L178). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/permutations-avoiding-two-patterns-of-length-thr/index.html#asc-des-gf-132-321).

## Ascents and descents over permutations avoiding $213$ and $231$

Let

$$G = \sum_{n \ge 0} \sum_{\sigma} x^n p^{\mathrm{asc}(\sigma)} q^{\mathrm{des}(\sigma)},$$

where $\sigma$ runs over the permutations of $\{0, 1, \dots, n-1\}$ that avoid both patterns
$213$ and $231$, and $\mathrm{asc}(\sigma)$ and $\mathrm{des}(\sigma)$ are the numbers of ascents
and descents of $\sigma$; $G$ is a formal power series in $x$ with coefficients in
$\mathbb{Q}[p, q]$. Then

$$(1 - px - qx)\, G = 1 + x - px - qx.$$

The lead-in of the source's Corollary 4 names the permutations avoiding $213$ and $312$ instead;
both classes have this distribution of ascents and descents.

## Sources

- Han, *Joint Distributions of 10 Classical Statistics over Permutations Avoiding Two Patterns of Length 3*, INTEGERS 26 (2026), Article A18, Corollary 4.

Stated but not proved: `MetaMathlibExt.ascDesGF_213_231` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/TwoPatternAvoidanceCountsWanted.lean, line 194](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/TwoPatternAvoidanceCountsWanted.lean#L194). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/permutations-avoiding-two-patterns-of-length-thr/index.html#asc-des-gf-213-231).

## Left-to-right and right-to-left extrema of $132$ and $213$

Writing permutations of
$\{0, 1, 2\}$ in one-based one-line notation, $132$ has $2$ left-to-right maxima, $2$
right-to-left maxima, $1$ left-to-right minimum and $2$ right-to-left minima, and $213$ has $2$
left-to-right maxima, $1$ right-to-left maximum, $2$ left-to-right minima and $2$ right-to-left
minima.

## Sources

- Han, *Joint Distributions of 10 Classical Statistics over Permutations Avoiding Two Patterns of Length 3*, INTEGERS 26 (2026), Article A18, Section 1 (`lrmax`, `rlmax`, `lrmin`, `rlmin`).

Formalized by `MetaMathlibExt.permExtrema_small`, a theorem declared in [WantedExt/Combinatorics/Enumerative/TwoPatternAvoidanceCountsWanted.lean, line 207](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/TwoPatternAvoidanceCountsWanted.lean#L207). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/permutations-avoiding-two-patterns-of-length-thr/index.html#perm-extrema-small).

## Double ascents, double descents, peaks and valleys in length three

Writing permutations
of $\{0, 1, 2\}$ in one-based one-line notation, and $\operatorname{dasc}$,
$\operatorname{ddes}$, $\operatorname{pk}$ and $\operatorname{vl}$ for the numbers of double
ascents, double descents, peaks and valleys, $\operatorname{dasc}(123) = 1$,
$\operatorname{ddes}(321) = 1$, $\operatorname{dasc}(132) = \operatorname{ddes}(132) = 0$,
$\operatorname{pk}(132) = 1$, $\operatorname{vl}(132) = 0$, $\operatorname{pk}(213) = 0$ and
$\operatorname{vl}(213) = 1$.

## Sources

- Han, *Joint Distributions of 10 Classical Statistics over Permutations Avoiding Two Patterns of Length 3*, INTEGERS 26 (2026), Article A18, Section 1 (`dasc`, `ddes`, `pk`, `vl`).

Formalized by `MetaMathlibExt.permDoubleAscents_peaks_small`, a theorem declared in [WantedExt/Combinatorics/Enumerative/TwoPatternAvoidanceCountsWanted.lean, line 225](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/TwoPatternAvoidanceCountsWanted.lean#L225). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/permutations-avoiding-two-patterns-of-length-thr/index.html#perm-double-ascents-peaks-small).

## Generating function of ten classical statistics over a pair of patterns

For
permutations $\tau$ and $\rho$ of $\{0, 1, 2\}$, let $S_n(\tau, \rho)$ be the set of permutations
of $\{0, 1, \dots, n-1\}$ that contain neither $\tau$ nor $\rho$ as a classical pattern. The
generating function $F_{(\tau, \rho)}$ is the formal power series

$$F_{(\tau, \rho)} = \sum_{n \ge 0} \sum_{\sigma \in S_n(\tau, \rho)} x^n
p^{\mathrm{asc}(\sigma)} q^{\mathrm{des}(\sigma)} u^{\mathrm{lrmax}(\sigma)}
v^{\mathrm{rlmax}(\sigma)} s^{\mathrm{lrmin}(\sigma)} t^{\mathrm{rlmin}(\sigma)}
y^{\mathrm{dasc}(\sigma)} z^{\mathrm{ddes}(\sigma)} \ell^{\mathrm{pk}(\sigma)}
m^{\mathrm{vl}(\sigma)}$$

in $x$ with coefficients in the polynomial ring $\mathbb{Q}[p, q, u, v, s, t, y, z, \ell, m]$.
Here $\mathrm{asc}$ and $\mathrm{des}$ count ascents and descents, $\mathrm{lrmax}$ and
$\mathrm{rlmax}$ left-to-right and right-to-left maxima, $\mathrm{lrmin}$ and $\mathrm{rlmin}$
left-to-right and right-to-left minima, $\mathrm{dasc}$ and $\mathrm{ddes}$ double ascents and
double descents, and $\mathrm{pk}$ and $\mathrm{vl}$ peaks and valleys. The empty permutation
($n = 0$) contributes the constant term $1$.

## Sources

- Han, *Joint Distributions of 10 Classical Statistics over Permutations Avoiding Two Patterns of Length 3*, INTEGERS 26 (2026), Article A18, Section 1 (the g.f. `F_(τ,ρ)`).

Formalized by `MetaMathlibExt.classicalStatGF`, a definition declared in [WantedExt/Combinatorics/Enumerative/TwoPatternAvoidanceCountsWanted.lean, line 242](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/TwoPatternAvoidanceCountsWanted.lean#L242). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/permutations-avoiding-two-patterns-of-length-thr/index.html#classical-stat-gf).

## Double ascent–double descent generating function of a pair of patterns

For
permutations $\tau$ and $\rho$ of $\{0, 1, 2\}$, let $S_n(\tau, \rho)$ be the set of permutations
of $\{0, 1, \dots, n-1\}$ that contain neither $\tau$ nor $\rho$ as a classical pattern. The
double ascent–double descent generating function of $(\tau, \rho)$ is the formal power series

$$\sum_{n \ge 0} \sum_{\sigma \in S_n(\tau, \rho)}
x^n y^{\mathrm{dasc}(\sigma)} z^{\mathrm{ddes}(\sigma)}$$

in $x$ with coefficients in the polynomial ring $\mathbb{Q}[y, z]$, where $\mathrm{dasc}(\sigma)$
and $\mathrm{ddes}(\sigma)$ are the numbers of double ascents and double descents of $\sigma$.
The empty permutation ($n = 0$) contributes the constant term $1$.

## Sources

- Han, *Joint Distributions of 10 Classical Statistics over Permutations Avoiding Two Patterns of Length 3*, INTEGERS 26 (2026), Article A18, Section 1 (`dasc`, `ddes`).

Formalized by `MetaMathlibExt.dascDdesGF`, a definition declared in [WantedExt/Combinatorics/Enumerative/TwoPatternAvoidanceCountsWanted.lean, line 259](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/TwoPatternAvoidanceCountsWanted.lean#L259). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/permutations-avoiding-two-patterns-of-length-thr/index.html#dasc-ddes-gf).

## Ten classical statistics over permutations avoiding $123$ and $132$

Let $F$ be the
joint generating function of the ten classical statistics over the permutations avoiding both
patterns $123$ and $132$: a formal power series in $x$ over
$\mathbb{Q}[p, q, u, v, s, t, y, z, \ell, m]$ in which $x$ marks the length and
$p, q, u, v, s, t, y, z, \ell, m$ mark the numbers of ascents, descents, left-to-right maxima,
right-to-left maxima, left-to-right minima, right-to-left minima, double ascents, double
descents, peaks and valleys, respectively. Then

$$
(1 - \ell m p q s v x^2 - q s x z - q s v x z + q^2 s^2 v x^2 z^2)\, F = 1 +
s x \bigl(t u v + p t^2 u^2 v x - q(\ell m p v x + z + v z)\bigr) +
q^2 s^3 t u v^2 x^3 \bigl(\ell p u x (m - z) + z(-1 - m p t u x + z + p t u x z)\bigr) +
q s^2 v x^2 \bigl(q z^2 + p t^2 u x \bigl(m(u + v) - u(1 + v) z\bigr) +
t u \bigl(-z - v(-1 + \ell p (m - u) x + z)\bigr)\bigr).
$$

## Sources

- Han, *Joint Distributions of 10 Classical Statistics over Permutations Avoiding Two Patterns of Length 3*, INTEGERS 26 (2026), Article A18, Theorem 2.

Stated but not proved: `MetaMathlibExt.classicalStatGF_123_132` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/TwoPatternAvoidanceCountsWanted.lean, line 271](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/TwoPatternAvoidanceCountsWanted.lean#L271). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/permutations-avoiding-two-patterns-of-length-thr/index.html#classical-stat-gf-123-132).

## Ten classical statistics over permutations avoiding $132$ and $321$

Let $F$ be the
joint generating function of the ten classical statistics over the permutations avoiding both
patterns $132$ and $321$: a formal power series in $x$ over
$\mathbb{Q}[p, q, u, v, s, t, y, z, \ell, m]$ in which $x$ marks the length and
$p, q, u, v, s, t, y, z, \ell, m$ mark the numbers of ascents, descents, left-to-right maxima,
right-to-left maxima, left-to-right minima, right-to-left minima, double ascents, double
descents, peaks and valleys, respectively. Then $(1 - ptxy)(1 - puxy)(1 - ptuxy)\, F$ equals

$$
1 + stuvx + pst^2u^2vx^2 + qs^2tuv^2x^2 + mpqs^2t^2u^2vx^3 + mpqs^2t^2uv^2x^3 +
\ell pqs^2tu^2v^2x^3 + \ell mp^2qs^2t^2u^3vx^4 + \ell mp^2qs^2t^2u^2v^2x^4 - ptxy - puxy -
pqs^2tu^2v^2x^3y - pst^2uvx^2y - pstu^2vx^2y - pst^2u^2vx^2y - p^2st^3u^2vx^3y -
p^2st^2u^3vx^3y - pqs^2t^2uv^2x^3y - ptuxy - pqs^2t^2u^2v^2x^3y - mp^2qs^2t^2u^3vx^4y -
\ell p^2qs^2t^2u^2v^2x^4y - mp^2qs^2t^2u^2v^2x^4y - mp^2qs^2t^3u^2v^2x^4y -
\ell p^2qs^2t^2u^3v^2x^4y - \ell mp^3qs^2t^3u^3v^2x^5y + p^2tux^2y^2 + p^2t^2ux^2y^2 +
p^2tu^2x^2y^2 + p^2st^2u^2vx^3y^2 + p^2st^3u^2vx^3y^2 + p^2st^2u^3vx^3y^2 +
p^3st^3u^3vx^4y^2 + p^2qs^2t^2u^2v^2x^4y^2 + p^2qs^2t^3u^2v^2x^4y^2 +
p^2qs^2t^2u^3v^2x^4y^2 + \ell p^3qs^2t^3u^3v^2x^5y^2 + mp^3qs^2t^3u^3v^2x^5y^2 -
p^3t^2u^2x^3y^3 - p^3st^3u^3vx^4y^3 - p^3qs^2t^3u^3v^2x^5y^3.
$$

## Sources

- Han, *Joint Distributions of 10 Classical Statistics over Permutations Avoiding Two Patterns of Length 3*, INTEGERS 26 (2026), Article A18, Theorem 3.

Stated but not proved: `MetaMathlibExt.classicalStatGF_132_321` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/TwoPatternAvoidanceCountsWanted.lean, line 298](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/TwoPatternAvoidanceCountsWanted.lean#L298). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/permutations-avoiding-two-patterns-of-length-thr/index.html#classical-stat-gf-132-321).

## Ten classical statistics over permutations avoiding $213$ and $231$

Let $F$ be the
joint generating function of the ten classical statistics over the permutations avoiding both
patterns $213$ and $231$: a formal power series in $x$ over
$\mathbb{Q}[p, q, u, v, s, t, y, z, \ell, m]$ in which $x$ marks the length and
$p, q, u, v, s, t, y, z, \ell, m$ mark the numbers of ascents, descents, left-to-right maxima,
right-to-left maxima, left-to-right minima, right-to-left minima, double ascents, double
descents, peaks and valleys, respectively. Then
$(1 - ptuxy)(1 - qsvxz)\bigl((1 - ptxy)(1 - qvxz) - \ell mpqtvx^2\bigr)\, F$ equals

$$
svx\Bigl(qz(qvxz - 1) + p^2t^3u^2x^2y\bigl(\ell(m - 1)qvx - (y - 1)(qvxz - 1)\bigr) +
t\bigl(u(1 - qvxz)(1 + pqxyz) + pqxz(\ell mqvx + y - qvxyz)\bigr) -
pt^2ux\bigl(-\ell quvx - u(y - 1)(qvxz - 1) + (1 + pqxyz)(\ell mqvx + y - qvxyz)\bigr)\Bigr) -
qs^2tuv^2x^2\Bigl(mptx(ptuxy - 1)\bigl(1 + (\ell - 1)qvxz\bigr) -
(ptxy - 1)\bigl((1 - z)(qvxz - 1) +
ptux\bigl(z(1 + \ell qvx - qvxz) + y(z - 1)(qvxz - 1)\bigr)\bigr)\Bigr) +
(ptuxy - 1)\bigl(\ell mpqtvx^2 - (1 - ptxy)(1 - qvxz)\bigr).
$$

## Sources

- Han, *Joint Distributions of 10 Classical Statistics over Permutations Avoiding Two Patterns of Length 3*, INTEGERS 26 (2026), Article A18, Theorem 5.

Stated but not proved: `MetaMathlibExt.classicalStatGF_213_231` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/TwoPatternAvoidanceCountsWanted.lean, line 341](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/TwoPatternAvoidanceCountsWanted.lean#L341). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/permutations-avoiding-two-patterns-of-length-thr/index.html#classical-stat-gf-213-231).

## Double ascents and double descents over permutations avoiding $231$ and $312$

Let

$$H = \sum_{n \ge 0} \sum_{\sigma} x^n y^{\mathrm{dasc}(\sigma)} z^{\mathrm{ddes}(\sigma)},$$

where $\sigma$ runs over the permutations of $\{0, 1, \dots, n-1\}$ that avoid both patterns
$231$ and $312$, and $\mathrm{dasc}(\sigma)$ and $\mathrm{ddes}(\sigma)$ are the numbers of
double ascents and double descents of $\sigma$; $H$ is a formal power series in $x$ with
coefficients in $\mathbb{Q}[y, z]$. Then

$$(1 - x(y + z) - x^2(1 - yz))\, H = 1 + x^2(1 + x)(1 - y)(1 - z) + x(1 - y - z).$$

The source's Corollary 3 also gives an identity (22) for ascents and descents, marked by $p$
and $q$, and an identity (24) for peaks and valleys, marked by $\ell$ and $m$, over this class;
both are false as printed (at $p = 2$, $q = 1$ the coefficient of $x^5$ in (22) is $75$, the true
value $81$; at $\ell = 2$, $m = 1$ the coefficient of $x^5$ in (24) is $28$, the true value
$29$).

## Sources

- Han, *Joint Distributions of 10 Classical Statistics over Permutations Avoiding Two Patterns of Length 3*, INTEGERS 26 (2026), Article A18, Corollary 3.

Stated but not proved: `MetaMathlibExt.dascDdesGF_231_312` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/TwoPatternAvoidanceCountsWanted.lean, line 377](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/TwoPatternAvoidanceCountsWanted.lean#L377). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/permutations-avoiding-two-patterns-of-length-thr/index.html#dasc-ddes-gf-231-312).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Permutations avoiding two patterns of length three](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-patterns/permutations-avoiding-two-patterns-of-length-thr/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Combinatorics/permutations/permutation-patterns/permutations-avoiding-two-patterns-of-length-thr)
