# OpenAI Math: a model's research manuscripts and their Lean (OpenAI)

[OpenAI Math](https://github.com/openai/math) is a collection of mathematical manuscripts written by an OpenAI model, which its README calls raw research data rather than polished papers, with Lean formalizations of some of their results. This chapter maps it at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae) (2026-10-30).

Its 721 manuscripts form 373 result families, an article each, under the 17 subjects of its overview; 245 with Lean: 561 statements, 528 of them proved in a file this chapter reads.

No Lean is run here. Each statement is quoted from the repository's statement file, which leaves its proof as `sorry` by design; its proof is the declaration of the same name in the solution module the statement's configuration names, or in a module that one imports, read from the source text. A statement is proved here when that declaration's value holds no `sorry`, whatever it uses. The families have no recorded dependencies.

The descriptions, titles, abstracts, Lean pages and statements are quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae), under its Apache-2.0 license.

- [Number theory](number-theory/README.md)
- [Algebraic and complex geometry](algebraic-and-complex-geometry/README.md)
- [Real and complex analysis](real-and-complex-analysis/README.md)
- [Convex and metric geometry](convex-and-metric-geometry/README.md)
- [Theoretical computer science](theoretical-computer-science/README.md)
- [Dynamical systems and ergodic theory](dynamical-systems-and-ergodic-theory/README.md)
- [Combinatorics](combinatorics/README.md)
- [Algebra](algebra/README.md)
- [Probability and statistical mechanics](probability-and-statistical-mechanics/README.md)
- [Mathematical logic](mathematical-logic/README.md)
- [Group theory](group-theory/README.md)
- [Mathematical physics](mathematical-physics/README.md)
- [Operator algebras](operator-algebras/README.md)
- [Topology](topology/README.md)
- [Functional analysis](functional-analysis/README.md)
- [Differential geometry](differential-geometry/README.md)
- [Partial differential equations](partial-differential-equations/README.md)
