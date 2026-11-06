---
navigation: transparent
---

# IsDedekindDomain.HeightOneSpectr… to NumberField.InfinitePlace.Comple…

- [IsDedekindDomain.HeightOneSpectrum.valuation\_comap](isdedekinddomain-heightonespectrum-valuation-com.md)
- [IsDedekindDomain.HeightOneSpectrum.Extension.adicCompletionSemialgHom](isdedekinddomain-heightonespectrum-extension-adi.md)
- [IsDedekindDomain.HeightOneSpectrum.Extension.valued\_adicCompletionSemialgHom](isdedekinddomain-heightonespectrum-extension-val.md)
- [IsDedekindDomain.HeightOneSpectrum.Extension.adicCompletionSemialgHom\_image\_adicCompletionIntegers](isdedekinddomain-heightonespectrum-extension-adi-2.md)
- [IsDedekindDomain.HeightOneSpectrum.adicCompletion.instIsModuleTopology](isdedekinddomain-heightonespectrum-adiccompletio.md)

Because of the commutative diagram

*(A commutative diagram in the source is not reproduced here.)*

we can view $L_w$ as an $L\otimes_KK_v$-algebra.

Now instead of fixing $w$ upstairs, we fix $v$ downstairs and consider all $w$ lying over it at once. So say $v$ is in the height one spectrum of $A$.

- [IsDedekindDomain.HeightOneSpectrum.Extension.finite](isdedekinddomain-heightonespectrum-extension-fin.md)

We write $w|v$ to denote the fact that $w$ is a prime of $B$ above $v$ of $A$.

- [IsDedekindDomain.HeightOneSpectrum.adicCompletion.semialgHomPi](isdedekinddomain-heightonespectrum-adiccompletio-2.md)

Because $K_v\to\prod_{w|v}L_w$ lies over $K\to L$, there's an induced $L$-algebra map $L\otimes_KK_v\to\prod_{w|v}L_w$. We are now able to state one of the key results in this section. The proof is probably the hardest proof in this section to formalize.

- [IsDedekindDomain.HeightOneSpectrum.adicCompletion.baseChangeAlgEquiv](isdedekinddomain-heightonespectrum-adiccompletio-3.md)
- [IsDedekindDomain.HeightOneSpectrum.adicCompletion.instIsModuleTopologyPi](isdedekinddomain-heightonespectrum-adiccompletio-4.md)

We now start thinking about what's going on at the integral level. We write $A_v$ for the integers of $K_v$ and $B_w$ for the integers of $L_w$.

- [IsDedekindDomain.HeightOneSpectrum.range\_baseChange\_comp\_tensorAdicCompletionTo\_eq\_pi](isdedekinddomain-heightonespectrum-range-basecha.md)

A summary of what we have so far: for all finite places $v$ of $A$ we have shown that the natural map $L\otimes_KK_v\to\prod_wL_w$ is an isomorphism of $L$-algebras, and that if $L\otimes_KK_v$ has the $K_v$-module topology and each $L_w$ has the valuation topology then this map is also a homeomorphism. Furthermore we have shown that there is an induced algebraic isomorphism $B\otimes_AA_v\equiv\prod_w B_w$ on the subrings of the left and right hand sides.

Recall that the finite adeles $\mathbb{A}_{A,K}^\infty$ is defined in mathlib to be the restricted product of the $K_v$ with respect to the $A_v$, equipped with a certain restricted product topology (which is not the subspace topology of the product topology, indeed $\prod_v A_v$ is open in this topology). We have seen in definition [IsDedekindDomain.HeightOneSpectrum.Extension.adicCompletionSemialgHom](isdedekinddomain-heightonespectrum-extension-adi.md) that there's a map $K_v\to L_w$ if $w|v$, extending $K\to L$, and we have seen in theorem [IsDedekindDomain.HeightOneSpectrum.Extension.adicCompletionSemialgHom\_image\_adicCompletionIntegers](isdedekinddomain-heightonespectrum-extension-adi-2.md) that this sends $A_v$ to $B_w$. We conclude

- [IsDedekindDomain.FiniteAdeleRing.mapSemialgHom](isdedekinddomain-finiteadelering-mapsemialghom.md)

Hence there's a natural $L$-algebra homomorphism $L\otimes_K\mathbb{A}_{A,K}^\infty\to\mathbb{A}_{B,L}^\infty$.

Our next goal in this section is the following two results. First the algebraic claim:

- [IsDedekindDomain.FiniteAdeleRing.baseChangeAlgEquiv](isdedekinddomain-finiteadelering-basechangealgeq.md)

Now $L\otimes_K\mathbb{A}_{A,K}^\infty$ is an $\mathbb{A}_{A,K}^\infty$-module and hence can be given the $\mathbb{A}_{A,K}^\infty$-module topology. We also claim

- [IsDedekindDomain.FiniteAdeleRing.baseChangeContinuousAlgEquiv](isdedekinddomain-finiteadelering-basechangeconti.md)

