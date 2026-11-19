---
declaration: lemma
origin: cited
mathlib: true
mathlib_declaration: IsCompactSystem.infClosure
---

# IsCompactSystem.infClosure

If $S$ is a compact system, then $S^{\cap f}$ is a compact system.

## Depends on

- [IsCompactSystem](def-iscompactsystem.md)
- [infClosure](def-infclosure.md)

## Proof depends on

- [IsCompactSystem.mono](lem-iscompactsystem-mono.md)

## Proof

$S_\delta$ is a compact system by Lemma [IsCompactSystem.countableInfClosure](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/debut.tex#L179), and $S^{\cap f} \subseteq S_\delta$, so we can apply Lemma [IsCompactSystem.mono](lem-iscompactsystem-mono.md).

## Lean

Formalized as [`IsCompactSystem.infClosure`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/IsCompactSystem.infClosure).

## Sources

- [Brownian motion blueprint: chapters/debut.tex, line 189](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/debut.tex#L189)
