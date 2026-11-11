---
declaration: lemma
origin: cited
lean: app_ent_PFR
statement: formalized
proof: formalized
---

# app-ent-pfr

Let $G=\mathbb{F}_2^n$ and $\alpha\in (0,1)$ and let $X,Y$ be $G$-valued random variables such that

$$
\mathbb{H}(X)+\mathbb{H}(Y)> \frac{20}{\alpha} d[X;Y].
$$

There is a non-trivial subgroup $H\leq G$ such that

$$
\log \lvert H\rvert \lt \frac{1+\alpha}{2}(\mathbb{H}(X)+\mathbb{H}(Y))
$$

and

$$
\mathbb{H}(\psi(X))+\mathbb{H}(\psi(Y))< \alpha (\mathbb{H}(X)+\mathbb{H}(Y))
$$

where $\psi:G\to G/H$ is the natural projection homomorphism.

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [Improved entropy version of PFR](../improving-the-exponents/entropy-pfr-improv.md)
- [Distance controls entropy difference](../entropic-ruzsa-calculus/part-01/ruzsa-diff.md)
- [Projection entropy and distance](../entropic-ruzsa-calculus/part-01/dist-projection.md)
- [Distance nonnegative](../entropic-ruzsa-calculus/part-01/ruzsa-nonneg.md)

## Proof

By [Improved entropy version of PFR](../improving-the-exponents/entropy-pfr-improv.md) there exists a subgroup $H$ such that $d[X;U_H] + d[Y;U_H] \leq 10 d[X;Y]$. Using [Projection entropy and distance](../entropic-ruzsa-calculus/part-01/dist-projection.md) we deduce that $\mathbb{H}(\psi(X)) + \mathbb{H}(\psi(X)) \leq 20 d[X;Y]$. The second claim follows adding these inequalities and using the assumption on $\mathbb{H}(X)+\mathbb{H}(Y)$.

Furthermore we have by [Distance controls entropy difference](../entropic-ruzsa-calculus/part-01/ruzsa-diff.md)

$$
\log \lvert H \rvert-\mathbb{H}(X)\leq 2d[X;U_H]
$$

and similarly for $Y$ and thus

$$
\begin{aligned}
\log \lvert  H\rvert
&\leq
\frac{\mathbb{H}(X)+\mathbb{H}(Y)}{2}+d[X;U_H] + d[Y;U_H] \leq
\frac{\mathbb{H}(X)+\mathbb{H}(Y)}{2}+ 10d[X;Y]
\\& <
\frac{1+\alpha}{2}(\mathbb{H}(X)+\mathbb{H}(Y)).
\end{aligned}
$$

Finally note that if $H$ were trivial then $\psi(X)=X$ and $\psi(Y)=Y$ and hence $\mathbb{H}(X)+\mathbb{H}(Y)=0$, which contradicts [Distance nonnegative](../entropic-ruzsa-calculus/part-01/ruzsa-nonneg.md).

## Lean

Formalized as [`app_ent_PFR`](https://teorth.github.io/pfr/docs/find/#doc/app_ent_PFR).

## Sources

- [Polynomial Freiman-Ruzsa blueprint: chapter/weak_pfr.tex, line 52](https://github.com/teorth/pfr/blob/1ef23c3c5a83db690fe3b3b5c2e8299fae17b81a/blueprint/src/chapter/weak_pfr.tex#L52)
