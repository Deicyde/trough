---
declaration: section
origin: cited
lean: MetaMathlibExt.qWeightedDigitSum, MetaMathlibExt.qWeightedDigitPartialSum, MetaMathlibExt.takagiLandsberg, MetaMathlibExt.qWeightedDigitSum_zero, MetaMathlibExt.qWeightedDigitSum_of_pos, MetaMathlibExt.takagiLandsberg_zero, MetaMathlibExt.qWeightedDigitPartialSum_dyadic_fluctuation, MetaMathlibExt.qWeighted_trollopeDelange
statement: formalized
---

# Binary digit sums and the Trollope–Delange formula

19 results, 15 proved and 4 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/binary-digit-sums-and-the-trollope-delange-formu/index.html).

## The $q$-weighted binary digit sum

Let $q$ be an element of a commutative ring and let
$k$ be a natural number with binary expansion $k = \sum_{i \ge 0} \omega_i 2^i$, where
$\omega_i \in \{0, 1\}$. The $q$-weighted binary digit sum of $k$ is
$s_q(k) = \sum_{i \ge 0} \omega_i q^{i+1}$, a finite sum because only finitely many $\omega_i$
are nonzero.

## Sources

- Aleksei Minabutdinov, *A q-Weighted Analogue of the Trollope-Delange Formula*, INTEGERS 26 (2026), Article A61, Section 1 (definition of `s_q`).

