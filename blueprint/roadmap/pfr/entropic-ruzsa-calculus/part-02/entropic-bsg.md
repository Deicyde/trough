---
declaration: lemma
origin: cited
lean: ent_bsg
statement: formalized
proof: formalized
---

# Balog-Szemerédi-Gowers

Let $A,B$ be $G$-valued random variables on $\Omega$, and set $Z := A+B$. Then

$$
\sum_{z}  \mathbb{P}[Z=z] d[(A | Z = z); (B | Z = z)] \leq 3  \mathbb{I}[A:B] + 2 \mathbb{H}[Z] - \mathbb{H}[A] - \mathbb{H}[B].\qquad\text{(2)}
$$

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [Existence of conditional independent trials](cond-indep-exist.md)
- [Entropy of conditionally independent variables](../../shannon-entropy-inequalities/part-02/cond-trial-ent.md)
- [Conditional entropy](../../shannon-entropy-inequalities/part-01/conditional-entropy-def.md)
- [Submodularity](../../shannon-entropy-inequalities/part-01/submodularity.md)
- [Copy preserves entropy](../part-01/copy-ent.md)
- [Entropy and relabeling](../../shannon-entropy-inequalities/part-01/relabeled-entropy.md)
- [Additivity of entropy](../../shannon-entropy-inequalities/part-02/add-entropy.md)
- [Ruzsa distance in independent case](../part-01/ruz-indep.md)

## Proof

Let $(A_1, B_1)$ and $(A_2, B_2)$ (and $Z'$, which by abuse of notation we call $Z$) be conditionally independent trials of $(A,B)$ relative to $Z$ as produced by [Existence of conditional independent trials](cond-indep-exist.md), thus $(A_1,B_1)$ and $(A_2,B_2)$ are coupled through the random variable $A_1 + B_1 = A_2 + B_2$, which by abuse of notation we shall also call $Z$.

Observe from [Ruzsa distance in independent case](../part-01/ruz-indep.md) that the left-hand side of (2) is

$$
\mathbb{H}[A_1 - B_2| Z] - \mathbb{H}[A_1 | Z]/2 - \mathbb{H}[B_2 | Z]/2.\qquad\text{(3)}
$$

since, crucially, $(A_1 | Z=z)$ and $(B_2 | Z=z)$ are independent for all $z$.

Applying submodularity ([Alternate form of submodularity](../../shannon-entropy-inequalities/part-02/alt-submodularity.md)) gives

$$
\begin{split}
&\mathbb{H}[A_1 - B_2] + \mathbb{H}[A_1 - B_2, A_1, B_1] \\
&\qquad \leq \mathbb{H}[A_1 - B_2, A_1] + \mathbb{H}[A_1 - B_2,B_1].
\end{split}\qquad\text{(4)}
$$

We estimate the second, third and fourth terms appearing here. First note that, by [Entropy of conditionally independent variables](../../shannon-entropy-inequalities/part-02/cond-trial-ent.md) and [Entropy and relabeling](../../shannon-entropy-inequalities/part-01/relabeled-entropy.md) (noting that the tuple $(A_1 - B_2, A_1, B_1)$ determines the tuple $(A_1, A_2, B_1, B_2)$ since $A_1+B_1=A_2+B_2$)

$$
\mathbb{H}[A_1 - B_2, A_1, B_1] = \mathbb{H}[A_1, B_1, A_2, B_2,Z] = 2\mathbb{H}[A,B] - \mathbb{H}[Z].\qquad\text{(5)}
$$

Next observe that

$$
\mathbb{H}[A_1 - B_2, A_1] = \mathbb{H}[A_1, B_2] \leq \mathbb{H}[A] + \mathbb{H}[B].\qquad\text{(6)}
$$

Finally, we have

$$
\mathbb{H}[A_1 - B_2, B_1] = \mathbb{H}[A_2 - B_1, B_1] = \mathbb{H}[A_2, B_1] \leq \mathbb{H}[A] + \mathbb{H}[B].\qquad\text{(7)}
$$

Substituting (5), (6) and (7) into (4) yields

$$
\mathbb{H}[A_1 - B_2] \leq 2 \mathbb{I}[A:B] + \mathbb{H}[Z]
$$

and so by [Conditioning reduces entropy](../../shannon-entropy-inequalities/part-01/cond-reduce.md)

$$
\mathbb{H}[A_1 - B_2 | Z]  \leq 2 \mathbb{I}[A:B] + \mathbb{H}[Z].
$$

Since

$$
\begin{aligned} \mathbb{H}[A_1 | Z] & = \mathbb{H}[A_1, A_1 + B_1] - \mathbb{H}[Z] \\ & = \mathbb{H}[A,B] - \mathbb{H}[Z] \\ & = \mathbb{H}[Z] -  \mathbb{I}[A:B] - 2 \mathbb{H}[Z]- \mathbb{H}[A]-\mathbb{H}[B]\end{aligned}
$$

and similarly for $\mathbb{H}[B_2 | Z]$, we see that (3) is bounded by $3 \mathbb{I}[A:B] + 2\mathbb{H}[Z]-\mathbb{H}[A]-\mathbb{H}[B]$ as claimed.

## Lean

Formalized as [`ent_bsg`](https://teorth.github.io/pfr/docs/find/#doc/ent_bsg).

## Sources

- [Polynomial Freiman-Ruzsa blueprint: chapter/distance.tex, line 266](https://github.com/teorth/pfr/blob/1ef23c3c5a83db690fe3b3b5c2e8299fae17b81a/blueprint/src/chapter/distance.tex#L266)
