---
declaration: section
origin: cited
lean: Finset.SubfamilyUnionFree, MathlibExt.Combinatorics.UnionFreeFamiliesErdosProblem447Wanted.IsUnionFree, MathlibExt.Combinatorics.UnionFreeFamiliesErdosProblem447Wanted.maxUnionFreeSize, MathlibExt.Combinatorics.UnionFreeFamiliesErdosProblem447Wanted.maxUnionFreeSizeLittleO, MathlibExt.Combinatorics.UnionFreeFamiliesErdosProblem447Wanted.maxUnionFreeSizeCentralBinomial, MathlibExt.Combinatorics.UnionFreeFamiliesErdosProblem447Wanted.maxUnionFreeSizeLittleO_holds, MathlibExt.Combinatorics.UnionFreeFamiliesErdosProblem447Wanted.maxUnionFreeSizeCentralBinomial_holds
statement: formalized
---

# Union-free families

7 results, 5 proved and 2 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/extremal-set-theory/intersecting-families/union-free-families/index.html).

## Families in which no member is a union of other members

A family $F$ of finite sets
is union-free over its subfamilies if no member $A \in F$ is the union of a nonempty
subfamily of $F$ that does not contain $A$.

Formalized by `Finset.SubfamilyUnionFree`, a definition declared in [MathlibExt/Data/Finset/SubfamilyUnionFree.lean, line 27](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Data/Finset/SubfamilyUnionFree.lean#L27). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/extremal-set-theory/intersecting-families/union-free-families/index.html#subfamily-union-free).

## Union-free family

A family $F$ of subsets of $\{0, \dots, n-1\}$ is union-free if there
are no pairwise distinct $A, B, C \in F$ with $A \cup B = C$.

Formalized by `MathlibExt.Combinatorics.UnionFreeFamiliesErdosProblem447Wanted.IsUnionFree`, a definition declared in [WantedExt/Combinatorics/UnionFreeFamiliesErdosProblem447Wanted.lean, line 38](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/UnionFreeFamiliesErdosProblem447Wanted.lean#L38). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/extremal-set-theory/intersecting-families/union-free-families/index.html#is-union-free).

## Maximum size of a union-free family

For a natural number $n$, the largest size $|F|$ of a
union-free family $F$ of subsets of $\{0, \dots, n-1\}$.

Formalized by `MathlibExt.Combinatorics.UnionFreeFamiliesErdosProblem447Wanted.maxUnionFreeSize`, a definition declared in [WantedExt/Combinatorics/UnionFreeFamiliesErdosProblem447Wanted.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/UnionFreeFamiliesErdosProblem447Wanted.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/extremal-set-theory/intersecting-families/union-free-families/index.html#max-union-free-size).

## Erdős Problem 447, first question

The assertion that the maximum size of a union-free
family of subsets of $\{0, \dots, n-1\}$ is $o(2^n)$ as $n \to \infty$.

Formalized by `MathlibExt.Combinatorics.UnionFreeFamiliesErdosProblem447Wanted.maxUnionFreeSizeLittleO`, a definition declared in [WantedExt/Combinatorics/UnionFreeFamiliesErdosProblem447Wanted.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/UnionFreeFamiliesErdosProblem447Wanted.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/extremal-set-theory/intersecting-families/union-free-families/index.html#max-union-free-size-little-o).

## Erdős Problem 447, second question

The assertion that, for every real $\varepsilon > 0$
and all sufficiently large $n$, the maximum size of a union-free family of subsets of
$\{0, \dots, n-1\}$ is at most $(1 + \varepsilon)\binom{n}{\lfloor n/2 \rfloor}$; that is, it is
at most $(1 + o(1))\binom{n}{\lfloor n/2 \rfloor}$.

Formalized by `MathlibExt.Combinatorics.UnionFreeFamiliesErdosProblem447Wanted.maxUnionFreeSizeCentralBinomial`, a definition declared in [WantedExt/Combinatorics/UnionFreeFamiliesErdosProblem447Wanted.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/UnionFreeFamiliesErdosProblem447Wanted.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/extremal-set-theory/intersecting-families/union-free-families/index.html#max-union-free-size-central-binomial).

## Union-free families have vanishing density (Erdős Problem 447)

The maximum size of a
union-free family of subsets of $\{0, \dots, n-1\}$ is $o(2^n)$ as $n \to \infty$.

This follows from Kleitman's bound $(1 + o(1))\binom{n}{\lfloor n/2 \rfloor}$; Erdős reported an
earlier unpublished proof by Sárközy and Szemerédi.

## Sources

- T. F. Bloom, Erdős Problems, Problem #447, https://www.erdosproblems.com/447 (status PROVED (LEAN)); resolution: D. Kleitman, Collections of subsets containing no two sets and their union, Proceedings of the LA Meeting AMS (1971), 153-155, |F| < (1 + o(1)) C(n, ⌊n/2⌋) (erdosproblems.com/447).

Stated but not proved: `MathlibExt.Combinatorics.UnionFreeFamiliesErdosProblem447Wanted.maxUnionFreeSizeLittleO_holds` is written with `theorem_wanted` in [WantedExt/Combinatorics/UnionFreeFamiliesErdosProblem447Wanted.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/UnionFreeFamiliesErdosProblem447Wanted.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/extremal-set-theory/intersecting-families/union-free-families/index.html#max-union-free-size-little-o-holds).

## Kleitman's bound for union-free families (Erdős Problem 447)

For every real
$\varepsilon > 0$ and all sufficiently large $n$, the maximum size of a union-free family of
subsets of $\{0, \dots, n-1\}$ is at most $(1 + \varepsilon)\binom{n}{\lfloor n/2 \rfloor}$; that
is, it is at most $(1 + o(1))\binom{n}{\lfloor n/2 \rfloor}$.

## Sources

- T. F. Bloom, Erdős Problems, Problem #447, https://www.erdosproblems.com/447 (status PROVED (LEAN)); resolution: D. Kleitman, Collections of subsets containing no two sets and their union, Proceedings of the LA Meeting AMS (1971), 153-155, |F| < (1 + o(1)) C(n, ⌊n/2⌋) (erdosproblems.com/447).

Stated but not proved: `MathlibExt.Combinatorics.UnionFreeFamiliesErdosProblem447Wanted.maxUnionFreeSizeCentralBinomial_holds` is written with `theorem_wanted` in [WantedExt/Combinatorics/UnionFreeFamiliesErdosProblem447Wanted.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/UnionFreeFamiliesErdosProblem447Wanted.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/extremal-set-theory/intersecting-families/union-free-families/index.html#max-union-free-size-central-binomial-hol).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Union-free families](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/extremal-set-theory/intersecting-families/union-free-families/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Combinatorics/extremal-set-theory/intersecting-families/union-free-families)
