---
declaration: theorem
origin: cited
lean: NumberField.AdeleRing.DivisionAlgebra.compact_quotient
statement: formalized
proof: formalized
---

# NumberField.AdeleRing.DivisionAlgebra.compact_quotient

If $D$ is a division algebra then the quotient $D^\times\backslash D_{\mathbb{A}}^{(1)}$ with its quotient topology coming from $D_{\mathbb{A}}^{(1)}$, is compact.

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [MeasureTheory.ringHaarChar_continuous](../../miniproject-haar-characters/initial-definitions/measuretheory-ringhaarchar-continuous.md)
- [NumberField.AdeleRing.DivisionAlgebra.Aux.antidiag_mem_C](../the-proof/numberfield-adelering-divisionalgebra-aux-antidi.md)
- [NumberField.AdeleRing.DivisionAlgebra.Aux.C_compact](../the-proof/numberfield-adelering-divisionalgebra-aux-c-comp.md)

## Proof

Indeed, if $M$ is the preimage of $C$ under the inclusion $D_{\mathbb{A}}^{(1)} \to D_{\mathbb{A}}\times D_{\mathbb{A}}$ sending $\nu$ to $(\nu,\nu^{-1})$, then $M$ is a closed subspace of a compact space so it's compact (note that $\delta_{D_{\mathbb{A}}}$ is continuous, by theorem [MeasureTheory.ringHaarChar_continuous](../../miniproject-haar-characters/initial-definitions/measuretheory-ringhaarchar-continuous.md), so $D_{\mathbb{A}}^{(1)}$ is a closed subset of $D_{\mathbb{A}}^\times$ which is itself a closed subset of $D_{\mathbb{A}}\times D_{\mathbb{A}}$). Lemma [NumberField.AdeleRing.DivisionAlgebra.Aux.antidiag_mem_C](../the-proof/numberfield-adelering-divisionalgebra-aux-antidi.md) shows that $M$ surjects onto $D^\times\backslash D_{\mathbb{A}}^{(1)}$ which is thus also compact.

## Lean

Formalized as [`NumberField.AdeleRing.DivisionAlgebra.compact_quotient`](https://ImperialCollegeLondon.github.io/FLT/docs/find/#doc/NumberField.AdeleRing.DivisionAlgebra.compact_quotient).

## Sources

- [Fermat's Last Theorem (Imperial) blueprint: chapter/FujisakiProject.tex, line 85](https://github.com/ImperialCollegeLondon/FLT/blob/a3210204ad8876e851e32f73dd97d882bf1ccd0a/blueprint/src/chapter/FujisakiProject.tex#L85)
