---
declaration: section
origin: cited
lean: Octonion.basisSign, Octonion.structureConstant, Octonion.basisSign_mul_self, Octonion.basisSign_mul_add_swap, Octonion.sum_structureConstant_mul, Octonion.crossing_identity, Octonion.abs_structureConstant_le_one, Octonion.abs_sum_structureConstant_mul_le_one
statement: formalized
proof: formalized
---

# Degen's eight-square identity

8 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/algebraic-identities/degen-s-eight-square-identity/index.html).

## Sign of a product of octonion basis elements

The sign of the product of basis elements indexed by `p` and `q`.

The output basis index is `p ^^^ q`. Bits are read least-significant first, so
bits 0, 1, and 2 correspond to the source coordinates 1, 2, and 3.

Formalized by `Octonion.basisSign`, a definition declared in [MathlibExt/Algebra/Octonion/StructureConstants.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Algebra/Octonion/StructureConstants.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/algebraic-identities/degen-s-eight-square-identity/index.html#basis-sign).

## Signed structure constant of the eight-square algebra

The signed structure constant for the basis product indexed by `p` and `q`.

Formalized by `Octonion.structureConstant`, a definition declared in [MathlibExt/Algebra/Octonion/StructureConstants.lean, line 94](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Algebra/Octonion/StructureConstants.lean#L94). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/algebraic-identities/degen-s-eight-square-identity/index.html#structure-constant).

## Basis multiplication signs square to one

Every basis multiplication sign squares to one.

Formalized by `Octonion.basisSign_mul_self`, a theorem declared in [MathlibExt/Algebra/Octonion/StructureConstants.lean, line 113](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Algebra/Octonion/StructureConstants.lean#L113). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/algebraic-identities/degen-s-eight-square-identity/index.html#basis-sign-mul-self).

## Sign cancellation for two decompositions of an xor index

The cancellation rule of signs for two distinct decompositions of one xor index.

Formalized by `Octonion.basisSign_mul_add_swap`, a theorem declared in [MathlibExt/Algebra/Octonion/StructureConstants.lean, line 119](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Algebra/Octonion/StructureConstants.lean#L119). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/algebraic-identities/degen-s-eight-square-identity/index.html#basis-sign-mul-add-swap).

## Contraction of two structure constants

Contracting two structure constants leaves their common xor component.

Formalized by `Octonion.sum_structureConstant_mul`, a theorem declared in [MathlibExt/Algebra/Octonion/StructureConstants.lean, line 127](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Algebra/Octonion/StructureConstants.lean#L127). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/algebraic-identities/degen-s-eight-square-identity/index.html#sum-structure-constant-mul).

## Eight-square crossing identity

The two contractions in the eight-square crossing decomposition.

Formalized by `Octonion.crossing_identity`, a theorem declared in [MathlibExt/Algebra/Octonion/StructureConstants.lean, line 134](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Algebra/Octonion/StructureConstants.lean#L134). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/algebraic-identities/degen-s-eight-square-identity/index.html#crossing-identity).

## Structure constants are bounded by one

A structure constant has absolute value at most one.

Formalized by `Octonion.abs_structureConstant_le_one`, a theorem declared in [MathlibExt/Algebra/Octonion/StructureConstants.lean, line 142](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Algebra/Octonion/StructureConstants.lean#L142). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/algebraic-identities/degen-s-eight-square-identity/index.html#abs-structure-constant-le-one).

## Contractions of structure constants are bounded by one

A contraction of two structure constants has absolute value at most one.

Formalized by `Octonion.abs_sum_structureConstant_mul_le_one`, a theorem declared in [MathlibExt/Algebra/Octonion/StructureConstants.lean, line 148](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Algebra/Octonion/StructureConstants.lean#L148). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/algebraic-identities/degen-s-eight-square-identity/index.html#abs-sum-structure-constant-mul-le-one).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Degen's eight-square identity](https://deicyde.github.io/atlas-lean/roadmap/Algebra/algebraic-identities/degen-s-eight-square-identity/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Algebra/algebraic-identities/degen-s-eight-square-identity)
