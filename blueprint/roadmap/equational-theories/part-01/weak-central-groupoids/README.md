# Weak central groupoids

In this chapter we study weak central groupoids [E1485](https://teorth.github.io/equational_theories/implications/?1485),

$$
x = (y \diamond x) \diamond (x \diamond (z \diamond y)).\qquad\text{(1)}
$$

The first observation is that this law is equivalent to its dual:

- [1485 equivalent to 2162](1485-dual.md)

Given a weak central groupoid $G$, define a directed graph with vertices in $G$ by declaring $x \to y$ if and only if $y = x \diamond z$ for some $z$. There is an equivalent characterization of this graph:

- [Equivalent characterization of graph](graph-dual.md)

Define a *good path* in $G$ to be a path of the form

$$
x \to x \diamond y \to y
$$

for some $x,y \in G$ (we allow loops). By the above lemma, this is a path in $G$. The following claims are clear from definition and the above lemma:

- Claim 1: If $x,y \in G$ then there is exactly one good path $x \to z \to y$ from $x$ to $y$.
- Claim 2: Any edge $x \to y$ in the directed graph is the initial segment of some good path $x \to y \to z$.
- Claim 3: Any edge $x \to y$ in the directed graph is the final segment of some good path $w \to x \to y$.

Slightly more non-trivial is

- [Claim 4](claim-4.md)

Conversely, we have

- [Reversing the claims](rev-claim.md)

This gives us a graph-theoretical route to construct weak central groupoids. We first introduce a weaker version of Claim 1:

- Claim 1': If $x,y \in G$ then there is at least one good path $x \to z \to y$ from $x$ to $y$.

Let us call a *relaxed weak central groupoid* a directed graph with some paths of length 2 designated as “good” that satisfy Claims 1', 2, 3, 4.

We also define a *partial weak central groupoid* to be a directed graph with some paths of length 2 that satisfy Claim 4 as well as the following opposite weakening of Claim 1:

- Claim 1”: If $x,y \in G$ then there is at most one good path $x \to z \to y$ from $x$ to $y$.

If we can upgrade Claim 1” to Claim 1, and we also have Claim 2 and Claim 3, then we call this a *complete weak central groupoid*, and by the previous proposition this is in correspondence with (1).

Let $G_0$ be a relaxed weak central groupoid. A *partial extension* of $G_0$ is a partial weak central groupoid $G$ with a “projection map” $\pi: G \to G_0$, which is a homomorphism in the sense that the image $\pi(x) \to \pi(y)$ of any edge $x \to y$ in $G$ is an edge in $G_0$, the image $\pi(x) \to \pi(y) \to \pi(z)$ of any good path $x \to y \to z$ in $G$ is a good path in $G_0$, and the image $\pi(x) \to \pi(y) \to \pi(z)$ of any bad path $x \to y \to z$ in $G$ is a bad path in $G_0$. Note that Claim 4 for $G$ is then automatic from Claim 4 of the base $G_0$. The extension is *complete* if the partial weak central groupoid is complete.

We have the following convenient completion property:

- [Completion property](greedy-prop.md)
- [1485 does not imply 1483](1485-refutes.md)
- [Twisting a weak central groupoid](twisting-a-weak-central-groupoid/README.md)
