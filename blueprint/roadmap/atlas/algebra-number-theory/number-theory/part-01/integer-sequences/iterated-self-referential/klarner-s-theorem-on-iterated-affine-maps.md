---
declaration: section
origin: cited
lean: MathlibExt.Combinatorics.AffineMapIterateRepetitionErdosProblem481Wanted.affineExpand, MathlibExt.Combinatorics.AffineMapIterateRepetitionErdosProblem481Wanted.affineIterateHasRepetition, MathlibExt.Combinatorics.AffineMapIterateRepetitionErdosProblem481Wanted.affineIterateHasRepetition_holds
statement: formalized
---

# Klarner's theorem on iterated affine maps

3 results, 2 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/iterated-self-referential/klarner-s-theorem-on-iterated-affine-maps/index.html).

## Affine expansion of a sequence

For $r \in \mathbb{N}$, maps
$a, b : \{0, \dots, r - 1\} \to \mathbb{N}$ and a finite sequence $A = (x_1, \dots, x_n)$ of
natural numbers, $T(A)$ is the sequence of length $rn$ obtained by listing the blocks
$(a_i x_1 + b_i, \dots, a_i x_n + b_i)$ one after another for $i = 0, 1, \dots, r - 1$.

The order of the entries does not affect whether an entry repeats.

Formalized by `MathlibExt.Combinatorics.AffineMapIterateRepetitionErdosProblem481Wanted.affineExpand`, a definition declared in [WantedExt/Combinatorics/AffineMapIterateRepetitionErdosProblem481Wanted.lean, line 39](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/AffineMapIterateRepetitionErdosProblem481Wanted.lean#L39). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/iterated-self-referential/klarner-s-theorem-on-iterated-affine-maps/index.html#affine-expand).

## Erdős Problem 481: repetitions under affine expansion

The statement that for every
$r \in \mathbb{N}$ and all maps $a, b : \{0, \dots, r - 1\} \to \mathbb{N}$ with $a_i \ge 1$ for
every $i$ and $\sum_{i < r} 1 / a_i > 1$, if $T$ is the affine expansion of $a$ and $b$, sending a
finite sequence $(x_1, \dots, x_n)$ of natural numbers to the sequence of all $a_i x_j + b_i$,
listed in blocks for $i = 0, 1, \dots, r - 1$ (the order does not affect whether an entry repeats),
then, starting from $A_1 = (1)$ with $A_{k+1} = T(A_k)$, some $A_k$ has a repeated entry.

Formalized by `MathlibExt.Combinatorics.AffineMapIterateRepetitionErdosProblem481Wanted.affineIterateHasRepetition`, a definition declared in [WantedExt/Combinatorics/AffineMapIterateRepetitionErdosProblem481Wanted.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/AffineMapIterateRepetitionErdosProblem481Wanted.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/iterated-self-referential/klarner-s-theorem-on-iterated-affine-maps/index.html#affine-iterate-has-repetition).

## Klarner's theorem (Erdős Problem 481)

For every $r \in \mathbb{N}$ and all maps
$a, b : \{0, \dots, r - 1\} \to \mathbb{N}$ with $a_i \ge 1$ for every $i$ and
$\sum_{i < r} 1 / a_i > 1$, let $T$ send a finite sequence $(x_1, \dots, x_n)$ of natural numbers
to the sequence of all $a_i x_j + b_i$, listed in blocks for $i = 0, 1, \dots, r - 1$. Then,
starting from $A_1 = (1)$ with $A_{k+1} = T(A_k)$, some $A_k$ has a repeated entry.

This was first shown by Klarner and generalized by Kolpakov and Talambutsa.

## Sources

- T. F. Bloom, Erdős Problems, Problem #481, https://www.erdosproblems.com/481 (status PROVED (LEAN)); resolution: D. A. Klarner, A sufficient condition for certain semigroups to be free, J. Algebra (1982), 140-148; A. Kolpakov and A. Talambutsa, On free semigroups of affine maps on the real line, Proc. Amer. Math. Soc. (2022), 2301-2307, erdosproblems.com/481: true, first shown by Klarner; generalized by Kolpakov and Talambutsa, https://www.erdosproblems.com/481.

Stated but not proved: `MathlibExt.Combinatorics.AffineMapIterateRepetitionErdosProblem481Wanted.affineIterateHasRepetition_holds` is written with `theorem_wanted` in [WantedExt/Combinatorics/AffineMapIterateRepetitionErdosProblem481Wanted.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/AffineMapIterateRepetitionErdosProblem481Wanted.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/iterated-self-referential/klarner-s-theorem-on-iterated-affine-maps/index.html#affine-iterate-has-repetition-holds).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Klarner's theorem on iterated affine maps](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/iterated-self-referential/klarner-s-theorem-on-iterated-affine-maps/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/integer-sequences/iterated-self-referential/klarner-s-theorem-on-iterated-affine-maps)
