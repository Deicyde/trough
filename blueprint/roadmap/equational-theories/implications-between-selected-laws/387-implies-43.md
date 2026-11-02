---
declaration: theorem
origin: cited
lean: Subgraph.Equation387_implies_Equation43
statement: formalized
proof: formalized
---

# 387 implies 43

[E387](https://teorth.github.io/equational_theories/implications/?387) $({x \diamond y = (y \diamond y) \diamond x})$ implies [E43](https://teorth.github.io/equational_theories/implications/?43) $({x \diamond y = y \diamond x})$.

## Depends on

- [Equation 387](../selected-laws/part-02/eq387.md)
- [Equation 43](../selected-laws/part-01/eq43.md)

## Proof

(From [MathOverflow](https://mathoverflow.net/a/450905/766)). By [E387](https://teorth.github.io/equational_theories/implications/?387), one has the law

$$
(x \diamond x) \diamond y = y \diamond x.
$$

Specializing to $y=x \diamond x$, we conclude

$$
(x \diamond x) \diamond (x \diamond x) = (x \diamond x) \diamond x
$$

and hence by another application of [E387](https://teorth.github.io/equational_theories/implications/?387) we see that $x \diamond x$ is idempotent:

$$
(x \diamond x) \diamond (x \diamond x) = x \diamond x.
$$

Now, replacing $x$ by $x \diamond x$ in (387-again) and then using (idem) we see that

$$
(x \diamond x) \diamond y = y \diamond (x \diamond x)
$$

so in particular $x \diamond x$ commutes with $y \diamond y$:

$$
(x \diamond x) \diamond (y \diamond y) = (y \diamond y) \diamond (x \diamond x).
$$

Also, from two applications of (387-again) one has

$$
(x \diamond x) \diamond (y \diamond y) = (y \diamond y) \diamond x = x \diamond y.
$$

Thus (op-idem) simplifies to $x \diamond y = y \diamond x$, which is [E43](https://teorth.github.io/equational_theories/implications/?43).

## Lean

Formalized as [`Subgraph.Equation387_implies_Equation43`](https://teorth.github.io/equational_theories/docs/find/#doc/Subgraph.Equation387_implies_Equation43).

## Sources

- [Equational Theories blueprint: chapter/implications.tex, line 5](https://github.com/teorth/equational_theories/blob/2ddb16c4c4c036242ad3e18167579b57cac2a006/blueprint/src/chapter/implications.tex#L5)
