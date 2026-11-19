---
declaration: lemma
origin: cited
mathlib: true
mathlib_declaration: isCompactSystem_isCompact
---

# isCompactSystem_isCompact

The family of compact sets of a T2 topological space is a compact system.

## Depends on

- [IsCompactSystem](def-iscompactsystem.md)

## Proof depends on

- [isCompactSystem_isCompact_isClosed](lem-iscompactsystem-iscompact-isclosed.md)

## Proof

The T2 assumption ensures that compact sets are closed, so the family of compact sets is the family of compact closed sets, which is a compact system by Lemma [isCompactSystem_isCompact_isClosed](lem-iscompactsystem-iscompact-isclosed.md).

## Lean

Formalized as [`isCompactSystem_isCompact`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/isCompactSystem_isCompact).

## Sources

- [Brownian motion blueprint: chapters/debut.tex, line 94](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/debut.tex#L94)
