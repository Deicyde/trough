---
declaration: theorem
origin: cited
lean: Erdos512.erdos_512
statement: formalized
---

# Erdős Problem 512

> *References:*
> - [erdosproblems.com/512](https://www.erdosproblems.com/512)
> - [Er61] Erdős, Paul, *Some unsolved problems*. Magyar Tud. Akad. Mat. Kutató Int. Közl.
>   (1961), 221-254.
> - [Ko81] Konyagin, S. V., *On the Littlewood problem*. Izv. Akad. Nauk SSSR Ser. Mat. (1981),
>   243-265, 463.
> - [MPS81] McGehee, O. Carruth and Pigno, Louis and Smith, Brent, *Hardy's inequality and the
>   $L^1$ norm of exponential sums*. Ann. of Math. (2) (1981), 613-618.

*Quoted from [FormalConjectures/ErdosProblems/512.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/512.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/512](https://www.erdosproblems.com/512).

The file states 1 research or textbook statement: 1 solved.

## `Erdos512.erdos_512`

Solved: stated here; a Lean proof is at [https://github.com/Jayyhk/erdos-lean/blob/f8a51976fd2e66a52b4928c109fb9ae877a1a507/problems/512/Erdos512.lean](https://github.com/Jayyhk/erdos-lean/blob/f8a51976fd2e66a52b4928c109fb9ae877a1a507/problems/512/Erdos512.lean).

> Is it true that, if $A\subset \mathbb{Z}$ is a finite set of size $N$, then
> $$\int_0^1 \left\lvert \sum_{n\in A}e(n\theta)\right\rvert \mathrm{d}\theta \gg \log N,$$
> where $e(x)=e^{2\pi ix }$?
>
> Littlewood's conjecture, proved independently by Konyagin [Ko81] and McGehee, Pigno, and
> Smith [MPS81].

```lean
theorem erdos_512 :
    ∃ c > (0 : ℝ), ∀ (N : ℕ) (A : Finset ℤ), A.card = N →
      c * Real.log N ≤ ∫ θ in (0 : ℝ)..1, ‖∑ n ∈ A, e (n * θ)‖
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md), [42 Harmonic analysis on Euclidean spaces](../../../by-subject/part-02/42-harmonic-analysis-on-euclidean-spaces/README.md). Declared in [FormalConjectures/ErdosProblems/512.lean, line 49](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/512.lean#L49).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/512.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/512.lean)
- [erdosproblems.com/512](https://www.erdosproblems.com/512)
