---
declaration: lemma
origin: cited
lean: Rep.trivialTateCohomology_coind₁, Rep.trivialTateCohomology_coind₁', Rep.trivialTateCohomology_ind₁'
statement: formalized
proof: formalized
---

# induced' trivial Tate

If $M$ is a representation of a finite group $G$ then the representations $\mathrm{ind}_1'(M)$ and $\mathrm{coind}_1'(M)$ have trivial Tate cohomology.

## Depends on

- [induced trivial Tate](../coinduction-and-induction/lem-induced-trivial-tate.md)
- [ind₁' iso ind₁](lem-ind1-iso-ind1.md)
- [coind₁' iso coind₁](lem-coind1-iso-coind1.md)

## Proof

This follows from [induced trivial Tate](../coinduction-and-induction/lem-induced-trivial-tate.md) together with the isomorphisms [ind₁ to coind₁](../coinduction-and-induction/def-ind1-to-coind1.md), [coind₁' iso coind₁](lem-coind1-iso-coind1.md) and [ind₁' iso ind₁](lem-ind1-iso-ind1.md).

## Lean

Formalized as [`Rep.trivialTateCohomology_coind₁`](https://kbuzzard.github.io/ClassFieldTheory/docs/find/#doc/Rep.trivialTateCohomology_coind₁), [`Rep.trivialTateCohomology_coind₁'`](https://kbuzzard.github.io/ClassFieldTheory/docs/find/#doc/Rep.trivialTateCohomology_coind₁'), [`Rep.trivialTateCohomology_ind₁'`](https://kbuzzard.github.io/ClassFieldTheory/docs/find/#doc/Rep.trivialTateCohomology_ind₁').

## Sources

- [Class field theory blueprint: _2_cohomology.tex, line 1189](https://github.com/kbuzzard/ClassFieldTheory/blob/629ae9ed781748980bb51ab6f5f338ad9d6db3e8/blueprint/src/_2_cohomology.tex#L1189)
