---
declaration: theorem
origin: cited
lean: Erdos444.erdos_444
statement: formalized
---

# Erdős Problem 444

> *References:*
> - [erdosproblems.com/444](https://www.erdosproblems.com/444)
> - [ErGr80] Erdős, P. and Graham, R., *Old and new problems and results in combinatorial number
>   theory*. Monographies de L'Enseignement Mathematique (1980).
> - [ErSa80] Erdős, P. and Sárközy, A., *Some asymptotic formulas on generalized divisor functions.
>   IV*. Studia Sci. Math. Hungar. (1980), 467-479.

*Quoted from [FormalConjectures/ErdosProblems/444.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/444.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/444](https://www.erdosproblems.com/444).

The file states 1 research or textbook statement: 1 solved. It also has 2 test statements, counted here but not shown.

## `Erdos444.erdos_444`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos444.lean#L38](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos444.lean#L38).

> Let $A\subseteq\mathbb{N}$ be infinite and $d_A(n)$ count the number of $a\in A$ which divide $n$.
> Is it true that, for every $k$,
>
> $$\limsup_{x\to \infty} \frac{\max_{n\lt x}d_A(n)}{\left(\sum_{n\in A\cap[1,x)}\frac{1}{n}\right)^k}
> =\infty?$$
>
> This is asked in [ErGr80, p.88]. The answer is yes, proved by Erdős and Sárközy [ErSa80].
>
> The maximum is over $1 \le n < x$, since every $a \in A$ divides $0$.

```lean
theorem erdos_444 : ∀ A : Set ℕ, A.Infinite → ∀ k : ℕ,
    atTop.limsup (fun x : ℝ ↦ (((Ico 1 ⌈x⌉₊).sup (divisorCount A) /
      (∑ n ∈ Ico 1 ⌈x⌉₊ with n ∈ A, (n : ℝ)⁻¹) ^ k : ℝ) : EReal)) = ⊤
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/444.lean, line 65](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/444.lean#L65).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/444.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/444.lean)
- [erdosproblems.com/444](https://www.erdosproblems.com/444)
