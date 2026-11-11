---
declaration: section
origin: cited
lean: MatrixDiscrepancy.signValue, MatrixDiscrepancy.discrepancy, MatrixDiscrepancy.ColumnAdmissible, MatrixDiscrepancy.dimensionConstant, MatrixDiscrepancy.komlosConstant, MatrixDiscrepancy.discrepancy_attained, MatrixDiscrepancy.UniformRectangularBound, KomlosDiscrepancyWanted.constantFormulationEquivalence
statement: formalized
---

# Komlós conjecture

29 results, 18 proved and 11 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/discrepancy-theory/koml-s-conjecture/index.html).

## Signs indexed by two elements

For $s \in \{0, 1\}$, the associated real sign is $-1$
if $s = 0$ and $1$ if $s = 1$.

Formalized by `MatrixDiscrepancy.signValue`, a definition declared in [MathlibExt/Combinatorics/MatrixDiscrepancy.lean, line 38](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/MatrixDiscrepancy.lean#L38). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/discrepancy-theory/koml-s-conjecture/index.html#sign-value).

## Discrepancy of a real matrix

For a real $m \times n$ matrix $A$, the discrepancy of $A$
is the infimum, over all sign vectors $x \in \{-1, 1\}^n$, of the maximum norm
$\|Ax\|_\infty = \max_i |(Ax)_i|$ (which is $0$ when $m = 0$), taken in $[0, \infty]$.

Formalized by `MatrixDiscrepancy.discrepancy`, a definition declared in [MathlibExt/Combinatorics/MatrixDiscrepancy.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/MatrixDiscrepancy.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/discrepancy-theory/koml-s-conjecture/index.html#discrepancy).

## Matrices with columns in the unit ball

A real $m \times n$ matrix $A$ is column
admissible when every column of $A$ lies in the closed Euclidean unit ball, that is,
$\sum_{i=1}^{m} A_{ij}^2 \le 1$ for every column index $j$.

Formalized by `MatrixDiscrepancy.ColumnAdmissible`, a definition declared in [MathlibExt/Combinatorics/MatrixDiscrepancy.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/MatrixDiscrepancy.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/discrepancy-theory/koml-s-conjecture/index.html#column-admissible).

## Komlós constant in a fixed dimension

For a natural number $n$, this is the supremum of
the discrepancy of $A$ over all real $n \times n$ matrices $A$ whose columns all have Euclidean
norm at most $1$, taken in $[0, \infty]$. The definition also applies to $n = 0$.

Formalized by `MatrixDiscrepancy.dimensionConstant`, a definition declared in [MathlibExt/Combinatorics/MatrixDiscrepancy.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/MatrixDiscrepancy.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/discrepancy-theory/koml-s-conjecture/index.html#dimension-constant).

## Komlós constant

The Komlós constant is the supremum, over all integers $n \ge 1$, of the
Komlós constant in dimension $n$, namely the supremum of the discrepancy of $A$ over all real
$n \times n$ matrices $A$ whose columns all have Euclidean norm at most $1$. It is taken in
$[0, \infty]$.

Formalized by `MatrixDiscrepancy.komlosConstant`, a definition declared in [MathlibExt/Combinatorics/MatrixDiscrepancy.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/MatrixDiscrepancy.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/discrepancy-theory/koml-s-conjecture/index.html#komlos-constant).

## The discrepancy is attained

For every real $m \times n$ matrix $A$, including the cases
$m = 0$ and $n = 0$, there is a sign vector $x \in \{-1, 1\}^n$ such that the discrepancy of $A$
equals $\|Ax\|_\infty$.

Formalized by `MatrixDiscrepancy.discrepancy_attained`, a theorem declared in [MathlibExt/Combinatorics/MatrixDiscrepancy.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/MatrixDiscrepancy.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/discrepancy-theory/koml-s-conjecture/index.html#discrepancy-attained).

## Uniform discrepancy bound for vectors in the unit ball

The statement that there is a real
constant $C > 0$ such that for all natural numbers $n$ and $d$ and all vectors
$v_1, \dots, v_n \in \mathbb{R}^d$ of Euclidean norm at most $1$, writing $v_{ij}$ for the
$j$-th coordinate of $v_i$, there are signs $\varepsilon_1, \dots, \varepsilon_n \in \{-1, 1\}$
with $\left|\sum_{i=1}^{n} \varepsilon_i v_{ij}\right| \le C$ for every coordinate index $j$.

Formalized by `MatrixDiscrepancy.UniformRectangularBound`, a definition declared in [MathlibExt/Combinatorics/MatrixDiscrepancy.lean, line 218](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/MatrixDiscrepancy.lean#L218). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/discrepancy-theory/koml-s-conjecture/index.html#uniform-rectangular-bound).

## Equivalence of the square and rectangular Komlós formulations (statement)

The statement
that the uniform discrepancy bound for vectors in the unit ball holds if and only if the Komlós
constant is finite.

## Sources

- optimization catalogue C24a, line 26, and AIM Problem 1.05. The padding bridge is requested, not assumed or claimed definitional.

Formalized by `KomlosDiscrepancyWanted.constantFormulationEquivalence`, a definition declared in [WantedExt/Combinatorics/KomlosDiscrepancyWanted.lean, line 35](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/KomlosDiscrepancyWanted.lean#L35). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/discrepancy-theory/koml-s-conjecture/index.html#constant-formulation-equivalence).

## Beck–Spencer–Gluskin logarithmic upper bound (statement)

The statement that there are a
real number $c > 0$ and a natural number $N \ge 3$ such that for every natural number $n \ge N$,
the Komlós constant in dimension $n$ is at most $c \log n$, where $\log$ is the natural logarithm.

## Sources

- optimization catalogue C24a, line 35, Beck (1981), Spencer (1985), and Gluskin (1989); their full original theorem texts remain a primary-source gap.

Formalized by `KomlosDiscrepancyWanted.beckSpencerGluskinLogUpperBound`, a definition declared in [WantedExt/Combinatorics/KomlosDiscrepancyWanted.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/KomlosDiscrepancyWanted.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/discrepancy-theory/koml-s-conjecture/index.html#beck-spencer-gluskin-log-upper-bound).

## Statement of Banaszczyk's Komlós bound

The proposition that there are a real constant
$c > 0$ and a natural number $N \ge 3$ such that for every natural number $n \ge N$, the Komlós
constant in dimension $n$ is at most $c \sqrt{\log n}$, where $\log$ is the natural logarithm.

## Sources

- optimization catalogue C24a, line 36, Banaszczyk (1998), also reported in retained BJ2025 introduction and BDG2019 Theorem `komlos`.

Formalized by `KomlosDiscrepancyWanted.banaszczyk1998SqrtLogUpperBound`, a definition declared in [WantedExt/Combinatorics/KomlosDiscrepancyWanted.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/KomlosDiscrepancyWanted.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/discrepancy-theory/koml-s-conjecture/index.html#banaszczyk1998-sqrt-log-upper-bound).

## Statement of the sublogarithmic Komlós bound

The proposition that for every real
$\varepsilon > 0$ there is a natural number $N \ge 3$ such that for every natural number
$n \ge N$, the Komlós constant in dimension $n$ is at most $\varepsilon \log n$, where $\log$ is
the natural logarithm. In other words, the Komlós constant in dimension $n$ is $o(\log n)$.

## Sources

- optimization catalogue C24a, line 36, the `o(log n)` comment.

Formalized by `KomlosDiscrepancyWanted.banaszczykSublogUpperBound`, a definition declared in [WantedExt/Combinatorics/KomlosDiscrepancyWanted.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/KomlosDiscrepancyWanted.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/discrepancy-theory/koml-s-conjecture/index.html#banaszczyk-sublog-upper-bound).

## Statement of the Bansal–Dadush–Garg Komlós bound

The proposition that there are a real
constant $c > 0$ and a natural number $N \ge 3$ such that for every natural number $n \ge N$, the
Komlós constant in dimension $n$ is at most $c \sqrt{\log n}$, where $\log$ is the natural
logarithm.

Only this numerical bound is stated, not the polynomial-time algorithm of the source.

## Sources

- Bansal, Dadush, and Garg, arXiv1605.02882, retained introduction lines 52-60, Theorem `komlos`; efficient randomized/high-probability computation is an explicit separate gap.

Formalized by `KomlosDiscrepancyWanted.bdg2019NumericalSqrtLogUpperBound`, a definition declared in [WantedExt/Combinatorics/KomlosDiscrepancyWanted.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/KomlosDiscrepancyWanted.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/discrepancy-theory/koml-s-conjecture/index.html#bdg2019-numerical-sqrt-log-upper-bound).

## Statement of the Bansal–Jiang Komlós bound

The proposition that there are a real
constant $c > 0$, a natural number $p$ and a natural number $N \ge 3$ such that for every natural
number $n \ge N$, the Komlós constant in dimension $n$ is at most
$c (\log n)^{1/4} (\log \log n)^p$, where $\log$ is the natural logarithm.

## Sources

- Bansal and Haotian Jiang, arXiv2508.03961, retained abstract lines 1-9 and introduction Theorem `thm:Komlos`. The abstract explicitly defines tilde as `poly(log log n)`; no degree is invented.

Formalized by `KomlosDiscrepancyWanted.bansalJiang2025QuarterLogUpperBound`, a definition declared in [WantedExt/Combinatorics/KomlosDiscrepancyWanted.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/KomlosDiscrepancyWanted.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/discrepancy-theory/koml-s-conjecture/index.html#bansal-jiang2025-quarter-log-upper-bound).

## Statement of the little-o square-root-log Komlós bound

The proposition that for every
real $\varepsilon > 0$ there is a natural number $N \ge 3$ such that for every natural number
$n \ge N$, the Komlós constant in dimension $n$ is at most $\varepsilon \sqrt{\log n}$, where
$\log$ is the natural logarithm. In other words, the Komlós constant in dimension $n$ is
$o(\sqrt{\log n})$.

## Sources

- optimization catalogue C24a, line 38, and BJ2025's retained abstract.

Formalized by `KomlosDiscrepancyWanted.bansalJiang2025LittleSqrtLogUpperBound`, a definition declared in [WantedExt/Combinatorics/KomlosDiscrepancyWanted.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/KomlosDiscrepancyWanted.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/discrepancy-theory/koml-s-conjecture/index.html#bansal-jiang2025-little-sqrt-log-upper-b).

## Kunisky's lower bound for the Komlós constant (statement)

The statement that the Komlós
constant is at least $1 + \sqrt{2}$.

The bound concerns the supremum over all dimensions; it does not assert that any single
dimension attains $1 + \sqrt{2}$.

## Sources

- optimization catalogue C24a, line 45, and retained Kunisky arXiv2111.02974v1, Theorem 1.1.

Formalized by `KomlosDiscrepancyWanted.kunisky2023LowerBound`, a definition declared in [WantedExt/Combinatorics/KomlosDiscrepancyWanted.lean, line 91](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/KomlosDiscrepancyWanted.lean#L91). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/discrepancy-theory/koml-s-conjecture/index.html#kunisky2023-lower-bound).

## Infinitely many dimensions with Komlós constant at least $1 + \sqrt{2}$ (statement)

The
statement that there are infinitely many natural numbers $n \ge 1$ such that the Komlós constant
in dimension $n$ is at least $1 + \sqrt{2}$.

## Sources

- optimization catalogue C24a, line 53. Retained Kunisky v1 only gives a sequence approaching the endpoint from below; the journal2023 comparison is unresolved. This request does not certify exact finite attainment.

Formalized by `KomlosDiscrepancyWanted.kuniskyInfinitelyManyDimensionsLowerBound`, a definition declared in [WantedExt/Combinatorics/KomlosDiscrepancyWanted.lean, line 99](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/KomlosDiscrepancyWanted.lean#L99). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/discrepancy-theory/koml-s-conjecture/index.html#kunisky-infinitely-many-dimensions-lower).

## Komlós conjecture for vector colorings (statement)

The statement that for all natural
numbers $m$ and $n \ge 1$ and every real $m \times n$ matrix $A$ whose columns all lie in the
closed Euclidean unit ball, there are unit vectors $u_1, \dots, u_n$ in the Euclidean space
$\mathbb{R}^n$ such that $\lVert \sum_{j=1}^{n} A_{ij} u_j \rVert \le 1$ for every row index $i$,
where $\lVert \cdot \rVert$ is the Euclidean norm.

## Sources

- Nikolov, arXiv1301.4039, retained KomlosSDP.tex lines 115-139, Theorem `thm:main`. Positive column dimension is explicit.

Formalized by `KomlosDiscrepancyWanted.nikolov2013VectorColoringBound`, a definition declared in [WantedExt/Combinatorics/KomlosDiscrepancyWanted.lean, line 106](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/KomlosDiscrepancyWanted.lean#L106). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/discrepancy-theory/koml-s-conjecture/index.html#nikolov2013-vector-coloring-bound).

## Statement of Nikolov's bound on vector discrepancy

This is the proposition that for all
natural numbers $m$ and $n$ with $n \ge 1$ and every real $m \times n$ matrix $A$ whose columns
all lie in the closed Euclidean unit ball, that is, $\sum_{i} A_{ij}^2 \le 1$ for every
column $j$, the vector discrepancy of $A$ is at most $1$.

This bounds the unit-vector relaxation, not the discrepancy over sign vectors.

## Sources

- Nikolov, arXiv1301.4039, retained KomlosSDP.tex, Theorem `thm:main`, and optimization catalogue C24a, line 55.

Formalized by `KomlosDiscrepancyWanted.nikolov2013VectorDiscrepancyUpperBound`, a definition declared in [WantedExt/Combinatorics/KomlosDiscrepancyWanted.lean, line 115](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/KomlosDiscrepancyWanted.lean#L115). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/discrepancy-theory/koml-s-conjecture/index.html#nikolov2013-vector-discrepancy-upper-bou).

## The square and rectangular Komlós formulations are equivalent

The following two
conditions are equivalent. (a) There is a real constant $C > 0$ such that for all natural numbers
$n$ and $d$ and all vectors $v_1, \dots, v_n \in \mathbb{R}^d$ of Euclidean norm at most $1$,
writing $v_{ij}$ for the $j$-th coordinate of $v_i$, there are signs
$\varepsilon_1, \dots, \varepsilon_n \in \{-1, 1\}$ with
$\left|\sum_{i=1}^{n} \varepsilon_i v_{ij}\right| \le C$ for every coordinate index $j$. (b) The
Komlós constant, the supremum over all $n \ge 1$ of the discrepancy of real $n \times n$ matrices
whose columns all have Euclidean norm at most $1$, is finite.

## Sources

- optimization catalogue C24a, line 26, and AIM Problem 1.05.

Stated but not proved: `KomlosDiscrepancyWanted.constantFormulationEquivalence_holds` is written with `theorem_wanted` in [WantedExt/Combinatorics/KomlosDiscrepancyWanted.lean, line 120](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/KomlosDiscrepancyWanted.lean#L120). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/discrepancy-theory/koml-s-conjecture/index.html#constant-formulation-equivalence-holds).

## Beck–Spencer–Gluskin logarithmic upper bound for the Komlós constant

There are a real
number $c > 0$ and a natural number $N \ge 3$ such that for every natural number $n \ge N$, the
Komlós constant in dimension $n$ (the supremum of the discrepancy of real $n \times n$ matrices
whose columns all have Euclidean norm at most $1$, taken in $[0, \infty]$) is at most $c \log n$,
where $\log$ is the natural logarithm.

## Sources

- optimization catalogue C24a, line 35, Beck, Spencer, and Gluskin.

Stated but not proved: `KomlosDiscrepancyWanted.beckSpencerGluskinLogUpperBound_holds` is written with `theorem_wanted` in [WantedExt/Combinatorics/KomlosDiscrepancyWanted.lean, line 123](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/KomlosDiscrepancyWanted.lean#L123). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/discrepancy-theory/koml-s-conjecture/index.html#beck-spencer-gluskin-log-upper-bound-hol).

## Banaszczyk's bound for the Komlós problem

There are a real constant $c > 0$ and a
natural number $N \ge 3$ such that for every natural number $n \ge N$, the Komlós constant in
dimension $n$ is at most $c \sqrt{\log n}$, where $\log$ is the natural logarithm.

## Sources

- optimization catalogue C24a, line 36, Banaszczyk (1998).

Stated but not proved: `KomlosDiscrepancyWanted.banaszczyk1998SqrtLogUpperBound_holds` is written with `theorem_wanted` in [WantedExt/Combinatorics/KomlosDiscrepancyWanted.lean, line 126](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/KomlosDiscrepancyWanted.lean#L126). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/discrepancy-theory/koml-s-conjecture/index.html#banaszczyk1998-sqrt-log-upper-bound-hold).

## Sublogarithmic bound for the Komlós problem

For every real $\varepsilon > 0$ there is a
natural number $N \ge 3$ such that for every natural number $n \ge N$, the Komlós constant in
dimension $n$ is at most $\varepsilon \log n$, where $\log$ is the natural logarithm. In other
words, the Komlós constant in dimension $n$ is $o(\log n)$.

## Sources

- optimization catalogue C24a, line 36, its sublogarithmic comment.

Stated but not proved: `KomlosDiscrepancyWanted.banaszczykSublogUpperBound_holds` is written with `theorem_wanted` in [WantedExt/Combinatorics/KomlosDiscrepancyWanted.lean, line 129](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/KomlosDiscrepancyWanted.lean#L129). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/discrepancy-theory/koml-s-conjecture/index.html#banaszczyk-sublog-upper-bound-holds).

## Bansal–Dadush–Garg bound for the Komlós problem, numerical form

There are a real
constant $c > 0$ and a natural number $N \ge 3$ such that for every natural number $n \ge N$, the
Komlós constant in dimension $n$ is at most $c \sqrt{\log n}$, where $\log$ is the natural
logarithm.

## Sources

- BDG2019, arXiv1605.02882, retained Theorem `komlos`.

Stated but not proved: `KomlosDiscrepancyWanted.bdg2019NumericalSqrtLogUpperBound_holds` is written with `theorem_wanted` in [WantedExt/Combinatorics/KomlosDiscrepancyWanted.lean, line 132](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/KomlosDiscrepancyWanted.lean#L132). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/discrepancy-theory/koml-s-conjecture/index.html#bdg2019-numerical-sqrt-log-upper-bound-h).

## Bansal–Jiang bound for the Komlós problem

There are a real constant $c > 0$, a natural
number $p$ and a natural number $N \ge 3$ such that for every natural number $n \ge N$, the
Komlós constant in dimension $n$ is at most $c (\log n)^{1/4} (\log \log n)^p$, where $\log$ is
the natural logarithm.

## Sources

- BJ2025, arXiv2508.03961, abstract and Theorem `thm:Komlos`.

Stated but not proved: `KomlosDiscrepancyWanted.bansalJiang2025QuarterLogUpperBound_holds` is written with `theorem_wanted` in [WantedExt/Combinatorics/KomlosDiscrepancyWanted.lean, line 135](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/KomlosDiscrepancyWanted.lean#L135). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/discrepancy-theory/koml-s-conjecture/index.html#bansal-jiang2025-quarter-log-upper-bound-2).

## Bansal–Jiang improvement on Banaszczyk's Komlós bound

For every real $\varepsilon > 0$
there is a natural number $N \ge 3$ such that for every natural number $n \ge N$, the Komlós
constant in dimension $n$ is at most $\varepsilon \sqrt{\log n}$, where $\log$ is the natural
logarithm. In other words, the Komlós constant in dimension $n$ is $o(\sqrt{\log n})$.

## Sources

- BJ2025, arXiv2508.03961, the improvement reported in its abstract.

Stated but not proved: `KomlosDiscrepancyWanted.bansalJiang2025LittleSqrtLogUpperBound_holds` is written with `theorem_wanted` in [WantedExt/Combinatorics/KomlosDiscrepancyWanted.lean, line 138](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/KomlosDiscrepancyWanted.lean#L138). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/discrepancy-theory/koml-s-conjecture/index.html#bansal-jiang2025-little-sqrt-log-upper-b-2).

## Kunisky's lower bound for the Komlós constant

The Komlós constant (the supremum over all
$n \ge 1$ of the discrepancy of real $n \times n$ matrices whose columns all have Euclidean norm
at most $1$, taken in $[0, \infty]$) is at least $1 + \sqrt{2}$.

## Sources

- Kunisky, arXiv2111.02974v1, Theorem 1.1; catalogue C24a, line 45.

Stated but not proved: `KomlosDiscrepancyWanted.kunisky2023LowerBound_holds` is written with `theorem_wanted` in [WantedExt/Combinatorics/KomlosDiscrepancyWanted.lean, line 142](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/KomlosDiscrepancyWanted.lean#L142). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/discrepancy-theory/koml-s-conjecture/index.html#kunisky2023-lower-bound-holds).

## Infinitely many dimensions have Komlós constant at least $1 + \sqrt{2}$

There are
infinitely many natural numbers $n \ge 1$ such that the Komlós constant in dimension $n$ (the
supremum of the discrepancy of real $n \times n$ matrices whose columns all have Euclidean norm
at most $1$, taken in $[0, \infty]$) is at least $1 + \sqrt{2}$.

## Sources

- catalogue C24a, line 53, unverified exact finite-endpoint assertion.

Stated but not proved: `KomlosDiscrepancyWanted.kuniskyInfinitelyManyDimensionsLowerBound_holds` is written with `theorem_wanted` in [WantedExt/Combinatorics/KomlosDiscrepancyWanted.lean, line 145](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/KomlosDiscrepancyWanted.lean#L145). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/discrepancy-theory/koml-s-conjecture/index.html#kunisky-infinitely-many-dimensions-lower-2).

## Nikolov's theorem: the Komlós conjecture holds for vector colorings

For all natural
numbers $m$ and $n \ge 1$ and every real $m \times n$ matrix $A$ whose columns all have Euclidean
norm at most $1$, there are unit vectors $u_1, \dots, u_n$ in the Euclidean space $\mathbb{R}^n$
such that $\lVert \sum_{j=1}^{n} A_{ij} u_j \rVert \le 1$ for every row index $i$, where
$\lVert \cdot \rVert$ is the Euclidean norm.

## Sources

- Nikolov, arXiv1301.4039, retained Theorem `thm:main`.

Stated but not proved: `KomlosDiscrepancyWanted.nikolov2013VectorColoringBound_holds` is written with `theorem_wanted` in [WantedExt/Combinatorics/KomlosDiscrepancyWanted.lean, line 149](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/KomlosDiscrepancyWanted.lean#L149). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/discrepancy-theory/koml-s-conjecture/index.html#nikolov2013-vector-coloring-bound-holds).

## Nikolov's bound on vector discrepancy

For all natural numbers $m$ and $n$ with
$n \ge 1$ and every real $m \times n$ matrix $A$ whose columns all lie in the closed
Euclidean unit ball, that is, $\sum_{i} A_{ij}^2 \le 1$ for every column $j$, the vector
discrepancy of $A$ is at most $1$.

## Sources

- Nikolov, arXiv1301.4039, retained Theorem `thm:main`; catalogue line 55.

Stated but not proved: `KomlosDiscrepancyWanted.nikolov2013VectorDiscrepancyUpperBound_holds` is written with `theorem_wanted` in [WantedExt/Combinatorics/KomlosDiscrepancyWanted.lean, line 152](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/KomlosDiscrepancyWanted.lean#L152). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/discrepancy-theory/koml-s-conjecture/index.html#nikolov2013-vector-discrepancy-upper-bou-2).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Komlós conjecture](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/discrepancy-theory/koml-s-conjecture/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/discrepancy-theory/koml-s-conjecture)
