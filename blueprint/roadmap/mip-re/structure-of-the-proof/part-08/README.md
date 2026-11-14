---
navigation: transparent
---

# The PCP's proof format and… to Answer-reduction quantitative…

The Lean field family is indexed by odd extension degrees, as required by the parameter choice. Requiring a field of cardinality $2^k$ for every natural $k$ would include $k=0$ and make the contract uninhabitable. The constructed verifier uses the canonical polynomial-basis representation and uniform field programs from the proved binary irreducible-polynomial constructor (Lemma [Uniform deterministic binary irreducible polynomials](../../background-results/part-05/lem-binary-uniform-irreducible.md)). Its exact axiom guard contains only Lean's standard axioms. Effective self-dual normal coordinates are supplied by Lemma [Deterministic self-dual normal basis](../../background-results/part-04/lem-self-dual-basis.md); integrating those coordinates into the downsizing consumers remains a separate obligation.

The theorem has four obligations, and they are separate in the source because they fail separately.

[$\bullet\bullet$ medium]

- [The PCP's proof format and query structure](lem-pcp-format.md)

[$\bullet\bullet$ medium]

- [PCP completeness](lem-pcp-completeness.md)

[$\bullet\bullet\bullet$ hard]

- [PCP soundness](lem-pcp-soundness.md)

[$\bullet\bullet$ medium]

- [PCP complexity](lem-pcp-complexity.md)

**Remark (Why $m$ is a power of two).** The hypothesis is not cosmetic and was a confirmed defect in the source. The $m$-variate low-degree test needs $m \mid q$, and $q$ is a power of two, so $m$ must be one as well. The padded description guarantees this only for the *outer* variable count $m' = 5m + 5 + s$; the inner $m$, inherited from the succinct-SAT reduction, carries no such guarantee, which leaves the conditionally linear functions of the axis-parallel and diagonal lines ill defined and the applications of low-degree soundness with an unverified hypothesis. The repair is to round $m$ up to a power of two in the padding step, which costs nothing asymptotically. A formalization must state it as a hypothesis, as Theorem [The bespoke PCP for deciders](../part-07/thm-pcp-decider.md) does.

[$\bullet\bullet\bullet$ hard]

- [Low-degree sandwich support](lem-ar-sandwich-support.md)

Comments. Both relations are the paper's consistency relation of `games.tex` — a disagreement probability — and not the squared distance that $\simeq_\delta$ denotes here; this entry previously stated the hypothesis and the conclusion as squared distances with an unspecified constant, which is equivalent up to the factor of [(1)](../../foundations/part-02/def-cross-distance.md) but is not how the source states it or how its consumer, Lemma [The answer-reduction giant sandwich](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/06_proof_structure.tex#L5871), uses it. The source defers the proof to NW19's Fact 4.34, whose import was audited (AuditSync26); the formalization re-derives it, and the constant $2\sqrt{2}$ it produces is the universal constant the source leaves implicit. Two generalizations cost nothing and are kept: $y$ may be drawn from any distribution independent of $x$, with the collision bound stated against it; and the families are arbitrary finite sets with evaluation maps, so the consumer's alphabets extended by zero projectors are covered without comment. The collision bound is a hypothesis: for polynomial families it is Lemma [Schwartz–Zippel](../../background-results/part-05/lem-schwartz-zippel.md), applied by the consumer.

The following answer-reduction obligations use the parameter routine and input hypotheses of Theorem [Answer reduction](../part-09/thm-answer-reduction.md). In measurement relations, “consistent” means close in the cross-party squared distance of Definition [Cross-party state-dependent distance](../../foundations/part-02/def-cross-distance.md); bounds on game failure are stated separately. Put $\theta=16^{|T^{\mathrm{ar}}|}\varepsilon_{\mathrm{out}}$, $E=\delta_{\mathrm{CL}}(\theta,q,m',d,m'+6)$ and $\rho=m'd/q$. The common upper bound $\kappa$ below absorbs both the individual and simultaneous errors; it is not a renaming of the source's individual $\delta_1$ or simultaneous $\delta_2$.

- [The PCP sampler of answer reduction](def-ar-pcp-sampler.md)
- [The answer-reduced decision predicate](def-ar-decider-predicate.md)
- [The typed answer-reduced game](def-ar-typed-game.md)
- [The typed answer-reduced sampler](lem-ar-typed-sampler.md)
- [The typed answer-reduced decider](lem-ar-typed-decider.md)
- [Answer-reduction construction](lem-ar-construction.md)
- [Answer-reduction completeness](lem-ar-completeness.md)
- [Typed soundness setup](lem-ar-soundness-setup.md)
- [Full-seed indexing for answer reduction](def-ar-seed-index.md)
- [Global PCP consistency tests](lem-ar-global-tests.md)
- [Input-codeword consistency tests](lem-ar-input-tests.md)
- [Common individual polynomial measurements](lem-ar-common-polynomials.md)
- [A simultaneous complete proof tuple](lem-ar-simultaneous-proof.md)
- [Decoding with the original answer cutoff](lem-ar-decoding.md)
- [Answer-reduction quantitative assembly](lem-ar-error-assembly.md)
