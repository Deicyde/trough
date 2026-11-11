---
declaration: section
origin: cited
lean: Polynomial.exists_monic_irreducible_zmod_two, BitVec.passesInverseTest, BitVec.passesInverseTest_iff_irreducible, BitVec.findIrreducibleModulus, BitVec.findIrreducibleModulus_spec, BitVec.findIrreducibleModulus_minimal
statement: formalized
proof: formalized
---

# Searching for irreducible polynomials over GF(2)

6 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/FieldTheory/finite-fields/searching-for-irreducible-polynomials-over-gf-2/index.html).

## Polynomial

## Monic irreducible binary polynomials exist in every degree

Over `ZMod 2`, there is a monic irreducible polynomial of every positive degree.

Formalized by `Polynomial.exists_monic_irreducible_zmod_two`, a theorem declared in [MathlibExt/FieldTheory/Finite/BinaryModulusSearch.lean, line 31](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/FieldTheory/Finite/BinaryModulusSearch.lean#L31). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/FieldTheory/finite-fields/searching-for-irreducible-polynomials-over-gf-2/index.html#exists-monic-irreducible-zmod-two).

## Exhaustive inverse test for a binary polynomial modulus

Test exhaustively whether every nonzero word has a multiplicative inverse modulo
`g.monicModulus`.

Formalized by `BitVec.passesInverseTest`, a definition declared in [MathlibExt/FieldTheory/Finite/BinaryModulusSearch.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/FieldTheory/Finite/BinaryModulusSearch.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/FieldTheory/finite-fields/searching-for-irreducible-polynomials-over-gf-2/index.html#passes-inverse-test).

## Inverse test succeeds exactly for irreducible moduli

At positive width, the exhaustive inverse test succeeds exactly for irreducible monic
moduli.

Formalized by `BitVec.passesInverseTest_iff_irreducible`, a theorem declared in [MathlibExt/FieldTheory/Finite/BinaryModulusSearch.lean, line 98](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/FieldTheory/Finite/BinaryModulusSearch.lean#L98). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/FieldTheory/finite-fields/searching-for-irreducible-polynomials-over-gf-2/index.html#passes-inverse-test-iff-irreducible).

## Exhaustive search for an irreducible binary modulus

Search the lower coefficient words in ascending order for the first word passing the
exhaustive inverse test. Width zero is deliberately reported as failure.

Formalized by `BitVec.findIrreducibleModulus`, a definition declared in [MathlibExt/FieldTheory/Finite/BinaryModulusSearch.lean, line 182](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/FieldTheory/Finite/BinaryModulusSearch.lean#L182). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/FieldTheory/finite-fields/searching-for-irreducible-polynomials-over-gf-2/index.html#find-irreducible-modulus).

## Exhaustive search returns an irreducible binary modulus

At every positive width, exhaustive search returns an irreducible binary modulus.

Formalized by `BitVec.findIrreducibleModulus_spec`, a theorem declared in [MathlibExt/FieldTheory/Finite/BinaryModulusSearch.lean, line 189](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/FieldTheory/Finite/BinaryModulusSearch.lean#L189). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/FieldTheory/finite-fields/searching-for-irreducible-polynomials-over-gf-2/index.html#find-irreducible-modulus-spec).

## Minimality of the binary modulus found by exhaustive search

The returned modulus is no larger than any lower coefficient word whose monic modulus is
irreducible.

Formalized by `BitVec.findIrreducibleModulus_minimal`, a theorem declared in [MathlibExt/FieldTheory/Finite/BinaryModulusSearch.lean, line 209](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/FieldTheory/Finite/BinaryModulusSearch.lean#L209). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/FieldTheory/finite-fields/searching-for-irreducible-polynomials-over-gf-2/index.html#find-irreducible-modulus-minimal).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Searching for irreducible polynomials over GF(2)](https://deicyde.github.io/atlas-lean/roadmap/FieldTheory/finite-fields/searching-for-irreducible-polynomials-over-gf-2/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/FieldTheory/finite-fields/searching-for-irreducible-polynomials-over-gf-2)
