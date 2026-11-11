---
declaration: section
origin: cited
lean: Cslib.Algorithms.Lean.ArcConsistency.BinaryCSP, Cslib.Algorithms.Lean.ArcConsistency.IsSolution, Cslib.Algorithms.Lean.ArcConsistency.ArcConsistent, Cslib.Algorithms.Lean.ArcConsistency.Symmetric, Cslib.Algorithms.Lean.ArcConsistency.revise, Cslib.Algorithms.Lean.ArcConsistency.indeg, Cslib.Algorithms.Lean.ArcConsistency.requeue, Cslib.Algorithms.Lean.ArcConsistency.potential
statement: formalized
proof: formalized
---

# AC-3 algorithm

21 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/heuristic-search-and-planning/ac-3-algorithm/index.html).

## Binary constraint satisfaction problem

A binary constraint satisfaction problem with
variables in $X$ and values in $D$ consists of a finite list of directed arcs $(x, y)$ with
$x, y \in X$, and, for all variables $x, y$ and values $a, b \in D$, a Boolean saying whether the
arc $(x, y)$ allows $x = a$ together with $y = b$.

Formalized by `Cslib.Algorithms.Lean.ArcConsistency.BinaryCSP`, a structure declared in [CSLibExt/Algorithms/Lean/CSP/AC3.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/CSP/AC3.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/heuristic-search-and-planning/ac-3-algorithm/index.html#binary-csp).

## Solution of a binary CSP within given domains

Let $P$ be a binary constraint
satisfaction problem with variables $X$ and values $D$, and give each variable $x$ a finite
domain $\mathrm{dom}(x) \subseteq D$. An assignment $\sigma : X \to D$ is a solution of $P$ within
$\mathrm{dom}$ when $\sigma(x) \in \mathrm{dom}(x)$ for every variable $x$ and, for every arc
$(x, y)$ of $P$, the arc $(x, y)$ allows the pair $(\sigma(x), \sigma(y))$.

Formalized by `Cslib.Algorithms.Lean.ArcConsistency.IsSolution`, a definition declared in [CSLibExt/Algorithms/Lean/CSP/AC3.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/CSP/AC3.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/heuristic-search-and-planning/ac-3-algorithm/index.html#is-solution).

## Arc consistency

Given a binary CSP $P$ and domains $\mathrm{dom}$, an arc $(x, y)$ is
consistent when for every value $a \in \mathrm{dom}(x)$ there is a value $b \in \mathrm{dom}(y)$
such that the arc $(x, y)$ allows $x = a$ together with $y = b$.

Formalized by `Cslib.Algorithms.Lean.ArcConsistency.ArcConsistent`, a definition declared in [CSLibExt/Algorithms/Lean/CSP/AC3.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/CSP/AC3.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/heuristic-search-and-planning/ac-3-algorithm/index.html#arc-consistent).

## Symmetric binary CSP

A binary constraint satisfaction problem is symmetric when, for
all variables $x, y$ and values $a, b$, the constraint on the ordered pair $(x, y)$ allows
$x = a$ together with $y = b$ exactly when the constraint on $(y, x)$ allows $y = b$ together
with $x = a$.

The condition concerns the allowed pairs for every ordered pair of variables; it does not
require the reverse of a listed arc to be listed.

Formalized by `Cslib.Algorithms.Lean.ArcConsistency.Symmetric`, a definition declared in [CSLibExt/Algorithms/Lean/CSP/AC3.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/CSP/AC3.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/heuristic-search-and-planning/ac-3-algorithm/index.html#symmetric).

## Revision of an arc

Let $P$ be a binary constraint satisfaction problem with values $D$,
$\mathrm{dom}$ finite domains for its variables, and $x$, $y$ variables. The revision of the arc
$(x, y)$ is the set of values $a \in \mathrm{dom}(x)$ that have a support in the domain of $y$:
some $b \in \mathrm{dom}(y)$ such that the arc $(x, y)$ allows the pair $(a, b)$.

Formalized by `Cslib.Algorithms.Lean.ArcConsistency.revise`, a definition declared in [CSLibExt/Algorithms/Lean/CSP/AC3.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/CSP/AC3.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/heuristic-search-and-planning/ac-3-algorithm/index.html#revise).

## In-degree of a variable

For a binary constraint satisfaction problem $P$ and a variable
$x$, the in-degree of $x$ is the number of arcs $(z, x)$ of $P$ ending at $x$, counted with
multiplicity in the list of arcs of $P$.

Formalized by `Cslib.Algorithms.Lean.ArcConsistency.indeg`, a definition declared in [CSLibExt/Algorithms/Lean/CSP/AC3.lean, line 82](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/CSP/AC3.lean#L82). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/heuristic-search-and-planning/ac-3-algorithm/index.html#indeg).

## Arcs requeued after a revision

For a binary constraint satisfaction problem $P$ and
variables $x$ and $y$, the arcs requeued after revising $(x, y)$ are the arcs $(z, x)$ of $P$
with $z \neq y$, in their order in the list of arcs of $P$.

AC-3 queues these arcs when revising $(x, y)$ shrinks the domain of $x$.

Formalized by `Cslib.Algorithms.Lean.ArcConsistency.requeue`, a definition declared in [CSLibExt/Algorithms/Lean/CSP/AC3.lean, line 85](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/CSP/AC3.lean#L85). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/heuristic-search-and-planning/ac-3-algorithm/index.html#requeue).

## Termination potential of AC-3

Let $P$ be a binary constraint satisfaction problem with
finitely many variables, $\mathrm{dom}$ finite domains for its variables and $q$ a queue of arcs.
The potential of $\mathrm{dom}$ and $q$ is

$$|q| + \sum_{x} |\mathrm{dom}(x)| \cdot \mathrm{indeg}(x),$$

where $|q|$ is the length of the queue, the sum runs over all variables $x$, and
$\mathrm{indeg}(x)$ is the in-degree of $x$ in $P$.

Formalized by `Cslib.Algorithms.Lean.ArcConsistency.potential`, a definition declared in [CSLibExt/Algorithms/Lean/CSP/AC3.lean, line 88](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/CSP/AC3.lean#L88). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/heuristic-search-and-planning/ac-3-algorithm/index.html#potential).

## A shrinking revision lowers the potential

Let $P$ be a binary constraint satisfaction
problem with finitely many variables, $\mathrm{dom}$ finite domains for its variables, $x$ and
$y$ variables and $q$ a queue of arcs. Suppose the revision $R$ of the arc $(x, y)$ with respect
to $\mathrm{dom}$ differs from $\mathrm{dom}(x)$, and let $\mathrm{dom}'$ agree with
$\mathrm{dom}$ except that $\mathrm{dom}'(x) = R$. Then the potential of $\mathrm{dom}'$ with the
queue $q$ followed by the arcs requeued after revising $(x, y)$ is strictly less than the
potential of $\mathrm{dom}$ with the queue $(x, y)$ followed by $q$.

Formalized by `Cslib.Algorithms.Lean.ArcConsistency.potential_lt`, a theorem declared in [CSLibExt/Algorithms/Lean/CSP/AC3.lean, line 107](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/CSP/AC3.lean#L107). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/heuristic-search-and-planning/ac-3-algorithm/index.html#potential-lt).

## The AC-3 algorithm

Given a binary CSP $P$ with finitely many variables, domains
$\mathrm{dom}$ and a queue $q$ of pairs of variables, AC-3 returns $\mathrm{dom}$ when $q$ is
empty. Otherwise it removes the first pair $(x, y)$ of $q$ and revises it: the revised domain of
$x$ consists of the values $a \in \mathrm{dom}(x)$ for which some $b \in \mathrm{dom}(y)$ has the
arc $(x, y)$ allowing $x = a$ together with $y = b$. If the revised domain equals
$\mathrm{dom}(x)$, AC-3 continues from $\mathrm{dom}$ with the rest of $q$; otherwise it replaces
the domain of $x$ by the revised domain and continues with the rest of $q$ followed by the arcs
$(z, x)$ of $P$ with $z \ne y$, in the order of the arc list of $P$. Each revision costs one unit
of time.

Formalized by `Cslib.Algorithms.Lean.ArcConsistency.ac3`, a definition declared in [CSLibExt/Algorithms/Lean/CSP/AC3.lean, line 130](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/CSP/AC3.lean#L130). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/heuristic-search-and-planning/ac-3-algorithm/index.html#ac3).

## AC-3 on the whole problem

For a binary CSP $P$ with finitely many variables and
domains $\mathrm{dom}$, AC-3 on the whole problem is AC-3 run from $\mathrm{dom}$ with the queue
initialized to the arc list of $P$; it returns the final domains together with the number of
revisions performed.

Formalized by `Cslib.Algorithms.Lean.ArcConsistency.ac3All`, a definition declared in [CSLibExt/Algorithms/Lean/CSP/AC3.lean, line 142](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/CSP/AC3.lean#L142). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/heuristic-search-and-planning/ac-3-algorithm/index.html#ac3-all).

## AC-3 only shrinks domains

For a binary CSP $P$ with finitely many variables, domains
$\mathrm{dom}$, a queue $q$ of pairs of variables and a variable $v$, the domain of $v$ returned
by AC-3 run from $\mathrm{dom}$ with queue $q$ is a subset of $\mathrm{dom}(v)$.

Formalized by `Cslib.Algorithms.Lean.ArcConsistency.ac3_subset`, a theorem declared in [CSLibExt/Algorithms/Lean/CSP/AC3.lean, line 147](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/CSP/AC3.lean#L147). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/heuristic-search-and-planning/ac-3-algorithm/index.html#ac3-subset).

## Revision keeps solution values

Let $P$ be a binary constraint satisfaction problem,
$\mathrm{dom}$ finite domains for its variables and $\sigma$ a solution of $P$ within
$\mathrm{dom}$. For every arc $(x, y)$ of $P$, the value $\sigma(x)$ lies in the revision of the
arc $(x, y)$ with respect to $\mathrm{dom}$.

Formalized by `Cslib.Algorithms.Lean.ArcConsistency.mem_revise_of_isSolution`, a theorem declared in [CSLibExt/Algorithms/Lean/CSP/AC3.lean, line 167](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/CSP/AC3.lean#L167). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/heuristic-search-and-planning/ac-3-algorithm/index.html#mem-revise-of-is-solution).

## No solution is lost

Let $P$ be a binary constraint satisfaction problem with finitely
many variables, $\mathrm{dom}$ finite domains for its variables, and $q$ a queue of arcs each of
which is an arc of $P$. Then every solution $\sigma$ of $P$ within $\mathrm{dom}$ is also a
solution of $P$ within the domains returned by AC-3 started from $\mathrm{dom}$ with queue $q$.

Formalized by `Cslib.Algorithms.Lean.ArcConsistency.isSolution_ac3`, a theorem declared in [CSLibExt/Algorithms/Lean/CSP/AC3.lean, line 175](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/CSP/AC3.lean#L175). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/heuristic-search-and-planning/ac-3-algorithm/index.html#is-solution-ac3).

## Solutions survive AC-3

Let $P$ be a binary constraint satisfaction problem with
finitely many variables and $\mathrm{dom}$ finite domains for its variables. If $\sigma$ is a
solution of $P$ within $\mathrm{dom}$, then for every variable $v$ the value $\sigma(v)$ lies in
the domain of $v$ returned by AC-3 run from $\mathrm{dom}$ with all arcs of $P$ queued.

Formalized by `Cslib.Algorithms.Lean.ArcConsistency.mem_ac3_of_isSolution`, a theorem declared in [CSLibExt/Algorithms/Lean/CSP/AC3.lean, line 199](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/CSP/AC3.lean#L199). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/heuristic-search-and-planning/ac-3-algorithm/index.html#mem-ac3-of-is-solution).

## An emptied domain rules out solutions

Let $P$ be a binary constraint satisfaction
problem with finitely many variables and $\mathrm{dom}$ finite domains for its variables. If AC-3,
run from $\mathrm{dom}$ with all arcs of $P$ queued, returns the empty domain for some variable
$v$, then no assignment $\sigma$ is a solution of $P$ within $\mathrm{dom}$.

Formalized by `Cslib.Algorithms.Lean.ArcConsistency.not_isSolution_of_ac3_eq_empty`, a theorem declared in [CSLibExt/Algorithms/Lean/CSP/AC3.lean, line 204](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/CSP/AC3.lean#L204). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/heuristic-search-and-planning/ac-3-algorithm/index.html#not-is-solution-of-ac3-eq-empty).

## Arc consistency after one AC-3 revision

Let $P$ be a binary CSP whose constraints are
symmetric, that is the arc $(x, y)$ allows $(a, b)$ exactly when the arc $(y, x)$ allows $(b, a)$.
Let $\mathrm{dom}$ be domains, let $x \ne y$ be variables, let $R$ be the set of values
$a \in \mathrm{dom}(x)$ for which some $b \in \mathrm{dom}(y)$ has the arc $(x, y)$ allowing
$x = a$ together with $y = b$, and let $\mathrm{dom}'$ be $\mathrm{dom}$ with the domain of $x$
replaced by $R$. Let $e$ be an arc of $P$ with two distinct endpoints such that $e = (x, y)$ or
$e$ is consistent with respect to $\mathrm{dom}$, and such that, if $R \ne \mathrm{dom}(x)$, then
$e$ is not of the form $(z, x)$ with $z \ne y$. Then $e$ is consistent with respect to
$\mathrm{dom}'$.

Formalized by `Cslib.Algorithms.Lean.ArcConsistency.arcConsistent_step`, a theorem declared in [CSLibExt/Algorithms/Lean/CSP/AC3.lean, line 215](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/CSP/AC3.lean#L215). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/heuristic-search-and-planning/ac-3-algorithm/index.html#arc-consistent-step).

## Arc consistency invariant of AC-3

Let $P$ be a binary CSP with finitely many variables
whose constraints are symmetric, that is the arc $(x, y)$ allows $(a, b)$ exactly when the arc
$(y, x)$ allows $(b, a)$, and whose arcs all join two distinct variables. Let $\mathrm{dom}$ be
domains and $q$ a queue whose entries are arcs of $P$, such that every arc of $P$ not in $q$ is
consistent with respect to $\mathrm{dom}$. Then every arc of $P$ is consistent with respect to the
domains returned by AC-3 run from $\mathrm{dom}$ with queue $q$.

The invariant: every arc of the problem outside the queue stays consistent, and at the end the
queue is empty.

Formalized by `Cslib.Algorithms.Lean.ArcConsistency.arcConsistent_ac3_of_inv`, a theorem declared in [CSLibExt/Algorithms/Lean/CSP/AC3.lean, line 253](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/CSP/AC3.lean#L253). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/heuristic-search-and-planning/ac-3-algorithm/index.html#arc-consistent-ac3-of-inv).

## AC-3 makes every arc consistent

**AC-3 makes every arc consistent**, for constraints given symmetrically on both
orientations of an arc and arcs between distinct variables.

Formalized by `Cslib.Algorithms.Lean.ArcConsistency.arcConsistent_ac3`, a theorem declared in [CSLibExt/Algorithms/Lean/CSP/AC3.lean, line 290](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/CSP/AC3.lean#L290). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/heuristic-search-and-planning/ac-3-algorithm/index.html#arc-consistent-ac3).

## AC-3 revisions are bounded by the potential

For a binary CSP $P$ with finitely many
variables, domains $\mathrm{dom}$ and a queue $q$ of pairs of variables, the number of revisions
AC-3 performs from $\mathrm{dom}$ with queue $q$ is at most the potential
$\ell + \sum_x |\mathrm{dom}(x)| \cdot \mathrm{indeg}(x)$, where $\ell$ is the length of $q$ and
$\mathrm{indeg}(x)$ is the number of entries of the arc list of $P$ ending at $x$.

Each revision lowers the potential by at least $1$.

Formalized by `Cslib.Algorithms.Lean.ArcConsistency.ac3_time_le_potential`, a theorem declared in [CSLibExt/Algorithms/Lean/CSP/AC3.lean, line 298](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/CSP/AC3.lean#L298). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/heuristic-search-and-planning/ac-3-algorithm/index.html#ac3-time-le-potential).

## Bound on the number of AC-3 revisions

For a binary CSP $P$ with finitely many variables
and initial domains $\mathrm{dom}$, AC-3 run from $\mathrm{dom}$ with every arc of $P$ queued
performs at most $m + \sum_x |\mathrm{dom}(x)| \cdot \mathrm{indeg}(x)$ revisions, where $m$ is
the length of the arc list of $P$ and $\mathrm{indeg}(x)$ is the number of entries of that list
ending at $x$.

This is $O(e d)$ for $e$ arcs and domains of size $d$.

Formalized by `Cslib.Algorithms.Lean.ArcConsistency.ac3_time_le`, a theorem declared in [CSLibExt/Algorithms/Lean/CSP/AC3.lean, line 320](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/CSP/AC3.lean#L320). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/heuristic-search-and-planning/ac-3-algorithm/index.html#ac3-time-le).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: AC-3 algorithm](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/heuristic-search-and-planning/ac-3-algorithm/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/ComputerScience/heuristic-search-and-planning/ac-3-algorithm)
