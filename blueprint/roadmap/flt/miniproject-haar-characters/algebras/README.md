# Algebras

Say $F$ is a locally compact topological ring (for example $\mathbb{R}$ or $\mathbb{C}$ or $\mathbb{Q}_p$, or the adeles of a number field), $V$ is a finite free $F$-module, and $\phi:V\to V$ is an invertible $F$-linear map. Then $V$ with its module topology (which is the product topology if one picks a basis) is a locally compact topological abelian group, and $\phi$ is additive. One can check that linearity implies continuity (this is IsModuleTopology.continuous\_of\_linearMap in mathlib), so in fact $\phi$ is a homeomorphism and our theory applies. The following lemma gives a formula for the scale factor $d_V(\phi)$.

- [MeasureTheory.addEquivAddHaarChar\_eq\_ringHaarChar\_det,
    MeasureTheory.addEquivAddHaarChar\_eq\_ringHaarChar\_det\_of\_existsListTransvecEtc](measuretheory-addequivaddhaarchar-eq-ringhaarcha.md)
- [MeasureTheory.algebra\_ringHaarChar\_eq\_ringHaarChar\_det](measuretheory-algebra-ringhaarchar-eq-ringhaarch.md)
