---
declaration: theorem
origin: cited
lean: Erdos40.erdos_40, Erdos40.erdos_40.variants.weaker, Erdos40.erdos_40.variants.implies_erdos_28
statement: formalized
---

# Erdős Problem 40

> *Reference:* [erdosproblems.com/40](https://www.erdosproblems.com/40)

*Quoted from [FormalConjectures/ErdosProblems/40.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/40.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/40](https://www.erdosproblems.com/40).

The file states 3 research or textbook statements: 2 open and 1 textbook result.

## `Erdos40.erdos_40`

Open: stated without proof.

> For what functions $g(N) → \infty$ is it true that
>
> $$\lvert A\cap \{1,\ldots,N\}\rvert \gg \frac{N^{1/2}}{g(N)}$$
>
> implies $\limsup 1_A\ast 1_A(n)=\infty$?

```lean
theorem erdos_40 :
    {g : ℕ → ℝ | Tendsto g atTop atTop ∧ Erdos40For g} = erdos_40.answer
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/40.lean, line 52](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/40.lean#L52).

## `Erdos40.erdos_40.variants.weaker`

Open: stated without proof.

> Is there any function $g(N) → \infty$ such that
>
> $$\lvert A\cap \{1,\ldots,N\}\rvert \gg \frac{N^{1/2}}{g(N)}$$
>
> implies $\limsup 1_A\ast 1_A(n)=\infty$?
>
> This is a weaker form of Erdős Problem 40, which asks for all such $g$. Establishing
> the implication for even one $g(N) → \infty$ already answers Erdős Problem 28
> positively, because a basis of order $2$ satisfies
> $\lvert A\cap \{1,\ldots,N\}\rvert \gg N^{1/2}$.

```lean
theorem erdos_40.variants.weaker :
    ∃ g : ℕ → ℝ, Tendsto g atTop atTop ∧ Erdos40For g
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/40.lean, line 67](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/40.lean#L67).

## `Erdos40.erdos_40.variants.implies_erdos_28`

Textbook result, proved here.

> Establishing the property in Erdős Problem 40 for any one function $g(N) → \infty$
> implies the Erdős-Turán conjecture, see Erdős Problem 28.

```lean
theorem erdos_40.variants.implies_erdos_28 (g : ℕ → ℝ) (hg : Tendsto g atTop atTop)
    (h_erdos_40 : Erdos40For g) : type_of% Erdos28.erdos_28
```

Category `textbook`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/40.lean, line 76](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/40.lean#L76).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/40.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/40.lean)
- [erdosproblems.com/40](https://www.erdosproblems.com/40)
