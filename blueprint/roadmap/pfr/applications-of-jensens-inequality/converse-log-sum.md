---
declaration: lemma
origin: cited
lean: Real.sum_mul_log_div_eq_iff
statement: formalized
proof: formalized
---

# converse log sum

If equality holds in [log sum inequality](log-sum.md), then $a_s=r\cdot b_s$ for every $s\in S$, for some constant $r\in \mathbb{R}$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [Concavity](concave.md)

## Proof

By the fact that $h$ is strictly concave and the equality condition of Jensen.

## Lean

Formalized as [`Real.sum_mul_log_div_eq_iff`](https://teorth.github.io/pfr/docs/find/#doc/Real.sum_mul_log_div_eq_iff).

## Sources

- [Polynomial Freiman-Ruzsa blueprint: chapter/jensen.tex, line 24](https://github.com/teorth/pfr/blob/1ef23c3c5a83db690fe3b3b5c2e8299fae17b81a/blueprint/src/chapter/jensen.tex#L24)
