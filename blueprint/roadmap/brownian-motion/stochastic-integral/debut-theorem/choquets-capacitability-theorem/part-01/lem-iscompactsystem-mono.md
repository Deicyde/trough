---
declaration: lemma
origin: cited
mathlib: true
mathlib_declaration: IsCompactSystem.mono
---

# IsCompactSystem.mono

If $S \subseteq T$ and $T$ is a compact system, then $S$ is a compact system.

## Depends on

- [IsCompactSystem](def-iscompactsystem.md)

## Proof

Any sequence of sets in $S$ is a sequence of sets in $T$, so if the intersection of the sequence is empty, then there is a finite subset of the sequence whose intersection is empty by the compact system property of $T$.

## Lean

Formalized as [`IsCompactSystem.mono`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/IsCompactSystem.mono).

## Sources

- [Brownian motion blueprint: chapters/debut.tex, line 107](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/debut.tex#L107)
