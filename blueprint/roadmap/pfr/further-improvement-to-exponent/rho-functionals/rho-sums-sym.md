---
declaration: lemma
origin: cited
lean: rho_of_sum_le
statement: formalized
proof: formalized
---

# Rho and sums, symmetrized

If $X,Y$ are independent, then

$$
\rho(X+Y) \leq \frac{1}{2}(\rho(X)+\rho(Y) + d[X;Y]).
$$

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [Rho and sums](rho-sums.md)

## Proof

Apply [Rho and sums](rho-sums.md) for $(X,Y)$ and $(Y,X)$ and take their average.

## Lean

Formalized as [`rho_of_sum_le`](https://teorth.github.io/pfr/docs/find/#doc/rho_of_sum_le).

## Sources

- [Polynomial Freiman-Ruzsa blueprint: chapter/further_improvement.tex, line 195](https://github.com/teorth/pfr/blob/1ef23c3c5a83db690fe3b3b5c2e8299fae17b81a/blueprint/src/chapter/further_improvement.tex#L195)
