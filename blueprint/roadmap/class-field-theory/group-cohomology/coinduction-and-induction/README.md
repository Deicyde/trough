# Coinduction and induction

- [trivial cohomology](def-trivial-cohomology.md)

In this section we shall describe certain representations with trivial homology and cohomology.

Let $\phi : S \to G$ be a group homomorphism and let $M$ be a representation of $S$. We define a representation $\mathrm{coind}_\phi(M)$ of $G$ as follows. As an $R$-module we have

$$
\mathrm{coind}_\phi(M) =
\{ f : G \to M| \forall s \in S, x \in G, f(\phi(s)x) = s \bullet f(x)\}.
$$

This space can be regarded as the $(G \to M)^S$, where the action of $S$ is $(s\bullet f)(x)=s \bullet f(\phi(s^{-1})\bullet x)$. The action of an element $g \in G$ on $f \in \mathrm{coind}_\phi(M)$ is defined by

$$
(g \bullet f)(x) = f(xg).
$$

The map $M \mapsto \mathrm{coind}_\phi(M)$ is a functor from $\mathbf{Rep}(R,S)$ to $\mathbf{Rep}(R,G)$, and is implemented in Mathlib as `Rep.coindFunctor`.

There is also a functor $\mathrm{ind}_\phi : \mathbf{Rep}(R,S) \to \mathbf{Rep}(R,G)$ which is defined as a quotient of $G \to_0 M$ rather than a subspace of $G \to M$:

$$
\mathrm{ind}_\phi(M) = (G \to_0 M) / \langle s \bullet f - f\rangle,
\qquad
(s \bullet f) (x) = s \bullet f (x \phi(s)).
$$

The action of an element $g \in G$ on $G \to_0 M$ is defined by $(g \bullet f)(x) = f(g^{-1} x)$; this action descends to $\mathrm{ind}_\phi(M)$. The functor $\mathrm{ind}_\phi : \mathbf{Rep}(R,S) \to \mathbf{Rep}(R,G)$ is implemented in Mathlib as `Rep.ind`.

The functors $\mathrm{ind}_\phi$ and $\mathrm{coind}_\phi$ are particularly important in the case that $S$ is a subgroup of $G$, and $\phi : S \to G$ is the inclusion map. This is because of the following result:

- [Shapiro's Lemma](lem-shapiro.md)

We shall be interested in the special case in which the group $S$ is the trivial group $1$. In this case the $S$-representation $M$ may be regarded as simply an $R$-module. This case is described again below.

- [induced](def-induced.md)
- [coind₁ trivial cohomology](lem-coind1-trivial-cohomology.md)
- [coind₁ invariants](lem-coind1-invariants.md)
- [ind₁ trivial homology](lem-ind1-trivial-homology.md)
- [ind₁ to coind₁](def-ind1-to-coind1.md)
- [induced trivial Tate](lem-induced-trivial-tate.md)
