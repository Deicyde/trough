---
declaration: section
origin: cited
lean: ArithmeticFunction.IsCompletelyMultiplicative, ArithmeticFunction.IsCompletelyMultiplicative.map_mul, ArithmeticFunction.IsCompletelyMultiplicative.isMultiplicative
statement: formalized
proof: formalized
---

# Completely multiplicative functions

3 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/completely-multiplicative-functions/index.html).

## Completely multiplicative arithmetic function

Let $R$ be a type with a multiplication and
a zero. An arithmetic function $f$ with values in $R$ (so $f(0) = 0$) is completely multiplicative
if $f(mn) = f(m) f(n)$ for all $m, n \in \mathbb{N} = \{0, 1, 2, \dots\}$.

The normalization $f(1) = 1$ is not part of the definition.

Formalized by `ArithmeticFunction.IsCompletelyMultiplicative`, a definition declared in [MathlibExt/NumberTheory/ArithmeticFunction/CompletelyMultiplicative.lean, line 31](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/ArithmeticFunction/CompletelyMultiplicative.lean#L31). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/completely-multiplicative-functions/index.html#is-completely-multiplicative).

## Completely multiplicative functions preserve products

Let $R$ be a type with a
multiplication and a zero, and let $f$ be a completely multiplicative arithmetic function with
values in $R$. Then $f(mn) = f(m) f(n)$ for all $m, n \in \mathbb{N}$.

Formalized by `ArithmeticFunction.IsCompletelyMultiplicative.map_mul`, a theorem declared in [MathlibExt/NumberTheory/ArithmeticFunction/CompletelyMultiplicative.lean, line 36](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/ArithmeticFunction/CompletelyMultiplicative.lean#L36). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/completely-multiplicative-functions/index.html#map-mul).

## Normalized completely multiplicative functions are multiplicative

Let $R$ be a monoid
with zero and let $f$ be a completely multiplicative arithmetic function with values in $R$ such
that $f(1) = 1$. Then $f$ is multiplicative: $f(1) = 1$ and $f(mn) = f(m) f(n)$ for all coprime
natural numbers $m$ and $n$.

Formalized by `ArithmeticFunction.IsCompletelyMultiplicative.isMultiplicative`, a theorem declared in [MathlibExt/NumberTheory/ArithmeticFunction/CompletelyMultiplicative.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/ArithmeticFunction/CompletelyMultiplicative.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/completely-multiplicative-functions/index.html#is-multiplicative).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Completely multiplicative functions](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/completely-multiplicative-functions/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/completely-multiplicative-functions)
