---
navigation: transparent
---

# Uniform deterministic binary… to The perturbation split

- [Uniform deterministic binary irreducible polynomials](lem-binary-uniform-irreducible.md)

Source and audit. This is the characteristic-two construction from Shoup (Sho90), using the squarefree factorization oracle and the two prime-power branches before coprime assembly. Exact guards for the constructor and its effective consumers exclude the former Shoup axiom and any replacement nonstandard axiom. The companion ledger's historical admission is unchanged.

- [Effective polynomial-basis field arithmetic](lem-effective-binary-field-arithmetic.md)

Scope. This is the addition and multiplication part of the effective-field node. Lemma [Effective inversion, Frobenius iteration and trace](lem-effective-field-inverse-trace.md) supplies element inversion and trace computation. Matrix algorithms, the normal-element construction and transport to a self-dual normal basis remain open. The supplied-modulus arithmetic and the uniform field constructor use only Lean's standard axioms.

- [Effective inversion, Frobenius iteration and trace](lem-effective-field-inverse-trace.md)

Scope. These are element operations. Effective matrix construction, Lemma [Effective normal element by fixed-space projections](lem-effective-normal-element.md) constructs the normal element, and Lemma [Effective self-dualization of a supplied normal basis](lem-effective-normal-selfdualization.md) supplies the effective self-dualizing basis change. They are composed in Lemma [Deterministic self-dual normal basis](../part-04/lem-self-dual-basis.md). Lemma [Effective Frobenius, trace Gram matrices and table transport](lem-effective-field-matrices.md) supplies the Frobenius matrix, inverse Gram computation and multiplication-table transport in any supplied basis. Lemma [Effective binary matrix arithmetic and elimination](lem-effective-binary-linear-algebra.md) supplies the binary matrix operations, elimination and solves.

- [Effective binary matrix arithmetic and elimination](lem-effective-binary-linear-algebra.md)

Reducing the graph of the original matrix map and retaining the certificate component gives a linear projection onto its kernel. Its images of the standard basis are the computed kernel generators; they number exactly the input dimension and may include zero or dependent vectors. Scope. The normal-element construction remains separate. These programs supply the kernels, solves and matrix inverse needed by that construction. The field-matrix applications are assembled in Lemma [Effective Frobenius, trace Gram matrices and table transport](lem-effective-field-matrices.md).

- [Effective Frobenius, trace Gram matrices and table transport](lem-effective-field-matrices.md)

Scope. These programs consume a supplied basis. The self-dualizing basis change is assembled in Lemma [Effective self-dualization of a supplied normal basis](lem-effective-normal-selfdualization.md); Lemma [Effective normal element by fixed-space projections](lem-effective-normal-element.md) constructs the initial normal element.

- [Effective normal element by fixed-space projections](lem-effective-normal-element.md)

Implementation. This performs the paper's fixed-space separation directly in the cyclic algebra. It constructs the CRT projections without printing polynomial factors or calling polynomial gcd; no standalone binary squarefree-factorization algorithm is claimed.

- [Effective self-dualization of a supplied normal basis](lem-effective-normal-selfdualization.md)

Scope. This constructs a self-dual normal basis from a supplied normal basis. Lemma [Effective normal element by fixed-space projections](lem-effective-normal-element.md) supplies that basis from unary $k$, and Lemma [Deterministic self-dual normal basis](../part-04/lem-self-dual-basis.md) composes the complete algorithm.

- [An admissible field with a bit representation](lem-admissible-field-exists.md)

Comments. This removes the field parameter of Theorem [The bespoke PCP for deciders](../../structure-of-the-proof/part-07/thm-pcp-decider.md) from the list of things this project assumes. It is deliberately weaker than Lemma [Deterministic self-dual normal basis](../part-04/lem-self-dual-basis.md): the basis is whatever Mathlib returns, so it is neither normal nor self-dual, there are no multiplication tables, and nothing is claimed about time. A consumer that needs $\kappa$ to be computed by the trace form (Lemma [Self-dual coordinates are trace pairings](../part-04/lem-downsize-field.md)) needs the self-dual normal basis, and `MIPRE.SAT.BinField` will have to carry more fields before it can be served; shaping that interface should wait until such a consumer exists.

