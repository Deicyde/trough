---
declaration: section
origin: cited
lean: minpoly.isIntegral_iff_mem_lifts, minpoly.isIntegral_iff_coeff_mem_range, IsIntegrallyClosed.minpoly_eq_map_iff_isIntegral
statement: formalized
proof: formalized
---

# Minimal polynomials and integrality

3 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/FieldTheory/extensions-and-closure/minimal-polynomials-and-integrality/index.html).

## Minimal polynomials

## Integrality via a lift of the minimal polynomial

Let $R$ be an integrally closed domain
with fraction field $K$, and let $L$ be a field extension of $K$ that is also an $R$-algebra,
with the $R$-algebra structure on $L$ the composite of $R \to K$ and $K \to L$. An element
$x \in L$ that is algebraic over $K$ is integral over $R$ if and only if the minimal polynomial
of $x$ over $K$ is the image of a polynomial in $R[X]$ under the map $R[X] \to K[X]$ that
applies $R \to K$ to each coefficient.

Formalized by `minpoly.isIntegral_iff_mem_lifts`, a theorem declared in [MathlibExt/FieldTheory/Minpoly/IntegrallyClosed.lean, line 35](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/FieldTheory/Minpoly/IntegrallyClosed.lean#L35). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/FieldTheory/extensions-and-closure/minimal-polynomials-and-integrality/index.html#is-integral-iff-mem-lifts).

## Integrality via the coefficients of the minimal polynomial

Let $R$ be an integrally
closed domain with fraction field $K$, and let $L$ be a field extension of $K$ that is also an
$R$-algebra, with the $R$-algebra structure on $L$ the composite of $R \to K$ and $K \to L$.
An element $x \in L$ that is algebraic over $K$ is integral over $R$ if and only if every
coefficient of the minimal polynomial of $x$ over $K$ lies in the image of $R$ in $K$.

Formalized by `minpoly.isIntegral_iff_coeff_mem_range`, a theorem declared in [MathlibExt/FieldTheory/Minpoly/IntegrallyClosed.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/FieldTheory/Minpoly/IntegrallyClosed.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/FieldTheory/extensions-and-closure/minimal-polynomials-and-integrality/index.html#is-integral-iff-coeff-mem-range).

## Integrality via equality of minimal polynomials

Let $A$ be an integrally closed domain
with fraction field $K$, and let $L$ be a field extension of $K$ that is also an $A$-algebra,
with the $A$-algebra structure on $L$ the composite of $A \to K$ and $K \to L$. An element
$\alpha \in L$ that is integral over $K$ is integral over $A$ if and only if the minimal
polynomial of $\alpha$ over $K$ equals the image of the minimal polynomial of $\alpha$ over $A$
under the map $A[X] \to K[X]$ that applies $A \to K$ to each coefficient. Here the minimal
polynomial of $\alpha$ over $A$ is taken to be $0$ when $\alpha$ is not integral over $A$.

## Sources

- Proposition 1.28, in equality form.

Formalized by `IsIntegrallyClosed.minpoly_eq_map_iff_isIntegral`, a theorem declared in [MathlibExt/FieldTheory/Minpoly/IntegrallyClosed.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/FieldTheory/Minpoly/IntegrallyClosed.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/FieldTheory/extensions-and-closure/minimal-polynomials-and-integrality/index.html#minpoly-eq-map-iff-is-integral).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Minimal polynomials and integrality](https://deicyde.github.io/atlas-lean/roadmap/FieldTheory/extensions-and-closure/minimal-polynomials-and-integrality/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/FieldTheory/extensions-and-closure/minimal-polynomials-and-integrality)
