---
declaration: section
origin: cited
lean: Cslib.Complexity.PolynomialEncoding.splitB, Cslib.Complexity.PolynomialEncoding.splitB_run, Cslib.Complexity.PolynomialEncoding.copyB_run
statement: formalized
proof: formalized
---

# Copying a bit block without consuming the source

3 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/conversions-between-bit-string-encodings/copying-a-bit-block-without-consuming-the-source/index.html).

## Two-destination bit-block transfer

Pop a bit block onto two distinct destinations, reversing both copies.

Formalized by `Cslib.Complexity.PolynomialEncoding.splitB`, a definition declared in [CSLibExt/Computability/Complexity/PolynomialEncoding/Copy.lean, line 30](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/PolynomialEncoding/Copy.lean#L30). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/conversions-between-bit-string-encodings/copying-a-bit-block-without-consuming-the-source/index.html#split-b).

## Two-destination bit transfer takes one step per bit plus one

Two-destination bit transfer takes one step per bit plus one,
with exact suffix and unrelated-stack preservation.

Formalized by `Cslib.Complexity.PolynomialEncoding.splitB_run`, a theorem declared in [CSLibExt/Computability/Complexity/PolynomialEncoding/Copy.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/PolynomialEncoding/Copy.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/conversions-between-bit-string-encodings/copying-a-bit-block-without-consuming-the-source/index.html#split-b-run).

## Bit-block copy keeps the order and restores source and scratch

Copy a bit block in its original order, restoring both the source
and scratch, in exactly `2 * p.length + 2` steps.

Formalized by `Cslib.Complexity.PolynomialEncoding.copyB_run`, a theorem declared in [CSLibExt/Computability/Complexity/PolynomialEncoding/Copy.lean, line 98](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Computability/Complexity/PolynomialEncoding/Copy.lean#L98). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/conversions-between-bit-string-encodings/copying-a-bit-block-without-consuming-the-source/index.html#copy-b-run).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Copying a bit block without consuming the source](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/np-completeness/cook-levin/conversions-between-bit-string-encodings/copying-a-bit-block-without-consuming-the-source/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/TheoryOfComputation/np-completeness/cook-levin/conversions-between-bit-string-encodings/copying-a-bit-block-without-consuming-the-source)
