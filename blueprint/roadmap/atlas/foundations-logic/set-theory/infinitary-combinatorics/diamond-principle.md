---
declaration: section
origin: cited
lean: MetaMathlibExt.Diamond, MetaMathlibExt.DiamondMinus
statement: formalized
proof: formalized
---

# Diamond principle

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/SetTheory/infinitary-combinatorics/diamond-principle/index.html).

## Diamond principle

◇_κ holds iff there is a sequence ⟨ S_α : α < κ⟩ with S_α ⊆ α for all α < κ, such that for every
X ⊆ κ, {α < κ : X ∩ α = S_α} is stationary in κ.

Formalized by `MetaMathlibExt.Diamond`, a definition declared in [MathlibExt/SetTheory/InfinitaryCombinatorics/Diamond.lean, line 31](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/SetTheory/InfinitaryCombinatorics/Diamond.lean#L31). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/SetTheory/infinitary-combinatorics/diamond-principle/index.html#diamond-principle).

## Diamond-minus principle

◇⁻_κ holds iff there is a sequence ⟨ 𝒜_α : α < κ⟩ with each 𝒜_α ⊆ 𝒫(α) and |𝒜_α| ≤ |α|, such
that for every X ⊆ κ the set {α < κ : X ∩ α ∈ 𝒜_α} is stationary in κ.

Formalized by `MetaMathlibExt.DiamondMinus`, a definition declared in [MathlibExt/SetTheory/InfinitaryCombinatorics/Diamond.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/SetTheory/InfinitaryCombinatorics/Diamond.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/SetTheory/infinitary-combinatorics/diamond-principle/index.html#diamond-minus-principle).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Diamond principle](https://deicyde.github.io/atlas-lean/roadmap/SetTheory/infinitary-combinatorics/diamond-principle/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/SetTheory/infinitary-combinatorics/diamond-principle)
