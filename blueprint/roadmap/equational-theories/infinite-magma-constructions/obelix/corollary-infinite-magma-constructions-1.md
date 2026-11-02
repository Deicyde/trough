---
declaration: corollary
origin: cited
---

# corollary-infinite\_magma\_constructions-1

There is an Obelix magma that is not Asterix (equation 65).

## Depends on

- [Equation 65](../../selected-laws/part-02/eq65.md)
- [Equation 1491](../../selected-laws/part-02/eq1491.md)
- [obelix-extend](obelix-extend.md)

## Proof

This requires picking an initial set that still satisfies the correct initial closure properties. Letting $x_1$, $x_2$, $x_3$ and $x_4$ be independent elements, then taking the function

$$
\{(0,0), (x_1,x_2), (x_2-x_1, x_3), (x_1+x_3, x_4)\}
$$

already has elements that contradict the Asterix equation, and it's a valid partial solution. By extending it, we can get an Obelix that does not satisfy the Asterix equation.

## Sources

- [Equational Theories blueprint: chapter/infinite_magma_constructions.tex, line 254](https://github.com/teorth/equational_theories/blob/2ddb16c4c4c036242ad3e18167579b57cac2a006/blueprint/src/chapter/infinite_magma_constructions.tex#L254)
