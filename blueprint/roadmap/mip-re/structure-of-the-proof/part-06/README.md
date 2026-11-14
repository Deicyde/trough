---
navigation: transparent
---

# An executable balanced seed… to The typed oracularized sampler

Comments. The exactness hypothesis is the consumer's and covers all $M t = M \log q$ coordinates of the register, whereas the paper's original questions have length $s(N) \leq Q$. Reaching an arbitrary original game therefore still needs the padding of the source register to $Q$ coordinates to be composed with this lemma; that step is not part of it.

- [An executable balanced seed selector and line stages](lem-intro-executable-seeded-lines.md)
- [Executable binary Pauli queries](lem-intro-executable-pauli-queries.md)
- [Full-register auxiliary programs](lem-intro-executable-padded-auxiliary.md)
- [Output relabelling for the explicit selector](lem-intro-explicit-selector-questions.md)
- [Arbitrary binary source registers and exact padding](lem-intro-binary-source-padding.md)

**Remark (Padding and the executable answer format).** The exact full-register padding preserves evaluation but changes factor and dual data. Its honest Read and Hide dual labels can carry unused coordinates. The new executable Read check implements this full-register variant, and the Sample program implements the padded sampling relation. The executable Hide checks use a row-space membership relation on the full register. A question-local quotient decoder converts accepted dual labels to the semantic local dual readouts, without identifying the two coordinate orders. Honest semantic labels satisfy the relaxed relation unchanged. Prefix guards and attained Introspect outputs supply the support needed by the clocked source calls. This bridge is proved in Lemma [Executable quotient hiding and the finite decision kernel](lem-intro-quotient-kernel.md); it does not require the full-register dual labels to lie in the original source subspace.

