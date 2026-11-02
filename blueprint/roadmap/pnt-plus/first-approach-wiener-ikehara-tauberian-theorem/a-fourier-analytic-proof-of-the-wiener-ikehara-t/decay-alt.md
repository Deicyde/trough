---
declaration: lemma
origin: cited
lean: decay_alt
statement: formalized
proof: formalized
discussion: https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/issues/564
---

# Decay bound, alternate form

If $\psi:\mathbb{R} \to \mathbb{C}$ is absolutely integrable, absolutely continuous, and $\psi'$ is of bounded variation, then

$$
|\hat \psi(u)| \leq ( \|\psi\|_1 + \| \psi' \|_{TV} / (2\pi)^2) / (1+|u|^2)
$$

for all $u \in \mathbb{R}$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [Preliminary decay bound III](prelim-decay-3.md)
- [Decay bounds](decay.md)
- [Preliminary decay bound I](prelim-decay.md)

## Proof

Should follow from previous lemmas.

## Lean

Formalized as [`decay_alt`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/decay_alt).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/Wiener.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/127b50e33f6033e2147921167a117af96d9ba4ea/PrimeNumberTheoremAnd/Wiener.lean)
