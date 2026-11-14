---
navigation: transparent
---

# From the identities to the… to The per-role failures

- [From the identities to the formula and the system; prop:completeness_and_soundness_of_PCP_for_V_n](lem-ar-pcp-sound.md)
- [The game accepts the decoded answers; cor:functional_viewpoint_final, item 2](thm-ar-pcp-accepts.md)

## Answer reduction: the completeness of the PCP

The honest PCP of paper II is $\mathsf{Induce}_C$ (Definition defn:inducing\_to\_a\_PCP, II:9081): the low-degree encodings of the tables, and helpers obtained by division by the polynomials $X_i(1 - X_i)$ (the paper's $\mathrm{Div}$ and $\mathrm{Mod}$). The paper needs the helpers of the linear part to depend linearly on the linear tables; here they are the values of a linear map, chosen once.

- [Linear certificates for vanishing on the cube](lem-ar-linear-certificates.md)
- [The honest PCP; $\mathsf{Induce}_C$](def-ar-induce.md)
- [Completeness of the PCP; prop:completeness_and_soundness_of_PCP_for_V_n](lem-ar-pcp-complete.md)
- [The readable and the linear parts of the honest PCP](lem-ar-pcp-parts.md)
- [The honest PCP of accepted answers; cor:functional_viewpoint_final, item 1](lem-ar-pcp-honest.md)

## Answer reduction: the answer-reduced game

The game $\mathrm{AnsRed}(\mathsf{V}_n)$ of Definition defn:combi\_ans\_red (II:10285), as typed tailored data (Definition [Detyping a tailored game](../part-03/def-tailored-detyping.md)) at one index of the input: the codewords of its answers name the polynomials of a PCP (Definition [The slots of a PCP](def-ar-slots.md)), and its four checks are linear constraints read in Lemma [Reading the answer-reduced constraints](lem-ar-tailored-reading.md), the form its completeness and soundness are proved against. The type graph is complete with loops, as the repository's typed games are, rather than the paper's tensor product of two paths (II:10313); per seed and role the game is then the seeded low-degree test itself, and only the constants of the soundness proof change.

- [The slots of a PCP](def-ar-slots.md)
- [Slot values and block-local polynomials](lem-ar-slots.md)
- [The answer-reduced game as typed tailored data; defn:combi_ans_red](def-ar-tailored-game.md)
- [Reading the answer-reduced constraints](lem-ar-tailored-reading.md)

## Completeness of the answer-reduced game

The honest strategy of the answer-reduced game measures the oracularization of a perfect Z-aligned permutation strategy of the input (Lemma [Completeness of oracularization, at the level of games](../../structure-of-the-proof/part-06/lem-oracular-completeness.md)), and answers each typed question with the honest low-degree answers of the polynomials of the honest PCP of the input answers (cor:functional\_viewpoint\_final): the oracle with all of them, an isolated player with the two of its own answer. Its answers pass the four checks (Lemma [The checks hold of honest answers](lem-ar-honest-checks.md)), and its answer bits are signed permutations, diagonal at the readable bits, because each is, the readable input bits fixed, an $\mathbb{F}_2$-affine function of the linear ones (Lemma [The answer bits of the honest answers](lem-ar-honest-bits.md)).

- [The honest answers](def-ar-honest-answers.md)
- [The honest PCP of an answer pair](lem-ar-pair-pcp.md)
- [The checks hold of honest answers](lem-ar-honest-checks.md)
- [Bits controlled by readable data](lem-ar-controlled-bits.md)
- [The answer bits of the honest answers](lem-ar-honest-bits.md)
- [The honest strategy of the answer-reduced game](def-ar-honest-strategy.md)
- [ZPC completeness of the answer-reduced game](thm-ar-zpc-complete.md)

## Soundness of the answer-reduced game

The soundness of the answer-reduced game (prop:completeness\_soundness\_combi\_ans\_red, item 2) follows the paper's perturbations in a bipartite model in which the seeded low-degree test is sound (Definition [The low-individual-degree test is sound in a model](../../downstream-results/part-03/def-lidt-sound-in.md)): polynomial measurements at every role (Lemma [The polynomial measurements](../part-07/lem-ar-sound-extract.md)), pruned to block-local outcomes (Lemma [Indifference, at two points of a line](../part-07/lem-ar-sound-indifference.md)) that pass the proof check densely (Lemma [The proof check, on the polynomials](../part-07/lem-ar-sound-check.md)), and decoded to answers of the input game (Lemma [The failure of the decoded strategy](../part-07/lem-ar-decoded-value.md)). Two things differ from the paper. The model's soundness gives conclusions at points only, so the indifference check is read at two points of one axis-parallel line instead of at the line. And the decoded strategy plays the typed oracularized game of the input, oracle included, so the bound reaches $\mathrm{val}^*(\mathsf{V}_n)$ through detyping and oracularization, and is stated in the error of the test's soundness rather than through the paper's $10^6 m \delta^{1/8} / (1 - 72 m / q)$ for the double cover.

Throughout, $T$ is a projective strategy in such a model for the answer-reduced typed game on an answer-reduced sampler, $\theta = 1 - \mathrm{val}(T)$ its failure, $Z$ the seeds of the input sampler, $W = \mathbb{F}_q^{D}$ the registers of the seeded test, $M = 2^j$ the test's variables, $d$ its individual degree, and $\mathrm{dis}(P, Q)$ the disagreement of a measurement $P$ of Alice's and $Q$ of Bob's.

- [The per-role low-degree strategies](def-ar-sound-roles.md)
- [The per-role failures](lem-ar-sound-roles.md)
