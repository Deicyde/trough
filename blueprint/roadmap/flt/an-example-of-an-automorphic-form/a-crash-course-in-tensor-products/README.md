# A crash course in tensor products

We've defined $\widehat{\mathbb{Q}}$ to be $\mathbb{Q}\otimes\widehat{\mathbb{Z}}$. Whatever does this mean? Well just to orient yourself, if $A$ and $B$ are additive abelian groups, then $A\otimes B$ is also an abelian group. And if $A$ and $B$ are commutative rings (as they are in our case), then $A\otimes B$ is also a commutative ring.

Even if $A$ and $B$ are completely concrete commutative rings, their tensor product $A\otimes B$ might be incomprehensible. For example $\mathbb{C}\otimes\mathbb{C}$ is completely incomprehensible (note that we are tensoring over the integers). It is not like the product of groups or the disjoint union of two sets, where you have a completely explicit unambiguous formula for each element.

In this sense, the theory of tensor products is a bit like the theory of continuous functions. Humanity started off studying concrete polynomial equations such as $x^2+1$ and then moved on to concrete analytic functions such as $\log(x)$ and $\sin(x)$, but eventually the abstract concept of a continuous function from the reals to the reals was born. There is no “formula” for a general continuous function, and continuous functions such as $e^{-1/x^2}$ or $|x|$ have no power series. Even if there *were* a formula for a specific continuous function of interest, it is not clear in general how to make sense of the claim that it's the “best” formula. In other words, there is no "canonical form" for a general continuous function, and yet we prove things about them anyway. We shall adopt the same attitude for elements of $A\otimes B$.

The first thing to know about the tensor product $A\otimes B$ of two abelian groups $A$ and $B$ is a “constructor” for the type. In other words, how can we make elements $A\otimes B$? Well, it turns out that given elements $a\in A$ and $b\in B$, we can form the element $a\otimes_t b\in A\otimes B$.

- [QHat.canonicalForm](qhat-canonicalform.md)
- [QHat.IsCoprime](qhat-iscoprime.md)
- [QHat.lowestTerms](qhat-lowestterms.md)
- [QHat.injective\_rat](qhat-injective-rat.md)
- [QHat.injective\_zHat](qhat-injective-zhat.md)
