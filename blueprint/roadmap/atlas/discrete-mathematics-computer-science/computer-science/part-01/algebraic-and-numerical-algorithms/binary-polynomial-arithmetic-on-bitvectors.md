---
declaration: section
origin: cited
lean: Polynomial.degree_ofCoeffList_lt, Polynomial.ofCoeffList_ofFn_coeff, Polynomial.toBitVec, BitVec.toPolynomial, BitVec.coeff_toPolynomial, BitVec.toBitVec_toPolynomial, Polynomial.toPolynomial_toBitVec, BitVec.toPolynomial_xor
statement: formalized
proof: formalized
---

# Binary polynomial arithmetic on bitvectors

26 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/binary-polynomial-arithmetic-on-bitvectors/index.html).

## Degree bound for a polynomial built from a coefficient list

A polynomial built from a low-coefficient-first list has degree strictly less than the list
length, including for an empty list and over a trivial semiring.

Formalized by `Polynomial.degree_ofCoeffList_lt`, a theorem declared in [MathlibExt/Algebra/Polynomial/BitVec.lean, line 38](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Algebra/Polynomial/BitVec.lean#L38). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/binary-polynomial-arithmetic-on-bitvectors/index.html#degree-of-coeff-list-lt).

## Reconstructing a polynomial from a fixed-width coefficient list

Reconstruct a polynomial from any fixed-width list containing all its possibly nonzero
coefficients.

Formalized by `Polynomial.ofCoeffList_ofFn_coeff`, a theorem declared in [MathlibExt/Algebra/Polynomial/BitVec.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Algebra/Polynomial/BitVec.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/binary-polynomial-arithmetic-on-bitvectors/index.html#of-coeff-list-of-fn-coeff).

## Bitvector of the low coefficients of a binary polynomial

Extract the lowest `s` binary coefficients of a polynomial as a fixed-width bitvector.
Coefficients at indices at least `s` are deliberately truncated.

Formalized by `Polynomial.toBitVec`, a definition declared in [MathlibExt/Algebra/Polynomial/BitVec.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Algebra/Polynomial/BitVec.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/binary-polynomial-arithmetic-on-bitvectors/index.html#to-bit-vec).

## Binary polynomial of a bitvector

The polynomial over `ZMod 2` whose coefficient of `X ^ i` is the `i`-th least-significant
bit of `w`.

Formalized by `BitVec.toPolynomial`, a definition declared in [MathlibExt/Algebra/Polynomial/BitVec.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Algebra/Polynomial/BitVec.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/binary-polynomial-arithmetic-on-bitvectors/index.html#to-polynomial).

## Coefficients of the binary polynomial of a bitvector

Every coefficient of the polynomial encoding is the corresponding least-significant bit;
indices outside the fixed width have coefficient zero.

Formalized by `BitVec.coeff_toPolynomial`, a theorem declared in [MathlibExt/Algebra/Polynomial/BitVec.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Algebra/Polynomial/BitVec.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/binary-polynomial-arithmetic-on-bitvectors/index.html#coeff-to-polynomial).

## Bitvector encoding recovers the original word

Extracting the coefficients of an encoded word recovers the original fixed-width word.

Formalized by `BitVec.toBitVec_toPolynomial`, a theorem declared in [MathlibExt/Algebra/Polynomial/BitVec.lean, line 85](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Algebra/Polynomial/BitVec.lean#L85). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/binary-polynomial-arithmetic-on-bitvectors/index.html#to-bit-vec-to-polynomial).

## Polynomial encoding recovers a low-degree polynomial

A polynomial whose degree is below the selected width is recovered after coefficient
extraction and fixed-width encoding.

Formalized by `Polynomial.toPolynomial_toBitVec`, a theorem declared in [MathlibExt/Algebra/Polynomial/BitVec.lean, line 105](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Algebra/Polynomial/BitVec.lean#L105). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/binary-polynomial-arithmetic-on-bitvectors/index.html#to-polynomial-to-bit-vec).

## Bitwise xor corresponds to polynomial addition over $\mathbb{F}_2$

Polynomial encoding turns bitwise xor into addition over `ZMod 2`; this is not the carried
integer addition on bitvectors.

Formalized by `BitVec.toPolynomial_xor`, a theorem declared in [MathlibExt/Algebra/Polynomial/BitVec.lean, line 124](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Algebra/Polynomial/BitVec.lean#L124). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/binary-polynomial-arithmetic-on-bitvectors/index.html#to-polynomial-xor).

## Monic binary modulus of a fixed-width word

The monic polynomial obtained by adjoining the width term `X ^ s` to the encoded lower
coefficients.

Formalized by `BitVec.monicModulus`, a definition declared in [MathlibExt/Algebra/Polynomial/BitVec.lean, line 134](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Algebra/Polynomial/BitVec.lean#L134). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/binary-polynomial-arithmetic-on-bitvectors/index.html#monic-modulus).

## The binary modulus is monic

The binary modulus associated to a fixed-width word is monic, including at width zero.

Formalized by `BitVec.monicModulus_monic`, a theorem declared in [MathlibExt/Algebra/Polynomial/BitVec.lean, line 138](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Algebra/Polynomial/BitVec.lean#L138). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/binary-polynomial-arithmetic-on-bitvectors/index.html#monic-modulus-monic).

## Degree of the binary modulus

The natural degree of the binary modulus is exactly the width of its lower coefficients.

Formalized by `BitVec.monicModulus_natDegree`, a theorem declared in [MathlibExt/Algebra/Polynomial/BitVec.lean, line 144](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Algebra/Polynomial/BitVec.lean#L144). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/binary-polynomial-arithmetic-on-bitvectors/index.html#monic-modulus-nat-degree).

## Fixed-width binary words as residues modulo a monic polynomial

Fixed-width binary words are in bijection with residues modulo their associated monic
polynomial. This is an ordinary equivalence because builtin bitvector addition has carries.

Formalized by `BitVec.adjoinRootEquiv`, a definition declared in [MathlibExt/RingTheory/AdjoinRoot/BitVec.lean, line 40](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/RingTheory/AdjoinRoot/BitVec.lean#L40). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/binary-polynomial-arithmetic-on-bitvectors/index.html#adjoin-root-equiv).

## Forward map of the binary word residue equivalence

The forward equivalence is the canonical quotient constructor applied to the polynomial
encoding.

Formalized by `BitVec.adjoinRootEquiv_apply`, a theorem declared in [MathlibExt/RingTheory/AdjoinRoot/BitVec.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/RingTheory/AdjoinRoot/BitVec.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/binary-polynomial-arithmetic-on-bitvectors/index.html#adjoin-root-equiv-apply).

## Inverse map of the binary word residue equivalence

The inverse equivalence extracts the canonical remainder's lowest `s` binary
coefficients.

Formalized by `BitVec.adjoinRootEquiv_symm_apply`, a theorem declared in [MathlibExt/RingTheory/AdjoinRoot/BitVec.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/RingTheory/AdjoinRoot/BitVec.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/binary-polynomial-arithmetic-on-bitvectors/index.html#adjoin-root-equiv-symm-apply).

## Remainder coefficients of an encoded binary word are its bits

The canonical remainder coordinates of an encoded word are exactly its low-first bits.

Formalized by `BitVec.adjoinRootEquiv_coeff`, a theorem declared in [MathlibExt/RingTheory/AdjoinRoot/BitVec.lean, line 85](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/RingTheory/AdjoinRoot/BitVec.lean#L85). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/binary-polynomial-arithmetic-on-bitvectors/index.html#adjoin-root-equiv-coeff).

## Bitwise xor corresponds to residue addition

Bitwise xor corresponds to quotient addition; builtin bitvector addition does not.

Formalized by `BitVec.adjoinRootEquiv_xor`, a theorem declared in [MathlibExt/RingTheory/AdjoinRoot/BitVec.lean, line 96](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/RingTheory/AdjoinRoot/BitVec.lean#L96). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/binary-polynomial-arithmetic-on-bitvectors/index.html#adjoin-root-equiv-xor).

## Reduction of the root power in a binary residue ring

The defining quotient equation reduces `root ^ s` to the encoded lower coefficients.

Formalized by `BitVec.adjoinRoot_root_pow`, a theorem declared in [MathlibExt/RingTheory/AdjoinRoot/BitVec.lean, line 102](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/RingTheory/AdjoinRoot/BitVec.lean#L102). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/binary-polynomial-arithmetic-on-bitvectors/index.html#adjoin-root-root-pow).

## Multiplication by $X$ of a binary polynomial residue

Multiply a binary residue by `X`, reducing by `X ^ s + g` when its top bit is set.

Formalized by `BitVec.mulXMod`, a definition declared in [MathlibExt/Data/BitVec/BinaryPolynomialArithmetic.lean, line 34](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Data/BitVec/BinaryPolynomialArithmetic.lean#L34). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/binary-polynomial-arithmetic-on-bitvectors/index.html#mul-xmod).

## Modular multiplication of binary polynomial residues

Multiply binary residues by low-first Horner evaluation of the second operand's bits.

Formalized by `BitVec.mulMod`, a definition declared in [MathlibExt/Data/BitVec/BinaryPolynomialArithmetic.lean, line 38](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Data/BitVec/BinaryPolynomialArithmetic.lean#L38). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/binary-polynomial-arithmetic-on-bitvectors/index.html#mul-mod).

## Modular powering of binary polynomial residues

Raise a binary residue to a natural power by tail-recursive repeated multiplication.

Formalized by `BitVec.powMod`, a definition declared in [MathlibExt/Data/BitVec/BinaryPolynomialArithmetic.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Data/BitVec/BinaryPolynomialArithmetic.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/binary-polynomial-arithmetic-on-bitvectors/index.html#pow-mod).

## Evaluation of modular multiplication by $X$

Multiplication by `X` has its expected evaluation in every commutative ring receiving
`ZMod 2`.

Formalized by `BitVec.eval₂_mulXMod`, a theorem declared in [MathlibExt/Data/BitVec/BinaryPolynomialArithmetic.lean, line 87](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Data/BitVec/BinaryPolynomialArithmetic.lean#L87). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/binary-polynomial-arithmetic-on-bitvectors/index.html#eval-mul-xmod).

## Evaluation of modular Horner multiplication

Horner multiplication has its expected evaluation in every commutative ring receiving
`ZMod 2`; the second operand may have any width.

Formalized by `BitVec.eval₂_mulMod`, a theorem declared in [MathlibExt/Data/BitVec/BinaryPolynomialArithmetic.lean, line 147](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Data/BitVec/BinaryPolynomialArithmetic.lean#L147). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/binary-polynomial-arithmetic-on-bitvectors/index.html#eval-mul-mod).

## Evaluation of modular powering

Repeated multiplication has its expected power evaluation for positive result width.

Formalized by `BitVec.eval₂_powMod`, a theorem declared in [MathlibExt/Data/BitVec/BinaryPolynomialArithmetic.lean, line 168](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Data/BitVec/BinaryPolynomialArithmetic.lean#L168). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/binary-polynomial-arithmetic-on-bitvectors/index.html#eval-pow-mod).

## Modular multiplication by $X$ matches the quotient root

Modular multiplication by `X` agrees with multiplication by the quotient root.

Formalized by `BitVec.adjoinRootEquiv_mulXMod`, a theorem declared in [MathlibExt/Data/BitVec/BinaryPolynomialArithmetic.lean, line 187](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Data/BitVec/BinaryPolynomialArithmetic.lean#L187). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/binary-polynomial-arithmetic-on-bitvectors/index.html#adjoin-root-equiv-mul-xmod).

## Modular multiplication matches the polynomial quotient

Modular Horner multiplication agrees with multiplication in the polynomial quotient.

Formalized by `BitVec.adjoinRootEquiv_mulMod`, a theorem declared in [MathlibExt/Data/BitVec/BinaryPolynomialArithmetic.lean, line 206](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Data/BitVec/BinaryPolynomialArithmetic.lean#L206). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/binary-polynomial-arithmetic-on-bitvectors/index.html#adjoin-root-equiv-mul-mod).

## Modular powering matches the polynomial quotient

Modular powering agrees with powering in the polynomial quotient, including width zero.

Formalized by `BitVec.adjoinRootEquiv_powMod`, a theorem declared in [MathlibExt/Data/BitVec/BinaryPolynomialArithmetic.lean, line 226](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Data/BitVec/BinaryPolynomialArithmetic.lean#L226). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/binary-polynomial-arithmetic-on-bitvectors/index.html#adjoin-root-equiv-pow-mod).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Binary polynomial arithmetic on bitvectors](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/algebraic-and-numerical-algorithms/binary-polynomial-arithmetic-on-bitvectors/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/ComputerScience/algebraic-and-numerical-algorithms/binary-polynomial-arithmetic-on-bitvectors)
