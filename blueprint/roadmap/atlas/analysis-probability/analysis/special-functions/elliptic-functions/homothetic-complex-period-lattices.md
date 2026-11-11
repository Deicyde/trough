---
declaration: section
origin: cited
lean: PeriodPair.IsHomothetic, PeriodPair.IsHomothetic.refl, PeriodPair.IsHomothetic.symm, PeriodPair.IsHomothetic.trans, PeriodPair.isHomothetic_equivalence
statement: formalized
proof: formalized
---

# Homothetic complex period lattices

5 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/elliptic-functions/homothetic-complex-period-lattices/index.html).

## Homothetic period pairs

A period pair is a pair $(\omega_1, \omega_2)$ of complex
numbers that are linearly independent over $\mathbb{R}$, and its lattice is
$\Lambda = \mathbb{Z}\omega_1 + \mathbb{Z}\omega_2 \subseteq \mathbb{C}$. Two period pairs
$L$ and $L'$ with lattices $\Lambda$ and $\Lambda'$ are homothetic when there is a nonzero
complex number $c$ such that $\Lambda' = c\Lambda = \{c\lambda : \lambda \in \Lambda\}$.

Formalized by `PeriodPair.IsHomothetic`, a definition declared in [MathlibExt/Analysis/SpecialFunctions/Elliptic/Homothety.lean, line 26](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/SpecialFunctions/Elliptic/Homothety.lean#L26). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/elliptic-functions/homothetic-complex-period-lattices/index.html#is-homothetic).

## Homothety of period pairs is reflexive

Every period pair $L$ is
homothetic to itself.

Formalized by `PeriodPair.IsHomothetic.refl`, a theorem declared in [MathlibExt/Analysis/SpecialFunctions/Elliptic/Homothety.lean, line 30](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/SpecialFunctions/Elliptic/Homothety.lean#L30). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/elliptic-functions/homothetic-complex-period-lattices/index.html#refl).

## Homothety of period pairs is symmetric

If a period pair $L$ is homothetic to a period
pair $L'$, then $L'$ is homothetic to $L$.

Formalized by `PeriodPair.IsHomothetic.symm`, a theorem declared in [MathlibExt/Analysis/SpecialFunctions/Elliptic/Homothety.lean, line 34](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/SpecialFunctions/Elliptic/Homothety.lean#L34). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/elliptic-functions/homothetic-complex-period-lattices/index.html#symm).

## Homothety of period pairs is transitive

For period pairs $L_1$, $L_2$, $L_3$,
if $L_1$ is homothetic to $L_2$ and $L_2$ is homothetic to $L_3$, then $L_1$ is homothetic
to $L_3$.

Formalized by `PeriodPair.IsHomothetic.trans`, a theorem declared in [MathlibExt/Analysis/SpecialFunctions/Elliptic/Homothety.lean, line 40](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/SpecialFunctions/Elliptic/Homothety.lean#L40). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/elliptic-functions/homothetic-complex-period-lattices/index.html#trans).

## Homothety of period pairs is an equivalence relation

On period pairs,
homothety is reflexive, symmetric and transitive.

Formalized by `PeriodPair.isHomothetic_equivalence`, a theorem declared in [MathlibExt/Analysis/SpecialFunctions/Elliptic/Homothety.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/SpecialFunctions/Elliptic/Homothety.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/elliptic-functions/homothetic-complex-period-lattices/index.html#is-homothetic-equivalence).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Homothetic complex period lattices](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/elliptic-functions/homothetic-complex-period-lattices/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Analysis/special-functions/elliptic-functions/homothetic-complex-period-lattices)
