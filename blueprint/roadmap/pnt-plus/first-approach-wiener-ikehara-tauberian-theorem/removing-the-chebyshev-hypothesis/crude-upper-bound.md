---
declaration: corollary
origin: cited
lean: crude_upper_bound
statement: formalized
proof: formalized
---

# crude-upper-bound

If $\psi: \mathbb{R} \to \mathbb{C}$ is $C^2$ and compactly supported with $f$ and $\hat \psi$ non-negative, then there exists a constant $B$ such that

$$
|\sum_{n=1}^\infty \frac{f(n)}{n} \hat \psi( \frac{1}{2\pi} \log \frac{n}{x} )| \leq B
$$

for all $x > 0$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [limiting-fourier-variant](limiting-fourier-variant.md)

## Proof

This readily follows from the previous lemma and the triangle inequality.

## Lean

Formalized as [`crude_upper_bound`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/crude_upper_bound).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/Wiener.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/a4fb6989b07e9c76b511807ae93e33e25b820e9b/PrimeNumberTheoremAnd/Wiener.lean)
