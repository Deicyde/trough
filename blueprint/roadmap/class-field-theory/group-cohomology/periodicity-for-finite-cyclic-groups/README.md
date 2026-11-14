# Periodicity for finite cyclic groups

In this section we shall assume that $G$ is a finite cyclic group of order $n$. We shall write $\mathrm{gen}$ for a fixed generator of $G$.

Given any representation $M$ of $G$, there is a map $\mathrm{map}_1 : \mathrm{coind}_1'(M) \to \mathrm{coind}_1'(M)$ which takes a function $f : G \to M$ to the function

$$
x \mapsto f(x) - f(\mathrm{gen}^{-1}\cdot x).
$$

The kernel of $\mathrm{map}_1$ consists of the constant functions $G \to M$, i.e. the image of the map $M \to \mathrm{coind}_1'(M)$. Hence by the first isomorphism theorem, the image of $\mathrm{map}_1$ is isomorphic to $\mathrm{up}(M)$.

Since $G$ is finite, the representations $\mathrm{coind}_1'(M)$ and $\mathrm{ind}_1'(M)$ are isomorphic, and we define $\mathrm{map}_2$ to be the corresponding map $\mathrm{ind}_1'(M) \to \mathrm{ind}_1'(M)$. This is given by

$$
\mathrm{map}_2(f) (x) = f(x) - f(\mathrm{gen}^{-1} \cdot x), \qquad i.e.\;
\mathrm{map}_2(\mathrm{single}(x,m)) = \mathrm{single}(x,m) - \mathrm{single}(\mathrm{gen} \cdot x, m).
$$

- [map2 image](lem-map2-image.md)
- [up iso down](def-up-iso-down.md)
- [periodic cohomology](cor-periodic-cohomology.md)

A very important example for us is the trivial representation of $G$ on ${\mathbb Z}$, which we describe very precisely here:

- [H2 cyclic Z](lem-h2-cyclic-z.md)
- [local inv](def-local-inv.md)
- [local inv iso](lem-local-inv-iso.md)
