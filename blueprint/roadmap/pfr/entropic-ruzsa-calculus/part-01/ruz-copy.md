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

- [Polynomial Freiman-Ruzsa blueprint: chapter/distance.tex, line 104](https://github.com/teorth/pfr/blob/1ef23c3c5a83db690fe3b3b5c2e8299fae17b81a/blueprint/src/chapter/distance.tex#L104)
