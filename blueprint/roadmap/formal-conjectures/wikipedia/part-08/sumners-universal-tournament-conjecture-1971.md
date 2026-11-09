---
declaration: theorem
origin: cited
lean: SumnerUniversalTournamentConjecture.sumner_conjecture, SumnerUniversalTournamentConjecture.sumner_conjecture.variants.large_n, SumnerUniversalTournamentConjecture.sumner_conjecture.variants.el_sahili, SumnerUniversalTournamentConjecture.sumner_conjecture.variants.sharp
statement: formalized
---

# Sumner's universal tournament conjecture (1971)

> *References:*
> * [Wikipedia](https://en.wikipedia.org/wiki/Sumner%27s_conjecture)
> * [HT91] Häggkvist, R. and Thomason, A. (1991). "Trees in tournaments." *Combinatorica* 11,
>   pp. 123--130.
> * [ES04] El Sahili, A. (2004). "Trees in tournaments." *J. Combin. Theory Ser. B* 92,
>   pp. 183--187.
> * [KMO11] Kühn, D., Mycroft, R. and Osthus, D. (2011). "A proof of Sumner's universal
>   tournament conjecture for large tournaments." *Proc. London Math. Soc.* 102, pp. 731--766.
>   [arXiv:1010.4430](https://arxiv.org/abs/1010.4430)

*Quoted from [FormalConjectures/Wikipedia/SumnerUniversalTournamentConjecture.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/SumnerUniversalTournamentConjecture.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 4 research or textbook statements: 1 open and 3 solved.

## `SumnerUniversalTournamentConjecture.sumner_conjecture`

Open: stated without proof.

> **Sumner's universal tournament conjecture (1971).**
>
> Every tournament on $2n - 2$ vertices contains every oriented tree on $n \ge 2$ vertices as a
> subgraph.

```lean
theorem sumner_conjecture :
    ∀ (n : ℕ), 2 ≤ n →
      ∀ {W : Type} [Fintype W] [DecidableEq W] (D : Digraph W) [DecidableRel D.Adj],
        Fintype.card W = n → IsOrientedTree D →
        ∀ {V : Type} [Fintype V] [DecidableEq V] (G : Digraph V) [DecidableRel G.Adj],
          Fintype.card V = 2 * n - 2 → G.IsTournament → Embeds D G
```

Category `research open`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/Wikipedia/SumnerUniversalTournamentConjecture.lean, line 57](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/SumnerUniversalTournamentConjecture.lean#L57).

## `SumnerUniversalTournamentConjecture.sumner_conjecture.variants.large_n`

Solved: stated here without proof.

> **Kühn–Mycroft–Osthus (2011): the conjecture holds for all sufficiently large $n$.**
>
> *Reference:* [KMO11].

```lean
theorem sumner_conjecture.variants.large_n :
    ∃ n₀ : ℕ, ∀ (n : ℕ), n₀ ≤ n →
      ∀ {W : Type} [Fintype W] [DecidableEq W] (D : Digraph W) [DecidableRel D.Adj],
        Fintype.card W = n → IsOrientedTree D →
        ∀ {V : Type} [Fintype V] [DecidableEq V] (G : Digraph V) [DecidableRel G.Adj],
          Fintype.card V = 2 * n - 2 → G.IsTournament → Embeds D G
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/Wikipedia/SumnerUniversalTournamentConjecture.lean, line 71](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/SumnerUniversalTournamentConjecture.lean#L71).

## `SumnerUniversalTournamentConjecture.sumner_conjecture.variants.el_sahili`

Solved: stated here without proof.

> **El Sahili (2004): tournaments on $3n - 3$ vertices suffice.**
>
> Every tournament on $3n - 3$ vertices contains every oriented tree on $n \ge 2$ vertices,
> improving the bound $12n$ of Häggkvist and Thomason [HT91].
>
> *Reference:* [ES04].

```lean
theorem sumner_conjecture.variants.el_sahili (n : ℕ) (hn : 2 ≤ n)
    {W : Type} [Fintype W] [DecidableEq W] (D : Digraph W) [DecidableRel D.Adj]
    (hW : Fintype.card W = n) (hD : IsOrientedTree D)
    {V : Type} [Fintype V] [DecidableEq V] (G : Digraph V) [DecidableRel G.Adj]
    (hV : Fintype.card V = 3 * n - 3) (hG : G.IsTournament) : Embeds D G
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/Wikipedia/SumnerUniversalTournamentConjecture.lean, line 88](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/SumnerUniversalTournamentConjecture.lean#L88).

## `SumnerUniversalTournamentConjecture.sumner_conjecture.variants.sharp`

Solved: stated here without proof.

> **The bound $2n - 2$ would be sharp.**
>
> For every $n \ge 2$ there is an oriented tree on $n$ vertices — the out-star, with arcs from a
> centre to the $n - 1$ other vertices — that embeds in no regular tournament on $2n - 3$ vertices:
> every vertex of such a tournament has out-degree $n - 2 < n - 1$.

```lean
theorem sumner_conjecture.variants.sharp (n : ℕ) (hn : 2 ≤ n) :
    ∃ (W : Type) (_ : Fintype W) (_ : DecidableEq W) (D : Digraph W) (_ : DecidableRel D.Adj),
      Fintype.card W = n ∧ IsOrientedTree D ∧
      ∃ (V : Type) (_ : Fintype V) (_ : DecidableEq V) (G : Digraph V) (_ : DecidableRel G.Adj),
        Fintype.card V = 2 * n - 3 ∧ G.IsTournament ∧ ¬ Embeds D G
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/Wikipedia/SumnerUniversalTournamentConjecture.lean, line 103](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/SumnerUniversalTournamentConjecture.lean#L103).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Wikipedia/SumnerUniversalTournamentConjecture.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/SumnerUniversalTournamentConjecture.lean)
- [Wikipedia](https://en.wikipedia.org/wiki/Sumner%27s_conjecture)
