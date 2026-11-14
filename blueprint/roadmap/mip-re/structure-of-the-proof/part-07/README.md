---
navigation: transparent
---

# The typed oracularized decider to The bespoke PCP for deciders

- [The typed oracularized decider](lem-oracle-typed-decider.md)
- [Running times of the typed oracularized decider](lem-oracle-decider-time.md)
- [Oracularization specification](def-oracularization-contract.md)

**Remark (The specification and the earlier contract).** An earlier version of `MIPRE.Oracularization` was untyped and level-preserving, with value transfers as fields. It was satisfied by a transformation that does not oracularize at all: keep the input sampler, and let the output decider reject any answer longer than the parse bound and otherwise run the input decider. At the parse bound its game is $\mathsf{V}_n$ itself, so completeness is the identity and soundness holds with $c = 1$. No field saw the *oracle form* of the output — that one player's answer alone decides the game check, and the other player's answer must equal one of its components — and that form is the only property of oracularization that answer reduction uses: the probabilistically checkable proof replaces exactly that game check (Lemma [Answer-reduction construction](../part-08/lem-ar-construction.md)), and the decoding step returns to exactly that form (Lemma [Decoding with the original answer cutoff](../part-08/lem-ar-decoding.md)).

The specification of Definition [Oracularization specification](def-oracularization-contract.md) sees the oracle form in both halves: the sampler is fixed to the oracle's, and the decider's acceptance implies the oracularized predicate. It is inhabited by the construction, and the value transfers are theorems about every inhabitant, both for the typed game and for the verifier with $\ell + 3$ levels that the detyping compiler produces. In the source, oracularization is internal to the proof of Theorem [Answer reduction](../part-09/thm-answer-reduction.md), whose analysis uses the typed verifier and detypes only the final answer-reduced verifier. The checked composition `MIPRE.GapCompression.ofPipeline` does not consume `MIPRE.Oracularization`, and the detyped verifier is not a stage of compression.

**Remark (What the audit changed in oracularization).** Node $1.3.5$ was added late — round 12 of the campaign found that `oracularization.tex` was covered by no ledger node at all, although both of its theorems are consumed by answer reduction — and it carries four repairs that the statement above has been written to respect.

1. The soundness constant $\delta_\textsc{Orac}$ carries *one square root*: the step from a $1 - O(\varepsilon)$ measurement-closeness to a $1 - O(\sqrt{\varepsilon})$ statement about the value is an application of (NW19, Fact 4.31), not an identity. An earlier revision of this blueprint wrote $\delta(\varepsilon) = \mathrm{poly}(\varepsilon)$, which is not merely imprecise but false as stated: $\sqrt{\varepsilon}$ is not a polynomial in $\varepsilon$.
2. The completeness witness's extra property is *identical measurement operators*, not symmetry of the state. The campaign found the claim that the constructed strategy is symmetric “by construction” unjustified — the hypothesis supplies a value-$1$ PCC strategy whose state is reused unchanged, and no lemma in the paper symmetrizes such a strategy while preserving projectivity, consistency and value $1$. SPCC was withdrawn from the completeness clause in consequence. The ambient interface starts from a different strategy representation; transferring this source witness requires Remark [Source PCC and the required representation bridge](../../foundations/README.md).
3. The oracle families are genuine projective measurements. Outcomes failing the decider's bounded parse are grouped into a distinguished outcome; leaving that implicit made them sub-measurements, which the later sandwiching argument may not use.
4. The truncation of answers to $B_\mathcal{D}(n)$ symbols is justified by a corollary of the timeout-counter form, not by the assertion that a timeout-form decider inspects at most $B_\mathcal{D}(n)$ symbols. Nothing forces $B_\mathcal{D}(n)$ to exceed the time bound $T$ against which the PCP decodes, so the truncation is load-bearing and a formalization must carry it explicitly.

## Answer reduction

