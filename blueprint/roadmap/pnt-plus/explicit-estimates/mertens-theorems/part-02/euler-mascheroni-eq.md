---
declaration: theorem
origin: cited
lean: Mertens.deriv_gamma_add_γ_eq_zero
statement: formalized
proof: formalized
discussion: https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/issues/1320
---

# Compatibility with Mathlib Euler-Mascheroni constant

$\gamma$ is the Euler–Mascheroni constant.

## Depends on

- [Alternate Formula for Euler-Mascheroni constant](../part-01/euler-mascheroni-const-alt.md)

## Proof depends on

- [The remainder term in Mertens second theorem (von Mangoldt form)](../part-01/mertens-second-error-mangoldt.md)
- [limiting behavior of log zeta](log-zeta-limit.md)
- [The remainder term in Mertens first theorem (von Mangoldt form)](../part-01/mertens-first-error-mangoldt.md)
- [Bound for second Mertens error (von Mangoldt form)](mertens-second-error-mangoldt-bound.md)
- [An identity for $\log \zeta(s)$](log-zeta-eq.md)

## Proof

Take limits as $s \to 1$ in the previous asymptotic using known asymptotics for $\zeta(s)$, and using that $- \Gamma'(1)$ is the Euler–Mascheroni constant.

## Lean

Formalized as [`Mertens.deriv_gamma_add_γ_eq_zero`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/Mertens.deriv_gamma_add_γ_eq_zero).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/IEANTN/Mertens.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/127b50e33f6033e2147921167a117af96d9ba4ea/PrimeNumberTheoremAnd/IEANTN/Mertens.lean)
