---
declaration: theorem
origin: cited
lean: MIPRE.LIDT.Co.Test.mainFormal
statement: formalized
proof: formalized
---

# The main theorem of the low individual degree test, in a dyadic pair

Let $S$ be a projective strategy for the low individual degree test whose two players act in a dyadic pair $M$ (Definition [Dyadic pairs](../part-05/def-dyadic-pair.md)) with a unit state, failing the test with probability at most $\varepsilon$, let $d \geq 1$, and let $k$ be an integer with $k \geq 400 m d$ and $k > 0$. Then there are projective measurements $G^\textsc{A}$ in the first player's algebra and $G^\textsc{B}$ in the second's, with outcomes the polynomials of individual degree at most $d$, such that the first player's point measurements are consistent with the evaluations of $G^\textsc{B}$, the evaluations of $G^\textsc{A}$ with the second player's point measurements, and $G^\textsc{A}$ with $G^\textsc{B}$, each up to the error of the vendored main theorem, which at the parameters of the canonical-line test is $\delta_{lidt}(\varepsilon, m, d, q, k)$ of Theorem [Quantum soundness of the canonical-line low individual degree test](../../background-results/part-01/thm-lidt-soundness.md).

## Depends on

- [Unsymmetrization in the doubled model](lem-doubled-unsymmetrization.md)
- [The main induction, in a symmetric model](lem-co-main-induction.md)
- [Orthonormalization, in a symmetric model](lem-co-orthonormalization.md)
- [The Schwartz–Zippel step, in a symmetric model](lem-co-schwartz-zippel-step.md)
- [No abelian projections in the doubled model](lem-doubled-model-no-abelian.md)

## Proof

The proof is the vendored one, `MIPStarRE.LDT.Test.mainFormal` in `MIPRE/Background/LIDT/MIPStarRE/LDT/Test/MainTheorem/`, rewritten over the models (`planning/c6b-plan.md`, milestones M12 and M13), with the role register replaced by the doubling. The symmetric strategy $S_D$ in $D(M)$ is $(3\varepsilon, 3\varepsilon, 3\varepsilon)$-good (Theorem [Symmetrization after the bridge](thm-doubled-symmetrization.md)), and $D(M)$ is a finite pair without abelian projections (Lemma [No abelian projections in the doubled model](lem-doubled-model-no-abelian.md)), so the main induction (Lemma [The main induction, in a symmetric model](lem-co-main-induction.md)) runs in $D(M)$ and returns a measurement $G$ in its local algebra. Its components are $2\sigma$-consistent with the points in $M$ (Lemma [Unsymmetrization in the doubled model](lem-doubled-unsymmetrization.md)). The step from points to whole polynomials runs in $D(M)$ on the pairing of the two components, whose self-consistency there is exactly their two-space consistency in $M$, so it adds $md/q$ (Lemma [The Schwartz–Zippel step, in a symmetric model](lem-co-schwartz-zippel-step.md)) with no loss of a factor of two. The rest of the vendored tail runs on $M$, with two players' algebras: the two-space orthonormalizations (Lemma [Orthonormalization, in a symmetric model](lem-co-orthonormalization.md)) at a positive error, since $d \geq 1$, a completion in the commutant that the finite pair identifies each algebra with (Lemma [The players' algebras of a finite pair, as commutants with their order](../part-05/lem-finite-pair-order.md)), and the vendored scalar cascade, verbatim. When the error is at least $1$, any projective measurements will do.

## Lean

Formalized as [`MIPRE.LIDT.Co.Test.mainFormal`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LIDT.Co.Test.mainFormal).

## Sources

- [MIP* = RE blueprint: content/08_downstream.tex, line 4168](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/08_downstream.tex#L4168)
