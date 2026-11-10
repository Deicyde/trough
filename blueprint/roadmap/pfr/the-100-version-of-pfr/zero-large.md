---
declaration: lemma
origin: cited
lean: sub_mem_symmGroup
statement: formalized
proof: formalized
---

# Zero Ruzsa distance implies large symmetry group

If $X$ is a $G$-valued random variable such that $d[X ;X]=0$, and $x,y \in G$ are such that $P[X=x], P[X=y]>0$, then $x-y \in \mathrm{Sym}[X]$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [Ruzsa distance in independent case](../entropic-ruzsa-calculus/part-01/ruz-indep.md)
- [Copy preserves Ruzsa distance](../entropic-ruzsa-calculus/part-01/ruz-copy.md)
- [Conditional entropy and relabeling](../shannon-entropy-inequalities/part-01/relabeled-entropy-cond.md)
- [Vanishing of mutual information](../shannon-entropy-inequalities/part-02/vanish-entropy.md)
- [Alternative formulae for mutual information](../shannon-entropy-inequalities/part-01/alternative-mutual.md)
- [Existence of independent copies](../entropic-ruzsa-calculus/part-01/independent-exist.md)
- [Symmetry group](sym-group-def.md)

## Proof

Let $X_1,X_2$ be independent copies of $X$ (from [Existence of independent copies](../entropic-ruzsa-calculus/part-01/independent-exist.md)). Let $A$ denote the range of $X$. From [Ruzsa distance in independent case](../entropic-ruzsa-calculus/part-01/ruz-indep.md) and [Copy preserves Ruzsa distance](../entropic-ruzsa-calculus/part-01/ruz-copy.md) we have

$$
\mathbb{H}[X_1-X_2] = \mathbb{H}[X_1].
$$

Observe from [Conditional entropy and relabeling](../shannon-entropy-inequalities/part-01/relabeled-entropy-cond.md) that

$$
\mathbb{H}[X_1-X_2|X_2] = \mathbb{H}[X_1|X_2] = \mathbb{H}[X_1]
$$

and hence by [Alternative formulae for mutual information](../shannon-entropy-inequalities/part-01/alternative-mutual.md)

$$
\mathbb{I}[X_1-X_2 : X_1] = 0.
$$

By [Vanishing of mutual information](../shannon-entropy-inequalities/part-02/vanish-entropy.md), $X_1-X_2$ and $X_1$ are therefore independent, thus the law of $(X_1-X_2|X_1=x)$ does not depend on $x \in A$. The claim follows.

## Lean

Formalized as [`sub_mem_symmGroup`](https://teorth.github.io/pfr/docs/find/#doc/sub_mem_symmGroup).

## Sources

- [Polynomial Freiman-Ruzsa blueprint: chapter/100_percent.tex, line 16](https://github.com/teorth/pfr/blob/1ef23c3c5a83db690fe3b3b5c2e8299fae17b81a/blueprint/src/chapter/100_percent.tex#L16)
