# Group cohomology and homology

Let $G$ be a group and $R$ a commutative ring. By a *representation of $G$ over $R$*, we shall mean an $R$-module $M$ with an action of $G$ by $R$-linear maps. We shall use the notation $g \bullet m$ for the action of an element $g \in G$ on an element $m \in M$. We'll call $M$ a *trivial* representation if for all $g \in G$ and all $m \in M$ we have $g \bullet m = m$. We'll write $\mathbf{Mod}(R)$ for the category of $R$-modules and $\mathbf{Rep}(R,G)$ for the category of such representations. In Mathlib these are called `ModuleCat R` and `Rep R G`.

If $S$ is a subgroup of $G$ and $M$ is a representation of $G$ then $M \downarrow S$ will mean the same $R$-module $M$, but regarded only as a representation of $S$. We shall write $M^S$ for the $R$-submodule of $S$-invariant vectors in $M$. If the subgroup $S$ is normal then $M^S$ is a representation of the quotient group $G/S$.

- [inflation restriction functors](def-inflation-restriction-functors.md)

Given a representation $M$ of $G$, there is a cochain complex of $R$-modules

$$
C^0(G,M) \stackrel{d^0}\to C^1(G,M)  \stackrel{d^1}\to C^2(G,M)  \stackrel{d^2}\to \cdots
$$

where each term $C^n(G,M)$ is the space of functions $G^n \to M$ with some appropriately defined linear maps $d^i$ linking them. The zeroth module $C^0(G,M)$ should be interpreted as just $M$. The first few of these linear maps $d^i$ are

$$
\begin{aligned}
(d^0 m)(x) &= x \bullet m - m
& m \in M, \\
(d^1 f)(x,y) &= x \bullet f(y) - f(xy) + f(x)
& f : G \to M,\\
(d^2 f)(x,y,z) &= x\bullet f(y,z) - f(xy,z) + f(x,yz) - f(x,y),
& f : G^2 \to M.
\end{aligned}
$$

The cochain complex $C^\bullet(G,M)$ is functorial in $M$ and is defined in Mathlib as `groupCohomology.cochainsFunctor`. The cohomology groups of $C^\bullet(G,M)$ are called the cohomology groups of the $G$-module $M$, and are written $H^n(G,M)$. These are defined in Mathlib as `groupCohomology M n`, or `(groupCohomology.functor n).obj M`.

**Example.** For example $H^0(G,M)$ is the kernel of the map $d^0 : M \to (G \to M)$. Since $(d^0m)(g) = g \bullet m - m$, an element $m$ is in this kernel if $m$ is in $M^G$, so we have $H^0(G,M) \cong M^G$.

**Example.** Suppose $M$ is a trivial representation of $G$. Then the map $d^0$ is zero, so $H^1(G,M)$ is the kernel of the map $(d^1f)(x,y) = f(x) + f(y) - f(xy)$. A function $f: G \to M$ is in this kernel if it is a group homomorphism, so we have $H^1(G,M) \cong \mathrm{Hom}(G,M)$.

- [Hn unit](lem-hn-unit.md)

**Remark.** The functions $d^i : (G^i \to M) \to (G^{i+1} \to M)$ do not depend on the ring $R$. Consequently, the additive groups $H^n(G,M)$ do not depend on $R$. More precisely there are forgetful functors $F_1 : \mathbf{Rep}(R,G) \to \mathbf{Rep}({\mathbb Z},G)$ and $F_2 : \mathbf{Mod}(R) \to \mathbf{Mod}({\mathbb Z})$, and there are isomorphisms of functors

$$
H^n \circ F_1 \cong F_2 \circ H^n.
$$

That said, it is very little extra work to prove the cohomological results discussed here in the generality of $\mathbf{Rep}(R,G)$ rather than $\mathbf{Rep}({\mathbb Z},G)$.

**Remark.** At this point it's worth stressing one particular aspect of this theory. Many of the proofs involve showing that certain diagrams commute. When writing proofs on paper, some mathematicians don't give too much thought to the reasons why a particular diagram commutes but when formalizing theorems we need to be more careful than this. For that reason it is important to define all of our objects in as functorial a way as possible. In the example from the previous remark, saying that there is an isomorphism $H^n(G,F_1(M)) \cong F_2(H^n(G,M))$ is not as good as saying that there is an isomorphism of functors $H^n \circ F_1 \cong F_2 \circ H^n$. The isomorphism of functors implies that for every map $f : A \to B$ in $\mathbf{Rep}(R,G)$ we have a commuting square in $\mathbf{Mod}({\mathbb Z})$, in which the vertical arrows are the isomorphisms of the objects

$$
\begin{matrix}
H^n(G,F_1(A)) & \stackrel{H^1(G,F_1(f))}\to & H^n(G,F_1(B))\\
\downarrow &&\downarrow \\
F_2(H^n(G,M)) & \stackrel{F_2(H^1(G,f))}\to & F_2 H^n(G,B)
\end{matrix} .
$$

This commuting square might be crucial in some other proof. This is also the reason why we work with the categories `Rep R G` and `ModuleCat R`, rather than with `Representation R G M` and `Module R M` which could be more familiar.

- [restriction map](def-restriction-map.md)
- [inflation map](def-inflation-map.md)
- [cochainsFunctor exact](lem-cochainsfunctor-exact.md)

As a consequence of this, we have the following (which is in Mathlib):

- [cohomology long exact sequence](def-cohomology-long-exact-sequence.md)
- [inflation restriction naturality](lem-inflation-restriction-naturality.md)
- [group homology](def-group-homology.md)

**Example.** We'll sometimes write $\mathrm{single}(g,m)$ for the function with value $m$ at $g$ and value zero elsewhere. The $R$-module $C_1(G,M)$ is spanned by the elements $\mathrm{single}(g,m)$ for $g \in G$ and $m \in M$ (`Finsupp.single` in Mathlib). For such elements we have

$$
d_0(\mathrm{single}(g,m))
=
g \bullet m - m.
$$

We shall write $I_G M$ for the submodule of $M$ spanned by elements of the form $g \bullet m - m$. The quotient $M / I_GM$ is commonly called the *coinvariants* of $M$ and is written $M_G$; this is the largest quotient module on which $G$ acts trivially. It follows that $H_0(G,M) \cong M_G$.

**Example.** In the case that $G=1$ is the trivial group then for all $n > 0$ we have $H_n(1,M)$. This follows in a similar way to [Hn unit](lem-hn-unit.md)

- [homology 1 trivial](lem-homology-1-trivial.md)
