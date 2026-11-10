---
declaration: lemma
origin: cited
lean: torsion_free_doubling
statement: formalized
proof: formalized
---

# torsion-free-doubling

If $G$ is torsion-free and $X,Y$ are $G$-valued random variables then $d[X;2Y]\leq 5d[X;Y]$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [Alternate form of submodularity](../shannon-entropy-inequalities/part-02/alt-submodularity.md)
- [Ruzsa triangle inequality](../entropic-ruzsa-calculus/part-01/ruzsa-triangle.md)
- [Distance controls entropy difference](../entropic-ruzsa-calculus/part-01/ruzsa-diff.md)

## Proof

Let $Y_1,Y_2$ be independent copies of $Y$ (also independent of $X$). Since $G$ is torsion-free we know $X,Y_1-Y_2,X-2Y_1$ uniquely determine $X,Y_1,Y_2$ and so

$$
\mathbb{H}(X,Y_1,Y_2,X-2Y_1)=\mathbb{H}(X,Y_1,Y_2)=\mathbb{H}(X)+2\mathbb{H}(Y).
$$

Similarly

$$
\mathbb{H}(X,X-2Y_1)=\mathbb{H}(X)+\mathbb{H}(2Y_1)=\mathbb{H}(X)+\mathbb{H}(Y).
$$

Furthermore

$$
\mathbb{H}(Y_1-Y_2,X-2Y_1)=\mathbb{H}(Y_1-Y_2,X-Y_1-Y_2)\leq \mathbb{H}(Y_1-Y_2)+\mathbb{H}(X-Y_1-Y_2).
$$

By submodularity ([Alternate form of submodularity](../shannon-entropy-inequalities/part-02/alt-submodularity.md))

$$
\mathbb{H}(X,Y_1,Y_2,X-2Y_1)+\mathbb{H}(X-2Y_1)\leq \mathbb{H}(X,X-2Y_1)+\mathbb{H}(Y_1-Y_2,X-2Y_1).
$$

Combining these inequalities

$$
\mathbb{H}(X-2Y_1)\leq \mathbb{H}(Y_1-Y_2)+\mathbb{H}(X-Y_1-Y_2)-\mathbb{H}(Y).
$$

Similarly we have

$$
\mathbb{H}(Y_1,Y_2,X-Y_1-Y_2)=\mathbb{H}(X)+2\mathbb{H}(Y),
$$

$$
\mathbb{H}(Y_1,X-Y_1-Y_2)=\mathbb{H}(Y)+\mathbb{H}(X-Y_2),
$$

and

$$
\mathbb{H}(Y_2,X-Y_1-Y_2)=\mathbb{H}(Y)+\mathbb{H}(X-Y_1)
$$

and by submodularity ([Alternate form of submodularity](../shannon-entropy-inequalities/part-02/alt-submodularity.md)) again

$$
\mathbb{H}(Y_1,Y_2,X-Y_1-Y_2)+ \mathbb{H}(X-Y_1-Y_2)\leq \mathbb{H}(Y_1,X-Y_1-Y_2)+\mathbb{H}(Y_2,X-Y_1-Y_2).
$$

Combining these inequalities (and recalling the definition of Ruzsa distance) gives

$$
\mathbb{H}(X-Y_1-Y_2)\leq \mathbb{H}(X-Y_1)+\mathbb{H}(X-Y_2)-\mathbb{H}(X)=2d[X;Y]+\mathbb{H}(Y).
$$

It follows that

$$
\mathbb{H}(X-2Y_1)\leq \mathbb{H}(Y_1-Y_2)+2d[X;Y]
$$

and so (using $\mathbb{H}(2Y)=\mathbb{H}(Y)$)

$$
\begin{aligned}
d[X;2Y]
&=\mathbb{H}(X-2Y_1)-\mathbb{H}(X)/2-\mathbb{H}(2Y)/2\\
&\leq \mathbb{H}(Y_1-Y_2)+2d[X;Y]-\mathbb{H}(X)/2-\mathbb{H}(Y)/2\\
&= d[Y_1;Y_2]+\frac{\mathbb{H}(Y)-\mathbb{H}(X)}{2}+2d[X;Y].
\end{aligned}
$$

Finally note that by the triangle inequality ([Ruzsa triangle inequality](../entropic-ruzsa-calculus/part-01/ruzsa-triangle.md)) we have

$$
d[Y_1;Y_2]\leq d[Y_1;X]+d[X;Y_2]=2d[X;Y].
$$

The result follows from $(\mathbb{H}(Y)-\mathbb{H}(X))/2\leq d[X;Y]$ ([Distance controls entropy difference](../entropic-ruzsa-calculus/part-01/ruzsa-diff.md)).

## Lean

Formalized as [`torsion_free_doubling`](https://teorth.github.io/pfr/docs/find/#doc/torsion_free_doubling).

## Sources

- [Polynomial Freiman-Ruzsa blueprint: chapter/weak_pfr.tex, line 3](https://github.com/teorth/pfr/blob/1ef23c3c5a83db690fe3b3b5c2e8299fae17b81a/blueprint/src/chapter/weak_pfr.tex#L3)
