---
declaration: section
origin: cited
lean: MathlibExt.Combinatorics.LineCompatibleSequencesErdosProblem733Wanted.lineSizes, MathlibExt.Combinatorics.LineCompatibleSequencesErdosProblem733Wanted.lineCompatibleCount, MathlibExt.Combinatorics.LineCompatibleSequencesErdosProblem733Wanted.lineCompatibleCountSubexponential, MathlibExt.Combinatorics.LineCompatibleSequencesErdosProblem733Wanted.lineCompatibleCountSubexponential_holds, MathlibExt.Combinatorics.LineIncidenceSetsCountErdosProblem607Wanted.lineIncidenceSet, MathlibExt.Combinatorics.LineIncidenceSetsCountErdosProblem607Wanted.lineIncidenceSetCount, MathlibExt.Combinatorics.LineIncidenceSetsCountErdosProblem607Wanted.lineIncidenceSetCountSubexponential, MathlibExt.Combinatorics.LineIncidenceSetsCountErdosProblem607Wanted.lineIncidenceSetCountSubexponential_holds
statement: formalized
---

# Point–line incidences

8 results, 6 proved and 2 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/point-line-incidences/index.html).

## Line sizes of a planar point set

For a finite set $P \subseteq \mathbb{R}^2$, this is
the multiset of the numbers $|\ell \cap P|$, where $\ell$ ranges over the lines determined by
$P$, that is, the distinct lines through two distinct points of $P$, each counted once.