After introspection the decider still runs in time exponential in $n$ (it simulates $\mathcal{D}$ at index $2^n$), and the players' answers are correspondingly long. Answer reduction composes the game with a PCP: by Theorem [Explicit succinct Cook–Levin](../../background-results/part-04/thm-succinct-sat.md) the statement “the original decider would have accepted our answers” is a succinct 3SAT instance; the players commit to a low-degree encoding of a satisfying assignment (their original answers plus the computation tableau) and the new decider spot-checks it, using the low individual degree test to certify the encoding and Lemma [Schwartz–Zippel](../../background-results/part-05/lem-schwartz-zippel.md) for the arithmetization. Answers and decider time become polylogarithmic in the original.

- [Succinct decoupled 5SAT](lem-decoupled-5sat.md)

**Remark (Two repairs this proof carries).** An earlier sketch here described decoupling as a generic syntactic transformation — split a clause that touches a block twice by adding a fresh variable and an equality clause — which is not the construction the source gives and does not produce the promised index lengths: $\ell_0$ is pinned to $\lceil \log 2T \rceil$ by the answer blocks, and a generic splitting fixes neither that nor $r_0$. The proof above is the source's.

The parities of the four padding conditions are a repair of the verification campaign, and the one place where a careless transcription breaks completeness rather than soundness. Blocks are $0$-indexed and the blank encodes as $10$, so the honest padding begins at the even index $2T$ and puts $1$ at even indices and $0$ at odd ones; the pre-repair text had it the other way round, which the honest assignment violates. The formalization's tape encoding agrees with the repaired parity, so nothing had to be adapted — but nothing was taken on trust either.

[$\checkmark$ (mostly) in Mathlib]

- [The low-degree code](def-ld-encoding.md)

Source. The paper states this in `preliminaries.tex`, Section `sec:ld-encoding`, alongside Lemma [Schwartz–Zippel](../../background-results/part-05/lem-schwartz-zippel.md); it is recorded here, with its consumer, because Theorem [The bespoke PCP for deciders](thm-pcp-decider.md) is the only place the blueprint uses it.

Comments. The identification of $\{0,1\}^m$ with $\{1, \ldots, M\}$ is any fixed bijection — the paper says “lexicographic”; the formalization uses the repository's existing little-endian `bitsVal` convention, so that the encoding of an answer block agrees with the tape indexing of Theorem [Explicit succinct Cook–Levin](../../background-results/part-04/thm-succinct-sat.md). The choice is invisible to the statements below, the same bijection appearing in the encoding and in the decoding.

- [Restriction to a line](def-line-restriction.md)

[$\bullet\bullet\bullet$ hard]

- [Padding preserves the complete answer tapes](lem-pcp-padding-semantics.md)
- [Effective indexing and padding arithmetic](lem-pcp-padding-programs.md)
- [Effective padded descriptions with an explicit output budget](prop-pcp-padded-describer.md)
- [Effective classical PCP parameters](lem-pcp-effective-parameters.md)
- [Circuit arithmetization with bounded input use](lem-pcp-circuit-arithmetization.md)
- [Effective circuit polynomial evaluation](lem-pcp-circuit-evaluator.md)
- [PCP semantics for a circuit describer](lem-pcp-circuit-semantics.md)
- [Encoded PCP view size and source runtime](lem-pcp-view-size.md)
- [The executable PCP tests](lem-pcp-executable-tests.md)
- [Formula arithmetization and occurrence bounds](lem-pcp-formula-arithmetization.md)
- [Boolean-cube zero certificates](lem-pcp-zero-basis.md)
- [The algebraic PCP tests](lem-pcp-algebra-tests.md)
- [PCP answer blocks, honest proof and decoded clauses](lem-pcp-proof-algebra.md)

Scope. Lemma [PCP semantics for a circuit describer](lem-pcp-circuit-semantics.md) supplies the clause-description polynomial and its relation to the input decider. Lemma [The executable PCP tests](lem-pcp-executable-tests.md) supplies the raw verifier and its runtime.

- [The bespoke PCP for deciders](thm-pcp-decider.md)
