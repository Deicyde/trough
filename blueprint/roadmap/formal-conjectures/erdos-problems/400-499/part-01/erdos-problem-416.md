---
declaration: theorem
origin: cited
lean: Erdos416.erdos_416.parts.i, Erdos416.erdos_416.variants.regularly_varying, Erdos416.erdos_416.parts.ii, Erdos416.erdos_416.variants.Pillai, Erdos416.erdos_416.variants.Erdos, Erdos416.erdos_416.variants.Maier_Pomerance, Erdos416.erdos_416.variants.Ford
statement: formalized
---

# Erdős Problem 416

> *References:*
> - [erdosproblems.com/416](https://www.erdosproblems.com/416)
> - [OAI26a] OpenAI, *An asymptotic formula for the number of totients*. OpenAI Math Release
>   preprint (2026).
>   https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/An-asymptotic-formula-for-the-number-of-totients-September-25-2026/An-asymptotic-formula-for-the-number-of-totients-September-25-2026.pdf

*Quoted from [FormalConjectures/ErdosProblems/416.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/416.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/416](https://www.erdosproblems.com/416).

The file states 7 research or textbook statements: 1 open and 6 solved.

## `Erdos416.erdos_416.parts.i`

Solved: stated here; a Lean proof is at [https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/OAI/NumberTheory/TotientAsymptotic/UnconditionalMain.lean#L12](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/OAI/NumberTheory/TotientAsymptotic/UnconditionalMain.lean#L12).

> Let `V(x)` count the number of `n≤x` such that `ϕ(m)=n` is solvable. Does `V(2x)/V(x)→2` ?
>
> Yes. This was proved by an internal OpenAI model in September 2026 [OAI26a]; see the linked
> Lean proof, which gives `V(cx)/V(x)→c` for every fixed `c>0`.

```lean
theorem erdos_416.parts.i :
    Filter.Tendsto (fun x => (V (2 * x) / V (x))) Filter.atTop (𝓝 2)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/416.lean, line 51](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/416.lean#L51).

## `Erdos416.erdos_416.variants.regularly_varying`

Solved: stated here; a Lean proof is at [https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/OAI/NumberTheory/TotientAsymptotic/UnconditionalMain.lean#L12](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/OAI/NumberTheory/TotientAsymptotic/UnconditionalMain.lean#L12).

> Let `V(x)` count the number of `n≤x` such that `ϕ(m)=n` is solvable. Then `V(cx)/V(x)→c` for
> every fixed `c>0`, which answers a question of Erdős and Hall. This was proved by an internal
> OpenAI model in September 2026 [OAI26a]; see the linked Lean proof.

```lean
theorem erdos_416.variants.regularly_varying (c : ℝ) (hc : 0 < c) :
    Filter.Tendsto (fun x => V (c * x) / V x) Filter.atTop (𝓝 c)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/416.lean, line 63](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/416.lean#L63).

## `Erdos416.erdos_416.parts.ii`

Open: stated without proof.

> Let `V(x)` count the number of `n≤x` such that `ϕ(m)=n` is solvable.
> Is there an asymptotic formula for `V(x)`?

```lean
theorem erdos_416.parts.ii :
    Filter.Tendsto (fun x => V x / erdos_416.parts.ii.answer x) atTop (𝓝 1)
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/416.lean, line 74](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/416.lean#L74).

## `Erdos416.erdos_416.variants.Pillai`

Solved: stated here without proof.

> Let `V(x)` count the number of `n≤x` such that `ϕ(m)=n` is solvable.
> Pillai proved `V(x)=o(x)`.
> Ref: S. Sivasankaranarayana Pillai, _On some functions connected with $\phi(n)$_

```lean
theorem erdos_416.variants.Pillai : V =o[atTop] id
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/416.lean, line 84](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/416.lean#L84).

## `Erdos416.erdos_416.variants.Erdos`

Solved: stated here without proof.

> Let `V(x)` count the number of `n≤x` such that `ϕ(m)=n` is solvable.
> Erdős proved V(x)=x(logx)^(−1+o(1)).
> Ref: Erdős, P., _On the normal number of prime factors of $p-1$ and some related problems concerning Euler's $\varphi$-function._

```lean
theorem erdos_416.variants.Erdos : ∃ f : ℝ → ℝ, f =o[atTop] (1 : ℝ → ℝ) ∧
    ∀ᶠ x in Filter.atTop, V x = x * x.log ^ (-1 + f x)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/416.lean, line 93](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/416.lean#L93).

## `Erdos416.erdos_416.variants.Maier_Pomerance`

Solved: stated here without proof.

> Let `V(x)` count the number of `n≤x` such that `ϕ(m)=n` is solvable.
> `V(x)=x/logx * e^((C+o(1))(log log log x)^2)`, for some explicit constant `C>0`.
> Ref:Maier, Helmut and Pomerance, Carl, _On the number of distinct values of Euler's $\phi$-function_.

```lean
theorem erdos_416.variants.Maier_Pomerance :
    0 < erdos_416.variants.Maier_Pomerance.answer ∧ ∃ f : ℝ → ℝ, f =o[atTop] (1 : ℝ → ℝ) ∧
      ∀ᶠ x in Filter.atTop, (V x : ℝ) = x / x.log *
        (rexp <| (erdos_416.variants.Maier_Pomerance.answer + f x) * x.log.log.log ^ 2)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/416.lean, line 106](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/416.lean#L106).

## `Erdos416.erdos_416.variants.Ford`

Solved: stated here without proof.

> Let `V(x)` count the number of `n≤x` such that `ϕ(m)=n` is solvable.
> `V(x) ≍ x/log x*e^(C_1*(log log log x − log log log log x)^2+C_2 log log log x − C_3 log log log log x)`
> Ref: Ford, Kevin, _The distribution of totients_.

```lean
theorem erdos_416.variants.Ford :
    let (C₁, C₂, C₃) : ℝ × ℝ × ℝ := erdos_416.variants.Ford.answer
    0 < C₁ ∧ 0 < C₂ ∧ 0 < C₃ ∧
    let G (x : ℝ) : ℝ := x / x.log * (rexp <| C₁ * (x.log.log.log - x.log.log.log.log) ^ 2
        + C₂* x.log.log.log - C₃ * x.log.log.log.log)
    V =Θ[atTop] G
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/416.lean, line 121](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/416.lean#L121).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/416.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/416.lean)
- [erdosproblems.com/416](https://www.erdosproblems.com/416)
