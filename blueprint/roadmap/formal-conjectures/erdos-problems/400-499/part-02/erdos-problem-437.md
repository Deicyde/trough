---
declaration: theorem
origin: cited
lean: Erdos437.erdos_437, Erdos437.erdos_437.variants.little_o, Erdos437.erdos_437.variants.tao
statement: formalized
---

# Erdős Problem 437

> *References:*
> - [erdosproblems.com/437](https://www.erdosproblems.com/437)
> - [ErGr80] Erdős, P. and Graham, R., _Old and new problems and results in combinatorial number
>   theory_. Monographies de L'Enseignement Mathematique (1980).
> - [BPZ24] Bui, Hung M. and Pratt, Kyle and Zaharescu, Alexandru, _A problem of
>   Erdős-Graham-Granville-Selfridge on integral points on hyperelliptic curves_. Math. Proc.
>   Cambridge Philos. Soc. (2024), 309--323.
> - [Ta24] Tao, Terence, _A result of Bui–Pratt–Zaharescu, and Erdős problem #437_. Blog post
>   (2024).

*Quoted from [FormalConjectures/ErdosProblems/437.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/437.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/437](https://www.erdosproblems.com/437).

The file states 3 research or textbook statements: 3 solved.

## `Erdos437.erdos_437`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos437.lean#L746](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos437.lean#L746).

> Let $1\leq a_1\lt \cdots\lt a_k\leq x$. How many of the partial products
> $a_1,a_1a_2,\ldots,a_1\cdots a_k$ can be squares? Is it true that, for any $\epsilon>0$, there can
> be more than $x^{1-\epsilon}$ squares?
>
> The answer is yes, which follows from work of Bui, Pratt, and Zaharescu [BPZ24], as noted by
> Tao [Ta24].

```lean
theorem erdos_437 :
    ∀ ε : ℝ, 0 < ε → ∀ᶠ x : ℕ in atTop, (x : ℝ) ^ (1 - ε) < L x
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/437.lean, line 62](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/437.lean#L62).

## `Erdos437.erdos_437.variants.little_o`

Solved: stated here without proof.

> Erdős and Graham write it is 'trivial' that there are $o(x)$ many such squares, although this is
> not quite trivial, using Siegel's theorem.

```lean
theorem erdos_437.variants.little_o :
    (fun x : ℕ ↦ (L x : ℝ)) =o[atTop] fun x : ℕ ↦ (x : ℝ)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/437.lean, line 71](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/437.lean#L71).

## `Erdos437.erdos_437.variants.tao`

Solved: stated here without proof.

> Tao [Ta24] shows that, if $u(x)=(\log x\log\log x)^{1/2}$, then
> $$x\exp(-(2^{1/2}+o(1))u(x)) \leq L(x) \leq x\exp(-(2^{-1/2}+o(1))u(x)).$$

```lean
theorem erdos_437.variants.tao :
    ∃ o₁ o₂ : ℕ → ℝ, Tendsto o₁ atTop (nhds 0) ∧ Tendsto o₂ atTop (nhds 0) ∧
      ∀ᶠ x : ℕ in atTop,
        x * exp (-(√2 + o₁ x) * √(log x * log (log x))) ≤ L x ∧
        L x ≤ x * exp (-((√2)⁻¹ + o₂ x) * √(log x * log (log x)))
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/437.lean, line 80](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/437.lean#L80).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/437.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/437.lean)
- [erdosproblems.com/437](https://www.erdosproblems.com/437)