Informally, the proofs are simple: componentwise we know that $L\otimes_KK_v$ is isomorphic both algebraically and topologically to $\prod_{w|v}L_w$, and that this isomorphism sends the open set $B\otimes_AA_v$ homeomorphically onto $\prod_{w|v}B_w$, so now it's “just a case of putting everything together”. Formally, we really need to spell this out, as there is a lot going on. We do this in the next subsection.

## Base change for nonarchimedean completions.

As usual we are in the AKLB set-up, so in particular $K$ is the field of fractions of the Dedekind domain $A$, $L/K$ is a finite separable extension, and $B$ is the integral closure of $A$ in $L$. The goal in this subsection is to spell out the following argument: Assume that $L\otimes_KK_v\cong\prod_{w|v}L_w$ algebraically and topologically for all $v$, with $B\otimes_AA_v$ identified with $\prod_{w|v}B_w$. Then $L\otimes_K\mathbb{A}_K^\infty\cong\mathbb{A}_L^\infty$, algebraically and topologically. Here the tensor products $L\otimes_K R$ (for $R$ a $K$-algebra with a topology) are all being given the $R$-module topology, which if we choose a basis for $L/K$ is just the product topology.

We start with the following observation. If $M$ is a $K$-module then there's a canonical map $B\otimes_AM\to L\otimes_KM$ sending $b\otimes m$ to $b\otimes m$ (this follows from the universal property of the tensor product). Our first goal is to show that this map is an isomorphism. Let us establish some lemmas first.

**Remark.** Is this already in mathlib?

*Proof.* Let $a=N_{L/K}(b)$, the norm. This is known to take nonzero elements of $L$ to nonzero elements of $K$ (because the norm is the determinant of an invertible linear map) and integral elements to integral elements. Furthermore $a/b\in L$ is the the product of the conjugates of $b$ in some normal closure of $L$, and hence it is integral, and thus in $B$.

- [IsDedekindDomain.AKLB.tensorProduct\_module\_algEquiv](isdedekinddomain-aklb-tensorproduct-module-algeq.md)

We now need to explain how tensor products sometimes commute with restricted products. Something we will need along the way is

The reason we care about this is the following.

Recall that $\mathbb{A}_K^\infty$ is the finite adeles of $K$, defined as the restricted product of the $K_v$ with respect to the $A_v$, where $v$ runs through the nonzero primes of $A$. Let $R$ denote the restricted product of the $B\otimes_A K_v$ with respect to the $B\otimes_A A_v$.

Recall from earlier in this section that if $v$ is a finite place of $A$ then the natural map from $B\otimes_A K_v$ to $L\otimes_KK_v$ is an isomorphism, and recall from the previous section that the natural map from $L\otimes_KK_v$ to $\prod_{w|v}L_w$ was also an isomorphism. This isomorphism sends $B\otimes_A A_v$ to $\prod_{w|v}B_w$ (I thank Matthew Jasper for pointing out to me that this statement was true at all primes, not just at unramified primes). Finally, the set of $w$ of $B$ dividing a fixed place $v$ of $A$ is finite. Let's now formalize the abstract statement which we need. Rather than following the notation for restricted product in the literature and writing $\mathbb{A}_K^\infty=\prod'_vK_v$ with the $\mathcal{O}_v$ implicit, we will write $\prod'_v(K_v,\mathcal{O}_v)$ in the below.

From this, we can deduce the theorem we claimed earlier:

Because this map factors through the isomorphism $B\otimes_A\mathbb{A}_K^\infty\to L\otimes_K\mathbb{A}_K^\infty$ we can finally deduce that the natural map $L\otimes_K\mathbb{A}_K^\infty\to\mathbb{A}_L^\infty$ is an algebraic isomorphism.

*The proof of [Theorem IsDedekindDomain.FiniteAdeleRing.baseChangeAlgEquiv](isdedekinddomain-finiteadelering-basechangealgeq.md) is shown with its statement.*

We still need to talk about topologies though, so let's finish by doing this. Let's start with some trivialities, expressed as definitions rather than theorems because they're constructions.

We now allow a slight change of index set. Unfortunately I don't think that we can deduce the results just stated above from this one, in Lean, because the product of $Y_w$ over a set of size 1 is not definitionally equal to $Y_w$.