- [The canonical sampler at every index](lem-intro-canonical-sampler.md)
- [The complete binary Pauli predicate](lem-intro-binary-pauli-predicate.md)
- [Executable quotient hiding and the finite decision kernel](lem-intro-quotient-kernel.md)
- [Full question transport and actual QLD extraction](lem-intro-numbered-transport.md)
- [The ambient compiler's resources and raw-game bridge](lem-intro-ambient-kernel.md)

**Remark (The coarse-operator repair and its checked Lean assembly).** The pinned manuscript already runs the $Z$ commutation analysis on the coarse operators. The earlier blueprint statement that this rewrite remained undone was stale. The checked product-form stage derives commutators from coarse joint measurements, now instantiated by the actual Sample and Read tests. Full hiding rigidity, its normalizer replacement, Read rigidity, and the common-ancilla dilation theorem are proved. The actual adaptive prefix law, Z and dual-X factorizations, weighted conditioning, minimal residual support, projective reassembly, next-prefix label assembly, and a concrete single-stage strategy replacement are now checked. Answer refinement and updating, next-prefix residual reassembly, the actual three-error budget, and exact preservation of the unchanged measurements' errors are also proved. Initialization, decoded valid-answer support, the raw selected-measurement identity, an explicit small-error threshold, and finite iteration on both players are now constructed and composed. Terminal extraction completes malformed outcomes without additional loss. The complete finite-game soundness theorem derives hiding and the second Z estimate from just the primitive Alice-X/Bob-Z guarantees; it handles approximate extracted states, all error sizes, and the paper's power profile. The actual QLD extraction adapter, full question and answer transports, uniform verifier construction, all-index budgets and raw finite-game connection are now proved in Lemmas [Full question transport and actual QLD extraction](lem-intro-numbered-transport.md) and [The ambient compiler's resources and raw-game bridge](lem-intro-ambient-kernel.md). Their top-level assembly supplies the ambient seven-level input contract in Lemma [Supplying ambient introspection](lem-introspection-supply.md). This does not claim the separate generic-depth, source-runtime theorem below.

### The theorem

- [Ambient introspection contract](def-introspection-contract.md)

**Remark (The positive-index soundness domain).** The ambient soundness contract requires $n\geq1$. For nonzero $a,b$, Lean's real power convention makes $\delta(\varepsilon,0)=0$; retaining soundness at zero would force an unintended exact conclusion at original index $1$. The paper's overview starts with $n\geq1$, although its later theorem display quantifies over all naturals. Moreover $2\leq2^n$ holds exactly when $n\geq1$, matching the bounded-input domain. The compression consumer already has $n\geq2$ and supplies this hypothesis.

*Proof.* Evaluate the two zero-base powers using their nonzero exponents. The index equivalence follows from monotonicity of $2^n$ and its value at zero.

- [Supplying ambient introspection](lem-introspection-supply.md)

The checked soundness analysis follows the rigidity argument of (JNVWY20, Section 8) and techniques introduced in (NW19): the Pauli basis test and the twirling, commutation and sandwiching toolkit. These lemmas use the bipartite setting, as in the sources; the pipeline carries $\mathrm{val}^*$ throughout (Remark Why the pipeline is bipartite throughout).

## Oracularization

Oracularization converts a normal form verifier into one where a single player (the “oracle”) receives both original questions and answers both, while the other player receives one of the two questions and must answer consistently. This makes the game's predicate a pointwise function of one player's answer — the format required by answer reduction. This is probably the easiest transformation in the paper and could be attempted first to fix the semantics.

- [Oracularization](thm-oracularization.md)

Formalized form. The ambient model has no timeout-counter form. The formalization replaces it with an index routine that supplies, at each index $n$, a parse cut $B(n)$ and a simulation budget $K(n)$; the decider runs its core under the clocked universal machine for $K(n)$ steps, which makes it total, as the detyping compiler requires. Soundness holds at every budget. Completeness holds once $K(n)$ covers the running time of the core, which is polynomial in the running times of $\mathsf{V}$ at $n$ (Lemma [Running times of the typed oracularized decider](../part-07/lem-oracle-decider-time.md)): this is the hypothesis that the timeout bound supplies in the source. The typed sampler has the levels of the input sampler, at least one.

- [The oracularized game](def-oracular-game.md)

Source. `oracularization.tex`, `sec:orac-def` and `fig:oracle-decider`, with the samplers, deciders and typed question strings stripped away: all oracularization uses of a sampler is the pair of maps $L^\textsc{A}, L^\textsc{B}$ on the seed space.

Comments. The oracularized game is synchronous with no extra hypothesis, which is what makes the PCC vocabulary of Definition [PCC strategy](../../foundations/part-01/def-pcc.md) available on it: equal questions carry equal roles, and the third check then rejects unequal answers.

Two of the four repairs of Remark What the audit changed in oracularization are about the verifier and are *not* addressed here, and it is worth being explicit rather than appearing to have discharged them. Grouping the decider's failed bounded parses into one distinguished outcome (repair 3) has no content at a finite game-level answer alphabet, where there is no parse to fail; what survives of it is the shape check, which rejects an answer whose shape does not match its role. The truncation of answers to $B_\mathcal{D}(n)$ symbols (repair 4) is a statement about a decider and does not appear at this level at all. Repair 2, that the completeness witness has identical measurement operators rather than a symmetric state, and repair 1, the single square root in the soundness loss, belong to the two clauses, which are separate obligations.

- [Completeness of oracularization, at the level of games](lem-oracular-completeness.md)
- [Soundness of oracularization, at the level of games](lem-oracular-soundness.md)
- [Soundness of oracularization, for bipartite strategies](lem-oracular-soundness-tensor.md)

**Remark (What the game-level clauses leave to the verifier level).** Lemmas [Completeness of oracularization, at the level of games](lem-oracular-completeness.md) and [Soundness of oracularization, at the level of games](lem-oracular-soundness.md) are the two clauses of Theorem [Oracularization](thm-oracularization.md) with the samplers, deciders and typed question strings stripped away, and they settle the two repairs that are about the strategies: repair 2, the identical measurement operators, is structural, because a synchronous strategy is one family played by both players; and repair 1, the single square root, is where the constant $24$ comes from. What they do *not* do is inhabit Definition [Oracularization specification](../part-07/def-oracularization-contract.md): the complexity clause, the bounded parse and its grouping (repair 3), the truncation to $B_\mathcal{D}(n)$ (repair 4) and the level accounting of Remark The specification and the earlier contract are all statements about a verifier and none of them appears at this level. The soundness constant here is $24$ rather than an unspecified $c$; the ambient contract asks only for some fixed $c>0$, so the game-level lemma is stronger than the contract needs on that point and silent on every other.

Lemma [Soundness of oracularization, at the level of games](lem-oracular-soundness.md) is stated for synchronous strategies, and a verifier-level statement cannot use that form: $\mathrm{val}^*$ is a supremum over tensor-product strategies, and so is the strategy transport of detyping, while the bridge from synchronous to general values (Theorem [Almost-synchronous strategies are near synchronous strategies](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/03_background_results.tex#L137)) is off the critical path. The paper's own soundness theorem is bipartite. Lemma [Soundness of oracularization, for bipartite strategies](lem-oracular-soundness-tensor.md) is that form, with the same constant.

- [The typed oracularized game](def-oracular-typed-game.md)
- [Value transfers of the typed oracularized game](lem-oracular-typed-transfers.md)
- [The typed oracularized sampler](lem-oracle-typed-sampler.md)
