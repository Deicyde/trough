---
tracks_lean: false
---

# Trough

Trough maps Lean formalization libraries: what each one formalizes and how its results depend on one another, not what the library may add. Each library gets the article unit that suits it, such as curated concepts for Mathlib, the declarations its roadmaps name for Tau Ceti and blueprint nodes for the research projects. The maps are rendered with [AutoformBot](https://github.com/facebookresearch/autoform-bot).

## Chapters

- [Mathlib](mathlib/README.md): One article per concept on Mathlib's four curated lists (overview, undergraduate, Freek's 100, 1000+) that Mathlib has, linked to its declarations, with edges collapsed from Mathlib's declaration graph.
- [Tau Ceti](tauceti/README.md): One article per declaration a roadmap's status names as a result or notable definition, and per result Tau Ceti's docstrings name, the forms of one result together, as Tau Ceti has it: its docstring, signature and dependencies, in a part per top-level area with a section per roadmap or area of modules.
- [ATLAS](https://github.com/facebookresearch/atlas-lean) (17,683 Lean files): Mapped separately: one article per documented public declaration, at <https://deicyde.github.io/atlas-lean/>.
- [Fermat's Last Theorem (Imperial)](flt/README.md): One article per node of its leanblueprint that is in Lean, with dependencies from its uses; the Verso blueprint (3 chapters) is left for later.
- [PNT+](pnt-plus/README.md): One article per node of its LeanArchitect blueprint that is in Lean, with dependencies from its uses; the Blueprint build workflow builds the blueprint weekly with `lake build :blueprint`.
- [Polynomial Freiman-Ruzsa](pfr/README.md): One article per node of its leanblueprint that is in Lean, with dependencies from its uses.
- [Equational Theories](equational-theories/README.md): One article per node of its leanblueprint that is in Lean, with dependencies from its uses; the equations and implication classes in the project's data files are left for later.
- [Strong PNT (Math Inc)](strongpnt/README.md): One article per node of its leanblueprint that is in Lean, with dependencies from its uses. The project gives no license, so the articles link to its statements rather than quote them.

## Libraries still to map

### Libraries

- [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (1,999 Lean files): One article per problem file (about 2,000), grouped by source; most are stated without a proof.
- [Physlib](https://github.com/leanprover-community/physlib) (1,520 Lean files): One article per documented declaration, grouped by physics area; granularity to be checked against a docstring count.
- [CSLib](https://github.com/leanprover/cslib) (341 Lean files): One article per documented public declaration.
- [Foundation](https://github.com/FormalizedFormalLogic/Foundation) (320 Lean files): One article per documented declaration; the Zoo's inclusion diagrams between logics as edges.
- [Analysis I companion](https://github.com/teorth/analysis) (109 Lean files): One article per textbook section (the Section_X_Y modules).

### Large corpora

- [Fermat's Last Theorem (Anthropic)](https://github.com/anthropics/fermats-last-theorem) (60,478 Lean files): One article per step of PROOF-PATH.md, linked to the Lean theorem it names.
- [OpenAI Math](https://github.com/openai/math) (163,097 Lean files): One article per result family in CONTENTS.md, joined to the 208 formalization.yaml main results.
- [Classification of Finite Simple Groups (Axiom)](https://github.com/AxiomMath/CFSG) (229,089 Lean files): Milestones from the in-Lean CFSG/Blueprint catalog and the formalization.yaml main results.
- [Lean Pool](https://github.com/LeanPool/lean-pool) (28,795 Lean files): One article per project in LeanPool/projects (317), with its main_results as statements.

### Formal Frontier libraries

Formal Frontier, a Mathlib Initiative program, publishes 44 agent-written libraries that fill gaps around Mathlib. Each will be mapped by its headline results: [adic-modules](https://github.com/FormalFrontier/adic-modules), [algebraic-direct-limits](https://github.com/FormalFrontier/algebraic-direct-limits), [algebraic-groups](https://github.com/FormalFrontier/algebraic-groups), [coherent-modules](https://github.com/FormalFrontier/coherent-modules), [complex-analysis](https://github.com/FormalFrontier/complex-analysis), [continuous-group-cohomology](https://github.com/FormalFrontier/continuous-group-cohomology), [dedekind-ideal-arithmetic](https://github.com/FormalFrontier/dedekind-ideal-arithmetic), [finite-etale-algebras](https://github.com/FormalFrontier/finite-etale-algebras), [finite-group-tate-cohomology](https://github.com/FormalFrontier/finite-group-tate-cohomology), [formal-power-series](https://github.com/FormalFrontier/formal-power-series), [fundamental-groupoids](https://github.com/FormalFrontier/fundamental-groupoids), [general-linear-groups](https://github.com/FormalFrontier/general-linear-groups), [graded-rings](https://github.com/FormalFrontier/graded-rings), [group-rings](https://github.com/FormalFrontier/group-rings), [group-theory](https://github.com/FormalFrontier/group-theory), [homological-algebra](https://github.com/FormalFrontier/homological-algebra), [ideal-completion](https://github.com/FormalFrontier/ideal-completion), [integral-closure](https://github.com/FormalFrontier/integral-closure), [iwasawa-modules](https://github.com/FormalFrontier/iwasawa-modules), [metrization](https://github.com/FormalFrontier/metrization), [minimal-primes](https://github.com/FormalFrontier/minimal-primes), [morphism-properties](https://github.com/FormalFrontier/morphism-properties), [multivariate-polynomials](https://github.com/FormalFrontier/multivariate-polynomials), [norm-forms](https://github.com/FormalFrontier/norm-forms), [polynomial-root-stability](https://github.com/FormalFrontier/polynomial-root-stability), [profinite-groups](https://github.com/FormalFrontier/profinite-groups), [projective-modules](https://github.com/FormalFrontier/projective-modules), [projective-space](https://github.com/FormalFrontier/projective-space), [quadratic-algebras](https://github.com/FormalFrontier/quadratic-algebras), [restricted-product-duality](https://github.com/FormalFrontier/restricted-product-duality), [ringed-spaces](https://github.com/FormalFrontier/ringed-spaces), [scheme-properties](https://github.com/FormalFrontier/scheme-properties), [sequence-growth](https://github.com/FormalFrontier/sequence-growth), [sheaf-cohomology](https://github.com/FormalFrontier/sheaf-cohomology), [simplicial-objects](https://github.com/FormalFrontier/simplicial-objects), [simplicial-rings](https://github.com/FormalFrontier/simplicial-rings), [smooth-regularity](https://github.com/FormalFrontier/smooth-regularity), [spectral-stone-duality](https://github.com/FormalFrontier/spectral-stone-duality), [sphere-topology](https://github.com/FormalFrontier/sphere-topology), [stable-range](https://github.com/FormalFrontier/stable-range), [supernatural-numbers](https://github.com/FormalFrontier/supernatural-numbers), [toric-ideals](https://github.com/FormalFrontier/toric-ideals), [valuation-integers](https://github.com/FormalFrontier/valuation-integers), [vector-bundles](https://github.com/FormalFrontier/vector-bundles).
