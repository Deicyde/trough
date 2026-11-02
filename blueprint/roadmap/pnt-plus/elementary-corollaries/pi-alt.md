---
declaration: corollary
origin: cited
lean: pi_alt
statement: formalized
proof: formalized
---

# pi-alt

One has

$$
\pi(x) = (1+o(1)) \frac{x}{\log x}
$$

as $x \to \infty$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [pi-asymp](pi-asymp.md)

## Proof

An integration by parts gives

$$
\int_2^x \frac{dt}{\log t} = \frac{x}{\log x} - \frac{2}{\log 2} +
\int_2^x \frac{dt}{\log^2 t}.
$$

We have the crude bounds

$$
\int_2^{\sqrt{x}} \frac{dt}{\log^2 t} = O( \sqrt{x} )
$$

and

$$
\int_{\sqrt{x}}^x \frac{dt}{\log^2 t} = O( \frac{x}{\log^2 x} )
$$

and combining all this we obtain

$$
\int_2^x \frac{dt}{\log t} = \frac{x}{\log x} + O( \frac{x}{\log^2 x} )
$$

$$
= (1+o(1)) \frac{x}{\log x}
$$

and the claim then follows from Theorem [pi-asymp](pi-asymp.md).

## Lean

Formalized as [`pi_alt`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/pi_alt).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/Consequences.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/127b50e33f6033e2147921167a117af96d9ba4ea/PrimeNumberTheoremAnd/Consequences.lean)
