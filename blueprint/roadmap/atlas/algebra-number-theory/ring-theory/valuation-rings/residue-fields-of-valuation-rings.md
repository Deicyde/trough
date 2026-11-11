---
declaration: section
origin: cited
lean: ValuationSubring.exists_root_mem_of_monic, ValuationSubring.isAlgClosed_residueField, ValuationSubring.algebra_isAlgebraic_zmod_residueField_of_isAlgebraic_rat, ValuationSubring.residue_injOn_pow_eq_one_and_exists_residue_eq_of_isAlgClosed
statement: formalized
proof: formalized
---

# Residue fields of valuation rings

4 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/valuation-rings/residue-fields-of-valuation-rings/index.html).

## Monic polynomials have roots in valuation subrings of closed fields

A monic polynomial over a valuation subring of an algebraically closed
field, of nonzero degree, has a root in the subring: take a root in the field,
it is integral over the subring, and valuation subrings are integrally closed.

Formalized by `ValuationSubring.exists_root_mem_of_monic`, a theorem declared in [MathlibExt/RingTheory/Valuation/ResidueField.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/Valuation/ResidueField.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/valuation-rings/residue-fields-of-valuation-rings/index.html#exists-root-mem-of-monic).

## Residue field of a valuation subring of a closed field is closed

The residue field of a valuation subring of an algebraically closed field
is algebraically closed: lift a monic irreducible polynomial to the valuation
subring, take a root there, and reduce it back.

Formalized by `ValuationSubring.isAlgClosed_residueField`, a theorem declared in [MathlibExt/RingTheory/Valuation/ResidueField.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/Valuation/ResidueField.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/valuation-rings/residue-fields-of-valuation-rings/index.html#is-alg-closed-residue-field).

## Residue fields in algebraic extensions of $\mathbb{Q}$ are algebraic

The residue field of a valuation subring of an algebraic extension of
`ℚ` is algebraic over `𝔽_p`.

Formalized by `ValuationSubring.algebra_isAlgebraic_zmod_residueField_of_isAlgebraic_rat`, a theorem declared in [MathlibExt/RingTheory/Valuation/ResidueFieldRoots.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/Valuation/ResidueFieldRoots.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/valuation-rings/residue-fields-of-valuation-rings/index.html#algebra-is-algebraic-zmod-residue-field).

## Roots of unity under the residue map of a valuation subring

The residue map is injective on `m`-th roots of unity, and every `m`-th
root of unity in the residue field lifts, when `m` is nonzero in the
residue field.

Formalized by `ValuationSubring.residue_injOn_pow_eq_one_and_exists_residue_eq_of_isAlgClosed`, a theorem declared in [MathlibExt/RingTheory/Valuation/ResidueFieldRoots.lean, line 139](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/Valuation/ResidueFieldRoots.lean#L139). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/valuation-rings/residue-fields-of-valuation-rings/index.html#residue-inj-on-pow-eq-one-and-exists-res).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Residue fields of valuation rings](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/valuation-rings/residue-fields-of-valuation-rings/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/RingTheory/valuation-rings/residue-fields-of-valuation-rings)
