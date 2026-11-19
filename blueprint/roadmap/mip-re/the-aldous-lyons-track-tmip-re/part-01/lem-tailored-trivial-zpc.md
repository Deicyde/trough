---
declaration: lemma
origin: cited
lean: MIPRE.Tailored.PermStrategy.trivial, MIPRE.Tailored.PermStrategy.trivial_proj, MIPRE.Tailored.hasPerfectZPC_of_accepts_zero
statement: formalized
proof: formalized
---

# The trivial strategy; II:1148

A tailored game that accepts the all-zero answers at every question pair of positive weight has a perfect ZPC strategy: in dimension $1$, every observable the identity.

## Depends on

- [Z-aligned permutation strategies commuting along edges; II:1043–1057, II:1279–1283](def-zpc-strategy.md)

## Proof

Every observable is the identity, which is a signed permutation matrix, diagonal and an involution, and commutes with everything. Each factor $\frac12({I} + (-1)^{a_X}{I})$ is ${I}$ at $a_X = 0$ and $0$ at $a_X = 1$, so $P^x_a$ is $1$ at $a = 0$ and $0$ elsewhere, and the value is $\sum_{x, y} \mu(x, y) = 1$. This is the case of the halting protocol in which the machine has halted (II:1978), and it shows that the definitions are not vacuous.

## Lean

Formalized as [`MIPRE.Tailored.PermStrategy.trivial`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.PermStrategy.trivial), [`MIPRE.Tailored.PermStrategy.trivial_proj`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.PermStrategy.trivial_proj), [`MIPRE.Tailored.hasPerfectZPC_of_accepts_zero`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.hasPerfectZPC_of_accepts_zero).

## Sources

- [MIP* = RE blueprint: content/09_tailored.tex, line 140](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/09_tailored.tex#L140)
