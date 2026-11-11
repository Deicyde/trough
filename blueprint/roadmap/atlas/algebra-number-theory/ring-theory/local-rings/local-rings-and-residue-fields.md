---
declaration: section
origin: cited
lean: IsLocalRing.charP_residueField_of_natCast_mem_maximalIdeal, IsLocalRing.quotient_of_ne_top
statement: formalized
proof: formalized
---

# Local rings and residue fields

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/local-rings/local-rings-and-residue-fields/index.html).

## Characteristic of the residue field of a local ring

If `(p : A)` lies in the maximal ideal of a local ring `A`, the residue
field has characteristic `p`: `p` maps to zero in the residue field.

Formalized by `IsLocalRing.charP_residueField_of_natCast_mem_maximalIdeal`, a theorem declared in [MathlibExt/RingTheory/LocalRing/CharP.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/LocalRing/CharP.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/local-rings/local-rings-and-residue-fields/index.html#char-p-residue-field-of-nat-cast-mem-max).

## Quotient of a local ring by a proper ideal is local

A quotient of a local ring by a proper ideal is local. Mathlib uses this
fact inline (via `IsLocalRing.of_surjective'`), but does not package it as a
standalone lemma.

Formalized by `IsLocalRing.quotient_of_ne_top`, a theorem declared in [MathlibExt/RingTheory/LocalRing/Quotient.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/LocalRing/Quotient.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/local-rings/local-rings-and-residue-fields/index.html#quotient-of-ne-top).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Local rings and residue fields](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/local-rings/local-rings-and-residue-fields/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/RingTheory/local-rings/local-rings-and-residue-fields)
