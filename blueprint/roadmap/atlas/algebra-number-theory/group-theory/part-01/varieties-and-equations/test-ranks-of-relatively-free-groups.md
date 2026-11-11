---
declaration: section
origin: cited
lean: MathlibExt.GroupTheory.TestRankNonabelianVarietyKourovka16Problem87Wanted.SatisfiesLaws, MathlibExt.GroupTheory.TestRankNonabelianVarietyKourovka16Problem87Wanted.verbalSubgroup, MathlibExt.GroupTheory.TestRankNonabelianVarietyKourovka16Problem87Wanted.RelativelyFreeGroup, MathlibExt.GroupTheory.TestRankNonabelianVarietyKourovka16Problem87Wanted.IsTestSet, MathlibExt.GroupTheory.TestRankNonabelianVarietyKourovka16Problem87Wanted.HasTestRank, MathlibExt.GroupTheory.TestRankNonabelianVarietyKourovka16Problem87Wanted.testRankVarietyAbelian, MathlibExt.GroupTheory.TestRankNonabelianVarietyKourovka16Problem87Wanted.testRankNonperiodicVarietyAllAbelian, MathlibExt.GroupTheory.TestRankNonabelianVarietyKourovka16Problem87Wanted.testRankVarietyAbelian_refuted
statement: formalized
---

# Test ranks of relatively free groups

9 results, 7 proved and 2 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/varieties-and-equations/test-ranks-of-relatively-free-groups/index.html).

## Groups satisfying a set of laws in countably many variables

Let $F_\mathbb{N}$ be the free
group on countably many generators and $W \subseteq F_\mathbb{N}$ a set of words, the laws. A group
$G$ satisfies the laws $W$ when $\varphi(w) = 1$ for every $w \in W$ and every homomorphism
$\varphi \colon F_\mathbb{N} \to G$, that is, every law takes the value $1$ under every
substitution of elements of $G$ for the variables. The variety defined by $W$ is the class of
these groups.

