---
declaration: section
origin: cited
lean: MetaMathlibExt.convergentMatrix, MetaMathlibExt.convergentMatrix_nil, MetaMathlibExt.convergentMatrix_cons, MetaMathlibExt.cfCylinder, MetaMathlibExt.cfCylinder_nil, MetaMathlibExt.fundInterval, MetaMathlibExt.fundInterval_of_lt, MetaMathlibExt.gaussKuzminMass
statement: formalized
---

# Gauss–Kuzmin masses of continued fraction strings

29 results, 15 proved and 14 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/gauss-kuzmin-masses-of-continued-fraction-string/index.html).

## Convergent matrix

For a finite string $a = (a_1, \ldots, a_n)$ of natural numbers, the
convergent matrix $C(a)$ is the $2 \times 2$ integer matrix given by the ordered product
$C(a) = \begin{pmatrix} 0 & 1 \\ 1 & a_1 \end{pmatrix} \cdots
\begin{pmatrix} 0 & 1 \\ 1 & a_n \end{pmatrix}$ (the identity matrix when $n = 0$). Its entries
are written $C(a) = \begin{pmatrix} p' & p \\ q' & q \end{pmatrix}$.

When $n \ge 1$ and all $a_i$ are positive, $p/q = [0; a_1, \ldots, a_n]$ and $p'/q'$ is the
preceding convergent.

## Sources

- Shreyas Singh, Zhuo Zhang and AJ Hildebrand, *An Elementary Characterization of the Gauss-Kuzmin Measure in the Theory of Continued Fractions*, INTEGERS 25 (2025), Article A89, Definition 2.1 and equation (2.8).

