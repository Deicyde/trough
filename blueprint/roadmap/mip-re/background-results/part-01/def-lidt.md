---
declaration: definition
origin: cited
lean: MIPRE.LIDT.lidtGame
statement: formalized
---

# Canonical-line low individual degree test

Let $\mathbb{F}$ be a finite field with $q$ elements and let $m \geq 1$ and $d$ be integers. The *$(m,q,d)$-low individual degree test* is the two-player game in which the verifier picks one of the following three sub-tests with probability $\tfrac13$ each, having sampled a uniform point $u \sim \mathbb{F}^m$.

1. **Axis-parallel lines test.** Sample a uniform direction $i \sim [m]$ and a uniform role. One player receives the line $\ell = \{u + t e_i\}$ and answers a univariate polynomial $f$ of degree at most $d$; the other receives $u$ and answers $a \in \mathbb{F}$. Accept if $f(u) = a$.
2. **Self-consistency test.** Both players receive $u$ and answer elements of $\mathbb{F}$. Accept if the answers are equal.
3. **Diagonal lines test.** Sample a uniform $j \sim [m]$, a uniform direction $v \in \mathbb{F}^m$ whose coordinates after the $j$-th vanish, and a uniform role. One player receives the line $\ell = \{u + t v\}$ and answers a univariate polynomial of degree at most $md$; the other receives $u$ and answers $a \in \mathbb{F}$. Accept if $f(u) = a$.

## Depends on

- [Nonlocal game](../../foundations/part-01/def-game.md)

## Lean

Formalized as [`MIPRE.LIDT.lidtGame`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LIDT.lidtGame).

## Sources

- [MIP* = RE blueprint: content/03_background_results.tex, line 568](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/03_background_results.tex#L568)
