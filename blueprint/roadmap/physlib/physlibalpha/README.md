# PhyslibAlpha

[PhyslibAlpha/](https://github.com/leanprover-community/physlib/tree/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha), downstream of Physlib in the same repository. Its README describes it:

> PhyslibAlpha exists for the rapid development of physics digitalizations, enabled by a lighter review process built to handle large-scale, human- or AI-generated contributions.

and gives its review in a section of its own:

> PhyslibAlpha sits downstream of `./Physlib` (within the same repository). The core idea is that PhyslibAlpha has lower review-standards than Physlib making it easier to contribute large PRs, AI-generated content, or formalizations which are not-quite-perfect. PRs for PhyslibAlpha must pass basic linter checks, described [here](https://github.com/leanprover-community/physlib/blob/master/scripts/lint/required/alpha/README.md). PRs must also undergo a light 'one-look' review checking 1) Whether the content is main-stream physics, 2) Whether it looks reasonable (no axioms, easy to read etc.), 3) Whether it is within the right place within PhyslibAlpha (mirroring its place in Physlib).
>
> Because of the lower-review bar for PhyslibAlpha we cannot promise to maintain contributions when they break — we will simply record when this happens.

Its 827 modules with a declaration are mapped here, an article each, on a page per area and per folder below it.

The docstrings, Lean statements and API maps are quoted from [leanprover-community/physlib](https://github.com/leanprover-community/physlib) at commit [2a1dfe43](https://github.com/leanprover-community/physlib/tree/2a1dfe43134b49b643642f13d33031754021bb5d), under its Apache-2.0 license.

- [ClassicalFieldTheory](classicalfieldtheory/README.md)
- [ClassicalMechanics](classicalmechanics/README.md)
- [CondensedMatter](condensedmatter/README.md)
- [Electromagnetism](electromagnetism/README.md)
- [Mathematics](mathematics/README.md)
- [Particles](particles/README.md)
- [ProbabilisticTheory](probabilistictheory/README.md)
- [QuantumMechanics](quantummechanics/README.md)
- [Relativity](relativity/README.md)
- [SpaceAndTime](spaceandtime/README.md)
