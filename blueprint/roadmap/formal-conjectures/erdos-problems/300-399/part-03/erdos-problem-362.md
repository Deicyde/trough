---
declaration: theorem
origin: cited
lean: Erdos362.erdos_362, Erdos362.erdos_362.variants.fixed_card
statement: formalized
---

# Erdős Problem 362

> *References:*
> - [erdosproblems.com/362](https://www.erdosproblems.com/362)
> - [Er65] Erdős, P., *Extremal problems in number theory*. Proc. Sympos. Pure Math., Vol. VIII
>   (1965), 181-189.
> - [Er73] Erdős, P., *Problems and results on combinatorial number theory*. A survey of
>   combinatorial theory (Proc. Internat. Sympos., Colorado State Univ., Fort Collins, Colo., 1971)
>   (1973), 117-138.
> - [ErGr80] Erdős, P. and Graham, R., *Old and new problems and results in combinatorial number
>   theory*. Monographies de L'Enseignement Mathematique (1980).
> - [SaSz65] Sárközi, A. and Szemerédi, E., *Über ein Problem von Erdős und Moser*. Acta Arith.
>   (1965), 205-208.
> - [St80] Stanley, Richard P., *Weyl groups, the hard Lefschetz theorem, and the Sperner property*.
>   SIAM J. Algebraic Discrete Methods (1980), 168-184.
> - [Ha77] Halász, G., *Estimates for the concentration function of combinatorial number theory and
>   probability*. Period. Math. Hungar. (1977), 197-211.

*Quoted from [FormalConjectures/ErdosProblems/362.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/362.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/362](https://www.erdosproblems.com/362).

The file states 2 research or textbook statements: 2 solved.

## `Erdos362.erdos_362`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos362.lean#L2541](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos362.lean#L2541).

> Let $A\subseteq \mathbb{N}$ be a finite set of size $N$. Is it true that, for any fixed $t$,
> there are
>
> $$\ll \frac{2^N}{N^{3/2}}$$
>
> many $S\subseteq A$ such that $\sum_{n\in S}n=t$?
>
> Erdős and Moser [Er65] proved the first bound with an additional factor of $(\log n)^{3/2}$.
> This was removed by Sárközy and Szemerédi [SaSz65], thereby answering the first question in the
> affirmative. Stanley [St80] has shown that this quantity is maximised when
> $A=\{-\lfloor \frac{N-1}{2}\rfloor,\ldots,\lfloor\frac{N}{2}\rfloor\}$.

```lean
theorem erdos_362 : ∃ C : ℝ, ∀ (A : Finset ℕ) (t : ℕ), A.Nonempty →
    ({S ∈ A.powerset | ∑ n ∈ S, n = t}.card : ℝ) ≤ C * 2 ^ A.card / (A.card : ℝ) ^ (3 / 2 : ℝ)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/362.lean, line 58](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/362.lean#L58).

## `Erdos362.erdos_362.variants.fixed_card`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos362.lean#L2541](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos362.lean#L2541).

> If we further ask that $\lvert S\rvert=l$ (for any fixed $l$) then is the number of solutions
>
> $$\ll \frac{2^N}{N^2},$$
>
> with the implied constant independent of $l$ and $t$?
>
> The second question was answered in the affirmative by Halász [Ha77], as a consequence of a more
> general multi-dimensional result.

```lean
theorem erdos_362.variants.fixed_card : ∃ C : ℝ, ∀ (A : Finset ℕ) (l t : ℕ),
    A.Nonempty →
      ({S ∈ A.powersetCard l | ∑ n ∈ S, n = t}.card : ℝ) ≤ C * 2 ^ A.card / (A.card : ℝ) ^ 2
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/362.lean, line 73](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/362.lean#L73).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/362.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/362.lean)
- [erdosproblems.com/362](https://www.erdosproblems.com/362)
