---
declaration: section
origin: cited
lean: MathlibExt.Analysis.FunctionalAnalysis.CountableBasisFiniteDimensional.finiteDimensional_of_countable_basis, MathlibExt.Analysis.FunctionalAnalysis.CountableBasisFiniteDimensional.not_countable_basis_of_not_finiteDimensional
statement: formalized
proof: formalized
---

# Hamel bases of Banach spaces

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/duality-and-weak-topologies/hamel-bases-of-banach-spaces/index.html).

## A Banach space with a countable Hamel basis is finite-dimensional

If `E` is a complete normed space over `𝕜 = ℝ, ℂ` admitting a Hamel basis
indexed by a countable type, then `E` is finite-dimensional. Completeness
is essential: it is what the Baire category argument uses.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.CountableBasisFiniteDimensional.finiteDimensional_of_countable_basis`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/CountableBasisFiniteDimensional.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/CountableBasisFiniteDimensional.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/duality-and-weak-topologies/hamel-bases-of-banach-spaces/index.html#finite-dimensional-of-countable-basis).

## An infinite-dimensional Banach space has no countable Hamel basis

Let $E$ be a complete
normed space over $\mathbb{K} = \mathbb{R}$ or $\mathbb{C}$. If $E$ is not finite-dimensional,
then no Hamel basis of $E$ is indexed by a countable set.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.CountableBasisFiniteDimensional.not_countable_basis_of_not_finiteDimensional`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/CountableBasisFiniteDimensional.lean, line 89](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/CountableBasisFiniteDimensional.lean#L89). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/duality-and-weak-topologies/hamel-bases-of-banach-spaces/index.html#not-countable-basis-of-not-finite-dimens).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Hamel bases of Banach spaces](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/duality-and-weak-topologies/hamel-bases-of-banach-spaces/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Analysis/banach-spaces/duality-and-weak-topologies/hamel-bases-of-banach-spaces)
