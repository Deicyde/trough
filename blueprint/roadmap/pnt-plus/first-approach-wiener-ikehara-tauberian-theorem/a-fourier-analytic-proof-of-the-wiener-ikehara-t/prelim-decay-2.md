---
declaration: lemma
origin: cited
lean: prelim_decay_2
statement: formalized
discussion: https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/issues/562
---

# Preliminary decay bound II

If $\psi:\mathbb{R} \to \mathbb{C}$ is absolutely integrable and of bounded variation, then

$$
|\hat \psi(u)| \leq \| \psi \|_{TV} / 2\pi |u|
$$

for all non-zero $u \in \mathbb{R}$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof

By Lebesgue–Stiejtes integration by parts we have

$$
2\pi i u \hat \psi(u) = \int _\mathbb{R} e(-tu) d\psi(t)
$$

and the claim then follows from the triangle inequality.

## Lean

Stated as [`prelim_decay_2`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/prelim_decay_2); the blueprint marks no proof of it as formalized.

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/Wiener.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/127b50e33f6033e2147921167a117af96d9ba4ea/PrimeNumberTheoremAnd/Wiener.lean)
