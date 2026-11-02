---
declaration: lemma
origin: cited
lean: ProbabilityTheory.IdentDistrib.rdist_congr
statement: formalized
proof: formalized
---

# Copy preserves Ruzsa distance

If $X',Y'$ are copies of $X,Y$ respectively then $d[X';Y']=d[X ;Y]$.

## Depends on

- [Ruzsa distance](ruz-dist-def.md)

## Proof depends on

- [Copy preserves entropy](copy-ent.md)

## Proof

Immediate from Definitions [Ruzsa distance](ruz-dist-def.md) and [Copy preserves entropy](copy-ent.md).

## Lean

Formalized as [`ProbabilityTheory.IdentDistrib.rdist_congr`](https://teorth.github.io/pfr/docs/find/#doc/ProbabilityTheory.IdentDistrib.rdist_congr).

## Sources

- [Polynomial Freiman-Ruzsa blueprint: chapter/distance.tex, line 104](https://github.com/teorth/pfr/blob/7e7fadf0c4d000fdb21b68505f3fd0e29a6e4a2f/blueprint/src/chapter/distance.tex#L104)
