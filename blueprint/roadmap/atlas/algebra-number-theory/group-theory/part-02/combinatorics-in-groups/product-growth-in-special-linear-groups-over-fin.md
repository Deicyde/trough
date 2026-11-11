---
declaration: section
origin: cited
lean: MathlibExt.Combinatorics.SL2TwoStepProductGrowthWanted.AIMCombinatorics0241_prodSet, MathlibExt.Combinatorics.SL2TwoStepProductGrowthWanted.conjecture, MathlibExt.Combinatorics.SL2TwoStepProductGrowthWanted.conjecture_holds
statement: formalized
---

# Product growth in special linear groups over finite fields

3 results, 2 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/combinatorics-in-groups/product-growth-in-special-linear-groups-over-fin/index.html).

## Product set of a finite set

For a finite subset $A$ of a type with a multiplication, the
product set $A \cdot A$ is the finite set $\{ab : a, b \in A\}$ of all products of two elements
of $A$.

## Sources

- AIM-COMBINATORICS-0241, Problem 3.4, aim-combinatorics-notes.json notes[240].

Formalized by `MathlibExt.Combinatorics.SL2TwoStepProductGrowthWanted.AIMCombinatorics0241_prodSet`, a definition declared in [WantedExt/Combinatorics/SL2TwoStepProductGrowthWanted.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/SL2TwoStepProductGrowthWanted.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/combinatorics-in-groups/product-growth-in-special-linear-groups-over-fin/index.html#aimcombinatorics0241-prod-set).

## Two-step product growth in $\mathrm{SL}_2(\mathbb{F}_p)$ (AIM Problem 3.4)

The statement
that for every real $C \ge 1$ there are a real $\delta > 0$ and a natural number $P_0$ such that
for every prime $p \ge P_0$ and every finite subset $A$ of $\mathrm{SL}_2(\mathbb{F}_p)$, where
$\mathbb{F}_p = \mathbb{Z}/p\mathbb{Z}$, with $C^{-1} p^{5/2} \le |A| \le C p^{5/2}$, the product
set $A \cdot A = \{ab : a, b \in A\}$ satisfies $|A \cdot A| > p^{5/2 + \delta}$.

This is a large-$p$ reading of the question of Green, after Venkatesh: if
$A \subseteq \mathrm{SL}_2(\mathbb{F}_p)$ satisfies $|A| \sim p^{5/2}$, does it follow that
$|A \cdot A| > p^{5/2 + \delta}$?

## Sources

- AIM-COMBINATORICS-0241, Problem 3.4, aim-combinatorics-notes.json notes[240], https://aimath.org/WWN/additivecomb/additivecomb.pdf.

Formalized by `MathlibExt.Combinatorics.SL2TwoStepProductGrowthWanted.conjecture`, a definition declared in [WantedExt/Combinatorics/SL2TwoStepProductGrowthWanted.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/SL2TwoStepProductGrowthWanted.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/combinatorics-in-groups/product-growth-in-special-linear-groups-over-fin/index.html#conjecture).

## Sets of size about $p^{5/2}$ in $\mathrm{SL}_2(\mathbb{F}_p)$ grow under multiplication

For
every real $C \ge 1$ there are a real $\delta > 0$ and a natural number $P_0$ such that for every
prime $p \ge P_0$ and every finite subset $A$ of $\mathrm{SL}_2(\mathbb{F}_p)$, where
$\mathbb{F}_p = \mathbb{Z}/p\mathbb{Z}$, with $C^{-1} p^{5/2} \le |A| \le C p^{5/2}$, the product
set $A \cdot A = \{ab : a, b \in A\}$ satisfies $|A \cdot A| > p^{5/2 + \delta}$.

Every nontrivial representation of $\mathrm{SL}_2(\mathbb{F}_p)$ has dimension at least
$(p-1)/2$, and the product-mixing bound of Gowers and Babai–Nikolov–Pyber then gives
$|A \cdot A| \gg p^3$ for such $A$, so every $\delta < 1/2$ works. This answers AIM
additive-combinatorics Problem 3.4 (Green, after Venkatesh).

## Sources

- N. Nikolov and L. Pyber, Product decompositions of quasirandom groups and a Jordan type theorem, arXiv:math/0703343, https://arxiv.org/abs/math/0703343.

Stated but not proved: `MathlibExt.Combinatorics.SL2TwoStepProductGrowthWanted.conjecture_holds` is written with `theorem_wanted` in [WantedExt/Combinatorics/SL2TwoStepProductGrowthWanted.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/SL2TwoStepProductGrowthWanted.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/combinatorics-in-groups/product-growth-in-special-linear-groups-over-fin/index.html#conjecture-holds).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Product growth in special linear groups over finite fields](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/combinatorics-in-groups/product-growth-in-special-linear-groups-over-fin/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/GroupTheory/combinatorics-in-groups/product-growth-in-special-linear-groups-over-fin)
