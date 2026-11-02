---
declaration: proposition
origin: cited
lean: tau_minimizer_exists
statement: formalized
proof: formalized
---

# $\tau$ has minimum

A pair $X_1, X_2$ of $\tau$-minimizers exist.

## Depends on

- [$\tau$-minimizer](tau-min-def.md)

## Proof depends on

- [$\tau$ depends only on distribution](tau-copy.md)

## Proof

By [$\tau$ depends only on distribution](tau-copy.md), $\tau$ only depends on the probability distributions of $X_1, X_2$. This ranges over a compact space, and $\tau$ is continuous. So $\tau$ has a minimum.

## Lean

Formalized as [`tau_minimizer_exists`](https://teorth.github.io/pfr/docs/find/#doc/tau_minimizer_exists).

## Sources

- [Polynomial Freiman-Ruzsa blueprint: chapter/entropy_pfr.tex, line 36](https://github.com/teorth/pfr/blob/7e7fadf0c4d000fdb21b68505f3fd0e29a6e4a2f/blueprint/src/chapter/entropy_pfr.tex#L36)
