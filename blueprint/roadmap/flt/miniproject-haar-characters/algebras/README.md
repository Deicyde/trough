# Algebras

Say $F$ is a locally compact topological ring (for example $\mathbb{R}$ or $\mathbb{C}$ or $\mathbb{Q}_p$, or the adeles of a number field), $V$ is a finite free $F$-module, and $\phi:V\to V$ is an invertible $F$-linear map. Then $V$ with its module topology (which is the product topology if one picks a basis) is a locally compact topological abelian group, and $\phi$ is additive. One can check that linearity implies continuity (this is IsModuleTopology.continuous\_of\_linearMap in mathlib), so in fact $\phi$ is a homeomorphism and our theory applies. The following lemma gives a formula for the scale factor $d_V(\phi)$.

- [MeasureTheory.addEquivAddHaarChar_eq_ringHaarChar_det, MeasureTheory.addEquivAddHaarChar_eq_ringHaarChar_det_of_existsListTransvecEtc](measuretheory-addequivaddhaarchar-eq-ringhaarcha.md)

Now say $F$ is a locally compact topological field, and that $R$ is a (possibly non-commutative) $F$-algebra. Recall that this means that ($R=0$ or) $F$ lies in the centre of $R$. Assume that $R$ is finite-dimensional as an $F$-vector space. Then if we give $R$ the $F$-module topology (which is just the product topology if we pick a basis) then it is known that $R$ becomes a topological ring. Now say $u\in R^\times$, and recall $\ell_u:R\to R$ is left multiplication by $u$. Then $\ell_u$ is easily checked to be an $F$-linear homeomorphism.

- [MeasureTheory.algebra_ringHaarChar_eq_ringHaarChar_det](measuretheory-algebra-ringhaarchar-eq-ringhaarch.md)
