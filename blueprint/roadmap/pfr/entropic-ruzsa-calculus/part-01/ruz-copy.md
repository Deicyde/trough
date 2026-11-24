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

- [Polynomial Freiman-Ruzsa blueprint: chapter/distance.tex, line 104](https://github.com/teorth/pfr/blob/1899ce8ed95fc310cce53d4c7ecfa2beb20ebec4/blueprint/src/chapter/distance.tex#L104)
