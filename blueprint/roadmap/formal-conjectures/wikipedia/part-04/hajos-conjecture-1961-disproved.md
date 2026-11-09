---
declaration: theorem
origin: cited
lean: HajosConjecture.hajos_conjecture, HajosConjecture.hajos_conjecture.variants.le_four, HajosConjecture.hajos_conjecture.variants.five_six, HajosConjecture.hajos_conjecture.variants.catlin
statement: formalized
---

# Hajós' conjecture (1961) — disproved

> *References:*
> * [Wikipedia](https://en.wikipedia.org/wiki/Hadwiger_conjecture_(graph_theory)#Generalizations)
> * [Ha61] Hajós, G. (1961). "Über eine Konstruktion nicht n-färbbarer Graphen."
>   *Wiss. Z. Martin-Luther-Univ. Halle-Wittenberg Math.-Natur. Reihe* 10, pp. 116--117.
> * [Di52] Dirac, G. A. (1952). "A property of 4-chromatic graphs and some remarks on critical
>   graphs." *J. London Math. Soc.* 27, pp. 85--92.
> * [Ca79] Catlin, P. A. (1979). "Hajós' graph-coloring conjecture: variations and
>   counterexamples." *J. Combin. Theory Ser. B* 26, pp. 268--274.
> * [EF81] Erdős, P. and Fajtlowicz, S. (1981). "On the conjecture of Hajós." *Combinatorica* 1,
>   pp. 141--143.
> * [Th05] Thomassen, C. (2005). "Some remarks on Hajós' conjecture." *J. Combin. Theory Ser. B*
>   93, pp. 95--105.

*Quoted from [FormalConjectures/Wikipedia/HajosConjecture.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/HajosConjecture.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 4 research or textbook statements: 1 open and 3 solved. It also has 1 API statement, counted here but not shown.

## `HajosConjecture.hajos_conjecture`

Solved: stated here without proof.

> **Hajós' conjecture (1961) — disproved.**
>
> Hajós conjectured that every graph with chromatic number at least $k$ contains a subdivision of
> $K_k$ (a strengthening of Hadwiger's conjecture). This is **false**: Catlin [Ca79] gave
> counterexamples for every $k \ge 7$, and Erdős and Fajtlowicz [EF81] showed that almost all
> graphs are counterexamples.

```lean
theorem hajos_conjecture : ¬
    ∀ {V : Type} [Fintype V] (G : SimpleGraph V) (k : ℕ),
      (k : ℕ∞) ≤ G.chromaticNumber → ContainsSubdivision (completeGraph (Fin k)) G
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/Wikipedia/HajosConjecture.lean, line 71](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/HajosConjecture.lean#L71).

## `HajosConjecture.hajos_conjecture.variants.le_four`

Solved: stated here without proof.

> **The cases $k \le 4$ (Dirac 1952).**
>
> Every graph with chromatic number at least $4$ contains a subdivision of $K_4$; the cases
> $k \le 3$ are elementary.
>
> *Reference:* [Di52].

```lean
theorem hajos_conjecture.variants.le_four
    {V : Type} [Fintype V] (G : SimpleGraph V) (k : ℕ) (hk : k ≤ 4)
    (h : (k : ℕ∞) ≤ G.chromaticNumber) : ContainsSubdivision (completeGraph (Fin k)) G
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/Wikipedia/HajosConjecture.lean, line 85](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/HajosConjecture.lean#L85).

## `HajosConjecture.hajos_conjecture.variants.five_six`

Open: stated without proof.

> **The cases $k = 5$ and $k = 6$ remain open.**
>
> Whether every $5$-chromatic graph contains a subdivision of $K_5$, and every $6$-chromatic graph
> a subdivision of $K_6$, is unknown (see [Th05]).

```lean
theorem hajos_conjecture.variants.five_six :
    ∀ {V : Type} [Fintype V] (G : SimpleGraph V) (k : ℕ), k = 5 ∨ k = 6 →
      (k : ℕ∞) ≤ G.chromaticNumber → ContainsSubdivision (completeGraph (Fin k)) G
```

Category `research open`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/Wikipedia/HajosConjecture.lean, line 97](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/HajosConjecture.lean#L97).

## `HajosConjecture.hajos_conjecture.variants.catlin`

Solved: stated here without proof.

> **Catlin (1979): counterexamples for every $k \ge 7$.**
>
> *Reference:* [Ca79].

```lean
theorem hajos_conjecture.variants.catlin (k : ℕ) (hk : 7 ≤ k) :
    ∃ (V : Type) (_ : Fintype V) (G : SimpleGraph V),
      (k : ℕ∞) ≤ G.chromaticNumber ∧ ¬ ContainsSubdivision (completeGraph (Fin k)) G
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/Wikipedia/HajosConjecture.lean, line 108](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/HajosConjecture.lean#L108).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Wikipedia/HajosConjecture.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/HajosConjecture.lean)
- [Wikipedia](https://en.wikipedia.org/wiki/Hadwiger_conjecture_%28graph_theory%29#Generalizations)
