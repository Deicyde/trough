# Base change

The “theorem” we want is that if $L/K$ is a finite extension of number fields, then $\mathbb{A}_L=L\otimes_K\mathbb{A}_K$. This isn't a theorem though, this is actually a *definition* (the map between the two objects) and a theorem about the definition (that it's an isomorphism). In fact the full claim is that it is both a homeomorphism and an $L$-algebra isomorphism. Before we can prove the theorem, we need to make the definition.

Recall that the adeles $\mathbb{A}_K$ of a number field is a product $\mathbb{A}_K^\infty\times K_\infty$ of the finite adeles and the infinite adeles. So our “theorem” follows immediately from the “theorem”s that $\mathbb{A}_L^\infty=L\otimes_K\mathbb{A}_K^\infty$ and $L_\infty=L\otimes_KK_\infty$ (both of these equalities mean an algebraic and topological isomorphism). We may thus treat the finite and infinite results separately.

## Base change for nonarchimedean completions.

As pointed out above, the theory of finite adeles works fine for Dedekind domains. So for the time being let $A$ be a Dedekind domain. Recall that the *height one spectrum* of $A$ is the nonzero prime ideals of $A$. Note that because we stick to the literature, rather than to common sense, fields are Dedekind domains in mathlib, and the height one spectrum of a field is empty. The reason I don't like allowing fields to be Dedekind domains is that geometrically the definition of Dedekind domain in the literature is “smooth affine curve, or a point”. But many theorems in algebraic geometry begin “let $C$ be a smooth curve”, rather than “let $C$ be a smooth curve or a point”.

Let $K$ be the field of fractions of $A$. If $v$ is in the height one spectrum of $A$, then we can put the $v$-adic topology on $A$ and on $K$, and consider the completions $A_v$ and $K_v$. The finite adele ring $\mathbb{A}_{A,K}^\infty$ is defined to be the restricted product of the $K_v$ with respect to the $A_v$, as $v$ runs over the height one spectrum of $A$. It is topologised by making $\prod_v A_v$ open with the product topology (here $A_v$ has the $v$-adic topology).

Now let $L/K$ be a finite separable extension, and let $B$ be the integral closure of $A$ in $L$. We want to relate the finite adeles of $K$ and of $L$. We work place by place, starting by fixing one place $w$ of $B$ and analysing the relation of $L_w$ and $B_w$ to the completions $K_v$ and $A_v$ where $v$ is the place of $A$ dividing $w$.

So let $w$ be a nonzero prime ideal of $B$. Say $w$ lies over $v$, a prime ideal of $A$. Then we can put the $w$-adic topology on $L$ and the $v$-adic topology on $K$. Furthermore we can equip $K$ with an additive $v$-adic valuation, that is, a function also called $v$ from $K$ to $\mathbb{Z}\cup\{\infty\}$ normalised so that if $\pi$ is a uniformiser for $v$ then $v(\pi)=1$. Similarly we consider $w$ as a function from $L$ to $\mathbb{Z}\cup\{\infty\}$. The next lemma explains how these valuations are related.

## [IsDedekindDomain.HeightOneSpectr… to pi\_tensorProduct\_of\_finitePre…](part-01/README.md)

- [IsDedekindDomain.HeightOneSpectrum.valuation\_comap](part-01/isdedekinddomain-heightonespectrum-valuation-com.md)
- [IsDedekindDomain.HeightOneSpectrum.Extension.adicCompletionSemialgHom](part-01/isdedekinddomain-heightonespectrum-extension-adi.md)
- [IsDedekindDomain.HeightOneSpectrum.Extension.valued\_adicCompletionSemialgHom](part-01/isdedekinddomain-heightonespectrum-extension-val.md)
- [IsDedekindDomain.HeightOneSpectrum.Extension.adicCompletionSemialgHom\_image\_adicCompletionIntegers](part-01/isdedekinddomain-heightonespectrum-extension-adi-2.md)
- [IsDedekindDomain.HeightOneSpectrum.adicCompletion.instIsModuleTopology](part-01/isdedekinddomain-heightonespectrum-adiccompletio.md)
- [IsDedekindDomain.HeightOneSpectrum.Extension.finite](part-01/isdedekinddomain-heightonespectrum-extension-fin.md)
- [IsDedekindDomain.HeightOneSpectrum.adicCompletion.semialgHomPi](part-01/isdedekinddomain-heightonespectrum-adiccompletio-2.md)
- [IsDedekindDomain.HeightOneSpectrum.adicCompletion.baseChangeAlgEquiv](part-01/isdedekinddomain-heightonespectrum-adiccompletio-3.md)
- [IsDedekindDomain.HeightOneSpectrum.adicCompletion.instIsModuleTopologyPi](part-01/isdedekinddomain-heightonespectrum-adiccompletio-4.md)
- [IsDedekindDomain.HeightOneSpectrum.adicCompletion.baseChangeContinuousAlgEquiv](part-01/isdedekinddomain-heightonespectrum-adiccompletio-5.md)
- [IsDedekindDomain.HeightOneSpectrum.range\_baseChange\_comp\_tensorAdicCompletionTo\_eq\_pi](part-01/isdedekinddomain-heightonespectrum-range-basecha.md)
- [IsDedekindDomain.FiniteAdeleRing.mapSemialgHom](part-01/isdedekinddomain-finiteadelering-mapsemialghom.md)
- [IsDedekindDomain.FiniteAdeleRing.baseChangeAlgEquiv](part-01/isdedekinddomain-finiteadelering-basechangealgeq.md)
- [IsDedekindDomain.FiniteAdeleRing.baseChangeContinuousAlgEquiv](part-01/isdedekinddomain-finiteadelering-basechangeconti.md)
- [IsDedekindDomain.dvd\_norm](part-01/isdedekinddomain-dvd-norm.md)
- [IsDedekindDomain.AKLB.surjective\_tensorProduct\_map](part-01/isdedekinddomain-aklb-surjective-tensorproduct-m.md)
- [IsDedekindDomain.FiniteAdeleRing.tensorProduct\_algEquiv](part-01/isdedekinddomain-finiteadelering-tensorproduct-a.md)
- [IsDedekindDomain.AKLB.tensorProduct\_module\_algEquiv](part-01/isdedekinddomain-aklb-tensorproduct-module-algeq.md)
- [IsDedekindDomain.AKLB.finitePresentation](part-01/isdedekinddomain-aklb-finitepresentation.md)
- [pi\_tensorProduct\_of\_finitePresentation](part-01/pi-tensorproduct-of-finitepresentation.md)

