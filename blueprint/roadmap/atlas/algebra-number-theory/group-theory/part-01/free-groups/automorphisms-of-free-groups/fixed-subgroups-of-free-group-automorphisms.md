---
declaration: section
origin: cited
lean: MathlibExt.GroupTheory.FixedSubgroupBasisLengthKourovka14Problem23Wanted.autNorm, MathlibExt.GroupTheory.FixedSubgroupBasisLengthKourovka14Problem23Wanted.fixedSubgroup, MathlibExt.GroupTheory.FixedSubgroupBasisLengthKourovka14Problem23Wanted.HasShortFixedBasis, MathlibExt.GroupTheory.FixedSubgroupBasisLengthKourovka14Problem23Wanted.fixedSubgroupBasisRecursiveBoundEachRank, MathlibExt.GroupTheory.FixedSubgroupBasisLengthKourovka14Problem23Wanted.fixedSubgroupBasisRecursiveBoundUniform, MathlibExt.GroupTheory.FixedSubgroupBasisLengthKourovka14Problem23Wanted.fixedSubgroupBasisRecursiveBoundEachRank_holds, MathlibExt.GroupTheory.FixedSubgroupBasisLengthKourovka14Problem23Wanted.fixedSubgroupBasisRecursiveBoundUniform_refuted, MathlibExt.GroupTheory.FreeGroupAutomorphismFixedPointKourovka10Problem25Wanted.Word
statement: formalized
---

# Fixed subgroups of free group automorphisms

11 results, 8 proved and 3 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/free-groups/automorphisms-of-free-groups/fixed-subgroups-of-free-group-automorphisms/index.html).

## Norm of an automorphism of a free group

Let $F_n$ be the free group on the basis
$x_0, \dots, x_{n-1}$, and for $w \in F_n$ let $|w|$ be the length of the reduced word
representing $w$. The norm of an automorphism $\alpha$ of $F_n$ is
$\|\alpha\| = \max(|\alpha(x_0)|, \dots, |\alpha(x_{n-1})|)$, taken to be $0$ when $n = 0$.

