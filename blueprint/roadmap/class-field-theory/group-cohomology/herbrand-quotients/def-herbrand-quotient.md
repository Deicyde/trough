---
declaration: definition
origin: cited
lean: Representation.herbrandQuotient, Rep.herbrandQuotient
statement: formalized
---

# herbrand quotient

Let $G$ be a finite cyclic group and $M$ a representation of $G$. Recall that there are isomorphisms $H^n_{\mathrm{Tate}}(G,M) \cong H^{n+2}_{\mathrm{Tate}}(G,M)$. We define the Herbrand quotient of $M$ to be

$$
h(G,M) = \frac{|H^0_{\mathrm{Tate}}(G,M)|}{|H^1_{\mathrm{Tate}}(G,M)|}.
$$

If either of the two cohomology groups are infinite then $h(G,M)$ defaults to $0$.

## Depends on

- [Tate cohomology](../tate-cohomology/def-tate-cohomology.md)

## Lean

Formalized as [`Representation.herbrandQuotient`](https://kbuzzard.github.io/ClassFieldTheory/docs/find/#doc/Representation.herbrandQuotient), [`Rep.herbrandQuotient`](https://kbuzzard.github.io/ClassFieldTheory/docs/find/#doc/Rep.herbrandQuotient).

## Sources

- [Class field theory blueprint: _2_cohomology.tex, line 1689](https://github.com/kbuzzard/ClassFieldTheory/blob/629ae9ed781748980bb51ab6f5f338ad9d6db3e8/blueprint/src/_2_cohomology.tex#L1689)
