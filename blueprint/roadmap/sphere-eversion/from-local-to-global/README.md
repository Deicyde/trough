# From local to global

In this chapter, we gather some topological preliminaries allowing to build global objects from local ones. This is usually not discussed in informal expositions where such arguments are either implicit or interspersed with more specific arguments.

We first need to discuss how to build a function having everywhere some local properties from a sequence of functions having those properties on bigger and bigger parts of the source space. We actually want to also accommodate finite sequences so we start with a definition of the source of our sequences.

- [index_type](def-index-type.md)

On each $\mathcal{I}_{N}$ we use the obvious linear ordering. In particular there is no maximal element when $N = 0$ and $N-1$ is maximal if $N$ is positive. The successor function $S \!: \mathcal{I}_{N} → \mathcal{I}_{N}$ is the function sending $n$ to $n+1$ unless $n$ is maximal, in which case $S(n) = n$.

Our first lemma gives a criterion ensuring that a sequence of functions is locally ultimately constant hence has a limit that locally ultimately agrees with the elements of the sequence. Remember that a family of sets $V_n$ in a topological space $X$ is locally finite if every point of $X$ has a neighborhood that intersects only finitely many $V_n$.

- [exists_forall_eventually_of_index_type](lem-exists-forall-eventually-of-index-type.md)

In the preceding lemma, the limit function $F$ inherits all local properties of the elements of the sequence. In order to make this precise, we need the language of germs of functions. One can define germs with respect to any filter but we will need only the case of neighborhood filters : two functions $f$ and $g$ define the same germ at some point $x$ if they coincide near $x$.

- [germ](def-germ.md)

For instance if $Y$ is also equipped with a topology then continuity is (equivalent to) a local predicate on functions from $X$ to $Y$ since a function is continuous if and only if it is continuous at every point $x$ and this condition only depends on the germ of the function at $x$.

We also need to build local predicates by localizing some local predicates near some subsets.

- [restrict_germ_predicate](def-restrict-germ-predicate.md)

Note the above definition hides a little lemma asserting that the obtained predicate is indeed local. An even smaller lemma asserts that a function satisfies $P_{|A}$ if and only if it satisfies $P$ at each point near $A$.

In the next lemma, there are three predicates or families of predicates. The local predicate $P₀$ is satisfied by every function appearing in the lemma, it could be a continuity or smoothness constraint. The family of local predicates $P₁$ is the main constraint and the goal is to build a function satisfying all of them. The family of predicates $P₂$ plays an auxiliary role, it does not have to be local, does not appear in the conclusion and is only used to bring more flexibility in the main inductive assumption. One can read “$f$ satisfies $P₂^i$” as “$f$ can be improved in $Uᵢ$”.

- [inductive_construction](lem-inductive-construction.md)

Next we will need a version of the above lemma building a homotopy of maps. In this version, $P₀$ is still a predicate such as continuity satisfied by all maps from $X$ to $Y$ entering the discussion. Then $P₀'$ is analogous but for maps from $ℝ × X$ to $Y$, and it will come with some affine invariance assumption ensuring its compatibility with concatenation of homotopies. Instead of having a completely general family of local predicates $P₁^i$, we fix a single local predicate $P₁$ but it will be required to hold only near some subset $K_i$ (as in [Definition restrict_germ_predicate](def-restrict-germ-predicate.md)).

Homotopies of maps from $X$ to $Y$ are usually meant to be continuous maps from $[0, 1] × X$ to $Y$. In a differential topology context, one requires smoothness and in order to be able to easily concatenate homotopies, it is very convenient to add the assumptions that those maps are independent of the time variable $t ∈ [0, 1]$ when $t$ is close to $0$ or $1$. Especially in a formalization context, it is even more convenient to assume homotopies are defined on $ℝ × X$, and time independent near $(-∞, 0] × X$ and $[1, +∞) × X$. Continuity or smoothness don't appear in the following abstract lemma where they are replaced by arbitrary local predicates.

- [inductive_htpy_construction](lem-inductive-htpy-construction.md)

In a different direction, we need a version of [Lemma inductive_construction](lem-inductive-construction.md) where we do not fix any family of subsets of the source space, but simply want to derive existence of a function satisfying some local predicates from the assumptions of existence of local solution and the ability to patch solutions. This requires putting a lot more constraints on the source topological space in order to use the following classical result.

- [exists_locally_finite_subcover_of_locally](lem-exists-locally-finite-subcover-of-locally.md)

In the next lemma, $P₀$ is again a background local predicate satisfied by all maps entering the discussion, and $P₁$ is the main target local predicate. We also use an extra predicate $P₀'$ that enters the patching assumption in an asymmetric way and will allows to deduce a relative version of the lemma.

- [inductive_construction_of_loc](lem-inductive-construction-of-loc.md)

From the above lemma we can deduce a version with only a base local predicate $P₀$ and a target one $P₁$ and starting from a function which is already good near some closed subset $K$. The is the version that is actually used in our application.

- [relative_inductive_construction_of_loc](lem-relative-inductive-construction-of-loc.md)
