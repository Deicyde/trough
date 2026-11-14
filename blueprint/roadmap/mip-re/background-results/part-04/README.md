---
navigation: transparent
---

# Explicit succinct Cook–Levin to Effective unary prime-power…

- [Explicit succinct Cook–Levin](thm-succinct-sat.md)

Lean statement. The theorem is the structure `MIPRE.SAT.SuccinctCookLevin`: the algorithm a polynomial-time function of the ambient model (`PolyTimeFun`) from $((\mathcal{D}, n, T, Q, \sigma), x, y)$ to circuits as data, “within $T$ steps” read as cost at most $T$ in the ambient model, the reading of every time bound of the pipeline, and the five items as fields. An earlier statement asked for a succinct description in the sense of Definition [Succinct description](../../foundations/part-02/def-succinct.md), which is a program answering bit queries and not the circuit the proof produces and the PCP consumes, and it carried none of the five items, all of which Lemma [Succinct decoupled 5SAT](../../structure-of-the-proof/part-07/lem-decoupled-5sat.md) and the PCP parameters depend on. The statement is validated by its consumer (`MIPRE.SAT.DecoupledDescriber`, Lemma [Succinct decoupled 5SAT](../../structure-of-the-proof/part-07/lem-decoupled-5sat.md)) before its proof; the route to the proof is `planning/succinct-cook-levin.md`.

Formalization status. Complete: statement and proof, the structure inhabited by `MIPRE.SAT.succinctCookLevin` (`MIPRE/TM/CookLevin/`). Three things the formalization settled against the first design, all recorded in `planning/succinct-cook-levin.md`. The index width has $W = e + 4$, not $e + 2$, because a position field must hold $2S + 7$; the state field is $\lceil \log |Q| \rceil$ bits rather than a fixed four. Two clauses beyond the tableau are needed: soundness needs answers of length at most $T$, and the tableau alone admits answers of length up to $2S$. And the canonical index of an answer cell of a free tape is its answer index, not its structured index — that is what ties the extension hypothesis on the first $4T$ variables to the time-$0$ row of the tape, and getting it wrong makes the soundness direction unprovable rather than merely awkward.

Two notes on the Lean, both about scale. The check circuit of the interpreter machine is the truth-table circuit of a fixed Boolean function on the window variables, so its gate count is $7 \cdot 2^{|\mathrm{window}|}$ — an enormous constant, exactly as the paper's `lem:pack-check-size` carries one. Nothing unfolds it, and nothing may: the defining terms of the state count and of the check circuit mention a cardinality and a truth table whose evaluation does not terminate in practice, so they are kept opaque (the state width is `irreducible` and the circuit is taken from an existential). And the program layer is written so that each of the fifty-odd family formulas costs one `simp`: a field record is a record of *readers* of the describer's input whose evaluation is a structure literal of those programs' own values, which makes every formula match its program definitionally.

Source. Cook (Coo71) and Levin for the tableau reduction; Papadimitriou and Yannakakis (PY86) for succinct representations and their complexity; the explicit form needed here is (JNVWY20, Section 10).

Comments. This is the classical core of answer reduction: the players prove satisfiability of $\varphi$ (arithmetized over a low-degree extension) instead of sending $(a,b)$. The statement is long but entirely combinatorial. Cook–Levin has been formalized in other proof assistants; a Lean formalization with the explicit-uniformity guarantees above is a substantial but well-specified sub-project.

A caution on the construction, from the verification campaign (Audit26) and not checked here: in the Tseitin encoding of (NW19), which the explicit form of (JNVWY20, Section 10) follows, the formula is reported to omit the output-wire conjunct, so that it is satisfiable for every input and the central equivalence of the construction fails as written. The statement above is end-to-end and so does not inherit the defect textually, but a formalization of it must supply what the repair needs: the output-wire conjunct, the out-degree-zero hypothesis that yields individual degree $6$, and the exact variable count on which the later PCP parameters depend — none of which the statement currently fixes.

- [Correctness of the Cook–Levin tableau](lem-correct-tableau.md)

Source. The tableau of (JNVWY20, Section 10) and the standard argument of Cook (Coo71); the companion paper's `answer_reduction.tex` (its `lem:correct-tableau`).