## [IsDedekindDomain.pi\_tensorProdu… to NumberField.InfiniteAdeleRing.pi…](part-02/README.md)

- [IsDedekindDomain.pi\_tensorProduct](part-02/isdedekinddomain-pi-tensorproduct.md)
- [IsDedekindDomain.FiniteAdeleRing.IntegraltensorProductAlgEquiv\_aux1](part-02/isdedekinddomain-finiteadelering-integraltensorp.md)
- [RestrictedProduct.relabelIso](part-02/restrictedproduct-relabeliso.md)
- [IsDedekindDomain.FiniteAdeleRing.IntegraltensorProductAlgEquiv\_aux2](part-02/isdedekinddomain-finiteadelering-integraltensorp-2.md)
- [IsDedekindDomain.FiniteAdeleRing.baseChangeIntegralAlgEquiv](part-02/isdedekinddomain-finiteadelering-basechangeinteg.md)
- [Definition: If $X_v$ and $Y_v$ are families of topological…](part-02/definition-adeleminiproject-1.md)
- [Definition: If all the $f_v$ are homeomorphisms identifying…](part-02/definition-adeleminiproject-2.md)
- [Theorem: In the same setup as definition RestrictedProduct.relabelIso…](part-02/theorem-adeleminiproject-1.md)
- [Corollary: $\mathbb{\mathbb{A}_L^\infty}$ is homeomorphic…](part-02/corollary-adeleminiproject-1.md)
- [Lemma: If $X_v$ and $Y_v$ are topological spaces…](part-02/lemma-adeleminiproject-1.md)
- [NumberField.InfinitePlace.Completion.denseRange\_algebraMap\_subtype\_pi](part-02/numberfield-infiniteplace-completion-denserange.md)
- [NumberField.InfinitePlace.Completion.finrank\_pi\_eq\_finrank\_tensorProduct](part-02/numberfield-infiniteplace-completion-finrank-pi.md)
- [NumberField.InfinitePlace.Completion.piExtension](part-02/numberfield-infiniteplace-completion-piextension.md)
- [NumberField.InfinitePlace.Completion.baseChange](part-02/numberfield-infiniteplace-completion-basechange.md)
- [NumberField.InfinitePlace.Completion.baseChange\_surjective](part-02/numberfield-infiniteplace-completion-basechange-2.md)
- [NumberField.InfinitePlace.Completion.baseChange\_injective](part-02/numberfield-infiniteplace-completion-basechange-3.md)
- [NumberField.InfinitePlace.Completion.instIsModuleTopologyValEqComapAlgebraMap\_fLT](part-02/numberfield-infiniteplace-completion-instismodul.md)
- [NumberField.InfinitePlace.Completion.baseChangeEquiv](part-02/numberfield-infiniteplace-completion-basechangee.md)
- [NumberField.InfinitePlace.Completion.piEquiv](part-02/numberfield-infiniteplace-completion-piequiv.md)
- [NumberField.InfiniteAdeleRing.piEquiv](part-02/numberfield-infiniteadelering-piequiv.md)

## [NumberField.InfiniteAdeleRing.in… to NumberField.AdeleRing.baseChange…](part-03/README.md)

- [NumberField.InfiniteAdeleRing.instIsModuleTopology\_fLT](part-03/numberfield-infiniteadelering-instismoduletopolo.md)
- [NumberField.InfiniteAdeleRing.baseChangeAlgEquiv](part-03/numberfield-infiniteadelering-basechangealgequiv.md)
- [NumberField.InfiniteAdeleRing.baseChangeEquiv](part-03/numberfield-infiniteadelering-basechangeequiv.md)
- [NumberField.AdeleRing.baseChangeEquiv](part-03/numberfield-adelering-basechangeequiv.md)
- [NumberField.AdeleRing.baseChange\_moduleTopology](part-03/numberfield-adelering-basechange-moduletopology.md)
