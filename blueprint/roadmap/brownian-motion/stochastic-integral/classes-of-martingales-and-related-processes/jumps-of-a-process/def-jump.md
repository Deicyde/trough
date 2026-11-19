---
declaration: definition
origin: cited
lean: Function.jump
statement: formalized
---

# Jumps of a process

The jumps of a process $X : T \to \Omega \to E$ is the process $\Delta X : T \to \Omega \to E$ defined by $(t, \omega) \mapsto X_t(\omega) - X_{t^-}(\omega)$ .

## Depends on

Its statement uses no other node of the blueprint.

## Lean

Formalized as [`Function.jump`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/Function.jump).

## Sources

- [Brownian motion blueprint: chapters/martingale_classes.tex, line 21](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/martingale_classes.tex#L21)
