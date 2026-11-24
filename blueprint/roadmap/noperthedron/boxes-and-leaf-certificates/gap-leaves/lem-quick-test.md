---
declaration: lemma
origin: cited
lean: Cayley.Pack.quick_real, Cayley.Pack.quick_G1
statement: formalized
proof: formalized
---

# Quick test

Suppose $A \ge c_0 - \mathrm{sl}$ and $|E_k - e_k| \le a_k$ on the box, where $c_0$, $e_k$ are constant terms and $\mathrm{sl}$, $a_k$ are coefficient sums. If

$$
c_0 - \mathrm{sl} - \mathrm{err} - \sum_k T_k e_k - \sum_k |T_k|\, a_k \ge 0,
$$

then $\mathrm{err} \le A - \sum_k T_k E_k$ on the box.

## Depends on

- [Gap polynomial](../the-gap-polynomial/lem-gap-poly.md)
- [Coefficient bound](../../lower-bounds-of-polynomials/the-coefficient-bound/thm-coef-bound.md)

## Proof

Linear arithmetic.

## Lean

Formalized as [`Cayley.Pack.quick_real`](https://jcreedcmu.github.io/Noperthedron/docs/find/#doc/Cayley.Pack.quick_real), [`Cayley.Pack.quick_G1`](https://jcreedcmu.github.io/Noperthedron/docs/find/#doc/Cayley.Pack.quick_G1).

## Sources

- [Noperthedron blueprint: chapters/certificates.tex, line 188](https://github.com/jcreedcmu/Noperthedron/blob/0143f65be7f59b3ac09b99debb9c37944a0a2f4b/blueprint/src/chapters/certificates.tex#L188)
