---
declaration: definition
origin: cited
lean: Cayley.K.pGapOK, Cayley.K.vtestG, Cayley.K.fullOK, Cayley.K.pairOK
statement: formalized
---

# gap_leaf

A gap leaf names an inner vertex $S$ and a direction $(w_0, w_1) \ne 0$. It passes if the box has scale $2^K$ with $K \le 16$ and $|w_0|, |w_1| \le 1024$ (which keeps the coefficients small enough for the packed arithmetic of Chapter [Lower bounds of polynomials](../../lower-bounds-of-polynomials/README.md), by Lemma [Norm guard](../../lower-bounds-of-polynomials/kronecker-packing/lem-norm-guard.md)), and for every one of the 90 outer vertices $T$ one of the following succeeds:

1. the *quick test*: a lower bound of $A - \sum_k T_k E_k$ built from the constant terms and coefficient sums of $A$ and the $E_k$, evaluated for all 90 vertices at once;
2. the *full test*: the coefficient lower bound or the Bernstein lower bound of the polynomial $A - \sum_k \hat T_k E_k$ is at least $\mathrm{err}$;
3. for the paired vertex $T = \sigma(S)$ in charts 0 and 4: the coefficient or Bernstein lower bound of $2L$ is at least $\mathrm{err}$ (or $\rho > 0$ on the whole box and the full test succeeds).

## Depends on

- [Gap polynomial](../the-gap-polynomial/lem-gap-poly.md)
- [Blow-up identity](../the-blow-up/lem-blowup-identity.md)

## Lean

Formalized as [`Cayley.K.pGapOK`](https://jcreedcmu.github.io/Noperthedron/docs/find/#doc/Cayley.K.pGapOK), [`Cayley.K.vtestG`](https://jcreedcmu.github.io/Noperthedron/docs/find/#doc/Cayley.K.vtestG), [`Cayley.K.fullOK`](https://jcreedcmu.github.io/Noperthedron/docs/find/#doc/Cayley.K.fullOK), [`Cayley.K.pairOK`](https://jcreedcmu.github.io/Noperthedron/docs/find/#doc/Cayley.K.pairOK).

## Sources

- [Noperthedron blueprint: chapters/certificates.tex, line 149](https://github.com/jcreedcmu/Noperthedron/blob/434011e647523fac1a7116a77df5ac6f283e3fbb/blueprint/src/chapters/certificates.tex#L149)
