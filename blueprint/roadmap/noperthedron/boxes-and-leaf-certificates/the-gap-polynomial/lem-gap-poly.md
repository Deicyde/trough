---
declaration: lemma
origin: cited
lean: Cayley.gap_identity, Cayley.Pack.Fp_real, Cayley.Pack.Fp_split
statement: formalized
proof: formalized
---

# Gap polynomial

$$
D_o\,\kappa_j\,D_r\,\mathrm{gap}_T
= \bigl\langle w,\ N_o\, M_j\, N(r)\, S \bigr\rangle - \kappa_j D_r \bigl\langle w,\ N_o\, T \bigr\rangle,
$$

where $N_o$ is the numerator of $s(u, v)$. As a function of the normalized coordinates $t$, this is (up to a fixed power of two) a polynomial with integer coefficients of degree at most $2$ in each variable. Writing $\alpha_k = w_0 (N_o)_{0k} + w_1 (N_o)_{1k}$, it equals $A - \sum_k T_k E_k$ with $A = \sum_k \alpha_k (M_j N(r) S)_k$ and $E_k = \alpha_k \kappa_j D_r$, which do not depend on $T$.

## Depends on

- [box](../boxes/def-box.md)
- [cayley](../../cayley-coordinates/def-cayley.md)
- [outer_rot](../../cayley-coordinates/outer-views/def-outer-rot.md)
- [charts](../../the-reduction/step-c-the-chart/def-charts.md)
- [Separation criterion](../../rupert-pairs/shadows-and-the-separation-criterion/thm-separation.md)

## Proof

$D_o\, s = N_o$ and $D_r \mathrm{Cay}(r) = N(r)$; the entries of $N_o$ have degree at most $2$ in each of $u, v$, and the entries of $N(r)$ and $D_r$ have degree at most $2$ in each of $r_0, r_1, r_2$ (or of $s_0, s_1, \rho$ in the blown-up charts, where $r = \rho\, c_f(s_0, s_1)$). The product is bilinear in these two groups of variables.

## Lean

Formalized as [`Cayley.gap_identity`](https://jcreedcmu.github.io/Noperthedron/docs/find/#doc/Cayley.gap_identity), [`Cayley.Pack.Fp_real`](https://jcreedcmu.github.io/Noperthedron/docs/find/#doc/Cayley.Pack.Fp_real), [`Cayley.Pack.Fp_split`](https://jcreedcmu.github.io/Noperthedron/docs/find/#doc/Cayley.Pack.Fp_split).

## Sources

- [Noperthedron blueprint: chapters/certificates.tex, line 52](https://github.com/jcreedcmu/Noperthedron/blob/434011e647523fac1a7116a77df5ac6f283e3fbb/blueprint/src/chapters/certificates.tex#L52)
