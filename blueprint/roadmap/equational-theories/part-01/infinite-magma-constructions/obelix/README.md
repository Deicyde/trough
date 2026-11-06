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
f(f^{2}(h) - f(h)) = h - f(h)\qquad\text{(1)}
$$

What differs is how we must proceed in order to satisfy this equation. We again start with a partial function $f$, picking some initial support that will suffice to invalidate the other equation we want to show a nonimplication for. We will progressively add more elements to the support (assuming our group is countable) until the function is total, and we will maintain some invariants:

It's easiest to work over the group of finitely supported functions from $\mathbb{N}$ (or any other countable set) to $\mathbb{Z}$. When picking fresh elements, it's important not only to take something outside of the group closure of the elements already in $f$, but actually out of their $\mathbb{Q}$-span, because we need guarantees that the fresh element $g$ doesn't satisfy relations like $2g = x$ as well.

Any partial solution can be extended to a complete solution.

The actual mechanical proof requires checking roughly a few dozen statements of the form "the fresh element is not related linearly to the existing elements". Each is individually obvious, and easily discharged.

By picking an appropriate partial solution, we can then show that there are Obelix magmas that are not Asterix.
