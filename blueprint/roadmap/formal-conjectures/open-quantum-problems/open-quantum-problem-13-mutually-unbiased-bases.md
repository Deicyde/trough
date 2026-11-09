---
declaration: theorem
origin: cited
lean: OpenQuantumProblem13.mutuallyUnbiasedBases_dim2, OpenQuantumProblem13.mutuallyUnbiasedBases_dim6_bounds, OpenQuantumProblem13.mutuallyUnbiasedBases_dim6_bounds.variants.upper_five, OpenQuantumProblem13.mutuallyUnbiasedBases_dim6, OpenQuantumProblem13.mutuallyUnbiasedBases_dim10, OpenQuantumProblem13.mutuallyUnbiasedBases_dim12, OpenQuantumProblem13.mutuallyUnbiasedBases_dim14, OpenQuantumProblem13.mutuallyUnbiasedBases_dim15, OpenQuantumProblem13.mutuallyUnbiasedBases
statement: formalized
---

# Open Quantum Problem 13: Mutually unbiased bases

> ## Mathematical problem
>
> For each integer $d \ge 2$, determine the maximum number $k$ for which there exist
> orthonormal bases $\mathcal{B}_1, \dots, \mathcal{B}_k$ of the complex Hilbert space
> $\mathbb{C}^d$ such that any two distinct bases are mutually unbiased.
>
> Concretely, if
> $\mathcal{B}_r = \{ e_0^{(r)}, \dots, e_{d-1}^{(r)} \}$
> and
> $\mathcal{B}_s = \{ e_0^{(s)}, \dots, e_{d-1}^{(s)} \}$,
> then $\mathcal{B}_r$ and $\mathcal{B}_s$ are mutually unbiased if for all $i, j$
> and all $r \ne s$,
> $|\langle e_i^{(r)}, e_j^{(s)} \rangle| = d^{-1/2}$.
>
> The problem is therefore to determine the maximal value
> $\mu(d) := \max \{ k : \text{there exist } k \text{ pairwise mutually unbiased
> orthonormal bases in } \mathbb{C}^d \}$.
>
> In this file, an orthonormal basis is represented by a unitary matrix whose columns are the
> basis vectors. For two such bases `U` and `V`, the matrix `relativeUnitary U V`, which is
> $U^\dagger V$, contains all cross-basis overlaps as its entries. Since Lean works more
> smoothly with squared norms, we formalize mutual unbiasedness by requiring
> $\| (relativeUnitary\ U\ V)_{ij} \|^2 = 1 / d$
> for all $i, j$, which is equivalent to
> $|\langle e_i^{(r)}, e_j^{(s)} \rangle| = d^{-1/2}$.
>
> ## Background
>
> Mutually unbiased bases are a basic structure in finite-dimensional quantum theory.
> They arise in quantum state determination, quantum tomography, quantum cryptography,
> finite geometry, and combinatorics.
>
> A general upper bound is $\mu(d) \le d + 1$.
> Equality is known when $d$ is a prime power, via constructions over finite fields.
> For composite dimensions that are not prime powers, the exact value of $\mu(d)$ is in
> general open.
>
> The smallest and most famous unresolved case is $d = 6$.
> The IQOQI OQP page emphasizes this dimension in particular: although many equivalent
> reformulations are known, no construction yielding more than three mutually unbiased bases
> in dimension six is known.
>
> ## What this file formalizes
>
> This file is organized around the quantity `IsMaxMUBCount d k`, which expresses that
> $k$ is the maximum number of mutually unbiased orthonormal bases in dimension $d$.
>
> - the open theorem `mutuallyUnbiasedBases` expresses the full problem for all $d \ge 2$;
> - the open theorem `mutuallyUnbiasedBases_dim6` expresses the especially important case
>   $d = 6$;
> - the solved theorem `mutuallyUnbiasedBases_dim2` proves the qubit case $\mu(2) = 3$;
> - the solved theorems `mutuallyUnbiasedBases_dim6_bounds` and
>   `mutuallyUnbiasedBases_dim6_bounds.variants.upper_five` record the bounds
>   $3 \le \mu(6) \le 7$ and $\mu(6) \le 5$.
>
> ## References
>
> *Primary source list entry:*
> - IQOQI Vienna Open Quantum Problems, problem 13:
>   https://oqp.iqoqi.oeaw.ac.at/mutually-unbiased-bases
> - Master list of open quantum problems:
>   https://oqp.iqoqi.oeaw.ac.at/open-quantum-problems
>
> ### Foundational papers
> - I. D. Ivanović,
>   *Geometrical description of quantal state determination*,
>   J. Phys. A 14, 3241-3245 (1981).
> - W. K. Wootters and B. D. Fields,
>   *Optimal state-determination by mutually unbiased measurements*,
>   Ann. Phys. 191, 363-381 (1989).
>
> ### General constructions and surveys
> - A. Klappenecker and M. Rötteler,
>   *Constructions of mutually unbiased bases*,
>   in *Finite Fields and Applications*, LNCS 2948 (2004).
>
> ### Dimension six and the maximal-number problem
> - M. Grassl,
>   *On SIC-POVMs and MUBs in Dimension 6*,
>   arXiv:quant-ph/0406175 (2004).
> - P. Butterley and W. Hall,
>   *Numerical evidence for the maximum number of mutually unbiased bases in dimension six*,
>   Phys. Lett. A 369, 5-8 (2007),
>   arXiv:quant-ph/0701122.
> - S. Brierley and S. Weigert,
>   *Maximal Sets of Mutually Unbiased Quantum States in Dimension Six*,
>   Phys. Rev. A 78, 042312 (2008),
>   arXiv:0808.1614.
> - P. Raynal, X. Lü, and B.-G. Englert,
>   *Mutually unbiased bases in dimension six: The four most distant bases*,
>   Phys. Rev. A 83, 062303 (2011),
>   arXiv:1103.1025.
> - [OAI26a] OpenAI,
>   *Exact Fourier certificates for complex Hadamard matrices of order six*.
>   OpenAI Math Release preprint (2026).
>   https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Exact-Fourier-certificates-for-complex-Hadamard-matrices-of-order-six-September-24-2026/Exact-Fourier-certificates-for-complex-Hadamard-matrices-of-order-six-September-24-2026.pdf
> - [OAI26b] OpenAI,
>   *The maximum number of mutually unbiased bases in dimension six*.
>   OpenAI Math Release preprint (2026).
>   https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/The-maximum-number-of-mutually-unbiased-bases-in-dimension-six-September-24-2026/The-maximum-number-of-mutually-unbiased-bases-in-dimension-six-September-24-2026.pdf
>
> ## Remark on the status of $d = 6$
>
> The dimension-six case is not known to be solved. At present, the best-known general picture is:
> - $3 \le \mu(6) \le 5$, where the upper bound was proved by an internal OpenAI model in
>   September 2026 [OAI26a] with a formal Lean proof,
> - a companion preprint [OAI26b] claims $\mu(6) = 3$ by a computer-assisted argument that is not
>   formalised,
> - and several analytic and numerical works give strong evidence that one cannot go beyond $3$.
>
> This is why the theorem `mutuallyUnbiasedBases_dim6` is marked as an open research statement.

