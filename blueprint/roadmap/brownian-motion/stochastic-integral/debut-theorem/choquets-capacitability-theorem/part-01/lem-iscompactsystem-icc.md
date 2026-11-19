---
declaration: lemma
origin: cited
lean: isCompactSystem_Icc
statement: formalized
proof: formalized
---

# isCompactSystem_Icc

The family of closed compact intervals of $\mathbb{R}$ is a compact system.

## Depends on

- [IsCompactSystem](def-iscompactsystem.md)

## Proof depends on

- [isCompactSystem_isCompact](lem-iscompactsystem-iscompact.md)
- [IsCompactSystem.mono](lem-iscompactsystem-mono.md)

## Proof

The family of closed compact intervals of $\mathbb{R}$ is a family of compact sets, so it is a compact system by Lemma [isCompactSystem_isCompact](lem-iscompactsystem-iscompact.md) and [IsCompactSystem.mono](lem-iscompactsystem-mono.md).

## Lean

Formalized as [`isCompactSystem_Icc`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/isCompactSystem_Icc).

## Sources

- [Brownian motion blueprint: chapters/debut.tex, line 120](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/debut.tex#L120)
