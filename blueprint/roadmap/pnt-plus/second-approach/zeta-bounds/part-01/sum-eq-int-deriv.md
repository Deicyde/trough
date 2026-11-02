---
declaration: lemma
origin: cited
lean: sum_eq_int_deriv
statement: formalized
proof: formalized
---

# sum-eq-int-deriv

Let $a < b$, and let $\phi$ be continuously differentiable on $[a, b]$. Then

$$
\sum_{a < n \le b} \phi(n) = \int_a^b \phi(x) \, dx
+ \left(\lfloor b \rfloor + \frac{1}{2} - b\right) \phi(b)
- \left(\lfloor a \rfloor + \frac{1}{2} - a\right) \phi(a)
- \int_a^b \left(\lfloor x \rfloor + \frac{1}{2} - x\right) \phi'(x) \, dx.
$$

## Depends on

Its statement uses no other node of the blueprint.

## Proof

This is first order Euler-Maclaurin.

## Lean

Formalized as [`sum_eq_int_deriv`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/sum_eq_int_deriv).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/ZetaBounds.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/127b50e33f6033e2147921167a117af96d9ba4ea/PrimeNumberTheoremAnd/ZetaBounds.lean)
