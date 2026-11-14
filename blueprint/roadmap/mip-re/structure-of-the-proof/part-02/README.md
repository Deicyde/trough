---
navigation: transparent
---

# Finite-game detyping soundness to Conditioning on part of a…

- [Finite-game detyping soundness](lem-detype-game-soundness.md)

**Remark (Turing machine conventions and the ambient cost model).** The paper fixes a concrete Turing machine formalism and a *timeout-counter* normal form $B(n) = c_0 (c_1 n)^{c_2}$: a machine is wrapped so that it always halts within its bound, and the wrapped description is canonical enough that the parameters can be read back off it. The ambient Lean model instead uses input-size-dependent resource budgets (Section [Efficient computability toolkit](../../computability/README.md)). This changes the transformation hypotheses; it does not establish the source's timeout or answer-truncation properties. Remark Runtime normalization obligation records the required adaptation, and Section [Departures from the paper](../../introduction/README.md) records the departure.

Three things in those nodes are worth keeping even so, because they are the kind of detail a formalization rediscovers the hard way. The canonical form has to be genuinely injective in the parameters for the timeout bound to be well defined at all, and the audit had to supply an explicit parser to establish it — in the source the parser's existence was asserted rather than constructed. The overhead polynomial relating a machine's running time to its bound needs the normalization $c_1 \geq 2$, without which the claim fails outright at $c_1 = 1$, $n = 1$. And the whole scheme rests on the bound dominating $n$, which holds only because the constants are positive integers. None of the three is deep; all three are the sort of thing that stops a formalization dead.

**Remark (Runtime normalization obligation).** The model distinction is recorded in Remark [The runtime-contract bridge remains an obligation](../../foundations/README.md); here are its consequences for the transformations. The source introspection theorem uses an absolute bound $N^\lambda$ at index $N$; its simulator rejects after that many steps. Definition [$\lambda$-bounded verifier in the ambient model](../../foundations/part-03/def-lambda-bounded.md) instead bounds ambient cost on data $d$ by $N^\lambda(\left\vert {d} \right\vert+1)^\lambda$. Even on questions and answers of length at most $N^\lambda$, this supplies a bound of order $N^{O(\lambda^2)}$, before simulation overhead, rather than $N^\lambda$. It also gives no answer-prefix invariance for arbitrary longer strings.

To derive the ambient transformation hypotheses from the source, a normalization construction must restrict the valid input formats, preserve the original answer cut, and prove preservation of values and perfect PCC witnesses. It must provide the absolute simulation budgets and the truncation properties required by the source, including bounded checks on malformed inputs. If this requires a reparameterization $\lambda' = p(\lambda)$, its effect on the introspection bound $\mathrm{poly}(2^{p(\lambda)n},\ell)$ and on the soundness margins must be propagated. Enlarging the answer alphabet to $N^{\lambda'}$ without rejecting answers beyond the original cut can change the game. A direct proof in the ambient model is another route.

Lemma [Absolute costs on the original legal answer cut](lem-intro-ambient-runtime.md) proves the absolute legal-input bound and its universal-simulator overhead. The ambient introspection and answer-reduction contracts now allow the polynomial-exponent bounds $2^{(\lambda n+1)^C}$ and $2^{(\lambda n+1)^\mu}$. Answer reduction also retains the input sampler's degree in its output budget, as in Lemma [Ambient sampler-cost absorption](lem-ar-ambient-sampler-cost.md). The full compression composition is checked with these revised contracts and still has polynomial output bounds. This is an explicit ambient adaptation; the paper's source-model theorem statements below retain their original time bounds. The absolute PCP clock, normalization construction and format-preservation clauses remain open. `Budget` and `Verifier.Within` record coefficients, degrees, question dimensions and explicit rejection bounds; `GapCompression.output_rejects_long` constrains the output. None of these supplies normalization for arbitrary $\lambda$-bounded inputs. The introspection, oracularization and answer-reduction source displays below use the paper's absolute-time convention and its bipartite PCC notion. Separate ambient contract definitions carry the Lean tags and statement marks; their inhabitants require the supply targets stated below. In particular, identifying source PCC witnesses with ambient completeness witnesses requires the two directions of Remark [Source PCC and the required representation bridge](../../foundations/README.md). The comparison is with `introspection.tex`, `oracularization.tex` and `ld_compiler.tex` in the companion paper pinned by (AuditSync26).

