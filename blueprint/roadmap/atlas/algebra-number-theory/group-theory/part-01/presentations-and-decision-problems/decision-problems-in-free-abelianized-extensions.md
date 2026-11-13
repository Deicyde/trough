---
declaration: section
origin: cited
lean: MathlibExt.GroupTheory.MetabelianizationDecisionProblemsKourovka12Problem98Wanted.IsRecursivelyEnumerable, MathlibExt.GroupTheory.MetabelianizationDecisionProblemsKourovka12Problem98Wanted.WordProblemSolvable, MathlibExt.GroupTheory.MetabelianizationDecisionProblemsKourovka12Problem98Wanted.ConjugacyProblemSolvable, MathlibExt.GroupTheory.MetabelianizationDecisionProblemsKourovka12Problem98Wanted.wordProblemIffMetabelianization, MathlibExt.GroupTheory.MetabelianizationDecisionProblemsKourovka12Problem98Wanted.conjugacyProblemIffMetabelianization, MathlibExt.GroupTheory.MetabelianizationDecisionProblemsKourovka12Problem98Wanted.metabelianizationWordProblemSolvesConjugacy, MathlibExt.GroupTheory.MetabelianizationDecisionProblemsKourovka12Problem98Wanted.wordProblemIffMetabelianization_holds, MathlibExt.GroupTheory.MetabelianizationDecisionProblemsKourovka12Problem98Wanted.conjugacyProblemIffMetabelianization_refuted
statement: formalized
---

# Decision problems in free abelianized extensions

9 results, 6 proved and 3 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/presentations-and-decision-problems/decision-problems-in-free-abelianized-extensions/index.html).

## Recursively enumerable subgroup of a free group

Let $n$ be a natural number and let $F$
be the free group on the generators $x_0, \dots, x_{n-1}$. A subgroup $N$ of $F$ is recursively
enumerable when the set of words $w$ (finite lists of letters, each a generator together with a
sign) whose image in $F$ lies in $N$ is recursively enumerable.

