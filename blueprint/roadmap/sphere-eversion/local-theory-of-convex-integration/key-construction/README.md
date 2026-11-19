# Key construction

The goal of this chapter is to explain the local aspects of (Theillière's implementation of) convex integration, the next chapter will cover global aspects.

The elementary step of convex integration modifies the derivative of a map in one direction. The precise meaning of “one direction” relies on the following definition.

- [dual_pair](def-dual-pair.md)

Let $E$ and $F$ be finite dimensional real normed vector spaces. Let $f \!: E → F$ be a smooth map, and let $(π, v)$ be a dual pair on $E$. We want to modify $Df$ in the direction of $v$ while almost preserving it on $\ker π$. Say we wish $Df(x)v$ could live in some open subset $Ω_x ⊂ F$. Assume there is a smooth family of loops $γ \!: E × 𝕊^1 → F$ such that each $γ_x$ takes values in $Ω_x$, and its average value $\overline{γ}_x = \int_{𝕊^1} γ_x$ is $Df(x)v$ for all $x$. Obviously such loops can exist only if $Df(x)v$ is in the convex hull of $Ω_x$, and we saw in the previous chapter that this is almost sufficient (and we'll see this is sufficiently almost sufficient for our purposes). Then we can modify $f$ to fulfil our wish using the following construction.

- [Theillière 2018](def-corrugation.md)

In the above definition, we mostly think of $N$ as a large natural number. But we don't actually require it, any positive real number will do.

The next proposition implies that, provided $N$ is large enough, we have achieved $Df'(x)v ∈ Ω_x$, almost without modifying derivatives in the directions of $\ker π$, and almost without moving $f(x)$.

- [Theillière 2018](cp-v.md)
