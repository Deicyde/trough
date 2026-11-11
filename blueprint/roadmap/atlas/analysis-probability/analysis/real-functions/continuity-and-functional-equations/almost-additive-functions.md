---
declaration: section
origin: cited
lean: MathlibExt.Analysis.ErdosProblem1126Wanted.conjecture, MathlibExt.Analysis.ErdosProblem1126Wanted.conjecture_holds
statement: formalized
---

# Almost additive functions

2 results, 1 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/continuity-and-functional-equations/almost-additive-functions/index.html).

## Erdős Problem 1126 on almost additive functions

This is the statement that for every
function $f : \mathbb{R} \to \mathbb{R}$ with $f(x + y) = f(x) + f(y)$ for almost every
$(x, y) \in \mathbb{R}^2$ with respect to Lebesgue measure on $\mathbb{R}^2$, there is a function
$h : \mathbb{R} \to \mathbb{R}$ with $h(x + y) = h(x) + h(y)$ for all $x, y \in \mathbb{R}$ and
$f(x) = h(x)$ for almost every $x \in \mathbb{R}$.

## Sources

- erdosproblems.com/1126 (record FC-ErdosProblem1126).

Formalized by `MathlibExt.Analysis.ErdosProblem1126Wanted.conjecture`, a definition declared in [WantedExt/Analysis/ErdosProblem1126Wanted.lean, line 32](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/ErdosProblem1126Wanted.lean#L32). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/continuity-and-functional-equations/almost-additive-functions/index.html#conjecture).

## Almost additive functions agree almost everywhere with additive functions

Let
$f : \mathbb{R} \to \mathbb{R}$ satisfy $f(x + y) = f(x) + f(y)$ for almost every
$(x, y) \in \mathbb{R}^2$ with respect to Lebesgue measure on $\mathbb{R}^2$. Then there is a
function $h : \mathbb{R} \to \mathbb{R}$ with $h(x + y) = h(x) + h(y)$ for all
$x, y \in \mathbb{R}$ and $f(x) = h(x)$ for almost every $x \in \mathbb{R}$.

## Sources

- de Bruijn [dB66] and Jurkat [Ju65], independently, per erdosproblems.com/1126, https://www.erdosproblems.com/1126.

Stated but not proved: `MathlibExt.Analysis.ErdosProblem1126Wanted.conjecture_holds` is written with `theorem_wanted` in [WantedExt/Analysis/ErdosProblem1126Wanted.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/ErdosProblem1126Wanted.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/continuity-and-functional-equations/almost-additive-functions/index.html#conjecture-holds).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Almost additive functions](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/continuity-and-functional-equations/almost-additive-functions/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Analysis/real-functions/continuity-and-functional-equations/almost-additive-functions)
