---
declaration: lemma
origin: cited
lean: MIPRE.Tailored.canonProg_accepts, MIPRE.Tailored.TailoredVerifier.tgame_accepts_iff
statement: formalized
proof: formalized
---

# The canonical decider decides the $n$-th game

The canonical decider accepts $(n, x, y, a, b)$ exactly when the four runs of $\mathcal{L}$ and the run of $\mathcal{P}$ halt and the check passes on their outputs. So, at questions $x, y$ of the $n$-th game $\mathsf{V}_n$, it accepts $(a, b)$ exactly when $\mathsf{V}_n$ does.

## Depends on

- [The canonical decider, as a program; II:1757–1787](def-canonical-decider.md)

## Proof

A run of a sequence of steps is a run of each step, the model being deterministic, and the polynomial-time pieces compute what they are meant to. For the second part: when the five runs halt, their outputs are the lengths and the constraints that $\mathsf{V}_n$ is read from. When one of them does not halt, $\mathsf{V}_n$ has at that edge the constraint list $\{J\}$, which no answer pair satisfies, and the canonical decider does not halt, which is a rejection.

## Lean

Formalized as [`MIPRE.Tailored.canonProg_accepts`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.canonProg_accepts), [`MIPRE.Tailored.TailoredVerifier.tgame_accepts_iff`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.TailoredVerifier.tgame_accepts_iff).

## Sources

- [MIP* = RE blueprint: content/09_tailored.tex, line 388](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/09_tailored.tex#L388)
