---
declaration: section
origin: cited
lean: MathlibExt.Algebra.Polynomial.ScottishBook148Wanted.auerbachPolynomialZeroSetSeparatesIffFactorsSignDefinite
statement: formalized
---

# Zeros of polynomials: its own results

1 result, 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/zeros-of-polynomials/index.html).

Location, counting and multiplicity of the zeros of polynomials: real-rootedness, stability, interlacing, root bounds and Sturm sequences.

## Auerbach's problem on zero sets of real polynomials

Let `P` be a nonzero real polynomial in `n` variables. Its zero set does
not cut (separate) Euclidean space, i.e. the complement of the zero set is
connected, if and only if every irreducible factor of `P` over the reals is
always nonnegative or always nonpositive (as a function). The complement of
a real algebraic hypersurface is semialgebraic, so connectedness of the
complement is equivalent to the path-connectedness used by Rojas.

## Sources

- H. Auerbach, Problem 148 of the Scottish Book; both necessity and sufficiency proved by J. M. Rojas, "About Herman Auerbach's problem on factors of real polynomials with connected zero set complement", 2015 (see the commentary in Mauldin (ed.), The Scottish Book, 2nd ed., 2015).

Stated but not proved: `MathlibExt.Algebra.Polynomial.ScottishBook148Wanted.auerbachPolynomialZeroSetSeparatesIffFactorsSignDefinite` is written with `theorem_wanted` in [WantedExt/Algebra/Polynomial/ScottishBook148Wanted.lean, line 35](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Algebra/Polynomial/ScottishBook148Wanted.lean#L35). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Algebra/zeros-of-polynomials/index.html#auerbach-polynomial-zero-set-separates-i).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Zeros of polynomials](https://deicyde.github.io/atlas-lean/roadmap/Algebra/zeros-of-polynomials/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Algebra/zeros-of-polynomials)
