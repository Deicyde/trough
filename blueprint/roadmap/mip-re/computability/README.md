# Computability

This chapter collects the computability-theoretic ingredients of the proof: classical statements with no quantum content, several of which partially exist in Mathlib. Like the results of Section [Background results](../background-results/README.md), these are external results that the project may initially assume as axioms, and each entry carries the same formalization-effort estimate. The concrete machine model and its canonical codes come first; then the toolkit of resource-bounded computability results; the recursive compression lemma, which builds on the toolkit, isolates the self-referential part of the proof.

## The machine model

The machine-level side of the project is formalized directly: a concrete multi-tape machine model with several input tapes, a canonical first-order syntax of machine *codes* with an exact binary serialization, and a reference evaluator.

- [Multi-input Turing machine](def-multiinput-tm.md)
- [Machine codes](def-machine-code.md)
- [Runs of coded machines](def-code-run.md)
- [Canonical serialization](lem-code-canonical.md)

The following two statements are the machine-level counterparts of Lemma [Efficient universal Turing machine](lem-universal-tm.md).

- [Universal machine](lem-universal-machine.md)
- [Bounded universal machine](lem-bounded-universal-machine.md)

## Efficient computability toolkit

[$\bullet\bullet\bullet$ hard] (infrastructure: requires a cost model for computation)

- [Efficient universal Turing machine](lem-universal-tm.md)
- [Efficient s-m-n](lem-smn.md)
- [Efficient Kleene recursion theorem](lem-kleene.md)

Source. Folklore; stated in this efficient form in (MNY), Lemmas 2.1–2.3.

Comments. Mathlib contains the non-resource-bounded versions (universal machine, s-m-n and the Rogers fixed-point theorem for `Nat.Partrec.Code`). The efficient versions require a cost model for the chosen machine model; this is real infrastructure work and a prerequisite for everything involving “polynomial-time”. The formalization's ambient model is not a Turing machine but a small first-order list-processing language (`MIPRE.Cost.Prog`, over binary trees) with a unit-cost semantics in which reading a value costs its size; it is polynomially equivalent to Turing-machine time, programs are their own tree serializations (so “a program $e$” and “$\left\vert {e} \right\vert$” are literal), and the s-m-n theorem is a linear-overhead syntactic operation. Mathlib's `Turing.ToPartrec.Code` was tried first and rejected: its programs cannot rebuild a list in polynomial time. A pragmatic first pass can replace “polynomial time” by “computable” wherever Section [Departures from the paper](../introduction/README.md) permits, deferring the cost model. The machine-level counterpart, for the concrete model of Section The machine model, is stated as Lemmas [Universal machine](lem-universal-machine.md) and [Bounded universal machine](lem-bounded-universal-machine.md); the pipeline consumes only the present ambient version.

## The abstract compression lemmas

[$\bullet$ easy] (given the toolkit of Section Efficient computability toolkit)

- [Recursive compression](lem-recursive-compression.md)

Source. Marks, Nezhadi and Yuen (MNY), Lemma 5.1 (the variant of their Lemma 3.1 with compression parameter $n$); the technique is implicit in (DRS08, FJVY19, JNVWY20). The proof is a fixed-point construction using the efficient universal machine, s-m-n and Kleene recursion theorems (Section Efficient computability toolkit).

Comments. This is the entire “self-referential” part of the proof, isolated in a statement with no quantum content. In the application (Section [The halting reduction](../structure-of-the-proof/README.md)), $A$ is the set of normal form verifier descriptions with ${\mathrm{val}^{s}} = 1$ and finite entanglement requirement, and $f(\mathsf{V}) = \mathrm{Ent}(\mathsf{V}, \frac12)$ (suitably formalized); the compression procedure is Theorem [Gap-preserving compression from ambient stage contracts](../structure-of-the-proof/part-09/thm-compression.md). The value-form pipeline of Section [Structure of the proof](../structure-of-the-proof/README.md) uses Lemma [Compressibility criterion](lem-compressible-criterion.md) below instead; this lemma is retained as the entanglement-form route (Remark [The entanglement form of (JNVWY20)](../structure-of-the-proof/README.md)), where the factor $\frac12$ in the entanglement bound of compression requires the variant with hypothesis $f(y) \geq \frac12 \max\{f(x), G(n)\}$ for a function $G$ growing faster than the levels. Note that (MNY) also proves a converse (their Lemma 4.1): a halting reduction of this kind exists *only if* a compression procedure does, which is evidence that this decomposition of the proof is canonical. The lemma and its proof are a self-contained computability project, an ideal early milestone.

