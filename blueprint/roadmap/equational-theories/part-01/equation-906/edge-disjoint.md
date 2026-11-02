---
declaration: corollary
origin: cited
---

# Edge disjointness of left cycles

For any integer $n$,

$$
L_y x = L_z x \implies L_y^{n} x = L_z^{n} x.
$$

## Depends on

Its statement uses no other node of the blueprint.

## Proof

This is trivial for $n=0,1$, and $n=-1$ follows from [(3)](README.md). Observe that if the claim holds for $n=0,-1,\dots,-m$ for any $m \geq 1$ then it also holds for $n=-m-1$. Finally, since there is a common period to all the $L_y$ by finiteness (or Legendre's theorem), the set of $n$ for which the claim holds is periodic. The claim follows.

## Sources

- [Equational Theories blueprint: chapter/906.tex, line 16](https://github.com/teorth/equational_theories/blob/2ddb16c4c4c036242ad3e18167579b57cac2a006/blueprint/src/chapter/906.tex#L16)
