# The free 854 magma

In this section we explicitly describe the free magma $M_{X, 854}$ on some set $X$ of generators relative to the 854 law.

We recall the free magma $M_X$ from [Free Magma](../../basic-theory-of-magmas/free-magma-def.md), though to avoid confusion we will denote the magma operation on $M_X$ by $*$ rather than $\diamond$. Recall that every word $w$ in $M_X$ has a length in $\mathbb{N}$, which is zero if $w$ is a generator in $X$, and is the sum of the lengths of $w_L$ and $w_R$ plus one if instead $w$ is of the form $w_L * w_R$ for the left and right components $w_L, w_R$ of $w$ (which are uniquely defined by $w$). We iterate this notation, for instance $w_{RL}$ is the left-component of $w_R$ (if it exists), thus $w = w_L * (w_{RL} * w_{RR})$ in this case.

We shall shortly define a relation $\to$ on $M_X$. To motivate this relation, we make the following observation about 854 magmas:

- [The 854 relation](854-relation.md)
- [Relation on the free group](free-relate.md)
- [Free 854 magma](free-854.md)
