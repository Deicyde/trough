# The Asterix equation

Over translation-invariant magmas, equational laws simplify to univariate functional equations.

For instance, writing $x = y+h$, we have

$$
y \diamond x = x + f(h)
$$

$$
x \diamond (y \diamond x) = x + f(h) + f^2(h)
$$

$$
y \diamond (x \diamond (y \diamond x)) = x + f(h) + f^2(h) + f( h + f(h) + f^2(h) )
$$

where $f^2 = f \circ f$, so the Asterix equation ([E65](https://teorth.github.io/equational_theories/implications/?65)) for such magmas simplifies to the univariant functional equation

$$
f(h) + f^2(h) + f( h + f(h) + f^2(h) ) = 0\qquad\text{(1)}
$$

for $h \in G$.

This equation has some degenerate solutions, for instance we can take $f(h) = c$ for any constant $c$ of order $3$ in $G$. It is challenging to construct more interesting solutions to this equation; however, we can do this if $G=\mathbb{Z}$ by a greedy algorithm. We need the following technical definition.

- [partial-solution](partial-solution.md)

We have the following iterative construction, that lets us add arbitrary elements to the core domain $E_0$:

- [Enlarging a partial solution](iteration.md)
- [extend](extend.md)
- [no-inject](no-inject.md)
- [Asterix does not imply Obelix](asterix-obelix.md)

On the other hand, for finite magmas the situation is different:

- [Asterix implies Obelix for finite magmas](asterix-obelix-finite.md)

A very similar argument shows that a finite magma that satisfies the Obelix law has $z \mapsto y \diamond z$ injective, hence surjective, and then satisfies the Asterix law.
