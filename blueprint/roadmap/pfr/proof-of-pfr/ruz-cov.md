---
declaration: lemma
origin: cited
lean: Finset.ruzsa_covering_add
statement: formalized
proof: formalized
---

# Ruzsa covering lemma

If $A,B$ are finite non-empty subsets of a group $G$, then $A$ can be covered by at most $|A+B|/|B|$ translates of $B-B$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof

Cover $A$ greedily by disjoint translates of $B$.

## Lean

Formalized as [`Finset.ruzsa_covering_add`](https://teorth.github.io/pfr/docs/find/#doc/Finset.ruzsa_covering_add).

## Sources

- [Polynomial Freiman-Ruzsa blueprint: chapter/pfr.tex, line 3](https://github.com/teorth/pfr/blob/1899ce8ed95fc310cce53d4c7ecfa2beb20ebec4/blueprint/src/chapter/pfr.tex#L3)
