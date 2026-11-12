---
declaration: section
origin: cited
lean: OAI.KaplanskyCounterexample.finitelyPresented_counterexample, OAI.KaplanskyCounterexample.main_theorem, OAI.GroupRingDeterminant.main, OAI.OddKaplansky.main_theorem
statement: formalized
proof: formalized
---

# 197. A torsion-free group algebra that is not directly finite

4 manuscripts and 4 Lean statements, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

Constructs a finitely presented torsion-free nonsofic group whose group algebra over 𝔽$_{2}$ is not directly finite, disproving Kaplansky's conjecture even without torsion. Companion examples give injective nonsurjective cellular automata on all configurations, refuting Gottschalk's surjunctivity conjecture. Another counterexample is an integral group-ring matrix, invertible over the rational group ring, with Fuglede–Kadison determinant strictly between zero and one, disproving the unrestricted Determinant Conjecture.

## A Torsion-Free Group Algebra That Is Not Directly Finite

We construct a finitely presented torsion-free counterexample to Kaplansky's direct finiteness conjecture over the field of two elements. The group admits a finite two-dimensional classifying complex.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/A-Torsion-Free-Group-Algebra-That-Is-Not-Directly-Finite-October-4-2026/direct-finiteness.pdf).

## A Counterexample to Kaplansky's Direct-Finiteness Conjecture in Characteristic Two

We disprove Kaplansky's direct-finiteness conjecture by constructing a finite field *K* of characteristic two, a finitely presented group *G*, and finite sums $a,b\in K[G]$ with $ab=1$ but $ba\ne1$. The group *G* is nonsofic. The same elements define a cellular automaton on $K^{G}$ that is injective but not surjective, disproving Gottschalk's surjunctivity conjecture.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/A-Counterexample-to-Kaplanskys-Direct-Finiteness-Conjecture-in-Characteristic-Two-September-23-2026/paper.pdf); the Lean below formalizes results from it.

## A Counterexample to the Group-Ring Determinant Conjecture

We disprove the unrestricted group-ring Determinant Conjecture. We construct a finitely generated group *G* and a square matrix over $\mathbb Z[G]$ that is invertible over $\mathbb Q[G]$ and has Fuglede–Kadison determinant strictly between zero and one. The logarithmic integral defining the determinant is finite.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/A-Counterexample-to-the-Group-Ring-Determinant-Conjecture-September-23-2026/paper.pdf); the Lean below formalizes results from it.

## A Counterexample to Kaplansky's Direct-Finiteness Conjecture in Odd Characteristic

We construct a counterexample to Kaplansky's direct-finiteness conjecture in odd characteristic. For one specified odd prime *p*, we obtain a field *K* of order $p^{4}$, a finitely generated group *G* containing torsion, and finite sums $a,b\in K[G]$ with $ab=1$ but $ba\ne1$. The same elements define a cellular automaton on $K^{G}$ that is injective but not surjective.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/A-Counterexample-to-Kaplanskys-Direct-Finiteness-Conjecture-in-Odd-Characteristic-September-26-2026/paper.pdf); the Lean below formalizes results from it.

## The Lean formalization

Kaplansky's direct-finiteness conjecture asserts that $ab=1$ implies $ba=1$ for $a,b\in K[G]$, for every field $K$ and group $G$. The formalized results construct a finite field of characteristic two and a group algebra violating this implication. One statement records the counterexample for a finitely generated group; the more detailed construction gives a finitely presented group with an element of odd prime order.

The detailed construction also gives a precise recipe for choosing the data and proves that the required search terminates. The further conclusion that the group is nonsofic is outside these statements.

A nonsingular integer matrix has absolute determinant at least $1$. The group-ring Determinant Conjecture extends this bound to matrices over $\mathbb Z[G]$ for every discrete group $G$. If $T_A$ is the operator induced by such a matrix $A$ on finite direct sums of $\ell^2(G)$, and $\mu_A$ is the spectral measure of $T_A^*T_A$ with respect to the group trace, the conjecture asserts

$\displaystyle \int_{(0,\infty)}\log t\,d\mu_A(t)\ge0,$

with the zero spectral atom omitted. For an invertible square matrix, this is equivalent to its Fuglede–Kadison determinant being at least $1$.

The formalized result contradicts that bound. It gives a finitely generated group $G$ and an $n\times n$ matrix over $\mathbb Z[G]$, with $n\ge1$, that is invertible over $\mathbb Q[G]$. Its bounded left-regular operator is invertible and has determinant strictly between $0$ and $1$.

The formalization uses the trace of $\log(T^*T)$ to define the determinant for the invertible operator $T$. The paper's additional spectral-measure integral conclusion is not included.

Kaplansky's direct-finiteness conjecture asserts that $ab=1$ implies $ba=1$ in every group algebra over a field. Let $p$ be the smallest prime divisor of $\bigl(\binom{1200}{600}!\bigr)^2+1$; this prime is odd. The formalized result constructs a field $K$ of order $p^4$, a finitely generated group $G$ with torsion, and elements $a,b$ violating this implication. The associated cellular automaton on all configurations $K^G$ is injective but not surjective.

The formalization also contains fixed-field transfer results, separate from the statement linked below.

## Lean: Finitely presented characteristic-two counterexample

Stated in [KaplanskyFinitelyPresented.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/KaplanskyFinitelyPresented.lean); one of the main results in the repository's formalization.yaml.

```lean
theorem finitelyPresented_counterexample :
    ∃ (K : Type) (_ : Field K) (_ : Fintype K) (_ : CharP K 2),
      ∃ (G : Type) (_ : Group G) (_ : Group.IsFinitelyPresented G),
        (∃ (ℓ : ℕ) (_ : ℓ.Prime) (_ : Odd ℓ) (g : G), orderOf g = ℓ) ∧
        ∃ a_out b_out : MonoidAlgebra K G, a_out * b_out = 1 ∧ b_out * a_out ≠ 1
```

Proved in [lean/OAI/RingTheory/DirectFiniteness/FinitelyPresented.lean, line 35](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/RingTheory/DirectFiniteness/FinitelyPresented.lean#L35).

## Lean: Characteristic-two direct-finiteness counterexample

Stated in [KaplanskyDirectFiniteness.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/KaplanskyDirectFiniteness.lean).

```lean
theorem main_theorem : MainClaim
```

Proved in [lean/OAI/RingTheory/DirectFiniteness/Main.lean, line 9](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/RingTheory/DirectFiniteness/Main.lean#L9).

## Lean: Group-ring determinant counterexample

Stated in [GroupRingDeterminant.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/GroupRingDeterminant.lean); one of the main results in the repository's formalization.yaml.

```lean
theorem main : MainStatement
```

Proved in [lean/OAI/Analysis/GroupDeterminants/Main.lean, line 13](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Analysis/GroupDeterminants/Main.lean#L13).

## Lean: Prescribed odd-characteristic counterexample

Stated in [OddKaplansky.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/OddKaplansky.lean); one of the main results in the repository's formalization.yaml.

```lean
theorem main_theorem : MainClaim
```

Proved in [lean/OAI/Algebra/OddKaplansky/Main.lean, line 81](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Algebra/OddKaplansky/Main.lean#L81).

## Depends on

No dependencies are recorded: the collection records none between its families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/197.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/197.md)
