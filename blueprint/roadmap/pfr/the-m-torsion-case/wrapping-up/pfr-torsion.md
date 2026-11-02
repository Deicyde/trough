---
declaration: theorem
origin: cited
lean: torsion_PFR
statement: formalized
proof: formalized
---

# PFR

Suppose that $G$ is an abelian group of torsion $m$ (not necessarily finite). If $A \subset G$ is a finite non-empty set with $|A+A| \leq K|A|$, then $A$ can be covered by at most $mK^{256m^3+1}$ translates of a finite subspace $H$ of $G$ with $|H| \leq |A|$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [pfr\_aux\_torsion](pfr-aux-torsion.md)

## Proof

If $G$ is finite, repeat the proof of [PFR](../../proof-of-pfr/pfr.md), but with [Lemma pfr\_aux\_torsion](pfr-aux-torsion.md) in place of [Lemma pfr\_aux](../../proof-of-pfr/pfr-aux.md). In general, reduce to the finite span of $A$ over $\mathrm{Z}/m\mathrm{Z}$.

## Lean

Formalized as [`torsion_PFR`](https://teorth.github.io/pfr/docs/find/#doc/torsion_PFR).

## Sources

- [Polynomial Freiman-Ruzsa blueprint: chapter/torsion.tex, line 892](https://github.com/teorth/pfr/blob/7e7fadf0c4d000fdb21b68505f3fd0e29a6e4a2f/blueprint/src/chapter/torsion.tex#L892)
