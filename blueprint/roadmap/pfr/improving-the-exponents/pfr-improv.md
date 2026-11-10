---
declaration: theorem
origin: cited
lean: PFR_conjecture_improv
statement: formalized
proof: formalized
---

# Improved PFR

If $A \subset {\bf F}_2^n$ is non-empty and $|A+A| \leq K|A|$, then $A$ can be covered by most $2K^{11}$ translates of a subspace $H$ of ${\bf F}_2^n$ with $|H| \leq |A|$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [pfr_aux-improv](pfr-aux-improv.md)

## Proof

By repeating the proof of [PFR](../proof-of-pfr/pfr.md) and using [Lemma pfr_aux-improv](pfr-aux-improv.md) one obtains $2K^{11}$ in place of $2K^{12}$.

## Lean

Formalized as [`PFR_conjecture_improv`](https://teorth.github.io/pfr/docs/find/#doc/PFR_conjecture_improv).

## Sources

- [Polynomial Freiman-Ruzsa blueprint: chapter/improved_exponent.tex, line 229](https://github.com/teorth/pfr/blob/7e7fadf0c4d000fdb21b68505f3fd0e29a6e4a2f/blueprint/src/chapter/improved_exponent.tex#L229)
