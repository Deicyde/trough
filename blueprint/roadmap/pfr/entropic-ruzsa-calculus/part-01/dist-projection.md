---
declaration: lemma
origin: cited
lean: ent_of_proj_le
statement: formalized
proof: formalized
---

# Projection entropy and distance

If $G$ is an additive group and $X$ is a $G$-valued random variable and $H\leq G$ is a finite subgroup then, with $\pi:G\to G/H$ the natural homomorphism we have (where $U_H$ is uniform on $H$)

$$
\mathbb{H}(\pi(X))\leq 2d[X;U_H].
$$

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [Existence of independent copies](independent-exist.md)
- [Distance controls entropy difference](ruzsa-diff.md)
- [Chain rule](../../shannon-entropy-inequalities/part-01/chain-rule.md)
- [Shearing preserves entropy](shear-ent.md)
- [Submodularity](../../shannon-entropy-inequalities/part-01/submodularity.md)
- [Jensen bound](../../shannon-entropy-inequalities/part-01/jensen-bound.md)

## Proof

WLOG, we make $X$, $U_H$ independent ([Existence of independent copies](independent-exist.md)). Now by Lemmas [Submodularity](../../shannon-entropy-inequalities/part-01/submodularity.md), [Shearing preserves entropy](shear-ent.md), [Jensen bound](../../shannon-entropy-inequalities/part-01/jensen-bound.md)

$$
\begin{aligned}
&\mathbb{H}(X-U_H|\pi(X)) \geq \mathbb{H}(X-U_H|X) &= \mathbb{H}(U_H) \\
&\mathbb{H}(X-U_H|\pi(X)) \leq \log |H| &= \mathbb{H}(U_H)
\end{aligned}
$$

By [Chain rule](../../shannon-entropy-inequalities/part-01/chain-rule.md)

$$
\mathbb{H}(X-U_H)=\mathbb{H}(\pi(X))+\mathbb{H}(X-U_H|\pi(X))=\mathbb{H}(\pi(X))+\mathbb{H}(U_H)
$$

and therefore

$$
d[X;U_H]=\mathbb{H}(\pi(X))+\frac{\mathbb{H}(U_H)-\mathbb{H}(X)}{2}.
$$

Furthermore by [Distance controls entropy difference](ruzsa-diff.md)

$$
d[X;U_H]\geq \frac{\lvert \mathbb{H}(X)-\mathbb{H}(U_H)\rvert}{2}.
$$

Adding these inequalities gives the result.

## Lean

Formalized as [`ent_of_proj_le`](https://teorth.github.io/pfr/docs/find/#doc/ent_of_proj_le).

## Sources

- [Polynomial Freiman-Ruzsa blueprint: chapter/distance.tex, line 166](https://github.com/teorth/pfr/blob/7e7fadf0c4d000fdb21b68505f3fd0e29a6e4a2f/blueprint/src/chapter/distance.tex#L166)
