---
declaration: corollary
origin: cited
lean: auto_cheby
statement: formalized
proof: formalized
---

# auto-cheby

One has

$$
\sum_{n \leq x} f(n) = O(x)
$$

for all $x \geq 1$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [second-fourier](../a-fourier-analytic-proof-of-the-wiener-ikehara-t/second-fourier.md)
- [first-fourier](../a-fourier-analytic-proof-of-the-wiener-ikehara-t/first-fourier.md)
- [crude-upper-bound](crude-upper-bound.md)
- [Wiener-Ikehara Theorem (1)](../a-fourier-analytic-proof-of-the-wiener-ikehara-t/wienerikehara.md)

## Proof

By applying Corollary [crude-upper-bound](crude-upper-bound.md) for a specific compactly supported function $\psi$, one can obtain a bound of the form $\sum_{(1-\varepsilon)x < n \leq x} f(n) = O(x)$ for all $x$ and some absolute constant $\varepsilon$ (which can be made explicit).

If $C$ is a sufficiently large constant, the claim $|\sum_{n \leq x} f(n)| \leq Cx$ can now be proven by strong induction on $x$, as the claim for $(1-\varepsilon)x$ implies the claim for $x$ by the triangle inequality (and the claim is trivial for $x < 1$).

## Lean

Formalized as [`auto_cheby`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/auto_cheby).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/Wiener.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/127b50e33f6033e2147921167a117af96d9ba4ea/PrimeNumberTheoremAnd/Wiener.lean)
