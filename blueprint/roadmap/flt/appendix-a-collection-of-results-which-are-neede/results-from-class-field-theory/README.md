# Results from class field theory

We start with the local case. In fact we restrict to the $p$-adic case, but only for simplicity of exposition because it's all we'll need (and, to be frank, because I'm not 100 percent of what is true in the function field case).

Let $K$ be a finite extension of $\mathbb{Q}_p$. We write $\widehat{\mathbb{Z}}$ for the profinite completion of $\mathbb{Z}$; it is isomorphic to $\prod_p\mathbb{Z}_p$ where $\mathbb{Z}_p$ is the $p$-adic integers and the product is over all primes.

It is impossible to say which of the two canonical isomorphisms is “the most canonical”; people working in different areas make different choices in order to locally minimise the number of minus signs in their results.

As a result, the absolute Galois group of $K$ surjects onto $\widehat{\mathbb{Z}}$; its kernel is said to be the *inertia subgroup* of this Galois group. Now pull back this surjection along the continuous map from $\mathbb{Z}$ (with its discrete topology) to $\widehat{\mathbb{Z}}$, in the category of topological groups. We end up with a group containing the inertia group as an open normal subgroup, and with quotient isomorphic to the integers.

The following theorem is nontrivial.

Note that María Inés de Frutos Fernández and Filippo Nuccio are working on a formalisation of the proof of this using Lubin–Tate formal groups.

Now let $M$ be an abelian group (with the discrete topology) equipped with a continuous action of $G_K$, the Galois group $\operatorname{Gal}(K^{\operatorname{sep}}/K)$ where we fix an algebraic closure $\overline{K}$ of $K$. Note that if one doesn't want to choose an algebraic closure of $K$ one can instead think of $M$ as being an etale sheaf of abelian groups on $\operatorname{Spec}(K)$.

Continuous group cohomology $H^i(G_K,M)$ in this setting can be defined using continuous cocycles and continuous coboundaries, or just as a colimit of usual group cohomology over the finite quotients of this absolute Galois group (or as etale cohomology, if you prefer). Here are some of the facts we will need about cohomology in this situation. A nice summary is that cohomology of a local Galois group behaves like the cohomology of a compact connected 2-manifold. All the theorems below will need extensive planning.

We now move onto the global case. If $N$ is a number field, that is, a finite extension of $\mathbb{Q}$, then let $\mathbb{A}_N^f:= N\otimes_{\mathbb{Z}}\widehat{\mathbb{Z}}$ denote the finite adeles of $N$ and let $N_\infty := N\otimes_{\mathbb{Q}}\mathbb{R}$ denote the product of the completions of $N$ at the infinite places, so $\mathbb{A}_N:=\mathbb{A}_N^f\times N_\infty$ is the ring of adeles of $N$.

We need the following consequence:

We also need Poitou-Tate duality; I'll refrain from writing it down for now, because we don't even have Galois cohomology in Lean yet (although we are very close to it).
