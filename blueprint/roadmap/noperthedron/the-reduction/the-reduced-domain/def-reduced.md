---
declaration: definition
origin: cited
lean: Cayley.Reduced
statement: formalized
---

# reduced

A tuple $(u, v, j, r)$ with $j \in \{0, \dots, 4\}$ is *reduced* if

1. (wedge and disk) $u \ge 0$, $0 \le v \le \frac{57}{128} u$, $u^2 + v^2 \le 1$;
2. (chart) $\operatorname{\mathrm{tr}}(B_k^T Q_j(r)) \le \operatorname{\mathrm{tr}}(B_j^T Q_j(r))$ for all $k \le 4$;
3. (orbit) $F(H^e Q_j(r) g_k) \le F(Q_j(r))$ for all $e \in \{0,1\}$ and $k$, where $H = s(u,v)^T R_z(\pi) s(u,v)$;
4. (bounds) $|r_i| \le 1$ if $j \le 3$ and $|r_i| \le 2$ if $j = 4$.

## Depends on

- [charts](../step-c-the-chart/def-charts.md)
- [orbit_score](../step-b-the-relative-rotation/def-orbit-score.md)
- [outer_rot](../../cayley-coordinates/outer-views/def-outer-rot.md)

## Lean

Formalized as [`Cayley.Reduced`](https://jcreedcmu.github.io/Noperthedron/docs/find/#doc/Cayley.Reduced).

## Sources

- [Noperthedron blueprint: chapters/reduction.tex, line 223](https://github.com/jcreedcmu/Noperthedron/blob/434011e647523fac1a7116a77df5ac6f283e3fbb/blueprint/src/chapters/reduction.tex#L223)
