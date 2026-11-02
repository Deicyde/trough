# Definition of spaces of automorphic forms

Let us now give some precise definitions. Recall that by $\mathbb{A}_F^\infty$ we mean the finite adeles of the totally real number field $F$.

A *level* is a compact open subgroup $U$ of $(D\otimes_F\mathbb{A}_F^\infty)^\times$. These are plentiful. The ring $D_f:=D\otimes_F\mathbb{A}_F^\infty$ is a topological ring, and hence the units $D_f^\times$ of this ring are a topological group. This group is locally profinite, and hence has many compact open subgroups; we will see explicit examples later on.

We regard $\mathbb{A}_F^\infty$ as a subring of $D_{\mathbb{A}^\infty}:=D\otimes_F\mathbb{A}_F^\infty$, which is possible because $F$ is a subring of $D$. More precisely we embed $\mathbb{A}_F^\infty$ into $D\otimes_F\mathbb{A}_F^\infty$ via the map sending $g$ to $1\otimes g$. Because $F$ is in the centre of $D$, we have that $\mathbb{A}_F^\infty$ is in the centre of $D_{\mathbb{A}^\infty}$ (in fact it is the centre, but we do not need this). As a consequence we can identify $(\mathbb{A}_F^\infty)^\times$ as a subgroup of $(D\otimes_F\mathbb{A}_F^\infty)^\times$. We may also regard $D$ as a subring of $D\otimes_F\mathbb{A}_F^\infty$ via the map $d\mapsto d\otimes 1$, and hence we can think of $D^\times$ as a subgroup of $(D\otimes_F\mathbb{A}_F^\infty)^\times$.

Let $R$ be an additive commutative group. Later on $R$ will be a commutative ring but we will not need this for the definition.

- [TotallyDefiniteQuaternionAlgebra.WeightTwoAutomorphicForm](totallydefinitequaternionalgebra-weighttwoautomo.md)

Let $S^D(R)$ denote the set of automorphic forms for $D^\times$. The space $S^D(R)$ is sometimes referred to as a space of “quaternionic modular forms” over $R$. Three basic observations about $S^D(R)$ are

- [TotallyDefiniteQuaternionAlgebra.WeightTwoAutomorphicForm.addCommGroup](totallydefinitequaternionalgebra-weighttwoautomo-2.md)
- [TotallyDefiniteQuaternionAlgebra.WeightTwoAutomorphicForm.module](totallydefinitequaternionalgebra-weighttwoautomo-3.md)
- [TotallyDefiniteQuaternionAlgebra.WeightTwoAutomorphicForm.distribMulAction](totallydefinitequaternionalgebra-weighttwoautomo-4.md)

If $R$ is a commutative ring then the action of $D_{\mathbb{A}^\infty}^\times$ commutes with the $R$-action.

Now let $U$ be a level, that is, a compact open subgroup of $D_{\mathbb{A}^\infty}^\times$.

- [TotallyDefiniteQuaternionAlgebra.WeightTwoAutomorphicFormOfLevel](totallydefinitequaternionalgebra-weighttwoautomo-5.md)

The Hecke algebras involved in the main modularity lifting theorems needed in the FLT project will be endomorphisms of these spaces $S^D(U;R)$.
