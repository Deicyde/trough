# Analysis I and An introduction to measure theory

[teorth/analysis](https://github.com/teorth/analysis) is Terence Tao's Lean companion to his textbook [*Analysis I*](https://terrytao.wordpress.com/books/analysis-i/), with a companion to his book [*An introduction to measure theory*](https://terrytao.wordpress.com/books/an-introduction-to-measure-theory/) in `Analysis/MeasureTheory/`. Its README says:

> The files in this directory contain a formalization of my text [_Analysis I_](https://terrytao.wordpress.com/books/analysis-i/) into [Lean](https://lean-lang.org/). The formalization is intended to be as faithful a paraphrasing as possible to the original text, while also showcasing Lean's features and syntax.  In particular, the formalization is _not_ optimized for efficiency, and in some cases may deviate from idiomatic Lean usage.
>
> Portions of the text that were left as exercises to the reader are rendered in this translation as `sorry`s.  Readers are welcome to fork the repository here to try their hand at these exercises, but I do not intend to place solutions in this repository directly.

and the README of its measure theory companion:

> The files in this directory contain a formalization of my text [_An introduction to measure theory_](https://terrytao.wordpress.com/books/an-introduction-to-measure-theory/) into [Lean](https://lean-lang.org/). The formalization is intended to be as faithful a paraphrasing as possible to the original text, while also showcasing Lean's features and syntax.  In particular, the formalization is _not_ optimized for efficiency, and in some cases may deviate from idiomatic Lean usage.
>
> Portions of the text that were left as exercises to the reader, as well as many of the proofs in the text are rendered in this translation as `sorry`s.  Readers who are not in my classes are also welcome to submit such proofs.

So the exercises are left as `sorry` by design, as the first README says.

## Facts

- Repository: [teorth/analysis](https://github.com/teorth/analysis), read at commit [a19a5bfa](https://github.com/teorth/analysis/tree/a19a5bfadc616467562995b75f46035232841943) (2026-10-17), the newest commit on its main branch whose “Build book” run passed.
- Lean toolchain v4.29.0-rc8, Mathlib at [698d2b68](https://github.com/leanprover-community/mathlib4/tree/698d2b68b870f1712040ab0c233d34372d4b56df).
- License: Apache-2.0.
- Written by Terence Tao, with the repository's [contributors](https://github.com/teorth/analysis/graphs/contributors).
- Its site, https://teorth.github.io/analysis/, has a Verso page for each section of Analysis I and doc-gen4 documentation for every module; each article links its section's pages.

## This map

This chapter has an article for each of the 92 section modules at that commit: 74 of [Analysis I](analysis-i/README.md) (61 sections, 4 chapter epilogues and 9 appendix sections), on a page per chapter, and 18 of [An introduction to measure theory](measure-theory/README.md) (its Notation module and 17 sections), on a page per section of its Chapter 1. An article quotes its section's module docstring, then has a block for each label of the book that a docstring in the file starts with (“Definition 6.1.3”, “Exercise 6.1.2”), in file order: the declarations carrying that label, each with its docstring, its Lean statement, its line in the source and its status. Several declarations can carry one label, and an `example`, which has no name, counts as a declaration. Declarations whose docstring starts with no label are counted in each article but not shown. [Other modules](other-modules/README.md) lists the 15 modules that belong to neither book.

There are 1,232 labelled items, carried by 1,571 declarations. In Analysis I, 972 items carried by 1,236 declarations: 290 proved here, 758 stated without proof (555 of them exercises) and 188 definitions (50 with a value left as `sorry`). In An introduction to measure theory, 260 items carried by 335 declarations: 90 proved here, 174 stated without proof (161 of them exercises) and 71 definitions (24 with a value left as `sorry`).

No Lean is run for this chapter. Statuses are read from the source text: a declaration's Lean statement is its text up to the `:=` or `where` that starts its value, and its status reads that value.

- “Proved here.”: a theorem, lemma or example whose proof, its text from that `:=` on, holds no `sorry`. This says nothing of the results the proof uses, which may themselves be stated without proof.
- “Stated without proof.”: a theorem, lemma or example whose proof holds `sorry`; “An exercise, stated without proof.” when its label names an exercise.
- “A definition.”: any other declaration (a `def`, `abbrev`, `structure`, `class`, `inductive` or `instance`) whose value holds no `sorry`; “A definition whose value is left as `sorry`.” when it does.

A label is the kind and number a docstring starts with, after any Verso `{given}` role. A `private` declaration is not read, as Lean renames it, and neither is a notation; 2 labelled docstrings are on such a declaration, as their articles say.

The docstrings are written in Verso's markup. The pages show a role such as `` {name}`x` `` as the code `x`, leave out the variables a `{given -show}` role names, as Verso's own pages do, and show Verso's formulas, `` $`x` ``, in TeX. The words are the repository's.

An edge from one section to another means that the first section's Lean file imports the other's: 106 imports between sections in all. It says nothing of which results use which. Each article lists them as what it depends on, shown on the site as “Statement uses”; its imports of Mathlib and of modules outside both books are not shown. No import points forward in its book's order.

The titles, module docstrings, docstrings, Lean statements and README text are quoted from [teorth/analysis](https://github.com/teorth/analysis) at commit [a19a5bfa](https://github.com/teorth/analysis/tree/a19a5bfadc616467562995b75f46035232841943), under its Apache-2.0 license; the books themselves are not quoted.

- [Analysis I](analysis-i/README.md)
- [An introduction to measure theory](measure-theory/README.md)
- [Other modules](other-modules/README.md)
