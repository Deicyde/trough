---
declaration: definition
origin: cited
lean: Extractor.Rewinding
statement: formalized
---

# Rewinding Extractor

A **rewinding extractor** consists of:

- An extractor state type
- Simulation oracles for challenges and oracle queries for the prover
- A function that runs the extractor with the prover's oracle interface, allowing for calling the prover multiple times

This allows the extractor to rewind the prover to earlier states and try different challenges. Only the interface is defined; no knowledge-soundness notion uses it yet.

## Depends on

- [Type Signature of a Prover](../part-01/def-prover.md)
- [Oracle Interface](../part-01/def-oracle-interface.md)

## Lean

Formalized as [`Extractor.Rewinding`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/Extractor.Rewinding).

## Sources

- [ArkLib blueprint: oracle_reductions/defs.tex, line 531](https://github.com/Verified-zkEVM/ArkLib/blob/e9bcc82d3d33a1814822b9b9e6b135bc80d614ee/blueprint/src/oracle_reductions/defs.tex#L531)
