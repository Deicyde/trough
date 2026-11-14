---
navigation: transparent
---

# Tailored gap compression, value… to $\mathrm{TMIP}^* = \mathrm{RE}$…

**Remark (Where the formalization departs from the paper).**

1. *The soundness bound.* The paper's clause (3) reads $\mathrm{val}^*(\mathfrak{G}_\mathcal{M}) < \frac12$; its proof (II:2046–2065) shows that $\mathrm{Ent}(\mathfrak{G}_\mathcal{M}, \frac12) = \infty$, that every finite-dimensional strategy has value $< \frac12$, which bounds the supremum by $\frac12$ only. Paper I uses the theorem with $\leq \frac12$ ((BCLV24), Theorem 7.4).
2. *Value form.* The paper states compression and parallel repetition in entanglement form, $\mathrm{Ent}(\mathsf{V}'_n, \frac12) \geq \max\{\mathrm{Ent}(\mathsf{V}_{2^n}, \frac12), 2^{2^{\lambda n} - 1}\}$ (II:1865), proved through the anchored repetition theorem of (BVY17) read as dimension-preserving (II:11425) and the almost-synchronous rounding of (Vid22) (II:3227, a proof idea; its quotation of (Vid22) at II:11350 is commented out of the source). The paper's Remark II:1876 says that what its proofs establish is the value form, which is what is formalized here, with direct repetition (Theorem [Direct parallel repetition for entangled strategies](../../parallel-repetition/thm-direct-repetition-q.md)) and the paper route of Theorem [Halting reduction](../../structure-of-the-proof/part-09/thm-halting.md), whose search branch replaces the base case $2^{2^{\lambda n} - 1}$. No entanglement bound is tracked.
3. *All strategies.* Soundness is proved in the quantum value $\mathrm{val}^*$ of tensor-product strategies, which bounds the paper's synchronous value from above (Lemma [Synchronous value lower-bounds the quantum value](../../foundations/part-01/lem-sync-le-valstar.md)).
4. *Question reduction.* The paper's question reduction is JNVWY's on its own Pauli basis game over $\mathbb{F}_2$ (II:3742), sound by a semi-stability theorem cited from de la Salle (II:3495); the paper notes that its combinatorial game is JNVWY's and that JNVWY's soundness covers it (II:5228–5233). The plan's Route A presents this project's introspection verifier (Theorem [Introspection](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/06_proof_structure.tex#L3993)) as a tailored verifier instead, which Phase 0 checked is possible (Remark Route A: the two checks).

**Remark (Route A: the two checks).** Two properties of this project's introspection verifier make the tailored presentation possible, and both hold (`planning/aldous-lyons-track.md`, section 4.2, with the evidence). Every check of the introspective predicate is *controlled-linear*: a predicate on the readable fields alone (the introspected question, the sampled seed, the prefixes read and hidden, and the $Z$-basis Pauli answers), or $\mathbb{F}_2$-affine equations on the linear fields (the duals, the hidden tails, the $X$-basis answers, the Pair and Magic Square answers) with coefficients computed from readable data and the questions; the input's answers must first be padded to constant lengths, as in the paper (II:6219). And the honest strategy is a signed-permutation strategy with diagonal readable observables when the input's is: its $X$-type observables are translations, its $Z$-type observables $\pm 1$ characters, its nonlinear post-processing acts on $Z$-basis outcomes only, and the input enters as controlled direct sums.

## Compression and its three stages

- [Tailored gap compression, value form; II:1852](def-tailored-compression.md)
- [The tailored halting verifier; II:1900–1925](def-tailored-halt-verifier.md)
- [The values of the tailored halting verifier; II:1978](lem-tailored-dhalt-values.md)
- [$\lambda$ for the tailored halting verifier; II:2002](lem-tailored-lambda.md)
- [The search program's specification](def-tailored-search-spec.md)
- [The tailored halting theorem at a fixed level; II:2021–2066](thm-tailored-halting-level.md)

## Tabulation, the search program and the reduction

- [Tailored game descriptions as games of the foundations](lem-tailored-bridge.md)
- [A tailored game description as a game description](lem-tailored-conversion.md)
- [Presentations](def-tailored-presents.md)
- [A presentation of a game without weight on its loops](lem-tailored-presents.md)
- [The tabulation of a tailored verifier](def-tailored-tabulation.md)
- [The tabulation is computable, and correct on bounded verifiers](lem-tailored-tabulation.md)
- [The search program](lem-tailored-search.md)
- [Halting from tailored compression; II:1887–2066](thm-tailored-halting.md)
- [The computable class $\mathrm{TMIP}^*$; II:787](def-tmipstar.md)
- [$\mathrm{TMIP}^* = \mathrm{RE}$, as classes; II:787, II:1838, II:6997](thm-tmipstar-eq-re.md)

## The polynomial-time class

- [The class $\mathrm{TMIP}^*$; II:787, II:1505](def-tmipstar-poly.md)

The paper's clause (1) of Theorem [$\mathrm{TMIP}^* = \mathrm{RE}$; II:1505, Theorem 7.4 of (BCLV24)](../part-01/thm-tmip-re.md) asks that sampling a question pair and evaluating the decision predicate take time polynomial in the input. The decision predicate is the canonical decider (Definition [The canonical decider, as a program; II:1757–1787](../part-01/def-canonical-decider.md)) on what the calculator and the processor output, so the efficiency clause bounds those two programs, as Definition [The class $\mathrm{MIP}^*_{1,1/2}(2,1)$](../../foundations/part-03/def-mipstar.md) bounds the decider. The canonical decider's own running time, a polynomial in theirs, is Lemma [The running time of the canonical decider](../part-04/lem-canonical-decider-cost.md) for tailored normal form verifiers; no statement here needs it. The completeness clause is read on the doubled game, as for tailored normal form verifiers (`TailoredVerifier.HasPerfectZPC`), and the threshold is $\leq \frac12$, as everywhere in this project (Remark Where the formalization departs from the paper). In Lean the verifier is a `TPolyVerifier`, whose sampler and bound form a `PolyVerifier` (`toPoly`), so that the distribution of $\mathfrak{G}_z$ is that of Definition [The class $\mathrm{MIP}^*_{1,1/2}(2,1)$](../../foundations/part-03/def-mipstar.md)'s game.

- [The class is contained in the computable one](lem-tmipstar-poly-sub.md)
- [Extending a tailored game along its questions](lem-tailored-extend.md)
- [$\mathrm{TMIP}^* = \mathrm{RE}$ for the polynomial-time class; II:787, II:1505](thm-tmipstar-poly-eq-re.md)
