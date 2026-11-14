---
navigation: transparent
---

# The doubled model is a finite… to Soundness in a model from the…

- [The doubled model is a finite pair, with the order of its parts](lem-doubled-model-finite-pair.md)
- [The role average in the doubled model](lem-doubled-model-role-average.md)
- [No abelian projections in the doubled model](lem-doubled-model-no-abelian.md)
- [Symmetrization after the bridge](thm-doubled-symmetrization.md)
- [Orthonormalization in the doubled model](thm-doubled-orthonormalization.md)
- [The summed semidefinite form, in a commutant with a vector trace](thm-summed-sdp.md)
- [The summed semidefinite form in the doubled model](cor-summed-sdp-doubled.md)

The rest of the vendored preliminaries is ported too (`planning/c6b-plan.md`, milestone M3): the comparison, triangle, Cauchy–Schwarz, completion and self-consistency lemmas that every later section of the vendored proof applies, over the symmetric model, with the swap and normalization hypotheses of the vendored statements dropped. Its two load-bearing propositions are the switch sandwich and the calculus of self-consistency (Lemma [The switch sandwich and self-consistency, in a symmetric model](lem-co-switch-sandwich-self-consistency.md)). So is the local-to-global variance inequality of the hypercube graph (milestone M5), for every family of operators and every vector state (Lemma [Local-to-global variance on the hypercube, for any vector state](lem-co-local-to-global.md)).

- [The switch sandwich and self-consistency, in a symmetric model](lem-co-switch-sandwich-self-consistency.md)
- [Local-to-global variance on the hypercube, for any vector state](lem-co-local-to-global.md)

Four further sections of the vendored proof are ported (`planning/c6b-plan.md`, milestones M4, M6, M7 and M8), each over the symmetric model and with the swap and normalization hypotheses of the vendored statements dropped: the definitions and statements of the main induction step, with the Schwartz–Zippel step of the vendored main theorem, which passes from consistency on points to consistency of whole polynomials (Lemma [The Schwartz–Zippel step, in a symmetric model](lem-co-schwartz-zippel-step.md)); the global variance of the points (Lemma [Global variance of the points, in a symmetric model](lem-co-global-variance-of-points.md)); the commutation of the slice measurements (Lemma [Commutation of the slice measurements, in a symmetric model](lem-co-commutation-g.md)); and orthonormalization in a symmetric model (Lemma [Orthonormalization, in a symmetric model](lem-co-orthonormalization.md)), whose rounding to projective measurements calls de la Salle's theorem (Corollaries [Orthonormalization in a finite pair without abelian projections](../part-05/cor-orthonormalization-finite-pair.md) and [Orthonormalization in a dyadic pair](../part-05/cor-orthonormalization-dyadic-pair.md)) in place of the vendored finite-dimensional route.

In these four lemmas $S$ is a symmetric model over $\mathcal{P}$ (Definition [Symmetric models](../part-05/def-sym-model.md)), with state $\Psi$, expectation $\mathrm{ev}$ and placements $L$ and $R$; a *polynomial* is a map $g : \mathbb{F}_q^m \to \mathbb{F}_q$ of individual degree at most $d$, for the parameters $q$, $m$ and $d$ of the low individual degree test of Theorem [Quantum soundness of the seeded CL test](../../background-results/part-01/thm-lidt-cl-soundness.md); and for submeasurements $A$ and $B$ in $\mathcal{P}$ with the same outcomes and totals $A_{\mathrm{total}} = \sum_a A_a$ and $B_{\mathrm{total}}$, their *consistency defect* is

$$
\mathrm{cons}(A, B) = \max\Bigl(0,\ \mathrm{ev}\bigl(L(A_{\mathrm{total}})\,
R(B_{\mathrm{total}})\bigr) - \sum_a \mathrm{ev}\bigl(L(A_a)\, R(B_a)\bigr)\Bigr),
$$

which is $\max(0, \sum_{a \neq b} \mathrm{ev}(L(A_a)\, R(B_b)))$.

- [The Schwartz–Zippel step, in a symmetric model](lem-co-schwartz-zippel-step.md)
- [Global variance of the points, in a symmetric model](lem-co-global-variance-of-points.md)
- [Commutation of the slice measurements, in a symmetric model](lem-co-commutation-g.md)
- [Orthonormalization, in a symmetric model](lem-co-orthonormalization.md)

The two remaining sections of the vendored proof before its induction step are ported too (`planning/c6b-plan.md`, milestones M10 and M11), over the symmetric model and with the swap and normalization hypotheses of the vendored statements dropped: self-improvement, which turns a measurement consistent with the points into a projective one with the same consistency up to a fixed loss (Lemma [Self-improvement, in a symmetric model](lem-co-self-improvement.md)), and pasting, which glues slice measurements in $m$ variables into a measurement in $m + 1$ (Lemma [Pasting, in a symmetric model](lem-co-ld-pasting.md)). Self-improvement solves the semidefinite program of the vendored proof by its summed form (Theorem [The summed semidefinite form, in a commutant with a vector trace](thm-summed-sdp.md)) and rounds by orthonormalization in a symmetric model (Lemma [Orthonormalization, in a symmetric model](lem-co-orthonormalization.md)), where the vendored development uses finite-dimensional strong duality and the finite-dimensional rounding; so it asks of the model what those two ask, a finite pair without abelian projections in its first player's operators, and it asks $d \geq 1$, which makes the error at which it rounds positive. In both lemmas $S$, the polynomials and the consistency defect $\mathrm{cons}$ are as in the four lemmas above.

- [Self-improvement, in a symmetric model](lem-co-self-improvement.md)
- [Pasting, in a symmetric model](lem-co-ld-pasting.md)

The remaining milestones of the port assemble these lemmas (`planning/c6b-plan.md`, milestones M12 to M14). The main induction of the vendored proof runs over the symmetric model (Lemma [The main induction, in a symmetric model](lem-co-main-induction.md)), with $d \geq 1$ threaded through to self-improvement, and it is applied in the doubled model $D(M)$ of a dyadic pair $M$, whose bipartite reading is a finite pair without abelian projections (Lemma [No abelian projections in the doubled model](lem-doubled-model-no-abelian.md)). Its output is one measurement in the local algebra of $D(M)$, which is unsymmetrized into one measurement for each player of $M$; the tail of the vendored main theorem then runs on $M$ itself, with two players' algebras.

- [The main induction, in a symmetric model](lem-co-main-induction.md)
- [Unsymmetrization in the doubled model](lem-doubled-unsymmetrization.md)
- [The main theorem of the low individual degree test, in a dyadic pair](thm-co-main-formal.md)
- [The canonical-line theorem in a dyadic pair](lem-co-lidt-canonical-line.md)
- [Soundness in a model from the canonical-line theorem in it](lem-lidt-sound-in-of-model-lidt.md)
