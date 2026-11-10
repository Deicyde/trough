---
declaration: lemma
origin: cited
lean: PFR_projection'
statement: formalized
proof: formalized
---

# pfr-projection'

If $G=\mathbb{F}_2^d$ and $\alpha\in (0,1)$ and $X,Y$ are $G$-valued random variables then there is a subgroup $H\leq \mathbb{F}_2^d$ such that

$$
\log \lvert H\rvert \leq \frac{1+\alpha}{2(1-\alpha)} (\mathbb{H}(X)+\mathbb{H}(Y))
$$

and if $\psi:G \to G/H$ is the natural projection then

$$
\mathbb{H}(\psi(X))+\mathbb{H}(\psi(Y))\leq \frac{20}{\alpha} d[\psi(X);\psi(Y)].
$$

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [app-ent-pfr](app-ent-pfr.md)

## Proof

Let $H\leq \mathbb{F}_2^d$ be a maximal subgroup such that

$$
\mathbb{H}(\psi(X))+\mathbb{H}(\psi(Y))> \frac{20}{\alpha} d[\psi(X);\psi(Y)]
$$

and such that there exists $c \ge 0$ with

$$
\log \lvert H\rvert \leq \frac{1+\alpha}{2(1-\alpha)}(1-c)(\mathbb{H}(X)+\mathbb{H}(Y))
$$

and

$$
\mathbb{H}(\psi(X))+\mathbb{H}(\psi(Y))\leq c (\mathbb{H}(X)+\mathbb{H}(Y)).
$$

Note that this exists since $H=\{0\}$ is an example of such a subgroup or we are done with this choice of $H$.

We know that $G/H$ is a $2$-elementary group and so by Lemma [app-ent-pfr](app-ent-pfr.md) there exists some non-trivial subgroup $H'\leq G/H$ such that

$$
\log \lvert H'\rvert < \frac{1+\alpha}{2}(\mathbb{H}(\psi(X))+\mathbb{H}(\psi(Y))
$$

and

$$
\mathbb{H}(\psi' \circ\psi(X))+\mathbb{H}(\psi' \circ \psi(Y))< \alpha(\mathbb{H}(\psi(X))+\mathbb{H}(\psi(Y)))
$$

where $\psi':G/H\to (G/H)/H'$. By group isomorphism theorems we know that there exists some $H''$ with $H\leq H''\leq G$ such that $H'\cong H''/H$ and $\psi' \circ \psi(X)=\psi''(X)$ where $\psi'':G\to G/H''$ is the projection homomorphism.

Since $H'$ is non-trivial we know that $H$ is a proper subgroup of $H''$. On the other hand we know that

$$
\log \lvert H''\rvert=\log \lvert H'\rvert+\log \lvert H\rvert< \frac{1+\alpha}{2(1-\alpha)}(1-\alpha c)(\mathbb{H}(X)+\mathbb{H}(Y))
$$

and

$$
\mathbb{H}(\psi''(X))+\mathbb{H}(\psi''(Y))< \alpha (\mathbb{H}(\psi(X))+\mathbb{H}(\psi(Y)))\leq \alpha c (\mathbb{H}(X)+\mathbb{H}(Y)).
$$

Therefore (using the maximality of $H$) it must be the first condition that fails, whence

$$
\mathbb{H}(\psi''(X))+\mathbb{H}(\psi''(Y))\leq \frac{20}{\alpha}d[\psi''(X);\psi''(Y)].
$$

## Lean

Formalized as [`PFR_projection'`](https://teorth.github.io/pfr/docs/find/#doc/PFR_projection').

## Sources

- [Polynomial Freiman-Ruzsa blueprint: chapter/weak_pfr.tex, line 86](https://github.com/teorth/pfr/blob/1ef23c3c5a83db690fe3b3b5c2e8299fae17b81a/blueprint/src/chapter/weak_pfr.tex#L86)
