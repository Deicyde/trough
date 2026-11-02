---
declaration: lemma
origin: cited
lean: decay_bounds
statement: formalized
proof: formalized
---

# Decay bounds

If $\psi:\mathbb{R} \to \mathbb{C}$ is $C^2$ and obeys the bounds

$$
|\psi(t)|, |\psi''(t)| \leq A / (1 + |t|^2)
$$

for all $t \in \mathbb{R}$, then

$$
|\hat \psi(u)| \leq C A / (1+|u|^2)
$$

for all $u \in \mathbb{R}$, where $C$ is an absolute constant.

## Depends on

Its statement uses no other node of the blueprint.

## Proof

From two integration by parts we obtain the identity

$$
(1+u^2) \hat \psi(u) = \int_{\bf R} (\psi(t) - \frac{u}{4\pi^2} \psi''(t)) e(-tu)\ dt.
$$

Now apply the triangle inequality and the identity $\int_{\bf R} \frac{dt}{1+t^2}\ dt = \pi$ to obtain the claim with $C = \pi + 1 / 4 \pi$.

## Lean

Formalized as [`decay_bounds`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/decay_bounds).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/Wiener.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/127b50e33f6033e2147921167a117af96d9ba4ea/PrimeNumberTheoremAnd/Wiener.lean)
