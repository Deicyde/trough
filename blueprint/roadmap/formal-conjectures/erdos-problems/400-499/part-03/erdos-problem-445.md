---
declaration: theorem
origin: cited
lean: Erdos445.erdos_445, Erdos445.erdos_445.variants.heilbronn, Erdos445.erdos_445.variants.heath_brown
statement: formalized
---

# Erdős Problem 445

> *References:*
> - [erdosproblems.com/445](https://www.erdosproblems.com/445)
> - [He00] Heath-Brown, D. R., Arithmetic applications of {K}loosterman sums. Nieuw Arch. Wiskd. (5)
>   (2000), 380--384.
> - [MathOverflow](https://mathoverflow.net/questions/69509/small-residue-classes-with-small-reciprocal)

*Quoted from [FormalConjectures/ErdosProblems/445.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/445.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/445](https://www.erdosproblems.com/445).

The file states 3 research or textbook statements: 1 open and 2 solved. It also has 1 test statement, counted here but not shown.

## `Erdos445.erdos_445`

Open: stated without proof.

> Is it true that, for any $c>1/2$, if $p$ is a sufficiently large prime then, for any
> $n\geq 0$, there exist $a,b\in(n,n+p^c)$ such that $ab\equiv 1\pmod{p}$?
>
> This is discussed in this MathOverflow question [MathOverflow].

```lean
theorem erdos_445 :
    ∀ c : ℝ, c > 1 / 2 →
      ∀ᶠ p : ℕ in atTop, p.Prime → ∀ n : ℕ, Erdos445Prop c p n
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/445.lean, line 53](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/445.lean#L53).

## `Erdos445.erdos_445.variants.heilbronn`

Solved: stated here without proof.

> Heilbronn (unpublished) proved this for $c$ sufficiently close to $1$.

```lean
theorem erdos_445.variants.heilbronn :
    ∃ c₀ < 1, ∀ c : ℝ, c > c₀ →
      ∀ᶠ p : ℕ in atTop, p.Prime → ∀ n : ℕ, Erdos445Prop c p n
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/445.lean, line 62](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/445.lean#L62).

## `Erdos445.erdos_445.variants.heath_brown`

Solved: stated here without proof.

> Heath-Brown [He00] used Kloosterman sums to prove this for all $c>3/4$.

```lean
theorem erdos_445.variants.heath_brown :
    ∀ c : ℝ, c > 3 / 4 →
      ∀ᶠ p : ℕ in atTop, p.Prime → ∀ n : ℕ, Erdos445Prop c p n
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/445.lean, line 71](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/445.lean#L71).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/445.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/445.lean)
- [erdosproblems.com/445](https://www.erdosproblems.com/445)
