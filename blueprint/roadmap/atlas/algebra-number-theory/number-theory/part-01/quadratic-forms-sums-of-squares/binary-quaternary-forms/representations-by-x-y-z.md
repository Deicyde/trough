---
declaration: section
origin: cited
lean: MathlibExt.NumberTheory.ErdosProblem1148Wanted.Erdos1148Prop, MathlibExt.NumberTheory.ErdosProblem1148Wanted.weaker_prop, MathlibExt.NumberTheory.ErdosProblem1148Wanted.eventualRepresentation, MathlibExt.NumberTheory.ErdosProblem1148Wanted.weakerBound, MathlibExt.NumberTheory.ErdosProblem1148Wanted.eventualRepresentation_holds
statement: formalized
---

# Representations by x² + y² − z²

5 results, 4 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/binary-quaternary-forms/representations-by-x-y-z/index.html).

## Bounded representation by $x^2 + y^2 - z^2$

A natural number $n$ has a bounded
representation by $x^2 + y^2 - z^2$ if there are natural numbers $x, y, z$ with
$n = x^2 + y^2 - z^2$ and $x^2 \le n$, $y^2 \le n$, $z^2 \le n$, where the subtraction is
truncated subtraction of natural numbers.

The truncation changes nothing: a nonzero truncated difference is the true difference, and
$0 = 0^2 + 0^2 - 0^2$.

Formalized by `MathlibExt.NumberTheory.ErdosProblem1148Wanted.Erdos1148Prop`, a definition declared in [WantedExt/NumberTheory/ErdosProblem1148Wanted.lean, line 31](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ErdosProblem1148Wanted.lean#L31). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/binary-quaternary-forms/representations-by-x-y-z/index.html#erdos1148-prop).

## Representation by $x^2 + y^2 - z^2$ with the bound $n + 2\sqrt{n}$

A natural number $n$ has this representation if there are natural numbers $x, y, z$ with
$n = x^2 + y^2 - z^2$, where the subtraction is truncated subtraction of natural numbers, and
each of $x^2$, $y^2$, $z^2$ is at most $n + 2\sqrt{n}$ as a real number.

This weaker bound is reported obvious in [Va99].

Formalized by `MathlibExt.NumberTheory.ErdosProblem1148Wanted.weaker_prop`, a definition declared in [WantedExt/NumberTheory/ErdosProblem1148Wanted.lean, line 35](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ErdosProblem1148Wanted.lean#L35). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/binary-quaternary-forms/representations-by-x-y-z/index.html#weaker-prop).

## Eventual bounded representation by $x^2 + y^2 - z^2$

The statement that every
sufficiently large natural number $n$ can be written as $n = x^2 + y^2 - z^2$ with natural
numbers $x, y, z$ satisfying $\max(x^2, y^2, z^2) \le n$.

Formalized by `MathlibExt.NumberTheory.ErdosProblem1148Wanted.eventualRepresentation`, a definition declared in [WantedExt/NumberTheory/ErdosProblem1148Wanted.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ErdosProblem1148Wanted.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/binary-quaternary-forms/representations-by-x-y-z/index.html#eventual-representation).

## Representability of every $n$ with the bound $n + 2\sqrt{n}$

The statement that every
natural number $n$ can be written as $n = x^2 + y^2 - z^2$ with natural numbers $x, y, z$,
the subtraction being truncated subtraction of natural numbers, such that each of $x^2$, $y^2$,
$z^2$ is at most $n + 2\sqrt{n}$.

Formalized by `MathlibExt.NumberTheory.ErdosProblem1148Wanted.weakerBound`, a definition declared in [WantedExt/NumberTheory/ErdosProblem1148Wanted.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ErdosProblem1148Wanted.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/binary-quaternary-forms/representations-by-x-y-z/index.html#weaker-bound).

## Every large integer is a bounded value of $x^2 + y^2 - z^2$ (Erdős Problem 1148)

For every sufficiently large natural number $n$ there are natural numbers $x, y, z$ with
$n = x^2 + y^2 - z^2$ and $\max(x^2, y^2, z^2) \le n$.

Resolved true: Resolved affirmatively (Chojecki with GPT-5.4 Pro via Duke-type theorem
[ELMV12]), per erdosproblems.com/1148. Source: P. Chojecki, Bounded Representations by
x^2+y^2-z^2, arXiv:2603.18087 (2026), https://arxiv.org/abs/2603.18087. Moved from
`OpenConjectures/NumberTheory/ErdosProblem1148`.

Stated but not proved: `MathlibExt.NumberTheory.ErdosProblem1148Wanted.eventualRepresentation_holds` is written with `theorem_wanted` in [WantedExt/NumberTheory/ErdosProblem1148Wanted.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ErdosProblem1148Wanted.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/binary-quaternary-forms/representations-by-x-y-z/index.html#eventual-representation-holds).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Representations by x² + y² − z²](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/binary-quaternary-forms/representations-by-x-y-z/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/quadratic-forms-sums-of-squares/binary-quaternary-forms/representations-by-x-y-z)
