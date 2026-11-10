---
declaration: theorem
origin: cited
lean: Erdos346.erdos_346, Erdos346.erdos_346.variants.f_isAddStronglyCompleteNatSeq, Erdos346.erdos_346.variants.f_not_isAddComplete, Erdos346.erdos_346.variants.gt_goldenRatio_not_IsAddComplete, Erdos346.erdos_346.variants.example
statement: formalized
---

# Erdős Problem 346

> *References:*
>  - [erdosproblems.com/346](https://www.erdosproblems.com/346)
>  - [Gr64d] Graham, R. L., A property of Fibonacci numbers. Fibonacci Quart. (1964), 1-10.
>  - [ErGr80] Erdős, P. and Graham, R., Old and new problems and results in combinatorial number
>     theory. Monographies de L'Enseignement Mathematique (1980).
>  -

*Quoted from [FormalConjectures/ErdosProblems/346.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/346.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/346](https://www.erdosproblems.com/346).

The file states 5 research or textbook statements: 5 solved. It also has 1 test statement and 3 API statements, counted here but not shown.

## `Erdos346.erdos_346`

Solved: stated here without proof.

> Is it true that for every lacunary, strongly complete sequence `A` that is not complete whenever
> infinitely many terms are removed from it, `lim A (n + 1) / A n = (1 + √5) / 2`?
>
> The answer is no. A counterexample recorded at [erdosproblems.com/346] has all successive ratios
> at least `6 / 5`, but has subsequences of successive ratios tending to two different limits,
> `(1 + √5) / 2` and `(1 + √5) / 2 + 1 / 4`.

```lean
theorem erdos_346 : ¬ ∀ {A : ℕ → ℕ}, IsLacunary A → IsAddStronglyCompleteNatSeq A →
    (∀ B : Set ℕ, B ⊆ range A → B.Infinite → ¬ IsAddComplete (range A \ B)) →
    Tendsto (fun n => A (n + 1) / (A n : ℝ)) atTop (𝓝 ((1 + √5) / 2))
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/346.lean, line 45](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/346.lean#L45).

## `Erdos346.erdos_346.variants.f_isAddStronglyCompleteNatSeq`

Solved: stated here without proof.

> The sequence `f` is strongly complete, and this is proved in [Gr64d].

```lean
theorem erdos_346.variants.f_isAddStronglyCompleteNatSeq : IsAddStronglyCompleteNatSeq f
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/346.lean, line 87](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/346.lean#L87).

## `Erdos346.erdos_346.variants.f_not_isAddComplete`

Proved here.

> The sequence `f` is not complete whenever infinitely many terms are removed from it, and this
> is proved in [Gr64d].

```lean
theorem erdos_346.variants.f_not_isAddComplete {B : Set ℕ} (h : B ⊆ range f) (hB : B.Infinite) :
    ¬ IsAddComplete (range f \ B)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/346.lean, line 151](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/346.lean#L151).

## `Erdos346.erdos_346.variants.gt_goldenRatio_not_IsAddComplete`

Proved here.

> Erdős and Graham [ErGr80] remark that it is easy to see that if `A (n + 1) / A n > (1 + √5) / 2`
> then the second property is automatically satisfied.

```lean
theorem erdos_346.variants.gt_goldenRatio_not_IsAddComplete {A : ℕ → ℕ}
    (hA : ∀ n, (1 + √5) / 2 * A n < A (n + 1)) {B : Set ℕ} (h : B ⊆ range A) (hB : B.Infinite) :
    ¬ IsAddComplete (range A \ B)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/346.lean, line 159](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/346.lean#L159).

## `Erdos346.erdos_346.variants.example`

Solved: stated here without proof.

> Erdős and Graham [ErGr80] also say that it is not hard to construct very irregular sequences
> satisfying the aforementioned properties: there is a strictly increasing sequence `A` that is
> strongly complete and not complete whenever infinitely many terms are removed from it, but with
> $\liminf_n A(n+1)/A(n) = 1$ and $\limsup_n A(n+1)/A(n) = \infty$.

```lean
theorem erdos_346.variants.example : ∃ A : ℕ → ℕ, StrictMono A ∧ IsAddStronglyCompleteNatSeq A ∧
    (∀ B : Set ℕ, B ⊆ range A → B.Infinite → ¬ IsAddComplete (range A \ B)) ∧
    liminf (fun n => A (n + 1) / (A n : ℝ)) atTop = 1 ∧
    limsup (fun n => A (n + 1) / (A n : ENNReal)) atTop = ⊤
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/346.lean, line 194](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/346.lean#L194).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/346.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/346.lean)
- [erdosproblems.com/346](https://www.erdosproblems.com/346)
