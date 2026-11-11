---
declaration: section
origin: cited
lean: MetaMathlibExt.nicomacheanNu, MetaMathlibExt.nicomacheanNu_examples, MetaMathlibExt.nicomacheanAlpha, MetaMathlibExt.nicomacheanAlpha_one_two_three, MetaMathlibExt.nicomachean_bagSquare_root_secondDifference_tendsto, MetaMathlibExt.exists_pos_rat_nicomacheanNu_eq_zero_large_den, MetaMathlibExt.exists_two_valued_nicomachean_large_gap, MetaMathlibExt.nicomachean_run_repeat_generatingFunctions
statement: formalized
---

# Nicomachus's theorem and its generalizations

29 results, 14 proved and 15 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/waring-figurate/nicomachus-s-theorem-and-its-generalizations/index.html).

## Nicomachean defect

For a finite sequence $\sigma = (a_1, \ldots, a_n)$ of elements of a
commutative ring, the Nicomachean defect of $\sigma$ is
$\nu(\sigma) = \left(\sum_{i=1}^n a_i\right)^2 - \sum_{i=1}^n a_i^3$.

## Sources

- Seon-Hong Kim and Kenneth B. Stolarsky, *Translations and Extensions of the Nicomachean Identity*, Journal of Integer Sequences 27 (2024), Article 24.6.3, Section 1.

