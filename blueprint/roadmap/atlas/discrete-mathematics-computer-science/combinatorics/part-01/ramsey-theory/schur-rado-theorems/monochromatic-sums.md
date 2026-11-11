---
declaration: section
origin: cited
lean: MathlibExt.Combinatorics.MonochromaticSumsLinearErdosProblem484Wanted.monochromaticSumsLinearCount, MathlibExt.Combinatorics.MonochromaticSumsLinearErdosProblem484Wanted.monochromaticSumsLinearCount_holds
statement: formalized
---

# Monochromatic sums

2 results, 1 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/schur-rado-theorems/monochromatic-sums/index.html).

## Erdős Problem 484: linearly many monochromatic sums

This is the statement that there is a
real constant $c > 0$ such that for every integer $k \ge 1$ there is an $N_0 \in \mathbb{N}$ with
the following property: for every $N \ge N_0$ and every colouring
$f : \mathbb{N} \to \{0, \dots, k-1\}$, at least $cN$ of the integers $n \in \{1, \dots, N\}$ can
be written as $n = a + b$ with $a, b \in \{1, \dots, N\}$, $a \ne b$ and $f(a) = f(b)$.

Only the colours of $1, \dots, N$ matter, so this is a statement about $k$-colourings of
$\{1, \dots, N\}$; $c$ does not depend on $k$, while $N_0$ may.

Formalized by `MathlibExt.Combinatorics.MonochromaticSumsLinearErdosProblem484Wanted.monochromaticSumsLinearCount`, a definition declared in [WantedExt/Combinatorics/MonochromaticSumsLinearErdosProblem484Wanted.lean, line 40](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/MonochromaticSumsLinearErdosProblem484Wanted.lean#L40). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/schur-rado-theorems/monochromatic-sums/index.html#monochromatic-sums-linear-count).

## Erdős–Sárközy–Sós theorem on monochromatic sums (Erdős Problem 484)

There is a real constant
$c > 0$ such that for every integer $k \ge 1$ there is an $N_0 \in \mathbb{N}$ such that for every
$N \ge N_0$ and every colouring $f : \mathbb{N} \to \{0, \dots, k-1\}$, at least $cN$ of the
integers $n \in \{1, \dots, N\}$ can be written as $n = a + b$ with $a, b \in \{1, \dots, N\}$,
$a \ne b$ and $f(a) = f(b)$.

Erdős, Sárközy and Sós proved that at least $N/2 - O(N^{1 - 1/2^{k+1}})$ even numbers in
$\{1, \dots, N\}$ are such monochromatic sums, so any $c < 1/2$ works.

## Sources

- T. F. Bloom, Erdős Problems, Problem #484, https://www.erdosproblems.com/484 (status PROVED (LEAN)); resolution: P. Erdős, A. Sárközy and V. T. Sós, On a conjecture of Roth and some related problems. I (1989), 47-59, erdosproblems.com/484: at least N/2 - O(N^{1 - 1/2^{k+1}}) even numbers are monochromatic sums, https://www.erdosproblems.com/484.

Stated but not proved: `MathlibExt.Combinatorics.MonochromaticSumsLinearErdosProblem484Wanted.monochromaticSumsLinearCount_holds` is written with `theorem_wanted` in [WantedExt/Combinatorics/MonochromaticSumsLinearErdosProblem484Wanted.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/MonochromaticSumsLinearErdosProblem484Wanted.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/schur-rado-theorems/monochromatic-sums/index.html#monochromatic-sums-linear-count-holds).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Monochromatic sums](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/schur-rado-theorems/monochromatic-sums/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/ramsey-theory/schur-rado-theorems/monochromatic-sums)
