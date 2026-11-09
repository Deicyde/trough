---
declaration: theorem
origin: cited
lean: Erdos440.erdos_440.parts.i, Erdos440.erdos_440.parts.ii, Erdos440.erdos_440.variants.erdos_szemeredi
statement: formalized
---

# Erdős Problem 440

> *References:*
> - [erdosproblems.com/440](https://www.erdosproblems.com/440)
> - [ErGr80] Erdős, P. and Graham, R., _Old and new problems and results in combinatorial number
>   theory_. Monographies de L'Enseignement Mathematique (1980).
> - [ErSz80] Erdős, Pál and Szemerédi, Endre, _Remarks on a problem of the American Mathematical
>   Monthly_. Mat. Lapok (1980), 121-124.

*Quoted from [FormalConjectures/ErdosProblems/440.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/440.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/440](https://www.erdosproblems.com/440).

The file states 3 research or textbook statements: 3 solved.

## `Erdos440.erdos_440.parts.i`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos440.lean#L602](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos440.lean#L602).

> Let $A=\{a_1\lt a_2\lt \cdots\}\subseteq \mathbb{N}$ be infinite and let $A(x)$ count the number of
> indices for which $\mathrm{lcm}(a_i,a_{i+1})\leq x$. Is it true that $A(x) \ll x^{1/2}$?
>
> The answer is yes: Tao has given a simple proof, and Erdős and Szemerédi [ErSz80] proved the
> sharp bound $A(x)\leq (c+o(1))x^{1/2}$ (see `erdos_440.variants.erdos_szemeredi`).

```lean
theorem erdos_440.parts.i :
    ∀ a : ℕ → ℕ, StrictMono a → (∀ i, 0 < a i) →
      (fun x : ℕ ↦ (count a x : ℝ)) =O[atTop] fun x : ℕ ↦ √x
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/440.lean, line 52](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/440.lean#L52).

## `Erdos440.erdos_440.parts.ii`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos440.lean#L602](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos440.lean#L602).

> How large can
> $$\liminf \frac{A(x)}{x^{1/2}}$$
> be?
>
> Taking $A=\mathbb{N}$ shows that $\liminf A(x)/x^{1/2}=1$ is possible. Erdős and Szemerédi
> [ErSz80] proved that it is always $\leq 1$.

```lean
theorem erdos_440.parts.ii :
    IsGreatest {l : ℝ | ∃ a : ℕ → ℕ, StrictMono a ∧ (∀ i, 0 < a i) ∧
      l = liminf (fun x : ℕ ↦ (count a x : ℝ) / √x) atTop} erdos_440.parts.ii.answer
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/440.lean, line 70](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/440.lean#L70).

## `Erdos440.erdos_440.variants.erdos_szemeredi`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos440.lean#L602](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos440.lean#L602).

> Erdős and Szemerédi [ErSz80] proved that $A(x)\leq (c+o(1))x^{1/2}$ where
> $$c=\sum_{n\geq 1}\frac{1}{n^{1/2}(n+1)}\approx 1.86,$$
> and that this constant is best possible (this was later rediscovered by van Doorn).

```lean
theorem erdos_440.variants.erdos_szemeredi :
    IsGreatest {l : ℝ | ∃ a : ℕ → ℕ, StrictMono a ∧ (∀ i, 0 < a i) ∧
      l = limsup (fun x : ℕ ↦ (count a x : ℝ) / √x) atTop} erdosSzemerediConstant
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/440.lean, line 87](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/440.lean#L87).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/440.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/440.lean)
- [erdosproblems.com/440](https://www.erdosproblems.com/440)