*Quoted from [FormalConjectures/OpenQuantumProblems/13.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OpenQuantumProblems/13.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 9 research or textbook statements: 6 open and 3 solved. It also has 2 test statements and 28 API statements, counted here but not shown.

## `OpenQuantumProblem13.mutuallyUnbiasedBases_dim2`

Proved here.

> In dimension $2$, the maximum number of mutually unbiased orthonormal bases is $3$.

```lean
theorem mutuallyUnbiasedBases_dim2 : IsMaxMUBCount 2 3
```

Category `research solved`; AMS [05 Combinatorics](../by-subject/part-01/05-combinatorics/README.md), [15 Linear and multilinear algebra; matrix theory](../by-subject/part-01/15-linear-and-multilinear-algebra-matrix-theory/README.md), [81 Quantum theory](../by-subject/part-03/81-quantum-theory/README.md), [94 Information and communication, circuits](../by-subject/part-03/94-information-and-communication-circuits/README.md). Declared in [FormalConjectures/OpenQuantumProblems/13.lean, line 526](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OpenQuantumProblems/13.lean#L526).

## `OpenQuantumProblem13.mutuallyUnbiasedBases_dim6_bounds`

Solved: stated here; a Lean proof is at [https://github.com/XC0R/formal-conjectures/blob/c8733543568e8011288a9fa7ef33375f5e5907d3/FormalConjectures/OpenQuantumProblems/13.lean#L1168](https://github.com/XC0R/formal-conjectures/blob/c8733543568e8011288a9fa7ef33375f5e5907d3/FormalConjectures/OpenQuantumProblems/13.lean#L1168).

> Known general bounds in dimension $6$: the maximal number of mutually unbiased bases
> satisfies $3 \le \mu(6) \le 7$.

```lean
theorem mutuallyUnbiasedBases_dim6_bounds :
    HasMUBs 6 3 ∧ ∀ m : ℕ, HasMUBs 6 m → m ≤ 7
```

Category `research solved`; AMS [05 Combinatorics](../by-subject/part-01/05-combinatorics/README.md), [15 Linear and multilinear algebra; matrix theory](../by-subject/part-01/15-linear-and-multilinear-algebra-matrix-theory/README.md), [81 Quantum theory](../by-subject/part-03/81-quantum-theory/README.md), [94 Information and communication, circuits](../by-subject/part-03/94-information-and-communication-circuits/README.md). Declared in [FormalConjectures/OpenQuantumProblems/13.lean, line 534](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OpenQuantumProblems/13.lean#L534).

## `OpenQuantumProblem13.mutuallyUnbiasedBases_dim6_bounds.variants.upper_five`

Solved: stated here; a Lean proof is at [https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/OAI/Analysis/MutuallyUnbiased/Main.lean#L22](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/OAI/Analysis/MutuallyUnbiased/Main.lean#L22).

> The upper bound $\mu(6) \le 5$: every family of mutually unbiased bases in $\mathbb{C}^6$
> has at most five members. This was proved by an internal OpenAI model in September 2026
> [OAI26a]; see the linked Lean proof. That proof represents each basis as an `OrthonormalBasis`
> of `EuclideanSpace ℂ (Fin 6)`, which corresponds to the columns of a unitary matrix here.

```lean
theorem mutuallyUnbiasedBases_dim6_bounds.variants.upper_five :
    ∀ m : ℕ, HasMUBs 6 m → m ≤ 5
```

Category `research solved`; AMS [05 Combinatorics](../by-subject/part-01/05-combinatorics/README.md), [15 Linear and multilinear algebra; matrix theory](../by-subject/part-01/15-linear-and-multilinear-algebra-matrix-theory/README.md), [81 Quantum theory](../by-subject/part-03/81-quantum-theory/README.md), [94 Information and communication, circuits](../by-subject/part-03/94-information-and-communication-circuits/README.md). Declared in [FormalConjectures/OpenQuantumProblems/13.lean, line 545](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OpenQuantumProblems/13.lean#L545).

## `OpenQuantumProblem13.mutuallyUnbiasedBases_dim6`

Open: stated without proof.

> Special case in dimension $6$: determine the maximal number of mutually unbiased
> orthonormal bases in $\mathbb{C}^6$.

```lean
theorem mutuallyUnbiasedBases_dim6 :
    IsMaxMUBCount 6 (mutuallyUnbiasedBases_dim6.answer)
```

Category `research open`; AMS [05 Combinatorics](../by-subject/part-01/05-combinatorics/README.md), [15 Linear and multilinear algebra; matrix theory](../by-subject/part-01/15-linear-and-multilinear-algebra-matrix-theory/README.md), [81 Quantum theory](../by-subject/part-03/81-quantum-theory/README.md), [94 Information and communication, circuits](../by-subject/part-03/94-information-and-communication-circuits/README.md). Declared in [FormalConjectures/OpenQuantumProblems/13.lean, line 556](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OpenQuantumProblems/13.lean#L556).

## `OpenQuantumProblem13.mutuallyUnbiasedBases_dim10`

Open: stated without proof.

> Special case in dimension $10$ (not a prime power): determine the maximal number of
> mutually unbiased orthonormal bases in $\mathbb{C}^{10}$.

```lean
theorem mutuallyUnbiasedBases_dim10 :
    IsMaxMUBCount 10 (mutuallyUnbiasedBases_dim10.answer)
```

Category `research open`; AMS [05 Combinatorics](../by-subject/part-01/05-combinatorics/README.md), [15 Linear and multilinear algebra; matrix theory](../by-subject/part-01/15-linear-and-multilinear-algebra-matrix-theory/README.md), [81 Quantum theory](../by-subject/part-03/81-quantum-theory/README.md), [94 Information and communication, circuits](../by-subject/part-03/94-information-and-communication-circuits/README.md). Declared in [FormalConjectures/OpenQuantumProblems/13.lean, line 565](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OpenQuantumProblems/13.lean#L565).

## `OpenQuantumProblem13.mutuallyUnbiasedBases_dim12`

Open: stated without proof.

> Special case in dimension $12$ (not a prime power): determine the maximal number of
> mutually unbiased orthonormal bases in $\mathbb{C}^{12}$.

```lean
theorem mutuallyUnbiasedBases_dim12 :
    IsMaxMUBCount 12 (mutuallyUnbiasedBases_dim12.answer)
```

Category `research open`; AMS [05 Combinatorics](../by-subject/part-01/05-combinatorics/README.md), [15 Linear and multilinear algebra; matrix theory](../by-subject/part-01/15-linear-and-multilinear-algebra-matrix-theory/README.md), [81 Quantum theory](../by-subject/part-03/81-quantum-theory/README.md), [94 Information and communication, circuits](../by-subject/part-03/94-information-and-communication-circuits/README.md). Declared in [FormalConjectures/OpenQuantumProblems/13.lean, line 574](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OpenQuantumProblems/13.lean#L574).

## `OpenQuantumProblem13.mutuallyUnbiasedBases_dim14`

Open: stated without proof.

> Special case in dimension $14$ (not a prime power): determine the maximal number of
> mutually unbiased orthonormal bases in $\mathbb{C}^{14}$.

```lean
theorem mutuallyUnbiasedBases_dim14 :
    IsMaxMUBCount 14 (mutuallyUnbiasedBases_dim14.answer)
```

Category `research open`; AMS [05 Combinatorics](../by-subject/part-01/05-combinatorics/README.md), [15 Linear and multilinear algebra; matrix theory](../by-subject/part-01/15-linear-and-multilinear-algebra-matrix-theory/README.md), [81 Quantum theory](../by-subject/part-03/81-quantum-theory/README.md), [94 Information and communication, circuits](../by-subject/part-03/94-information-and-communication-circuits/README.md). Declared in [FormalConjectures/OpenQuantumProblems/13.lean, line 583](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OpenQuantumProblems/13.lean#L583).

## `OpenQuantumProblem13.mutuallyUnbiasedBases_dim15`

Open: stated without proof.

> Special case in dimension $15$ (not a prime power): determine the maximal number of
> mutually unbiased orthonormal bases in $\mathbb{C}^{15}$.

```lean
theorem mutuallyUnbiasedBases_dim15 :
    IsMaxMUBCount 15 (mutuallyUnbiasedBases_dim15.answer)
```

Category `research open`; AMS [05 Combinatorics](../by-subject/part-01/05-combinatorics/README.md), [15 Linear and multilinear algebra; matrix theory](../by-subject/part-01/15-linear-and-multilinear-algebra-matrix-theory/README.md), [81 Quantum theory](../by-subject/part-03/81-quantum-theory/README.md), [94 Information and communication, circuits](../by-subject/part-03/94-information-and-communication-circuits/README.md). Declared in [FormalConjectures/OpenQuantumProblems/13.lean, line 592](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OpenQuantumProblems/13.lean#L592).

## `OpenQuantumProblem13.mutuallyUnbiasedBases`

Open: stated without proof.

> Open Quantum Problem 13: determine the maximal number of mutually unbiased orthonormal
> bases in $\mathbb{C}^d$ for $d \ge 2$.

```lean
theorem mutuallyUnbiasedBases (d : ℕ) (hd : 2 ≤ d) :
    IsMaxMUBCount d (mutuallyUnbiasedBases.answer d)
```

Category `research open`; AMS [05 Combinatorics](../by-subject/part-01/05-combinatorics/README.md), [15 Linear and multilinear algebra; matrix theory](../by-subject/part-01/15-linear-and-multilinear-algebra-matrix-theory/README.md), [81 Quantum theory](../by-subject/part-03/81-quantum-theory/README.md), [94 Information and communication, circuits](../by-subject/part-03/94-information-and-communication-circuits/README.md). Declared in [FormalConjectures/OpenQuantumProblems/13.lean, line 601](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OpenQuantumProblems/13.lean#L601).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OpenQuantumProblems/13.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OpenQuantumProblems/13.lean)
