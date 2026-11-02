# The goal

There are several goals to this miniproject.

1. Define the adeles $\mathbb{A}_K$ of a number field $K$ and give them the structure of a $K$-algebra (status: now in mathlib thanks to Salvatore Mercuri);
2. Prove that $\mathbb{A}_K$ is a locally compact topological ring (status: [also proved by Mercuri](https://github.com/smmercuri/adele-ring_locally-compact) but not yet in mathlib);
3. Base change: show that if $L/K$ is a finite extension of number fields then the natural map $L\otimes_K\mathbb{A}_K\to\mathbb{A}_L$ is an isomorphism, both algebraic and topological; (status: not formalized yet, but there is a plan – see the project dashboard);
4. Prove that $K \subseteq \mathbb{A}_K$ is a discrete subgroup and the quotient is compact (status: not formalized yet, but there is a plan – see the project dashboard);
5. Get this stuff into mathlib (status: (1) done, (2)–(4) not done).

We briefly go through the basic definitions. Let $K$ be a number field. Let $\widehat{\mathbb{Z}}=\projlim_{N\geq1}(\mathbb{Z}/N\mathbb{Z})$ be the profinite completion of $\mathbb{Z}$, equipped with the projective limit topology.

A cheap definition of the finite adeles $\mathbb{A}_K^\infty$ of $K$ is $K\otimes_{\mathbb{Z}}\widehat{\mathbb{Z}}$, equipped with the $\widehat{\mathbb{Z}}$-module topology. A cheap definition of the infinite adeles $K_\infty$ of $K$ is $K\otimes_{\mathbb{Q}}\mathbb{R}$ with the $\mathbb{R}$-module topology (this is a finite-dimensional $\mathbb{R}$-vector space so this is just the usual topology on $\mathbb{R}^n$). A cheap definition of the adeles of $K$ is $\mathbb{A}_K^\infty\times K_\infty$ with the product topology. This is a commutative topological ring.

However in the literature (and in mathlib) we see different definitions. The finite adeles of $K$ are usually defined in the books as the so-called restricted product $\prod'_{\mathfrak{p}}K_{\mathfrak{p}}$ over the completions $K_{\mathfrak{p}}$ of $K$ at all maximal ideals $\mathfrak{p}\subseteq\mathcal{O}_K$ of the integers of $K$. Here the restricted product is the subset of $\prod_{\mathfrak{p}}K_{\mathfrak{p}}$ consisting of elements which are in the integers $\mathcal{O}_{K,\mathfrak{p}}$ of $K_{\mathfrak{p}}$ for all but finitely many $\mathfrak{p}$. This is the definition given in mathlib. Mathlib also has the proof that they're a topological ring; furthermore the construction of the finite adeles in mathlib works for any Dedekind domain (this was pointed out to me by María Inés de Frutos Fernández; the adeles are an arithmetic object, but the finite adeles are an algebraic object).

Similarly the infinite adeles of a number field $K$ are usually defined as $\prod_v K_v$, the product running over the archimedean completions of $K$, and this is the mathlib definition.

The adeles of a number field $K$ are the product of the finite and infinite adeles, and mathlib knows that they're a $K$-algebra and a topological ring.
