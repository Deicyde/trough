# Running a greedy algorithm

Define a *partial 854 magma* to be a partial function $\diamond: \mathbb{N} \times \mathbb{N} \to \mathbb{N}$ satisfying the following axioms:

- (Equation 854) If $x,y,z \in \mathbb{N}$ are such that $(y \diamond z) \diamond (x \diamond z)$ is well-defined, then $x \diamond ((y \diamond z) \diamond (x \diamond z))$ is well-defined and equal to $x$.
- (Equation 8) If $x \in \mathbb{N}$ are such that $x \diamond x$ is well-defined, then $x \diamond (x \diamond x)$ is well-defined and equal to $x$.
- (Equation 101) If $x,y \in \mathbb{N}$ are such that $(x \diamond y) \diamond x$ is well-defined, then $x \diamond ((x \diamond y) \diamond x)$ is well-defined and equal to $x$.
- (Equation 46155) If $x,y \in \mathbb{N}$ are such that $x \diamond (x \diamond y)$ is well-defined, then $(x \diamond y) \diamond (x \diamond (x \diamond y))$ is well-defined and equal to $x \diamond y$.
- (Equation 378) If $x,y \in \mathbb{N}$ is such that $x \diamond y$ is well-defined, then $(x \diamond y) \diamond y$ is well-defined and equal to $x \diamond y$.
- (No idempotence) If $x \in \mathbb{N}$ is such that $x \diamond x$ is well-defined, then $x \diamond x \neq x$.
- (Auxiliary law) If $x,y \in \mathbb{N}$ are such that $x \diamond (x \diamond y)$ is well-defined and equal to $x$, then $x=y$.
- (Unique factorization) If $x,y,x',y' \in \mathbb{N}$ are such that $x \diamond y$, $x' \diamond y'$ are well-defined and equal to each other, then at least one of the assertions $x \diamond y = x$, $x' \diamond y' = x'$, or $(x,y) = (x',y')$ is true.
- (Monotonicity) If $x,y \in \mathbb{N}$ is such that $x \diamond y$ is defined, then either $x \diamond y = x$ or $x \diamond y > x, y$.

The first five laws are known consequences of 854. The no idempotence law was known for the free magma $M_{854}$ because it maps to finite magmas without idempotents, such as $\mathbb{Z}/3\mathbb{Z}$ with law $x \diamond y = x - 1_{x=y}$. The unique factorization law is also known for the free magma by [Unique factorization](../unique-factorization.md). The auxiliary law is a “leap of faith” that helped close the greedy argument, and the monotonicity property is a technical consequence of the greedy construction that will also help close the argument.

The following observation is key.

- [Greedy construction](854-extend.md)
- [854 extension](extend-854.md)
- [854 does not not imply 413](854-413.md)
- [854 does not not imply 1045](854-1045.md)
