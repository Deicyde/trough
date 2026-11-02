---
declaration: lemma
origin: cited
lean: rdist_of_neg_le
statement: formalized
proof: formalized
---

# Flipping a sign

If $X,Y$ are $G$-valued, then

$$
d[X ; -Y]  \leq 3 d[X;Y].
$$

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [Copy preserves Ruzsa distance](../../entropic-ruzsa-calculus/part-01/ruz-copy.md)
- [Existence of independent copies](../../entropic-ruzsa-calculus/part-01/independent-exist.md)
- [Existence of conditional independent trials](../../entropic-ruzsa-calculus/part-02/cond-indep-exist.md)
- [Alternate form of submodularity](../../shannon-entropy-inequalities/part-02/alt-submodularity.md)
- [Ruzsa distance in independent case](../../entropic-ruzsa-calculus/part-01/ruz-indep.md)
- [Negation preserves entropy](../../entropic-ruzsa-calculus/part-01/neg-ent.md)
- [Entropy and relabeling](../../shannon-entropy-inequalities/part-01/relabeled-entropy.md)
- [Additivity of entropy](../../shannon-entropy-inequalities/part-02/add-entropy.md)
- [Subadditivity](../../shannon-entropy-inequalities/part-01/subadditive.md)
- [Data processing for a single variable](../data-processing-inequality/data-process-single.md)

## Proof

Without loss of generality (using [Copy preserves Ruzsa distance](../../entropic-ruzsa-calculus/part-01/ruz-copy.md) and [Existence of independent copies](../../entropic-ruzsa-calculus/part-01/independent-exist.md)) we may take $X,Y$ to be independent. By $(X_1,Y_1)$, $(X_2,Y_2)$ be copies of $(X,Y)$ that are conditionally independent over $X_1-Y_1=X_2-Y_2$ (this exists thanks to [Existence of conditional independent trials](../../entropic-ruzsa-calculus/part-02/cond-indep-exist.md)). By [Existence of independent copies](../../entropic-ruzsa-calculus/part-01/independent-exist.md), we can also find another copy $(X_3,Y_3)$ of $(X,Y)$ that is independent of $X_1,Y_1,X_2,Y_2$. From [Alternate form of submodularity](../../shannon-entropy-inequalities/part-02/alt-submodularity.md), one has

$$
\mathbb{H}[X_3-Y_2, X_1-Y_3, X_2, Y_1, X_3, Y_3, X_3+Y_3] + \mathbb{H}[X_3+Y_3] \leq \mathbb{H}[X_3-Y_2, X_1-Y_3, X_2, Y_1, X_3+Y_3] + \mathbb{H}[X_3, Y_3, X_3+Y_3].
$$

From [Ruzsa distance in independent case](../../entropic-ruzsa-calculus/part-01/ruz-indep.md), [Negation preserves entropy](../../entropic-ruzsa-calculus/part-01/neg-ent.md), [Copy preserves Ruzsa distance](../../entropic-ruzsa-calculus/part-01/ruz-copy.md) we have

$$
\mathbb{H}[X_3+Y_3] = \frac{1}{2} \mathbb{H}[X_3] + \frac{1}{2} \mathbb{H}[-Y_3] + d[X_3;-Y_3] = \frac{1}{2} \mathbb{H}[X] + \frac{1}{2} \mathbb{H}[Y] + d[X;-Y].
$$

Since $X_3+Y_3$ is a function of $X_3,Y_3$, we see from [Entropy and relabeling](../../shannon-entropy-inequalities/part-01/relabeled-entropy.md) and [Additivity of entropy](../../shannon-entropy-inequalities/part-02/add-entropy.md) that

$$
\mathbb{H}[X_3,Y_3,X_3+Y_3] = \mathbb{H}[X_3,Y_3] = \mathbb{H}[X,Y] = \mathbb{H}[X]+\mathbb{H}[Y].
$$

Because $X_1-Y_1=X_2-Y_2$, we have

$$
X_3+Y_3 = (X_3-Y_2) - (X_1-Y_3) + (X_2+Y_1)
$$

