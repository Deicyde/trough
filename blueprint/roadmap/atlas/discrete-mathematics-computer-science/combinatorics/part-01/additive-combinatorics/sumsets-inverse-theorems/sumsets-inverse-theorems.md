---
declaration: section
origin: cited
lean: MathlibExt.Combinatorics.Additive.CauchyDavenportChowlaWanted.cauchy_davenport_chowla
statement: formalized
proof: formalized
---

# Sumsets and inverse theorems: its own results

1 result, proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/index.html).

Size and structure of A+B, hA and restricted or signed sumsets: Cauchy–Davenport and Vosper, Freiman-type and polynomial Freiman–Ruzsa theorems, small doubling, sums of dilates, h-fold sumsets with distinct terms, rectification, sets determined by k-sums, max-min (lunar) decompositions, and sum-product and product-set growth.

## Cauchy–Davenport–Chowla theorem

Let $q$ be a positive integer and let $A$ and $B$ be
nonempty subsets of $\mathbb{Z}/q\mathbb{Z}$ such that $0 \in B$ and every nonzero element of $B$
is a unit of $\mathbb{Z}/q\mathbb{Z}$. Then $|A + B| \ge \min(q, |A| + |B| - 1)$, where
$A + B = \{a + b : a \in A, b \in B\}$.

## Sources

- R. C. Vaughan, *The Hardy–Littlewood Method*, 2nd ed., Cambridge Tracts in Mathematics 125, Cambridge University Press, 1997, Lemma 2.14; also stated as Lemma 3.5 in H. Wang and S. Tian, arXiv:2608.12397v1. Mathlib's `ZMod.cauchy_davenport` covers the prime-modulus special case.

Formalized by `MathlibExt.Combinatorics.Additive.CauchyDavenportChowlaWanted.cauchy_davenport_chowla`, a theorem declared in [MathlibExt/Combinatorics/Additive/CauchyDavenportChowla.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Additive/CauchyDavenportChowla.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/index.html#cauchy-davenport-chowla).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Sumsets and inverse theorems](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems)
