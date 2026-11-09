---
declaration: theorem
origin: cited
lean: Erdos724.erdos_724, Erdos724.erdos_724.variants.euler_conjecture, Erdos724.erdos_724.variants.bose_parker_shrikhande, Erdos724.erdos_724.variants.chowla_erdos_straus, Erdos724.erdos_724.variants.wilson, Erdos724.erdos_724.variants.beth, Erdos724.erdos_724.variants.le_sub_one
statement: formalized
---

# Erdős Problem 724

> *References:*
> - [erdosproblems.com/724](https://www.erdosproblems.com/724)
> - [OEIS A001438](https://oeis.org/A001438)
> - [Be83c] Beth, Thomas, *Eine Bemerkung zur Abschätzung der Anzahl orthogonaler lateinischer
>   Quadrate mittels Siebverfahren*. Abh. Math. Sem. Univ. Hamburg (1983), 284-288.
> - [BPS60] Bose, R. C. and Shrikhande, S. S. and Parker, E. T., *Further results on the
>   construction of mutually orthogonal Latin squares and the falsity of Euler's conjecture*.
>   Canadian J. Math. (1960), 189-203.
> - [CES60] Chowla, S. and Erdős, P. and Straus, E. G., *On the maximal number of pairwise
>   orthogonal Latin squares of a given order*. Canadian J. Math. (1960), 204-208.
> - [Er81] Erdős, P., *On the combinatorial problems which I would most like to see solved*.
>   Combinatorica (1981), 25-42.
> - [Wi74] Wilson, Richard M., *Concerning the number of mutually orthogonal Latin squares*.
>   Discrete Math. (1974), 181-198.

*Quoted from [FormalConjectures/ErdosProblems/724.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/724.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/724](https://www.erdosproblems.com/724).

The file states 7 research or textbook statements: 1 open, 5 solved and 1 textbook result.

## `Erdos724.erdos_724`

Open: stated without proof.

> Let $f(n)$ be the maximum number of mutually orthogonal Latin squares of order $n$. Is it true
> that
>
> $$f(n) \gg n^{1/2}?$$
>
> This question is from [Er81].

```lean
theorem erdos_724 :
    ∃ c > (0 : ℝ), ∀ᶠ n : ℕ in atTop, c * Real.sqrt (n : ℝ) ≤ (maxMOLS n : ℝ)
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/724.lean, line 69](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/724.lean#L69).

## `Erdos724.erdos_724.variants.euler_conjecture`

Solved: stated here without proof.

> Euler conjectured that $f(n) = 1$ when $n \equiv 2 \pmod{4}$. This is false: Bose, Parker, and
> Shrikhande [BPS60] proved $f(n) \geq 2$ for $n \geq 7$, so for example $f(10) \geq 2$.

```lean
theorem erdos_724.variants.euler_conjecture :
    ¬ ∀ n : ℕ, n ≡ 2 [MOD 4] → maxMOLS n = 1
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/724.lean, line 78](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/724.lean#L78).

## `Erdos724.erdos_724.variants.bose_parker_shrikhande`

Solved: stated here without proof.

> Bose, Parker, and Shrikhande [BPS60] proved that $f(n) \geq 2$ for all $n \geq 7$.

```lean
theorem erdos_724.variants.bose_parker_shrikhande :
    ∀ n : ℕ, 7 ≤ n → 2 ≤ maxMOLS n
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/724.lean, line 86](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/724.lean#L86).

## `Erdos724.erdos_724.variants.chowla_erdos_straus`

Solved: stated here without proof.

> Chowla, Erdős, and Straus [CES60] proved that
>
> $$f(n) \gg n^{1/91}.$$

```lean
theorem erdos_724.variants.chowla_erdos_straus :
    ∃ c > (0 : ℝ), ∀ᶠ n : ℕ in atTop,
      c * (n : ℝ) ^ ((1 : ℝ) / 91) ≤ (maxMOLS n : ℝ)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/724.lean, line 95](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/724.lean#L95).

## `Erdos724.erdos_724.variants.wilson`

Solved: stated here without proof.

> Wilson [Wi74] proved that
>
> $$f(n) \gg n^{1/17}.$$

```lean
theorem erdos_724.variants.wilson :
    ∃ c > (0 : ℝ), ∀ᶠ n : ℕ in atTop,
      c * (n : ℝ) ^ ((1 : ℝ) / 17) ≤ (maxMOLS n : ℝ)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/724.lean, line 105](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/724.lean#L105).

## `Erdos724.erdos_724.variants.beth`

Solved: stated here without proof.

> Beth [Be83c] proved that
>
> $$f(n) \gg n^{1/14.8}.$$

```lean
theorem erdos_724.variants.beth :
    ∃ c > (0 : ℝ), ∀ᶠ n : ℕ in atTop,
      c * (n : ℝ) ^ ((1 : ℝ) / 14.8) ≤ (maxMOLS n : ℝ)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/724.lean, line 115](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/724.lean#L115).

## `Erdos724.erdos_724.variants.le_sub_one`

Textbook result, proved here.

> For $n \geq 2$ there are at most $n - 1$ mutually orthogonal Latin squares of order $n$:
>
> $$f(n) \leq n - 1.$$
>
> This is classical; see OEIS A001438.

```lean
theorem erdos_724.variants.le_sub_one :
    ∀ n : ℕ, 2 ≤ n → maxMOLS n ≤ n - 1
```

Category `textbook`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/724.lean, line 126](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/724.lean#L126).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/724.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/724.lean)
- [erdosproblems.com/724](https://www.erdosproblems.com/724)
