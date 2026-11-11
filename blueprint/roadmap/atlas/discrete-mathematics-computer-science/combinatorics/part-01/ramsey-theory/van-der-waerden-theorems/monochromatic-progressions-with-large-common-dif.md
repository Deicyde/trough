---
declaration: section
origin: cited
lean: MathlibExt.Combinatorics.MonochromaticProgressionLargeDifferenceErdosProblem645Wanted.monochromaticProgressionLargeDifference, MathlibExt.Combinatorics.MonochromaticProgressionLargeDifferenceErdosProblem645Wanted.monochromaticProgressionLargeDifference_holds
statement: formalized
---

# Monochromatic progressions with large common difference

2 results, 1 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/van-der-waerden-theorems/monochromatic-progressions-with-large-common-dif/index.html).

## Erdős Problem 645

The statement that for every colouring of the positive integers with
two colours there are positive integers $x$ and $d$ with $d > x$ such that $x$, $x + d$ and
$x + 2d$ all have the same colour.

Formalized by `MathlibExt.Combinatorics.MonochromaticProgressionLargeDifferenceErdosProblem645Wanted.monochromaticProgressionLargeDifference`, a definition declared in [WantedExt/Combinatorics/MonochromaticProgressionLargeDifferenceErdosProblem645Wanted.lean, line 36](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/MonochromaticProgressionLargeDifferenceErdosProblem645Wanted.lean#L36). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/van-der-waerden-theorems/monochromatic-progressions-with-large-common-dif/index.html#monochromatic-progression-large-differen).

## Erdős Problem 645 is true

For every colouring of the positive integers with two colours
there are positive integers $x$ and $d$ with $d > x$ such that $x$, $x + d$ and $x + 2d$ all
have the same colour.

Brown and Landman proved more: for every increasing function $f$ there is such a monochromatic
progression with $d > f(x)$. Erdős Problems also records a short argument of Alweiss.

## Sources

- T. F. Bloom, Erdős Problems, Problem #645, https://www.erdosproblems.com/645 (status PROVED (LEAN)); resolution: T. C. Brown and B. M. Landman, Monochromatic arithmetic progressions with large differences, Bull. Austral. Math. Soc. (1999), 21-35, erdosproblems.com/645: first proved by Brown and Landman, with d > f(x) for any increasing f; the page records a short argument of Alweiss, https://www.erdosproblems.com/645.

Stated but not proved: `MathlibExt.Combinatorics.MonochromaticProgressionLargeDifferenceErdosProblem645Wanted.monochromaticProgressionLargeDifference_holds` is written with `theorem_wanted` in [WantedExt/Combinatorics/MonochromaticProgressionLargeDifferenceErdosProblem645Wanted.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/MonochromaticProgressionLargeDifferenceErdosProblem645Wanted.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/van-der-waerden-theorems/monochromatic-progressions-with-large-common-dif/index.html#monochromatic-progression-large-differen-2).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Monochromatic progressions with large common difference](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/van-der-waerden-theorems/monochromatic-progressions-with-large-common-dif/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/ramsey-theory/van-der-waerden-theorems/monochromatic-progressions-with-large-common-dif)