Recall definition [RestrictedProduct.relabelIso](https://github.com/ImperialCollegeLondon/FLT/blob/a3210204ad8876e851e32f73dd97d882bf1ccd0a/blueprint/src/chapter/AdeleMiniproject.tex#L556), giving us a bijection between two restricted products.

Recall that if

$$
R
$$

is a commutative ring, and two

$$
R
$$

-modules both have the

$$
R
$$

-module topology, then any

$$
R
$$

-linear morphism between them is automatically continuous. We know that $\mathbb{A}_L^\infty$ is $\mathbb{A}_K^\infty$-linearly isomorphic to $L\otimes_K\mathbb{A}_K^\infty$ and our claim is that if $L\otimes_K\mathbb{A}_K^\infty$ is given the $\mathbb{A}_K^\infty$-module topology then this isomorphism is also a homeomorphism; to prove this, we thus just need to check that $\mathbb{A}_L^\infty$ has the $\mathbb{A}_K^\infty$-module topology. Equivalently, by the previous result, we need to check that the restricted product topology on the $\mathbb{A}_K^\infty$-algebra $\prod'_v(B\otimes_AK_v,B\otimes_AA_v)$ is the $\mathbb{A}_K^\infty$-module topology.

We now need to make restricted products of modules into modules over restricted product of rings. The API, which should be straightforward so we don't give details here, is: if $R_v$ are rings with subrings $S_v$ and if $M_v$ are $R_v$-modules with $S_v$-stable submodules $N_v$, then $\prod'_v(M_v,N_v)$ is naturally a module over $\prod'_v(R_v,S_v)$, and that $R_v$-morphisms $M_v\to M_v'$ sending $N_v$ to $N_v'$ induce $\prod'_v(R_s,S_v)$-linear maps $\prod'_v(M_v,N_v)\to\prod'_v(M'_v,N'_v)$. From this one deduces that isomorphisms on the factors induce isomorphisms on the restricted products.

Now $A_v$ is a PID, so $B\otimes_AA_v$ is free (as it is finitely-generated and torsion-free). This means that there is an isomorphism $B\otimes_AA_v\cong(A_v)^n$, which extends to an isomorphism $B\otimes_AK_v\cong K_v^n$. These isomorphisms are also homeomorphisms. If we fix such isomorphisms for all $v$ then we get an induced $\mathbb{A}_K^\infty$-module isomorphism + homeomorphism $\prod'_v(B\otimes_AK_v,B\otimes_AA_v)=\prod'_v(K_n^n,A_v^n)$. So it suffices to prove that the $\prod'_v(K_v,A_v)$-module $\prod'_v(K_v^n,A_v^n)$ has the $\prod'_v(K_v,A_v)$-module topology. This follows from the fact that the product topology on two modules with the module topology is the module topology (a fact in mathlib) and the following result.

As a corollary one can prove by induction on $n$ that the restricted product of $n$th powers is homeomorphic to the $n$th power of the restricted product and this is the result we require.

## Base change for infinite adeles

Recall that if $K$ is a number field then the infinite adeles of $K$ are defined to be the product $\prod_{v\mid\infty} K_v$ of all the completions of $K$ at the infinite places.

The result we need here is that if $L/K$ is a finite extension of number fields, then the map $K\to L$ extends to a continuous $K$-algebra map $K_\infty\to L_\infty$, and thus to a continuous $L$-algebra isomorphism $L\otimes_KK_\infty\to L_\infty$. Perhaps a cheap proof would be to deduce it from the fact that $K_\infty=K\otimes_{\mathbb{Q}}\mathbb{R}$.

The overall strategy is to first establish, for each infinite place $v$ of $K$, homeomorphisms between for the completion $K_v$ and the product $\prod_{w\mid v}L_w$ of completions of $L$ at all infinite places $w$ of $L$ lying above $v$. We then use these homeomorphisms to construct base change for the infinite adele ring.

### Weak approximation at infinite places

First, we require a preliminary result that $K$ is dense inside any product of completions $\prod_{v\in S} K_v$ of $K$ at infinite places.

- [NumberField.InfinitePlace.Completion.denseRange\_algebraMap\_subtype\_pi](numberfield-infiniteplace-completion-denserange.md)

### Base change at infinite places

- [NumberField.InfinitePlace.Completion.piExtension](numberfield-infiniteplace-completion-piextension.md)

The map in [NumberField.InfinitePlace.Completion.piExtension](numberfield-infiniteplace-completion-piextension.md) can be lifted to an $L$-algebra homomorphism defined on $L\otimes_K K_v$.

- [NumberField.InfinitePlace.Completion.baseChange](numberfield-infiniteplace-completion-basechange.md)
- [NumberField.InfinitePlace.Completion.baseChange\_surjective](numberfield-infiniteplace-completion-basechange-2.md)
- [NumberField.InfinitePlace.Completion.baseChange\_injective](numberfield-infiniteplace-completion-basechange-3.md)

We have established that the map of Definition [NumberField.InfinitePlace.Completion.baseChange](numberfield-infiniteplace-completion-basechange.md) gives an $L$-algebra isomorphism between $L\otimes_K K_v$ and $\prod_{w\mid v}L_w$. The left-hand side is given the $K_v$-module topology, while we show that the right-hand side also has the $K_v$-module topology.

- [NumberField.InfinitePlace.Completion.instIsModuleTopologyValEqComapAlgebraMap\_fLT](numberfield-infiniteplace-completion-instismodul.md)
