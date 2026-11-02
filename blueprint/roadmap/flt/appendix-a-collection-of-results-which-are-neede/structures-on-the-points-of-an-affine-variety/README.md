# Structures on the points of an affine variety.

All rings and algebras in this section are commutative with a 1, and all morphisms send 1 to 1.

Let $X=\operatorname{Spec}(A)$ be an affine scheme of finite type over a field $K$. For example $X$ could be an affine algebraic variety; in fact we shall only be interested in smooth affine varieties in the applications, but the initial definition and theorem are fine for all finite type schemes.

If $R$ is any $K$-algebra then one can talk about the $R$-points $X(R)$ of $X$, which in this case naturally bijects with the $K$-algebra homomorphisms from $A$ to $R$.

- [topology\_on\_affine\_variety\_points](topology-on-affine-variety-points.md)
- [topology\_on\_affine\_variety\_computation](topology-on-affine-variety-computation.md)

We now specialise to the smooth case. I want to make the following conjectural “definition”:

- [manifold\_on\_algebraic\_variety\_points](manifold-on-algebraic-variety-points.md)

**Remark.** Probably this is fine for a broader class of fields $K$.

- [manifold\_on\_algebraic\_variety\_computation](manifold-on-algebraic-variety-computation.md)
- [lie\_group\_from\_algebraic\_group](lie-group-from-algebraic-group.md)

**Remark.** The corollary, for sure, is true! And it's all we need. I have not yet made any serious effort to find a reference for the definition or independence, although there seem to be some ideas [here](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/top.20space.20.2F.20manifold.20structure.20on.20points.20of.20alg.20varieties/near/431812525). As a toy example, one can embed $\operatorname{GL}_n(\mathbb{R})$ into either $\mathbb{R}^{n^2+1}$ via $M\mapsto (M,\det(M)^{-1})$ or into $\mathbb{R}^{2n^2}$ via $M\mapsto (M,M^{-1})$ and the claim is that the two induced manifold structures are the same.
