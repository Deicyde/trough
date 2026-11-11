---
declaration: section
origin: cited
lean: MathlibExt.GroupTheory.WordProblemSolvableShared.WordProblemSolvable, MathlibExt.GroupTheory.NovikovUnsolvableWanted.GroupTheory.NovikovUnsolvableProblem.novikov_unsolvable
statement: formalized
---

# Word problem for groups

2 results, 1 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/presentations-and-decision-problems/word-problem-for-groups/index.html).

## Solvable word problem

Let $G$ be a group, $n$ a natural number and $\varphi$ a
homomorphism from the free group on $n$ generators to $G$. The word problem is solvable for
$\varphi$ when the predicate on words $w$ (finite lists of letters, each a generator together
with a sign) given by $\varphi(w) = 1$ in $G$ is computable: some algorithm decides, given a
word $w$, whether $\varphi(w) = 1$.

When $\varphi$ is surjective, for instance the quotient map of a presentation of $G$ on $n$
generators, this is the classical word problem for $G$ with respect to these generators.

Formalized by `MathlibExt.GroupTheory.WordProblemSolvableShared.WordProblemSolvable`, a definition declared in [WantedExt/GroupTheory/WordProblemSolvableShared.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/WordProblemSolvableShared.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/presentations-and-decision-problems/word-problem-for-groups/index.html#word-problem-solvable).

## Novikov–Boone theorem (unsolvability of the word problem)

There exist a natural number
$n$ and a finite set $R$ of elements of the free group $F_n$ on generators $g_1, \dots, g_n$ such
that the word problem of the canonical surjection from $F_n$ onto the presented group
$\langle g_1, \dots, g_n \mid R \rangle$ is not solvable: no algorithm decides, for a word $w$ in
the $g_i$ and their inverses, whether $w$ represents the identity of
$\langle g_1, \dots, g_n \mid R \rangle$.

## Sources

- P.S. Novikov, 'On the algorithmic unsolvability of the word problem in group theory', Trudy Mat. Inst. Steklov. 44 (1955) 1–143 (Russian); W.W. Boone, 'The word problem', Ann. of Math. (2) 70 (1959) 207–265 (announced 1958). §122 in O. Knill, *Some Fundamental Theorems in Mathematics* (https://people.math.harvard.edu/~knill/graphgeometry/papers/fundamental.pdf). Problem `novikov_unsolvable` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.GroupTheory.NovikovUnsolvableWanted.GroupTheory.NovikovUnsolvableProblem.novikov_unsolvable` is written with `theorem_wanted` in [WantedExt/GroupTheory/NovikovUnsolvableWanted.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/NovikovUnsolvableWanted.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/presentations-and-decision-problems/word-problem-for-groups/index.html#novikov-unsolvable).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Word problem for groups](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/presentations-and-decision-problems/word-problem-for-groups/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/GroupTheory/presentations-and-decision-problems/word-problem-for-groups)
