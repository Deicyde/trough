# The Bernstein bound

On $[-1, 1]$ a quadratic $a_0 + a_1 t + a_2 t^2$ equals $b_0 \beta_0(t) + b_1 \beta_1(t) + b_2 \beta_2(t)$ with

$$
(b_0, b_1, b_2) = (a_0 - a_1 + a_2,\ a_0 - a_2,\ a_0 + a_1 + a_2),\qquad
\beta_0 = \Bigl(\frac{1 - t}{2}\Bigr)^2,\ \beta_1 = \frac{1 - t^2}{2},\ \beta_2 = \Bigl(\frac{1 + t}{2}\Bigr)^2.
$$

The $\beta_\kappa$ are nonnegative on $[-1, 1]$ and sum to $1$.

- [bernstein](def-bernstein.md)
- [Bernstein bound](thm-bern-bound.md)

Neither bound dominates the other (for $p = t^2$ the coefficient bound is $0$ and the Bernstein bound is $-1$), but on the gap polynomials the Bernstein bound is usually much sharper; using it in addition halved the number of leaves in the certificate. It costs more to compute, so the checker tries the coefficient bound first.
