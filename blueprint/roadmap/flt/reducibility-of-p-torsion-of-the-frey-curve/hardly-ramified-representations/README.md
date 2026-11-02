# Hardly ramified representations

Let $(a,b,c,p)$ be a Frey package (so in particular $p\geq5$ is prime and $a^p+b^p=c^p$), let $E$ be the corresponding Frey curve over $\mathbb{Q}$, and let $\rho:\operatorname{Gal}(\overline{\mathbb{Q}}/\mathbb{Q})\to\operatorname{Aut}(E(\overline{\mathbb{Q}})[p])$ be the 2-dimensional Galois representation on the $p$-torsion of $E$. Recall that our goal is to prove that $\rho$ is reducible.

What we need to leverage is the fact that $\rho$ has very little ramification. To give a toy example before we start: if $K$ is a number field (i.e., a finite extension of $\mathbb{Q}$) and if the extension $K/\mathbb{Q}$ is unramified at all primes, then an old theorem of Minkowski tells us that $K=\mathbb{Q}$. We want to prove a theorem in a similar vein, namely that if a 2-dimensional mod $p$ Galois representation is “hardly ramified”, then it is reducible. Below, we give a precise definition of what it means for a continuous 2-dimensional representation $\operatorname{Gal}(\overline{\mathbb{Q}}/\mathbb{Q})\to\operatorname{GL}_2(R)$ to be hardly ramified. Before we do that, we need to say precisely which topological rings $R$ we will allow. We say that a topological ring is emphpro-Artinian if it is a projective limit of Artin local rings each equipped with the discrete topology, and if it has the projective limit topology. We are only concerned with local pro-Artinian rings with finite residue field; such things can be checked to be the same thing as topological local rings with finite residue field whose underlying topological space is profinite, and such that additive translates of open ideals form a basis for the topology. Let us call such rings “coefficient rings” for now.

**Remark.** We make some remarks to orient the reader.

- Any complete local Noetherian ring with finite residue field is a coefficient ring, if the ring is equipped with the $\mathfrak{m}$-adic topology where $\mathfrak{m}$ is the maximal ideal. In this case, all powers of $\mathfrak{m}$ are open.
- In particular finite fields, and integer rings of finite extensions of $\mathbb{Q}_p$, are coefficient rings.
- If $R$ is a coefficient ring then $R$ is isomorphic to the projective limit of the finite rings $R/I$ as $I$ runs over the open ideals of $R$.
- A non-Noetherian example of a coefficient ring is the projective limit over $n$ of the rings $\mathbb{Z}/p\mathbb{Z}[\varepsilon_1,\ldots,\varepsilon_n]/(\forall i,j,\varepsilon_i\varepsilon_j=0)$; these rings are convenient to include as coefficient rings for technical reasons; they make representability theorems easier.
- The category of coefficient rings is equivalent to the pro-category of the category of finite local rings.
- A coefficient ring is pseudocompact in the sense of Grothendieck. A pseudocompact local ring is however a more general concept as such a thing may have an infinite residue field and would thus not be profinite.
- If $R$ is a coefficient ring with residue field of characteristic $\ell$, then there is a unique continuous map $\mathbb{Z}_\ell\to R$. Indeed, it suffices to prove that there is a unique continuous map $\mathbb{Z}_\ell\to R/I$ for each open ideal $I$, but $R/I$ is a finite local ring with residue field of characteristic $\ell$. $R/I$ is hence Artinian, so some power of the maximal ideal is zero by Nakayama. This means that $\ell^N=0$ for some sufficiently large $N$, and hence $R/I$ is a $\mathbb{Z}/\ell^N\mathbb{Z}$-algebra and thus admits admits a unique map from $\mathbb{Z}_\ell$.
- It will be more convenient to fix once and for all the integer $\mathcal{O}$ in a finite extension of $\mathbb{Q}_\ell$ and consider “coefficient $\mathcal{O}$-algebras”, namely coefficient rings $R$ equipped with a continuous map $\mathcal{O}\to R$ which is a local homomorphism inducing an isomorphism on residue fields.

