---
declaration: theorem
origin: cited
lean: Erdos540.erdos_540
statement: formalized
---

# Erdős Problem 540

> *References:*
> - [erdosproblems.com/540](https://www.erdosproblems.com/540)
> - [Er65b] Erdős, Paul, *Some recent advances and current problems in number theory*. Lectures on
>   Modern Mathematics, Vol. III (1965), 196-244.
> - [Er73] Erdős, P., *Problems and results on combinatorial number theory*. A survey of combinatorial
>   theory (Proc. Internat. Sympos., Colorado State Univ., Fort Collins, Colo., 1971) (1973), 117-138.
> - [ErGr80] Erdős, P. and Graham, R., *Old and new problems and results in combinatorial number
>   theory*. Monographies de L'Enseignement Mathematique (1980).
> - [Ol68] Olson, John E., *An addition theorem modulo {$p$}*. J. Combinatorial Theory (1968), 45--52.
> - [Ba12] Balandraud, Éric, *An addition theorem and maximal zero-sum free sets in
>   $\mathbb{Z}/p\mathbb{Z}$*. Israel J. Math. (2012), 405-429.
> - [HaZe96] Hamidoune, Yahya Ould and Zémor, Gilles, *On zero-free subset sums*. Acta Arith. (1996),
>   143--152.
> - [Gu04] Guy, Richard K., *Unsolved problems in number theory*. (2004), xviii+437.
> - [ErHe64] Erdős, P. and Heilbronn, H., *On the addition of residue classes
>   mod $p$*. Acta Arith. (1964), 149--159.
> - [Sz70] Szemerédi, E., *On a conjecture of Erdős and Heilbronn*. Acta Arith.
>   (1970), 227-229.

*Quoted from [FormalConjectures/ErdosProblems/540.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/540.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/540](https://www.erdosproblems.com/540).

The file states 1 research or textbook statement: 1 solved.

## `Erdos540.erdos_540`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/main/src/v4.29.1/ErdosProblems/Erdos540.lean](https://github.com/plby/lean-proofs/blob/main/src/v4.29.1/ErdosProblems/Erdos540.lean).

> Is it true that if $A\subseteq \mathbb{Z}/N\mathbb{Z}$ has size $\gg N^{1/2}$ then there exists
> some non-empty $S\subseteq A$ such that $\sum_{n\in S}n\equiv 0\pmod{N}$?
>
> Szemerédi proved the answer is yes, in fact for arbitrary finite abelian groups.

```lean
theorem erdos_540 :
    ∃ C : ℝ, 0 < C ∧
      ∀ (N : ℕ), 0 < N → ∀ A : Finset (ZMod N),
        C * Real.sqrt N ≤ A.card →
          HasZeroSubsetSum A
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/540.lean, line 59](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/540.lean#L59).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/540.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/540.lean)
- [erdosproblems.com/540](https://www.erdosproblems.com/540)
