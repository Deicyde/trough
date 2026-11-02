# Adelic groups

We are finally ready to discuss the group $G$ and the subgroups $U$ which we will be using to define our Hecke operators. Let $K$ be a number field, let $D$ a quaternion algebra over $K$ and let $\mathbb{A}_K^\infty$ be the finite adeles of $K$; recall that this is a commutative topological ring, defined to be the restricted product of the commutative topological fields $K_v$ as $v$ runs through the finite places of $K$, with respect to the compact open subrings $\mathcal{O}_v$.

The group $G$ we are interested in for the rest of this miniproject is the group $(D\otimes_K\mathbb{A}_K^\infty)^\times$. We want to write down compact open subgroups of this group, but the first thing we need to do is to find a way of talking about elements of the group.

We will assume that there exists an $\mathbb{A}_K^\infty$-algebra isomorphism $D\otimes_K\mathbb{A}_K^\infty=M_2(\mathbb{A}_K^\infty)$ and we will fix such an isomorphism $r$ (called a *rigidification* in the Lean code). We give both of these $\mathbb{A}_K^\infty$-algebras the $\mathbb{A}_K^\infty$-module topology, which is a fancy way of saying the product topology (they are both free of rank 4 as $\mathbb{A}_K^\infty$-modules); the rigidification is then a homeomorphism (because all $\mathbb{A}_K^\infty$-module maps between modules with the $\mathbb{A}_K^\infty$-module topology are continuous).

This means that our group $G$ is isomorphic (both algebraically and topologically) to $GL_2(\mathbb{A}_K^\infty)$. Before we go any further, let say something about matrix rings over complete fields.

- [GL2.restrictedProduct](gl2-restrictedproduct.md)
