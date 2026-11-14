---
navigation: transparent
---

# Unital dyadic matrix units to The doubled model

The orthonormalization step of the port applies Theorem [Orthonormalization in algebras without abelian projections](../../background-results/part-01/thm-orthonormalization-no-abelian.md) in algebras cut out by a purely algebraic condition that excludes abelian projections (Theorem [Dyadic matrix units exclude abelian projections](thm-no-abelian-dyadic.md)): matrix units of every size $2^n$.

- [Unital dyadic matrix units](def-dyadic-units.md)
- [Transport of dyadic matrix units](lem-dyadic-units-closure.md)
- [Pauli sites give dyadic matrix units](lem-pauli-sites-units.md)
- [Dyadic matrix units exclude abelian projections](thm-no-abelian-dyadic.md)
- [Dyadic pairs](def-dyadic-pair.md)
- [Dyadic pairs are closed under ancilla extensions](lem-dyadic-pair-closure.md)
- [The twisted Pauli algebra](lem-pauli-algebra.md)
- [Amplification by an algebra with dyadic matrix units](lem-amplification-dyadic.md)
- [${\omega^{\mathrm{co}}}$ is approached in dyadic pairs](lem-co-value-finite-pair.md)
- [The low-individual-degree test is sound in dyadic pairs](def-lidt-sound-fin.md)
- [Answer reduction is sound in ${\omega^{\mathrm{co}}}$, given the test in dyadic pairs](thm-ar-sound-co-fin.md)
- [The Pauli basis test, given the seeded test in dyadic pairs](lem-qld-approx-co-fin.md)
- [$\mathrm{MIP}^{\mathrm{co}} = \mathrm{coRE}$, from the soundness of the low-individual-degree test in dyadic pairs](cor-mipco-from-lidt-fin.md)

The hypothesis of Corollary [$\mathrm{MIP}^{\mathrm{co}} = \mathrm{coRE}$, from the soundness of the low-individual-degree test in dyadic pairs](cor-mipco-from-lidt-fin.md) is Theorem [Quantum soundness of the seeded CL test](../../background-results/part-01/thm-lidt-cl-soundness.md) in every dyadic pair. It is proved (Theorem [The low-individual-degree test is sound in dyadic pairs](../part-07/thm-lidt-sound-fin.md)), so $\mathrm{MIP}^{\mathrm{co}} = \mathrm{coRE}$ holds without hypothesis (Theorem [$\mathrm{MIP}^{\mathrm{co}} = \mathrm{coRE}$](../part-07/thm-mipco-eq-core-unconditional.md)). The proof is the port of the vendored proof described above, C6b of `planning/mipco-track.md`, planned and recorded in `planning/c6b-plan.md`; `reports/lidt-co-audit.md`, Section 5, sizes it, and `reports/c6b-paper-proofs.md` records the mathematics it adds. Its orthonormalization tier is the II$_1$ one: the class is narrowed to the dyadic pairs, whose algebras have no nonzero abelian projection (Theorem [Dyadic matrix units exclude abelian projections](thm-no-abelian-dyadic.md)), and in those orthonormalization holds unconditionally (Corollary [Orthonormalization in a dyadic pair](cor-orthonormalization-dyadic-pair.md)).

- [Orthonormalization in a finite pair without abelian projections](cor-orthonormalization-finite-pair.md)
- [Orthonormalization in a dyadic pair](cor-orthonormalization-dyadic-pair.md)

The port is complete (`planning/c6b-plan.md`, Section 3, milestones M0 to M14). It replaces the vendored state on $\mathbb{C}^\iota \otimes \mathbb{C}^\iota$, and the swap hypotheses that come with it, by a *symmetric model* (Definition [Symmetric models](def-sym-model.md)), in which swap symmetry is a theorem (Lemma [Swap symmetry in a symmetric model](lem-sym-model-swap.md)), and rewrites the vendored proof over it file by file, under `MIPRE/Background/LIDT/Co/`, keeping the vendored names and importing the vendored classical layer rather than porting it. The first section ported in full is the commutativity of points (Lemma [Commutativity of points, in a symmetric model](lem-co-commutativity-points.md)), and the last is the main theorem (Theorem [The main theorem of the low individual degree test, in a dyadic pair](../part-06/thm-co-main-formal.md)), from which the soundness of the seeded test in dyadic pairs follows (Theorem [The low-individual-degree test is sound in dyadic pairs](../part-07/thm-lidt-sound-fin.md)).

- [Symmetric models](def-sym-model.md)
- [Swap symmetry in a symmetric model](lem-sym-model-swap.md)
- [Commutativity of points, in a symmetric model](lem-co-commutativity-points.md)

For a finite pair the symmetric model is supplied by a doubling on $\mathcal{H} \oplus \mathcal{H}$ (`planning/c6b-plan.md`, milestone M2; `reports/c6b-paper-proofs.md`, Section 4), which replaces the vendored role-register symmetrization, a construction for tensor products only. Entering and leaving the doubled model costs the vendored constants: $3\varepsilon$ for the goodness of the symmetric strategy (Theorem [Symmetrization after the bridge](../part-06/thm-doubled-symmetrization.md)) and $100 \eta^{1/4}$ for orthonormalization (Theorem [Orthonormalization in the doubled model](../part-06/thm-doubled-orthonormalization.md)). The unsymmetrization at the vendored cut, at $2\sigma$, has its arithmetic here (Lemma [The role average in the doubled model](../part-06/lem-doubled-model-role-average.md)); its input, the point consistency of the ported main induction, is not yet ported. The semidefinite step of the vendored proof, Lemma 9.2 of (JNVWY21qld), is proved there by strong duality in finite dimension. Here it is replaced by a summed form proved with the trace (Theorem [The summed semidefinite form, in a commutant with a vector trace](../part-06/thm-summed-sdp.md); milestone M9, Section 5 of the report), solved componentwise in the doubled model (Corollary [The summed semidefinite form in the doubled model](../part-06/cor-summed-sdp-doubled.md)).

- [The players' algebras of a finite pair, as commutants with their order](lem-finite-pair-order.md)
- [The doubled model](def-doubled-model.md)
