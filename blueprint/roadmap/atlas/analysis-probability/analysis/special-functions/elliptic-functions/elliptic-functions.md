---
declaration: section
origin: cited
lean: PeriodPair.IsLatticePeriodic, PeriodPair.IsEllipticFunction
statement: formalized
proof: formalized
---

# Elliptic functions: its own results

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/elliptic-functions/index.html).

## Lattice-periodic functions

Let $L$ be a pair of $\mathbb{R}$-linearly independent
complex numbers $\omega_1, \omega_2$ with period lattice
$\Lambda = \mathbb{Z}\omega_1 + \mathbb{Z}\omega_2$. A function $f : \mathbb{C} \to \mathbb{C}$
is lattice-periodic for $L$ when every element of $\Lambda$ is a period of $f$, that is,
$f(z + \omega) = f(z)$ for all $\omega \in \Lambda$ and all $z \in \mathbb{C}$.

Formalized by `PeriodPair.IsLatticePeriodic`, a definition declared in [MathlibExt/Analysis/SpecialFunctions/Elliptic/Function.lean, line 22](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/SpecialFunctions/Elliptic/Function.lean#L22). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/elliptic-functions/index.html#is-lattice-periodic).

## Elliptic functions

Let $L$ be a pair of $\mathbb{R}$-linearly independent complex
numbers $\omega_1, \omega_2$ with period lattice
$\Lambda = \mathbb{Z}\omega_1 + \mathbb{Z}\omega_2$. A function $f : \mathbb{C} \to \mathbb{C}$
is an elliptic function for $L$ when it is meromorphic at every point of $\mathbb{C}$ and
lattice-periodic for $L$, that is, $f(z + \omega) = f(z)$ for all $z \in \mathbb{C}$ and all
$\omega \in \Lambda$.

Formalized by `PeriodPair.IsEllipticFunction`, a structure declared in [MathlibExt/Analysis/SpecialFunctions/Elliptic/Function.lean, line 26](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/SpecialFunctions/Elliptic/Function.lean#L26). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/elliptic-functions/index.html#is-elliptic-function).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Elliptic functions](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/elliptic-functions/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Analysis/special-functions/elliptic-functions)