## The Schwartz–Zippel lemma

[$\checkmark$ (mostly) in Mathlib]

- [Schwartz–Zippel](lem-schwartz-zippel.md)

Source. (Sch80, Zip79). A version is available in Mathlib (multivariate polynomials over finite fields).

Comments. Used throughout the low-degree machinery (distance of the Reed–Muller code, soundness of arithmetization). Three shapes are formalized, because three consumers want three different ones: the probability bound $d/q$ above; the individual-degree variant $m d / q$, derived from Mathlib's `schwartz_zippel_sum_degreeOf` rather than through the lossy $\text{total degree} \leq m d$; and the univariate case as a count rather than a probability — two distinct polynomials of degree at most $d$ agree at no more than $d$ points — which is the form Lemma [Transfer of synchronicity](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/03_background_results.tex#L996) uses. The probabilities are stated over $\mathbb{R}$, which is where the low-degree machinery's error terms live, rather than over Mathlib's $\mathbb{Q}_{\geq 0}$.

## Approximating the value from below ($\mathrm{MIP}^* \subseteq \mathrm{RE}$)

[$\bullet\bullet$ medium]

- [The value is approximable from below](lem-value-lower-approx.md)

Source. Folklore; see (JNVWY20, Section 12), and statement (S) in the proof of `cor:mip-re` of `recursive.tex` for a complete argument. The statement was previously given for ${\mathrm{val}^{s}}$ “and likewise for $\mathrm{val}^*$”; it is now the $\mathrm{val}^*$ statement, which is the one the pipeline consumes (Remark [Relation to the abstract compression lemma](../../structure-of-the-proof/README.md)) and the one the paper proves. The ${\mathrm{val}^{s}}$ analogue needs its own enumeration and density argument, since rounding the entries of a synchronous strategy preserves neither projectivity nor synchronicity; it is not needed and not planned. Thresholds are nonnegative rationals written as fractions $p/q$ of naturals, as in the paper's (S), where $t \in [0,1]$; a negative threshold is trivial since $\mathrm{val}^* \geq 0$. In Lean the game description is `HaltingGameValue.GameData` (Definition [Game description](../../foundations/part-02/def-game-description.md)), read as a game of the foundations by `GameData.game`, and recursive enumerability is Mathlib's `REPred`, the domain of a partial computable function; integers travel as pairs of naturals, because Mathlib's primitive recursion has no arithmetic on $\mathbb{Z}$. The form the compressibility criterion consumes (its hypothesis that the complement of $B$ is the halting set of a program, Lemma [Compressibility criterion](../../computability/lem-compressible-criterion.md)) is `MIPRE.exists_semidecider_lt_quantumValue`: for a computable family of game descriptions and a threshold $p/q$, a well-scoped program of the ambient model halting exactly on the strings whose game has value greater than $p/q$. It comes from the generic passage `MIPRE.Cost.exists_semidecider` from an `REPred` on bit strings to a program (Definition [Recursively enumerable](../../foundations/part-02/def-re.md)): a `ToPartrec` code for the predicate, translated into the model by `Prog.ofCode`, run after an ambient loop has shifted every bit up by one, since a `ToPartrec` code cannot see trailing zeros of its input and the bit $0$ encodes as `nil`.

