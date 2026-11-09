---
declaration: theorem
origin: cited
lean: Erdos18.factorial_isPractical, Erdos18.erdos_18a, Erdos18.erdos_18b, Erdos18.erdos_18c, Erdos18.erdos_18_upper_bound, Erdos18.erdos_18_vose
statement: formalized
---

# Erdős Problem 18

> *Reference:*
> * [erdosproblems.com/18](https://www.erdosproblems.com/18)
> * [ErGr80] Erdős, P. and Graham, R. L. (1980). Old and New Problems and Results in Combinatorial Number
> Theory. Monographies de L'Enseignement Mathématique, 28. Université de Genève. (See the
> sections on Egyptian fractions or practical numbers).
> * [Vo85] Vose, Michael D., Egyptian fractions. Bull. London Math. Soc. (1985), 21-24.

*Quoted from [FormalConjectures/ErdosProblems/18.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/18.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/18](https://www.erdosproblems.com/18).

The file states 6 research or textbook statements: 3 open, 2 solved and 1 textbook result. It also has 7 test statements, counted here but not shown.

## `Erdos18.factorial_isPractical`

Textbook result, proved here.

> $h(n!)$ is well-defined since $n!$ is practical for $n ≥ 1$.

```lean
theorem factorial_isPractical (n : ℕ) : Nat.IsPractical n.factorial
```

Category `textbook`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/18.lean, line 182](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/18.lean#L182).

## `Erdos18.erdos_18a`

Open: stated without proof.

> **Conjecture 1.**
> Are there infinitely many practical numbers $m$ such that $h(m) < (\log \log m)^{O(1)}$?
>
> More precisely: does there exist a constant $C > 0$ such that for infinitely many
> practical numbers $m$, we have $h(m) < (\log \log m)^C$?

```lean
theorem erdos_18a :
    ∃ C : ℝ, 0 < C ∧ ∃ᶠ m in atTop, Nat.IsPractical m ∧
      (practicalH m : ℝ) < (log (log m)) ^ C
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/18.lean, line 234](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/18.lean#L234).

## `Erdos18.erdos_18b`

Open: stated without proof.

> **Conjecture 2.**
> Is it true that $h(n!) < n^{o(1)}$? That is, for all $\varepsilon > 0$,
> is $h(n!) < n^\varepsilon$ for sufficiently large $n$?

```lean
theorem erdos_18b :
    ∀ ε : ℝ, 0 < ε → ∀ᶠ n : ℕ in atTop, (practicalH n.factorial : ℝ) < (n : ℝ) ^ ε
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/18.lean, line 245](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/18.lean#L245).

## `Erdos18.erdos_18c`

Open: stated without proof.

> **Conjecture 3.**
> Or perhaps even $h(n!) < (\log n)^{O(1)}$?
>
> Erdős offered \$250 for a proof or disproof.

```lean
theorem erdos_18c :
    ∃ C : ℝ, 0 < C ∧ ∀ᶠ n : ℕ in atTop, (practicalH n.factorial : ℝ) < (log n) ^ C
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/18.lean, line 256](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/18.lean#L256).

## `Erdos18.erdos_18_upper_bound`

Solved: stated here; a Lean proof is at [https://github.com/linrock/math-proofs/blob/b246a4165f55ada0614aa2b85c8bc6381522e808/erdos-18/Solution.lean#L31](https://github.com/linrock/math-proofs/blob/b246a4165f55ada0614aa2b85c8bc6381522e808/erdos-18/Solution.lean#L31).

> **Erdős's Theorem.**
> Erdős proved that $h(n!) < n$ for all $n \ge 1$.

```lean
theorem erdos_18_upper_bound :
    ∀ᶠ n : ℕ in atTop, practicalH (Nat.factorial n) < n
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/18.lean, line 267](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/18.lean#L267).

## `Erdos18.erdos_18_vose`

Solved: stated here without proof.

> **Vose's Theorem.**
> Vose proved the existence of infinitely many practical numbers $m$ such that
> $h(m) \ll (\log m)^{1/2}$. This gives a positive answer to a weaker form of Conjecture 1.

```lean
theorem erdos_18_vose :
    ∃ C : ℝ, 0 < C ∧ ∃ᶠ m in atTop, Nat.IsPractical m ∧
      (practicalH m : ℝ) < C * (log m) ^ (1 / 2 : ℝ)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/18.lean, line 277](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/18.lean#L277).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/18.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/18.lean)
- [erdosproblems.com/18](https://www.erdosproblems.com/18)
