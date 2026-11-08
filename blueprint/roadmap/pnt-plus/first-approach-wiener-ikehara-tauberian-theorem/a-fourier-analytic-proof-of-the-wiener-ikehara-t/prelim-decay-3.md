---
declaration: lemma
origin: cited
lean: prelim_decay_3
statement: formalized
discussion: https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/issues/563
---

# Preliminary decay bound III

If $\psi:\mathbb{R} \to \mathbb{C}$ is absolutely integrable, absolutely continuous, and $\psi'$ is of bounded variation, then

$$
|\hat \psi(u)| \leq \| \psi' \|_{TV} / (2\pi |u|)^2
$$

for all non-zero $u \in \mathbb{R}$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [Preliminary decay bound II](prelim-decay-2.md)

## Proof

Should follow from previous lemma.

## Lean

Stated as [`prelim_decay_3`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/prelim_decay_3); the blueprint does not mark its proof formalized.

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/Wiener.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/127b50e33f6033e2147921167a117af96d9ba4ea/PrimeNumberTheoremAnd/Wiener.lean)
