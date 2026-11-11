---
declaration: section
origin: cited
lean: MathlibExt.Combinatorics.ErdosLovaszCoverFamilyErdosProblem21Wanted.IsErdosLovaszFamily, MathlibExt.Combinatorics.ErdosLovaszCoverFamilyErdosProblem21Wanted.intersectingFamilyFullCoverLinearSize, MathlibExt.Combinatorics.ErdosLovaszCoverFamilyErdosProblem21Wanted.intersectingFamilyFullCoverLinearSize_holds
statement: formalized
---

# Intersecting families with large cover number

3 results, 2 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/extremal-set-theory/hypergraph-colouring-matching/intersecting-families-with-large-cover-number/index.html).

## Erdős–Lovász family

For a natural number $n$, a finite family $\mathcal{F}$ of finite
sets of natural numbers is an Erdős–Lovász family of order $n$ when every member of
$\mathcal{F}$ has exactly $n$ elements, any two members of $\mathcal{F}$ (not necessarily
distinct) have a common element, and every set of at most $n - 1$ natural numbers is disjoint
from some member of $\mathcal{F}$, where $n - 1$ is read as $0$ when $n = 0$.

Formalized by `MathlibExt.Combinatorics.ErdosLovaszCoverFamilyErdosProblem21Wanted.IsErdosLovaszFamily`, a definition declared in [WantedExt/Combinatorics/ErdosLovaszCoverFamilyErdosProblem21Wanted.lean, line 38](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/ErdosLovaszCoverFamilyErdosProblem21Wanted.lean#L38). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/extremal-set-theory/hypergraph-colouring-matching/intersecting-families-with-large-cover-number/index.html#is-erdos-lovasz-family).

## Erdős Problem 21 (Erdős–Lovász)

The statement that there is a natural number $C$ such
that for every $n \ge 1$ there is a finite family $\mathcal{F}$ of finite sets of natural numbers
in which every member has exactly $n$ elements, any two members have a common element, every
set of at most $n - 1$ natural numbers is disjoint from some member, and
$|\mathcal{F}| \le C n$. This expresses $f(n) \ll n$, where $f(n)$ is the least size of such a
family.

Formalized by `MathlibExt.Combinatorics.ErdosLovaszCoverFamilyErdosProblem21Wanted.intersectingFamilyFullCoverLinearSize`, a definition declared in [WantedExt/Combinatorics/ErdosLovaszCoverFamilyErdosProblem21Wanted.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/ErdosLovaszCoverFamilyErdosProblem21Wanted.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/extremal-set-theory/hypergraph-colouring-matching/intersecting-families-with-large-cover-number/index.html#intersecting-family-full-cover-linear-si).

## Kahn's theorem on the Erdős–Lovász problem

There is a natural number $C$ such that for
every $n \ge 1$ there is a finite family $\mathcal{F}$ of finite sets of natural numbers with
the following properties: every member of $\mathcal{F}$ has exactly $n$ elements, any two
members of $\mathcal{F}$ have a common element, every set of at most $n - 1$ natural numbers is
disjoint from some member of $\mathcal{F}$, and $|\mathcal{F}| \le C n$.

Kahn proved this, improving his earlier bound $O(n \log n)$ obtained from random lines in
projective planes; it answers Erdős Problem 21 in the affirmative.

## Sources

- T. F. Bloom, Erdős Problems, Problem #21, https://www.erdosproblems.com/21 (status PROVED (LEAN)); resolution: J. Kahn, On a problem of Erdős and Lovász. II. n(r) = O(r), J. Amer. Math. Soc. 7 (1994), 125-143, main theorem n(r) = O(r); erdosproblems.com/21: solved by Kahn [Ka94], https://doi.org/10.2307/2152722.

Stated but not proved: `MathlibExt.Combinatorics.ErdosLovaszCoverFamilyErdosProblem21Wanted.intersectingFamilyFullCoverLinearSize_holds` is written with `theorem_wanted` in [WantedExt/Combinatorics/ErdosLovaszCoverFamilyErdosProblem21Wanted.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/ErdosLovaszCoverFamilyErdosProblem21Wanted.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/extremal-set-theory/hypergraph-colouring-matching/intersecting-families-with-large-cover-number/index.html#intersecting-family-full-cover-linear-si-2).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Intersecting families with large cover number](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/extremal-set-theory/hypergraph-colouring-matching/intersecting-families-with-large-cover-number/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/extremal-set-theory/hypergraph-colouring-matching/intersecting-families-with-large-cover-number)
