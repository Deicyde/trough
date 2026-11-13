---
declaration: theorem
origin: cited
lean: OpenQuantumProblem35.ame_2_exists, OpenQuantumProblem35.ame_3_exists, OpenQuantumProblem35.ame_2_2_exists, OpenQuantumProblem35.ame_3_2_exists, OpenQuantumProblem35.ame_5_2_exists, OpenQuantumProblem35.ame_6_2_exists, OpenQuantumProblem35.ame_4_2_not_exists, OpenQuantumProblem35.ame_7_2_not_exists, OpenQuantumProblem35.ame_7_exists_iff, OpenQuantumProblem35.ame_4_3_exists, OpenQuantumProblem35.ame_4_6_exists, OpenQuantumProblem35.ame_7_6_open, OpenQuantumProblem35.ame_7_10_open, OpenQuantumProblem35.ame_8_4_open, OpenQuantumProblem35.ame_8_6_open, OpenQuantumProblem35.ame_8_10_open, OpenQuantumProblem35.ame_9_6_open, OpenQuantumProblem35.ame_9_10_open, OpenQuantumProblem35.ame_10_6_open, OpenQuantumProblem35.ame_10_10_open, OpenQuantumProblem35.ame_11_3_open, OpenQuantumProblem35.ame_11_4_open, OpenQuantumProblem35.ame_11_5_open, OpenQuantumProblem35.ame_11_6_open, OpenQuantumProblem35.ame_11_10_open, OpenQuantumProblem35.ame_12_5_open, OpenQuantumProblem35.ame_12_6_open, OpenQuantumProblem35.ame_12_10_open, OpenQuantumProblem35.oqp_35
statement: formalized
---

# Open Quantum Problem 35: existence of absolutely maximally entangled pure states

