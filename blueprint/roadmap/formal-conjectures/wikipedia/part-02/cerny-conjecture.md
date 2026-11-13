---
declaration: theorem
origin: cited
lean: CernyConjecture.cerny_conjecture, CernyConjecture.shitov_upper_bound
statement: formalized
---

# Černý Conjecture

> A **synchronizing word** (also called a reset word) for a deterministic finite automaton (DFA)
> $M = (Q, \Sigma, \delta)$ is a word $w \in \Sigma^\*$ such that reading $w$ from any state always
> leads to the same single state — formally, $\exists p \in Q, \forall q \in Q, \delta^\*(q, w) = p$.
>
> A DFA is called **synchronizing** if it admits at least one synchronizing word.
>
> The **Černý conjecture** asserts that every synchronizing DFA with $n$ states has a
> synchronizing word of length at most $(n - 1)^2$. This bound is sharp: the family of Černý
> automata $C_n$ witnesses it, requiring exactly $(n - 1)^2$ steps.
>
> **Status:** Open. The best known upper bound is
> $\left(\frac{7}{48} + \frac{2 \cdot 15625}{1597536}\right) n^3 + o(n^3) \approx 0.1654\,n^3$
> (Shitov, 2019). The bound $(n - 1)^2$ has been verified for small $n$ and for special classes of
> automata (e.g., Eulerian, aperiodic, cyclic automata).
>
> We use Mathlib's `DFA α σ` (from `Mathlib.Computability.DFA`), together with the auxiliary
> `DFA.IsSynchronizingWord` and `DFA.IsSynchronizing` predicates defined in
> `FormalConjecturesForMathlib.Computability.DFA`.
>
> *References:*
> - [Wikipedia: Synchronizing word](https://en.wikipedia.org/wiki/Synchronizing_word)
> - J. Černý, [*Poznámka k homogénnym experimentom s konečnými automatmi*](https://dml.cz/bitstream/handle/10338.dmlcz/126647/MathSlov_14-1964-3_2.pdf),
>   Matematicko-fyzikálny časopis, Vol. 14 (1964), No. 3, 208--216.
> - Y. Shitov, *An improvement to a recent upper bound for synchronizing words of finite automata*,
>   J. Autom. Lang. Comb. Vol. 24 (2019), 367--373.

*Quoted from [FormalConjectures/Wikipedia/CernyConjecture.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/CernyConjecture.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 2 research or textbook statements: 1 open and 1 solved.

## `CernyConjecture.cerny_conjecture`

Open: stated without proof.

> **Černý Conjecture**: Every synchronizing DFA with $n$ states admits a
> synchronizing word of length at most $(n - 1)^2$.

```lean
theorem cerny_conjecture :
    ∀ {α : Type*} {σ : Type*} [Fintype σ] (M : DFA α σ) (hM : M.IsSynchronizing) ,
    ∃ w : List α, M.IsSynchronizingWord w ∧ w.length ≤ (Fintype.card σ - 1)^2
```

Category `research open`; AMS [68 Computer science](../../by-subject/part-02/68-computer-science/README.md). Declared in [FormalConjectures/Wikipedia/CernyConjecture.lean, line 60](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/CernyConjecture.lean#L60).

## `CernyConjecture.shitov_upper_bound`

Solved: stated here without proof.

> **Shitov's bound (2019)**: Every synchronizing DFA with $n$ states admits a synchronizing
> word of length at most $\left(\frac{7}{48} + \frac{2 \cdot 15625}{1597536}\right) n^3 + o(n^3)$,
> where the $o(n^3)$ term is uniform over all alphabets. This is the best known upper bound
> towards the Černý conjecture.

```lean
theorem shitov_upper_bound :
    ∃ f : ℝ → ℝ, f =o[atTop] (fun n : ℝ => n ^ 3) ∧
    ∀ {α : Type*} {σ : Type*} [Fintype σ] (M : DFA α σ) (hM : M.IsSynchronizing) ,
    ∃ w : List α, M.IsSynchronizingWord w ∧
    (w.length : ℝ) ≤ (7 / 48 + 2 * 15625 / 1597536) * (Fintype.card σ : ℝ) ^ 3
      + f (Fintype.card σ : ℝ)
```

Category `research solved`; AMS [68 Computer science](../../by-subject/part-02/68-computer-science/README.md). Declared in [FormalConjectures/Wikipedia/CernyConjecture.lean, line 71](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/CernyConjecture.lean#L71).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Wikipedia/CernyConjecture.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/CernyConjecture.lean)
- [Wikipedia: Synchronizing word](https://en.wikipedia.org/wiki/Synchronizing_word)
