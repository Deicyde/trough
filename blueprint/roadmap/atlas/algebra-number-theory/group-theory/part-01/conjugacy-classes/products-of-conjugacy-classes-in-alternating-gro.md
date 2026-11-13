---
declaration: section
origin: cited
lean: MathlibExt.GroupTheory.ProductThreeConjugacyClassesAlternatingKourovka20Problem23Wanted.productOfThreeLargeClassesIsAlternatingGroup, MathlibExt.GroupTheory.ProductThreeConjugacyClassesAlternatingKourovka20Problem23Wanted.productOfThreeLargeClassesIsAlternatingGroup_holds
statement: formalized
---

# Products of conjugacy classes in alternating groups

2 results, 1 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/conjugacy-classes/products-of-conjugacy-classes-in-alternating-gro/index.html).

## Products of three large conjugacy classes in alternating groups (Kourovka 20.23)

The
statement that there are a real number $\delta$ with $0 < \delta < 1$ and a natural number $N$
such that for every $n \ge N$ and all conjugacy classes $A$, $B$, $C$ of the alternating group
$\mathrm{Alt}(n)$, each of size at least $|\mathrm{Alt}(n)|^{\delta}$, the product set $ABC$ is
all of $\mathrm{Alt}(n)$.

Formalized by `MathlibExt.GroupTheory.ProductThreeConjugacyClassesAlternatingKourovka20Problem23Wanted.productOfThreeLargeClassesIsAlternatingGroup`, a definition declared in [WantedExt/GroupTheory/ProductThreeConjugacyClassesAlternatingKourovka20Problem23Wanted.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/ProductThreeConjugacyClassesAlternatingKourovka20Problem23Wanted.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/conjugacy-classes/products-of-conjugacy-classes-in-alternating-gro/index.html#product-of-three-large-classes-is-altern).

## Three large conjugacy classes multiply to the whole alternating group

There are a real number
$\delta$ with $0 < \delta < 1$ and a natural number $N$ such that for every $n \ge N$ and all
conjugacy classes $A$, $B$, $C$ of the alternating group $\mathrm{Alt}(n)$, each of size at least
$|\mathrm{Alt}(n)|^{\delta}$, the product set $ABC$ is all of $\mathrm{Alt}(n)$. This is the
positive answer to Kourovka Problem 20.23.

Dona (2025, Theorem 1.2) proves this with the size bound written as
$|\mathrm{Alt}(n)|^{1-\varepsilon}$ for a small $\varepsilon > 0$.

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Problem 20.23 (M. Garonzi, A. Maróti); resolution: D. Dona, Products of three conjugacy classes in the alternating group, preprint, arXiv:2505.06012 (2025), Theorem 1.2: there are δ > 0 and n₀ such that for n ≥ n₀ any three conjugacy classes of G = Alt(n) of size at least |G|^(1-δ) satisfy C₁C₂C₃ = G (a positive answer to Problem 20.23 with exponent 1 - δ); the Kourovka Notebook (21st issue) marks 20.23 solved, https://arxiv.org/abs/2505.06012.

Stated but not proved: `MathlibExt.GroupTheory.ProductThreeConjugacyClassesAlternatingKourovka20Problem23Wanted.productOfThreeLargeClassesIsAlternatingGroup_holds` is written with `theorem_wanted` in [WantedExt/GroupTheory/ProductThreeConjugacyClassesAlternatingKourovka20Problem23Wanted.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/ProductThreeConjugacyClassesAlternatingKourovka20Problem23Wanted.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/conjugacy-classes/products-of-conjugacy-classes-in-alternating-gro/index.html#product-of-three-large-classes-is-altern-2).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Products of conjugacy classes in alternating groups](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/conjugacy-classes/products-of-conjugacy-classes-in-alternating-gro/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/GroupTheory/conjugacy-classes/products-of-conjugacy-classes-in-alternating-gro)
