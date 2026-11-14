# Consistency of New Foundations

The blueprint of Consistency of New Foundations, read at commit [edbce7eb](https://github.com/leanprover-community/con-nf/tree/edbce7eb98351870f553cfab6ccb7cab327e4259) (2026-10-23): one article for each of its 59 nodes whose Lean declarations it names and marks formalized, or in Mathlib. Its other 100 nodes have no article, and a section of only those is left out: the map records what the project contains, not what it plans. A statement for which the blueprint marks no proof `\leanok` says so. Dependencies are the blueprint's `\uses`: a statement's under *Depends on*, a proof's under *Proof depends on*.

The text is the blueprint's, under its Apache-2.0 license: each page has a section's prose, remarks and examples in the blueprint's order, with each node's statement and proof where the node stands.

We give a self-contained account of a version of the proof of Holmes and Wilshaw ([Holmes and Wilshaw 2024](https://arxiv.org/abs/1503.01406)) that Quine's set theory *New Foundations* ([Quine 1937](https://api.semanticscholar.org/CorpusID:123927264)) is consistent relative to the metatheory ZFC. This version of the proof is written in a style that is particularly amenable to the formalisation in Lean (leanprover-community-con-nf); to that end, type-theoretic concerns and dependencies between parts of the proof are explicitly spelled out.

- [Introduction](introduction/README.md)
- [Setting up the environment](setting-up-the-environment/README.md)
- [Freedom of action](freedom-of-action/README.md)
- [The counting argument](the-counting-argument/README.md)
- [Auxiliary results](auxiliary-results/README.md)