- [Compressibility criterion](lem-compressible-criterion.md)
- [Compressibility criterion, nested classes](lem-compressible-criterion-nested.md)

Source. Lin (Lin25), the compression criterion for $\mathrm{RE}$-complete problems (direction “weakly compressible implies $\mathrm{RE}$-complete”), whose self-referential sequence has exactly these three branches; the formulation through succinct descriptions is that of (MNY) and of Lemma [Recursive compression](lem-recursive-compression.md). Lin's theorem is an equivalence: given that the no-instances form a $\mathrm{coRE}$ set, a decision problem is $\mathrm{RE}$-complete if and only if it is compressible.

Comments. This is the lemma the main theorem uses (Section [The halting reduction](../structure-of-the-proof/README.md)): $A$ is the set of normal form verifier descriptions with a value-$1$ PCC strategy, $B$ the set of those with $\mathrm{val}^* \leq \frac12$, and $S$ the $\mathrm{val}^*$ half of the enumeration of Lemma [The value is approximable from below](../background-results/part-05/lem-value-lower-approx.md). Compared with Lemma [Recursive compression](lem-recursive-compression.md), the growth hypothesis on a measure is replaced by the semidecidability of the complement of $B$ — both directions of the specification of $S$ are used — and nothing about entanglement is required of the compression procedure. The Lean proof reuses the toolkit of Section Efficient computability toolkit: the search branch runs the semidecision procedure through the clocked universal machine, and the start level of the recursion is carried as data next to the current level.

The Lean file proves a *per-level* form first, `compressibility_criterion_levels`, and derives the statement above from it. There the classes are families $A_n, B_n$ indexed by the level $n$ of the recursion, the semidecision procedure receives the pair $(x, n)$, and the compression hypothesis reads: for $n \geq n_0$, if $\hat x$ describes $x$ succinctly with parameter $n$ and $2\left\vert {\hat x} \right\vert \leq n$, then $x \in A_{2n+1}$ implies $\textsc{Compr}(\hat x, n) \in A_n$, and likewise for $B$; the conclusion places $g(e)$ in $A_{r(e)}$ or $B_{r(e)}$ at the explicit start level $r(e) = 2^{K + 1 + \left\vert {e} \right\vert}$, which is at least $n_0$. This is exactly what the proof uses, and it is the form an instantiation by gap-preserving compression can meet (Remark [Relation to the abstract compression lemma](../structure-of-the-proof/README.md)): $\textsc{Compr}$ runs in time polynomial in the *length* of $(\hat x, n)$, hence polylogarithmic in $n$, while a single bit query to $\hat x$ costs up to $n$, so $\textsc{Compr}$ cannot read the string $x$ it compresses and can only embed $\hat x$ into its output, for a reader whose budget is polynomial in $n$ — the decider of a game at index $n$. The size slack $2\left\vert {\hat x} \right\vert \leq n$ keeps that output short, and the levels are what let the class of the output be judged at the index where it is played.

The hypothesis $\left\vert {x} \right\vert \leq n + 1$ is not an extra demand on $\textsc{Compr}$ but a *weakening* of what it must cover, and it was added because obligation O4 cannot be met without it. The proof already has it: the described string is the output of a run whose cost the threshold constant bounds by $n + 1$, so $\left\vert {x} \right\vert \leq \left\vert {\mathrm{encode}(x)} \right\vert \leq t \leq n + 1$, and until this was carried over the proof discarded it into Definition [Succinct description](../foundations/part-02/def-succinct.md)'s $\left\vert {x} \right\vert \leq 2^n$ through $n + 1 \leq 2^n$. Why O4 needs it: the class $A$ of the halting reduction asks for a value-$1$ PCC strategy at the answer bound $\mathrm{poly}(n, \lambda_x)$ read off the described string's own compression parameter $\lambda_x$, while the only source of such a strategy for a compressed verifier is the completeness clause of Theorem [Gap-preserving compression from ambient stage contracts](../structure-of-the-proof/part-09/thm-compression.md), which takes its input at the bound $(2^n)^\lambda$ with $\lambda$ the parameter the compressor *writes into its output* and so bounded by the compressor's own output size. Nothing in Definition [$\lambda$-bounded verifier in the ambient model](../foundations/part-03/def-lambda-bounded.md) constrains $\lambda_x$ — for a compression procedure whose compressed sampler does not vary with $\lambda$, membership in either class is insensitive to it — so with only $\left\vert {x} \right\vert \leq 2^n$ the two bounds cannot be related by any single choice of $\lambda$. With $\left\vert {x} \right\vert \leq n + 1$ we get $\lambda_x < 2^{n+1}$, hence an answer bound of $2^{O(n)}$ against $(2^n)^\lambda$, which $\lambda \geq 2\deg(\mathrm{bound}) + 1$ already dominates for $n$ above a threshold read off $\mathrm{bound}$ as well; the Lean says so and checks it (`MIPRE.Halting.exists_ansBound_le`).

