---
declaration: theorem
origin: cited
lean: Erdos1025.erdos_1025
statement: formalized
---

# Erdős Problem 1025

> *References:*
> - [erdosproblems.com/1025](https://www.erdosproblems.com/1025)
> - [Er71] Erdős, P., *Some unsolved problems in graph theory and combinatorial analysis*.
>   Combinatorial Mathematics and its Applications (Proc. Conf., Oxford, 1969) (1971), 97-109.
> - [ErHa58] Erdős, P. and Hajnal, A., *On the structure of set mappings*. Acta Math. Acad. Sci.
>   Hungar. (1958), 111-133.
> - [Sp72] Spencer, Joel, *Turán's theorem for $k$-graphs*. Discrete Math. (1972), 183--186.
> - [CFS16] Conlon, David and Fox, Jacob and Sudakov, Benny, *Short proofs of some extremal results
>   II*. J. Combin. Theory Ser. B (2016), 173--196.

*Quoted from [FormalConjectures/ErdosProblems/1025.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1025.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/1025](https://www.erdosproblems.com/1025).

The file states 1 research or textbook statement: 1 solved.

## `Erdos1025.erdos_1025`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos1025.lean#L829](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos1025.lean#L829).

> Let $f$ be a function from all pairs of elements in $\{1,\ldots,n\}$ to $\{1,\ldots,n\}$ such
> that $f(x,y)\neq x$ and $\neq y$ for all $x,y$. We call $X\subseteq \{1,\ldots,n\}$ independent
> if whenever $x,y\in X$ we have $f(x,y)\not\in X$.
>
> Let $g(n)$ be such that, in every function $f$, there is an independent set of size at least
> $g(n)$. Estimate $g(n)$.
>
> A question of Erdős and Hajnal [ErHa58], who could prove $n^{1/3} \ll g(n) \ll (n\log n)^{1/2}$.
> Spencer [Sp72] proved $g(n)\gg n^{1/2}$. Conlon, Fox, and Sudakov [CFS16] proved
> $g(n)\ll n^{1/2}$.

```lean
theorem erdos_1025 : (fun n : ℕ => (g n : ℝ)) =Θ[atTop] fun n : ℕ => √n
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/1025.lean, line 67](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1025.lean#L67).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/1025.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1025.lean)
- [erdosproblems.com/1025](https://www.erdosproblems.com/1025)
