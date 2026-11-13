---
declaration: section
origin: cited
lean: MathlibExt.GroupTheory.AlmostPalindromicWidthKourovka19Problem8Wanted.IsAlmostPalindrome, MathlibExt.GroupTheory.AlmostPalindromicWidthKourovka19Problem8Wanted.almostPalindromicWidthFinite, MathlibExt.GroupTheory.AlmostPalindromicWidthKourovka19Problem8Wanted.almostPalindromicWidthFinite_refuted
statement: formalized
---

# Palindromic width of free groups

3 results, 2 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/free-groups/subgroups-of-free-groups/palindromic-width-of-free-groups/index.html).

## Almost palindromes

For a natural number $m$, a word $w$ in the letters $x^{\pm 1}$ and
$y^{\pm 1}$ is an almost $m$-palindrome if there is a palindrome $p$ in the same letters with the
same length as $w$ such that $w$ and $p$ differ in at most $m$ positions. The word $w$ need not be
reduced.

Formalized by `MathlibExt.GroupTheory.AlmostPalindromicWidthKourovka19Problem8Wanted.IsAlmostPalindrome`, a definition declared in [WantedExt/GroupTheory/AlmostPalindromicWidthKourovka19Problem8Wanted.lean, line 41](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/AlmostPalindromicWidthKourovka19Problem8Wanted.lean#L41). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/free-groups/subgroups-of-free-groups/palindromic-width-of-free-groups/index.html#is-almost-palindrome).

## Finite almost-palindromic width of $F_2$ (Kourovka 19.8)

The proposition that there are
positive integers $m$ and $c$ such that every element of the free group $F_2$ on generators $x, y$
is a product of at most $c$ elements, each represented by an almost $m$-palindrome, that is, by a
word in $x^{\pm 1}, y^{\pm 1}$ (not necessarily reduced) that differs from a palindrome of the
same length in at most $m$ positions.

This is the question posed by V. G. Bardakov as Kourovka Problem 19.8.

Formalized by `MathlibExt.GroupTheory.AlmostPalindromicWidthKourovka19Problem8Wanted.almostPalindromicWidthFinite`, a definition declared in [WantedExt/GroupTheory/AlmostPalindromicWidthKourovka19Problem8Wanted.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/AlmostPalindromicWidthKourovka19Problem8Wanted.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/free-groups/subgroups-of-free-groups/palindromic-width-of-free-groups/index.html#almost-palindromic-width-finite).

## The almost-palindromic width of $F_2$ is infinite (Kourovka 19.8)

There are no positive
integers $m$ and $c$ such that every element of the free group $F_2$ on generators $x, y$ is a
product of at most $c$ elements, each represented by an almost $m$-palindrome, that is, by a word
in $x^{\pm 1}, y^{\pm 1}$ (not necessarily reduced) that differs from a palindrome of the same
length in at most $m$ positions. So the question of Kourovka Problem 19.8 has a negative answer.

Staiger proved more: for every $m \ge 0$, the $m$-almost-palindromic width of every non-abelian
free group is infinite.

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Problem 19.8 (V. G. Bardakov); resolution: M. Staiger, On the almost-palindromic width of free groups, J. Algebra 659 (2024), 475-481 (arXiv:2306.15752), Section 1: m-almost-palindromes are words of the free monoid on the letters x^{±1}, y^{±1} (not necessarily reduced) within Hamming distance m of a palindrome, and the width is taken for the group elements they represent; Theorem 1: for a non-abelian free group F and every m ≥ 0 the m-almost-palindromic width of F is infinite; the Kourovka Notebook (21st issue) marks 19.8 solved: No, there are no such integers, https://arxiv.org/abs/2306.15752.

Stated but not proved: `MathlibExt.GroupTheory.AlmostPalindromicWidthKourovka19Problem8Wanted.almostPalindromicWidthFinite_refuted` is written with `theorem_wanted` in [WantedExt/GroupTheory/AlmostPalindromicWidthKourovka19Problem8Wanted.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/AlmostPalindromicWidthKourovka19Problem8Wanted.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/free-groups/subgroups-of-free-groups/palindromic-width-of-free-groups/index.html#almost-palindromic-width-finite-refuted).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Palindromic width of free groups](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/free-groups/subgroups-of-free-groups/palindromic-width-of-free-groups/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/GroupTheory/free-groups/subgroups-of-free-groups/palindromic-width-of-free-groups)
