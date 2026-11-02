---
declaration: lemma
origin: cited
lean: ProbabilityTheory.max_entropy_sub_mutualInfo_le_entropy_add, ProbabilityTheory.max_entropy_sub_mutualInfo_le_entropy_sub
statement: formalized
proof: formalized
---

# Lower bound of sumset

If $X,Y$ are $G$-valued random variables on $\Omega$, we have

$$
\max(\mathbb{H}[X], \mathbb{H}[Y]) -  \mathbb{I}[X:Y] \leq \mathbb{H}[X \pm Y].
$$

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [Conditioning reduces entropy](../../shannon-entropy-inequalities/part-01/cond-reduce.md)
- [Alternative formulae for mutual information](../../shannon-entropy-inequalities/part-01/alternative-mutual.md)
- [Shearing preserves entropy](shear-ent.md)
- [Negation preserves entropy](neg-ent.md)

## Proof

By [Conditioning reduces entropy](../../shannon-entropy-inequalities/part-01/cond-reduce.md), [Shearing preserves entropy](shear-ent.md), [Alternative formulae for mutual information](../../shannon-entropy-inequalities/part-01/alternative-mutual.md), [Negation preserves entropy](neg-ent.md) we have

$$
\mathbb{H}[X\pm Y] \geq \mathbb{H}[X\pm Y|Y] = \mathbb{H}[X|Y]= \mathbb{H}[X] -  \mathbb{I}[X:Y]
$$

and similarly with the roles of $X,Y$ reversed, giving the claim.

## Lean

Formalized as [`ProbabilityTheory.max_entropy_sub_mutualInfo_le_entropy_add`](https://teorth.github.io/pfr/docs/find/#doc/ProbabilityTheory.max_entropy_sub_mutualInfo_le_entropy_add), [`ProbabilityTheory.max_entropy_sub_mutualInfo_le_entropy_sub`](https://teorth.github.io/pfr/docs/find/#doc/ProbabilityTheory.max_entropy_sub_mutualInfo_le_entropy_sub).

## Sources

- [Polynomial Freiman-Ruzsa blueprint: chapter/distance.tex, line 23](https://github.com/teorth/pfr/blob/7e7fadf0c4d000fdb21b68505f3fd0e29a6e4a2f/blueprint/src/chapter/distance.tex#L23)
