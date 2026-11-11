---
declaration: section
origin: cited
lean: MathlibExt.GroupTheory.ReducedIncidenceAlgebraDomainKourovka13Problem29Wanted.incMul, MathlibExt.GroupTheory.ReducedIncidenceAlgebraDomainKourovka13Problem29Wanted.IsInA, MathlibExt.GroupTheory.ReducedIncidenceAlgebraDomainKourovka13Problem29Wanted.IsInvariant, MathlibExt.GroupTheory.ReducedIncidenceAlgebraDomainKourovka13Problem29Wanted.invariantIncidenceAlgebraIsDomain, MathlibExt.GroupTheory.ReducedIncidenceAlgebraDomainKourovka13Problem29Wanted.invariantIncidenceAlgebraIsDomain_holds
statement: formalized
---

# Orbit algebras of permutation groups

5 results, 4 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/permutation-groups/infinite-permutation-groups/orbit-algebras-of-permutation-groups/index.html).

## Product of the reduced incidence algebra

Let $\Omega$ be a set. For functions $f$ and $g$
from the finite subsets of $\Omega$ to $\mathbb{Q}$, their product $fg$ is the function on finite
subsets given by $(fg)(X) = \sum_{Y \subseteq X} f(Y)\, g(X \setminus Y)$.

If $f$ vanishes off the $n$-element subsets and $g$ vanishes off the $m$-element subsets, this is
the product of Kourovka Problem 13.29, and $fg$ vanishes off the $(n+m)$-element subsets.

Formalized by `MathlibExt.GroupTheory.ReducedIncidenceAlgebraDomainKourovka13Problem29Wanted.incMul`, a definition declared in [WantedExt/GroupTheory/ReducedIncidenceAlgebraDomainKourovka13Problem29Wanted.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/ReducedIncidenceAlgebraDomainKourovka13Problem29Wanted.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/permutation-groups/infinite-permutation-groups/orbit-algebras-of-permutation-groups/index.html#inc-mul).

## Elements of the reduced incidence algebra

Let $\Omega$ be a set. A function $f$ from the
finite subsets of $\Omega$ to $\mathbb{Q}$ lies in the algebra $A = \bigoplus_n V_n$, where $V_n$
consists of the functions vanishing off the $n$-element subsets, when there is a natural number
$N$ such that $f(X) = 0$ for every finite subset $X$ of $\Omega$ with more than $N$ elements.

Formalized by `MathlibExt.GroupTheory.ReducedIncidenceAlgebraDomainKourovka13Problem29Wanted.IsInA`, a definition declared in [WantedExt/GroupTheory/ReducedIncidenceAlgebraDomainKourovka13Problem29Wanted.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/ReducedIncidenceAlgebraDomainKourovka13Problem29Wanted.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/permutation-groups/infinite-permutation-groups/orbit-algebras-of-permutation-groups/index.html#is-in-a).

## Invariant functions on finite subsets

Let $G$ be a group of permutations of a set
$\Omega$. A function $f$ from the finite subsets of $\Omega$ to $\mathbb{Q}$ is $G$-invariant when
$f(\sigma(X)) = f(X)$ for every $\sigma \in G$ and every finite subset $X$ of $\Omega$, where
$\sigma(X)$ is the image of $X$ under $\sigma$.

Formalized by `MathlibExt.GroupTheory.ReducedIncidenceAlgebraDomainKourovka13Problem29Wanted.IsInvariant`, a definition declared in [WantedExt/GroupTheory/ReducedIncidenceAlgebraDomainKourovka13Problem29Wanted.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/ReducedIncidenceAlgebraDomainKourovka13Problem29Wanted.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/permutation-groups/infinite-permutation-groups/orbit-algebras-of-permutation-groups/index.html#is-invariant).

## Cameron's conjecture on invariant incidence algebras (Kourovka 13.29)

The statement that
for every infinite set $\Omega$ and every group $G$ of permutations of $\Omega$ all of whose orbits
are infinite, the following holds: if $f$ and $g$ are nonzero functions from the finite subsets of
$\Omega$ to $\mathbb{Q}$ that are $G$-invariant ($f(\sigma(X)) = f(X)$ for all $\sigma \in G$ and
all finite $X$, and likewise for $g$) and that each vanish on all subsets of size larger than some
bound, then their product $fg$ in the reduced incidence algebra, given by
$(fg)(X) = \sum_{Y \subseteq X} f(Y)\, g(X \setminus Y)$, is not identically zero. In other words,
the algebra $A^G$ of $G$-invariant elements of the reduced incidence algebra $A$ has no zero
divisors.

Formalized by `MathlibExt.GroupTheory.ReducedIncidenceAlgebraDomainKourovka13Problem29Wanted.invariantIncidenceAlgebraIsDomain`, a definition declared in [WantedExt/GroupTheory/ReducedIncidenceAlgebraDomainKourovka13Problem29Wanted.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/ReducedIncidenceAlgebraDomainKourovka13Problem29Wanted.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/permutation-groups/infinite-permutation-groups/orbit-algebras-of-permutation-groups/index.html#invariant-incidence-algebra-is-domain).

## Cameron's conjecture on invariant incidence algebras holds (Pouzet)

Let $\Omega$ be an
infinite set and let $G$ be a group of permutations of $\Omega$ all of whose orbits are infinite.
Let $f$ and $g$ be nonzero functions from the finite subsets of $\Omega$ to $\mathbb{Q}$ that are
$G$-invariant ($f(\sigma(X)) = f(X)$ for all $\sigma \in G$ and all finite $X$, and likewise for
$g$) and that each vanish on all subsets of size larger than some bound. Then their product in the
reduced incidence algebra, $(fg)(X) = \sum_{Y \subseteq X} f(Y)\, g(X \setminus Y)$, is not
identically zero. In other words, the algebra $A^G$ of $G$-invariant elements of the reduced
incidence algebra $A$ has no zero divisors.

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Archive of Solved Problems, Problem 13.29 (P. J. Cameron); resolution: M. Pouzet, Theor. Inform. Appl. 42 (2008), no. 1, 83-103, Kourovka Archive, Problem 13.29: the conjecture is proved.

Stated but not proved: `MathlibExt.GroupTheory.ReducedIncidenceAlgebraDomainKourovka13Problem29Wanted.invariantIncidenceAlgebraIsDomain_holds` is written with `theorem_wanted` in [WantedExt/GroupTheory/ReducedIncidenceAlgebraDomainKourovka13Problem29Wanted.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/ReducedIncidenceAlgebraDomainKourovka13Problem29Wanted.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/permutation-groups/infinite-permutation-groups/orbit-algebras-of-permutation-groups/index.html#invariant-incidence-algebra-is-domain-ho).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Orbit algebras of permutation groups](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/permutation-groups/infinite-permutation-groups/orbit-algebras-of-permutation-groups/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/GroupTheory/permutation-groups/infinite-permutation-groups/orbit-algebras-of-permutation-groups)
