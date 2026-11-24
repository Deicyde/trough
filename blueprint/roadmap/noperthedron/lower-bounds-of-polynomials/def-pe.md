---
declaration: definition
origin: cited
lean: Cayley.Pack.PE, Cayley.Pack.PE.ev, Cayley.Pack.PE.nrm
statement: formalized
---

# pe

A *polynomial expression* is a term built from integer constants, the variables $t_0, \dots, t_4$, addition, subtraction and multiplication. It can be evaluated in any commutative ring. Its *norm* is computed by replacing every constant by its absolute value and evaluating at $t = (1, \dots, 1)$; it bounds the sum of the absolute values of the coefficients of the polynomial.

## Depends on

Its statement uses no other node of the blueprint.

## Lean

Formalized as [`Cayley.Pack.PE`](https://jcreedcmu.github.io/Noperthedron/docs/find/#doc/Cayley.Pack.PE), [`Cayley.Pack.PE.ev`](https://jcreedcmu.github.io/Noperthedron/docs/find/#doc/Cayley.Pack.PE.ev), [`Cayley.Pack.PE.nrm`](https://jcreedcmu.github.io/Noperthedron/docs/find/#doc/Cayley.Pack.PE.nrm).

## Sources

- [Noperthedron blueprint: chapters/polybounds.tex, line 10](https://github.com/jcreedcmu/Noperthedron/blob/0143f65be7f59b3ac09b99debb9c37944a0a2f4b/blueprint/src/chapters/polybounds.tex#L10)
