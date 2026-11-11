---
declaration: section
origin: cited
lean: MathlibExt.Combinatorics.SimpleGraph.GirthFiveExtremalValuesWanted.girthFiveExtremalNumber, MathlibExt.Combinatorics.SimpleGraph.GirthFiveExtremalValuesWanted.girthFiveExtremalNumber_one_to_twenty, MathlibExt.Combinatorics.SimpleGraph.GirthFiveExtremalValuesWanted.girthFiveExtremalNumber_fifty
statement: formalized
---

# Extremal graphs of girth five

3 results, 1 proved and 2 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/extremal-graph-theory/extremal-graphs-of-girth-five/index.html).

## Girth-five extremal number

For a natural number $n$, $\mathrm{ex}(n; \{C_3, C_4\})$
is the largest number of edges of a simple graph on $n$ vertices whose girth is at least $5$,
that is, which contains no triangle and no four-cycle (OEIS A006856). An acyclic graph has
infinite girth, so the empty graph always qualifies.

Formalized by `MathlibExt.Combinatorics.SimpleGraph.GirthFiveExtremalValuesWanted.girthFiveExtremalNumber`, a definition declared in [WantedExt/Combinatorics/SimpleGraph/GirthFiveExtremalValuesWanted.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/SimpleGraph/GirthFiveExtremalValuesWanted.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/extremal-graph-theory/extremal-graphs-of-girth-five/index.html#girth-five-extremal-number).

## Girth-five extremal numbers up to twenty vertices

For $n = 1, 2, \dots, 20$ the
girth-five extremal numbers $\mathrm{ex}(n; \{C_3, C_4\})$, the largest numbers of edges of a
simple graph on $n$ vertices that contains no triangle and no four-cycle, are, in order,
$0, 1, 2, 3, 5, 6, 8, 10, 12, 15, 16, 18, 21, 23, 26, 28, 31, 34, 38, 41$.

## Sources

- D. K. Garnick, Y. H. H. Kwong, and F. Lazebnik, *Extremal graphs without three-cycles or four-cycles*, J. Graph Theory 17 (1993), 633–645 (`n ≤ 24`); OEIS A006856; listed in leansolving/SqueezeBench `SqueezeBench/Problems/ExGirthFive/README.md`.

Stated but not proved: `MathlibExt.Combinatorics.SimpleGraph.GirthFiveExtremalValuesWanted.girthFiveExtremalNumber_one_to_twenty` is written with `theorem_wanted` in [WantedExt/Combinatorics/SimpleGraph/GirthFiveExtremalValuesWanted.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/SimpleGraph/GirthFiveExtremalValuesWanted.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/extremal-graph-theory/extremal-graphs-of-girth-five/index.html#girth-five-extremal-number-one-to-twenty).

## Girth-five extremal number on fifty vertices

The girth-five extremal number
$\mathrm{ex}(50; \{C_3, C_4\})$, the largest number of edges of a simple graph on $50$
vertices that contains no triangle and no four-cycle, equals $175$.

For graphs on $n$ vertices of girth at least $5$, the Hoffman–Singleton graph attains the
Moore-type bound $\frac{n}{2} \sqrt{n - 1}$ on the number of edges, with $n = 50$.

## Sources

- A. J. Hoffman and R. R. Singleton, *On Moore graphs with diameters 2 and 3*, IBM J. Res. Develop. 4 (1960), 497–504; OEIS A006856; listed in SqueezeBench `SqueezeBench/Problems/ExGirthFive/README.md`.

Stated but not proved: `MathlibExt.Combinatorics.SimpleGraph.GirthFiveExtremalValuesWanted.girthFiveExtremalNumber_fifty` is written with `theorem_wanted` in [WantedExt/Combinatorics/SimpleGraph/GirthFiveExtremalValuesWanted.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/SimpleGraph/GirthFiveExtremalValuesWanted.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/extremal-graph-theory/extremal-graphs-of-girth-five/index.html#girth-five-extremal-number-fifty).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Extremal graphs of girth five](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/extremal-graph-theory/extremal-graphs-of-girth-five/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/GraphTheory/extremal-graph-theory/extremal-graphs-of-girth-five)