Comments. The Lean route to the $\mathrm{val}^*$ half departs from the paper's proof of (S). The paper enumerates *approximate* candidates — tuples with entries in $\frac1k \mathbb{Z}[i]$ satisfying relaxed POVM constraints, tested by positive semidefiniteness (Lemma [Decidable candidate set: a norm constraint is two psd tests](lem-norm-two-psd.md)) — and repairs each into an exact POVM by conjugating with $T_x^{-1/2}$, with the explicit slack $\Delta(d,k) = 250(\left\vert {\mathcal{A}} \right\vert + \left\vert {\mathcal{B}} \right\vert)^2 d/k$ (its Claims “Stability” and “Density”; ledger nodes `1.1.7.2.3` and `1.1.7.2.4`). The formalization enumerates *exact* projective strategies instead: every projective measurement is $U \Pi_a U^*$ for a unitary $U$ and coordinate projections $\Pi_a$, and up to a phase every unitary is the Cayley transform of a skew-Hermitian matrix, which is what gets rounded (Lemma [Gaussian-rational projective measurements are dense](lem-rational-pvm-dense.md)). Every candidate is then a genuine strategy, so only the density half of the argument is needed, with no slack, no matrix square root and no positive-semidefiniteness test, and the biconditional of Lemma [Exact rational strategies suffice](lem-rational-strategies-suffice.md) is sharp. Lemma [Decidable candidate set: a norm constraint is two psd tests](lem-norm-two-psd.md) is proved but no longer on the path (the ledger's node `1.1.7.2.1`, exact arithmetic and the decidability of the candidate test, is accounted for by the primitive recursive check itself); Lemma [The perturbation split](lem-perturbation-split.md) is used as stated. The choice was made for the formalization's sake — the stability claim needs the functional calculus for $T_x^{-1/2}$ and the candidate test needs decidability of positive semidefiniteness over $\mathbb{Q}(i)$, both heavier in Lean than the Cayley parametrization — and it proves the same statement (S); it reverses the route decision recorded in Finding 3 of `planning/ledger-informed-plan.md`, which is annotated accordingly.

- [Gaussian-rational projective measurements are dense](lem-rational-pvm-dense.md)
- [Exact rational strategies suffice](lem-rational-strategies-suffice.md)

Comments. The lemma is the mathematical content of Lemma [The value is approximable from below](lem-value-lower-approx.md), isolated from the computability: only the right-hand side involves the enumeration. It accounts for the ledger's stability and density nodes (`1.1.7.2.3`, `1.1.7.2.4`) by a different proof, as explained under Lemma [The value is approximable from below](lem-value-lower-approx.md): stability is vacuous for exact candidates, and density is Lemma [Gaussian-rational projective measurements are dense](lem-rational-pvm-dense.md) plus the Lipschitz bound, whose constant $4\left\vert {\mathcal{A}} \right\vert\left\vert {\mathcal{B}} \right\vert$ is crude and immaterial. The nonemptiness of the answer alphabets is what makes a strategy exist at all: with it $\mathrm{val}^*$ is a supremum over a nonempty set, without it the supremum is $0$ by convention and the equivalence fails for $t < 0$. Game descriptions (Definition [Game description](../../foundations/part-02/def-game-description.md)) always satisfy it. In Lean the data type `ExactStrategy` carries no proofs, so that the computability layer can enumerate it and test validity.

- [Decidable candidate set: a norm constraint is two psd tests](lem-norm-two-psd.md)
- [The perturbation split](lem-perturbation-split.md)

Comments. This is the easy inclusion $\mathrm{MIP}^* \subseteq \mathrm{RE}$ and one half of Theorem [$\mathrm{MIP}^* = \mathrm{RE}$](../../the-main-theorem/thm-mipstar-eq-re.md). The pipeline consumes only the $\mathrm{val}^*$ half, as the semidecision procedure of Remark [Relation to the abstract compression lemma](../../structure-of-the-proof/README.md). The commuting-operator analogue (approximating ${\mathrm{val}^{\mathrm{co}}}$ from *above* via the NPA hierarchy (NPA08)) is *not* needed for the main theorem, but becomes relevant for the downstream consequences in Section [Downstream results](../../downstream-results/README.md).
