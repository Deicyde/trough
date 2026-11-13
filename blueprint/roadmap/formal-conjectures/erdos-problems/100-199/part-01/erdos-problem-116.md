---
declaration: theorem
origin: cited
lean: Erdos116.erdos_116, Erdos116.erdos_116.variants.log, Erdos116.erdos_116.variants.upper, Erdos116.erdos_116.variants.polya
statement: formalized
---

# Erdős Problem 116

> *References:*
> - [erdosproblems.com/116](https://www.erdosproblems.com/116)
> - [EHP58] Erdős, P. and Herzog, F. and Piranian, G., *Metric properties of polynomials*. J.
>   Analyse Math. (1958), 125-148.
> - [Er61] Erdős, Paul, *Some unsolved problems*. Magyar Tud. Akad. Mat. Kutató Int. Közl. (1961),
>   221-254.
> - [Er82e] Erdős, Paul, *Some of my favourite problems which recently have been solved*. (1982),
>   59--79.
> - [Er90] Erdős, Paul, *Some of my favourite unsolved problems*. A tribute to Paul Erdős (1990),
>   467-478.
> - [Er97c] Erdős, Paul, *Some of my favorite problems and results*. The mathematics of Paul Erdős,
>   I (1997), 47-67.
> - [Po61] Pommerenke, Ch., *On metric properties of complex polynomials*. Michigan Math. J. (1961),
>   97-115.
> - [KLR25] M. Krishnapur, E. Lundberg, and K. Ramachandran, *On the area of polynomial
>   lemniscates*. arXiv:2503.18270 (2025).
> - [Wa88] Wagner, Gerold, *On the area of lemniscate domains*. J. Analyse Math. (1988), 159-167.
> - [Po28] G. Pólya, *Beitrag zue Verallgemeinerung des Verzerrungssatzes auf mehrfach
>   zusammenhängende Gebiete*. S-B. Akad. Wiss. (1928), 228-232 and 280-282.

*Quoted from [FormalConjectures/ErdosProblems/116.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/116.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/116](https://www.erdosproblems.com/116).

The file states 4 research or textbook statements: 4 solved.

## `Erdos116.erdos_116`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos116.lean#L918](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos116.lean#L918).

> Let $p(z)=\prod_{i=1}^n (z-z_i)$ for $\lvert z_i\rvert \leq 1$. Is it true that
>
> $$\lvert\{ z: \lvert p(z)\rvert <1\}\rvert>n^{-O(1)}$$
>
> (or perhaps even $>(\log n)^{-O(1)}$)?
>
> Conjectured by Erdős, Herzog, and Piranian [EHP58]. The lower bound $\gg n^{-4}$ follows from a
> result of Pommerenke [Po61]. The lower bound $\gg (\log n)^{-1}$ was proved by Krishnapur,
> Lundberg, and Ramachandran [KLR25].
>
> Wagner [Wa88] proves, for $n\geq 3$, the existence of such polynomials with
>
> $$\lvert\{ z: \lvert p(z)\rvert <1\}\rvert \ll_\epsilon (\log\log n)^{-1/2+\epsilon}$$
>
> for all $\epsilon>0$. Krishnapur, Lundberg, and Ramachandran [KLR25] improved this upper bound to
> $\ll (\log\log n)^{-1}$.
>
> Pólya [Po28] showed the upper bound $\lvert\{ z: \lvert p(z)\rvert <1\}\rvert \leq \pi$ always
> holds, and this is achieved only when the $z_i$ are identical.

```lean
theorem erdos_116 : ∃ c : ℝ, 0 < c ∧ ∃ C : ℕ, ∀ n : ℕ, 0 < n →
    ∀ z : Fin n → ℂ, (∀ i, ‖z i‖ ≤ 1) →
      ENNReal.ofReal (c / n ^ C) ≤ volume {w : ℂ | ‖∏ i, (w - z i)‖ < 1}
```

Category `research solved`; AMS [30 Functions of a complex variable](../../../by-subject/part-01/30-functions-of-a-complex-variable/README.md). Declared in [FormalConjectures/ErdosProblems/116.lean, line 70](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/116.lean#L70).

## `Erdos116.erdos_116.variants.log`

Solved: stated here without proof.

> The lower bound $\lvert\{ z: \lvert p(z)\rvert <1\}\rvert \gg (\log n)^{-1}$ was proved by
> Krishnapur, Lundberg, and Ramachandran [KLR25]; in particular the answer to the $(\log n)^{-O(1)}$
> form of the question is also yes.

```lean
theorem erdos_116.variants.log : ∃ c : ℝ, 0 < c ∧ ∀ n : ℕ, 2 ≤ n →
    ∀ z : Fin n → ℂ, (∀ i, ‖z i‖ ≤ 1) →
      ENNReal.ofReal (c / Real.log n) ≤ volume {w : ℂ | ‖∏ i, (w - z i)‖ < 1}
```

Category `research solved`; AMS [30 Functions of a complex variable](../../../by-subject/part-01/30-functions-of-a-complex-variable/README.md). Declared in [FormalConjectures/ErdosProblems/116.lean, line 81](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/116.lean#L81).

## `Erdos116.erdos_116.variants.upper`

Solved: stated here without proof.

> Krishnapur, Lundberg, and Ramachandran [KLR25] proved that there are polynomials with
> $\lvert\{ z: \lvert p(z)\rvert <1\}\rvert \ll (\log\log n)^{-1}$, improving a result of Wagner
> [Wa88].

```lean
theorem erdos_116.variants.upper : ∃ C : ℝ, ∀ n : ℕ, 3 ≤ n →
    ∃ z : Fin n → ℂ, (∀ i, ‖z i‖ ≤ 1) ∧
      volume {w : ℂ | ‖∏ i, (w - z i)‖ < 1} ≤ ENNReal.ofReal (C / Real.log (Real.log n))
```

Category `research solved`; AMS [30 Functions of a complex variable](../../../by-subject/part-01/30-functions-of-a-complex-variable/README.md). Declared in [FormalConjectures/ErdosProblems/116.lean, line 92](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/116.lean#L92).

## `Erdos116.erdos_116.variants.polya`

Solved: stated here without proof.

> Pólya [Po28]: $\lvert\{ z: \lvert p(z)\rvert <1\}\rvert \leq \pi$ always holds.

```lean
theorem erdos_116.variants.polya (n : ℕ) (z : Fin n → ℂ) :
    volume {w : ℂ | ‖∏ i, (w - z i)‖ < 1} ≤ ENNReal.ofReal Real.pi
```

Category `research solved`; AMS [30 Functions of a complex variable](../../../by-subject/part-01/30-functions-of-a-complex-variable/README.md). Declared in [FormalConjectures/ErdosProblems/116.lean, line 99](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/116.lean#L99).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/116.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/116.lean)
- [erdosproblems.com/116](https://www.erdosproblems.com/116)
