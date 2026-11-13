---
declaration: section
origin: cited
lean: Polynomial.IsPrimitivePolynomial, Polynomial.IsPrimitivePolynomial.monic, Polynomial.IsPrimitivePolynomial.irreducible, Polynomial.IsPrimitivePolynomial.root_orderOf, Polynomial.IsPrimitivePolynomial.iff, Polynomial.IsPrimitivePolynomial.iff_isPrimitiveRoot, Polynomial.IsPrimitivePolynomial.zmod_iff
statement: formalized
proof: formalized
---

# Primitive polynomials over finite fields

7 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/FieldTheory/finite-fields/primitive-polynomials-over-finite-fields/index.html).

## Primitive polynomial over a finite field

Let $F$ be a finite field with $q$ elements,
let $f \in F[X]$, and let $n$ be the degree of $f$ (with $n = 0$ if $f = 0$). Then $f$ is
primitive if it is monic, it is irreducible, and the class of $X$ in the quotient ring
$F[X]/(f)$ has multiplicative order $q^n - 1$.

Formalized by `Polynomial.IsPrimitivePolynomial`, a definition declared in [MathlibExt/FieldTheory/Finite/PrimitivePolynomial.lean, line 33](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/FieldTheory/Finite/PrimitivePolynomial.lean#L33). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/FieldTheory/finite-fields/primitive-polynomials-over-finite-fields/index.html#is-primitive-polynomial).

## Primitive polynomials are monic

Every primitive polynomial over a finite field is
monic.

Formalized by `Polynomial.IsPrimitivePolynomial.monic`, a theorem declared in [MathlibExt/FieldTheory/Finite/PrimitivePolynomial.lean, line 40](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/FieldTheory/Finite/PrimitivePolynomial.lean#L40). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/FieldTheory/finite-fields/primitive-polynomials-over-finite-fields/index.html#monic).

## Primitive polynomials are irreducible

Every primitive polynomial over a finite field is
irreducible.

Formalized by `Polynomial.IsPrimitivePolynomial.irreducible`, a theorem declared in [MathlibExt/FieldTheory/Finite/PrimitivePolynomial.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/FieldTheory/Finite/PrimitivePolynomial.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/FieldTheory/finite-fields/primitive-polynomials-over-finite-fields/index.html#irreducible).

## Order of the root of a primitive polynomial

Let $F$ be a finite field with $q$ elements
and let $f \in F[X]$ be a primitive polynomial of degree $n$. Then the class of $X$ in the
quotient ring $F[X]/(f)$ has multiplicative order $q^n - 1$.

Formalized by `Polynomial.IsPrimitivePolynomial.root_orderOf`, a theorem declared in [MathlibExt/FieldTheory/Finite/PrimitivePolynomial.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/FieldTheory/Finite/PrimitivePolynomial.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/FieldTheory/finite-fields/primitive-polynomials-over-finite-fields/index.html#root-order-of).

## Defining characterization of primitive polynomials

Let $F$ be a finite field with $q$
elements, let $f \in F[X]$, and let $n$ be the degree of $f$ (with $n = 0$ if $f = 0$). Then $f$
is primitive if and only if $f$ is monic, $f$ is irreducible, and the class of $X$ in the
quotient ring $F[X]/(f)$ has multiplicative order $q^n - 1$.

Formalized by `Polynomial.IsPrimitivePolynomial.iff`, a theorem declared in [MathlibExt/FieldTheory/Finite/PrimitivePolynomial.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/FieldTheory/Finite/PrimitivePolynomial.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/FieldTheory/finite-fields/primitive-polynomials-over-finite-fields/index.html#iff).

## Primitive polynomials via primitive roots of unity

Let $F$ be a finite field with $q$
elements, let $f \in F[X]$, and let $n$ be the degree of $f$ (with $n = 0$ if $f = 0$). Let
$\alpha$ be the class of $X$ in the quotient ring $F[X]/(f)$. Then $f$ is primitive if and only
if $f$ is monic, $f$ is irreducible, and $\alpha$ is a primitive $(q^n - 1)$-th root of unity,
that is, $\alpha^{q^n - 1} = 1$ and $q^n - 1$ divides every natural number $l$ with
$\alpha^l = 1$.

Formalized by `Polynomial.IsPrimitivePolynomial.iff_isPrimitiveRoot`, a theorem declared in [MathlibExt/FieldTheory/Finite/PrimitivePolynomial.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/FieldTheory/Finite/PrimitivePolynomial.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/FieldTheory/finite-fields/primitive-polynomials-over-finite-fields/index.html#iff-is-primitive-root).

## Primitive polynomials over $\mathbb{Z}/p\mathbb{Z}$

Let $p$ be a prime, let $f$ be a
polynomial over $\mathbb{Z}/p\mathbb{Z}$, and let $n$ be the degree of $f$ (with $n = 0$ if
$f = 0$). Then $f$ is primitive if and only if $f$ is monic, $f$ is irreducible, and the class of
$X$ in the quotient ring $(\mathbb{Z}/p\mathbb{Z})[X]/(f)$ has multiplicative order $p^n - 1$.

## Sources

- ATLAS Definition 3.14.

Formalized by `Polynomial.IsPrimitivePolynomial.zmod_iff`, a theorem declared in [MathlibExt/FieldTheory/Finite/PrimitivePolynomial.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/FieldTheory/Finite/PrimitivePolynomial.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/FieldTheory/finite-fields/primitive-polynomials-over-finite-fields/index.html#zmod-iff).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Primitive polynomials over finite fields](https://deicyde.github.io/atlas-lean/roadmap/FieldTheory/finite-fields/primitive-polynomials-over-finite-fields/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/FieldTheory/finite-fields/primitive-polynomials-over-finite-fields)
