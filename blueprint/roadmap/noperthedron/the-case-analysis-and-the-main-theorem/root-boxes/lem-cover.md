---
declaration: lemma
origin: cited
lean: Cayley.Pack.cover, Cayley.Pack.rootK_inv
statement: formalized
proof: formalized
---

# Coverage

Every reduced $(u, v, j, r)$ is an admissible point of one of the root boxes of chart $j$.

## Depends on

- [root_boxes](def-root-boxes.md)
- [reduced](../../the-reduction/the-reduced-domain/def-reduced.md)
- [bad](../../boxes-and-leaf-certificates/boxes/def-bad.md)
- [exists_face](../../the-reduction/blowing-up-charts-0-and-4/lem-exists-face.md)

## Proof

The wedge and disk conditions give $0 \le u \le 1$ and $0 \le v \le \frac{57}{128}u \le \frac12$. In charts 1–3, $|r_i| \le 1$. In charts 0 and 4, Lemma [exists_face](../../the-reduction/blowing-up-charts-0-and-4/lem-exists-face.md) writes $r = \rho\, c_f(s_0, s_1)$ with $0 \le \rho \le 1$ or $0 \le \rho \le 2$.

## Lean

Formalized as [`Cayley.Pack.cover`](https://jcreedcmu.github.io/Noperthedron/docs/find/#doc/Cayley.Pack.cover), [`Cayley.Pack.rootK_inv`](https://jcreedcmu.github.io/Noperthedron/docs/find/#doc/Cayley.Pack.rootK_inv).

## Sources

- [Noperthedron blueprint: chapters/main.tex, line 21](https://github.com/jcreedcmu/Noperthedron/blob/434011e647523fac1a7116a77df5ac6f283e3fbb/blueprint/src/chapters/main.tex#L21)
