---
declaration: lemma
origin: cited
lean: MeasureTheory.addEquivAddHaarChar_eq_addEquivAddHaarChar_of_isOpenEmbedding
statement: formalized
proof: formalized
discussion: https://github.com/ImperialCollegeLondon/FLT/issues/551
---

# MeasureTheory.addEquivAddHaarChar\_eq\_addEquivAddHaarChar\_of\_isOpenEmbedding

If $f:A\to B$ is a group homomorphism and open embedding between locally compact topological additive groups and if $\alpha:A\to A$ and $\beta:B\to B$ are additive homeomorphisms such that the square commutes (i.e., $f\circ\alpha=\beta\circ f$) then $d_A(\alpha)=d_B(\beta)$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [Topology.IsOpenEmbedding.isHaarMeasure\_comap](topology-isopenembedding-ishaarmeasure-comap.md)
- [Topology.IsOpenEmbedding.regular\_comap](topology-isopenembedding-regular-comap.md)
- [MeasureTheory.addEquivAddHaarChar\_smul\_integral\_comap](../initial-definitions/measuretheory-addequivaddhaarchar-smul-integral-2.md)

## Proof

Choose a regular Haar measure $\mu_B$ on $B$. We just saw in lemmas [Topology.IsOpenEmbedding.isHaarMeasure\_comap](topology-isopenembedding-ishaarmeasure-comap.md) and [Topology.IsOpenEmbedding.regular\_comap](topology-isopenembedding-regular-comap.md) that its pullback $\mu_A:=f^*\mu_B$ to $A$ is also a regular Haar measure. Now fix a continuous compactly-supported function $g$ on $A$ with $0\lt \int g(a)d\mu(a)\lt \infty$. Then $d_A(\alpha)\int g(a)d\mu_A(a)=\int g(a)d(\alpha^*\mu_A)(a)$ by lemma [MeasureTheory.addEquivAddHaarChar\_smul\_integral\_comap](../initial-definitions/measuretheory-addequivaddhaarchar-smul-integral-2.md). This equals $\int g(a)d(\alpha^* f^*\mu_B)(a)$ by definition, which is $\int g(a)d(f^*\beta^*\mu_B)(a)$ because pullback of pullback is pullback. This equals $d_B(\beta)\int g(a) d(f^*\mu_B)(a)$ by corollary [MeasureTheory.addEquivAddHaarChar\_comap](../initial-definitions/measuretheory-addequivaddhaarchar-comap.md) which is $d_B(\beta)\int g(a)d\mu_A(a)$ by definition, and so $d_A(\alpha)=d_B(\beta)$ as required.

## Lean

Formalized as [`MeasureTheory.addEquivAddHaarChar_eq_addEquivAddHaarChar_of_isOpenEmbedding`](https://ImperialCollegeLondon.github.io/FLT/docs/find/#doc/MeasureTheory.addEquivAddHaarChar_eq_addEquivAddHaarChar_of_isOpenEmbedding).

## Sources

- [Fermat's Last Theorem (Imperial) blueprint: chapter/HaarCharacterProject.tex, line 574](https://github.com/ImperialCollegeLondon/FLT/blob/a3210204ad8876e851e32f73dd97d882bf1ccd0a/blueprint/src/chapter/HaarCharacterProject.tex#L574)
