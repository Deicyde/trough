# Lean Pool

[Lean Pool](https://github.com/LeanPool/lean-pool) keeps Lean projects that are outside Mathlib's scope. As its README describes, each is imported from a permissively licensed repository into a directory of its own, brought to Lean Pool's Lean and Mathlib, and merged once it passes Lean Pool's CI and an LLM review. This chapter maps its 334 projects at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd) (2026-11-08), built with Lean v4.35.0 and Mathlib at [56a00585](https://github.com/leanprover-community/mathlib4/tree/56a005855ea17e0b0958f73ec801ae140b0a1679). Each project has a card, `LeanPool/projects/<slug>.yaml`, with its title, summary, authors, sources, license, provenance, MSC2020 classes and main results, each a Lean declaration with an informal statement. There is a section per top-level MSC2020 class, the class of the first code a card lists (40 sections), and an article per card, titled by the card's title. An article quotes the card's summary, names its authors, links its sources and the project's own repository, gives its provenance and license, and lists its main results.

The cards list 1,341 main results, 509 of them among the cards' main declarations, whose names Lean Pool's CI checks with `#check`. No Lean is run for this chapter: each main result's declaration is looked for in its project's files by reading the source text, following `namespace`, `section` and `end`, and a name counts only when a declaration command names it in full under the namespaces it sits in, in one file of the project. The scan finds 1,331 of the 1,341 declarations, and 508 of the 509 main declarations. A found declaration links its page in Lean Pool's [documentation](https://leanpool.github.io/lean-pool/), which Lean Pool rebuilds daily from its main branch, and its line at the pinned commit; a main result the scan does not find keeps its informal statement and says so. Articles show no Lean signatures and have no dependencies, as edges between declarations need Lean.

A card's provenance says who wrote the project's Lean proofs, in the words of Lean Pool's contributing guide: “human” (“written by people”), “AI” (“mostly produced by an AI system”) or “mix” (“both contributed substantially”). Of the cards, 207 say AI, 73 human and 54 mix.

The quoted text is the cards', in Lean Pool's repository under the Apache-2.0 license, as written, except that a < before a letter, or an & that would start a character reference, which the site cannot show as text, is set in code. Each article names the project's authors and gives the sources its card names: links to a DOI, arXiv, a URL and a paper or manuscript, a citation, the mathematical source, and the card's notes on them. Of the projects, 48 were published under the MIT license, and Lean Pool redistributes them under Apache-2.0; where Lean Pool's notice file keeps a copyright line or a note for one, its article quotes it.

## [MSC2020 classes 03 to 35](part-01/README.md)

- [Mathematical logic and foundations](part-01/03-mathematical-logic-and-foundations/README.md)
- [Combinatorics](part-01/05-combinatorics/README.md)
- [Order, lattices, ordered algebraic structures](part-01/06-order/README.md)
- [Number theory](part-01/11-number-theory/README.md)
- [Field theory and polynomials](part-01/12-field-theory-and-polynomials/README.md)
- [Commutative algebra](part-01/13-commutative-algebra/README.md)
- [Algebraic geometry](part-01/14-algebraic-geometry/README.md)
- [Linear and multilinear algebra; matrix theory](part-01/15-linear-and-multilinear-algebra/README.md)
- [Associative rings and algebras](part-01/16-associative-rings-and-algebras/README.md)
- [Nonassociative rings and algebras](part-01/17-nonassociative-rings-and-algebras/README.md)
- [Category theory; homological algebra](part-01/18-category-theory/README.md)
- [Group theory and generalizations](part-01/20-group-theory-and-generalizations/README.md)
- [Topological groups, Lie groups](part-01/22-topological-groups/README.md)
- [Real functions](part-01/26-real-functions/README.md)
- [Measure and integration](part-01/28-measure-and-integration/README.md)
- [Functions of a complex variable](part-01/30-functions-of-a-complex-variable/README.md)
- [Several complex variables and analytic spaces](part-01/32-several-complex-variables-and-analytic-spaces/README.md)
- [Special functions](part-01/33-special-functions/README.md)
- [Ordinary differential equations](part-01/34-ordinary-differential-equations/README.md)
- [Partial differential equations](part-01/35-partial-differential-equations/README.md)

## [MSC2020 classes 37 to 94](part-02/README.md)

- [Dynamical systems and ergodic theory](part-02/37-dynamical-systems-and-ergodic-theory/README.md)
- [Harmonic analysis on Euclidean spaces](part-02/42-harmonic-analysis-on-euclidean-spaces/README.md)
- [Functional analysis](part-02/46-functional-analysis/README.md)
- [Operator theory](part-02/47-operator-theory/README.md)
- [Calculus of variations and optimal control; optimization](part-02/49-calculus-of-variations-and-optimal-control/README.md)
- [Geometry](part-02/51-geometry/README.md)
- [Convex and discrete geometry](part-02/52-convex-and-discrete-geometry/README.md)
- [Differential geometry](part-02/53-differential-geometry/README.md)
- [Algebraic topology](part-02/55-algebraic-topology/README.md)
- [Manifolds and cell complexes](part-02/57-manifolds-and-cell-complexes/README.md)
- [Global analysis, analysis on manifolds](part-02/58-global-analysis/README.md)
- [Probability theory and stochastic processes](part-02/60-probability-theory-and-stochastic-processes/README.md)
- [Statistics](part-02/62-statistics/README.md)
- [Numerical analysis](part-02/65-numerical-analysis/README.md)
- [Computer science](part-02/68-computer-science/README.md)
- [Mechanics of particles and systems](part-02/70-mechanics-of-particles-and-systems/README.md)
- [Quantum theory](part-02/81-quantum-theory/README.md)
- [Operations research, mathematical programming](part-02/90-operations-research/README.md)
- [Game theory, economics, finance, and other social and behavioral sciences](part-02/91-game-theory/README.md)
- [Information and communication theory, circuits](part-02/94-information-and-communication-theory/README.md)
