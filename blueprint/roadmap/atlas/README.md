# ATLAS: textbook mathematics in Lean (Meta)

[ATLAS](https://github.com/facebookresearch/atlas-lean), the Autoformalized Textbook Library At Scale from Meta, is a Lean library of textbook mathematics formalized with LLMs, generated with [AutoformBot](https://github.com/facebookresearch/autoform-bot). Its vault, the roadmap the ATLAS site publishes, is kept on the `wiki/autoform-blueprint` branch of [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean); this chapter maps it as read at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d) (2026-11-11), Lean toolchain v4.35.0, Mathlib v4.35.0.

The vault files its results by area, subject and topic. There are 45,879 results in 3,605 topics, an article each, under 27 subjects in 6 areas, with a page for each subject and each branch between a subject and its topics. Each result is an informal statement, and the vault's link annotations give the Lean declaration that formalizes it. Of the results, 37,870 proved, 3 with `sorry` in their value, 7,998 stated but not proved and 8 without a declaration.

No Lean is run for this chapter. A declaration is found where the repository's Lean declares it, read from the source text of 13,276 files under `MathlibExt/`, `CSLibExt/`, `PhyslibExt/`, `WantedExt/` and `Atlas/`, under the namespaces it sits in; its line is the line its keyword is on. A result is proved when its declaration's value holds no `sorry`; `theorem_wanted`, `def_wanted` and `proof_wanted` state a result whose proof is deferred, which the blocks call stated but not proved. The articles have no dependencies: the vault records no edges between its results.

The archived first release, under `v1/`, is under a non-commercial license that also forbids use for training models, so it is not read. The ATLAS site, https://deicyde.github.io/atlas-lean/, publishes the vault, a card per result; each block links its card there.

The statements, titles and prose are quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d), under its Apache-2.0 license (its LICENSE file adds that the code is not meant for training models). Each result's line is linked.

- [Foundations & Logic](foundations-logic/README.md)
- [Algebra & Number Theory](algebra-number-theory/README.md)
- [Geometry & Topology](geometry-topology/README.md)
- [Analysis & Probability](analysis-probability/README.md)
- [Discrete Mathematics & Computer Science](discrete-mathematics-computer-science/README.md)
- [Applied Mathematics](applied-mathematics/README.md)
