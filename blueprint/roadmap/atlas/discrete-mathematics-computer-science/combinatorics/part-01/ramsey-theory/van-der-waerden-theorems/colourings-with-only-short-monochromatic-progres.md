---
declaration: section
origin: cited
lean: MathlibExt.Combinatorics.ShortMonochromaticProgressionsErdosProblem984Wanted.twoColouringShortProgressions, MathlibExt.Combinatorics.ShortMonochromaticProgressionsErdosProblem984Wanted.twoColouringShortProgressions_holds
statement: formalized
---

# Colourings with only short monochromatic progressions

2 results, 1 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/van-der-waerden-theorems/colourings-with-only-short-monochromatic-progres/index.html).

## Statement of Erdős Problem 984 on short monochromatic progressions

The proposition that
there is a colouring of the positive integers with two colours such that for every real
$\varepsilon > 0$ there is a real constant $C_\varepsilon$ with the following property: whenever
$a \ge 1$, $d \ge 1$ and $k \ge 0$ are integers and $a, a + d, \dots, a + (k - 1)d$ all have the
same colour, $k \le C_\varepsilon a^\varepsilon$.

Formalized by `MathlibExt.Combinatorics.ShortMonochromaticProgressionsErdosProblem984Wanted.twoColouringShortProgressions`, a definition declared in [WantedExt/Combinatorics/ShortMonochromaticProgressionsErdosProblem984Wanted.lean, line 39](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/ShortMonochromaticProgressionsErdosProblem984Wanted.lean#L39). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/van-der-waerden-theorems/colourings-with-only-short-monochromatic-progres/index.html#two-colouring-short-progressions).

## Erdős Problem 984: a two-colouring with short monochromatic progressions exists

There is a
colouring of the positive integers with two colours such that for every real $\varepsilon > 0$
there is a real constant $C_\varepsilon$ with the following property: whenever $a \ge 1$,
$d \ge 1$ and $k \ge 0$ are integers and $a, a + d, \dots, a + (k - 1)d$ all have the same
colour, $k \le C_\varepsilon a^\varepsilon$.

## Sources

- T. F. Bloom, Erdős Problems, Problem #984, https://www.erdosproblems.com/984 (status PROVED); resolution: Z. Hunter, proof in the erdosproblems.com/984 comments, using Green's red-blue colourings for off-diagonal van der Waerden numbers, erdosproblems.com/984: 'Zach Hunter has proved the answer is yes (see the comments)'; the comment colours each block I_t = [100^t, 100^{t+1}) with no red 3-term progression and no blue progression of length k_t = |I_t|^{o(1)} for odd t (colours swapped for even t), https://www.erdosproblems.com/forum/thread/984.

Stated but not proved: `MathlibExt.Combinatorics.ShortMonochromaticProgressionsErdosProblem984Wanted.twoColouringShortProgressions_holds` is written with `theorem_wanted` in [WantedExt/Combinatorics/ShortMonochromaticProgressionsErdosProblem984Wanted.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/ShortMonochromaticProgressionsErdosProblem984Wanted.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/van-der-waerden-theorems/colourings-with-only-short-monochromatic-progres/index.html#two-colouring-short-progressions-holds).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Colourings with only short monochromatic progressions](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/van-der-waerden-theorems/colourings-with-only-short-monochromatic-progres/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/ramsey-theory/van-der-waerden-theorems/colourings-with-only-short-monochromatic-progres)