Formalized by `MathlibExt.Combinatorics.LineCompatibleSequencesErdosProblem733Wanted.lineSizes`, a definition declared in [WantedExt/Combinatorics/LineCompatibleSequencesErdosProblem733Wanted.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/LineCompatibleSequencesErdosProblem733Wanted.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/point-line-incidences/index.html#line-sizes).

## Number of line-compatible sequences

For a natural number $n$, $f(n)$ is the number of
distinct multisets that arise as the line sizes of some $n$-point set $P \subseteq \mathbb{R}^2$,
that is, as the multiset of the numbers $|\ell \cap P|$ over the distinct lines $\ell$ through
two distinct points of $P$, each line counted once. These multisets are the line-compatible
sequences for $n$; there are finitely many, since each has at most $n^2$ entries, all at most
$n$.

Formalized by `MathlibExt.Combinatorics.LineCompatibleSequencesErdosProblem733Wanted.lineCompatibleCount`, a definition declared in [WantedExt/Combinatorics/LineCompatibleSequencesErdosProblem733Wanted.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/LineCompatibleSequencesErdosProblem733Wanted.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/point-line-incidences/index.html#line-compatible-count).

## Subexponential count of line-compatible sequences (statement)

The proposition that
there is a real constant $C$ such that for every natural number $n$, the number $f(n)$ of
line-compatible sequences for $n$ is at most $e^{C \sqrt{n}}$; that is, there are at most
$\exp(O(\sqrt{n}))$ line-compatible sequences. This is Erdős Problem 733.

Formalized by `MathlibExt.Combinatorics.LineCompatibleSequencesErdosProblem733Wanted.lineCompatibleCountSubexponential`, a definition declared in [WantedExt/Combinatorics/LineCompatibleSequencesErdosProblem733Wanted.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/LineCompatibleSequencesErdosProblem733Wanted.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/point-line-incidences/index.html#line-compatible-count-subexponential).

## Szemerédi–Trotter bound on line-compatible sequences

There is a real constant $C$ such that
for every natural number $n$, the number of line-compatible sequences for $n$, that is, of
distinct multisets of the numbers $|\ell \cap P|$ over the distinct lines $\ell$ through two
distinct points of an $n$-point set $P \subseteq \mathbb{R}^2$, each line counted once, is at
most $e^{C \sqrt{n}}$. This answers Erdős Problem 733.

## Sources

- T. F. Bloom, Erdős Problems, Problem #733, https://www.erdosproblems.com/733 (status PROVED); resolution: E. Szemerédi and W. T. Trotter, Extremal problems in discrete geometry, Combinatorica 3 (1983), 381-392, erdosproblems.com/733: 'This is true, and was proved by Szemerédi and Trotter', https://doi.org/10.1007/BF02579194.

Stated but not proved: `MathlibExt.Combinatorics.LineCompatibleSequencesErdosProblem733Wanted.lineCompatibleCountSubexponential_holds` is written with `theorem_wanted` in [WantedExt/Combinatorics/LineCompatibleSequencesErdosProblem733Wanted.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/LineCompatibleSequencesErdosProblem733Wanted.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/point-line-incidences/index.html#line-compatible-count-subexponential-hol).

## Line-incidence set of a finite planar point set

For a finite set
$P \subseteq \mathbb{R}^2$, $A(P)$ is the set of the numbers $|\ell \cap P|$ over the lines $\ell$
determined by $P$, that is, the lines through at least two distinct points of $P$.

Formalized by `MathlibExt.Combinatorics.LineIncidenceSetsCountErdosProblem607Wanted.lineIncidenceSet`, a definition declared in [WantedExt/Combinatorics/LineIncidenceSetsCountErdosProblem607Wanted.lean, line 39](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/LineIncidenceSetsCountErdosProblem607Wanted.lean#L39). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/point-line-incidences/index.html#line-incidence-set).

## Number of line-incidence sets

For a finite set $P \subseteq \mathbb{R}^2$, let $A(P)$ be
the set of the numbers $|\ell \cap P|$ over the lines $\ell$ through at least two distinct points
of $P$. For a natural number $n$, $F(n)$ is the number of distinct sets $A(P)$ over all $n$-point
sets $P \subseteq \mathbb{R}^2$. Every such $A(P)$ is a subset of $\{0, \dots, n\}$.

Formalized by `MathlibExt.Combinatorics.LineIncidenceSetsCountErdosProblem607Wanted.lineIncidenceSetCount`, a definition declared in [WantedExt/Combinatorics/LineIncidenceSetsCountErdosProblem607Wanted.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/LineIncidenceSetsCountErdosProblem607Wanted.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/point-line-incidences/index.html#line-incidence-set-count).

## Erdős Problem 607: subexponentially many line-incidence sets

For a finite set
$P \subseteq \mathbb{R}^2$, let $A(P)$ be the set of the numbers $|\ell \cap P|$ over the lines
$\ell$ through at least two distinct points of $P$, and let $F(n)$ be the number of distinct sets
$A(P)$ over all $n$-point sets $P \subseteq \mathbb{R}^2$. This is the statement that there is a
real constant $C$ such that $F(n) \le e^{C\sqrt{n}}$ for every natural number $n$, that is,
$F(n) \le \exp(O(\sqrt{n}))$.

Formalized by `MathlibExt.Combinatorics.LineIncidenceSetsCountErdosProblem607Wanted.lineIncidenceSetCountSubexponential`, a definition declared in [WantedExt/Combinatorics/LineIncidenceSetsCountErdosProblem607Wanted.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/LineIncidenceSetsCountErdosProblem607Wanted.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/point-line-incidences/index.html#line-incidence-set-count-subexponential).

## Szemerédi–Trotter bound for line-incidence sets (Erdős Problem 607)

For a finite set
$P \subseteq \mathbb{R}^2$, let $A(P)$ be the set of the numbers $|\ell \cap P|$ over the lines
$\ell$ through at least two distinct points of $P$, and let $F(n)$ be the number of distinct sets
$A(P)$ over all $n$-point sets $P \subseteq \mathbb{R}^2$. There is a real constant $C$ such that
$F(n) \le e^{C\sqrt{n}}$ for every natural number $n$.

## Sources

- T. F. Bloom, Erdős Problems, Problem #607, https://www.erdosproblems.com/607 (status PROVED); resolution: E. Szemerédi and W. T. Trotter, Extremal problems in discrete geometry, Combinatorica 3 (1983), 381-392, erdosproblems.com/607: proved by Szemerédi and Trotter [SzTr83], https://doi.org/10.1007/BF02579194.

Stated but not proved: `MathlibExt.Combinatorics.LineIncidenceSetsCountErdosProblem607Wanted.lineIncidenceSetCountSubexponential_holds` is written with `theorem_wanted` in [WantedExt/Combinatorics/LineIncidenceSetsCountErdosProblem607Wanted.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/LineIncidenceSetsCountErdosProblem607Wanted.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/point-line-incidences/index.html#line-incidence-set-count-subexponential-2).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Point–line incidences](https://deicyde.github.io/atlas-lean/roadmap/Geometry/discrete-geometry/part-01/point-line-incidences/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Geometry/discrete-geometry/part-01/point-line-incidences)
