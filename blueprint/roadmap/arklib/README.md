# ArkLib

[Verified-zkEVM/ArkLib](https://github.com/Verified-zkEVM/ArkLib) says in its README:

> ArkLib is a Lean 4 library for formally verifying **succinct non-interactive arguments of knowledge** (SNARKs).

Its blueprint, read at commit [e9bcc82d](https://github.com/Verified-zkEVM/ArkLib/tree/e9bcc82d3d33a1814822b9b9e6b135bc80d614ee) (2026-11-23): one article for each of its 263 nodes whose Lean declarations it names and marks formalized, or in Mathlib. Its other 19 nodes have no article, and a section of only those is left out: the map records what the project contains, not what it plans. A statement for which the blueprint marks no proof `\leanok` says so. Dependencies are the blueprint's `\uses`: a statement's under *Depends on*, a proof's under *Proof depends on*.

The text is the blueprint's, under its Apache-2.0 license: each page has a section's prose, remarks and examples in the blueprint's order, with each node's statement and proof where the node stands.

- [Introduction](introduction/README.md)
- [Oracle Reductions](oracle-reductions/README.md)
- [Proof Systems](proof-systems/README.md)
- [Commitment Schemes](commitment-schemes/README.md)
- [Supporting Theories](supporting-theories/README.md)
- [References](references/README.md)