Comments. The lemma is Cook–Levin for one fixed machine; the theorem applies it to a fixed interpreter machine for the decider's program, and the succinct description is a circuit for the clauses of this formula — pieces S2 and S3 of `planning/succinct-cook-levin.md`. The interpreter machine (S2) is formalized: `MIPRE.TM.Interp.U`, with `accepts_of_acceptsWithin` and `acceptsWithin_of_accepts` (`MIPRE/TM/Interp/Run.lean`) — on the inputs $(\mathcal{D}, n, T, x, y, a, b)$ with $\left\vert {a} \right\vert, \left\vert {b} \right\vert \leq T$, it halts having output exactly $1$, within an explicit polynomial number of steps, if and only if $\mathcal{D}$ accepts $(n, x, y, a, b)$ within cost $T$. The local check circuit is a parameter of the formula, with its specification a hypothesis of the lemma, so that the lemma is proved once and the circuit supplied with the describer. The windows are five cells wide: a head at one of the middle three cells then sees, in the window, both the cell it leaves and the cell it reaches, and the clamped moves of an input head at the ends of the input are decided from the window alone.

## Self-dual normal bases

[$\bullet\bullet$ medium]

*( Thomas: Is this needed? )*

- [Self-dual and normal bases](def-self-dual-basis.md)
- [Self-dual coordinates are trace pairings](lem-downsize-field.md)

Source. Items 1 and 2 of the paper's `lem:downsize_field` (`preliminaries.tex`); ledger node `1.1.6.1.11`, which also records that neither item needs normality or odd $k$. The paper's third item, compatibility of the downsized matrix map with $\kappa$ ($\kappa_{\mathrm{m}}(M)\kappa(v) = \kappa(Mv)$), is not formalized here: it is wanted by the conditionally linear downsizing of Lemma [Downsizing](../../structure-of-the-proof/part-01/lem-cl-downsize.md), which is stated over $\mathbb{F}_2$ and so has not needed it.

Comments. These two identities are why the pipeline insists on self-duality rather than on an arbitrary basis: they make $\kappa$ computable by the trace form, with no matrix inversion, and turn the trace form into the standard inner product on coordinates. They are also what collapses the Pauli phase index $G_E \kappa(b)$ to $\kappa(b)$ at $G_E = I$ (ledger node `1.1.6.1.13`).

- [Deterministic self-dual normal basis](lem-self-dual-basis.md)

Source. Shoup's deterministic irreducible-polynomial construction (Sho90), and then the companion campaign's own constructions. The attribution here used to name Lenstra's isomorphism algorithm (Len91) and the classical characteristic-$2$ existence results, following the discussion in (JNVWY20, Section 3); the campaign has since *proved* both steps — ledger node $1.1.6.1.6$ discharges the normal-basis construction contract “formerly attributed to Lenstra” and node $1.1.6.1.8$ the self-dualization contract “formerly attributed to Wang” — and the Lean development now proves the remaining Shoup construction as well.

Comments. Needed so that verifiers can do field arithmetic over $\mathbb{F}_{2^k}$ using only $\mathbb{F}_2$-data (the “downsize” maps), uniformly and deterministically. This is why field sizes are restricted to $q = 2^k$, $k$ odd (“admissible”). Self-contained algebra/algorithmics; independent of everything quantum. Two consumers now name it: the admissible field with a bit representation that Theorem [The bespoke PCP for deciders](../../structure-of-the-proof/part-07/thm-pcp-decider.md) takes as a parameter (`MIPRE.SAT.BinField`), and the downsized samplers of Lemma [Downsizing](../../structure-of-the-proof/part-01/lem-cl-downsize.md) once they move past field size $2$.

The companion ledger retains its historical admission of Shoup's construction at node $1.1.6.1.1$. The Lean declaration `MIPRE.LowDegree.exists_shoup_irreducible` is now a theorem, proved by the explicit program of Lemma [Uniform deterministic binary irreducible polynomials](../part-05/lem-binary-uniform-irreducible.md). Its input is the requested degree in unary, so the ambient bound is polynomial in the degree and includes printing all coefficient bits. The proof covers every positive degree in characteristic two, including powers of two, with fixed behavior at degree zero.

The complete effective self-dual normal-basis construction in `SAT/EffectiveNormalBasis.lean` composes this proved field constructor with the verified normal-element, inverse-Gram self-dualization, and multiplication-table programs. Fixed-space separation is performed directly in the cyclic algebra, as detailed in Lemma [Effective normal element by fixed-space projections](../part-05/lem-effective-normal-element.md); this avoids materializing polynomial factors while implementing the primitive-projection argument. Exact axiom guards in `MIPRE/Axioms.lean` check the field constructor, the classical PCP decider, and this effective basis theorem against Lean's standard axioms alone. This local proof does not rewrite the companion ledger's events or discharge unrelated unfinished pipeline theorems.

