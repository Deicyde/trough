# Initial definitions

## Scaling Haar measure on a group

Let $A$ be a locally compact topological additive abelian group. There's then a regular additive Haar measure $\mu$ on $A$, unique up to a positive scalar factor. If $\phi:(A,+)\cong(A,+)$ is a homeomorphism and an additive automorphism of $A$, then we can push forward $\mu$ along $\phi$ to get a second measure $\phi_*\mu$ on $A$, with the property that $(\phi_*\mu)(X)=\mu(\phi^{-1}X)$ for any Borel subset $X$ of $A$.

Now $\phi_*\mu$ is a translation-invariant and regular measure, and hence also a Haar measure on $A.$ It must thus differ from $\mu$ by a positive scalar factor, which we call $d_A(\phi)$. There is a choice of normalization here between $d_A(\phi)$ and $d_A(\phi)^{-1}$, so let us be more precise.

- [MeasureTheory.addEquivAddHaarChar](measuretheory-addequivaddhaarchar.md)

To give an example, if $\phi$ is multiplication by $2$ on the real numbers, if $X=[0,1]$, and if $\mu$ is Lebesgue measure on the Borel subsets of $\mathbb{R}$, we have that $\phi_*\mu(X)=\mu(\phi^{-1}(X))=\mu([0,1/2])=1/2$, so $1=d_A(\phi)/2$ meaning that $d_A(\phi)=2$. Similarly if $\phi$ is multiplication by $-2$ and $X=[0,1]$ then $\phi^{-1}(X)=[-1/2,0]$ which again has measure $1/2$, so $d_A(\phi)$ is 2 again.

Strictly speaking our definition of $d_A(\phi)$ depends on the choice of regular Haar measure $\mu$. Note that mathlib offers a fixed Borel regular Haar measure MeasureTheory.Measure.haar on any locally compact topological group and the actual definition of $d_A$ in the code uses this definition. Note also that the code defines everything for multiplicative groups and uses @\[to\_additive\] to deduce the corresponding results for additive groups.

Here are some basic results about this construction. In all of them, $A$ is a locally compact topological group and $\phi:A\to A$ is a group isomorphism and a homeomorphism. The first lemma shows that the definition of $d_A(\phi)$ is indeed independent of the choice of Haar measure.

- [MeasureTheory.addEquivAddHaarChar\_eq](measuretheory-addequivaddhaarchar-eq.md)
- [MeasureTheory.addEquivAddHaarChar\_smul\_map](measuretheory-addequivaddhaarchar-smul-map.md)

We can of course also pull a Haar measure $\mu$ back along a homeomorphism $\phi$, giving a measure $\phi^*\mu$ such that $\phi^*\mu(X)=\mu(\phi(X))$.

- [MeasureTheory.addEquivAddHaarChar\_comap](measuretheory-addequivaddhaarchar-comap.md)

Now let $\mu$ be any regular additive Haar measure on $A$.

- [MeasureTheory.addEquivAddHaarChar\_smul\_preimage](measuretheory-addequivaddhaarchar-smul-preimage.md)
- [MeasureTheory.addEquivAddHaarChar\_smul\_integral\_map](measuretheory-addequivaddhaarchar-smul-integral.md)

We also have the following variant:

- [MeasureTheory.addEquivAddHaarChar\_smul\_integral\_comap](measuretheory-addequivaddhaarchar-smul-integral-2.md)

Note that as a consequence of lemma [MeasureTheory.addEquivAddHaarChar\_smul\_preimage](measuretheory-addequivaddhaarchar-smul-preimage.md), if $X$ is a Borel subset of $A$ with positive finite measure then we can read off $d_A(\phi)$ by $d_A(\phi)=\mu(X)/\mu(\phi^{-1}(X))$, and hence also by $d_A(\phi)=\mu(\phi(X))/\mu(X)$. A nice special case is when $\mu(X)=1$, in which case we have $d_A(\phi)=\mu(\phi(X))$ for all $\phi$, or $d_A(\phi)=1/\mu(\phi^{-1}(X))$. Similarly, by lemma [MeasureTheory.addEquivAddHaarChar\_smul\_integral\_map](measuretheory-addequivaddhaarchar-smul-integral.md), if $f$ is a measurable function with $0\lt \int f(x)d\mu(x)\lt \infty$ then we can read off $d_A(\phi)$ by $d_A(\phi)=(\int f(x)d\mu(x))/(\int f(x)\phi_*\mu(x))$. Note that mathlib supplies such $f$ with the function exists\_continuous\_nonneg\_pos. The following are also straightforward.

- [MeasureTheory.addEquivAddHaarChar\_refl](measuretheory-addequivaddhaarchar-refl.md)
- [MeasureTheory.addEquivAddHaarChar\_trans](measuretheory-addequivaddhaarchar-trans.md)

## Scaling Haar measure on a ring

Now let $R$ be a locally compact topological ring. The *Haar character* of $R$, or more precisely the *left Haar character* of $R$, is a group homomorphism $R^\times\to\mathbb{R}^\times$ defined in the following way. If $u\in R^\times$ then left multiplication by $u$, namely the map $\ell_u:(R,+)\to(R,+)$ defined by $\ell_u(r)=ur$, is a homeomorphism and an additive automorphism of $(R,+)$, so the preceding theory applies to $\ell_u$.

- [MeasureTheory.ringHaarChar](measuretheory-ringhaarchar.md)

Lemmas [MeasureTheory.addEquivAddHaarChar\_refl](measuretheory-addequivaddhaarchar-refl.md) and [MeasureTheory.addEquivAddHaarChar\_trans](measuretheory-addequivaddhaarchar-trans.md) immediately imply that $\delta_R$ is a group homomorphism from $R^\times$ to $\mathbb{R}_{>0}$. Also immediate from previous lemmas is

- [MeasureTheory.ringHaarChar\_mul\_integral](measuretheory-ringhaarchar-mul-integral.md)
- [MeasureTheory.ringHaarChar\_mul\_volume](measuretheory-ringhaarchar-mul-volume.md)

The next result lies a little deeper.

- [MeasureTheory.ringHaarChar\_continuous](measuretheory-ringhaarchar-continuous.md)
