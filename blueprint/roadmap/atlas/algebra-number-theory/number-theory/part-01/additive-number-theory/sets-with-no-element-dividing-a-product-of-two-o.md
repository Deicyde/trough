---
declaration: section
origin: cited
lean: MathlibExt.NumberTheory.ErdosDivisibilityFamilyGrowthWanted.Good, MathlibExt.NumberTheory.ErdosDivisibilityFamilyGrowthWanted.F, MathlibExt.NumberTheory.ErdosDivisibilityFamilyGrowthWanted.conjecture, MathlibExt.NumberTheory.ErdosDivisibilityFamilyGrowthWanted.conjecture_holds
statement: formalized
---

# Sets with no element dividing a product of two others

4 results, 3 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/additive-number-theory/sets-with-no-element-dividing-a-product-of-two-o/index.html).

## Sets in which no element divides the product of two others

A finite set $A$ of natural
numbers is good when every element of $A$ is positive and no $a \in A$ divides $bc$ for any
$b, c \in A$ with $a \ne b$ and $a \ne c$; here $b = c$ is allowed.

Formalized by `MathlibExt.NumberTheory.ErdosDivisibilityFamilyGrowthWanted.Good`, a definition declared in [WantedExt/NumberTheory/ErdosDivisibilityFamilyGrowthWanted.lean, line 33](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ErdosDivisibilityFamilyGrowthWanted.lean#L33). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/additive-number-theory/sets-with-no-element-dividing-a-product-of-two-o/index.html#good).

## Maximum size of a good subset

For a natural number $n$, $F(n)$ is the largest size of a
good subset of $\{1, \dots, n\}$, defined as the supremum of the sizes of the good sets
$A \subseteq \{1, \dots, n\}$.

Formalized by `MathlibExt.NumberTheory.ErdosDivisibilityFamilyGrowthWanted.F`, a definition declared in [WantedExt/NumberTheory/ErdosDivisibilityFamilyGrowthWanted.lean, line 38](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ErdosDivisibilityFamilyGrowthWanted.lean#L38). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/additive-number-theory/sets-with-no-element-dividing-a-product-of-two-o/index.html#f).

## Statement of Erdős Problem 793

For a natural number $n$, let $F(n)$ be the largest size
of a set $A \subseteq \{1, \dots, n\}$ with $a \nmid bc$ for all $a, b, c \in A$ such that
$a \ne b$ and $a \ne c$, and let $\pi(n)$ be the number of primes at most $n$. This is the
proposition that there is a real constant $C > 0$ such that
$(F(n) - \pi(n)) / (n^{2/3} / (\log n)^2) \to C$ as $n \to \infty$.
Equivalently, $F(n) = \pi(n) + (C + o(1))\, n^{2/3} / (\log n)^2$.

Formalized by `MathlibExt.NumberTheory.ErdosDivisibilityFamilyGrowthWanted.conjecture`, a definition declared in [WantedExt/NumberTheory/ErdosDivisibilityFamilyGrowthWanted.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ErdosDivisibilityFamilyGrowthWanted.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/additive-number-theory/sets-with-no-element-dividing-a-product-of-two-o/index.html#conjecture).

## Erdős Problem 793 has a positive answer

Let $F(n)$ be the largest size of a set
$A \subseteq \{1, \dots, n\}$ such that $a \nmid bc$ whenever $a, b, c \in A$ with $a \ne b$ and
$a \ne c$ ($b = c$ is allowed), and let $\pi(n)$ be the number of primes at most $n$. Then there
is a real constant $C > 0$ such that $(F(n) - \pi(n)) / (n^{2/3} / (\log n)^2) \to C$ as
$n \to \infty$.

Chojecki (2026, Theorem 1.1) proves this with $C = 27/2$.

## Sources

- P. Chojecki, The Second Term for Strongly 2-Primitive Sets, arXiv preprint (2026), arXiv:2607.15306, https://arxiv.org/abs/2607.15306.

Stated but not proved: `MathlibExt.NumberTheory.ErdosDivisibilityFamilyGrowthWanted.conjecture_holds` is written with `theorem_wanted` in [WantedExt/NumberTheory/ErdosDivisibilityFamilyGrowthWanted.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ErdosDivisibilityFamilyGrowthWanted.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/additive-number-theory/sets-with-no-element-dividing-a-product-of-two-o/index.html#conjecture-holds).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Sets with no element dividing a product of two others](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/additive-number-theory/sets-with-no-element-dividing-a-product-of-two-o/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/additive-number-theory/sets-with-no-element-dividing-a-product-of-two-o)