Formalized by `MetaMathlibExt.convergentMatrix`, a definition declared in [WantedExt/NumberTheory/GaussKuzminSymmetryWanted.lean, line 31](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/GaussKuzminSymmetryWanted.lean#L31). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/gauss-kuzmin-masses-of-continued-fraction-string/index.html#convergent-matrix).

## Convergent matrix of the empty string

The convergent matrix of the empty string is the
$2 \times 2$ identity matrix.

## Sources

- Shreyas Singh, Zhuo Zhang and AJ Hildebrand, *An Elementary Characterization of the Gauss-Kuzmin Measure in the Theory of Continued Fractions*, INTEGERS 25 (2025), Article A89, Section 2.2.

Formalized by `MetaMathlibExt.convergentMatrix_nil`, a theorem declared in [WantedExt/NumberTheory/GaussKuzminSymmetryWanted.lean, line 39](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/GaussKuzminSymmetryWanted.lean#L39). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/gauss-kuzmin-masses-of-continued-fraction-string/index.html#convergent-matrix-nil).

## Prepending a digit to a string

For every natural number $t$ and every finite string $a$
of natural numbers, the convergent matrix of the string $(t, a)$, obtained by prepending $t$ to
$a$, is $C(t, a) = \begin{pmatrix} 0 & 1 \\ 1 & t \end{pmatrix} C(a)$.

## Sources

- Shreyas Singh, Zhuo Zhang and AJ Hildebrand, *An Elementary Characterization of the Gauss-Kuzmin Measure in the Theory of Continued Fractions*, INTEGERS 25 (2025), Article A89, equation (2.8).

Formalized by `MetaMathlibExt.convergentMatrix_cons`, a theorem declared in [WantedExt/NumberTheory/GaussKuzminSymmetryWanted.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/GaussKuzminSymmetryWanted.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/gauss-kuzmin-masses-of-continued-fraction-string/index.html#convergent-matrix-cons).

## Fundamental interval of a string

For a finite string $a = (a_1, \ldots, a_n)$ of natural
numbers, the fundamental interval $I(a)$ is the set of real numbers $x \in [0, 1)$ whose
continued fraction expansion $x = [0; a_1(x), a_2(x), \ldots]$ has at least $n$ digits, with
$a_i(x) = a_i$ for $1 \le i \le n$.

The digits are those produced by the continued fraction algorithm, so a rational $x$ uses the
finite expansion whose last digit is at least $2$ (the resolution in the paper's footnote 2).

## Sources

- Shreyas Singh, Zhuo Zhang and AJ Hildebrand, *An Elementary Characterization of the Gauss-Kuzmin Measure in the Theory of Continued Fractions*, INTEGERS 25 (2025), Article A89, equation (1.4).

Formalized by `MetaMathlibExt.cfCylinder`, a definition declared in [WantedExt/NumberTheory/GaussKuzminSymmetryWanted.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/GaussKuzminSymmetryWanted.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/gauss-kuzmin-masses-of-continued-fraction-string/index.html#cf-cylinder).

## Fundamental interval of the empty string

The fundamental interval of the empty string is
the whole interval: $I(()) = [0, 1)$.

## Sources

- Shreyas Singh, Zhuo Zhang and AJ Hildebrand, *An Elementary Characterization of the Gauss-Kuzmin Measure in the Theory of Continued Fractions*, INTEGERS 25 (2025), Article A89, equation (1.4).

Formalized by `MetaMathlibExt.cfCylinder_nil`, a theorem declared in [WantedExt/NumberTheory/GaussKuzminSymmetryWanted.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/GaussKuzminSymmetryWanted.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/gauss-kuzmin-masses-of-continued-fraction-string/index.html#cf-cylinder-nil).

## Half-open interval between two reals

For real numbers $\alpha$ and $\beta$, the interval
$\langle \alpha, \beta \rangle$ is $[\alpha, \beta)$ if $\alpha < \beta$, and $(\beta, \alpha]$
otherwise.

## Sources

- Shreyas Singh, Zhuo Zhang and AJ Hildebrand, *An Elementary Characterization of the Gauss-Kuzmin Measure in the Theory of Continued Fractions*, INTEGERS 25 (2025), Article A89, Section 2.3 (interval notation).

Formalized by `MetaMathlibExt.fundInterval`, a definition declared in [WantedExt/NumberTheory/GaussKuzminSymmetryWanted.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/GaussKuzminSymmetryWanted.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/gauss-kuzmin-masses-of-continued-fraction-string/index.html#fund-interval).

## Half-open interval between increasing endpoints

For real numbers $\alpha$ and $\beta$,
write $\langle \alpha, \beta \rangle$ for $[\alpha, \beta)$ if $\alpha < \beta$ and for
$(\beta, \alpha]$ otherwise. If $\alpha < \beta$, then
$\langle \alpha, \beta \rangle = [\alpha, \beta)$.

## Sources

- Shreyas Singh, Zhuo Zhang and AJ Hildebrand, *An Elementary Characterization of the Gauss-Kuzmin Measure in the Theory of Continued Fractions*, INTEGERS 25 (2025), Article A89, Section 2.3.

Formalized by `MetaMathlibExt.fundInterval_of_lt`, a theorem declared in [WantedExt/NumberTheory/GaussKuzminSymmetryWanted.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/GaussKuzminSymmetryWanted.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/gauss-kuzmin-masses-of-continued-fraction-string/index.html#fund-interval-of-lt).

## Gauss–Kuzmin mass of a string

For a finite string $a$ of natural numbers with
fundamental interval $I(a)$, the Gauss–Kuzmin mass of $a$ is
$P_{GK}(a) = \frac{1}{\log 2} \int_{I(a)} \frac{dx}{1 + x}$, the measure of $I(a)$ under the
Gauss–Kuzmin measure with density $\frac{1}{(1 + x) \log 2}$.

## Sources

- Shreyas Singh, Zhuo Zhang and AJ Hildebrand, *An Elementary Characterization of the Gauss-Kuzmin Measure in the Theory of Continued Fractions*, INTEGERS 25 (2025), Article A89, equations (1.5) and (1.6).

Formalized by `MetaMathlibExt.gaussKuzminMass`, a definition declared in [WantedExt/NumberTheory/GaussKuzminSymmetryWanted.lean, line 91](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/GaussKuzminSymmetryWanted.lean#L91). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/gauss-kuzmin-masses-of-continued-fraction-string/index.html#gauss-kuzmin-mass).

## Gauss–Kuzmin mass of the empty string

The Gauss–Kuzmin mass of the empty string is
$P_{GK}(()) = \frac{1}{\log 2} \int_{[0, 1)} \frac{dx}{1 + x}$.

## Sources

- Shreyas Singh, Zhuo Zhang and AJ Hildebrand, *An Elementary Characterization of the Gauss-Kuzmin Measure in the Theory of Continued Fractions*, INTEGERS 25 (2025), Article A89, equation (1.6).

Formalized by `MetaMathlibExt.gaussKuzminMass_nil`, a theorem declared in [WantedExt/NumberTheory/GaussKuzminSymmetryWanted.lean, line 99](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/GaussKuzminSymmetryWanted.lean#L99). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/gauss-kuzmin-masses-of-continued-fraction-string/index.html#gauss-kuzmin-mass-nil).

## Characteristic number of a string

For a finite string $a$ of natural numbers with
convergent matrix $C(a) = \begin{pmatrix} p' & p \\ q' & q \end{pmatrix}$, the characteristic
number of $a$ is the integer $\chi(a) = (p + q)(q' + q)$.

## Sources

- Shreyas Singh, Zhuo Zhang and AJ Hildebrand, *An Elementary Characterization of the Gauss-Kuzmin Measure in the Theory of Continued Fractions*, INTEGERS 25 (2025), Article A89, Definition 5.1, equation (5.2).

Formalized by `MetaMathlibExt.characteristicNumber`, a definition declared in [WantedExt/NumberTheory/GaussKuzminSymmetryWanted.lean, line 108](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/GaussKuzminSymmetryWanted.lean#L108). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/gauss-kuzmin-masses-of-continued-fraction-string/index.html#characteristic-number).

## Characteristic number of the empty string

The characteristic number of the empty string
is $\chi(()) = 1$.

## Sources

- Shreyas Singh, Zhuo Zhang and AJ Hildebrand, *An Elementary Characterization of the Gauss-Kuzmin Measure in the Theory of Continued Fractions*, INTEGERS 25 (2025), Article A89, Definition 5.1.

Formalized by `MetaMathlibExt.characteristicNumber_nil`, a theorem declared in [WantedExt/NumberTheory/GaussKuzminSymmetryWanted.lean, line 117](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/GaussKuzminSymmetryWanted.lean#L117). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/gauss-kuzmin-masses-of-continued-fraction-string/index.html#characteristic-number-nil).

## Stable strings

For a finite string $a = (a_1, \dots, a_n)$ of natural numbers, let
$M(t) = \begin{pmatrix} 0 & 1 \\ 1 & t \end{pmatrix}$ and write the convergent matrix of $a$ as

$$C(a) = M(a_1) M(a_2) \cdots M(a_n) = \begin{pmatrix} p' & p \\ q' & q \end{pmatrix},$$

computed over the integers, with the empty product equal to the identity matrix. The string $a$ is
stable if $p = 2q'$.

## Sources

- Shreyas Singh, Zhuo Zhang and AJ Hildebrand, *An Elementary Characterization of the Gauss-Kuzmin Measure in the Theory of Continued Fractions*, INTEGERS 25 (2025), Article A89, Definition 5.4, equation (5.9).

Formalized by `MetaMathlibExt.IsStableString`, a definition declared in [WantedExt/NumberTheory/GaussKuzminSymmetryWanted.lean, line 125](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/GaussKuzminSymmetryWanted.lean#L125). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/gauss-kuzmin-masses-of-continued-fraction-string/index.html#is-stable-string).

## The empty string is stable

The empty string is a stable string.

Its convergent matrix is the identity matrix, so its top-right entry $p$ and its bottom-left entry
$q'$ are both $0$, and $p = 2q'$ holds.

## Sources

- Shreyas Singh, Zhuo Zhang and AJ Hildebrand, *An Elementary Characterization of the Gauss-Kuzmin Measure in the Theory of Continued Fractions*, INTEGERS 25 (2025), Article A89, Definition 5.4.

Formalized by `MetaMathlibExt.isStableString_nil`, a theorem declared in [WantedExt/NumberTheory/GaussKuzminSymmetryWanted.lean, line 133](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/GaussKuzminSymmetryWanted.lean#L133). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/gauss-kuzmin-masses-of-continued-fraction-string/index.html#is-stable-string-nil).

## Nontrivial symmetry of a string

A finite string $a$ of natural numbers has a nontrivial
symmetry if there is a string $b$ that is a rearrangement of $a$ (the same entries with the same
multiplicities, in some order) such that $b \ne a$, $b$ is not the reverse of $a$, and
$P_{GK}(b) = P_{GK}(a)$, where $P_{GK}$ denotes the Gauss–Kuzmin measure of a string.

## Sources

- Shreyas Singh, Zhuo Zhang and AJ Hildebrand, *An Elementary Characterization of the Gauss-Kuzmin Measure in the Theory of Continued Fractions*, INTEGERS 25 (2025), Article A89, Definition 1.4.

Formalized by `MetaMathlibExt.HasNontrivialSymmetry`, a definition declared in [WantedExt/NumberTheory/GaussKuzminSymmetryWanted.lean, line 142](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/GaussKuzminSymmetryWanted.lean#L142). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/gauss-kuzmin-masses-of-continued-fraction-string/index.html#has-nontrivial-symmetry).

## The empty string has no nontrivial symmetry

The empty string has no nontrivial symmetry.

## Sources

- Shreyas Singh, Zhuo Zhang and AJ Hildebrand, *An Elementary Characterization of the Gauss-Kuzmin Measure in the Theory of Continued Fractions*, INTEGERS 25 (2025), Article A89, Definition 1.4.

Formalized by `MetaMathlibExt.not_hasNontrivialSymmetry_nil`, a theorem declared in [WantedExt/NumberTheory/GaussKuzminSymmetryWanted.lean, line 150](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/GaussKuzminSymmetryWanted.lean#L150). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/gauss-kuzmin-masses-of-continued-fraction-string/index.html#not-has-nontrivial-symmetry-nil).

## Generalized Gauss–Kuzmin theorem

For a real number $x$, let $a_1(x), a_2(x), \dots$ be
the partial denominators of the continued fraction expansion of $x$. For almost every real $x$,
with respect to Lebesgue measure, the following holds: for every string $b = (b_1, \dots, b_n)$
of positive integers, the number of indices $i \in \{0, \dots, N - 1\}$ such that
$a_{i+j}(x) = b_j$ for all $j = 1, \dots, n$, divided by $N$, tends to the Gauss–Kuzmin measure
$P_{GK}(b)$ as $N \to \infty$.

## Sources

- Shreyas Singh, Zhuo Zhang and AJ Hildebrand, *An Elementary Characterization of the Gauss-Kuzmin Measure in the Theory of Continued Fractions*, INTEGERS 25 (2025), Article A89, Proposition 1.2, quoted from Iosifescu and Kraaikamp, Proposition 4.1.2.

Stated but not proved: `MetaMathlibExt.gaussKuzmin_string_frequency` is written with `theorem_wanted` in [WantedExt/NumberTheory/GaussKuzminSymmetryWanted.lean, line 162](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/GaussKuzminSymmetryWanted.lean#L162). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/gauss-kuzmin-masses-of-continued-fraction-string/index.html#gauss-kuzmin-string-frequency).

## Reversal symmetry of the Gauss–Kuzmin mass

For every string $a$ of positive integers,
$P_{GK}(\overleftarrow{a}) = P_{GK}(a)$, where $P_{GK}$ is the Gauss–Kuzmin mass and
$\overleftarrow{a}$ is the reverse of $a$.

## Sources

- Shreyas Singh, Zhuo Zhang and AJ Hildebrand, *An Elementary Characterization of the Gauss-Kuzmin Measure in the Theory of Continued Fractions*, INTEGERS 25 (2025), Article A89, Proposition 1.3, equations (1.8) and (1.9).

Stated but not proved: `MetaMathlibExt.gaussKuzminMass_reverse` is written with `theorem_wanted` in [WantedExt/NumberTheory/GaussKuzminSymmetryWanted.lean, line 175](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/GaussKuzminSymmetryWanted.lean#L175). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/gauss-kuzmin-masses-of-continued-fraction-string/index.html#gauss-kuzmin-mass-reverse).

## Reversal symmetry forces the Gauss–Kuzmin density

Let $f$ be a real function that is
continuous and nonnegative on $[0, 1]$ with $\int_0^1 f(x)\,dx = 1$, and let $S$ be an infinite
set of natural numbers. Write $I(a)$ for the fundamental interval of a string $a$ and
$\overleftarrow{a}$ for the reverse of $a$. If
$\int_{I(a)} f(x)\,dx = \int_{I(\overleftarrow{a})} f(x)\,dx$ for every string $a$ of positive
integers whose length lies in $S$, then $f(x) = \frac{1}{\log 2 \cdot (1 + x)}$ for every
$x \in [0, 1]$.

## Sources

- Shreyas Singh, Zhuo Zhang and AJ Hildebrand, *An Elementary Characterization of the Gauss-Kuzmin Measure in the Theory of Continued Fractions*, INTEGERS 25 (2025), Article A89, Theorem 1.

Stated but not proved: `MetaMathlibExt.density_eq_gaussKuzmin_of_reverse_symmetric` is written with `theorem_wanted` in [WantedExt/NumberTheory/GaussKuzminSymmetryWanted.lean, line 185](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/GaussKuzminSymmetryWanted.lean#L185). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/gauss-kuzmin-masses-of-continued-fraction-string/index.html#density-eq-gauss-kuzmin-of-reverse-symme).

## Symmetry up to a fixed length does not force the Gauss–Kuzmin density

Write $I(a)$ for
the fundamental interval of a string $a$ and $\overleftarrow{a}$ for the reverse of $a$. For every
integer $N \ge 1$ there is a real function $f$, continuous and nonnegative on $[0, 1]$ with
$\int_0^1 f(x)\,dx = 1$, such that $\int_{I(a)} f(x)\,dx = \int_{I(\overleftarrow{a})} f(x)\,dx$
for every string $a$ of positive integers of length at most $N$, but
$f(x) \ne \frac{1}{\log 2 \cdot (1 + x)}$ for some $x \in [0, 1]$.

## Sources

- Shreyas Singh, Zhuo Zhang and AJ Hildebrand, *An Elementary Characterization of the Gauss-Kuzmin Measure in the Theory of Continued Fractions*, INTEGERS 25 (2025), Article A89, Theorem 2.

Stated but not proved: `MetaMathlibExt.exists_reverse_symmetric_density_ne_gaussKuzmin` is written with `theorem_wanted` in [WantedExt/NumberTheory/GaussKuzminSymmetryWanted.lean, line 199](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/GaussKuzminSymmetryWanted.lean#L199). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/gauss-kuzmin-masses-of-continued-fraction-string/index.html#exists-reverse-symmetric-density-ne-gaus).

## Convergent matrices of reversed and extended strings

Let $a = (a_1, \ldots, a_n)$ be a
finite string of positive integers with convergent matrix
$C(a) = \begin{pmatrix} p' & p \\ q' & q \end{pmatrix}$, let $t \ge 1$ be an integer, and write
$\overleftarrow{a} = (a_n, \ldots, a_1)$ for the reversed string. Then
(i) $C(\overleftarrow{a}) = \begin{pmatrix} p' & q' \\ p & q \end{pmatrix}$;
(ii) $C(a_1, \ldots, a_n, t) = \begin{pmatrix} p & p' + tp \\ q & q' + tq \end{pmatrix}$;
(iii) $C(t, a_1, \ldots, a_n) = \begin{pmatrix} q' & q \\ p' + tq' & p + tq \end{pmatrix}$;
(iv) $C(t, a_n, \ldots, a_1) = \begin{pmatrix} p & q \\ p' + tp & q' + tq \end{pmatrix}$.

## Sources

- Shreyas Singh, Zhuo Zhang and AJ Hildebrand, *An Elementary Characterization of the Gauss-Kuzmin Measure in the Theory of Continued Fractions*, INTEGERS 25 (2025), Article A89, Lemma 2.2.

Stated but not proved: `MetaMathlibExt.convergentMatrix_reverse_append_cons` is written with `theorem_wanted` in [WantedExt/NumberTheory/GaussKuzminSymmetryWanted.lean, line 213](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/GaussKuzminSymmetryWanted.lean#L213). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/gauss-kuzmin-masses-of-continued-fraction-string/index.html#convergent-matrix-reverse-append-cons).

## Fundamental intervals of reversed and extended strings

Let $a = (a_1, \ldots, a_n)$ be a
finite string of positive integers with convergent matrix
$C(a) = \begin{pmatrix} p' & p \\ q' & q \end{pmatrix}$, let $t \ge 1$ be an integer, write
$\overleftarrow{a} = (a_n, \ldots, a_1)$ for the reversed string, and for real numbers $x$ and $y$
let $\langle x, y \rangle$ be $[x, y)$ if $x < y$ and $(y, x]$ otherwise. Write $I(b)$ for the
fundamental interval of a string $b$, and set $u = (p' + tp)/(q' + tq)$, $v = q/(p + tq)$ and
$w = q/(q' + tq)$. Then each of the following equalities holds up to a set of Lebesgue measure
zero:
(i) $I(\overleftarrow{a}) = \langle q'/q, \; q'/q + (-1)^n / (q(p + q)) \rangle$;
(ii) $I(a_1, \ldots, a_n, t) = \langle u, \; u + (-1)^{n+1} / ((q' + tq)(q' + (t + 1)q)) \rangle$;
(iii) $I(t, a_1, \ldots, a_n) = \langle v, \; v + (-1)^{n+1} / ((p + tq)(p' + p + t(q' + q)))
\rangle$;
(iv) $I(t, a_n, \ldots, a_1) = \langle w, \; w + (-1)^{n+1} / ((q' + tq)(p' + q' + t(p + q)))
\rangle$.

## Sources

- Shreyas Singh, Zhuo Zhang and AJ Hildebrand, *An Elementary Characterization of the Gauss-Kuzmin Measure in the Theory of Continued Fractions*, INTEGERS 25 (2025), Article A89, Lemma 2.4.

Stated but not proved: `MetaMathlibExt.cfCylinder_reverse_append_cons_ae_eq` is written with `theorem_wanted` in [WantedExt/NumberTheory/GaussKuzminSymmetryWanted.lean, line 237](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/GaussKuzminSymmetryWanted.lean#L237). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/gauss-kuzmin-masses-of-continued-fraction-string/index.html#cf-cylinder-reverse-append-cons-ae-eq).

## Explicit Gauss–Kuzmin mass of a string

Let $a$ be a string of $n$ positive integers, let
$p$, $q'$ and $q$ be the upper-right, lower-left and lower-right entries of its convergent matrix
$C(a)$, and let $\overleftarrow{a}$ be the reverse of $a$. Then the Gauss–Kuzmin masses satisfy
$P_{GK}(a) = P_{GK}(\overleftarrow{a})$ and
$P_{GK}(a) = \left|\log_2\left(1 + \frac{(-1)^n}{(p + q)(q' + q)}\right)\right|$.

## Sources

- Shreyas Singh, Zhuo Zhang and AJ Hildebrand, *An Elementary Characterization of the Gauss-Kuzmin Measure in the Theory of Continued Fractions*, INTEGERS 25 (2025), Article A89, Lemma 2.5, equation (2.13).

Stated but not proved: `MetaMathlibExt.gaussKuzminMass_eq_abs_logb` is written with `theorem_wanted` in [WantedExt/NumberTheory/GaussKuzminSymmetryWanted.lean, line 276](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/GaussKuzminSymmetryWanted.lean#L276). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/gauss-kuzmin-masses-of-continued-fraction-string/index.html#gauss-kuzmin-mass-eq-abs-logb).

## Symmetric one-digit extensions fix the density at a rational point

Let $f$ be a real
function that is continuous and nonnegative on $[0, 1]$ with $\int_0^1 f(x)\,dx = 1$. Let
$a = (a_1, \dots, a_n)$ be a string of positive integers, let $p$ and $q$ be the upper-right and
lower-right entries of its convergent matrix $C(a)$, so that $p/q = [0; a_1, \dots, a_n]$, and let
$\overleftarrow{a}$ be the reverse of $a$. Write $I(b)$ for the fundamental interval of a string
$b$, $(a, t)$ for $a$ followed by $t$, and $(t, \overleftarrow{a})$ for $t$ followed by
$\overleftarrow{a}$. If $\int_{I(a, t)} f(x)\,dx = \int_{I(t, \overleftarrow{a})} f(x)\,dx$ for
every integer $t \ge 1$, then $f(p/q) = f(0)/(1 + p/q)$.

## Sources

- Shreyas Singh, Zhuo Zhang and AJ Hildebrand, *An Elementary Characterization of the Gauss-Kuzmin Measure in the Theory of Continued Fractions*, INTEGERS 25 (2025), Article A89, Lemma 3.1.

Stated but not proved: `MetaMathlibExt.density_cfValue_eq_of_append_symmetric` is written with `theorem_wanted` in [WantedExt/NumberTheory/GaussKuzminSymmetryWanted.lean, line 288](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/GaussKuzminSymmetryWanted.lean#L288). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/gauss-kuzmin-masses-of-continued-fraction-string/index.html#density-cf-value-eq-of-append-symmetric).

## Reversal symmetry from agreement with the Gauss–Kuzmin measure

Let $\mu$ be a probability
measure on $\mathbb{R}$ and let $N \ge 1$. For a string $a$ of positive integers write $I(a)$ for
its fundamental interval, $P_{GK}(a)$ for its Gauss–Kuzmin measure and $a^{\mathrm{rev}}$ for its
reverse. If $\mu(I(a)) = P_{GK}(a)$ for every string $a$ of exactly $N$ positive integers, then
$\mu(I(a)) = \mu(I(a^{\mathrm{rev}}))$ for every string $a$ of at most $N$ positive integers.

## Sources

- Shreyas Singh, Zhuo Zhang and AJ Hildebrand, *An Elementary Characterization of the Gauss-Kuzmin Measure in the Theory of Continued Fractions*, INTEGERS 25 (2025), Article A89, Lemma 4.1.

Stated but not proved: `MetaMathlibExt.reverse_symmetric_of_eq_gaussKuzmin_at_length` is written with `theorem_wanted` in [WantedExt/NumberTheory/GaussKuzminSymmetryWanted.lean, line 302](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/GaussKuzminSymmetryWanted.lean#L302). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/gauss-kuzmin-masses-of-continued-fraction-string/index.html#reverse-symmetric-of-eq-gauss-kuzmin-at).

## Gauss–Kuzmin masses agree exactly when characteristic numbers do

Write $P_{GK}$ for the
Gauss–Kuzmin mass and $\chi$ for the characteristic number of a string. If $a$ and $b$ are strings
of positive integers whose lengths have the same parity, then $P_{GK}(a) = P_{GK}(b)$ if and only
if $\chi(a) = \chi(b)$.

## Sources

- Shreyas Singh, Zhuo Zhang and AJ Hildebrand, *An Elementary Characterization of the Gauss-Kuzmin Measure in the Theory of Continued Fractions*, INTEGERS 25 (2025), Article A89, Lemma 5.2.

Stated but not proved: `MetaMathlibExt.gaussKuzminMass_eq_iff_characteristicNumber_eq` is written with `theorem_wanted` in [WantedExt/NumberTheory/GaussKuzminSymmetryWanted.lean, line 314](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/GaussKuzminSymmetryWanted.lean#L314). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/gauss-kuzmin-masses-of-continued-fraction-string/index.html#gauss-kuzmin-mass-eq-iff-characteristic).

## Swapping the first two of three digits changes the characteristic number

For positive
integers $a$, $b$, $c$ with $a \ne b$, the strings $(a, b, c)$ and $(b, a, c)$ have different
characteristic numbers: $\chi(a, b, c) \ne \chi(b, a, c)$.

## Sources

- Shreyas Singh, Zhuo Zhang and AJ Hildebrand, *An Elementary Characterization of the Gauss-Kuzmin Measure in the Theory of Continued Fractions*, INTEGERS 25 (2025), Article A89, Lemma 5.3.

Stated but not proved: `MetaMathlibExt.characteristicNumber_swap_ne` is written with `theorem_wanted` in [WantedExt/NumberTheory/GaussKuzminSymmetryWanted.lean, line 323](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/GaussKuzminSymmetryWanted.lean#L323). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/gauss-kuzmin-masses-of-continued-fraction-string/index.html#characteristic-number-swap-ne).

## Families of stable strings

(i) For every positive integer $t$, the strings $(t, 2t)$ and
$(t, 1, 2t + 1)$ are stable. (ii) If $a = (a_1, \dots, a_m)$ is a stable string of positive
integers, then for every positive integer $t$ the string $(t, a_m, \dots, a_1, 2t)$, obtained from
the reverse of $a$ by adding $t$ at the front and $2t$ at the end, is stable. (iii) For every
$n \ge 2$ there are infinitely many stable strings of $n$ positive integers.

## Sources

- Shreyas Singh, Zhuo Zhang and AJ Hildebrand, *An Elementary Characterization of the Gauss-Kuzmin Measure in the Theory of Continued Fractions*, INTEGERS 25 (2025), Article A89, Lemma 5.5.

Stated but not proved: `MetaMathlibExt.isStableString_families` is written with `theorem_wanted` in [WantedExt/NumberTheory/GaussKuzminSymmetryWanted.lean, line 334](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/GaussKuzminSymmetryWanted.lean#L334). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/gauss-kuzmin-masses-of-continued-fraction-string/index.html#is-stable-string-families).

## Nontrivial symmetries from stable strings

Let $n \ge 1$ and let $a = (a_1, \dots, a_n)$ be
a stable string of positive integers. Put $a^+ = (2, 1, a_1, \dots, a_{n-1}, a_n + 1)$ and
$\sigma(a^+) = (2, a_n + 1, a_{n-1}, \dots, a_1, 1)$. Then $\sigma(a^+)$ is a rearrangement of
$a^+$, it differs both from $a^+$ and from the reverse of $a^+$, and
$P_{GK}(\sigma(a^+)) = P_{GK}(a^+)$, where $P_{GK}$ denotes the Gauss–Kuzmin measure of a string.

## Sources

- Shreyas Singh, Zhuo Zhang and AJ Hildebrand, *An Elementary Characterization of the Gauss-Kuzmin Measure in the Theory of Continued Fractions*, INTEGERS 25 (2025), Article A89, Lemma 5.7, equations (5.12) and (5.13).

Stated but not proved: `MetaMathlibExt.stable_plus_nontrivial_symmetry` is written with `theorem_wanted` in [WantedExt/NumberTheory/GaussKuzminSymmetryWanted.lean, line 348](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/GaussKuzminSymmetryWanted.lean#L348). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/gauss-kuzmin-masses-of-continued-fraction-string/index.html#stable-plus-nontrivial-symmetry).

## No nontrivial symmetries in length three, infinitely many from length four

(i) No string
of three positive integers has a nontrivial symmetry. (ii) For every $n \ge 4$ there are infinitely
many strings of $n$ positive integers that have a nontrivial symmetry.

## Sources

- Shreyas Singh, Zhuo Zhang and AJ Hildebrand, *An Elementary Characterization of the Gauss-Kuzmin Measure in the Theory of Continued Fractions*, INTEGERS 25 (2025), Article A89, Theorem 3.

Stated but not proved: `MetaMathlibExt.nontrivialSymmetry_length_three_and_infinite` is written with `theorem_wanted` in [WantedExt/NumberTheory/GaussKuzminSymmetryWanted.lean, line 361](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/GaussKuzminSymmetryWanted.lean#L361). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/gauss-kuzmin-masses-of-continued-fraction-string/index.html#nontrivial-symmetry-length-three-and-inf).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Gauss–Kuzmin masses of continued fraction strings](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/continued-fractions-expansions/part-01/gauss-kuzmin-masses-of-continued-fraction-string/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/continued-fractions-expansions/part-01/gauss-kuzmin-masses-of-continued-fraction-string)
