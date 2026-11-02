---
declaration: theorem
origin: cited
lean: Mertens.E₃.abs_le, Mertens.E₃.bound, Mertens.E₃.bound', Mertens.E₃.bound'', Mertens.E₃.bound'''
statement: formalized
proof: formalized
discussion: https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/issues/1330
---

# Mertens' third theorem error bound

For any $x \geq 2$, one has

$$
E_3(x) = O\left(\frac{1}{\log x}\right)
$$

## Depends on

- [The remainder term in Mertens third theorem](mertens-third-error.md)

## Proof depends on

- [The remainder term in Mertens second theorem (von Mangoldt form)](../part-01/mertens-second-error-mangoldt.md)
- [Alternate Formula for Euler-Mascheroni constant](../part-01/euler-mascheroni-const-alt.md)
- [Formula for Meissel-Mertens constant](meissel-mertens-eq.md)
- [Bound for second error (prime form)](mertens-second-error-prime-abs-le.md)
- [The remainder term in Mertens first theorem (von Mangoldt form)](../part-01/mertens-first-error-mangoldt.md)
- [The Meissel-Mertens constant](meissel-mertens-constant.md)
- [Compatibility with Mathlib Euler-Mascheroni constant](euler-mascheroni-eq.md)
- [Mertens' third theorem error term](mertens-third-theorem-error.md)

## Proof

Estimating the error in [Formula for Meissel-Mertens constant](meissel-mertens-eq.md) using the first order Taylor expansion of log one gets

$$
\sum_{p \le x}(\log (1-1/p)+1/p) = (M - \gamma) + O(1/x).
$$

The result follows by combining with [Bound for second error (prime form)](mertens-second-error-prime-abs-le.md).

## Lean

Formalized as [`Mertens.E₃.abs_le`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/Mertens.E₃.abs_le), [`Mertens.E₃.bound`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/Mertens.E₃.bound), [`Mertens.E₃.bound'`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/Mertens.E₃.bound'), [`Mertens.E₃.bound''`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/Mertens.E₃.bound''), [`Mertens.E₃.bound'''`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/Mertens.E₃.bound''').

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/IEANTN/Mertens.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/127b50e33f6033e2147921167a117af96d9ba4ea/PrimeNumberTheoremAnd/IEANTN/Mertens.lean)