- [Absolute costs on the original legal answer cut](lem-intro-ambient-runtime.md)
- [Ambient sampler-cost absorption](lem-ar-ambient-sampler-cost.md)

### The introspective verifier

- [The introspective verifier](def-intro-verifier.md)

[$\bullet\bullet\bullet$ hard]

- [Introspection type graph and typed CL family](lem-intro-type-presentation.md)
- [The parsed introspection decision predicate](lem-intro-parsed-predicate.md)
- [The executable five-level introspection sampler](lem-intro-executable-sampler.md)

**Remark (A false step in computing the hidden subspace).** The decider has to compute, for a level $k$ and a prefix $u$, the orthogonal complement $(L^v_{k+1, u})^\perp$ of the conditionally linear map at that level. The printed procedure computed it by taking a basis of $\ker(M)$ and forming its canonical complement — and the canonical complement of a basis of $\ker(M)$ is *not* a basis of $\ker(M)^\perp$. Over $\mathbb{F}_2^2$ the map $L(x_1, x_2) = (x_1 + x_2, 0)$ is a counterexample, found independently by two checkers. Only the computation was wrong: the test itself is defined abstractly through the complement, so the statement of Lemma [Complexity of the introspective verifier](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/06_proof_structure.tex#L1165) and its bound are unaffected. It is recorded because a formalization must supply a procedure that is actually correct, and this is the obvious place to get it wrong. The same audit closed a second seam here, an answer-length bound of $8Q$ that only holds once the honest answer is truncated the way oracularization and answer reduction already truncate theirs.

### Completeness: two identities about Pauli measurements

The honest strategy measures EPR pairs in the bases the sampled question prescribes, so the completeness proof is not an approximation argument at all: it is two exact statements about how Pauli operators interact with measurements of a linear map, and then a check that the seven tests of the decider all pass with certainty. Both identities are finite-field linear algebra, and both are plausible early Lean targets.

[$\bullet\bullet$ medium]

- [Pauli operators against a linear-map measurement](lem-pauli-linear-fourier.md)

[$\bullet$ easy]

- [A commutation criterion for $X$ and $Z$ measurements](lem-pauli-commute-criterion.md)

[$\bullet\bullet\bullet$ hard]

- [Projectivity of sampling and hiding readouts](lem-intro-linear-readout-projectivity.md)
- [Completeness of introspection](lem-intro-completeness.md)

### The soundness toolkit

Soundness needs three groups of lemmas before the induction can start, and they are separated here because they are independent of introspection and reusable: a Pauli twirl, a conversion from sub-measurements to measurements, and a way to condition on part of a question.

[$\bullet\bullet\bullet$ hard]

- [Exact Pauli twirling](lem-pauli-twirl.md)
- [Linear-map blocks of the twirl](lem-pauli-linear-mixing.md)
- [Commutator Parseval identity](lem-pauli-commutator-transfer.md)
- [Approximate commutation controls unitary mixing](lem-pauli-unitary-mixing.md)
- [Combining two approximate commutations](lem-pauli-two-sided-commutation.md)

[$\bullet\bullet$ medium]

- [Completing a nearby submeasurement](lem-close-submeasurement.md)
- [Retained-fibre mixing in coordinate presentations](lem-pauli-mixing-coordinates.md)
- [Pauli mixing with a retained classical fibre](lem-pauli-mixing.md)

[$\bullet\bullet\bullet$ hard]

- [Conditioning on part of a question](lem-conditional-measurement.md)
