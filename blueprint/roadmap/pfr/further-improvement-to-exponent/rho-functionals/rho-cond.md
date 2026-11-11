---
declaration: lemma
origin: cited
lean: condRhoMinus_le, condRhoPlus_le, condRho_le
statement: formalized
proof: formalized
---

# Rho and conditioning

If $X,Z$ are defined on the same space, one has

$$
\rho^-(X|Z) \leq \rho^-(X) + \mathbb{H}[X] - \mathbb{H}[X|Z]
$$

$$
\rho^+(X|Z) \leq \rho^+(X)
$$

and

$$
\rho(X|Z) \leq \rho(X) + \frac{1}{2}( \mathbb{H}[X] - \mathbb{H}[X|Z] ).
$$

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [Kullback–Leibler and conditioning](../kullback-leibler-divergence/kl-cond.md)

## Proof

The first inequality follows from [Kullback–Leibler and conditioning](../kullback-leibler-divergence/kl-cond.md). The second and third inequalities are direct corollaries of the first.

## Lean

Formalized as [`condRhoMinus_le`](https://teorth.github.io/pfr/docs/find/#doc/condRhoMinus_le), [`condRhoPlus_le`](https://teorth.github.io/pfr/docs/find/#doc/condRhoPlus_le), [`condRho_le`](https://teorth.github.io/pfr/docs/find/#doc/condRho_le).

## Sources

- [Polynomial Freiman-Ruzsa blueprint: chapter/further_improvement.tex, line 181](https://github.com/teorth/pfr/blob/1ef23c3c5a83db690fe3b3b5c2e8299fae17b81a/blueprint/src/chapter/further_improvement.tex#L181)
