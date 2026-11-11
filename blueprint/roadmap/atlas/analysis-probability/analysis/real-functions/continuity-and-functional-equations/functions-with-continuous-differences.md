---
declaration: section
origin: cited
lean: MathlibExt.Analysis.ErdosProblem907Wanted.conjecture, MathlibExt.Analysis.ErdosProblem907Wanted.conjecture_holds
statement: formalized
---

# Functions with continuous differences

2 results, 1 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/continuity-and-functional-equations/functions-with-continuous-differences/index.html).

## Erdős Problem 907

The statement that every function $f : \mathbb{R} \to \mathbb{R}$
such that $x \mapsto f(x + h) - f(x)$ is continuous for every $h > 0$ can be written as
$f = g + a$ with $g : \mathbb{R} \to \mathbb{R}$ continuous and $a : \mathbb{R} \to \mathbb{R}$
additive, that is, $a(x + y) = a(x) + a(y)$ for all real $x$ and $y$.

Formalized by `MathlibExt.Analysis.ErdosProblem907Wanted.conjecture`, a definition declared in [WantedExt/Analysis/ErdosProblem907Wanted.lean, line 31](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/ErdosProblem907Wanted.lean#L31). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/continuity-and-functional-equations/functions-with-continuous-differences/index.html#conjecture).

## De Bruijn's theorem on continuous differences (Erdős Problem 907)

Let
$f : \mathbb{R} \to \mathbb{R}$ be a function such that for every $h > 0$ the function
$x \mapsto f(x + h) - f(x)$ is continuous. Then there are functions
$g, a : \mathbb{R} \to \mathbb{R}$ with $g$ continuous and $a$ additive, that is,
$a(x + y) = a(x) + a(y)$ for all real $x$ and $y$, such that $f = g + a$.

## Sources

- N. G. de Bruijn, Functions whose differences belong to a given class, Nieuw Archief voor Wiskunde (2) (1951), 194–218, https://mathscinet.ams.org/mathscinet-getitem?mr=43870; External Lean proof of Erdős Problem 907, plby/lean-proofs, https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/v4.29.1/ErdosProblems/Erdos907.lean.

Stated but not proved: `MathlibExt.Analysis.ErdosProblem907Wanted.conjecture_holds` is written with `theorem_wanted` in [WantedExt/Analysis/ErdosProblem907Wanted.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/ErdosProblem907Wanted.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/continuity-and-functional-equations/functions-with-continuous-differences/index.html#conjecture-holds).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Functions with continuous differences](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/continuity-and-functional-equations/functions-with-continuous-differences/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Analysis/real-functions/continuity-and-functional-equations/functions-with-continuous-differences)
