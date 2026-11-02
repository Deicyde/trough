---
navigation: transparent
---

# IsDedekindDomain.HeightOneSpectr… to pi\_tensorProduct\_of\_finitePre…

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
- [IsDedekindDomain.HeightOneSpectrum.adicCompletion.baseChangeContinuousAlgEquiv](isdedekinddomain-heightonespectrum-adiccompletio-5.md)

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

- [IsDedekindDomain.dvd\_norm](isdedekinddomain-dvd-norm.md)

**Remark.** Is this already in mathlib?

*Proof.* Let $a=N_{L/K}(b)$, the norm. This is known to take nonzero elements of $L$ to nonzero elements of $K$ (because the norm is the determinant of an invertible linear map) and integral elements to integral elements. Furthermore $a/b\in L$ is the the product of the conjugates of $b$ in some normal closure of $L$, and hence it is integral, and thus in $B$.

- [IsDedekindDomain.AKLB.surjective\_tensorProduct\_map](isdedekinddomain-aklb-surjective-tensorproduct-m.md)
- [IsDedekindDomain.FiniteAdeleRing.tensorProduct\_algEquiv](isdedekinddomain-finiteadelering-tensorproduct-a.md)
- [IsDedekindDomain.AKLB.tensorProduct\_module\_algEquiv](isdedekinddomain-aklb-tensorproduct-module-algeq.md)

We now need to explain how tensor products sometimes commute with restricted products. Something we will need along the way is

- [IsDedekindDomain.AKLB.finitePresentation](isdedekinddomain-aklb-finitepresentation.md)

The reason we care about this is the following.

- [pi\_tensorProduct\_of\_finitePresentation](pi-tensorproduct-of-finitepresentation.md)
