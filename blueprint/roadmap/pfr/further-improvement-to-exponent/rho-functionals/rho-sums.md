---
declaration: lemma
origin: cited
lean: rhoMinus_of_sum, rhoPlus_of_sum, rho_of_sum
statement: formalized
proof: formalized
---

# Rho and sums

If $X,Y$ are independent, one has

$$
\rho^-(X+Y) \leq \rho^-(X)
$$

$$
\rho^+(X+Y) \leq \rho^+(X) + \mathbb{H}[X+Y] - \mathbb{H}[X]
$$

and

$$
\rho(X+Y) \leq \rho(X) + \frac{1}{2}( \mathbb{H}[X+Y] - \mathbb{H}[X] ).
$$

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [Kullback–Leibler and sums](../kullback-leibler-divergence/kl-sums.md)

## Proof

The first inequality follows from [Kullback–Leibler and sums](../kullback-leibler-divergence/kl-sums.md). The second and third inequalities are direct corollaries of the first.

## Lean

Formalized as [`rhoMinus_of_sum`](https://teorth.github.io/pfr/docs/find/#doc/rhoMinus_of_sum), [`rhoPlus_of_sum`](https://teorth.github.io/pfr/docs/find/#doc/rhoPlus_of_sum), [`rho_of_sum`](https://teorth.github.io/pfr/docs/find/#doc/rho_of_sum).

## Sources

- [Polynomial Freiman-Ruzsa blueprint: chapter/further_improvement.tex, line 149](https://github.com/teorth/pfr/blob/7e7fadf0c4d000fdb21b68505f3fd0e29a6e4a2f/blueprint/src/chapter/further_improvement.tex#L149)
