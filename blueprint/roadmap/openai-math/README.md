# OpenAI Math: a model's research manuscripts and their Lean (OpenAI)

This chapter maps [OpenAI Math](https://github.com/openai/math). Its [README](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/README.md) opens: “This repository contains mathematical manuscripts and supporting proof artifacts produced by an unnamed internal OpenAI model.” It adds: “Some of the unformalized results could have issues.” “In our view, these manuscripts are best understood as a form of raw research data, rather than polished academic papers.”

On how the results were produced: “The vast majority of results were obtained with the same procedure using an unreleased internal OpenAI model.” “Exceptions to this fixed procedure include work on a zero-free region for the Riemann zeta function and proof of the Hodge Conjecture for CM abelian varieties. Additionally, the writeup for the Re(s) > 11/12 zero-free region for the Riemann zeta function was human edited for readability.”

Its [formalization.yaml](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/formalization.yaml) describes the Lean: “Lean formalizations accompanying a mathematics manuscript collection.”

## Facts

From the repository and its formalization.yaml; the review and automation statements are quoted as written.

- Repository: [openai/math](https://github.com/openai/math), read at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae) (2026-10-30).
- Lean toolchain v4.34.1, Mathlib at [d13f23b7](https://github.com/leanprover-community/mathlib4/tree/d13f23b723b8a846827a245b89c10fc7d3f11612).
- License: Apache-2.0.
- Authors: OpenAI.
- Review status: “unchecked”.
- Automation: agent

Its 721 manuscripts form 373 result families, an article each, under the 17 subjects of its overview; 245 with Lean: 547 statements, 521 of them proved in a file this chapter reads.

No Lean is run here. Each statement is quoted from the repository's statement file, which leaves its proof as `sorry` by design; its proof is the declaration of the same name in the solution module the statement's configuration names, in a module that one imports, or in the file formalization.yaml names for it, read from the source text. A statement is proved here when that declaration's value holds no `sorry`, whatever it uses. The articles have no edges.

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