Formalized by `MathlibExt.GroupTheory.TestRankNonabelianVarietyKourovka16Problem87Wanted.SatisfiesLaws`, a definition declared in [WantedExt/GroupTheory/TestRankNonabelianVarietyKourovka16Problem87Wanted.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/TestRankNonabelianVarietyKourovka16Problem87Wanted.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/varieties-and-equations/test-ranks-of-relatively-free-groups/index.html#satisfies-laws).

## Verbal subgroup of a free group of finite rank

Let $W$ be a set of laws in the free group
$F_\mathbb{N}$ on countably many generators, and let $F_r$ be the free group on $r$ generators. The
verbal subgroup $V_W(F_r)$ of $F_r$ for $W$ is the normal closure in $F_r$ of all elements
$\varphi(w)$ with $w \in W$ and $\varphi \colon F_\mathbb{N} \to F_r$ a homomorphism.

Formalized by `MathlibExt.GroupTheory.TestRankNonabelianVarietyKourovka16Problem87Wanted.verbalSubgroup`, an abbreviation declared in [WantedExt/GroupTheory/TestRankNonabelianVarietyKourovka16Problem87Wanted.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/TestRankNonabelianVarietyKourovka16Problem87Wanted.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/varieties-and-equations/test-ranks-of-relatively-free-groups/index.html#verbal-subgroup).

## Relatively free group as a quotient of a free group

Let $W$ be a set of laws in the free
group $F_\mathbb{N}$ on countably many generators, and let $r \in \mathbb{N}$. The free
$r$-generator group $G_r$ of the variety defined by $W$ is the quotient $F_r / V_W(F_r)$ of the
free group $F_r$ on $r$ generators by its verbal subgroup $V_W(F_r)$ for $W$.

Formalized by `MathlibExt.GroupTheory.TestRankNonabelianVarietyKourovka16Problem87Wanted.RelativelyFreeGroup`, an abbreviation declared in [WantedExt/GroupTheory/TestRankNonabelianVarietyKourovka16Problem87Wanted.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/TestRankNonabelianVarietyKourovka16Problem87Wanted.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/varieties-and-equations/test-ranks-of-relatively-free-groups/index.html#relatively-free-group).

## Test set of a group

A subset $S$ of a group $G$ is a test set when every endomorphism of
$G$ that fixes every element of $S$ is bijective, that is, an automorphism of $G$.

Formalized by `MathlibExt.GroupTheory.TestRankNonabelianVarietyKourovka16Problem87Wanted.IsTestSet`, a definition declared in [WantedExt/GroupTheory/TestRankNonabelianVarietyKourovka16Problem87Wanted.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/TestRankNonabelianVarietyKourovka16Problem87Wanted.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/varieties-and-equations/test-ranks-of-relatively-free-groups/index.html#is-test-set).

## Test rank of a group

A group $G$ has test rank $r \in \mathbb{N}$ when $G$ has a test set
of cardinality $r$ and every test set of $G$ has cardinality at least $r$ (an infinite set counting
as having cardinality $\infty$), that is, when the minimum of the cardinalities of the test sets of
$G$ is $r$.

Formalized by `MathlibExt.GroupTheory.TestRankNonabelianVarietyKourovka16Problem87Wanted.HasTestRank`, a definition declared in [WantedExt/GroupTheory/TestRankNonabelianVarietyKourovka16Problem87Wanted.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/TestRankNonabelianVarietyKourovka16Problem87Wanted.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/varieties-and-equations/test-ranks-of-relatively-free-groups/index.html#has-test-rank).

## Timoshenko's test rank question, part (a)

The statement that for every set $W$ of laws in
the free group $F_\mathbb{N}$ on countably many generators, if for every $r \ge 1$ the free
$r$-generator group $G_r$ of the variety defined by $W$ has test rank $r$, then this variety is
abelian: every group satisfying the laws $W$ is abelian.

This is Kourovka Notebook Problem 16.87(a) (E. I. Timoshenko), which asks whether the statement
holds.

Formalized by `MathlibExt.GroupTheory.TestRankNonabelianVarietyKourovka16Problem87Wanted.testRankVarietyAbelian`, a definition declared in [WantedExt/GroupTheory/TestRankNonabelianVarietyKourovka16Problem87Wanted.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/TestRankNonabelianVarietyKourovka16Problem87Wanted.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/varieties-and-equations/test-ranks-of-relatively-free-groups/index.html#test-rank-variety-abelian).

## Timoshenko's test rank question, part (b)

The statement that for every set $W$ of laws in
the free group $F_\mathbb{N}$ on countably many generators, if for every $r \ge 1$ the free
$r$-generator group $G_r$ of the variety defined by $W$ has test rank $r$ and the variety is not
periodic (there is no $n > 0$ with $g^n = 1$ for every element $g$ of every group satisfying $W$),
then the variety is the variety of all abelian groups: a group satisfies the laws $W$ if and only
if it is abelian.

This is Kourovka Notebook Problem 16.87(b) (E. I. Timoshenko), which asks whether the statement
holds.

Formalized by `MathlibExt.GroupTheory.TestRankNonabelianVarietyKourovka16Problem87Wanted.testRankNonperiodicVarietyAllAbelian`, a definition declared in [WantedExt/GroupTheory/TestRankNonabelianVarietyKourovka16Problem87Wanted.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/TestRankNonabelianVarietyKourovka16Problem87Wanted.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/varieties-and-equations/test-ranks-of-relatively-free-groups/index.html#test-rank-nonperiodic-variety-all-abelia).

## Negative answer to Timoshenko's test rank question, part (a)

There is a set $W$ of laws
in the free group $F_\mathbb{N}$ on countably many generators such that for every $r \ge 1$ the
free $r$-generator group $G_r$ of the variety defined by $W$ has test rank $r$, but the variety is
not abelian: some group satisfying the laws $W$ is not abelian.

The witness is the variety defined by $[[x, y], z] = 1$ and $[x, y]^p = 1$ for a prime $p$, which
contains the non-abelian group $\mathrm{UT}_3(\mathbb{F}_p)$.

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Problem 16.87 (E. I. Timoshenko); resolution: M. Kinyon and J. Urban (with Codex gpt-6-astra), Results on problems from the Kourovka Notebook, preprint, version 4 (19 September 2026), Section 3.23 (Problem 16.87): the variety M_p defined by [[x, y], z] = 1 and [x, y]^p = 1 (p prime) is nonabelian (it contains UT_3(F_p)) and nonperiodic (it contains Z), and Proposition 3.9 shows that its free group of rank r has test rank r for every r ≥ 1; the Kourovka Notebook (21st issue) marks 16.87 solved (a), b) No, it is not true in both cases; AI solution confirmed by E. I. Timoshenko), https://kourovkanotebookorg.wordpress.com/wp-content/uploads/2026/09/kourovka-mathematics.pdf.

Stated but not proved: `MathlibExt.GroupTheory.TestRankNonabelianVarietyKourovka16Problem87Wanted.testRankVarietyAbelian_refuted` is written with `theorem_wanted` in [WantedExt/GroupTheory/TestRankNonabelianVarietyKourovka16Problem87Wanted.lean, line 96](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/TestRankNonabelianVarietyKourovka16Problem87Wanted.lean#L96). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/varieties-and-equations/test-ranks-of-relatively-free-groups/index.html#test-rank-variety-abelian-refuted).

## Non-periodic varieties with full test rank need not be abelian

Resolved false: the same variety (`[[x, y], z] = 1`, `[x, y]^p = 1`, `p` prime) is not periodic
since it contains `ℤ`, its free groups of every rank `r ≥ 1` have test rank `r` (Kinyon-Urban,
Proposition 3.9), and it is not the variety of all abelian groups since it contains the non-abelian
group `UT₃(𝔽_p)`. The Kourovka Notebook (21st issue) answers 16.87(b) "No" (AI solution confirmed by
E. I. Timoshenko). Source: E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group
Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Problem 16.87 (E. I.
Timoshenko); resolution: M. Kinyon and J. Urban (with Codex gpt-6-astra), Results on problems from
the Kourovka Notebook, preprint, version 4 (19 September 2026), Section 3.23 (Problem 16.87): the
variety M_p defined by [[x, y], z] = 1 and [x, y]^p = 1 (p prime) is nonabelian (it contains
UT_3(F_p)) and nonperiodic (it contains Z), and Proposition 3.9 shows that its free group of rank r
has test rank r for every r ≥ 1; the Kourovka Notebook (21st issue) marks 16.87 solved (a), b) No,
it is not true in both cases; AI solution confirmed by E. I. Timoshenko),
https://kourovkanotebookorg.wordpress.com/wp-content/uploads/2026/09/kourovka-mathematics.pdf.

Stated but not proved: `MathlibExt.GroupTheory.TestRankNonabelianVarietyKourovka16Problem87Wanted.testRankNonperiodicVarietyAllAbelian_refuted` is written with `theorem_wanted` in [WantedExt/GroupTheory/TestRankNonabelianVarietyKourovka16Problem87Wanted.lean, line 113](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/TestRankNonabelianVarietyKourovka16Problem87Wanted.lean#L113). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/varieties-and-equations/test-ranks-of-relatively-free-groups/index.html#test-rank-nonperiodic-variety-all-abelia-2).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Test ranks of relatively free groups](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/varieties-and-equations/test-ranks-of-relatively-free-groups/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/GroupTheory/varieties-and-equations/test-ranks-of-relatively-free-groups)
