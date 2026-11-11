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
(x \diamond x) \diamond y = y \diamond x.\qquad\text{(1)}
$$

Specializing to $y=x \diamond x$, we conclude

$$
(x \diamond x) \diamond (x \diamond x) = (x \diamond x) \diamond x
$$

and hence by another application of [E387](https://teorth.github.io/equational_theories/implications/?387) we see that $x \diamond x$ is idempotent:

$$
(x \diamond x) \diamond (x \diamond x) = x \diamond x.\qquad\text{(2)}
$$

Now, replacing $x$ by $x \diamond x$ in (1) and then using (2) we see that

$$
(x \diamond x) \diamond y = y \diamond (x \diamond x)
$$

so in particular $x \diamond x$ commutes with $y \diamond y$:

$$
(x \diamond x) \diamond (y \diamond y) = (y \diamond y) \diamond (x \diamond x).\qquad\text{(3)}
$$

Also, from two applications of (1) one has

$$
(x \diamond x) \diamond (y \diamond y) = (y \diamond y) \diamond x = x \diamond y.
$$

Thus (3) simplifies to $x \diamond y = y \diamond x$, which is [E43](https://teorth.github.io/equational_theories/implications/?43).

## Lean

Formalized as [`Subgraph.Equation387_implies_Equation43`](https://teorth.github.io/equational_theories/docs/find/#doc/Subgraph.Equation387_implies_Equation43).

## Sources

- [Equational Theories blueprint: chapter/implications.tex, line 5](https://github.com/teorth/equational_theories/blob/8b87204d5b201e1cf6c69b8dcabb0558109bee00/blueprint/src/chapter/implications.tex#L5)
