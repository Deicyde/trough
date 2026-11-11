---
declaration: section
origin: cited
lean: MetaMathlibExt.IsAlmostDisjointFamilyKappa, MetaMathlibExt.AlmostDisjointModNS, MetaMathlibExt.IsAlmostDisjointFunFamily
statement: formalized
proof: formalized
---

# Almost disjoint families

3 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/SetTheory/infinitary-combinatorics/almost-disjoint-families/index.html).

## $\kappa$-almost disjoint family of sets

A family F ⊆ 𝒫(I) is *κ-almost disjoint* if |A| = κ for every A ∈ F and |A ∩ B| < κ for all
distinct A, B ∈ F.

Formalized by `MetaMathlibExt.IsAlmostDisjointFamilyKappa`, a definition declared in [MathlibExt/SetTheory/InfinitaryCombinatorics/AlmostDisjoint.lean, line 39](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/SetTheory/InfinitaryCombinatorics/AlmostDisjoint.lean#L39). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/SetTheory/infinitary-combinatorics/almost-disjoint-families/index.html#kappa-almost-disjoint-family-of-sets).

## Functions almost disjoint modulo the nonstationary ideal

Functions f, g ∈ ∏_{α<ω₁} A_α are *almost disjoint mod the nonstationary ideal* if the set {  α
< ω₁ : f(α) = g(α)  } on which they agree is nonstationary in ω₁.

Formalized by `MetaMathlibExt.AlmostDisjointModNS`, a definition declared in [MathlibExt/SetTheory/InfinitaryCombinatorics/AlmostDisjoint.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/SetTheory/InfinitaryCombinatorics/AlmostDisjoint.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/SetTheory/infinitary-combinatorics/almost-disjoint-families/index.html#functions-almost-disjoint-modulo-the-non).

## Almost disjoint family of functions on a regular cardinal

Let κ be a regular cardinal. A family of functions κ → κ is *almost disjoint* if for all f and g
in the family with f≠ g, |{ α ∣ f(α ) = g(α ) }|<κ..

Formalized by `MetaMathlibExt.IsAlmostDisjointFunFamily`, a definition declared in [MathlibExt/SetTheory/InfinitaryCombinatorics/AlmostDisjoint.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/SetTheory/InfinitaryCombinatorics/AlmostDisjoint.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/SetTheory/infinitary-combinatorics/almost-disjoint-families/index.html#almost-disjoint-family-of-functions-on-a).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Almost disjoint families](https://deicyde.github.io/atlas-lean/roadmap/SetTheory/infinitary-combinatorics/almost-disjoint-families/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/SetTheory/infinitary-combinatorics/almost-disjoint-families)
