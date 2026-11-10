---
declaration: theorem
origin: cited
lean: Erdos263.erdos_263.parts.i, Erdos263.erdos_263.parts.ii, Erdos263.erdos_263.variants.folklore, Erdos263.erdos_263.variants.sub_doubly_exponential, Erdos263.erdos_263.variants.super_doubly_exponential, Erdos263.erdos_263.variants.super_doubly_exponential_eventual, Erdos263.erdos_263.variants.doubly_exponential_all_but_countable
statement: formalized
---

# Erdős Problem 263

> *Reference:* [erdosproblems.com/263](https://www.erdosproblems.com/263)

*Quoted from [FormalConjectures/ErdosProblems/263.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/263.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/263](https://www.erdosproblems.com/263).

The file states 7 research or textbook statements: 1 open and 6 solved.

## `Erdos263.erdos_263.parts.i`

Open: stated without proof.

> Is $a_n = 2^{2^n}$ an irrationality sequence in the above sense?

```lean
theorem erdos_263.parts.i : IsIrrationalitySequence (fun n : ℕ => 2 ^ 2 ^ n)
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/263.lean, line 67](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/263.lean#L67).

## `Erdos263.erdos_263.parts.ii`

Solved: stated here without proof.

> Must every irrationality sequence $a_n$ in the above sense
> satisfy $a_n^{1/n} \to \infty$ as $n \to \infty$?
>
> The answer is no. [Liam Price's construction](https://www.erdosproblems.com/forum/thread/263#post-6338)
> gives a strictly increasing irrationality sequence with $\liminf a_n^{1/n} = 1$.

```lean
theorem erdos_263.parts.ii :
    ¬ (∀ a : ℕ → ℕ,
      IsIrrationalitySequence a →
        atTop.Tendsto (fun n : ℕ => (a n : ℝ) ^ (1 / (n : ℝ))) atTop)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/263.lean, line 78](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/263.lean#L78).

## `Erdos263.erdos_263.variants.folklore`

Solved: stated here; a Lean proof is at [https://github.com/anatoliiohorodnyk/lean-fc-proofs/blob/5da9642575b26c2c816a49bcb56b33fed5456619/Proofs/T_Erdos263_erdos_263_variants_folklore.lean#L399](https://github.com/anatoliiohorodnyk/lean-fc-proofs/blob/5da9642575b26c2c816a49bcb56b33fed5456619/Proofs/T_Erdos263_erdos_263_variants_folklore.lean#L399).

> A folklore result states that any $a_n$ satisfying $\lim_{n \to \infty} a_n^{\frac{1}{2^n}} = \infty$
> has $\sum \frac{1}{a_n}$ converging to an irrational number.

```lean
theorem erdos_263.variants.folklore (a : ℕ -> ℕ)
    (ha : atTop.Tendsto (fun n : ℕ => (a n : ℝ) ^ (1 / (2 ^ n : ℝ))) atTop) :
    Irrational <| ∑' n, (1 : ℝ) / (a n : ℝ)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/263.lean, line 90](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/263.lean#L90).

## `Erdos263.erdos_263.variants.sub_doubly_exponential`

Solved: stated here without proof.

> Kovač and Tao [KoTa24] proved that any strictly increasing sequence $a_n$ such that
> $\sum \frac{1}{a_n}$ converges and $\lim \frac{a_{n+1}}{a_n^2} = 0$ is not
> an irrationality sequence in the above sense.
>
> [KoTa24] Kovač, V. and Tao T., On several irrationality problems for Ahmes series.
>          arXiv:2406.17593 (2024).

```lean
theorem erdos_263.variants.sub_doubly_exponential (a: ℕ -> ℕ)
    (ha' : StrictMono a)
    (ha'' : Summable (fun n : ℕ => 1 / (a n : ℝ)))
    (ha''' : atTop.Tendsto (fun n : ℕ => (a (n + 1) : ℝ) / a n ^ 2) (𝓝 0)) :
    ¬ IsIrrationalitySequence a
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/263.lean, line 104](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/263.lean#L104).

## `Erdos263.erdos_263.variants.super_doubly_exponential`

Solved: stated here; a Lean proof is at [https://github.com/arex1337/erdos-263-lean/blob/95de79a5cd49050df80e95be6cfc161580830799/Erdos263/Folklore.lean#L700](https://github.com/arex1337/erdos-263-lean/blob/95de79a5cd49050df80e95be6cfc161580830799/Erdos263/Folklore.lean#L700).

> On the other hand, if there exists some $\varepsilon > 0$ such that $a_n$ satisfies
> $\liminf \frac{a_{n+1}}{a_n^{2+\varepsilon}} > 0$, then $a_n$ is an irrationality sequence
> by the above folklore result `erdos_263.variants.folklore`.

```lean
theorem erdos_263.variants.super_doubly_exponential (a: ℕ -> ℕ)
    (ha : ∀ n : ℕ, a n > 0)
    (ha' : StrictMono a)
    (ha'' : ∃ ε : ℝ, ε > 0 ∧
      Filter.atTop.liminf (fun n : ℕ => (a (n + 1) : ℝ) / a n ^ (2 + ε)) > 0) :
    IsIrrationalitySequence a
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/263.lean, line 119](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/263.lean#L119).

## `Erdos263.erdos_263.variants.super_doubly_exponential_eventual`

Solved: stated here; a Lean proof is at [https://github.com/anatoliiohorodnyk/lean-fc-proofs/blob/5da9642575b26c2c816a49bcb56b33fed5456619/Proofs/T_Erdos263_erdos_263_variants_super_doubly_exponential_eventual.lean#L515](https://github.com/anatoliiohorodnyk/lean-fc-proofs/blob/5da9642575b26c2c816a49bcb56b33fed5456619/Proofs/T_Erdos263_erdos_263_variants_super_doubly_exponential_eventual.lean#L515).

> The same folklore result with the growth hypothesis stated as an eventual lower bound
> $a_{n+1} \geq c\, a_n^{2+\varepsilon}$. Unlike the real-valued `liminf` in
> `erdos_263.variants.super_doubly_exponential`, this form also covers sequences such as
> $a_n = 2^{(n+1)!}$, for which the ratio $a_{n+1} / a_n^{2+\varepsilon}$ tends to $+\infty$ and the
> real `liminf` defaults to $0$.

```lean
theorem erdos_263.variants.super_doubly_exponential_eventual (a : ℕ → ℕ)
    (ha : ∀ n : ℕ, a n > 0)
    (ha' : StrictMono a)
    (ha'' : ∃ ε c : ℝ, 0 < ε ∧ 0 < c ∧
      ∀ᶠ n in atTop, c * (a n : ℝ) ^ (2 + ε) ≤ (a (n + 1) : ℝ)) :
    IsIrrationalitySequence a
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/263.lean, line 136](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/263.lean#L136).

## `Erdos263.erdos_263.variants.doubly_exponential_all_but_countable`

Solved: stated here without proof.

> Koizumi [Ko25] showed that $a_n = \lfloor \alpha^{2^n} \rfloor$ is an irrationality sequence
> for all but countably many $\alpha > 1$, in the nondecreasing sense `IsWeakIrrationalitySequence`.
> The strictly increasing predicate would fail on the whole interval $1 < \alpha < 4/3$, where
> $a_0 = a_1 = 1$.
>
> [Ko25] Koizumi, J., Irrationality of the reciprocal sum of doubly exponential sequences,
>        arXiv:2504.05933 (2025).

```lean
theorem erdos_263.variants.doubly_exponential_all_but_countable :
    ∀ᶠ (α : ℝ) in .cocountable, α > 1 →
      IsWeakIrrationalitySequence (fun n : ℕ => ⌊α ^ 2 ^ n⌋₊)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/263.lean, line 154](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/263.lean#L154).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/263.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/263.lean)
- [erdosproblems.com/263](https://www.erdosproblems.com/263)
