---
declaration: section
origin: cited
lean: MathlibExt.NumberTheory.ErdosProblem1196Wanted.IsPrimitive, MathlibExt.NumberTheory.ErdosProblem1196Wanted.conjecture, MathlibExt.NumberTheory.ErdosProblem1196Wanted.conjecture_holds
statement: formalized
---

# Primitive sets

3 results, 2 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/additive-number-theory/primitive-sets/index.html).

## Primitive set in a commutative monoid

A subset $A$ of a commutative monoid $M$ is
primitive if for all $x, y \in A$ with $x \mid y$, the elements $x$ and $y$ are associated,
that is, $x u = y$ for some unit $u$ of $M$. In $\mathbb{N}$, where $1$ is the only unit, this
says that no element of $A$ divides a different element of $A$.

Formalized by `MathlibExt.NumberTheory.ErdosProblem1196Wanted.IsPrimitive`, a definition declared in [WantedExt/NumberTheory/ErdosProblem1196Wanted.lean, line 34](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ErdosProblem1196Wanted.lean#L34). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/additive-number-theory/primitive-sets/index.html#is-primitive).

## Asymptotic primitive set bound

The statement that there is a function
$o : \mathbb{N} \to \mathbb{R}$ with $o(x) \to 0$ as $x \to \infty$ such that for every natural
number $x > 0$ and every primitive set $A$ of natural numbers contained in $[x, \infty)$, the
series $\sum_{a \in A} \frac{1}{a \log a}$ is summable and
$\sum_{a \in A} \frac{1}{a \log a} < 1 + o(x)$. Here a set of natural numbers is primitive if
no element divides a different element, and the term for $a = 1$, where $\log a = 0$, is taken
to be $0$.

Formalized by `MathlibExt.NumberTheory.ErdosProblem1196Wanted.conjecture`, a definition declared in [WantedExt/NumberTheory/ErdosProblem1196Wanted.lean, line 38](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ErdosProblem1196Wanted.lean#L38). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/additive-number-theory/primitive-sets/index.html#conjecture).

## Erdős Problem 1196 on primitive sets

There is a function $o : \mathbb{N} \to \mathbb{R}$
with $o(x) \to 0$ as $x \to \infty$ such that for every natural number $x > 0$ and every
primitive set $A$ of natural numbers contained in $[x, \infty)$, the series
$\sum_{a \in A} \frac{1}{a \log a}$ is summable and $\sum_{a \in A} \frac{1}{a \log a} < 1 + o(x)$.
Here a set of natural numbers is primitive if no element divides a different element, and the
term for $a = 1$, where $\log a = 0$, is taken to be $0$.

Resolved true: Resolved affirmatively (GPT-5.4 Pro prompted by Price; account [ABLLPSTT26]), per
erdosproblems.com/1196. Source: B. Alexeev, K. Barreto, Y. Li, J. D. Lichtman, L. Price, J. I.
Shah, Q. Tang, T. Tao, Primitive sets and von Mangoldt chains: Erdős Problem #1196 and beyond,
arXiv:2605.00301 (2026), https://arxiv.org/abs/2605.00301. Moved from
`OpenConjectures/NumberTheory/ErdosProblem1196`.

Stated but not proved: `MathlibExt.NumberTheory.ErdosProblem1196Wanted.conjecture_holds` is written with `theorem_wanted` in [WantedExt/NumberTheory/ErdosProblem1196Wanted.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ErdosProblem1196Wanted.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/additive-number-theory/primitive-sets/index.html#conjecture-holds).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Primitive sets](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/additive-number-theory/primitive-sets/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/additive-number-theory/primitive-sets)