Formalized by `MetaMathlibExt.nicomacheanNu`, a definition declared in [WantedExt/NumberTheory/NicomacheanTranslationsWanted.lean, line 39](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/NicomacheanTranslationsWanted.lean#L39). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/waring-figurate/nicomachus-s-theorem-and-its-generalizations/index.html#nicomachean-nu).

## Examples of the Nicomachean defect

For the Nicomachean defect $\nu$ of a sequence of
integers, $\nu(1, 2, 3, 4) = 0$, $\nu(1, 2) = 0$, $\nu(3, 3, 3) = 0$,
$\nu(1, 2, 2, 3, 4, 5, 6, 8) = 0$ and $\nu(1, 2, 2, 3, 4, 6, 6, 8) = -28$.

The last two are the values at $x = 5$ and $x = 6$ of the paper's identity
$\nu(1, 2, 2, 3, 4, x, 6, 8) = (5 - x)(x - 4)(8 + x)$; the identity itself is not stated here.

## Sources

- Seon-Hong Kim and Kenneth B. Stolarsky, *Translations and Extensions of the Nicomachean Identity*, Journal of Integer Sequences 27 (2024), Article 24.6.3, Section 1.

Formalized by `MetaMathlibExt.nicomacheanNu_examples`, a theorem declared in [WantedExt/NumberTheory/NicomacheanTranslationsWanted.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/NicomacheanTranslationsWanted.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/waring-figurate/nicomachus-s-theorem-and-its-generalizations/index.html#nicomachean-nu-examples).

## The Nicomachean progression factor

For rational numbers $n$, $s$ and $a$, define

$$\alpha(n, s, a) = 2n^2 + na - a^2 + \frac{n(n-1)(s - s^2)}{2} - (n-1)as.$$

This is the second factor of $\nu(S_m)$, where
$\nu(a_1, \dots, a_k) = (a_1 + \dots + a_k)^2 - (a_1^3 + \dots + a_k^3)$ is the Nicomachean defect,
$S = (a, a + s, \dots, a + (n-1)s)$, and $S_m$ joins $n$ copies of $n$ with the translated
progressions $S, S + n, \dots, S + mn$.

## Sources

- Seon-Hong Kim and Kenneth B. Stolarsky, *Translations and Extensions of the Nicomachean Identity*, Journal of Integer Sequences 27 (2024), Article 24.6.3, Section 6, equation (nusm).

Formalized by `MetaMathlibExt.nicomacheanAlpha`, a definition declared in [WantedExt/NumberTheory/NicomacheanTranslationsWanted.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/NicomacheanTranslationsWanted.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/waring-figurate/nicomachus-s-theorem-and-its-generalizations/index.html#nicomachean-alpha).

## Specializations of the Nicomachean factor at $s = 1, 2, 3$

Let
$\alpha(n, s, a) = 2n^2 + na - a^2 + n(n-1)(s - s^2)/2 - (n-1)as$. For all rational numbers $n$
and $a$, $\alpha(n, 1, a) = 2n^2 + a - a^2$, $\alpha(n, 2, a) = n^2 + (1 - a)n - a^2 + 2a$ and
$\alpha(n, 3, a) = -(a + n - 3)(a + n)$.

## Sources

- Seon-Hong Kim and Kenneth B. Stolarsky, *Translations and Extensions of the Nicomachean Identity*, Journal of Integer Sequences 27 (2024), Article 24.6.3, Section 6.

Formalized by `MetaMathlibExt.nicomacheanAlpha_one_two_three`, a theorem declared in [WantedExt/NumberTheory/NicomacheanTranslationsWanted.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/NicomacheanTranslationsWanted.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/waring-figurate/nicomachus-s-theorem-and-its-generalizations/index.html#nicomachean-alpha-one-two-three).

## Second differences of roots of translated Nicomachean bag squares

Write
$\nu(a_1, \dots, a_k) = (a_1 + \dots + a_k)^2 - (a_1^3 + \dots + a_k^3)$ for the Nicomachean defect
of a finite sequence. For natural numbers $m$ let

$$t(m) = \frac{3(m^2 - 6m - 3) + \sqrt{3(m-1)^2(35m^2 + 34m + 11)}}{24},$$



$$s(m) = \frac{3(m^2 - 6m - 3) - \sqrt{3(m-1)^2(35m^2 + 34m + 11)}}{24},$$

let $A_m^2$ be the sequence of the $m^2$ products $ij$ with $1 \le i, j \le m$ (the bag square of
$(1, 2, \dots, m)$), let $A_m^2 + x$ be the sequence obtained by adding $x$ to every entry, and let
$\rho(m)$ be the supremum of the set of real $x$ with $\nu(A_m^2 + x) = 0$. Then, as $m \to \infty$,
the second differences $t(m+2) - 2t(m+1) + t(m)$ and $\rho(m+2) - 2\rho(m+1) + \rho(m)$ converge
to $(3 + \sqrt{105})/12$, and $s(m+2) - 2s(m+1) + s(m)$ converges to $(3 - \sqrt{105})/12$.

For $m \ge 1$, $\nu(A_m^2 + x)$ is a cubic polynomial in $x$ with leading coefficient $-m^2$, so
$\rho(m)$ is its largest real root.

## Sources

- Seon-Hong Kim and Kenneth B. Stolarsky, *Translations and Extensions of the Nicomachean Identity*, Journal of Integer Sequences 27 (2024), Article 24.6.3, Proposition 1 (`jis-2024-24.6.3-prop-1`).

Stated but not proved: `MetaMathlibExt.nicomachean_bagSquare_root_secondDifference_tendsto` is written with `theorem_wanted` in [WantedExt/NumberTheory/NicomacheanTranslationsWanted.lean, line 85](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/NicomacheanTranslationsWanted.lean#L85). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/waring-figurate/nicomachus-s-theorem-and-its-generalizations/index.html#nicomachean-bag-square-root-second-diffe).

## Nicomachean sequences of rationals with large denominators

Write
$\nu(a_1, \dots, a_n) = (a_1 + \dots + a_n)^2 - (a_1^3 + \dots + a_n^3)$ for the Nicomachean defect
of a finite sequence. For every natural number $Q$ there is a finite sequence $\sigma$ of positive
rational numbers with $\nu(\sigma) = 0$ having an entry whose denominator in lowest terms is
greater than $Q$.

## Sources

- Seon-Hong Kim and Kenneth B. Stolarsky, *Translations and Extensions of the Nicomachean Identity*, Journal of Integer Sequences 27 (2024), Article 24.6.3, Proposition 3 (`jis-2024-24.6.3-prop-3`).

Stated but not proved: `MetaMathlibExt.exists_pos_rat_nicomacheanNu_eq_zero_large_den` is written with `theorem_wanted` in [WantedExt/NumberTheory/NicomacheanTranslationsWanted.lean, line 104](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/NicomacheanTranslationsWanted.lean#L104). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/waring-figurate/nicomachus-s-theorem-and-its-generalizations/index.html#exists-pos-rat-nicomachean-nu-eq-zero-la).

## Two-valued Nicomachean sequences with a large gap

Write
$\nu(a_1, \dots, a_n) = (a_1 + \dots + a_n)^2 - (a_1^3 + \dots + a_n^3)$ for the Nicomachean defect
of a finite sequence. For every real $\varepsilon > 0$ there are integers $0 < a < b$ and a finite
sequence $\sigma$ whose entries all equal $a$ or $b$, in which both $a$ and $b$ occur, such that
$\nu(\sigma) = 0$ and $(b - a)/L > 1 - \varepsilon$, where $L$ is the length of $\sigma$.

## Sources

- Seon-Hong Kim and Kenneth B. Stolarsky, *Translations and Extensions of the Nicomachean Identity*, Journal of Integer Sequences 27 (2024), Article 24.6.3, Proposition 4 (`jis-2024-24.6.3-prop-4`).

Stated but not proved: `MetaMathlibExt.exists_two_valued_nicomachean_large_gap` is written with `theorem_wanted` in [WantedExt/NumberTheory/NicomacheanTranslationsWanted.lean, line 113](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/NicomacheanTranslationsWanted.lean#L113). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/waring-figurate/nicomachus-s-theorem-and-its-generalizations/index.html#exists-two-valued-nicomachean-large-gap).

## Generating functions for run-and-repeat Nicomachean sequences

For integers $j, m \ge 1$
let $\sigma(j, m)$ be the integer sequence $(1, 2, \ldots, j + 1, m, \ldots, m)$ in which $m$ is
repeated $2j$ times, and let $\nu$ denote the Nicomachean defect. Call $j \ge 1$ admissible if
$\nu(\sigma(j, m)) = 0$ for some integer $m \ge 1$, let $j_k$ be the $k$-th smallest admissible
integer (counting from $k = 0$), and let $m_k = j_k + \lfloor \sqrt{2j_k^2 + 3j_k + 2} \rfloor$.
Then $\nu(\sigma(j_k, m_k)) = 0$ for every $k$, and in the ring of formal power series over
$\mathbb{Z}$

$$
(X - 1)(1 - 6X + X^2)(1 + 6X + X^2) \sum_{k \ge 0} j_k X^k = X^4 + X^3 - 19X^2 - 5X - 2
$$

and

$$
(1 - X)(1 - 6X + X^2)(1 + 6X + X^2) \sum_{k \ge 0} m_k X^k = 6(1 + X)^2.
$$

For admissible $j$ the square root is an integer and $m = j + \sqrt{2j^2 + 3j + 2}$ is the
positive root of $\nu(\sigma(j, m)) = 0$ in $m$, so these say that $(j_k)$ and $(m_k)$ have the
generating functions $(x^4 + x^3 - 19x^2 - 5x - 2)/((x - 1)(1 - 6x + x^2)(1 + 6x + x^2))$ and
$6(1 + x)^2/((1 - x)(1 - 6x + x^2)(1 + 6x + x^2))$.

## Sources

- Seon-Hong Kim and Kenneth B. Stolarsky, *Translations and Extensions of the Nicomachean Identity*, Journal of Integer Sequences 27 (2024), Article 24.6.3, Proposition 5 (`jis-2024-24.6.3-prop-5`).

Stated but not proved: `MetaMathlibExt.nicomachean_run_repeat_generatingFunctions` is written with `theorem_wanted` in [WantedExt/NumberTheory/NicomacheanTranslationsWanted.lean, line 126](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/NicomacheanTranslationsWanted.lean#L126). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/waring-figurate/nicomachus-s-theorem-and-its-generalizations/index.html#nicomachean-run-repeat-generating-functi).

## Nicomachean sequences with a large gap at the top

Write
$\nu(a_1, \dots, a_n) = (a_1 + \dots + a_n)^2 - (a_1^3 + \dots + a_n^3)$ for the Nicomachean defect
of a finite sequence. For every natural number $G$ there is a finite sequence $\sigma$ of
positive integers with $\nu(\sigma) = 0$ and entries $a < b$ of $\sigma$ such that $b$ is the
largest entry of $\sigma$ and occurs exactly once, every entry other than $b$ is at most $a$, and
$b - a > G$.

## Sources

- Seon-Hong Kim and Kenneth B. Stolarsky, *Translations and Extensions of the Nicomachean Identity*, Journal of Integer Sequences 27 (2024), Article 24.6.3, Proposition 6 (`jis-2024-24.6.3-prop-6`).

Stated but not proved: `MetaMathlibExt.exists_nicomachean_large_top_gap` is written with `theorem_wanted` in [WantedExt/NumberTheory/NicomacheanTranslationsWanted.lean, line 146](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/NicomacheanTranslationsWanted.lean#L146). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/waring-figurate/nicomachus-s-theorem-and-its-generalizations/index.html#exists-nicomachean-large-top-gap).

## Golden-ratio sequences with vanishing Nicomachean defect

Let $\varphi = (1 + \sqrt 5)/2$
be the golden ratio and write
$\nu(a_1, \dots, a_k) = (a_1 + \dots + a_k)^2 - (a_1^3 + \dots + a_k^3)$ for the Nicomachean defect
of a finite sequence of real numbers. For every natural number $N$ there is a finite sequence
$\sigma$ of positive real numbers, each of the form $p + q\varphi$ with $p, q \in \mathbb{Z}$, such
that $\nu(\sigma) = 0$, $\sigma$ contains $\varphi^{-n}$ for every $1 \le n \le N$, and $\sigma$ has
a subsequence of irrational entries whose length is more than half the length of $\sigma$.

## Sources

- Seon-Hong Kim and Kenneth B. Stolarsky, *Translations and Extensions of the Nicomachean Identity*, Journal of Integer Sequences 27 (2024), Article 24.6.3, Proposition 7 (`jis-2024-24.6.3-prop-7`).

Stated but not proved: `MetaMathlibExt.exists_goldenRatio_nicomachean_sequence` is written with `theorem_wanted` in [WantedExt/NumberTheory/NicomacheanTranslationsWanted.lean, line 158](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/NicomacheanTranslationsWanted.lean#L158). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/waring-figurate/nicomachus-s-theorem-and-its-generalizations/index.html#exists-golden-ratio-nicomachean-sequence).

## Adjoined Nicomachean sequences are eventually arithmetic progressions

Write
$\nu(a_1, \dots, a_n) = (a_1 + \dots + a_n)^2 - (a_1^3 + \dots + a_n^3)$ for the Nicomachean defect
of a finite sequence. Let $(a_1, \dots, a_n)$ be a finite, possibly empty, sequence of real numbers
and let $x_1, x_2, x_3, \dots$ be nonzero real numbers with $x_{j+1} \ne -x_j$ for every $j \ge 1$.
If $\nu(a_1, \dots, a_n, x_1, \dots, x_l) = 0$ for every $l \ge 1$, then $x_{j+1} = x_j + 1$ for
every $j \ge 2$; that is, $x_2, x_3, \dots$ is an arithmetic progression with difference $1$.

## Sources

- Seon-Hong Kim and Kenneth B. Stolarsky, *Translations and Extensions of the Nicomachean Identity*, Journal of Integer Sequences 27 (2024), Article 24.6.3, Proposition 8 (`jis-2024-24.6.3-prop-8`).

Stated but not proved: `MetaMathlibExt.nicomachean_adjoined_arithmeticProgression` is written with `theorem_wanted` in [WantedExt/NumberTheory/NicomacheanTranslationsWanted.lean, line 171](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/NicomacheanTranslationsWanted.lean#L171). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/waring-figurate/nicomachus-s-theorem-and-its-generalizations/index.html#nicomachean-adjoined-arithmetic-progress).

## Positive integer roots of the Nicomachean factor for $s = 1, 2$

Let
$\alpha(n, s, a) = 2n^2 + na - a^2 + n(n-1)(s - s^2)/2 - (n-1)as$ and let $F_0 = 0$, $F_1 = 1$,
$F_{k+2} = F_{k+1} + F_k$ be the Fibonacci numbers. Let $n \ge 1$ be a natural number. Then
$\alpha(n, 1, h) = 0$ for some positive integer $h$ if and only if $2n^2 = k(k+1)$ for some natural
number $k$, that is, $n^2$ is a triangular number; $\alpha(n, 2, h) = 0$ for some positive integer
$h$ if and only if $n = F_{2k}$ for some $k \ge 1$; and if $n = F_{2k}$ with $k \ge 1$, then every
positive integer $h$ with $\alpha(n, 2, h) = 0$ equals $F_{2k-1} + 1$.

By the factor theorem, $\alpha(n, s, h) = 0$ says that $a - h$ divides $\alpha(n, s, a)$ as a
polynomial in $a$. The case $n = 0$ is excluded: $\alpha(0, 2, a)$ has the root $2$.

## Sources

- Seon-Hong Kim and Kenneth B. Stolarsky, *Translations and Extensions of the Nicomachean Identity*, Journal of Integer Sequences 27 (2024), Article 24.6.3, Proposition 9 (`jis-2024-24.6.3-prop-9`).

Stated but not proved: `MetaMathlibExt.nicomacheanAlpha_posIntRoot_iff` is written with `theorem_wanted` in [WantedExt/NumberTheory/NicomacheanTranslationsWanted.lean, line 185](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/NicomacheanTranslationsWanted.lean#L185). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/waring-figurate/nicomachus-s-theorem-and-its-generalizations/index.html#nicomachean-alpha-pos-int-root-iff).

## Nicomachean families sharing a quadratic factor

Write
$\nu(a_1, \dots, a_n) = (a_1 + \dots + a_n)^2 - (a_1^3 + \dots + a_n^3)$ for the Nicomachean defect
of a finite sequence. For every natural number $N$ there are finite sequences
$\sigma_1, \dots, \sigma_N$ of positive integers, pairwise distinct as multisets, and an integer
$c$ such that for every $i$ we have $\nu(\sigma_i) = 0$ and, for all integers $a$ and $b$, the
sequence $(\sigma_i, a, b)$ obtained by appending $a$ and $b$ to $\sigma_i$ satisfies
$\nu(\sigma_i, a, b) = -(a + b)(a^2 - ab + b^2 - a - b - 2c)$.

Since $\nu(\sigma_i) = 0$, the identity forces $c$ to be the sum of the entries of every
$\sigma_i$. Positivity of the entries, the paper's setting, excludes trivial families such as
$(k, -k, 1)$.

## Sources

- Seon-Hong Kim and Kenneth B. Stolarsky, *Translations and Extensions of the Nicomachean Identity*, Journal of Integer Sequences 27 (2024), Article 24.6.3, Proposition 12 (`jis-2024-24.6.3-prop-12`).

Stated but not proved: `MetaMathlibExt.exists_nicomachean_family_same_quadratic_factor` is written with `theorem_wanted` in [WantedExt/NumberTheory/NicomacheanTranslationsWanted.lean, line 199](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/NicomacheanTranslationsWanted.lean#L199). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/waring-figurate/nicomachus-s-theorem-and-its-generalizations/index.html#exists-nicomachean-family-same-quadratic).

## Triangular numbers as reals

For a natural number $m$, $T_m = m(m+1)/2$ is the $m$-th
triangular number, viewed as a real number.

Formalized by `MathlibExt.NumberTheory.NicomachusGeneralizationWanted.nicomachusTriangular`, a definition declared in [WantedExt/NumberTheory/NicomachusGeneralizationWanted.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/NicomachusGeneralizationWanted.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/waring-figurate/nicomachus-s-theorem-and-its-generalizations/index.html#nicomachus-triangular).

## The odd-case cube sum $L_{m,o}$

For a natural number $m$ and a real number $x$,

$$L_{m,o}(x) = \sum_{j=1}^{m} (2j - 1)^3 + x^3 +
\sum_{j=2}^{m} \bigl((2j - 2) + (j - 1)x\bigr)^3.$$

Formalized by `MathlibExt.NumberTheory.NicomachusGeneralizationWanted.nicomachusLOdd`, a definition declared in [WantedExt/NumberTheory/NicomachusGeneralizationWanted.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/NicomachusGeneralizationWanted.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/waring-figurate/nicomachus-s-theorem-and-its-generalizations/index.html#nicomachus-lodd).

## The odd-case square $R_{m,o}(x)$

For a natural number $m$ and a real number $x$,

$$R_{m,o}(x) = \bigl(T_{2m-1} + (1 + T_{m-1})\,x\bigr)^2,$$

where $T_n = n(n+1)/2$ is the $n$-th triangular number (for $m = 0$ the indices $2m - 1$ and
$m - 1$ are read as $0$).

Formalized by `MathlibExt.NumberTheory.NicomachusGeneralizationWanted.nicomachusROdd`, a definition declared in [WantedExt/NumberTheory/NicomachusGeneralizationWanted.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/NicomachusGeneralizationWanted.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/waring-figurate/nicomachus-s-theorem-and-its-generalizations/index.html#nicomachus-rodd).

## The odd-case polynomial $P_{m,o}$

For a natural number $m$ and a real number $x$,

$$P_{m,o}(x) = \sum_{j=0}^{m} (4j + 1 + jx) \bigl((j + 1)(j - 2) + j^2 x\bigr).$$

Formalized by `MathlibExt.NumberTheory.NicomachusGeneralizationWanted.nicomachusPOdd`, a definition declared in [WantedExt/NumberTheory/NicomachusGeneralizationWanted.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/NicomachusGeneralizationWanted.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/waring-figurate/nicomachus-s-theorem-and-its-generalizations/index.html#nicomachus-podd).

## The even-case cube sum $L_{m,e}$

For a natural number $m$ and a real number $x$,

$$L_{m,e}(x) = \sum_{j=1}^{m} (2j - 1)^3 + x^3 + \sum_{j=1}^{m} (2j + jx)^3.$$

Formalized by `MathlibExt.NumberTheory.NicomachusGeneralizationWanted.nicomachusLEven`, a definition declared in [WantedExt/NumberTheory/NicomachusGeneralizationWanted.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/NicomachusGeneralizationWanted.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/waring-figurate/nicomachus-s-theorem-and-its-generalizations/index.html#nicomachus-leven).

## The even-case square $R_{m,e}$

For a natural number $m$ and a real number $x$,

$$R_{m,e}(x) = \bigl(T_{2m} + (1 + T_m)\,x\bigr)^2,$$

where $T_n = n(n+1)/2$ is the $n$-th triangular number.

Formalized by `MathlibExt.NumberTheory.NicomachusGeneralizationWanted.nicomachusREven`, a definition declared in [WantedExt/NumberTheory/NicomachusGeneralizationWanted.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/NicomachusGeneralizationWanted.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/waring-figurate/nicomachus-s-theorem-and-its-generalizations/index.html#nicomachus-reven).

## Faulhaber expansion of the odd-case polynomial

For real numbers $m$ and $x$, let

$$\widetilde{P}(m, x) = -2(m + 1) - (9 + 2x) \, \frac{m(m+1)}{2} - 3 \cdot \frac{m(m+1)(2m+1)}{6} +
(4 + 5x + x^2) \left(\frac{m(m+1)}{2}\right)^2.$$

This is the polynomial in $m$ obtained from the sum defining the odd-case polynomial
$P_{m,o}(x)$ by the Faulhaber formulas for $\sum_{j=0}^{m} j^p$ with $p \le 3$; it agrees with
$P_{m,o}(x)$ at every natural number $m$.

Formalized by `MathlibExt.NumberTheory.NicomachusGeneralizationWanted.nicomachusPClosed`, a definition declared in [WantedExt/NumberTheory/NicomachusGeneralizationWanted.lean, line 86](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/NicomachusGeneralizationWanted.lean#L86). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/waring-figurate/nicomachus-s-theorem-and-its-generalizations/index.html#nicomachus-pclosed).

## The even-case polynomial $P_{m,e}$

For a natural number $m$ and a real number $x$,
$P_{m,e}(x) = \widetilde{P}(-m - 1, x)$, where $\widetilde{P}(m, x)$ is the Faulhaber expansion
of the odd-case polynomial $P_{m,o}(x)$ as a polynomial in $m$ (the paper defines $P_{m,e}(x)$
by substituting $-m - 1$ for $m$ in that expansion).

Formalized by `MathlibExt.NumberTheory.NicomachusGeneralizationWanted.nicomachusPEven`, a definition declared in [WantedExt/NumberTheory/NicomachusGeneralizationWanted.lean, line 93](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/NicomachusGeneralizationWanted.lean#L93). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/waring-figurate/nicomachus-s-theorem-and-its-generalizations/index.html#nicomachus-peven).

## The Kim–Stolarsky convergents $\alpha_k$

The rational numbers $\alpha_k$, for natural
numbers $k$, are defined by $\alpha_0 = 0$, $\alpha_1 = 1$ and
$\alpha_{k+1} = \frac{15 + 7\alpha_k}{13 + 6\alpha_k}$ for $k \ge 1$.

For $k \ge 1$, $\alpha_k$ is the continued-fraction convergent $[1; 6, 3, \ldots, 6, 3]$ with
$2k - 2$ partial quotients after the semicolon (Equation (12) of Kim and Stolarsky); the value
$\alpha_0 = 0$ is a placeholder.

Formalized by `MathlibExt.NumberTheory.NicomachusGeneralizationWanted.nicomachusAlpha`, a definition declared in [WantedExt/NumberTheory/NicomachusGeneralizationWanted.lean, line 100](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/NicomachusGeneralizationWanted.lean#L100). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/waring-figurate/nicomachus-s-theorem-and-its-generalizations/index.html#nicomachus-alpha).

## The Kim–Stolarsky integers $u_k$

For a natural number $k$, $u_k$ is the coefficient of
$x^{k-1}$ in the power series expansion over $\mathbb{Q}$ of

$$\frac{1 + 502x + x^2}{(1 - x)(1 - 398x + x^2)}.$$

For $k \ge 1$ these are the integers $u_k$ of Proposition 1 of Kim and Stolarsky; for $k = 0$ the
exponent $k - 1$ is read as $0$, so $u_0 = u_1 = 1$.

Formalized by `MathlibExt.NumberTheory.NicomachusGeneralizationWanted.nicomachusU`, a definition declared in [WantedExt/NumberTheory/NicomachusGeneralizationWanted.lean, line 109](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/NicomachusGeneralizationWanted.lean#L109). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/waring-figurate/nicomachus-s-theorem-and-its-generalizations/index.html#nicomachus-u).

## Generalized Nicomachus identity, odd case

Let $L_{m,o}$ be the odd-case cube sum,
$R_{m,o}$ the odd-case square and $P_{m,o}$ the odd-case polynomial. For every natural number
$m \ge 2$ and every real number $x$,

$$L_{m+1,o}(x) - R_{m+1,o}(x) = x \, P_{m,o}(x) - x^2 + x^3.$$

## Sources

- Seon-Hong Kim and Kenneth B. Stolarsky, "A Balanced Three or More-term Generalization of Nicomachus' Identity", Theorem 1.

Stated but not proved: `MathlibExt.NumberTheory.NicomachusGeneralizationWanted.nicomachusLOdd_sub_ROdd_succ_eq` is written with `theorem_wanted` in [WantedExt/NumberTheory/NicomachusGeneralizationWanted.lean, line 120](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/NicomachusGeneralizationWanted.lean#L120). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/waring-figurate/nicomachus-s-theorem-and-its-generalizations/index.html#nicomachus-lodd-sub-rodd-succ-eq).

## Generalized Nicomachus identity, even case

Let $L_{m,e}$ be the even-case cube sum,
$R_{m,e}$ the even-case square and $P_{m,e}$ the even-case polynomial. For every natural number
$m \ge 2$ and every real number $x$,

$$L_{m,e}(x) - R_{m,e}(x) = x \, P_{m,e}(x) - x^2 + x^3.$$

## Sources

- Seon-Hong Kim and Kenneth B. Stolarsky, "A Balanced Three or More-term Generalization of Nicomachus' Identity", Theorem 1.

Stated but not proved: `MathlibExt.NumberTheory.NicomachusGeneralizationWanted.nicomachusLEven_sub_REven_eq` is written with `theorem_wanted` in [WantedExt/NumberTheory/NicomachusGeneralizationWanted.lean, line 130](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/NicomachusGeneralizationWanted.lean#L130). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/waring-figurate/nicomachus-s-theorem-and-its-generalizations/index.html#nicomachus-leven-sub-reven-eq).

## Closed form for the Kim–Stolarsky integers $u_k$

Let $u_k$ be the coefficient of
$x^{k-1}$ in the power series expansion of $(1 + 502x + x^2)/((1 - x)(1 - 398x + x^2))$. For every
integer $k \ge 1$,

$$u_k = \frac{5(10 - 3\sqrt{11})^{2k-1} + 5(10 + 3\sqrt{11})^{2k-1} - 56}{44}.$$

## Sources

- Seon-Hong Kim and Kenneth B. Stolarsky, "A Balanced Three or More-term Generalization of Nicomachus' Identity", Proposition 1.

Stated but not proved: `MathlibExt.NumberTheory.NicomachusGeneralizationWanted.nicomachusU_eq_closedForm` is written with `theorem_wanted` in [WantedExt/NumberTheory/NicomachusGeneralizationWanted.lean, line 140](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/NicomachusGeneralizationWanted.lean#L140). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/waring-figurate/nicomachus-s-theorem-and-its-generalizations/index.html#nicomachus-u-eq-closed-form).

## Recurrence for the Kim–Stolarsky integers $u_k$

Let $u_k$ be the coefficient of
$x^{k-1}$ in the power series expansion of $(1 + 502x + x^2)/((1 - x)(1 - 398x + x^2))$. For every
integer $k \ge 1$,

$$u_{k+1} = 252 + 199u_k + 30\sqrt{(3 + 2u_k)(23 + 22u_k)}.$$

## Sources

- Seon-Hong Kim and Kenneth B. Stolarsky, "A Balanced Three or More-term Generalization of Nicomachus' Identity", Proposition 1.

Stated but not proved: `MathlibExt.NumberTheory.NicomachusGeneralizationWanted.nicomachusU_succ_eq` is written with `theorem_wanted` in [WantedExt/NumberTheory/NicomachusGeneralizationWanted.lean, line 150](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/NicomachusGeneralizationWanted.lean#L150). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/waring-figurate/nicomachus-s-theorem-and-its-generalizations/index.html#nicomachus-u-succ-eq).

## The convergents $\alpha_k$ in terms of the integers $u_k$

Let $\alpha_k$ be the
Kim–Stolarsky convergents, with $\alpha_1 = 1$ and
$\alpha_{k+1} = (15 + 7\alpha_k)/(13 + 6\alpha_k)$ for $k \ge 1$, and let $u_k$ be the
coefficient of $x^{k-1}$ in the power series expansion of
$(1 + 502x + x^2)/((1 - x)(1 - 398x + x^2))$. For every integer $k \ge 1$,

$$\alpha_k = \frac{-1 + \sqrt{11 - \frac{10}{3 + 2u_k}}}{2}.$$

## Sources

- Seon-Hong Kim and Kenneth B. Stolarsky, "A Balanced Three or More-term Generalization of Nicomachus' Identity", Proposition 2.

Stated but not proved: `MathlibExt.NumberTheory.NicomachusGeneralizationWanted.nicomachusAlpha_eq` is written with `theorem_wanted` in [WantedExt/NumberTheory/NicomachusGeneralizationWanted.lean, line 161](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/NicomachusGeneralizationWanted.lean#L161). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/waring-figurate/nicomachus-s-theorem-and-its-generalizations/index.html#nicomachus-alpha-eq).

## Kim–Stolarsky balanced quadratic sum

Let $k \ge 1$, let $\alpha_k$ be the numbers of
Equation (12) (so $\alpha_1 = 1$ and $\alpha_{k+1} = (15 + 7\alpha_k)/(13 + 6\alpha_k)$), let $u_k$
be the integers of Proposition 1, and let $T_n = n(n+1)/2$. With
$(a, b, c) = (1, \alpha_k, -(1 + \alpha_k))$ and $(d, e, f) = (-a, -c, -b)$ as in (17), for every
natural number $m$,

$$\sum_{j=1}^{m} (a + bj + cj^2)(d + ej + fj^2) =
T_{m-1}\left(\frac{(1 + m)(2 - 3m^2)}{3(3 + 2u_k)} + (3 + 2m)\,T_{m-1}\right).$$

## Sources

- Seon-Hong Kim and Kenneth B. Stolarsky, "A Balanced Three or More-term Generalization of Nicomachus' Identity", Theorem 2.

Stated but not proved: `MathlibExt.NumberTheory.NicomachusGeneralizationWanted.sum_quadratic_mul_quadratic_eq` is written with `theorem_wanted` in [WantedExt/NumberTheory/NicomachusGeneralizationWanted.lean, line 172](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/NicomachusGeneralizationWanted.lean#L172). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/waring-figurate/nicomachus-s-theorem-and-its-generalizations/index.html#sum-quadratic-mul-quadratic-eq).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Nicomachus's theorem and its generalizations](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/waring-figurate/nicomachus-s-theorem-and-its-generalizations/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/quadratic-forms-sums-of-squares/waring-figurate/nicomachus-s-theorem-and-its-generalizations)
