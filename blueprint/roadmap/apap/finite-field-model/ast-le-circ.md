---
declaration: lemma
origin: cited
lean: cLpNorm_conv_le_cLpNorm_dconv
statement: formalized
proof: formalized
---

# ast_le_circ

For any function $f:G\to \mathbb{C}$ and integer $k\geq 1$

$$
\| f\ast f\|_{2k}\leq \| f\circ f\|_{2k}.
$$

## Depends on

Its statement uses no other node of the blueprint.

## Proof

To finish, similar trick to unbalancing.

## Lean

Formalized as [`cLpNorm_conv_le_cLpNorm_dconv`](https://yaeldillies.github.io/apap/docs/find/#doc/cLpNorm_conv_le_cLpNorm_dconv).

## Sources

- [Kelley-Meka bound blueprint: chapter/ff.tex, line 63](https://github.com/YaelDillies/apap/blob/b401f6e22417e6dbe6f87d6620571ea6c513aed3/blueprint/src/chapter/ff.tex#L63)
