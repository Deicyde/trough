---
declaration: theorem
origin: cited
lean: Erdos1171.erdos_1171, Erdos1171.erdos_1171.variants.k_one
statement: formalized
---

# Erdős Problem 1171

> *Reference:* [erdosproblems.com/1171](https://www.erdosproblems.com/1171)

*Quoted from [FormalConjectures/ErdosProblems/1171.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1171.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/1171](https://www.erdosproblems.com/1171).

The file states 2 research or textbook statements: 1 open and 1 solved. It also has 1 API statement, counted here but not shown.

## `Erdos1171.erdos_1171`

Open: stated without proof.

> **Erdős Problem 1171.** Is it true that for all finite $k < \omega$,
> $$\omega_1^2 \to (\omega_1 \cdot \omega, \underbrace{3, \ldots, 3}_{k})^2_{k+1}?$$
>
> In any $(k+1)$-coloring of the pairs of the complete graph on $\omega_1^2$, either
> there is a color-0 set of order type $\omega_1 \cdot \omega$, or there is a
> monochromatic triangle $K_3$ in some non-zero color. The case $k = 1$
> (`erdos_1171.variants.k_one`) is the Erdős–Hajnal theorem [EH74].

```lean
theorem erdos_1171 :
    ∀ k : ℕ, OrdinalMultiColorRamsey (ω_ 1 ^ 2) (ω_ 1 * ω) 3 k
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/1171.lean, line 43](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1171.lean#L43).

## `Erdos1171.erdos_1171.variants.k_one`

Solved: stated here without proof.

> **Erdős–Hajnal theorem** [EH74]: the case $k = 1$,
> $\omega_1^2 \to (\omega_1 \cdot \omega, 3)^2$.

```lean
theorem k_one : OrdinalMultiColorRamsey (ω_ 1 ^ 2) (ω_ 1 * ω) 3 1
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/1171.lean, line 54](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1171.lean#L54).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/1171.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1171.lean)
- [erdosproblems.com/1171](https://www.erdosproblems.com/1171)
