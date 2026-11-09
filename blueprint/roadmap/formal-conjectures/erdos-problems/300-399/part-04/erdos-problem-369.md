---
declaration: theorem
origin: cited
lean: Erdos369.erdos_369
statement: formalized
---

# Erdős Problem 369

> *References:*
> - [erdosproblems.com/369](https://www.erdosproblems.com/369)
> - [ErGr80] Erdős, P. and Graham, R., *Old and new problems and results in combinatorial number
>   theory*. Monographies de L'Enseignement Mathematique (1980).
> - [EgSe76] Eggleton, R. B. and Selfridge, J. L., *Consecutive integers with no large prime factors*.
>   J. Austral. Math. Soc. Ser. A (1976), 1--11.
> - [BFMW20] Bober, J. W. and Fretwell, D. and Martin, G. and Wooley, T. D., *Smooth values of
>   polynomials*. J. Aust. Math. Soc. (2020), 245--261.
> - [BaWo98] Balog, Antal and Wooley, Trevor D., *On strings of consecutive integers with no large
>   prime factors*. J. Austral. Math. Soc. Ser. A (1998), 266-276.

*Quoted from [FormalConjectures/ErdosProblems/369.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/369.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/369](https://www.erdosproblems.com/369).

The file states 1 research or textbook statement: 1 solved.

## `Erdos369.erdos_369`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/1d7b3f00780b85ed0462e79a1cd5650ee9055655/src/v4.29.1/ErdosProblems/Erdos369.lean](https://github.com/plby/lean-proofs/blob/1d7b3f00780b85ed0462e79a1cd5650ee9055655/src/v4.29.1/ErdosProblems/Erdos369.lean).

> Let $\epsilon>0$ and $k\geq 2$. Is it true that, for all sufficiently large $n$, there is a
> sequence of $k$ consecutive integers in $\{1,\ldots,n\}$ all of which are $n^\epsilon$-smooth?
>
> The problem is trivially true as written (simply taking $\{1,\ldots,k\}$ and $n>k^{1/\epsilon}$).
> There are (at least) two possible variants which are non-trivial, and it is not clear which
> Erdős and Graham meant. We formalize the second: each $m\in P$ (where $P$ is the sequence of $k$
> consecutive integers sought for) must be in $[n/2,n]$. In this case a positive answer also
> follows directly from the result of Balog and Wooley [BaWo98] for infinitely many $n$. Proving
> this is true for all large $n$ does not follow immediately from [BaWo98], but can be deduced
> using a similar construction, as shown by SkyYang.

```lean
theorem erdos_369 :
    ∀ (ε : ℝ) (hε : 0 < ε) (k : ℕ) (hk : 2 ≤ k),
      ∀ᶠ (n : ℕ) in atTop, ∃ a : ℕ, n / 2 ≤ a + 1 ∧ a + k ≤ n ∧
        ∀ j < k, ∀ p ∈ (a + 1 + j).primeFactors, (p : ℝ) ≤ (n : ℝ) ^ ε
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/369.lean, line 55](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/369.lean#L55).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/369.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/369.lean)
- [erdosproblems.com/369](https://www.erdosproblems.com/369)
