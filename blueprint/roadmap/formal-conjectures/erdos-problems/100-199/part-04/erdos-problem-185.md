---
declaration: theorem
origin: cited
lean: Erdos185.erdos_185, Erdos185.erdos_185.variants.moser
statement: formalized
---

# Erdős Problem 185

> *References:*
> - [erdosproblems.com/185](https://www.erdosproblems.com/185)
> - [Er73] Erdős, P., *Problems and results on combinatorial number theory*. A survey of
>   combinatorial theory (Proc. Internat. Sympos., Colorado State Univ., Fort Collins, Colo., 1971)
>   (1973), 117-138.
> - [FuKa91] Furstenberg, H. and Katznelson, Y., *A density version of the Hales-Jewett Theorem*.
>   Journal d'Analyse Mathématique (1991), 64-119.

*Quoted from [FormalConjectures/ErdosProblems/185.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/185.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/185](https://www.erdosproblems.com/185).

The file states 2 research or textbook statements: 2 solved.

## `Erdos185.erdos_185`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos185.lean#L49](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos185.lean#L49).

> Let $f_3(n)$ be the maximal size of a subset of $\{0,1,2\}^n$ which contains no three points on
> a line. Is it true that $f_3(n)=o(3^n)$?
>
> Originally considered by Moser. It is trivial that $f_3(n)\geq R_3(3^n)$, the maximal size of a
> subset of $\{1,\ldots,3^n\}$ without a three-term arithmetic progression. Moser showed that
>
> $$f_3(n) \gg \frac{3^n}{\sqrt{n}}.$$
>
> The answer is yes, which is a corollary of the density Hales-Jewett theorem, proved by
> Furstenberg and Katznelson [FuKa91].

```lean
theorem erdos_185 : (fun n : ℕ => (f3 n : ℝ)) =o[atTop] fun n : ℕ => (3 : ℝ) ^ n
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/185.lean, line 60](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/185.lean#L60).

## `Erdos185.erdos_185.variants.moser`

Solved: stated here without proof.

> Moser showed that $f_3(n) \gg \frac{3^n}{\sqrt{n}}$.

```lean
theorem erdos_185.variants.moser :
    (fun n : ℕ => (3 : ℝ) ^ n / √n) =O[atTop] fun n : ℕ => (f3 n : ℝ)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/185.lean, line 65](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/185.lean#L65).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/185.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/185.lean)
- [erdosproblems.com/185](https://www.erdosproblems.com/185)
