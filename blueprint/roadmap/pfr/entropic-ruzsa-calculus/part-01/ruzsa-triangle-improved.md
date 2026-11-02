---
declaration: lemma
origin: cited
lean: ent_of_diff_le
statement: formalized
proof: formalized
---

# Improved Ruzsa triangle inequality

If $X,Y,Z$ are $G$-valued random variables on $\Omega$ with $(X,Y)$ independent of $Z$, then

$$
\mathbb{H}[X - Y] \leq \mathbb{H}[X-Z] + \mathbb{H}[Z-Y] - \mathbb{H}[Z]
$$

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [Alternate form of submodularity](../../shannon-entropy-inequalities/part-02/alt-submodularity.md)
- [Subadditivity](../../shannon-entropy-inequalities/part-01/subadditive.md)
- [Entropy and relabeling](../../shannon-entropy-inequalities/part-01/relabeled-entropy.md)
- [Additivity of entropy](../../shannon-entropy-inequalities/part-02/add-entropy.md)

## Proof

Apply [Alternate form of submodularity](../../shannon-entropy-inequalities/part-02/alt-submodularity.md) to obtain

$$
\mathbb{H}[X - Z, X - Y] + \mathbb{H}[Y, X - Y] \geq \mathbb{H}[X - Z, Y, X - Y] + \mathbb{H}[X - Y].
$$

Using

$$
\mathbb{H}[X - Z, X - Y] \leq \mathbb{H}[X - Z] + \mathbb{H}[Y - Z]
$$

(from [Entropy and relabeling](../../shannon-entropy-inequalities/part-01/relabeled-entropy.md), [Subadditivity](../../shannon-entropy-inequalities/part-01/subadditive.md)),

$$
\mathbb{H}[Y, X - Y] = \mathbb{H}[X, Y]
$$

(from [Entropy and relabeling](../../shannon-entropy-inequalities/part-01/relabeled-entropy.md)), and

$$
\mathbb{H}[X - Z, Y, X - Y] = \mathbb{H}[X, Y, Z] = \mathbb{H}[X, Y] + \mathbb{H}[Z]
$$

(from [Entropy and relabeling](../../shannon-entropy-inequalities/part-01/relabeled-entropy.md) and [Additivity of entropy](../../shannon-entropy-inequalities/part-02/add-entropy.md)) and rearranging, we indeed obtain (submod-explicit).

## Lean

Formalized as [`ent_of_diff_le`](https://teorth.github.io/pfr/docs/find/#doc/ent_of_diff_le).

## Sources

- [Polynomial Freiman-Ruzsa blueprint: chapter/distance.tex, line 187](https://github.com/teorth/pfr/blob/7e7fadf0c4d000fdb21b68505f3fd0e29a6e4a2f/blueprint/src/chapter/distance.tex#L187)
