---
declaration: theorem
origin: cited
lean: Erdos927.erdos_927
statement: formalized
---

# Erdős Problem 927

> *References:*
> - [erdosproblems.com/927](https://www.erdosproblems.com/927)
> - [MoMo65] Moon, J. W. and Moser, L., *On cliques in graphs*. Israel J. Math. (1965), 23-28.
> - [Er66b] Erdős, P., *On cliques in graphs*. Israel J. Math. (1966), 233--234.
> - [Er69b] Erdős, P., *Problems and results in chromatic graph theory*. Proof Techniques in Graph
>   Theory (Proc. Second Ann Arbor Graph Theory Conf., Ann Arbor, Mich., 1968) (1969), 27-35.
> - [Er71] Erdős, P., *Some unsolved problems in graph theory and combinatorial analysis*.
>   Combinatorial Mathematics and its Applications (Proc. Conf., Oxford, 1969) (1971), 97-109.
> - [Sp71] Spencer, J. H., *On cliques in graphs*. Israel J. Math. (1971), 419-421.

*Quoted from [FormalConjectures/ErdosProblems/927.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/927.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/927](https://www.erdosproblems.com/927).

The file states 1 research or textbook statement: 1 solved.

## `Erdos927.erdos_927`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos927.lean#L23](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos927.lean#L23).

> Let $g(n)$ be the maximum number of different sizes of cliques that can occur in a graph on $n$
> vertices. Estimate $g(n)$ - in particular, is it true that
>
> $$g(n) = n - \log_2 n - \log_*(n) + O(1),$$
>
> where $\log_*(n)$ is the number of iterated logarithms such that $\log \cdots \log n < 1$?
>
> A quantity first considered by Moon and Moser [MoMo65], who proved
> $n - \log_2 n - 2 \log \log n < g(n) \le n - \lfloor \log_2 n \rfloor$. Erdős [Er66b] improved the
> lower bound to $n - \log_2 n - \log_*(n) - O(1) < g(n)$ and conjectured this was the correct order
> of magnitude. This was disproved by Spencer [Sp71], who proved that in fact
> $g(n) > n - \log_2 n - O(1)$.
>
> Here $\log_2 n$ and $\log_*(n)$ are formalised as `Nat.log 2 n` and `Nat.iteratedLog 2 n`
> (iterating `Nat.log 2` until the value is at most `1`); both differ from the quantities in the
> problem by $O(1)$, so the statement is unaffected. See also `erdos_775.variants.spencer` and
> `erdos_775.variants.moon_moser`.

```lean
theorem erdos_927 :
    ¬ ∃ C : ℕ, ∀ᶠ n : ℕ in atTop,
      g n + Nat.log 2 n + Nat.iteratedLog 2 n ≤ n + C ∧
        n ≤ g n + Nat.log 2 n + Nat.iteratedLog 2 n + C
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/927.lean, line 68](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/927.lean#L68).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/927.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/927.lean)
- [erdosproblems.com/927](https://www.erdosproblems.com/927)