Formalized by `MathlibExt.GroupTheory.FixedSubgroupBasisLengthKourovka14Problem23Wanted.autNorm`, a definition declared in [WantedExt/GroupTheory/FixedSubgroupBasisLengthKourovka14Problem23Wanted.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/FixedSubgroupBasisLengthKourovka14Problem23Wanted.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/free-groups/automorphisms-of-free-groups/fixed-subgroups-of-free-group-automorphisms/index.html#aut-norm).

## Fixed subgroup of a free group automorphism

For an automorphism $\alpha$ of the free
group $F_n$ on $x_0, \dots, x_{n-1}$, the fixed subgroup of $\alpha$ is the subgroup
$\mathrm{Fix}(\alpha) = \{x \in F_n \mid \alpha(x) = x\}$ of $F_n$.

Formalized by `MathlibExt.GroupTheory.FixedSubgroupBasisLengthKourovka14Problem23Wanted.fixedSubgroup`, a definition declared in [WantedExt/GroupTheory/FixedSubgroupBasisLengthKourovka14Problem23Wanted.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/FixedSubgroupBasisLengthKourovka14Problem23Wanted.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/free-groups/automorphisms-of-free-groups/fixed-subgroups-of-free-group-automorphisms/index.html#fixed-subgroup).

## Fixed subgroups with a short free basis

Let $\alpha$ be an automorphism of the free group
$F_n$ on $x_0, \dots, x_{n-1}$, let $|w|$ be the length of the reduced word representing
$w \in F_n$, and let $L$ be a natural number. The fixed subgroup $\mathrm{Fix}(\alpha)$ has a
short free basis with bound $L$ when, for some $k \ge 0$, it has a free basis
$y_1, \dots, y_k$ with $|y_i| \le L$ for every $i$.

Formalized by `MathlibExt.GroupTheory.FixedSubgroupBasisLengthKourovka14Problem23Wanted.HasShortFixedBasis`, a definition declared in [WantedExt/GroupTheory/FixedSubgroupBasisLengthKourovka14Problem23Wanted.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/FixedSubgroupBasisLengthKourovka14Problem23Wanted.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/free-groups/automorphisms-of-free-groups/fixed-subgroups-of-free-group-automorphisms/index.html#has-short-fixed-basis).

## Kourovka Problem 14.23, rank-dependent form

For every $n$ there is a computable
function $f : \mathbb{N} \to \mathbb{N}$ such that for every automorphism $\alpha$ of the free
group $F_n$ on $x_0, \dots, x_{n-1}$, the fixed subgroup $\mathrm{Fix}(\alpha)$ has a finite
free basis all of whose elements have reduced word length at most $f(\|\alpha\|)$, where
$\|\alpha\|$ is the maximum of the reduced word lengths of $\alpha(x_0), \dots, \alpha(x_{n-1})$.

This is the form of Kourovka Notebook Problem 14.23 (O. V. Bogopolski) in which $f$ may depend
on the rank $n$.

Formalized by `MathlibExt.GroupTheory.FixedSubgroupBasisLengthKourovka14Problem23Wanted.fixedSubgroupBasisRecursiveBoundEachRank`, a definition declared in [WantedExt/GroupTheory/FixedSubgroupBasisLengthKourovka14Problem23Wanted.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/FixedSubgroupBasisLengthKourovka14Problem23Wanted.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/free-groups/automorphisms-of-free-groups/fixed-subgroups-of-free-group-automorphisms/index.html#fixed-subgroup-basis-recursive-bound-eac).

## Kourovka Problem 14.23, rank-uniform form

There is a computable function
$f : \mathbb{N} \to \mathbb{N}$ such that for every $n$ and every automorphism $\alpha$ of the
free group $F_n$ on $x_0, \dots, x_{n-1}$, the fixed subgroup $\mathrm{Fix}(\alpha)$ has a
finite free basis all of whose elements have reduced word length at most $f(\|\alpha\|)$, where
$\|\alpha\|$ is the maximum of the reduced word lengths of $\alpha(x_0), \dots, \alpha(x_{n-1})$.

This is the form of Kourovka Notebook Problem 14.23 (O. V. Bogopolski) in which one $f$ must
work for all ranks $n$.

Formalized by `MathlibExt.GroupTheory.FixedSubgroupBasisLengthKourovka14Problem23Wanted.fixedSubgroupBasisRecursiveBoundUniform`, a definition declared in [WantedExt/GroupTheory/FixedSubgroupBasisLengthKourovka14Problem23Wanted.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/FixedSubgroupBasisLengthKourovka14Problem23Wanted.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/free-groups/automorphisms-of-free-groups/fixed-subgroups-of-free-group-automorphisms/index.html#fixed-subgroup-basis-recursive-bound-uni).

## Kourovka Problem 14.23 holds for each rank

For every $n$ there is a computable function
$f : \mathbb{N} \to \mathbb{N}$ such that for every automorphism $\alpha$ of the free group $F_n$
on $x_0, \dots, x_{n-1}$, the fixed subgroup $\mathrm{Fix}(\alpha)$ has a finite free basis all
of whose elements have reduced word length at most $f(\|\alpha\|)$, where $\|\alpha\|$ is the
maximum of the reduced word lengths of $\alpha(x_0), \dots, \alpha(x_{n-1})$.

This follows from the algorithm computing a basis of $\mathrm{Fix}(\alpha)$ (Kharlampovich,
Proposition 2); the Kourovka Notebook (21st issue) records this answer.

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Problem 14.23 (O. V. Bogopolski); resolution: O. Kharlampovich, Two observations on Problems 14.23 and 17.32 of the Kourovka Notebook, preprint (2026), Proposition 2 (each rank); O. Kharlampovich, A counterexample to the rank-uniform form of Kourovka Notebook Problem 14.23, preprint (2026), Theorem 1, the Kourovka Notebook (21st issue) marks 14.23 solved: true for each given rank, false if one function must work for all ranks, https://kourovkanotebookorg.wordpress.com/wp-content/uploads/2026/08/kourovka_14_23_uniform_counterexample.pdf.

Stated but not proved: `MathlibExt.GroupTheory.FixedSubgroupBasisLengthKourovka14Problem23Wanted.fixedSubgroupBasisRecursiveBoundEachRank_holds` is written with `theorem_wanted` in [WantedExt/GroupTheory/FixedSubgroupBasisLengthKourovka14Problem23Wanted.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/FixedSubgroupBasisLengthKourovka14Problem23Wanted.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/free-groups/automorphisms-of-free-groups/fixed-subgroups-of-free-group-automorphisms/index.html#fixed-subgroup-basis-recursive-bound-eac-2).

## Kourovka Problem 14.23 fails uniformly in the rank

There is no computable function
$f : \mathbb{N} \to \mathbb{N}$ such that for every $n$ and every automorphism $\alpha$ of the
free group $F_n$ on $x_0, \dots, x_{n-1}$, the fixed subgroup $\mathrm{Fix}(\alpha)$ has a
finite free basis all of whose elements have reduced word length at most $f(\|\alpha\|)$, where
$\|\alpha\|$ is the maximum of the reduced word lengths of $\alpha(x_0), \dots, \alpha(x_{n-1})$.

Kharlampovich (Theorem 1) proves more: for every $r \ge 3$ there is an automorphism $\alpha_r$
of the free group of rank $2r - 1$ with $\|\alpha_r\| = 3$ such that every generating set of
$\mathrm{Fix}(\alpha_r)$ contains an element of length at least $r$, so no function at all,
computable or not, works for all ranks; the Kourovka Notebook (21st issue) records this answer.

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Problem 14.23 (O. V. Bogopolski); resolution: O. Kharlampovich, Two observations on Problems 14.23 and 17.32 of the Kourovka Notebook, preprint (2026), Proposition 2 (each rank); O. Kharlampovich, A counterexample to the rank-uniform form of Kourovka Notebook Problem 14.23, preprint (2026), Theorem 1, the Kourovka Notebook (21st issue) marks 14.23 solved: true for each given rank, false if one function must work for all ranks, https://kourovkanotebookorg.wordpress.com/wp-content/uploads/2026/08/kourovka_14_23_uniform_counterexample.pdf.

Stated but not proved: `MathlibExt.GroupTheory.FixedSubgroupBasisLengthKourovka14Problem23Wanted.fixedSubgroupBasisRecursiveBoundUniform_refuted` is written with `theorem_wanted` in [WantedExt/GroupTheory/FixedSubgroupBasisLengthKourovka14Problem23Wanted.lean, line 96](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/FixedSubgroupBasisLengthKourovka14Problem23Wanted.lean#L96). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/free-groups/automorphisms-of-free-groups/fixed-subgroups-of-free-group-automorphisms/index.html#fixed-subgroup-basis-recursive-bound-uni-2).

## Encoded words in a free group of finite rank

A word of rank $r$ is a finite list of pairs
$(i, \varepsilon)$ with $i < r$ and $\varepsilon$ a Boolean. It encodes the element of the free
group $F_r$ of rank $r$ that is the product of its letters, where $(i, \mathrm{true})$ stands for
the $i$-th free generator and $(i, \mathrm{false})$ for its inverse.

Formalized by `MathlibExt.GroupTheory.FreeGroupAutomorphismFixedPointKourovka10Problem25Wanted.Word`, an abbreviation declared in [WantedExt/GroupTheory/FreeGroupAutomorphismFixedPointKourovka10Problem25Wanted.lean, line 40](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/FreeGroupAutomorphismFixedPointKourovka10Problem25Wanted.lean#L40). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/free-groups/automorphisms-of-free-groups/fixed-subgroups-of-free-group-automorphisms/index.html#word).

## Endomorphism of a free group given by generator images

Let $F_r$ be the free group on
generators $e_0, \dots, e_{r-1}$. Given, for each $i < r$, a word $u_i$ in these generators and
their inverses, this is the endomorphism of $F_r$ sending each $e_i$ to the element of $F_r$
represented by $u_i$.

Formalized by `MathlibExt.GroupTheory.FreeGroupAutomorphismFixedPointKourovka10Problem25Wanted.endo`, a definition declared in [WantedExt/GroupTheory/FreeGroupAutomorphismFixedPointKourovka10Problem25Wanted.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/FreeGroupAutomorphismFixedPointKourovka10Problem25Wanted.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/free-groups/automorphisms-of-free-groups/fixed-subgroups-of-free-group-automorphisms/index.html#endo).

## Decidability of fixed points of free group automorphisms (Kourovka 10.25)

The assertion
that for every natural number $r$ there is a computable function $f$ which takes the images of the
$r$ free generators of the free group $F_r$, each encoded as a word in the generators and their
inverses, and returns a Boolean, such that whenever the endomorphism $\varphi$ of $F_r$ sending each
generator to its image is bijective, $f$ returns true exactly when $\varphi(w) = w$ for some
$w \neq 1$ in $F_r$.

Formalized by `MathlibExt.GroupTheory.FreeGroupAutomorphismFixedPointKourovka10Problem25Wanted.automorphismFixedPointDecidable`, a definition declared in [WantedExt/GroupTheory/FreeGroupAutomorphismFixedPointKourovka10Problem25Wanted.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/FreeGroupAutomorphismFixedPointKourovka10Problem25Wanted.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/free-groups/automorphisms-of-free-groups/fixed-subgroups-of-free-group-automorphisms/index.html#automorphism-fixed-point-decidable).

## Fixed points of free group automorphisms are decidable (Kourovka 10.25)

For every natural
number $r$ there is a computable function $f$ which takes the images of the $r$ free generators of
the free group $F_r$, each encoded as a word in the generators and their inverses, and returns a
Boolean, such that whenever the endomorphism $\varphi$ of $F_r$ sending each generator to its image
is bijective, $f$ returns true exactly when $\varphi(w) = w$ for some $w \neq 1$ in $F_r$.

The Kourovka Archive answers Problem 10.25 "Yes, it does", citing Bogopolski and Maslakova (2016),
who give an algorithm computing a basis of the fixed subgroup of an automorphism of a free group of
finite rank; the automorphism has a non-trivial fixed point exactly when that basis is nonempty.

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Archive of Solved Problems, Problem 10.25 (G. S. Makanin); resolution: O. Bogopolski and O. Maslakova, Int. J. Algebra Comput. 26, no. 1 (2016), 29-67, algorithm computing a basis of the fixed subgroup of an automorphism of a free group of finite rank; Kourovka Archive, Problem 10.25 ("Yes, it does").

Stated but not proved: `MathlibExt.GroupTheory.FreeGroupAutomorphismFixedPointKourovka10Problem25Wanted.automorphismFixedPointDecidable_holds` is written with `theorem_wanted` in [WantedExt/GroupTheory/FreeGroupAutomorphismFixedPointKourovka10Problem25Wanted.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/FreeGroupAutomorphismFixedPointKourovka10Problem25Wanted.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/free-groups/automorphisms-of-free-groups/fixed-subgroups-of-free-group-automorphisms/index.html#automorphism-fixed-point-decidable-holds).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Fixed subgroups of free group automorphisms](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/free-groups/automorphisms-of-free-groups/fixed-subgroups-of-free-group-automorphisms/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/GroupTheory/free-groups/automorphisms-of-free-groups/fixed-subgroups-of-free-group-automorphisms)