- [Self-dualization in the group algebra](lem-group-algebra-selfdualization.md)

Comments. This is the self-dualization step of Lemma [Deterministic self-dual normal basis](lem-self-dual-basis.md), and it is where oddness of $k$ is used. If $\alpha$ is a normal element of $\mathbb{F}_{2^k}/\mathbb{F}_2$ with Galois group $G$, the trace-form Gram matrix of its orbit is the circulant determined by $c \in \mathbb{F}_2[G]$, $c(g) = \mathrm{tr}(\alpha \cdot g\alpha)$: it is a unit, because the Gram matrix of a basis under the nondegenerate trace form is invertible, and it is fixed by the involution $\tau$ induced by $g \mapsto g^{-1}$, because that Gram matrix is symmetric. Replacing $\alpha$ by $a \cdot \alpha$ replaces $c$ by $a \cdot \tau(a) \cdot c$, so a self-dual normal basis is exactly a solution of $a \cdot \tau(a) = c^{-1}$, which is what the lemma supplies. Nodes $1.1.6.1.7$ and $1.1.6.1.8$ carry an explicit circulant Gram manipulation instead; the argument above replaces it, and needs no factorization of $X^k - 1$ and no norm computation in the factors.

What the lemma does *not* do is assemble a basis: the group algebra must be made to act on $\mathbb{F}_{2^k}$, the Gram identity must be proved, and $c$ must be shown to be a unit. Those three are bookkeeping, and Lemma [Existence of a self-dual normal basis](lem-self-dual-basis-exists.md) now carries them out; the algorithm is a separate matter again.

- [The binary square-root program](lem-binary-square-root-program.md)

Scope. This completes the square-root operation only. Computing the normal element, the inverse Gram element and the transported field tables remains part of Lemma [Deterministic self-dual normal basis](lem-self-dual-basis.md).

- [Existence of a self-dual normal basis](lem-self-dual-basis-exists.md)

Comments. This is existence, not construction, so it is not Lemma [Deterministic self-dual normal basis](lem-self-dual-basis.md) and does not discharge any ledger node: the normal element comes from Mathlib's `IsGalois.normalBasis`, which is a theorem and not an algorithm, and nothing here is claimed to run in $\mathrm{poly}(k)$. What it does settle is that the three bookkeeping items left open by Lemma [Self-dualization in the group algebra](lem-group-algebra-selfdualization.md) — making the group algebra act, the Gram identity, and unitness of $c$ — are genuinely bookkeeping, and that the short self-dualization argument assembles. The formalization indexes the group algebra by $G$ itself rather than by $\mathbb{Z}/k$, which is what makes $\mathrm{ofAlg}$ the inverse of Mathlib's `normalBasis.repr` on the nose; the `CommGroup` instance comes from cyclicity, supplied locally.

- [Effective normalization of binary polynomials](lem-binary-polynomial-normalization.md)

Scope. This generic normalization result is used by the complete irreducible-polynomial constructor in Lemma [Uniform deterministic binary irreducible polynomials](../part-05/lem-binary-uniform-irreducible.md).

- [Effective monic binary division](lem-binary-monic-division.md)
- [Canonical coordinates in monic binary quotients](lem-binary-monic-quotient.md)

Scope. The coordinate maps describe the semantics of the explicit coefficient programs. They do not enumerate a quotient or supply an abstract field conversion as an executable primitive.

- [Canonical binary Euclidean algorithms](lem-binary-euclidean-algorithms.md)
- [Effective Frobenius fixed spaces in binary quotients](lem-binary-quotient-fixed-space.md)

Scope. Computing a spanning family does not enumerate its binary linear combinations. The next lemma extracts and reconstructs the factors.

- [Deterministic squarefree binary factorization](lem-binary-squarefree-factorization.md)
- [Effective closed Frobenius orbit polynomials](lem-binary-orbit-polynomial.md)
- [Effective odd-prime nonresidues](lem-binary-odd-prime-nonresidue.md)
- [Effective irreducibles of every power-of-two degree](lem-binary-power-two-irreducible.md)
- [Effective irreducibles of every odd-prime-power degree](lem-binary-odd-prime-power-irreducible.md)
- [Effective combination of coprime degrees](lem-binary-coprime-degree-combination.md)
- [Effective unary prime-power decomposition](lem-binary-degree-decomposition.md)
