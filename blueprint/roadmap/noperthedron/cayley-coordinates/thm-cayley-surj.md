---
declaration: theorem
origin: cited
lean: Cayley.exists_cayleyMatrix_of_trace_nonneg
statement: formalized
proof: formalized
---

# cayley_surj

Every $A \in SO(3)$ with $\operatorname{\mathrm{tr}} A \ge 0$ is $\mathrm{Cay}(r)$ for some $r$ with $|r|^2 \le 3$.

## Depends on

- [cayley_so3](lem-cayley-so3.md)

## Proof

Let $d = 1 + \operatorname{\mathrm{tr}} A > 0$ and let $r = (A_{21} - A_{12},\ A_{02} - A_{20},\ A_{10} - A_{01}) / d$ be the skew part of $A$ divided by $d$. (In terms of the unit quaternion $(q_0, q)$ of $A$, $d = 4 q_0^2$ and $r = q / q_0$.) A rotation satisfies $A A^T = A^T A = I$ and is its own cofactor matrix. These quadratic relations give, by linear combination,

$$
r_0^2 = \frac{1 + A_{00} - A_{11} - A_{22}}{d}, \qquad
r_0 r_1 = \frac{A_{01} + A_{10}}{d},
$$

and the four similar identities for the other squares and products. Hence $|r|^2 = (3 - \operatorname{\mathrm{tr}} A)/d \le 3$ and $D(r) = 4/d$, and substituting the six identities into the entries of $N(r)/D(r)$ gives $A$.

## Lean

Formalized as [`Cayley.exists_cayleyMatrix_of_trace_nonneg`](https://jcreedcmu.github.io/Noperthedron/docs/find/#doc/Cayley.exists_cayleyMatrix_of_trace_nonneg).

## Sources

- [Noperthedron blueprint: chapters/cayley.tex, line 79](https://github.com/jcreedcmu/Noperthedron/blob/0143f65be7f59b3ac09b99debb9c37944a0a2f4b/blueprint/src/chapters/cayley.tex#L79)
