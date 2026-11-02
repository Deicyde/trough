---
declaration: theorem
origin: cited
lean: better_PFR_conjecture
statement: formalized
proof: formalized
---

# PFR with $C=9$

If $A \subset {\bf F}_2^n$ is finite non-empty with $|A+A| \leq K|A|$, then there exists a subgroup $H$ of ${\bf F}_2^n$ with $|H| \leq |A|$ such that $A$ can be covered by at most $2K^9$ translates of $H$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [pfr-9-aux'](pfr-9-aux-2.md)
- [Ruzsa covering lemma](../../proof-of-pfr/ruz-cov.md)

## Proof

Given [Corollary pfr-9-aux'](pfr-9-aux-2.md), the proof is the same as that of [PFR](../../proof-of-pfr/pfr.md).

## Lean

Formalized as [`better_PFR_conjecture`](https://teorth.github.io/pfr/docs/find/#doc/better_PFR_conjecture).

## Sources

- [Polynomial Freiman-Ruzsa blueprint: chapter/further_improvement.tex, line 376](https://github.com/teorth/pfr/blob/7e7fadf0c4d000fdb21b68505f3fd0e29a6e4a2f/blueprint/src/chapter/further_improvement.tex#L376)
