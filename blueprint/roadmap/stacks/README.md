# The Stacks Project in Lean (Axiom)

[The Stacks Project in Lean](https://github.com/AxiomMath/Stacks), from Axiom Math, formalizes [the Stacks Project](https://stacks.math.columbia.edu) in Lean on top of Mathlib, indexed by Stacks tag, with a site at https://stacks.axiommath.ai/. This chapter maps it as read at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7) (2026-11-06), Lean toolchain v4.35.0, Mathlib v4.35.0. The repository runs no continuous integration, so the commit is the newest of its main branch, not one a build is known to pass.

Its formalization.yaml describes it: “`Stacks` is a Lean 4 formalization, on top of Mathlib, of statements and proofs of The Stacks Project, indexed by Stacks tag. `StacksCore` is the human-reviewed library; `StacksFrontier` holds drafted formalizations that build and are axiom-clean but are not yet reviewed. The formalization was generated collaboratively between human formalisers at Axiom Math and AxiomProver, their in-house theorem proving system. …” Its README: “`import Stacks` brings in both tiers. Every proof in either tier is kernel-checked; the tiers differ in who has reviewed the code.” It describes StacksCore as “human-reviewed formalizations, checked against the Stacks Project and brought to Mathlib standards of naming, generality and style.” and StacksFrontier as “formalizations written by AI agents.”

## Facts

From the repository and its formalization.yaml; the review and automation statements are quoted as written.

- Repository: [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks), read at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7) (2026-11-06).
- Lean toolchain v4.35.0, Mathlib at [56a00585](https://github.com/leanprover-community/mathlib4/tree/56a005855ea17e0b0958f73ec801ae140b0a1679).
- License: Apache-2.0.
- Authors: Kenny Lau, Brian Nugent, Ashvin A. Swaminathan, Yunzhou Xie.
- Maintainers: Ashvin A. Swaminathan, Kenny Lau, Brian Nugent, Yunzhou Xie.
- Review status: “self-assessed”.
- Review notes: “StacksCore is human-reviewed. StacksFrontier builds with no sorry and only the standard axioms, and each statement was checked against its Stacks tag, but it has not yet had human review. The development took place in a repository internal to Axiom Math.”
- Reviewers: “Kenny Lau”, “Brian Nugent”, “Yunzhou Xie”.
- Automation: autonomous; models “AxiomProver”
- Automation: manual
- Automation notes: “Foundational definitions and the StacksCore library formalised and reviewed by hand; most of StacksFrontier formalised autonomously”

There are 2,898 articles, one for each section of the Stacks Project with a tag that a declaration carries, in 109 chapters and 9 parts as the Stacks Project orders them. They hold 16,441 tags. A tag's block lists the declarations of the repository that carry it, 38,763 entries in all (463 in StacksCore, 38,300 in StacksFrontier): a declaration carrying several tags is in each tag's block, so these are 38,378 declarations (451 and 37,927). The blocks also list the 3,601 declarations registered for their tags with `add_to_stacks` or an `attribute` command, 1,050 of them declared in the repository itself, whose entries link their lines. The README describes `add_to_stacks` as registering a tag that Mathlib already covers on the Mathlib declaration, and the other registered declarations link to Mathlib's documentation. The repository has 445 Lean files in StacksCore and 62,527 in StacksFrontier.

No Lean is run for this chapter. Tags are read from the source text, as the attributes are written: a declaration carries a tag when the `@[...]` list right before it has `stacks TAG` or `stacks_fixed TAG`, or an `attribute [stacks TAG]` command names it; `add_to_stacks TAG name` registers a declaration by name, which the block links to its line when the repository declares that name and to Mathlib's documentation otherwise. A declaration's name is read under the namespaces it sits in; an instance with no name is shown without one, and a `private` declaration under the name it is written with. Its Lean statement runs to the `:=` or `where` that starts its value, and its line is the line its keyword is on. No declaration's value read here contains `sorry`, as the README says. The articles have no dependencies: edges between declarations need Lean.

The parts, chapters and sections, their numbers and titles, are the Stacks Project's, read from [its repository](https://github.com/stacks/stacks-project) at commit [a04446e5](https://github.com/stacks/stacks-project/tree/a04446e57ec1fbc252a871afcec7752fb2807b14), and each tag is placed in the section its label is in there. The Stacks Project is under the GNU Free Documentation License, so its text is not quoted: each block links its tag's page at stacks.math.columbia.edu. The repository's site, https://stacks.axiommath.ai/, links each tag to its Lean code, but its tag pages answer as missing pages when fetched, so the blocks do not link them.

Declarations also carry the items of EGA and SGA they prove, which the blocks note with the attribute's comment as written; two indexes list them, [EGA](ega/README.md) (1,868 items) and [SGA](sga/README.md) (1,968 items), of the 2,743 and 3,327 the repository carries.

The docstrings and Lean statements are quoted from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7), under its Apache-2.0 license. Each declaration's line is linked.

- [Preliminaries](preliminaries/README.md)
- [Schemes](schemes/README.md)
- [Topics in Scheme Theory](topics-in-scheme-theory/README.md)
- [Algebraic Spaces](algebraic-spaces/README.md)
- [Topics in Geometry](topics-in-geometry/README.md)
- [Deformation Theory](deformation-theory/README.md)
- [Algebraic Stacks](algebraic-stacks/README.md)
- [Topics in Moduli Theory](topics-in-moduli-theory/README.md)
- [Miscellany](miscellany/README.md)
- [EGA](ega/README.md)
- [SGA](sga/README.md)

Tags that the Stacks Project does not list at commit [a04446e5](https://github.com/stacks/stacks-project/tree/a04446e57ec1fbc252a871afcec7752fb2807b14), so with no article: 082O, carried by `AlgebraicGeometry.Space.quotientRestrictCokernelIso` (registered).
