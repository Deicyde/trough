---
declaration: section
origin: cited
lean: MathlibExt.Combinatorics.NoSingletonIntersectionErdosProblem702Wanted.noSingletonIntersectionBound, MathlibExt.Combinatorics.NoSingletonIntersectionErdosProblem702Wanted.noSingletonIntersectionBound_holds
statement: formalized
---

# Families with no singleton intersection

2 results, 1 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/extremal-set-theory/intersecting-families/families-with-no-singleton-intersection/index.html).

## Erdős Problem 702 on singleton intersections

For every $k \ge 4$ and every sufficiently
large $n$ (depending on $k$), every family of more than $\binom{n-2}{k-2}$ subsets of
$\{1, \dots, n\}$, each with exactly $k$ elements, contains two sets $A$ and $B$ with
$|A \cap B| = 1$.

This is Frankl's form of the problem of Erdős and Sós; without the hypothesis that $n$ is large
the statement fails, for instance for $k = 4$ and $n = 5$.

Formalized by `MathlibExt.Combinatorics.NoSingletonIntersectionErdosProblem702Wanted.noSingletonIntersectionBound`, a definition declared in [WantedExt/Combinatorics/NoSingletonIntersectionErdosProblem702Wanted.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/NoSingletonIntersectionErdosProblem702Wanted.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/extremal-set-theory/intersecting-families/families-with-no-singleton-intersection/index.html#no-singleton-intersection-bound).

## Frankl's theorem on families with no singleton intersection

For every $k \ge 4$ and every
sufficiently large $n$ (depending on $k$), every family of more than $\binom{n-2}{k-2}$ subsets of
$\{1, \dots, n\}$, each with exactly $k$ elements, contains two sets $A$ and $B$ with
$|A \cap B| = 1$.

This resolves Erdős Problem 702 of Erdős and Sós; Katona had the case $k = 4$. The hypothesis that
$n$ is large is needed ($k = 4$, $n = 5$).

## Sources

- T. F. Bloom, Erdős Problems, Problem #702, https://www.erdosproblems.com/702 (status PROVED); resolution: P. Frankl, On families of finite sets no two of which intersect in a singleton, Bull. Austral. Math. Soc. 17 (1977), 125-134, P. Keevash, D. Mubayi and R. M. Wilson, Set systems with no singleton intersection, abstract: 'Frankl showed that |F| ≤ C(n-2, k-2) for k ≥ 4 and n sufficiently large, confirming a conjecture of Erdős and Sós'; erdosproblems.com/702: Frankl proved this for all k ≥ 4, https://www.math.cmu.edu/users/mubayi/papers/no-singleton.pdf.

Stated but not proved: `MathlibExt.Combinatorics.NoSingletonIntersectionErdosProblem702Wanted.noSingletonIntersectionBound_holds` is written with `theorem_wanted` in [WantedExt/Combinatorics/NoSingletonIntersectionErdosProblem702Wanted.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/NoSingletonIntersectionErdosProblem702Wanted.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/extremal-set-theory/intersecting-families/families-with-no-singleton-intersection/index.html#no-singleton-intersection-bound-holds).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Families with no singleton intersection](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/extremal-set-theory/intersecting-families/families-with-no-singleton-intersection/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Combinatorics/extremal-set-theory/intersecting-families/families-with-no-singleton-intersection)