That settles the class $A$ direction. The class $B$ direction needs the same inequality read the other way — the soundness clause of Theorem [Gap-preserving compression from ambient stage contracts](../structure-of-the-proof/part-09/thm-compression.md) wants the value bounded at $(2^n)^\lambda$, and enlarging the answer bound can only raise a value — so a single $\lambda$ serves both only once the described string's own decider is known to reject answers longer than its answer bound, which is what $\mathrm{poly}(n, \lambda_x)$ was chosen to be. The paper's $\mathsf{V}^{\mathsf{halt}}$ has that by construction — Step 6 of its decider is an explicit length check, spent in the amended proof of Lemma [Values of the halting verifier](../structure-of-the-proof/part-09/lem-dhalt-values.md) — and the instantiation asks for it as a clause of membership in $A_n$ and $B_n$ (Remark [Relation to the abstract compression lemma](../structure-of-the-proof/README.md), item 1; `Verifier.RejectsLong`): the two distinguished strings have it, the compressor's output has it by the length check of Theorem [Gap-preserving compression from ambient stage contracts](../structure-of-the-proof/part-09/thm-compression.md)'s decider (`output_rejects_long`), and its violation is enumerable (Lemma [The semidecider of the halting reduction](../structure-of-the-proof/part-09/lem-halting-semidecider.md)). The alternative, a well-formedness predicate threaded through this lemma and instantiated to the same clause, would have left the classes alone and touched this lemma's proof instead; the classes were chosen so that this lemma stays as stated. Nothing more is asked of it.

[$\bullet$ easy]

- [Halting form of the two reduction lemmas](lem-halting-form.md)

Comments. This is the seam at which the development meets Mathlib's halting problem, hence the form Theorem [Halting reduces to the game value; Theorem 12.2 of (JNVWY20), synchronous form](../the-main-theorem/thm-main.md) consumes: `Nat.Partrec.Code` is what `Computable` is stated against, while the two reduction lemmas are proved about programs of the cost model of Section Efficient computability toolkit, whose polynomial-time predicate the fixed-point construction needs. Separating the two keeps the cost model out of the main statement entirely.

## Deciding a cost budget, and semideciders on encoded values

Lemma [Compressibility criterion](lem-compressible-criterion.md) consumes semidecidability as an *equivalence*: its program $S$ halts on exactly the complement of $B$. When the criterion is instantiated by the halting reduction that complement is a disjunction of two searches (Remark [Relation to the abstract compression lemma](../structure-of-the-proof/README.md), item 3), one of them for an input on which a time bound of Definition [$\lambda$-bounded verifier in the ambient model](../foundations/part-03/def-lambda-bounded.md) fails. Recognizing such an input exactly — and not merely recognizing a program that runs for a long time — is what the first lemma here provides; the second moves the resulting semidecider off bit strings, the criterion's $B$ being indexed by a level as well as a string.

- [Halting within a cost budget is decidable](lem-cost-budget-decidable.md)

Comments. A step budget does not decide a cost budget, which is why this is not a corollary of `Machine.runForD` (Remark [Relation to the abstract compression lemma](../structure-of-the-proof/README.md), item 3): a step is not a unit of cost, reading a variable or a constant being charged the size of the value, so a run of $3k$ steps can cost far more than $k$ and finding a value after $3k$ steps says only that the program halted. The clocked universal machine of Lemma [Efficient universal Turing machine](lem-universal-tm.md) decides the same question as a *program*; what is added here is the Lean-level decision procedure, which is what a computability statement about a family of verifiers can be built from.

[$\bullet$ easy]

- [Semideciders on encoded values](lem-semidecide-encoded.md)

Comments. The detour through a serialization is what keeps the translation into `ToPartrec` codes untouched. That translation is delicate for one reason — a `ToPartrec` code cannot see trailing zeros of its input list, while the bit `false` encodes as the datum $\mathtt{nil}$ — and doing it again for each new type of argument would repeat the delicate step; serializing first does it once.

[$\bullet$ easy]
