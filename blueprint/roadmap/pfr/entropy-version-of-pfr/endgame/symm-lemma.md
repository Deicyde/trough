---
declaration: lemma
origin: cited
lean: I₃_eq
statement: formalized
proof: formalized
---

# Symmetry identity

We have

$$
I(U:W | S) = I(V:W | S).
$$

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [Copy preserves entropy](../../entropic-ruzsa-calculus/part-01/copy-ent.md)
- [Alternate formula for conditional mutual information](../../shannon-entropy-inequalities/part-02/conditional-mutual-alt.md)
- [Chain rule](../../shannon-entropy-inequalities/part-01/chain-rule.md)

## Proof

This should follow from [Copy preserves entropy](../../entropic-ruzsa-calculus/part-01/copy-ent.md), [Alternate formula for conditional mutual information](../../shannon-entropy-inequalities/part-02/conditional-mutual-alt.md), and [Chain rule](../../shannon-entropy-inequalities/part-01/chain-rule.md).

## Lean

Formalized as [`I₃_eq`](https://teorth.github.io/pfr/docs/find/#doc/I₃_eq).

## Sources

- [Polynomial Freiman-Ruzsa blueprint: chapter/entropy_pfr.tex, line 245](https://github.com/teorth/pfr/blob/1ef23c3c5a83db690fe3b3b5c2e8299fae17b81a/blueprint/src/chapter/entropy_pfr.tex#L245)