Because a coefficient ring $R$ with residue field of characteristic $\ell$ is naturally a $\mathbb{Z}_\ell$-algebra, we can talk about the $\ell$-adic cyclotomic character $\operatorname{Gal}(\overline{\mathbb{Q}}/\mathbb{Q})\to R^\times$. We are now ready to define hardly ramified representations.

- [hardly\_ramified](hardly-ramified.md)

A well-known result, which basically goes back to Frey, is the following:

- [Frey\_curve\_hardly\_ramified](frey-curve-hardly-ramified.md)

Note that irreducibility and absolute irreducibility for hardly ramified mod $\ell$ representations are the same, because our assumptions that $\ell\geq3$ and that the determinant is cyclotomic imply that the image of complex conjugation has distinct eigenvalues defined over the ground field.

The key theorem about hardly ramified representations is the following.

- [hardly\_ramified\_reducible](hardly-ramified-reducible.md)

Note that this (deep) claim is a consequence of Serre's conjecture ([Serre 1987](https://doi.org/10.1215/S0012-7094-87-05413-5)), now a theorem of Khare and Wintenberger ([Khare and Wintenberger 2009](https://doi.org/10.1007/s00222-009-0206-6)), and indeed we shall use methods introduced by Khare and Wintenberger to prove this special case of Serre's conjecture. Given this result, we can deduce Theorem [Wiles,Taylor–Wiles, Ribet,…](../../first-reductions-of-the-problem/reduction-to-two-big-theorems/wiles-frey.md) (which we restate here) easily:

- [Wiles\_Frey\_again](wiles-frey-again.md)

Our job of reducing FLT to theorems of the 1980s is hence reduced to proving Theorem [hardly\_ramified\_reducible](hardly-ramified-reducible.md).

## Hardly ramified mod $p$ representations are reducible

In this section we will state three theorems, from which Theorem [hardly\_ramified\_reducible](hardly-ramified-reducible.md) easily follows.

Firstly, we claim that an irreducible hardly ramified mod $\ell$ representation lifts to an $\ell$-adic representation.

- [hardly\_ramified\_lifts](hardly-ramified-lifts.md)

Next we claim that a hardly ramified $\ell$-adic representation “spreads out” to a compatible family of hardly ramified $q$-adic representations for all odd primes $q$ (note that we have not made a definition of a hardly ramified 2-adic representation).

- [hardly\_ramified\_spreads\_out](hardly-ramified-spreads-out.md)

In particular, we can “move” from an irreducible hardly ramified mod $\ell$ representation to a hardly ramified 3-adic representation, and hence to a hardly ramified mod 3 representation.

However, we can essentially completely classify the hardly ramified mod 3 Galois representations:

- [hardly\_ramified\_mod3\_reducible](hardly-ramified-mod3-reducible.md)

And we can use this to essentially completely classify the hardly ramified 3-adic Galois representations:

- [hardly\_ramified\_3adic\_reducible](hardly-ramified-3adic-reducible.md)

Theorem [hardly\_ramified\_reducible](hardly-ramified-reducible.md) (if $\ell\geq 3$ is a prime and $\overline{\rho}:\operatorname{Gal}(\overline{\mathbb{Q}}/\mathbb{Q})\to\operatorname{GL}_2(\mathbb{Z}/\ell\mathbb{Z})$ is hardly ramified, then $\overline{\rho}$ is reducible) is an easy consequence of these theorems, as we now show.

*The proof of [Theorem hardly\_ramified\_reducible](hardly-ramified-reducible.md) is shown with its statement.*

What remains then (modulo several results which were known in the 1980s), is to prove the three theorems [hardly\_ramified\_lifts](hardly-ramified-lifts.md), [hardly\_ramified\_spreads\_out](hardly-ramified-spreads-out.md) and [hardly\_ramified\_3adic\_reducible](hardly-ramified-3adic-reducible.md). By far the easiest is theorem [hardly\_ramified\_3adic\_reducible](hardly-ramified-3adic-reducible.md); this follows from old estimates of Fontaine (ultimately relying on bounds for root discriminants due to Odlyzko and Poitou), originally developed to prove that there was no nontrivial abelian scheme over $\mathbb{Z}.$ The other two theorems are deeper, and both use modern variants of Wiles' $R=T$ machinery.

We have not yet written any more LaTeX on how to proceed further; the rest of this blueprint should be considered as more unfocussed thoughts.