Formalized by `MetaMathlibExt.qWeightedDigitSum`, a definition declared in [WantedExt/NumberTheory/QWeightedTrollopeDelangeWanted.lean, line 30](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/QWeightedTrollopeDelangeWanted.lean#L30). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/binary-digit-sums-and-the-trollope-delange-formu/index.html#q-weighted-digit-sum).

## Partial sums of the $q$-weighted binary digit sum

For an element $q$ of a commutative
ring and a natural number $n$, the partial sum is $S_q(n) = \sum_{k=0}^{n-1} s_q(k)$, where $s_q$
is the $q$-weighted binary digit sum.

## Sources

- Aleksei Minabutdinov, *A q-Weighted Analogue of the Trollope-Delange Formula*, INTEGERS 26 (2026), Article A61, Section 1 (definition of `S_q`).

Formalized by `MetaMathlibExt.qWeightedDigitPartialSum`, a definition declared in [WantedExt/NumberTheory/QWeightedTrollopeDelangeWanted.lean, line 37](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/QWeightedTrollopeDelangeWanted.lean#L37). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/binary-digit-sums-and-the-trollope-delange-formu/index.html#q-weighted-digit-partial-sum).

## The Takagi–Landsberg function

For a real or complex parameter $a$ and a real number $x$,
let $\tau(y)$ denote the distance from a real number $y$ to the nearest integer. The
Takagi–Landsberg function is $\mathcal{T}_a(x) = \sum_{n \ge 0} a^n \tau(2^n x)$, where the
value is taken to be $0$ when the series does not converge absolutely. The series converges for
$|a| < 1$, and at dyadic rationals $x$ it is a finite sum.

## Sources

- Aleksei Minabutdinov, *A q-Weighted Analogue of the Trollope-Delange Formula*, INTEGERS 26 (2026), Article A61, Section 1.1, equation (TakagiLandsberg).

Formalized by `MetaMathlibExt.takagiLandsberg`, a definition declared in [WantedExt/NumberTheory/QWeightedTrollopeDelangeWanted.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/QWeightedTrollopeDelangeWanted.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/binary-digit-sums-and-the-trollope-delange-formu/index.html#takagi-landsberg).

## The $q$-weighted digit sum of zero

For every element $q$ of a commutative ring, the
$q$-weighted binary digit sum of $0$ is $s_q(0) = 0$.

## Sources

- Aleksei Minabutdinov, *A q-Weighted Analogue of the Trollope-Delange Formula*, INTEGERS 26 (2026), Article A61, Section 1.

Formalized by `MetaMathlibExt.qWeightedDigitSum_zero`, a theorem declared in [WantedExt/NumberTheory/QWeightedTrollopeDelangeWanted.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/QWeightedTrollopeDelangeWanted.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/binary-digit-sums-and-the-trollope-delange-formu/index.html#q-weighted-digit-sum-zero).

## Binary recursion for the $q$-weighted digit sum

Let $q$ be an element of a commutative
ring and let $k > 0$ be a natural number. Then the $q$-weighted binary digit sum satisfies
$s_q(k) = q\,(k \bmod 2) + q\,s_q(\lfloor k/2 \rfloor)$.

This gives the paper's relations $s_q(2j) = q\,s_q(j)$ for $j \ge 1$ and
$s_q(2j+1) = q\,s_q(j) + q$ for $j \ge 0$.

## Sources

- Aleksei Minabutdinov, *A q-Weighted Analogue of the Trollope-Delange Formula*, INTEGERS 26 (2026), Article A61, proof of Theorem 1, equations (s(2j)) and (s(2j+1)).

Formalized by `MetaMathlibExt.qWeightedDigitSum_of_pos`, a theorem declared in [WantedExt/NumberTheory/QWeightedTrollopeDelangeWanted.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/QWeightedTrollopeDelangeWanted.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/binary-digit-sums-and-the-trollope-delange-formu/index.html#q-weighted-digit-sum-of-pos).

## The Takagi–Landsberg function vanishes at zero

For every real or complex parameter $a$,
the Takagi–Landsberg function satisfies $\mathcal{T}_a(0) = 0$.

## Sources

- Aleksei Minabutdinov, *A q-Weighted Analogue of the Trollope-Delange Formula*, INTEGERS 26 (2026), Article A61, Section 1.1.

Formalized by `MetaMathlibExt.takagiLandsberg_zero`, a theorem declared in [WantedExt/NumberTheory/QWeightedTrollopeDelangeWanted.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/QWeightedTrollopeDelangeWanted.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/binary-digit-sums-and-the-trollope-delange-formu/index.html#takagi-landsberg-zero).

## Dyadic values of the normalized $q$-weighted fluctuation

Let $q$ be a complex number
with $|q| > 1/2$, let $N > 0$ be a natural number, and let $j \le 2^{N-1}$ be a natural number.
Put $t_j = j / 2^{N-1}$ and $a = 1/(2q)$. Then

$$\frac{S_q(2j) - t_j\,S_q(2^N)}{(2q)^{N-1}} = -q\,\mathcal{T}_a(t_j),$$

where $S_q$ is the partial sum of the $q$-weighted binary digit sum and $\mathcal{T}_a$ is the
Takagi–Landsberg function. With $l = 2^N$ we have $t_j l = 2j$, so the numerator is the
fluctuation $S_q(t_j l) - t_j\,S_q(l)$ at the grid point $t_j$ of $[0, 1]$.

## Sources

- Aleksei Minabutdinov, *A q-Weighted Analogue of the Trollope-Delange Formula*, INTEGERS 26 (2026), Article A61, Proposition 1.

Stated but not proved: `MetaMathlibExt.qWeightedDigitPartialSum_dyadic_fluctuation` is written with `theorem_wanted` in [WantedExt/NumberTheory/QWeightedTrollopeDelangeWanted.lean, line 86](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/QWeightedTrollopeDelangeWanted.lean#L86). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/binary-digit-sums-and-the-trollope-delange-formu/index.html#q-weighted-digit-partial-sum-dyadic-fluc).

## The $q$-weighted Trollope–Delange formula

Let $q$ be a real number with $|q| > 1/2$ and
$q \ne 1$, and put $a = 1/(2q)$. For a positive integer $n$, let $k = \lfloor \log_2 n \rfloor$
and let $u = \log_2 n - k$ be the fractional part of $\log_2 n$. Write
$F(u) = 2^{1-u}\,\mathcal{T}_a(2^{u-1})$. Then

$$\frac{S_q(n)}{n} = \frac{q}{2}\left(\frac{1 - q^{k+1}}{1 - q} - q^k F(u)\right),$$

where $S_q$ is the partial sum of the $q$-weighted binary digit sum and $\mathcal{T}_a$ is the
Takagi–Landsberg function.

## Sources

- Aleksei Minabutdinov, *A q-Weighted Analogue of the Trollope-Delange Formula*, INTEGERS 26 (2026), Article A61, Theorem 1.

Stated but not proved: `MetaMathlibExt.qWeighted_trollopeDelange` is written with `theorem_wanted` in [WantedExt/NumberTheory/QWeightedTrollopeDelangeWanted.lean, line 100](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/QWeightedTrollopeDelangeWanted.lean#L100). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/binary-digit-sums-and-the-trollope-delange-formu/index.html#q-weighted-trollope-delange).

## Girgensohn's lemma

Let $G$ be a function from the natural numbers to the real numbers, and
for a positive integer $n$ let $p_n = 2^{\lfloor \log_2 n \rfloor}$, so that $(n - p_n)/p_n$ is a
dyadic rational in $[0, 1)$. The following are equivalent: (i) for all positive integers $m$ and
$n$ with $(m - p_m)/p_m = (n - p_n)/p_n$ we have $G(m) = G(n)$, that is, $F((n - p_n)/p_n) = G(n)$
well-defines a function $F$ of these dyadic rationals; (ii) $G(2n) = G(n)$ for every positive
integer $n$.

## Sources

- Aleksei Minabutdinov, *A q-Weighted Analogue of the Trollope-Delange Formula*, INTEGERS 26 (2026), Article A61, Lemma 1, quoting Girgensohn, *Digital Sums and Functional Equations*, Lemma 1.

Stated but not proved: `MetaMathlibExt.dyadicMantissa_wellDefined_iff_doubling_invariant` is written with `theorem_wanted` in [WantedExt/NumberTheory/QWeightedTrollopeDelangeWanted.lean, line 115](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/QWeightedTrollopeDelangeWanted.lean#L115). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/binary-digit-sums-and-the-trollope-delange-formu/index.html#dyadic-mantissa-well-defined-iff-doublin).

## Carry in adding a natural number to a dyadic integer

Let $\omega$ be a dyadic integer,
written as its sequence $(\omega_0, \omega_1, \dots)$ of binary digits $\omega_i \in \{0, 1\}$
(least significant digit first), and let $j$ be a natural number with binary digits
$j_0, j_1, \dots$. The carry $c_i$ into digit $i$ in the binary addition of $j$ to $\omega$ is
defined by $c_0 = 0$ and $c_{i+1} = \lfloor (\omega_i + j_i + c_i)/2 \rfloor$.

## Sources

- Aleksei Minabutdinov, *A q-Weighted Analogue of the Trollope-Delange Formula*, INTEGERS 26 (2026), Article A61, Section 5 (dyadic integers and the odometer).

Formalized by `MetaMathlibExt.dyadicAddNatCarry`, a definition declared in [WantedExt/NumberTheory/QWeightedTrollopeDelangeWanted.lean, line 126](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/QWeightedTrollopeDelangeWanted.lean#L126). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/binary-digit-sums-and-the-trollope-delange-formu/index.html#dyadic-add-nat-carry).

## Adding a natural number to a dyadic integer

Let $\omega$ be a dyadic integer, written as
its sequence $(\omega_0, \omega_1, \dots)$ of binary digits $\omega_i \in \{0, 1\}$ (least
significant digit first), and let $j$ be a natural number with binary digits $j_0, j_1, \dots$.
The dyadic integer $\omega + j$ has $i$-th digit $(\omega_i + j_i + c_i) \bmod 2$, where the
carries are given by $c_0 = 0$ and $c_{i+1} = \lfloor (\omega_i + j_i + c_i)/2 \rfloor$.

## Sources

- Aleksei Minabutdinov, *A q-Weighted Analogue of the Trollope-Delange Formula*, INTEGERS 26 (2026), Article A61, Section 5 (dyadic integers and the odometer).

Formalized by `MetaMathlibExt.dyadicAddNat`, a definition declared in [WantedExt/NumberTheory/QWeightedTrollopeDelangeWanted.lean, line 134](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/QWeightedTrollopeDelangeWanted.lean#L134). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/binary-digit-sums-and-the-trollope-delange-formu/index.html#dyadic-add-nat).

## Dyadic odometer

The dyadic odometer is the map $T$ on the dyadic integers $\mathbb{Z}_2$,
viewed as binary digit sequences $\omega = (\omega_0, \omega_1, \dots)$ (least significant digit
first), given by $T\omega = \omega + 1$, binary addition of $1$ with carries.

## Sources

- Aleksei Minabutdinov, *A q-Weighted Analogue of the Trollope-Delange Formula*, INTEGERS 26 (2026), Article A61, Section 5.

Formalized by `MetaMathlibExt.dyadicOdometer`, a definition declared in [WantedExt/NumberTheory/QWeightedTrollopeDelangeWanted.lean, line 141](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/QWeightedTrollopeDelangeWanted.lean#L141). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/binary-digit-sums-and-the-trollope-delange-formu/index.html#dyadic-odometer).

## First digits of the odometer at zero

Let $T$ be the dyadic odometer $T\omega = \omega + 1$
on dyadic integers $\omega = (\omega_0, \omega_1, \dots)$, written as binary digit sequences. The
image $T(0)$ of the zero sequence $(0, 0, 0, \dots)$ has digits $T(0)_0 = 1$, $T(0)_1 = 0$ and
$T(0)_2 = 0$.

## Sources

- Aleksei Minabutdinov, *A q-Weighted Analogue of the Trollope-Delange Formula*, INTEGERS 26 (2026), Article A61, Section 5.

Formalized by `MetaMathlibExt.dyadicOdometer_zero_apply`, a theorem declared in [WantedExt/NumberTheory/QWeightedTrollopeDelangeWanted.lean, line 147](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/QWeightedTrollopeDelangeWanted.lean#L147). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/binary-digit-sums-and-the-trollope-delange-formu/index.html#dyadic-odometer-zero-apply).

## Haar measure on the dyadic integers

The Haar measure on the dyadic integers
$\mathbb{Z}_2$, viewed as the space $\{0, 1\}^{\mathbb{N}}$ of binary digit sequences: the infinite
product of the uniform probability measures on $\{0, 1\}$, one for each digit.

## Sources

- Aleksei Minabutdinov, *A q-Weighted Analogue of the Trollope-Delange Formula*, INTEGERS 26 (2026), Article A61, Section 5.

Formalized by `MetaMathlibExt.dyadicHaar`, a definition declared in [WantedExt/NumberTheory/QWeightedTrollopeDelangeWanted.lean, line 156](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/QWeightedTrollopeDelangeWanted.lean#L156). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/binary-digit-sums-and-the-trollope-delange-formu/index.html#dyadic-haar).

## Odometer partial sums

Let $q \in \mathbb{C}$, let $\omega = (\omega_0, \omega_1, \dots)$ be
a dyadic integer written as its binary digit sequence, let $T$ be the dyadic odometer
$T\omega = \omega + 1$, and let $s_q(\omega) = \sum_{i \ge 0} \omega_i q^{i+1}$, taken to be $0$
when the series is not absolutely summable. For real $x$ the odometer partial sum is

$$S_{q,\omega}(x) = \sum_{j < \lfloor x \rfloor_+} s_q(T^j \omega) +
\{x\} \, s_q(T^{\lfloor x \rfloor_+} \omega),$$

where $\lfloor x \rfloor_+ = \max(\lfloor x \rfloor, 0)$ and $\{x\} = x - \lfloor x \rfloor$. So
$S_{q,\omega}(n) = \sum_{j < n} s_q(T^j \omega)$ for every natural number $n$, and for $x \ge 0$
the function $S_{q,\omega}$ interpolates these values linearly between consecutive integers.

## Sources

- Aleksei Minabutdinov, *A q-Weighted Analogue of the Trollope-Delange Formula*, INTEGERS 26 (2026), Article A61, Sections 4 and 5.

Formalized by `MetaMathlibExt.odometerDigitPartialSum`, a definition declared in [WantedExt/NumberTheory/QWeightedTrollopeDelangeWanted.lean, line 173](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/QWeightedTrollopeDelangeWanted.lean#L173). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/binary-digit-sums-and-the-trollope-delange-formu/index.html#odometer-digit-partial-sum).

## The odometer partial sum vanishes at zero

For every $q \in \mathbb{C}$ and every dyadic
integer $\omega$, the interpolated odometer partial sum satisfies $S_{q,\omega}(0) = 0$.

## Sources

- Aleksei Minabutdinov, *A q-Weighted Analogue of the Trollope-Delange Formula*, INTEGERS 26 (2026), Article A61, Section 5.

Formalized by `MetaMathlibExt.odometerDigitPartialSum_zero`, a theorem declared in [WantedExt/NumberTheory/QWeightedTrollopeDelangeWanted.lean, line 181](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/QWeightedTrollopeDelangeWanted.lean#L181). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/binary-digit-sums-and-the-trollope-delange-formu/index.html#odometer-digit-partial-sum-zero).

## Maximal fluctuation of the odometer partial sums

Let $q$ be a complex number, let
$\omega = (\omega_0, \omega_1, \dots)$ be a dyadic integer (a sequence of binary digits), let $l$
be a natural number, and let $S_{q,\omega}$ denote the interpolated odometer partial sums. The
maximal fluctuation is the supremum over $t \in [0, 1]$ of
$|S_{q,\omega}(t l) - t\,S_{q,\omega}(l)|$.

This is the scale of the canonical normalizing coefficient of the sources: "the normalizing
coefficient $R_n$ is canonically defined to be equal to the maximum in $t \in [0, 1]$ of
$|\mathcal{S}(t \cdot l_n(x)) - t \cdot \mathcal{S}(l_n)|$".

## Sources

- Aleksei Minabutdinov, *Limiting curves for the dyadic odometer and the generalized Trollope-Delange formula*, Section 2.2 (definition of `φ_n` and `R_n`), and *A q-Weighted Analogue of the Trollope-Delange Formula*, INTEGERS 26 (2026), Article A61, Section 3 (definition of the normalization factor `R_n`).

Formalized by `MetaMathlibExt.odometerMaxFluctuation`, a definition declared in [WantedExt/NumberTheory/QWeightedTrollopeDelangeWanted.lean, line 194](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/QWeightedTrollopeDelangeWanted.lean#L194). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/binary-digit-sums-and-the-trollope-delange-formu/index.html#odometer-max-fluctuation).

## Stabilizing sequence for the dyadic odometer

Let $q \in \mathbb{C}$, let $\omega$ be a
dyadic integer, let $S_{q,\omega}$ be the interpolated odometer partial sum, and for a natural
number $l$ let $M_{q,\omega}(l) = \sup_{t \in [0, 1]} |S_{q,\omega}(tl) - t S_{q,\omega}(l)|$ be the
maximal fluctuation. A sequence $(l_n)$ of natural numbers is a stabilizing sequence for
$(q, \omega)$ with normalizing sequence $(R_n)$ of complex numbers and limiting curve
$\varphi : \mathbb{R} \to \mathbb{C}$ when: every $l_n$ is positive and $l_n \to \infty$; every
$R_n$ is nonzero and $|R_n| \to \infty$; there are real constants $c > 0$ and $C$ with
$c M_{q,\omega}(l_n) \le |R_n| \le C M_{q,\omega}(l_n)$ for all sufficiently large $n$;
$\varphi$ is continuous on $[0, 1]$; and the functions
$t \mapsto (S_{q,\omega}(t l_n) - t S_{q,\omega}(l_n))/R_n$ converge uniformly on $[0, 1]$ to
$\varphi$.

The normalizing sequence $R_n$ is chosen of the order of $M_{q,\omega}(l_n)$, not equal to it:
with equality every normalized fluctuation would have supremum norm at most $1$, so the limit in
Theorem 2 of Article A61 could not be the negative Takagi–Landsberg function $-\mathcal{T}_a$
(for example $\mathcal{T}_{3/4}(1/3) = 4/3$). This matches the sources' usage, where
$\varphi^{l_n,R_n}$ is parametrized by the chosen $R_n$ (e.g. $R_n = (2q)^{n-1}$ along
$l_n = 2^n$ in Article A61, Section 3); unbounded growth of $R_n$ is the necessary condition for
a limiting curve recorded in the odometer paper.

## Sources

- Aleksei Minabutdinov, *Limiting curves for the dyadic odometer and the generalized Trollope-Delange formula*, Definition 1 and Section 3.1, restated in *A q-Weighted Analogue of the Trollope-Delange Formula*, INTEGERS 26 (2026), Article A61, Section 3.

Formalized by `MetaMathlibExt.IsStabilizingSeq`, a definition declared in [WantedExt/NumberTheory/QWeightedTrollopeDelangeWanted.lean, line 216](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/QWeightedTrollopeDelangeWanted.lean#L216). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/binary-digit-sums-and-the-trollope-delange-formu/index.html#is-stabilizing-seq).

## Odometer limiting curve is the negative Takagi–Landsberg function

Let $q \in \mathbb{C}$
with $1/2 < |q| < 1$ and put $a = 1/(2q)$. Then for almost every dyadic integer $\omega$ with
respect to the Haar measure on $\mathbb{Z}_2$ there are a sequence $(l_n)$ of natural numbers and
a sequence $(R_n)$ of complex numbers such that $(l_n)$ is a stabilizing sequence for
$(q, \omega)$ with normalizing sequence $(R_n)$ and limiting curve $t \mapsto -\mathcal{T}_a(t)$,
where $\mathcal{T}_a$ is the Takagi–Landsberg function. In particular, with $S_{q,\omega}$ the
interpolated odometer partial sums, the normalized fluctuations
$(S_{q,\omega}(t l_n) - t S_{q,\omega}(l_n))/R_n$ converge uniformly on $[0, 1]$ to
$-\mathcal{T}_a(t)$.

This is Theorem 2 of the source, which quotes it from the author's earlier work.

## Sources

- Aleksei Minabutdinov, *A q-Weighted Analogue of the Trollope-Delange Formula*, INTEGERS 26 (2026), Article A61, Theorem 2.

Stated but not proved: `MetaMathlibExt.odometer_limitingCurve_eq_neg_takagi` is written with `theorem_wanted` in [WantedExt/NumberTheory/QWeightedTrollopeDelangeWanted.lean, line 238](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/QWeightedTrollopeDelangeWanted.lean#L238). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/binary-digit-sums-and-the-trollope-delange-formu/index.html#odometer-limiting-curve-eq-neg-takagi).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Binary digit sums and the Trollope–Delange formula](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/binary-digit-sums-and-the-trollope-delange-formu/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/digits-numeration/digit-properties/binary-digit-sums-and-the-trollope-delange-formu)
