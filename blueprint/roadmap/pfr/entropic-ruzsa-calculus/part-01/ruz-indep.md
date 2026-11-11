---
declaration: lemma
origin: cited
lean: ProbabilityTheory.IndepFun.rdist_eq
statement: formalized
proof: formalized
---

# Ruzsa distance in independent case

If $X,Y$ are independent $G$-random variables then

$$
d[X ;Y] := \mathbb{H}[X - Y] - \mathbb{H}[X]/2 - \mathbb{H}[Y]/2.
$$

## Depends on

- [Ruzsa distance](ruz-dist-def.md)

## Proof depends on

- [Entropy and relabeling](../../shannon-entropy-inequalities/part-01/relabeled-entropy.md)
- [Copy preserves entropy](copy-ent.md)

## Proof

Immediate from [Ruzsa distance](ruz-dist-def.md) and Lemmas [Entropy and relabeling](../../shannon-entropy-inequalities/part-01/relabeled-entropy.md), [Copy preserves entropy](copy-ent.md).

## Lean

Formalized as [`ProbabilityTheory.IndepFun.rdist_eq`](https://teorth.github.io/pfr/docs/find/#doc/ProbabilityTheory.IndepFun.rdist_eq).

## Sources

- [Polynomial Freiman-Ruzsa blueprint: chapter/distance.tex, line 113](https://github.com/teorth/pfr/blob/1ef23c3c5a83db690fe3b3b5c2e8299fae17b81a/blueprint/src/chapter/distance.tex#L113)
