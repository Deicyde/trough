---
tracks_lean: false
---

# Trough

Trough maps Lean formalization libraries: what each one formalizes and how its results depend on one another, not what the library may add. Each library gets the article unit that suits it, such as curated concepts for Mathlib, the declarations its roadmaps name for Tau Ceti, blueprint nodes for the research projects and headline results for Formal Frontier. The maps are rendered with [AutoformBot](https://github.com/facebookresearch/autoform-bot).

## Chapters

- [Mathlib](mathlib/README.md): One article per concept on Mathlib's four curated lists (overview, undergraduate, Freek's 100, 1000+) that Mathlib has, linked to its declarations, with edges collapsed from Mathlib's declaration graph.
- [Tau Ceti](tauceti/README.md): One article per declaration a roadmap's status names as a result or notable definition, as Tau Ceti has it: its docstring, signature and dependencies, in a section per roadmap.
- [ATLAS](https://github.com/facebookresearch/atlas-lean) (17,683 Lean files): Mapped separately: one article per documented public declaration, at <https://deicyde.github.io/atlas-lean/>.
- [Fermat's Last Theorem (Imperial)](flt/README.md): One article per node of its leanblueprint that is in Lean, with dependencies from its uses; the Verso blueprint (3 chapters) is left for later.
- [PNT+](pnt-plus/README.md): One article per node of its LeanArchitect blueprint that is in Lean, with dependencies from its uses; the Blueprint build workflow builds the blueprint weekly with `lake build :blueprint`.
- [Polynomial Freiman-Ruzsa](pfr/README.md): One article per node of its leanblueprint that is in Lean, with dependencies from its uses.
- [Equational Theories](equational-theories/README.md): One article per node of its leanblueprint that is in Lean, with dependencies from its uses; the equations and implication classes in the project's data files are left for later.
- [Strong PNT (Math Inc)](strongpnt/README.md): One article per node of its leanblueprint that is in Lean, with dependencies from its uses. The project gives no license, so the articles link to its statements rather than quote them.
- [Formal Frontier](formal-frontier/README.md): 44 libraries, a part per subject. One article per highlight in a library's formalization.yaml whose declarations the scan finds, and per headline result in its README whose declaration link names a declaration the scan finds in the linked file; the main results its formalization.yaml lists are on a page of their own.

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
