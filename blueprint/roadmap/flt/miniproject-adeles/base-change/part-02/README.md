---
navigation: transparent
---

# IsDedekindDomain.pi\_tensorProdu… to NumberField.InfiniteAdeleRing.pi…

- [IsDedekindDomain.pi\_tensorProduct](isdedekinddomain-pi-tensorproduct.md)

Recall that $\mathbb{A}_K^\infty$ is the finite adeles of $K$, defined as the restricted product of the $K_v$ with respect to the $A_v$, where $v$ runs through the nonzero primes of $A$. Let $R$ denote the restricted product of the $B\otimes_A K_v$ with respect to the $B\otimes_A A_v$.

- [IsDedekindDomain.FiniteAdeleRing.IntegraltensorProductAlgEquiv\_aux1](isdedekinddomain-finiteadelering-integraltensorp.md)

Recall from earlier in this section that if $v$ is a finite place of $A$ then the natural map from $B\otimes_A K_v$ to $L\otimes_KK_v$ is an isomorphism, and recall from the previous section that the natural map from $L\otimes_KK_v$ to $\prod_{w|v}L_w$ was also an isomorphism. This isomorphism sends $B\otimes_A A_v$ to $\prod_{w|v}B_w$ (I thank Matthew Jasper for pointing out to me that this statement was true at all primes, not just at unramified primes). Finally, the set of $w$ of $B$ dividing a fixed place $v$ of $A$ is finite. Let's now formalize the abstract statement which we need. Rather than following the notation for restricted product in the literature and writing $\mathbb{A}_K^\infty=\prod'_vK_v$ with the $\mathcal{O}_v$ implicit, we will write $\prod'_v(K_v,\mathcal{O}_v)$ in the below.

- [RestrictedProduct.relabelIso](restrictedproduct-relabeliso.md)
- [IsDedekindDomain.FiniteAdeleRing.IntegraltensorProductAlgEquiv\_aux2](isdedekinddomain-finiteadelering-integraltensorp-2.md)

From this, we can deduce the theorem we claimed earlier:

- [IsDedekindDomain.FiniteAdeleRing.baseChangeIntegralAlgEquiv](isdedekinddomain-finiteadelering-basechangeinteg.md)

Because this map factors through the isomorphism $B\otimes_A\mathbb{A}_K^\infty\to L\otimes_K\mathbb{A}_K^\infty$ we can finally deduce that the natural map $L\otimes_K\mathbb{A}_K^\infty\to\mathbb{A}_L^\infty$ is an algebraic isomorphism.

*The proof of [Theorem IsDedekindDomain.FiniteAdeleRing.baseChangeAlgEquiv](../part-01/isdedekinddomain-finiteadelering-basechangealgeq.md) is shown with its statement.*

We still need to talk about topologies though, so let's finish by doing this. Let's start with some trivialities, expressed as definitions rather than theorems because they're constructions.

- [Definition: If $X_v$ and $Y_v$ are families of topological…](definition-adeleminiproject-1.md)
- [Definition: If all the $f_v$ are homeomorphisms identifying…](definition-adeleminiproject-2.md)

We now allow a slight change of index set. Unfortunately I don't think that we can deduce the results just stated above from this one, in Lean, because the product of $Y_w$ over a set of size 1 is not definitionally equal to $Y_w$.

Recall definition [RestrictedProduct.relabelIso](restrictedproduct-relabeliso.md), giving us a bijection between two restricted products.

- [Theorem: In the same setup as definition RestrictedProduct.relabelIso…](theorem-adeleminiproject-1.md)
- [Corollary: $\mathbb{\mathbb{A}_L^\infty}$ is homeomorphic…](corollary-adeleminiproject-1.md)

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

- [Lemma: If $X_v$ and $Y_v$ are topological spaces…](lemma-adeleminiproject-1.md)

