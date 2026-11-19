---
declaration: definition
origin: cited
lean: Witness.InvLens, Extractor.Lens
statement: formalized
---

# Extractor Lens

An extractor runs from output witnesses back to input witnesses, so lifting an extractor needs a witness lens in the reverse direction. An *inverse witness lens* consists of:

- a projection $\mathsf{StmtIn}_{\mathsf{outer}} \times \mathsf{WitOut}_{\mathsf{outer}} \to \mathsf{WitOut}_{\mathsf{inner}}$ of output witnesses;
- a lifting $\mathsf{StmtIn}_{\mathsf{outer}} \times \mathsf{WitOut}_{\mathsf{outer}} \to \mathsf{WitIn}_{\mathsf{inner}} \to \mathsf{WitIn}_{\mathsf{outer}}$ of extracted input witnesses.

An extractor lens pairs a statement lens with an inverse witness lens.

## Depends on

- [Statement Lens](../part-01/def-statement-lens.md)

## Lean

Formalized as [`Witness.InvLens`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/Witness.InvLens), [`Extractor.Lens`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/Extractor.Lens).

## Sources

- [ArkLib blueprint: oracle_reductions/composition.tex, line 308](https://github.com/Verified-zkEVM/ArkLib/blob/e1c185ba001d225d1f3ea84071d67a8c6c56d6a0/blueprint/src/oracle_reductions/composition.tex#L308)