> **Problem:** For which numbers of parties $n$ and local dimensions $d$ does there
> exist a pure absolutely maximally entangled state $\psi$?
>
> A pure state $\psi$ on $n$ parties of local dimension $d$ is called
> **absolutely maximally entangled (AME)** if, for every subset of at most half
> of the parties, the corresponding reduced density matrix is maximally mixed.
>
> *References:*
> - Open Quantum Problems, Problem 35:
>   <https://oqp.iqoqi.oeaw.ac.at/existence-of-absolutely-maximally-entangled-pure-states>
> - Formal Conjectures issue #3452:
>   <https://github.com/google-deepmind/formal-conjectures/issues/3452>
> - W. Helwig, W. Cui, A. Riera, J. I. Latorre, and H.-K. Lo,
>   *Absolute Maximal Entanglement and Quantum Secret Sharing*,
>   Phys. Rev. A 86, 052335 (2012), arXiv:1204.2289.
> - D. Goyeneche, D. Alsina, J. I. Latorre, A. Riera, and K. Życzkowski,
>   *Absolutely Maximally Entangled states, combinatorial designs and multi-unitary matrices*,
>   Phys. Rev. A 92, 032316 (2015), arXiv:1506.08857.
> - A. Higuchi and A. Sudbery,
>   *How entangled can two couples get?*,
>   Phys. Lett. A 273, 213-217 (2000), arXiv:quant-ph/0005013.
> - A. J. Scott,
>   *Multipartite entanglement, quantum-error-correcting codes, and entangling power of quantum
>   evolutions*, Phys. Rev. A 69, 052330 (2004), arXiv:quant-ph/0310137.
> - F. Huber, O. Gühne, and J. Siewert,
>   *Absolutely maximally entangled states of seven qubits do not exist*,
>   Phys. Rev. Lett. 118, 200502 (2017), arXiv:1608.06228.
> - F. Huber and M. Grassl,
>   *Quantum Codes of Maximal Distance and Highly Entangled Subspaces*,
>   Quantum 4, 284 (2020), arXiv:1907.07733.
> - S. A. Rather, A. Burchardt, W. Bruzda, G. Rajchel-Mieldzioć,
>   A. Lakshminarayan, and K. Życzkowski,
>   *Thirty-six entangled officers of Euler: Quantum solution to a classically impossible problem*,
>   Phys. Rev. Lett. 128, 080507 (2022), arXiv:2104.05122.
> - G. Rajchel-Mieldzioć, R. Bistroń, A. Rico, A. Lakshminarayan,
>   and K. Życzkowski,
>   *Absolutely maximally entangled pure states of multipartite quantum systems*,
>   arXiv:2508.04777 (2025).
> - S. Bevins and Y. Bidav,
>   *Symmetry-guided constructions of absolutely maximally entangled states in five open cases*,
>   [arXiv:2608.05781](https://arxiv.org/abs/2608.05781) (2026).
> - F. Shi, X. Zhang, Q. Zhao, and L. Li,
>   *Complete Existence Classification of Seven-Partite Absolutely Maximally Entangled States*,
>   [arXiv:2608.01011](https://arxiv.org/abs/2608.01011) (2026).
>
> This file formalizes the problem of determining for which pairs $(n,d)$ there exists an
> absolutely maximally entangled pure state $\mathrm{AME}(n,d)$.
>
> We represent an $n$-partite state of local dimension $d$ by the finite-dimensional Hilbert space
> `EuclideanSpace ℂ (Config n d)`, whose coordinates in the computational basis are amplitudes.
> The helper `mkStateVector` turns an amplitude function into such a state, and normalization is
> imposed explicitly via `IsNormalized`, i.e. via the ambient $L^2$ norm.
>
> The main reusable lemma is `reducedDensityFirst_of_completion`: if a state is a
> uniform superposition over the graph of an injective completion function
> `completion : Config m d → Config (n - m) d`,
> then the reduced state on the first $m$ parties is maximally mixed.
>
> As demonstration, we show that the Bell states with $n=2$ and GHZ states with $n=3$ are
> AME states, and the GHZ state with $n=4$ is not an AME state.

*Quoted from [FormalConjectures/OpenQuantumProblems/35.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OpenQuantumProblems/35.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 29 research or textbook statements: 10 open and 19 solved. It also has 6 test statements and 27 API statements, counted here but not shown.

## `OpenQuantumProblem35.ame_2_exists`

Proved here.

> The Bell state witnesses the existence of $\mathrm{AME}(2,d)$ for every local dimension $d \ge 2$.

```lean
theorem ame_2_exists {d : ℕ} (hd : 2 ≤ d) : ExistsAME 2 d
```

Category `research solved`; AMS [05 Combinatorics](../by-subject/part-01/05-combinatorics/README.md), [15 Linear and multilinear algebra; matrix theory](../by-subject/part-01/15-linear-and-multilinear-algebra-matrix-theory/README.md), [81 Quantum theory](../by-subject/part-03/81-quantum-theory/README.md), [94 Information and communication, circuits](../by-subject/part-03/94-information-and-communication-circuits/README.md). Declared in [FormalConjectures/OpenQuantumProblems/35.lean, line 646](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OpenQuantumProblems/35.lean#L646).

## `OpenQuantumProblem35.ame_3_exists`

Proved here.

> The $3$-party GHZ state witnesses the existence of $\mathrm{AME}(3,d)$ for every local dimension $d \ge 2$.

```lean
theorem ame_3_exists {d : ℕ} (hd : 2 ≤ d) : ExistsAME 3 d
```

Category `research solved`; AMS [05 Combinatorics](../by-subject/part-01/05-combinatorics/README.md), [15 Linear and multilinear algebra; matrix theory](../by-subject/part-01/15-linear-and-multilinear-algebra-matrix-theory/README.md), [81 Quantum theory](../by-subject/part-03/81-quantum-theory/README.md), [94 Information and communication, circuits](../by-subject/part-03/94-information-and-communication-circuits/README.md). Declared in [FormalConjectures/OpenQuantumProblems/35.lean, line 651](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OpenQuantumProblems/35.lean#L651).

## `OpenQuantumProblem35.ame_2_2_exists`

Proved here.

> Source-backed benchmark statement: the Bell state witnesses the existence of an $\mathrm{AME}(2,2)$ state.

```lean
theorem ame_2_2_exists : ExistsAME 2 2
```

Category `research solved`; AMS [05 Combinatorics](../by-subject/part-01/05-combinatorics/README.md), [15 Linear and multilinear algebra; matrix theory](../by-subject/part-01/15-linear-and-multilinear-algebra-matrix-theory/README.md), [81 Quantum theory](../by-subject/part-03/81-quantum-theory/README.md), [94 Information and communication, circuits](../by-subject/part-03/94-information-and-communication-circuits/README.md). Declared in [FormalConjectures/OpenQuantumProblems/35.lean, line 716](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OpenQuantumProblems/35.lean#L716).

## `OpenQuantumProblem35.ame_3_2_exists`

Proved here.

> Source-backed benchmark statement: the three-qubit GHZ state witnesses the existence of an $\mathrm{AME}(3,2)$ state.

```lean
theorem ame_3_2_exists : ExistsAME 3 2
```

Category `research solved`; AMS [05 Combinatorics](../by-subject/part-01/05-combinatorics/README.md), [15 Linear and multilinear algebra; matrix theory](../by-subject/part-01/15-linear-and-multilinear-algebra-matrix-theory/README.md), [81 Quantum theory](../by-subject/part-03/81-quantum-theory/README.md), [94 Information and communication, circuits](../by-subject/part-03/94-information-and-communication-circuits/README.md). Declared in [FormalConjectures/OpenQuantumProblems/35.lean, line 721](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OpenQuantumProblems/35.lean#L721).

## `OpenQuantumProblem35.ame_5_2_exists`

Solved: stated here; a Lean proof is at [https://github.com/zblore/fc-ame-5-2/blob/f0720e63065eb40c58a40f7b7af3d21f94d06453/AME52/FormalTarget.lean#L25-L26](https://github.com/zblore/fc-ame-5-2/blob/f0720e63065eb40c58a40f7b7af3d21f94d06453/AME52/FormalTarget.lean#L25-L26).

> Source-backed benchmark statement: an $\mathrm{AME}(5,2)$ state exists. This is one of the four qubit cases $n=2,3,5,6$; see the OQP page and Scott (2004).

```lean
theorem ame_5_2_exists : ExistsAME 5 2
```

Category `research solved`; AMS [05 Combinatorics](../by-subject/part-01/05-combinatorics/README.md), [15 Linear and multilinear algebra; matrix theory](../by-subject/part-01/15-linear-and-multilinear-algebra-matrix-theory/README.md), [81 Quantum theory](../by-subject/part-03/81-quantum-theory/README.md), [94 Information and communication, circuits](../by-subject/part-03/94-information-and-communication-circuits/README.md). Declared in [FormalConjectures/OpenQuantumProblems/35.lean, line 728](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OpenQuantumProblems/35.lean#L728).

## `OpenQuantumProblem35.ame_6_2_exists`

Solved: stated here; a Lean proof is at [https://github.com/zblore/fc-ame-6-2/blob/2a69b05aa65fec335b7e981deab2848865e9a688/AME62/FormalTarget.lean#L25-L26](https://github.com/zblore/fc-ame-6-2/blob/2a69b05aa65fec335b7e981deab2848865e9a688/AME62/FormalTarget.lean#L25-L26).

> Source-backed benchmark statement: an $\mathrm{AME}(6,2)$ state exists. This is one of the four qubit cases $n=2,3,5,6$; see the OQP page and Scott (2004).

```lean
theorem ame_6_2_exists : ExistsAME 6 2
```

Category `research solved`; AMS [05 Combinatorics](../by-subject/part-01/05-combinatorics/README.md), [15 Linear and multilinear algebra; matrix theory](../by-subject/part-01/15-linear-and-multilinear-algebra-matrix-theory/README.md), [81 Quantum theory](../by-subject/part-03/81-quantum-theory/README.md), [94 Information and communication, circuits](../by-subject/part-03/94-information-and-communication-circuits/README.md). Declared in [FormalConjectures/OpenQuantumProblems/35.lean, line 735](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OpenQuantumProblems/35.lean#L735).

## `OpenQuantumProblem35.ame_4_2_not_exists`

Solved: stated here; a Lean proof is at [https://github.com/zblore/fc-ame-4-2/blob/201550986844ea1e7fff36dc48681ca8b3c1600b/AME42/FormalTarget.lean#L26-L33](https://github.com/zblore/fc-ame-4-2/blob/201550986844ea1e7fff36dc48681ca8b3c1600b/AME42/FormalTarget.lean#L26-L33).

> Source-backed benchmark statement: no $\mathrm{AME}(4,2)$ state exists; see Higuchi--Sudbery (2000) and the OQP page.

```lean
theorem ame_4_2_not_exists : ¬ ExistsAME 4 2
```

Category `research solved`; AMS [05 Combinatorics](../by-subject/part-01/05-combinatorics/README.md), [15 Linear and multilinear algebra; matrix theory](../by-subject/part-01/15-linear-and-multilinear-algebra-matrix-theory/README.md), [81 Quantum theory](../by-subject/part-03/81-quantum-theory/README.md), [94 Information and communication, circuits](../by-subject/part-03/94-information-and-communication-circuits/README.md). Declared in [FormalConjectures/OpenQuantumProblems/35.lean, line 742](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OpenQuantumProblems/35.lean#L742).

## `OpenQuantumProblem35.ame_7_2_not_exists`

Solved: stated here; a Lean proof is at [https://palomar-registry.org/entry.html?id=PALOMAR-2026-11-02-000010](https://palomar-registry.org/entry.html?id=PALOMAR-2026-11-02-000010).

> Source-backed benchmark statement: no $\mathrm{AME}(7,2)$ state exists; see Huber--Gühne--Siewert (2017) and the OQP page.

```lean
theorem ame_7_2_not_exists : ¬ ExistsAME 7 2
```

Category `research solved`; AMS [05 Combinatorics](../by-subject/part-01/05-combinatorics/README.md), [15 Linear and multilinear algebra; matrix theory](../by-subject/part-01/15-linear-and-multilinear-algebra-matrix-theory/README.md), [81 Quantum theory](../by-subject/part-03/81-quantum-theory/README.md), [94 Information and communication, circuits](../by-subject/part-03/94-information-and-communication-circuits/README.md). Declared in [FormalConjectures/OpenQuantumProblems/35.lean, line 748](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OpenQuantumProblems/35.lean#L748).

## `OpenQuantumProblem35.ame_7_exists_iff`

Solved: stated here; a Lean proof is at [https://palomar-registry.org/entry.html?id=PALOMAR-2026-11-02-000010](https://palomar-registry.org/entry.html?id=PALOMAR-2026-11-02-000010).

> For a physical local dimension $d \ge 2$, a seven-party AME state exists exactly when
> $d \ge 3$. The hypothesis excludes the degenerate dimension $d = 1$, for which the unique
> computational-basis state is AME under the definitions of this file.
> Shi--Zhang--Zhao--Li (2026) construct cyclic quadratic-phase states in every odd dimension and
> a coupled binary--odd-dimensional state in every dimension congruent to `2` modulo `4`; together
> with power-of-two constructions and the product property, this covers every `d ≥ 3`.

```lean
theorem ame_7_exists_iff (d : ℕ) (hd : 2 ≤ d) : ExistsAME 7 d ↔ 3 ≤ d
```

Category `research solved`; AMS [05 Combinatorics](../by-subject/part-01/05-combinatorics/README.md), [15 Linear and multilinear algebra; matrix theory](../by-subject/part-01/15-linear-and-multilinear-algebra-matrix-theory/README.md), [81 Quantum theory](../by-subject/part-03/81-quantum-theory/README.md), [94 Information and communication, circuits](../by-subject/part-03/94-information-and-communication-circuits/README.md). Declared in [FormalConjectures/OpenQuantumProblems/35.lean, line 759](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OpenQuantumProblems/35.lean#L759).

## `OpenQuantumProblem35.ame_4_3_exists`

Solved: stated here; a Lean proof is at [https://github.com/AllenGrahamHart/FormalConjectures-Bench/blob/8fb9479e9cbfde68d6990ed008b24c883cbd2750/formalizations/openquantum35_ame43/OpenQuantum35AME43Formalization.lean#L333](https://github.com/AllenGrahamHart/FormalConjectures-Bench/blob/8fb9479e9cbfde68d6990ed008b24c883cbd2750/formalizations/openquantum35_ame43/OpenQuantum35AME43Formalization.lean#L333).

> Source-backed benchmark statement: an $\mathrm{AME}(4,3)$ state exists; see Helwig et al. (2012) and Goyeneche et al. (2015).

```lean
theorem ame_4_3_exists : ExistsAME 4 3
```

Category `research solved`; AMS [05 Combinatorics](../by-subject/part-01/05-combinatorics/README.md), [15 Linear and multilinear algebra; matrix theory](../by-subject/part-01/15-linear-and-multilinear-algebra-matrix-theory/README.md), [81 Quantum theory](../by-subject/part-03/81-quantum-theory/README.md), [94 Information and communication, circuits](../by-subject/part-03/94-information-and-communication-circuits/README.md). Declared in [FormalConjectures/OpenQuantumProblems/35.lean, line 766](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OpenQuantumProblems/35.lean#L766).

## `OpenQuantumProblem35.ame_4_6_exists`

Solved: stated here; a Lean proof is at [https://github.com/zblore/fc-ame-4-6/blob/d42273127096f5cbdc2c05f6d727f2dc75d5ea81/AME46/FormalTarget.lean#L23-L24](https://github.com/zblore/fc-ame-4-6/blob/d42273127096f5cbdc2c05f6d727f2dc75d5ea81/AME46/FormalTarget.lean#L23-L24).

> Source-backed benchmark statement: an $\mathrm{AME}(4,6)$ state exists; see Rather et al. (2022).

```lean
theorem ame_4_6_exists : ExistsAME 4 6
```

Category `research solved`; AMS [05 Combinatorics](../by-subject/part-01/05-combinatorics/README.md), [15 Linear and multilinear algebra; matrix theory](../by-subject/part-01/15-linear-and-multilinear-algebra-matrix-theory/README.md), [81 Quantum theory](../by-subject/part-03/81-quantum-theory/README.md), [94 Information and communication, circuits](../by-subject/part-03/94-information-and-communication-circuits/README.md). Declared in [FormalConjectures/OpenQuantumProblems/35.lean, line 773](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OpenQuantumProblems/35.lean#L773).

## `OpenQuantumProblem35.ame_7_6_open`

Proved here.

> An $\mathrm{AME}(7,6)$ state exists, by the complete seven-party classification of
> Shi--Zhang--Zhao--Li (2026).

```lean
theorem ame_7_6_open :
    ExistsAME 7 6
```

Category `research solved`; AMS [05 Combinatorics](../by-subject/part-01/05-combinatorics/README.md), [15 Linear and multilinear algebra; matrix theory](../by-subject/part-01/15-linear-and-multilinear-algebra-matrix-theory/README.md), [81 Quantum theory](../by-subject/part-03/81-quantum-theory/README.md), [94 Information and communication, circuits](../by-subject/part-03/94-information-and-communication-circuits/README.md). Declared in [FormalConjectures/OpenQuantumProblems/35.lean, line 781](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OpenQuantumProblems/35.lean#L781).

## `OpenQuantumProblem35.ame_7_10_open`

Proved here.

> An $\mathrm{AME}(7,10)$ state exists, by the complete seven-party classification of
> Shi--Zhang--Zhao--Li (2026).

```lean
theorem ame_7_10_open :
    ExistsAME 7 10
```

Category `research solved`; AMS [05 Combinatorics](../by-subject/part-01/05-combinatorics/README.md), [15 Linear and multilinear algebra; matrix theory](../by-subject/part-01/15-linear-and-multilinear-algebra-matrix-theory/README.md), [81 Quantum theory](../by-subject/part-03/81-quantum-theory/README.md), [94 Information and communication, circuits](../by-subject/part-03/94-information-and-communication-circuits/README.md). Declared in [FormalConjectures/OpenQuantumProblems/35.lean, line 788](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OpenQuantumProblems/35.lean#L788).

## `OpenQuantumProblem35.ame_8_4_open`

Open: stated without proof.

> Open benchmark statement: does an $\mathrm{AME}(8,4)$ state exist?

```lean
theorem ame_8_4_open :
    ExistsAME 8 4
```

Category `research open`; AMS [05 Combinatorics](../by-subject/part-01/05-combinatorics/README.md), [15 Linear and multilinear algebra; matrix theory](../by-subject/part-01/15-linear-and-multilinear-algebra-matrix-theory/README.md), [81 Quantum theory](../by-subject/part-03/81-quantum-theory/README.md), [94 Information and communication, circuits](../by-subject/part-03/94-information-and-communication-circuits/README.md). Declared in [FormalConjectures/OpenQuantumProblems/35.lean, line 794](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OpenQuantumProblems/35.lean#L794).

## `OpenQuantumProblem35.ame_8_6_open`

Open: stated without proof.

> Open benchmark statement: does an $\mathrm{AME}(8,6)$ state exist?

```lean
theorem ame_8_6_open :
    ExistsAME 8 6
```

Category `research open`; AMS [05 Combinatorics](../by-subject/part-01/05-combinatorics/README.md), [15 Linear and multilinear algebra; matrix theory](../by-subject/part-01/15-linear-and-multilinear-algebra-matrix-theory/README.md), [81 Quantum theory](../by-subject/part-03/81-quantum-theory/README.md), [94 Information and communication, circuits](../by-subject/part-03/94-information-and-communication-circuits/README.md). Declared in [FormalConjectures/OpenQuantumProblems/35.lean, line 800](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OpenQuantumProblems/35.lean#L800).

## `OpenQuantumProblem35.ame_8_10_open`

Open: stated without proof.

> Open benchmark statement: does an $\mathrm{AME}(8,10)$ state exist?

```lean
theorem ame_8_10_open :
    ExistsAME 8 10
```

Category `research open`; AMS [05 Combinatorics](../by-subject/part-01/05-combinatorics/README.md), [15 Linear and multilinear algebra; matrix theory](../by-subject/part-01/15-linear-and-multilinear-algebra-matrix-theory/README.md), [81 Quantum theory](../by-subject/part-03/81-quantum-theory/README.md), [94 Information and communication, circuits](../by-subject/part-03/94-information-and-communication-circuits/README.md). Declared in [FormalConjectures/OpenQuantumProblems/35.lean, line 806](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OpenQuantumProblems/35.lean#L806).

## `OpenQuantumProblem35.ame_9_6_open`

Solved: stated here; a Lean proof is at [https://github.com/KitaKen1/ame-9-6-lean/blob/500ee827dffbeed9bb2ed502adcd6690943a7463/lean/AME96/FormalTarget.lean#L13](https://github.com/KitaKen1/ame-9-6-lean/blob/500ee827dffbeed9bb2ed502adcd6690943a7463/lean/AME96/FormalTarget.lean#L13).

> Open benchmark statement: does an $\mathrm{AME}(9,6)$ state exist?
>
> Answer: Yes. A witness found by Kenta Kitamura (KitaKen1 on GitHub)
> is given here:
> https://github.com/KitaKen1/ame-9-6-lean

```lean
theorem ame_9_6_open :
    ExistsAME 9 6
```

Category `research solved`; AMS [05 Combinatorics](../by-subject/part-01/05-combinatorics/README.md), [15 Linear and multilinear algebra; matrix theory](../by-subject/part-01/15-linear-and-multilinear-algebra-matrix-theory/README.md), [81 Quantum theory](../by-subject/part-03/81-quantum-theory/README.md), [94 Information and communication, circuits](../by-subject/part-03/94-information-and-communication-circuits/README.md). Declared in [FormalConjectures/OpenQuantumProblems/35.lean, line 819](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OpenQuantumProblems/35.lean#L819).

## `OpenQuantumProblem35.ame_9_10_open`

Solved: stated here; a Lean proof is at [https://github.com/niketp03/atlas-fc-verified/blob/15e4b3a7584e218cec531aeaf71cce72a8a9ecb1/AtlasFCSolutions/Oqp35.lean#L1238](https://github.com/niketp03/atlas-fc-verified/blob/15e4b3a7584e218cec531aeaf71cce72a8a9ecb1/AtlasFCSolutions/Oqp35.lean#L1238).

> Open benchmark statement: does an $\mathrm{AME}(9,10)$ state exist?
>
> Solved: a Lean 4 proof, derived from the Atlas proofs in
> [facebookresearch/atlas-lean](https://github.com/facebookresearch/atlas-lean), is linked in
> `formal_proof`.

```lean
theorem ame_9_10_open :
    ExistsAME 9 10
```

Category `research solved`; AMS [05 Combinatorics](../by-subject/part-01/05-combinatorics/README.md), [15 Linear and multilinear algebra; matrix theory](../by-subject/part-01/15-linear-and-multilinear-algebra-matrix-theory/README.md), [81 Quantum theory](../by-subject/part-03/81-quantum-theory/README.md), [94 Information and communication, circuits](../by-subject/part-03/94-information-and-communication-circuits/README.md). Declared in [FormalConjectures/OpenQuantumProblems/35.lean, line 834](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OpenQuantumProblems/35.lean#L834).

## `OpenQuantumProblem35.ame_10_6_open`

Open: stated without proof.

> Open benchmark statement: does an $\mathrm{AME}(10,6)$ state exist?

```lean
theorem ame_10_6_open :
    ExistsAME 10 6
```

Category `research open`; AMS [05 Combinatorics](../by-subject/part-01/05-combinatorics/README.md), [15 Linear and multilinear algebra; matrix theory](../by-subject/part-01/15-linear-and-multilinear-algebra-matrix-theory/README.md), [81 Quantum theory](../by-subject/part-03/81-quantum-theory/README.md), [94 Information and communication, circuits](../by-subject/part-03/94-information-and-communication-circuits/README.md). Declared in [FormalConjectures/OpenQuantumProblems/35.lean, line 840](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OpenQuantumProblems/35.lean#L840).

## `OpenQuantumProblem35.ame_10_10_open`

Open: stated without proof.

> Open benchmark statement: does an $\mathrm{AME}(10,10)$ state exist?

```lean
theorem ame_10_10_open :
    ExistsAME 10 10
```

Category `research open`; AMS [05 Combinatorics](../by-subject/part-01/05-combinatorics/README.md), [15 Linear and multilinear algebra; matrix theory](../by-subject/part-01/15-linear-and-multilinear-algebra-matrix-theory/README.md), [81 Quantum theory](../by-subject/part-03/81-quantum-theory/README.md), [94 Information and communication, circuits](../by-subject/part-03/94-information-and-communication-circuits/README.md). Declared in [FormalConjectures/OpenQuantumProblems/35.lean, line 846](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OpenQuantumProblems/35.lean#L846).

## `OpenQuantumProblem35.ame_11_3_open`

Open: stated without proof.

> Open benchmark statement: does an $\mathrm{AME}(11,3)$ state exist?

```lean
theorem ame_11_3_open :
    ExistsAME 11 3
```

Category `research open`; AMS [05 Combinatorics](../by-subject/part-01/05-combinatorics/README.md), [15 Linear and multilinear algebra; matrix theory](../by-subject/part-01/15-linear-and-multilinear-algebra-matrix-theory/README.md), [81 Quantum theory](../by-subject/part-03/81-quantum-theory/README.md), [94 Information and communication, circuits](../by-subject/part-03/94-information-and-communication-circuits/README.md). Declared in [FormalConjectures/OpenQuantumProblems/35.lean, line 852](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OpenQuantumProblems/35.lean#L852).

## `OpenQuantumProblem35.ame_11_4_open`

Solved: stated here; a Lean proof is at [https://github.com/mo271/formal-conjectures/blob/91bed229b434b68d66f5fd35cdcfee19a79985e8/FormalConjectures/OpenQuantumProblems/35.lean#L1861](https://github.com/mo271/formal-conjectures/blob/91bed229b434b68d66f5fd35cdcfee19a79985e8/FormalConjectures/OpenQuantumProblems/35.lean#L1861).

> Open benchmark statement: does an $\mathrm{AME}(11,4)$ state exist?
>
> Answer: `AME(11, 4)` exists. The graph state defined by the circulant matrix Gamma
>     over $GF(4)$ with first row $(0, 0, 0, 1, ω, ω, ω, ω, 1, 0, 0)$ is an
>     absolutely maximally entangled state of $11$ ququarts.
>    This result has been found by Moritz Firsching and Goran Žužić using an
> experimental pipeline
>
>
>  Before, it was already known that there is a quantum code for `[11,0]]_5`, which corresponds to an `AME(11,4)` state (which is another approach to a solution).

```lean
theorem ame_11_4_open :
    ExistsAME 11 4
```

Category `research solved`; AMS [05 Combinatorics](../by-subject/part-01/05-combinatorics/README.md), [15 Linear and multilinear algebra; matrix theory](../by-subject/part-01/15-linear-and-multilinear-algebra-matrix-theory/README.md), [81 Quantum theory](../by-subject/part-03/81-quantum-theory/README.md), [94 Information and communication, circuits](../by-subject/part-03/94-information-and-communication-circuits/README.md). Declared in [FormalConjectures/OpenQuantumProblems/35.lean, line 870](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OpenQuantumProblems/35.lean#L870).

## `OpenQuantumProblem35.ame_11_5_open`

Solved: stated here; a Lean proof is at [https://github.com/google-deepmind/formal-conjectures/blob/47383bf7fbe86effc9ac184446e320f26ddbee3a/FormalConjectures/OpenQuantumProblems/35.lean#L2138](https://github.com/google-deepmind/formal-conjectures/blob/47383bf7fbe86effc9ac184446e320f26ddbee3a/FormalConjectures/OpenQuantumProblems/35.lean#L2138).

> Open benchmark statement: does an $\mathrm{AME}(11,5)$ state exist?
>
> The DeepMind prover agent has shown that such a state exists.

```lean
theorem ame_11_5_open :
    ExistsAME 11 5
```

Category `research solved`; AMS [05 Combinatorics](../by-subject/part-01/05-combinatorics/README.md), [15 Linear and multilinear algebra; matrix theory](../by-subject/part-01/15-linear-and-multilinear-algebra-matrix-theory/README.md), [81 Quantum theory](../by-subject/part-03/81-quantum-theory/README.md), [94 Information and communication, circuits](../by-subject/part-03/94-information-and-communication-circuits/README.md). Declared in [FormalConjectures/OpenQuantumProblems/35.lean, line 881](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OpenQuantumProblems/35.lean#L881).

## `OpenQuantumProblem35.ame_11_6_open`

Open: stated without proof.

> Open benchmark statement: does an $\mathrm{AME}(11,6)$ state exist?

```lean
theorem ame_11_6_open :
    ExistsAME 11 6
```

Category `research open`; AMS [05 Combinatorics](../by-subject/part-01/05-combinatorics/README.md), [15 Linear and multilinear algebra; matrix theory](../by-subject/part-01/15-linear-and-multilinear-algebra-matrix-theory/README.md), [81 Quantum theory](../by-subject/part-03/81-quantum-theory/README.md), [94 Information and communication, circuits](../by-subject/part-03/94-information-and-communication-circuits/README.md). Declared in [FormalConjectures/OpenQuantumProblems/35.lean, line 887](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OpenQuantumProblems/35.lean#L887).

## `OpenQuantumProblem35.ame_11_10_open`

Solved: stated here; a Lean proof is at [https://github.com/KitaKen1/ame-11-10-lean/blob/6b7d009a43970587a3386b690221bec4339ce271/lean/AME11_10FC.lean#L15-L21](https://github.com/KitaKen1/ame-11-10-lean/blob/6b7d009a43970587a3386b690221bec4339ce271/lean/AME11_10FC.lean#L15-L21).

> Open benchmark statement: does an $\mathrm{AME}(11,10)$ state exist?
>
> Answer: Yes. A witness found by Kenta Kitamura (KitaKen1 on GitHub)
> is given here:
> https://github.com/KitaKen1/ame-11-10-lean

```lean
theorem ame_11_10_open :
    ExistsAME 11 10
```

Category `research solved`; AMS [05 Combinatorics](../by-subject/part-01/05-combinatorics/README.md), [15 Linear and multilinear algebra; matrix theory](../by-subject/part-01/15-linear-and-multilinear-algebra-matrix-theory/README.md), [81 Quantum theory](../by-subject/part-03/81-quantum-theory/README.md), [94 Information and communication, circuits](../by-subject/part-03/94-information-and-communication-circuits/README.md). Declared in [FormalConjectures/OpenQuantumProblems/35.lean, line 901](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OpenQuantumProblems/35.lean#L901).

## `OpenQuantumProblem35.ame_12_5_open`

Solved: stated here without proof.

> Does an $\mathrm{AME}(12,5)$ state exist?
>
> The answer is yes. Bevins and Bidav construct an explicit Hermitian self-dual MDS code with
> parameters $[12,6,7]_{25}$, whose associated nonbinary stabilizer state is an
> $\mathrm{AME}(12,5)$ state.

```lean
theorem ame_12_5_open :
    ExistsAME 12 5
```

Category `research solved`; AMS [05 Combinatorics](../by-subject/part-01/05-combinatorics/README.md), [15 Linear and multilinear algebra; matrix theory](../by-subject/part-01/15-linear-and-multilinear-algebra-matrix-theory/README.md), [81 Quantum theory](../by-subject/part-03/81-quantum-theory/README.md), [94 Information and communication, circuits](../by-subject/part-03/94-information-and-communication-circuits/README.md). Declared in [FormalConjectures/OpenQuantumProblems/35.lean, line 911](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OpenQuantumProblems/35.lean#L911).

## `OpenQuantumProblem35.ame_12_6_open`

Open: stated without proof.

> Open benchmark statement: does an $\mathrm{AME}(12,6)$ state exist?

```lean
theorem ame_12_6_open :
    ExistsAME 12 6
```

Category `research open`; AMS [05 Combinatorics](../by-subject/part-01/05-combinatorics/README.md), [15 Linear and multilinear algebra; matrix theory](../by-subject/part-01/15-linear-and-multilinear-algebra-matrix-theory/README.md), [81 Quantum theory](../by-subject/part-03/81-quantum-theory/README.md), [94 Information and communication, circuits](../by-subject/part-03/94-information-and-communication-circuits/README.md). Declared in [FormalConjectures/OpenQuantumProblems/35.lean, line 917](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OpenQuantumProblems/35.lean#L917).

## `OpenQuantumProblem35.ame_12_10_open`

Open: stated without proof.

> Open benchmark statement: does an $\mathrm{AME}(12,10)$ state exist?

```lean
theorem ame_12_10_open :
    ExistsAME 12 10
```

Category `research open`; AMS [05 Combinatorics](../by-subject/part-01/05-combinatorics/README.md), [15 Linear and multilinear algebra; matrix theory](../by-subject/part-01/15-linear-and-multilinear-algebra-matrix-theory/README.md), [81 Quantum theory](../by-subject/part-03/81-quantum-theory/README.md), [94 Information and communication, circuits](../by-subject/part-03/94-information-and-communication-circuits/README.md). Declared in [FormalConjectures/OpenQuantumProblems/35.lean, line 923](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OpenQuantumProblems/35.lean#L923).

## `OpenQuantumProblem35.oqp_35`

Open: stated without proof.

> Open Quantum Problem 35: classify all pairs $(n,d)$ with $n \ge 2$ and $d \ge 2$ for which an $\mathrm{AME}(n,d)$ state exists.

```lean
theorem oqp_35 :
    {nd : ℕ × ℕ | 2 ≤ nd.1 ∧ 2 ≤ nd.2 ∧ ExistsAME nd.1 nd.2} = oqp_35.answer
```

Category `research open`; AMS [05 Combinatorics](../by-subject/part-01/05-combinatorics/README.md), [15 Linear and multilinear algebra; matrix theory](../by-subject/part-01/15-linear-and-multilinear-algebra-matrix-theory/README.md), [81 Quantum theory](../by-subject/part-03/81-quantum-theory/README.md), [94 Information and communication, circuits](../by-subject/part-03/94-information-and-communication-circuits/README.md). Declared in [FormalConjectures/OpenQuantumProblems/35.lean, line 933](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OpenQuantumProblems/35.lean#L933).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OpenQuantumProblems/35.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OpenQuantumProblems/35.lean)
- [https://oqp.iqoqi.oeaw.ac.at/existence-of-absolutely-maximally-entangled-pure-states](https://oqp.iqoqi.oeaw.ac.at/existence-of-absolutely-maximally-entangled-pure-states)