As a corollary one can prove by induction on $n$ that the restricted product of $n$th powers is homeomorphic to the $n$th power of the restricted product and this is the result we require.

## Base change for infinite adeles

Recall that if $K$ is a number field then the infinite adeles of $K$ are defined to be the product $\prod_{v\mid\infty} K_v$ of all the completions of $K$ at the infinite places.

The result we need here is that if $L/K$ is a finite extension of number fields, then the map $K\to L$ extends to a continuous $K$-algebra map $K_\infty\to L_\infty$, and thus to a continuous $L$-algebra isomorphism $L\otimes_KK_\infty\to L_\infty$. Perhaps a cheap proof would be to deduce it from the fact that $K_\infty=K\otimes_{\mathbb{Q}}\mathbb{R}$.

The overall strategy is to first establish, for each infinite place $v$ of $K$, homeomorphisms between for the completion $K_v$ and the product $\prod_{w\mid v}L_w$ of completions of $L$ at all infinite places $w$ of $L$ lying above $v$. We then use these homeomorphisms to construct base change for the infinite adele ring.

### Weak approximation at infinite places

First, we require a preliminary result that $K$ is dense inside any product of completions $\prod_{v\in S} K_v$ of $K$ at infinite places.

- [NumberField.InfinitePlace.Completion.denseRange\_algebraMap\_subtype\_pi](numberfield-infiniteplace-completion-denserange.md)

### Dimensionality of $\prod_{w\mid v}L_w$ as a $K_v$-vector space

This subsection contains a result that the $K_v$-dimension of $L \otimes_K K_v$ is equal to the $K_v$-dimension of $\prod_{w\mid v}L_w$.

- [NumberField.InfinitePlace.Completion.finrank\_pi\_eq\_finrank\_tensorProduct](numberfield-infiniteplace-completion-finrank-pi.md)

### Base change at infinite places

- [NumberField.InfinitePlace.Completion.piExtension](numberfield-infiniteplace-completion-piextension.md)

The map in [NumberField.InfinitePlace.Completion.piExtension](numberfield-infiniteplace-completion-piextension.md) can be lifted to an $L$-algebra homomorphism defined on $L\otimes_K K_v$.

- [NumberField.InfinitePlace.Completion.baseChange](numberfield-infiniteplace-completion-basechange.md)
- [NumberField.InfinitePlace.Completion.baseChange\_surjective](numberfield-infiniteplace-completion-basechange-2.md)
- [NumberField.InfinitePlace.Completion.baseChange\_injective](numberfield-infiniteplace-completion-basechange-3.md)

We have established that the map of Definition [NumberField.InfinitePlace.Completion.baseChange](numberfield-infiniteplace-completion-basechange.md) gives an $L$-algebra isomorphism between $L\otimes_K K_v$ and $\prod_{w\mid v}L_w$. The left-hand side is given the $K_v$-module topology, while we show that the right-hand side also has the $K_v$-module topology.

- [NumberField.InfinitePlace.Completion.instIsModuleTopologyValEqComapAlgebraMap\_fLT](numberfield-infiniteplace-completion-instismodul.md)
- [NumberField.InfinitePlace.Completion.baseChangeEquiv](numberfield-infiniteplace-completion-basechangee.md)
- [NumberField.InfinitePlace.Completion.piEquiv](numberfield-infiniteplace-completion-piequiv.md)

### Base change for the infinite adele ring

First, we induce a $K_{\infty}$-algebra on $L_{\infty}$ from the action of each $K_v$ on $\prod_{w\mid v}L_w$. Specifically, this means that for $x \in K_{\infty}$ and $y \in L_{\infty}$, we have $(x \cdot y)_w = x_{v_w} \cdot y_w$, where $v_w$ is the restriction of $w$ to $K$. We show that $L_{\infty}$ has the $K_{\infty}$-module topology.

- [NumberField.InfiniteAdeleRing.piEquiv](numberfield-infiniteadelering-piequiv.md)
