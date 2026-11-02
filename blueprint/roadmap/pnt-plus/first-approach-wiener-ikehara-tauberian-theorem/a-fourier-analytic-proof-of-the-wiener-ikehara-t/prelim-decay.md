---
declaration: lemma
origin: cited
lean: prelim_decay
statement: formalized
proof: formalized
discussion: https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/issues/561
---

# Preliminary decay bound I

If $\psi:\mathbb{R} \to \mathbb{C}$ is absolutely integrable then

$$
|\hat \psi(u)| \leq \| \psi \|_1
$$

for all $u \in \mathbb{R}$. where $C$ is an absolute constant.

## Depends on

Its statement uses no other node of the blueprint.

## Proof

Immediate from the triangle inequality.

## Lean

Formalized as [`prelim_decay`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/prelim_decay).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/Wiener.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/127b50e33f6033e2147921167a117af96d9ba4ea/PrimeNumberTheoremAnd/Wiener.lean)
