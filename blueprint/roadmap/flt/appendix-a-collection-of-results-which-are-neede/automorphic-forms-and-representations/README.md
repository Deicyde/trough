# Automorphic forms and representations

This section needs a lot of work; I am just attempting to write down some approximation to the (well-known) definitions but in great generality (far greater than we need). Some definitions below are short on details; indeed there may even be errors or imprecisions right now (because we are working in more generality than I am used to). It will be a very interesting project to get these details down. One reference (which leaves a lot of exercises) is Borel-Casselman in (Borel and Casselman 1979). Even *stating* these definitions will be a big challenge in Lean; indeed one of the motivations of the project is that it forces us to write down all the below properly.

Let $G$ be a connected reductive group over a number field $N$. We note that $G(\mathbb{A}_N^f)$ is a (locally profinite) topological space and $G(N_\infty)$ is a real Lie group; their product is $G(\mathbb{A}_N)$. If $g\in G(\mathbb{A}_N)$, write $g_f\in G(\mathbb{A}_N^f)$ for the finite part and $g_\infty\in G(N_\infty)$ for its infinite part.

For some reason, in the literature people seem to fix a choice of maximal compact subgroup $U_\infty$ of $G(N_\infty)$. I believe that all such subgroups are conjugate, and probably this gives some route between the different definitions coming from the different choices.

Example: if $G=\operatorname{GL}_2$ and $N=\mathbb{Q}$ then $N_\infty=\mathbb{R}$ and $G(N_\infty)$ is just $\operatorname{GL}_2(\mathbb{R})$ with its usual Lie group structure and we can take $U_\infty$ to be $O_2(\mathbb{R})$; $G(\mathbb{A}_N^f)$ is the restricted product of $\operatorname{GL}_2(\mathbb{Q}_p)$ over $\operatorname{GL}_2(\mathbb{Z}_p)$, for all primes $p$.

By assumption, $G(N_\infty)$ admits a finite-dimensional (algebraic) representation $\rho$ with finite kernel. Consider $\rho$ as taking values in $GL_N(\mathbb{C})=\operatorname{Aut}_{\mathbb{C}}(V)$. Fix a hermitian sesquilinear form on $V$ which is $U_\infty$ invariant, and now define a norm $||g||_\rho$ on $G(N_\infty)$ by

$$
||g||_\rho=(\operatorname{tr} \rho(g)^*\rho(g))^{1/2},
$$

where the asterisk denotes adjoint with respect to the sesquilinear form. According to the article by Borel–Jacquet in (Borel and Casselman 1979) (p189), if $\rho'$ is another such choice then there exists a positive real $C$ and a positive integer $n$ such that $||g||_{\rho'}\leq C||g||_\rho^n$ for all $g\in G(N_\infty)$.

We can now give the definition of an automorphic form. For FLT we only need the definition for $G$ being either an abelian algebraic group, or an inner form of $GL(2)$, but we have chosen to work in full generality here.

Automorphic forms form a typically infinite-dimensional vector space.

The cuspidal automorphic forms form a complex subspace of the space of automorphic forms.

For non-cuspidal representations, they do not decompose as a direct sum; there is a continuous spectrum which decomposes as a direct integral. We may not ever need these. As a result the definition of an automorphic representation has to be slightly modified in the non-cuspidal case.

Admissibility is a finiteness condition on an irreducible representation of $(G(\mathbb{A}_N^f)\times U_\infty,\mathfrak{g})$; automorphic representations are admissible, and this seems to boil down to theorems of Godement and Harish-Chandra in the general case.

As mentioned above, we only need all of this for abelian algebraic groups and for inner forms of $\operatorname{GL}_2$ over totally real fields, where everything can be made more concrete (and in particular where I can write down concrete definitions, although this still needs to be done). In particular, we don't strictly speaking need all of the above, we could just cheat and deal with $\operatorname{GL}_2(\mathbb{R})$ and $\mathbb{H}^\times$ separately.

The theorems I need are: Jacquet-Langlands for inner forms of $\operatorname{GL}_2$ over totally real fields, and multiplicity 1 for these inner forms. We also need cyclic base change plus classification of image, all for totally definite quaternion algebras, and we need automorphic induction from $\operatorname{GL}_1(K)$ to $\operatorname{GL}_2(F)$ when $K/F$ is a degree 2 totally imaginary extension. There seems to be little point formalising the statements of the theorems if we cannot yet even formalise the definition of an automorphic representation properly.
