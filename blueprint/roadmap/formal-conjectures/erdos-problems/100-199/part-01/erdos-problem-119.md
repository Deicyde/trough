---
declaration: theorem
origin: cited
lean: Erdos119.erdos_119.parts.i, Erdos119.erdos_119.parts.ii, Erdos119.erdos_119.parts.iii
statement: formalized
---

# Erdős Problem 119

> *References:*
> - [erdosproblems.com/119](https://www.erdosproblems.com/119)
> - [Be91] Beck, J., The modulus of polynomials with zeros on the unit circle: A problem of Erdős.
>   Annals of Math. (1991), 609-651.
> - [Er57] Erdős, Paul, Some unsolved problems. Michigan Math. J. (1957), 291-300.
> - [Er61] Erdős, Paul, Some unsolved problems. Magyar Tud. Akad. Mat. Kutató Int. Közl. (1961),
>   221-254.
> - [Er64b] Erdős, P., Problems and results on diophantine approximations. Compositio Math. (1964),
>   52-65.
> - [Er82e] Erdős, Paul, Some of my favourite problems which recently have been solved. (1982), 59--79.
> - [Er90] Erdős, Paul, Some of my favourite unsolved problems. A tribute to Paul Erdős (1990),
>   467-478.
> - [Er97f] Erdős, Paul, Some unsolved problems. Combinatorics, geometry and probability (Cambridge,
>   1993) (1997), 1-10.
> - [Ha74] Hayman, W. K., Research problems in function theory: new problems. (1974), 155--180.
> - [Li77] Linden, C. N., The modulus of polynomials with zeros on the unit circle. Bull. London Math.
>   Soc. (1977), 65--69.
> - [Va99] Various, Some of Paul's favorite problems. Booklet produced for the conference "Paul Erdős
>   and his mathematics", Budapest, July 1999 (1999).
> - [Wa80] Wagner, Gerold, On a problem of Erdős in {D}iophantine approximation. Bull. London Math.
>   Soc. (1980), 81--88.

*Quoted from [FormalConjectures/ErdosProblems/119.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/119.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/119](https://www.erdosproblems.com/119).

The file states 3 research or textbook statements: 3 solved.

## `Erdos119.erdos_119.parts.i`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/1268917deaaaa0d674f651287027baa26cea9920/src/latest/ErdosProblems/Erdos119.lean#L1759](https://github.com/plby/lean-proofs/blob/1268917deaaaa0d674f651287027baa26cea9920/src/latest/ErdosProblems/Erdos119.lean#L1759).

> Is it true that $\limsup M_n = \infty$?
>
> This is Problem 4.1 in [Ha74] where it is attributed to Erdős.
>
> The weaker conjecture that $\limsup M_n=\infty$ was proved by Wagner [Wa80], who show that there is
> some $c>0$ with $M_n>(\log n)^c$ infinitely often.

```lean
theorem erdos_119.parts.i :
    ∀ (z : ℕ → ℂ) (hz : ∀ i : ℕ, ‖z i‖ = 1),
      atTop.limsup (fun n => (M z n : EReal)) = ⊤
```

Category `research solved`; AMS [30 Functions of a complex variable](../../../by-subject/part-01/30-functions-of-a-complex-variable/README.md). Declared in [FormalConjectures/ErdosProblems/119.lean, line 77](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/119.lean#L77).

## `Erdos119.erdos_119.parts.ii`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/1268917deaaaa0d674f651287027baa26cea9920/src/latest/ErdosProblems/Erdos119.lean#L1712](https://github.com/plby/lean-proofs/blob/1268917deaaaa0d674f651287027baa26cea9920/src/latest/ErdosProblems/Erdos119.lean#L1712).

> Is it true that there exists $c > 0$ such that for infinitely many $n$ we have $M_n > n^c$?
>
> The second question was answered by Beck [Be91], who proved that there exists some $c>0$ such that
> $\max_{n\leq N} M_n > N^c$.

```lean
theorem erdos_119.parts.ii :
    ∀ (z : ℕ → ℂ) (hz : ∀ i : ℕ, ‖z i‖ = 1),
      ∃ (c : ℝ) (hc : c > 0), Infinite {n : ℕ | M z n > n ^ c}
```

Category `research solved`; AMS [30 Functions of a complex variable](../../../by-subject/part-01/30-functions-of-a-complex-variable/README.md). Declared in [FormalConjectures/ErdosProblems/119.lean, line 90](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/119.lean#L90).

## `Erdos119.erdos_119.parts.iii`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/1268917deaaaa0d674f651287027baa26cea9920/src/latest/ErdosProblems/Erdos119.lean#L1687](https://github.com/plby/lean-proofs/blob/1268917deaaaa0d674f651287027baa26cea9920/src/latest/ErdosProblems/Erdos119.lean#L1687).

> Is it true that there exists $c > 0$ such that, for all large $n$, $\sum_{k \leq n} M_k > n^{1 + c}$?
>
> The \$100 prize was offered for the third question in [Er97f]. This was resolved by GPT 5.6 and
> Korsky (see the proof claims), who proved that $\sum_{k\leq n}M_k \gg \frac{n^{5/4}}{\sqrt{\log n}}$
> (and hence for infinitely many $n$ we have $M_n> n^{1/4-o(1)}$).

```lean
theorem erdos_119.parts.iii :
    ∀ (z : ℕ → ℂ) (hz : ∀ i : ℕ, ‖z i‖ = 1),
      ∃ (c : ℝ) (hc : c > 0), ∀ᶠ n in atTop,
        ∑ k ∈ range n, M z k > n ^ (1 + c)
```

Category `research solved`; AMS [30 Functions of a complex variable](../../../by-subject/part-01/30-functions-of-a-complex-variable/README.md). Declared in [FormalConjectures/ErdosProblems/119.lean, line 104](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/119.lean#L104).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/119.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/119.lean)
- [erdosproblems.com/119](https://www.erdosproblems.com/119)
