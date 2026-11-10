---
declaration: lemma
origin: cited
lean: condRho_of_sum_le
statement: formalized
proof: formalized
---

# Rho and conditioning, symmetrized

If $X,Y$ are independent, then

$$
\rho(X | X+Y) \leq \frac{1}{2}(\rho(X)+\rho(Y) + d[X;Y]).
$$

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [Rho invariant](rho-invariant.md)
- [Rho and conditioning](rho-cond.md)

## Proof

First apply [Rho and conditioning](rho-cond.md) to get $\rho(X|X+Y)\le \rho(X) + \frac{1}{2}(\mathbb{H}[X+Y]-\mathbb{H}[Y])$, and $\rho(Y|X+Y)\le \rho(Y)+\frac{1}{2}(\mathbb{H}[X+Y]-\mathbb{H}[X])$. Then apply [Rho invariant](rho-invariant.md) to get $\rho(Y|X+Y)=\rho(X|X+Y)$ and take the average of the two inequalities.

## Lean

Formalized as [`condRho_of_sum_le`](https://teorth.github.io/pfr/docs/find/#doc/condRho_of_sum_le).

## Sources

- [Polynomial Freiman-Ruzsa blueprint: chapter/further_improvement.tex, line 203](https://github.com/teorth/pfr/blob/1ef23c3c5a83db690fe3b3b5c2e8299fae17b81a/blueprint/src/chapter/further_improvement.tex#L203)
