---
declaration: lemma
origin: cited
lean: Cayley.num_sub_denom, Cayley.Pack.Lp_real
statement: formalized
proof: formalized
---

# Blow-up identity

In charts 0 and 4, with $r = \rho\, c$,

$$
D_o\, \kappa_j\, D_r\, \mathrm{gap}_{\sigma(S)}
= 2 \rho\, \bigl\langle w,\ N_o\, M_j \bigl(c \times S + \rho\, c \times (c \times S)\bigr) \bigr\rangle
= 2\rho\, L(X).
$$

## Depends on

- [Rodrigues form](../../cayley-coordinates/lem-cayley-rodrigues.md)
- [Gap polynomial](../the-gap-polynomial/lem-gap-poly.md)
- [tau_pair](../../the-reduction/step-b-the-relative-rotation/lem-tau-pair.md)

## Proof

$Q_j(r) S - \sigma(S) = B_j(\mathrm{Cay}(r) S - S)$ in both charts (for chart 4, $\sigma(S) = \tau S = B_4 S$). Apply Lemma [Rodrigues form](../../cayley-coordinates/lem-cayley-rodrigues.md) and $r = \rho c$.

## Lean

Formalized as [`Cayley.num_sub_denom`](https://jcreedcmu.github.io/Noperthedron/docs/find/#doc/Cayley.num_sub_denom), [`Cayley.Pack.Lp_real`](https://jcreedcmu.github.io/Noperthedron/docs/find/#doc/Cayley.Pack.Lp_real).

## Sources

- [Noperthedron blueprint: chapters/certificates.tex, line 90](https://github.com/jcreedcmu/Noperthedron/blob/434011e647523fac1a7116a77df5ac6f283e3fbb/blueprint/src/chapters/certificates.tex#L90)
