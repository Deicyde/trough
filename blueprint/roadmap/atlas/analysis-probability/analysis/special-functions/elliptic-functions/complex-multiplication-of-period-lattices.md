---
declaration: section
origin: cited
lean: PeriodPair.endomorphismRing, PeriodPair.IsProperIdeal
statement: formalized
proof: formalized
---

# Complex multiplication of period lattices

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/elliptic-functions/complex-multiplication-of-period-lattices/index.html).

## Endomorphism ring of a period lattice

Let $\omega_1, \omega_2$ be
$\mathbb{R}$-linearly independent complex numbers with period lattice
$\Lambda = \mathbb{Z}\omega_1 + \mathbb{Z}\omega_2$. The endomorphism ring of $\Lambda$ is the
subring of $\mathbb{C}$ consisting of all $a \in \mathbb{C}$ such that $a z \in \Lambda$ for every
$z \in \Lambda$.

Formalized by `PeriodPair.endomorphismRing`, a definition declared in [MathlibExt/Analysis/SpecialFunctions/Elliptic/ComplexMultiplication.lean, line 24](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/SpecialFunctions/Elliptic/ComplexMultiplication.lean#L24). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/elliptic-functions/complex-multiplication-of-period-lattices/index.html#endomorphism-ring).

## Lattices that are proper ideals

Let $\Lambda$ be the period lattice of a pair of
$\mathbb{R}$-linearly independent complex numbers, and let $\mathcal{O}$ be a subring of
$\mathbb{C}$. Then $\Lambda$ is a proper ideal of $\mathcal{O}$ when the endomorphism ring of
$\Lambda$, the subring of all $a \in \mathbb{C}$ with $a z \in \Lambda$ for every $z \in \Lambda$,
equals $\mathcal{O}$.

The ambient assumptions that $\mathcal{O}$ is an imaginary quadratic order and that $\Lambda$ is
an $\mathcal{O}$-ideal are deliberately kept separate from this predicate.

Formalized by `PeriodPair.IsProperIdeal`, a definition declared in [MathlibExt/Analysis/SpecialFunctions/Elliptic/ComplexMultiplication.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/SpecialFunctions/Elliptic/ComplexMultiplication.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/elliptic-functions/complex-multiplication-of-period-lattices/index.html#is-proper-ideal).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Complex multiplication of period lattices](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/elliptic-functions/complex-multiplication-of-period-lattices/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Analysis/special-functions/elliptic-functions/complex-multiplication-of-period-lattices)
