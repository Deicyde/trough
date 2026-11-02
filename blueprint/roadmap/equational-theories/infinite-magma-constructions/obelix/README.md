# Obelix

Obelix magmas are those satisfying equation 1491, [E1491](https://teorth.github.io/equational_theories/implications/?1491):

$$
x = (y \diamond x) \diamond (y \diamond (y \diamond x))
$$

Obelix is not particularly *structurally* similar to an Asterix, besides their shared resistance to small counterexamples. A related set of ideas can be used to construct an Obelix that does not satisfy some given other equations. The common idea is to define the magma operation

$$
x \diamond y = x + f(y-x) = x + f(h)
$$

on some underlying abelian group. For the case of Obelix, the resulting functional equation is

$$
f(f^{2}(h) - f(h)) = h - f(h)
$$

What differs is how we must proceed in order to satisfy this equation. We again start with a partial function $f$, picking some initial support that will suffice to invalidate the other equation we want to show a nonimplication for. We will progressively add more elements to the support (assuming our group is countable) until the function is total, and we will maintain some invariants:

- [partial-solution2](partial-solution2.md)
- [obelix-extend](obelix-extend.md)
- [corollary-infinite\_magma\_constructions-1](corollary-infinite-magma-constructions-1.md)
