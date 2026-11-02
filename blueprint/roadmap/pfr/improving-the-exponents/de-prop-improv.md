---
declaration: theorem
origin: cited
lean: tau_strictly_decreases'
statement: formalized
proof: formalized
---

# Improved $\tau$-decrement

Suppose $0 < \eta < 1/8$. Let $X_1, X_2$ be tau-minimizers. Then $d[X_1;X_2] = 0$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [Constructing good variables, III'](averaged-construct-good.md)
- [Bound on distance differences](dist-diff-bound.md)
- [Bound on conditional mutual informations](../entropy-version-of-pfr/endgame/uvw-s.md)

## Proof

From [Constructing good variables, III'](averaged-construct-good.md), [Bound on distance differences](dist-diff-bound.md), and [Bound on conditional mutual informations](../entropy-version-of-pfr/endgame/uvw-s.md) one has

$$
k \leq 8\eta k - \frac{(1 -5 \eta - \frac{4}{6} \eta)(2 \eta k - I_1)}{(1-\eta)}.
$$

For any $\eta < 1/8$, we see from [First estimate](../entropy-version-of-pfr/first-estimate/first-estimate.md) that the expression $\frac{(1 -5 \eta - \frac{4}{6} \eta)(2 \eta k - I_1)}{(1-\eta)}$ is nonnegative, and hence $k = 0$ as required.

## Lean

Formalized as [`tau_strictly_decreases'`](https://teorth.github.io/pfr/docs/find/#doc/tau_strictly_decreases').

## Sources

- [Polynomial Freiman-Ruzsa blueprint: chapter/improved_exponent.tex, line 174](https://github.com/teorth/pfr/blob/7e7fadf0c4d000fdb21b68505f3fd0e29a6e4a2f/blueprint/src/chapter/improved_exponent.tex#L174)
