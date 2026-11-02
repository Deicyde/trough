---
declaration: lemma
origin: cited
lean: PFR_projection
statement: formalized
proof: formalized
---

# pfr-projection

If $G=\mathbb{F}_2^d$ and $\alpha\in (0,1)$ and $X,Y$ are $G$-valued random variables then there is a subgroup $H\leq \mathbb{F}_2^d$ such that

$$
\log \lvert H\rvert \leq 2 (\mathbb{H}(X)+\mathbb{H}(Y))
$$

and if $\psi:G \to G/H$ is the natural projection then

$$
\mathbb{H}(\psi(X))+\mathbb{H}(\psi(Y))\leq 34 d[\psi(X);\psi(Y)].
$$

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [pfr-projection'](pfr-projection.md)

## Proof

Specialize [Lemma pfr-projection'](pfr-projection.md) to $\alpha=3/5$. In the second inequality, it gives a bound $100/3 < 34$.

## Lean

Formalized as [`PFR_projection`](https://teorth.github.io/pfr/docs/find/#doc/PFR_projection).

## Sources

- [Polynomial Freiman-Ruzsa blueprint: chapter/weak_pfr.tex, line 127](https://github.com/teorth/pfr/blob/7e7fadf0c4d000fdb21b68505f3fd0e29a6e4a2f/blueprint/src/chapter/weak_pfr.tex#L127)