Formalized by `MathlibExt.GroupTheory.MetabelianizationDecisionProblemsKourovka12Problem98Wanted.IsRecursivelyEnumerable`, a definition declared in [WantedExt/GroupTheory/MetabelianizationDecisionProblemsKourovka12Problem98Wanted.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/MetabelianizationDecisionProblemsKourovka12Problem98Wanted.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/presentations-and-decision-problems/decision-problems-in-free-abelianized-extensions/index.html#is-recursively-enumerable).

## Solvable word problem for a quotient of a free group

Let $n$ be a natural number, let $F$
be the free group on the generators $x_0, \dots, x_{n-1}$ and let $N$ be a subgroup of $F$. The word
problem for $F / N$ is solvable when membership in $N$ is decidable: the predicate on words $w$
(finite lists of letters, each a generator together with a sign) that the image of $w$ in $F$ lies
in $N$ is computable.

Formalized by `MathlibExt.GroupTheory.MetabelianizationDecisionProblemsKourovka12Problem98Wanted.WordProblemSolvable`, a definition declared in [WantedExt/GroupTheory/MetabelianizationDecisionProblemsKourovka12Problem98Wanted.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/MetabelianizationDecisionProblemsKourovka12Problem98Wanted.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/presentations-and-decision-problems/decision-problems-in-free-abelianized-extensions/index.html#word-problem-solvable).

## Solvable conjugacy problem for a quotient of a free group

Let $n$ be a natural number,
let $F$ be the free group on the generators $x_0, \dots, x_{n-1}$ and let $N$ be a subgroup of $F$.
The conjugacy problem for $F / N$ is solvable when the predicate on pairs of words $(w, v)$ (finite
lists of letters, each a generator together with a sign) that some $u \in F$ satisfies
$u w u^{-1} v^{-1} \in N$, with $w$ and $v$ read as elements of $F$, is computable.

When $N$ is normal, this says that conjugacy of the images of $w$ and $v$ in $F / N$ is
decidable.

Formalized by `MathlibExt.GroupTheory.MetabelianizationDecisionProblemsKourovka12Problem98Wanted.ConjugacyProblemSolvable`, a definition declared in [WantedExt/GroupTheory/MetabelianizationDecisionProblemsKourovka12Problem98Wanted.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/MetabelianizationDecisionProblemsKourovka12Problem98Wanted.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/presentations-and-decision-problems/decision-problems-in-free-abelianized-extensions/index.html#conjugacy-problem-solvable).

## Kourovka Problem 12.98(a) (V. E. Shpil'rain)

The statement that for every natural
number $n$ and every recursively enumerable normal subgroup $R$ of the free group $F$ on $n$
generators, with commutator subgroup $[R, R]$, the word problem for $F / R$ is solvable if and only
if the word problem for $F / [R, R]$ is solvable.

Formalized by `MathlibExt.GroupTheory.MetabelianizationDecisionProblemsKourovka12Problem98Wanted.wordProblemIffMetabelianization`, a definition declared in [WantedExt/GroupTheory/MetabelianizationDecisionProblemsKourovka12Problem98Wanted.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/MetabelianizationDecisionProblemsKourovka12Problem98Wanted.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/presentations-and-decision-problems/decision-problems-in-free-abelianized-extensions/index.html#word-problem-iff-metabelianization).

## Kourovka Problem 12.98(b) (V. E. Shpil'rain)

The statement that for every natural
number $n$ and every recursively enumerable normal subgroup $R$ of the free group $F$ on $n$
generators, with commutator subgroup $[R, R]$, the conjugacy problem for $F / R$ is solvable if and
only if the conjugacy problem for $F / [R, R]$ is solvable.

Formalized by `MathlibExt.GroupTheory.MetabelianizationDecisionProblemsKourovka12Problem98Wanted.conjugacyProblemIffMetabelianization`, a definition declared in [WantedExt/GroupTheory/MetabelianizationDecisionProblemsKourovka12Problem98Wanted.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/MetabelianizationDecisionProblemsKourovka12Problem98Wanted.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/presentations-and-decision-problems/decision-problems-in-free-abelianized-extensions/index.html#conjugacy-problem-iff-metabelianization).

## Kourovka Problem 12.98(c) (V. E. Shpil'rain)

The statement that for every natural
number $n$ and every recursively enumerable normal subgroup $R$ of the free group $F$ on $n$
generators, with commutator subgroup $[R, R]$, if the word problem for $F / [R, R]$ is solvable
then the conjugacy problem for $F / [R, R]$ is solvable.

Formalized by `MathlibExt.GroupTheory.MetabelianizationDecisionProblemsKourovka12Problem98Wanted.metabelianizationWordProblemSolvesConjugacy`, a definition declared in [WantedExt/GroupTheory/MetabelianizationDecisionProblemsKourovka12Problem98Wanted.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/MetabelianizationDecisionProblemsKourovka12Problem98Wanted.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/presentations-and-decision-problems/decision-problems-in-free-abelianized-extensions/index.html#metabelianization-word-problem-solves-co).

## Kourovka 12.98(a) has a positive answer

For every natural number $n$ and every recursively
enumerable normal subgroup $R$ of the free group $F$ on $n$ generators, with commutator subgroup
$[R, R]$, the word problem for $F / R$ is solvable if and only if the word problem for $F / [R, R]$
is solvable.

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Archive of Solved Problems, Problem 12.98 (V. E. Shpil'rain); resolution: M. I. Anokhin, Math. Notes 61 (1997), no. 1-2, 3-8, Kourovka Archive, Problem 12.98: a) Yes, it is; b) No, it is not; c) No, it is not.

Stated but not proved: `MathlibExt.GroupTheory.MetabelianizationDecisionProblemsKourovka12Problem98Wanted.wordProblemIffMetabelianization_holds` is written with `theorem_wanted` in [WantedExt/GroupTheory/MetabelianizationDecisionProblemsKourovka12Problem98Wanted.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/MetabelianizationDecisionProblemsKourovka12Problem98Wanted.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/presentations-and-decision-problems/decision-problems-in-free-abelianized-extensions/index.html#word-problem-iff-metabelianization-holds).

## Kourovka 12.98(b) has a negative answer

It is not the case that for every natural number $n$
and every recursively enumerable normal subgroup $R$ of the free group $F$ on $n$ generators, with
commutator subgroup $[R, R]$, the conjugacy problem for $F / R$ is solvable if and only if the
conjugacy problem for $F / [R, R]$ is solvable: for some such $n$ and $R$, exactly one of these two
conjugacy problems is solvable.

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Archive of Solved Problems, Problem 12.98 (V. E. Shpil'rain); resolution: M. I. Anokhin, Math. Notes 61 (1997), no. 1-2, 3-8, Kourovka Archive, Problem 12.98: a) Yes, it is; b) No, it is not; c) No, it is not.

Stated but not proved: `MathlibExt.GroupTheory.MetabelianizationDecisionProblemsKourovka12Problem98Wanted.conjugacyProblemIffMetabelianization_refuted` is written with `theorem_wanted` in [WantedExt/GroupTheory/MetabelianizationDecisionProblemsKourovka12Problem98Wanted.lean, line 92](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/MetabelianizationDecisionProblemsKourovka12Problem98Wanted.lean#L92). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/presentations-and-decision-problems/decision-problems-in-free-abelianized-extensions/index.html#conjugacy-problem-iff-metabelianization-2).

## Kourovka 12.98(c) has a negative answer

It is not the case that for every natural number $n$
and every recursively enumerable normal subgroup $R$ of the free group $F$ on $n$ generators, with
commutator subgroup $[R, R]$, solvability of the word problem for $F / [R, R]$ implies solvability
of the conjugacy problem for $F / [R, R]$: for some such $n$ and $R$, the word problem for
$F / [R, R]$ is solvable but its conjugacy problem is not.

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Archive of Solved Problems, Problem 12.98 (V. E. Shpil'rain); resolution: M. I. Anokhin, Math. Notes 61 (1997), no. 1-2, 3-8, Kourovka Archive, Problem 12.98: a) Yes, it is; b) No, it is not; c) No, it is not.

Stated but not proved: `MathlibExt.GroupTheory.MetabelianizationDecisionProblemsKourovka12Problem98Wanted.metabelianizationWordProblemSolvesConjugacy_refuted` is written with `theorem_wanted` in [WantedExt/GroupTheory/MetabelianizationDecisionProblemsKourovka12Problem98Wanted.lean, line 102](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/MetabelianizationDecisionProblemsKourovka12Problem98Wanted.lean#L102). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/presentations-and-decision-problems/decision-problems-in-free-abelianized-extensions/index.html#metabelianization-word-problem-solves-co-2).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Decision problems in free abelianized extensions](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/presentations-and-decision-problems/decision-problems-in-free-abelianized-extensions/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/GroupTheory/presentations-and-decision-problems/decision-problems-in-free-abelianized-extensions)
