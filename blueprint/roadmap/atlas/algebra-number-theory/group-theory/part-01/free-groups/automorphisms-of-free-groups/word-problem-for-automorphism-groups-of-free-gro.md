---
declaration: section
origin: cited
lean: MathlibExt.GroupTheory.AutFreeGroupWordProblemPolyTimeKourovka16Problem109Wanted.evalAutWord, MathlibExt.GroupTheory.AutFreeGroupWordProblemPolyTimeKourovka16Problem109Wanted.autWordProblem, MathlibExt.GroupTheory.AutFreeGroupWordProblemPolyTimeKourovka16Problem109Wanted.autFreeGroupWordProblemInP, MathlibExt.GroupTheory.AutFreeGroupWordProblemPolyTimeKourovka16Problem109Wanted.autFreeGroupWordProblemInP_holds
statement: formalized
---

# Word problem for automorphism groups of free groups

4 results, 3 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/free-groups/automorphisms-of-free-groups/word-problem-for-automorphism-groups-of-free-gro/index.html).

## The automorphism spelled by a word

Let $F_n$ be the free group on $n$ generators and let
$g_0, \dots, g_{k-1}$ be automorphisms of $F_n$. A word $w = ((i_1, b_1), \dots, (i_r, b_r))$ is a
finite list of letters $(i, b)$ with $i \in \mathbb{N}$ and $b$ a boolean. The automorphism
spelled by $w$ over $(g_i)$ is the product $a_1 a_2 \cdots a_r$ in $\operatorname{Aut}(F_n)$,
whose group operation is composition, where for $i_j < k$ the factor $a_j$ is $g_{i_j}$ if $b_j$ is
true and $g_{i_j}^{-1}$ if $b_j$ is false, and for $i_j \ge k$ the factor $a_j$ is the identity.
The empty word spells the identity.

Formalized by `MathlibExt.GroupTheory.AutFreeGroupWordProblemPolyTimeKourovka16Problem109Wanted.evalAutWord`, a definition declared in [WantedExt/GroupTheory/AutFreeGroupWordProblemPolyTimeKourovka16Problem109Wanted.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/AutFreeGroupWordProblemPolyTimeKourovka16Problem109Wanted.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/free-groups/automorphisms-of-free-groups/word-problem-for-automorphism-groups-of-free-gro/index.html#eval-aut-word).

## The word problem of Aut(Fₙ) for a family of automorphisms

Let $F_n$ be the free group on
$n$ generators and let $g_0, \dots, g_{k-1}$ be automorphisms of $F_n$. A word is a finite list of
letters $(i, b)$ with $i \in \mathbb{N}$ and $b$ a boolean. The word problem for $(g_i)$ is the
decision problem that accepts a bitstring $x$ exactly when $x$ decodes, under the canonical
bitstring encoding of lists of pairs of a natural number and a boolean, to a word $w$ such that
every letter $(i, b)$ of $w$ has $i < k$ and the automorphism spelled by $w$ over $(g_i)$ is the
identity; here the letter $(i, \mathrm{true})$ stands for $g_i$ and $(i, \mathrm{false})$ for
$g_i^{-1}$. Bitstrings that do not decode to a word are rejected.

Formalized by `MathlibExt.GroupTheory.AutFreeGroupWordProblemPolyTimeKourovka16Problem109Wanted.autWordProblem`, a definition declared in [WantedExt/GroupTheory/AutFreeGroupWordProblemPolyTimeKourovka16Problem109Wanted.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/AutFreeGroupWordProblemPolyTimeKourovka16Problem109Wanted.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/free-groups/automorphisms-of-free-groups/word-problem-for-automorphism-groups-of-free-gro/index.html#aut-word-problem).

## Polynomial-time word problem for Aut(Fₙ) (Kourovka 16.109)

The proposition that for
every $n \ge 2$, writing $F_n$ for the free group on $n$ generators, for every natural number $k$
and every family $g_0, \dots, g_{k-1}$ of automorphisms of $F_n$ that generates
$\operatorname{Aut}(F_n)$, the word problem of $\operatorname{Aut}(F_n)$ for the family
$(g_i)$, a decision problem on bitstrings, belongs to the complexity class P.

Formalized by `MathlibExt.GroupTheory.AutFreeGroupWordProblemPolyTimeKourovka16Problem109Wanted.autFreeGroupWordProblemInP`, a definition declared in [WantedExt/GroupTheory/AutFreeGroupWordProblemPolyTimeKourovka16Problem109Wanted.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/AutFreeGroupWordProblemPolyTimeKourovka16Problem109Wanted.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/free-groups/automorphisms-of-free-groups/word-problem-for-automorphism-groups-of-free-gro/index.html#aut-free-group-word-problem-in-p).

## The word problem for Aut(Fₙ) is solvable in polynomial time

Let $n \ge 2$ and let $F_n$ be the
free group on $n$ generators. For every natural number $k$ and every family
$g_0, \dots, g_{k-1}$ of automorphisms of $F_n$ that generates $\operatorname{Aut}(F_n)$, the word
problem of $\operatorname{Aut}(F_n)$ for this family belongs to the complexity class P. Here a word
is a finite list of letters $(i, b)$ with $i \in \mathbb{N}$ and $b$ a boolean, the letter
$(i, \mathrm{true})$ standing for $g_i$ and $(i, \mathrm{false})$ for $g_i^{-1}$, and the word
problem is the decision problem on bitstrings that accepts exactly the bitstrings that decode,
under the canonical bitstring encoding of lists of pairs of a natural number and a boolean, to a
word whose letter indices are all below $k$ and whose product in $\operatorname{Aut}(F_n)$ is the
identity; bitstrings that do not decode to a word are rejected.

Schleimer proves (Theorem 5.2) that the word problem for $\operatorname{Aut}(F_m)$ is solvable in
polynomial time, and observes (Remark 5.1) that changing the generating set alters running times
by at most a multiplicative constant; the Kourovka Archive answers 16.109 "Yes, there is".

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Archive of Solved Problems, Problem 16.109 (V. E. Shpilrain); resolution: S. Schleimer, Polynomial-time word problems, Comment. Math. Helv. 83 (2008), 741-765, Theorem 5.2 (the word problem for Aut(F_m) is polynomial time) and Remark 5.1 (choosing a different generating set alters running times by at most a multiplicative constant); Kourovka Archive, Problem 16.109 (Yes, there is), https://wrap.warwick.ac.uk/44057/.

Stated but not proved: `MathlibExt.GroupTheory.AutFreeGroupWordProblemPolyTimeKourovka16Problem109Wanted.autFreeGroupWordProblemInP_holds` is written with `theorem_wanted` in [WantedExt/GroupTheory/AutFreeGroupWordProblemPolyTimeKourovka16Problem109Wanted.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/AutFreeGroupWordProblemPolyTimeKourovka16Problem109Wanted.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/free-groups/automorphisms-of-free-groups/word-problem-for-automorphism-groups-of-free-gro/index.html#aut-free-group-word-problem-in-p-holds).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Word problem for automorphism groups of free groups](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/free-groups/automorphisms-of-free-groups/word-problem-for-automorphism-groups-of-free-gro/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/GroupTheory/free-groups/automorphisms-of-free-groups/word-problem-for-automorphism-groups-of-free-gro)