and thus by [Entropy and relabeling](../../shannon-entropy-inequalities/part-01/relabeled-entropy.md)

$$
\mathbb{H}[X_3-Y_2, X_1-Y_3, X_2, Y_1, X_3+Y_3] = \mathbb{H}[X_3-Y_2, X_1-Y_3, X_2, Y_1]
$$

and hence by [Subadditivity](../../shannon-entropy-inequalities/part-01/subadditive.md)

$$
\mathbb{H}[X_3-Y_2, X_1-Y_3, X_2, Y_1, X_3+Y_3] \leq \mathbb{H}[X_3-Y_2] + \mathbb{H}[X_1-Y_3] + \mathbb{H}[X_2] + \mathbb{H}[Y_1].
$$

Since $X_3,Y_2$ are independent, we see from [Ruzsa distance in independent case](../../entropic-ruzsa-calculus/part-01/ruz-indep.md), [Copy preserves Ruzsa distance](../../entropic-ruzsa-calculus/part-01/ruz-copy.md) that

$$
\mathbb{H}[X_3-Y_2] = \frac{1}{2} \mathbb{H}[X] + \frac{1}{2} \mathbb{H}[Y] + d[X; Y].
$$

Similarly

$$
\mathbb{H}[X_1-Y_3] = \frac{1}{2} \mathbb{H}[X] + \frac{1}{2} \mathbb{H}[Y] + d[X; Y].
$$

We conclude that

$$
\mathbb{H}[X_3-Y_2, X_1-Y_3, X_2, Y_1, X_3+Y_3] \leq 2\mathbb{H}[X] + 2\mathbb{H}[Y] + 2d[X; Y].
$$

Finally, from [Data processing for a single variable](../data-processing-inequality/data-process-single.md) we have

$$
\mathbb{H}[X_1,Y_1,X_2,Y_2,X_3,Y_3] \leq \mathbb{H}[X_3-Y_2, X_1-Y_3, X_2, Y_1, X_3, Y_3, X_3+Y_3].
$$

From [Additivity of entropy](../../shannon-entropy-inequalities/part-02/add-entropy.md) followed by [Entropy of conditionally independent variables](../../shannon-entropy-inequalities/part-02/cond-trial-ent.md), we have

$$
\mathbb{H}[X_1,Y_1,X_2,Y_2,X_3,Y_3] = \mathbb{H}[X_1,Y_1,X_1-Y_1] + \mathbb{H}[X_2,Y_2,X_2-Y_2] - \mathbb{H}[X_1-Y_1] + \mathbb{H}[X_3,Y_3]
$$

and thus by [Ruzsa distance in independent case](../../entropic-ruzsa-calculus/part-01/ruz-indep.md), [Copy preserves Ruzsa distance](../../entropic-ruzsa-calculus/part-01/ruz-copy.md), [Entropy and relabeling](../../shannon-entropy-inequalities/part-01/relabeled-entropy.md), [Additivity of entropy](../../shannon-entropy-inequalities/part-02/add-entropy.md)

$$
\mathbb{H}[X_1,Y_1,X_2,Y_2,X_3,Y_3] = \mathbb{H}[X] + \mathbb{H}[Y] + \mathbb{H}[X] + \mathbb{H}[Y] -\left(\frac{1}{2}\mathbb{H}[X] + \frac{1}{2}\mathbb{H}[Y] + d[X; Y]\right) + \mathbb{H}[X] + \mathbb{H}[Y].
$$

Applying all of these estimates, the claim now follows from linear arithmetic.

## Lean

Formalized as [`rdist_of_neg_le`](https://teorth.github.io/pfr/docs/find/#doc/rdist_of_neg_le).

## Sources

- [Polynomial Freiman-Ruzsa blueprint: chapter/torsion.tex, line 39](https://github.com/teorth/pfr/blob/7e7fadf0c4d000fdb21b68505f3fd0e29a6e4a2f/blueprint/src/chapter/torsion.tex#L39)
