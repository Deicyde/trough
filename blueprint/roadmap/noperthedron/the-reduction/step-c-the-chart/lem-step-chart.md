---
declaration: lemma
origin: cited
lean: Cayley.step_chart
statement: formalized
proof: formalized
---

# step_chart

Every $Q \in SO(3)$ is $Q_j(r)$ for some $j$ that maximizes $\operatorname{\mathrm{tr}}(B_k^T Q)$ over $k \in \{0, \dots, 4\}$ and some $r$ with $|r_i| \le 1$ (if $j \le 3$) or $|r_i| \le 2$ (if $j = 4$).

## Depends on

- [klein_sum](lem-klein-sum.md)
- [cayley_trace](../../cayley-coordinates/lem-cayley-trace.md)
- [cayley_surj](../../cayley-coordinates/thm-cayley-surj.md)

## Proof

Take any maximizing $j$. By Lemma [klein_sum](lem-klein-sum.md) the four Klein traces sum to $0$, so the largest trace is nonnegative, and Theorem [cayley_surj](../../cayley-coordinates/thm-cayley-surj.md) gives $B_j^T Q = \mathrm{Cay}(r)$ with $|r|^2 \le 3$. This settles $j = 4$. For $j \le 3$, maximality against the other three Klein charts and the trace formula of Lemma [klein_sum](lem-klein-sum.md) give $4 - 4 r_i^2 \ge 0$ for each $i$.

## Lean

Formalized as [`Cayley.step_chart`](https://jcreedcmu.github.io/Noperthedron/docs/find/#doc/Cayley.step_chart).

## Sources

- [Noperthedron blueprint: chapters/reduction.tex, line 202](https://github.com/jcreedcmu/Noperthedron/blob/434011e647523fac1a7116a77df5ac6f283e3fbb/blueprint/src/chapters/reduction.tex#L202)
