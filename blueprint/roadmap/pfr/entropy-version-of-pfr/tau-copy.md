---
declaration: lemma
origin: cited
lean: ProbabilityTheory.IdentDistrib.tau_eq
statement: formalized
proof: formalized
---

# $\tau$ depends only on distribution

If $X'_1, X'_2$ are copies of $X_1,X_2$, then $\tau[X'_1;X'_2] = \tau[X_1;X_2]$.

## Depends on

- [$\tau$ functional](tau-def.md)

## Proof depends on

- [Copy preserves entropy](../entropic-ruzsa-calculus/part-01/copy-ent.md)

## Proof

Immediate from [Copy preserves entropy](../entropic-ruzsa-calculus/part-01/copy-ent.md).

## Lean

Formalized as [`ProbabilityTheory.IdentDistrib.tau_eq`](https://teorth.github.io/pfr/docs/find/#doc/ProbabilityTheory.IdentDistrib.tau_eq).

## Sources

- [Polynomial Freiman-Ruzsa blueprint: chapter/entropy_pfr.tex, line 17](https://github.com/teorth/pfr/blob/1ef23c3c5a83db690fe3b3b5c2e8299fae17b81a/blueprint/src/chapter/entropy_pfr.tex#L17)
