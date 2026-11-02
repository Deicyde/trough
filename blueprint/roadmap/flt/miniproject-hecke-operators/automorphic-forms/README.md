# Automorphic forms

We recall some of the definitions of spaces of automorphic forms, from the quaternion algebra project, section [Miniproject: Quaternion algebras](../../miniproject-quaternion-algebras/README.md).

We fix a totally real field $F$, a totally definite quaternion algebra $D/F$, and a coefficient (additive abelian) group $R$. Set $G=(D\otimes_F\mathbb{A}_F^\infty)^\times$ as in the previous section. Note that $G$ naturally contains copies of $D^\times$ and $(\mathbb{A}_F^\infty)^\times$. Recall from definition [TotallyDefiniteQuaternionAlgebra.WeightTwoAutomorphicForm](../../miniproject-quaternion-algebras/definition-of-spaces-of-automorphic-forms/totallydefinitequaternionalgebra-weighttwoautomo.md) that an $R$-valued weight 2 automorphic form is a function $f:G\to R$ satisfying the following axioms:

1. $f(dg)=f(g)$ for all $d\in D^\times\subseteq(D\otimes_F\mathbb{A}_F^\times)$;
2. There exists a compact open subgroup of $U$ (the *level* of $f$) such that $f(gu)=f(g)$ for all $g\in G$ and $u\in U$;
3. $f(gz)=f(g)$ for all $z\in(\mathbb{A}_F^\infty)^\times$.

It can be checked that the collection of all such forms is an additive abelian group, and if $R$ is a ring then it is naturally an $R$-module. Let's call this group $A$ for short. Then $A$ has a left action of $G$, with $g\cdot f$ defined via $(g\cdot f)(x):=f(xg)$. Recall from definition [TotallyDefiniteQuaternionAlgebra.WeightTwoAutomorphicFormOfLevel](../../miniproject-quaternion-algebras/definition-of-spaces-of-automorphic-forms/totallydefinitequaternionalgebra-weighttwoautomo-5.md) that a weight 2 automorphic form of level $U$ is simply an element of the fixed points $A^U$. In other words, the forms of level $U$ are the forms satisfying the three axioms defining an automorphic form but with the compact open subgroup in the second axiom being $U$.
