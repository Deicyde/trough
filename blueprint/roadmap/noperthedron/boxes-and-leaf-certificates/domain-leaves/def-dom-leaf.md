---
declaration: definition
origin: cited
lean: Cayley.K.pDomOK
statement: formalized
---

# dom_leaf

A domain leaf names one condition of Definition [reduced](../../the-reduction/the-reduced-domain/def-reduced.md) that fails on the whole box:

1. (disk) $u^2 + v^2 > 1$, tested at the corner with the smallest $u$ and $v$, both of which must be nonnegative;
2. (wedge) $v > \frac{57}{128} u$, tested at the corner with the largest $u$ and the smallest $v$, where $u$ must be nonnegative;
3. (chart $k$) $\operatorname{\mathrm{tr}}(B_j^T Q_j(r)) < \operatorname{\mathrm{tr}}(B_k^T Q_j(r))$, a polynomial inequality after clearing $D_r$;
4. (orbit $e, g, a$) $F(Q_j(r)) < F(H^e Q_j(r) g_g)$, established through the term $\operatorname{\mathrm{tr}}(B_a^T H^e Q_j(r) g_g) - [a = 4]\,\frac18$ with $a \in \{0, 4\}$, again a polynomial inequality after clearing denominators, with the tabulated $\hat g_g$ in place of $g_g$ and an explicit error allowance.

## Depends on

- [reduced](../../the-reduction/the-reduced-domain/def-reduced.md)
- [box](../boxes/def-box.md)

## Lean

Formalized as [`Cayley.K.pDomOK`](https://jcreedcmu.github.io/Noperthedron/docs/find/#doc/Cayley.K.pDomOK).

## Sources

- [Noperthedron blueprint: chapters/certificates.tex, line 206](https://github.com/jcreedcmu/Noperthedron/blob/434011e647523fac1a7116a77df5ac6f283e3fbb/blueprint/src/chapters/certificates.tex#L206)
