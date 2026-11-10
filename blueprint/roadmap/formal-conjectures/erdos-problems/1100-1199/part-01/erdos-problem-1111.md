---
declaration: theorem
origin: cited
lean: Erdos1111.erdos_1111, Erdos1111.erdos_1111.variants.wagon, Erdos1111.erdos_1111.variants.el_zahar_erdos, Erdos1111.erdos_1111.variants.three_three, Erdos1111.erdos_1111.variants.nguyen_scott_seymour
statement: formalized
---

# Erdős Problem 1111

> *References:*
> - [erdosproblems.com/1111](https://www.erdosproblems.com/1111)
> - [ElEr85] El-Zahar, M. and Erdős, P., *On the existence of two non-neighboring subgraphs in a
>   graph*. Combinatorica 5 (1985), 295-300.
> - [NSS24] Nguyen, T., Scott, A. and Seymour, P., *On a problem of El-Zahar and Erdős*.
>   J. Combin. Theory Ser. B 165 (2024), 211-222. [arXiv:2303.13449](https://arxiv.org/abs/2303.13449)
> - [Wa80b] Wagon, S., *A bound on the chromatic number of graphs without certain induced
>   subgraphs*. J. Combin. Theory Ser. B 29 (1980), 345-346.

*Quoted from [FormalConjectures/ErdosProblems/1111.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1111.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/1111](https://www.erdosproblems.com/1111).

The file states 5 research or textbook statements: 1 open and 4 solved. It also has 1 API statement, counted here but not shown.

## `Erdos1111.erdos_1111`

Open: stated without proof.

> If $G$ is a finite graph and $A,B$ are disjoint sets of vertices then we call $A,B$ anticomplete
> if there are no edges between $A$ and $B$.
>
> If $t,c\geq 1$ then there exists $d\geq 1$ such that if $\chi(G)\geq d$ and $\omega(G)\lt t$ then
> there are anticomplete sets $A,B$ with $\chi(A)\geq \chi(B)\geq c$.
>
> El-Zahar and Erdős [ElEr85] pose this as a question. Here $\chi(A)$ is the chromatic number of
> the induced subgraph $G[A]$. Swapping $A$ and $B$, the conclusion says that both $\chi(A)$ and
> $\chi(B)$ are at least $c$.

```lean
theorem erdos_1111 :
    ∀ t c : ℕ, 1 ≤ t → 1 ≤ c → ∃ d : ℕ, 1 ≤ d ∧
      ∀ (V : Type*) [Finite V] (G : SimpleGraph V),
        (d : ℕ∞) ≤ G.chromaticNumber → G.CliqueFree t →
          ∃ A B : Set V, Anticomplete G A B ∧
            (c : ℕ∞) ≤ (G.induce A).chromaticNumber ∧
            (c : ℕ∞) ≤ (G.induce B).chromaticNumber
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/1111.lean, line 61](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1111.lean#L61).

## `Erdos1111.erdos_1111.variants.wagon`

Solved: stated here without proof.

> El-Zahar and Erdős note that a result of Wagon [Wa80b] implies $d(t,2)\leq \binom{t}{2}+1$, where
> $d(t,c)$ is the minimal $d$ in the problem.

```lean
theorem erdos_1111.variants.wagon (t : ℕ) :
    ∀ (V : Type*) [Finite V] (G : SimpleGraph V),
      ((t.choose 2 + 1 : ℕ) : ℕ∞) ≤ G.chromaticNumber → G.CliqueFree t →
        ∃ A B : Set V, Anticomplete G A B ∧
          2 ≤ (G.induce A).chromaticNumber ∧ 2 ≤ (G.induce B).chromaticNumber
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/1111.lean, line 75](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1111.lean#L75).

## `Erdos1111.erdos_1111.variants.el_zahar_erdos`

Solved: stated here without proof.

> El-Zahar and Erdős [ElEr85] proved the case $c = 3$: $d(t,3)$ exists for every $t$.

```lean
theorem erdos_1111.variants.el_zahar_erdos :
    ∀ t : ℕ, 1 ≤ t → ∃ d : ℕ, 1 ≤ d ∧
      ∀ (V : Type*) [Finite V] (G : SimpleGraph V),
        (d : ℕ∞) ≤ G.chromaticNumber → G.CliqueFree t →
          ∃ A B : Set V, Anticomplete G A B ∧
            3 ≤ (G.induce A).chromaticNumber ∧ 3 ≤ (G.induce B).chromaticNumber
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/1111.lean, line 86](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1111.lean#L86).

## `Erdos1111.erdos_1111.variants.three_three`

Solved: stated here without proof.

> El-Zahar and Erdős [ElEr85] proved $d(3,3)\leq 8$.

```lean
theorem erdos_1111.variants.three_three :
    ∀ (V : Type*) [Finite V] (G : SimpleGraph V),
      8 ≤ G.chromaticNumber → G.CliqueFree 3 →
        ∃ A B : Set V, Anticomplete G A B ∧
          3 ≤ (G.induce A).chromaticNumber ∧ 3 ≤ (G.induce B).chromaticNumber
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/1111.lean, line 98](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1111.lean#L98).

## `Erdos1111.erdos_1111.variants.nguyen_scott_seymour`

Solved: stated here without proof.

> Nguyen, Scott, and Seymour [NSS24] prove that if $t,c\geq 1$ then there exists $d\geq 1$ such
> that if $\chi(G)\geq d$ and $\omega(G)\lt t$ then there are anticomplete sets $A,B$ with
> $\chi(B)\geq c$ and such that the minimum degree of the induced graph on $A$ is at least $c$.

```lean
theorem erdos_1111.variants.nguyen_scott_seymour :
    ∀ t c : ℕ, 1 ≤ t → 1 ≤ c → ∃ d : ℕ, 1 ≤ d ∧
      ∀ (V : Type*) [Finite V] (G : SimpleGraph V),
        (d : ℕ∞) ≤ G.chromaticNumber → G.CliqueFree t →
          ∃ A B : Set V, Anticomplete G A B ∧
            A.Nonempty ∧ (∀ v ∈ A, c ≤ (A ∩ G.neighborSet v).ncard) ∧
            (c : ℕ∞) ≤ (G.induce B).chromaticNumber
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/1111.lean, line 111](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1111.lean#L111).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/1111.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1111.lean)
- [erdosproblems.com/1111](https://www.erdosproblems.com/1111)
