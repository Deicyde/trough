---
declaration: lemma
origin: cited
lean: Cayley.klein_trace_sum, Cayley.trace_diag_mul_cay
statement: formalized
proof: formalized
---

# klein_sum

$\sum_{k=0}^{3} \operatorname{\mathrm{tr}}(B_k^T X) = 0$ for every $3 \times 3$ matrix $X$, and

$$
\operatorname{\mathrm{tr}}\bigl(\mathrm{diag}(a, b, c)\,\mathrm{Cay}(x, y, z)\bigr) =
\frac{a(1 + x^2 - y^2 - z^2) + b(1 - x^2 + y^2 - z^2) + c(1 - x^2 - y^2 + z^2)}{1 + x^2 + y^2 + z^2}.
$$

## Depends on

- [charts](def-charts.md)

## Proof

The diagonal entries of $\sum_k B_k$ vanish; the second identity is a direct computation.

## Lean

Formalized as [`Cayley.klein_trace_sum`](https://jcreedcmu.github.io/Noperthedron/docs/find/#doc/Cayley.klein_trace_sum), [`Cayley.trace_diag_mul_cay`](https://jcreedcmu.github.io/Noperthedron/docs/find/#doc/Cayley.trace_diag_mul_cay).

## Sources

- [Noperthedron blueprint: chapters/reduction.tex, line 200](https://github.com/jcreedcmu/Noperthedron/blob/0143f65be7f59b3ac09b99debb9c37944a0a2f4b/blueprint/src/chapters/reduction.tex#L200)
