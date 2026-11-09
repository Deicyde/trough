---
declaration: theorem
origin: cited
lean: Erdos1116.erdos_1116
statement: formalized
---

# Erdős Problem 1116

> *References:*
> - [erdosproblems.com/1116](https://www.erdosproblems.com/1116)
> - [Ha74] Hayman, W. K., *Research problems in function theory: new problems*. Proceedings of
>   the Symposium on Complex Analysis (Canterbury, 1973), London Math. Soc. Lecture Note Ser. 12
>   (1974), 155--180.
> - [To76] Toppila, Sakari, *On the counting function for the $a$-values of a meromorphic
>   function*. Ann. Acad. Sci. Fenn. Ser. A I Math. 2 (1976), 565--572.
>   [PDF](https://www.acadsci.fi/mathematica/Vol02/vol02pp565-572.pdf)
> - [Go78] Gol'dberg, A. A., *Counting functions of sequences of $a$-points for entire
>   functions*. Sibirsk. Mat. Zh. 19 (1978), 28--36, 236.
> - [HaLi18] Hayman, W. K. and Lingham, E. F., *Research problems in function theory*.
>   [arXiv:1809.07200](https://arxiv.org/abs/1809.07200) (2018).

*Quoted from [FormalConjectures/ErdosProblems/1116.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1116.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/1116](https://www.erdosproblems.com/1116).

The file states 1 research or textbook statement: 1 solved.

## `Erdos1116.erdos_1116`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos1116.lean#L4968](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos1116.lean#L4968).

> For a meromorphic function $f$ let $n(r,a)$ count the number of roots of $f(z)=a$ in the disc
> $\lvert z\rvert \lt r$. Does there exist a meromorphic (or entire) $f$ such that for every
> $a\neq b$
> $$\limsup_{r\to \infty}\frac{n(r,a)}{n(r,b)}=\infty?$$
>
> This is Problem 1.25 in [Ha74], where it is attributed to Erdős. Gol'dberg [Go78] and Toppila
> [To76, Theorem 3] constructed such entire functions. We state this case, for finite
> $a\neq b$, using `UnboundedCountRatio`.

```lean
theorem erdos_1116 :
    ∃ f : ℂ → ℂ, Differentiable ℂ f ∧
      ∀ a b : ℂ, a ≠ b → UnboundedCountRatio f a b
```

Category `research solved`; AMS [30 Functions of a complex variable](../../../by-subject/part-01/30-functions-of-a-complex-variable/README.md). Declared in [FormalConjectures/ErdosProblems/1116.lean, line 77](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1116.lean#L77).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/1116.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1116.lean)
- [erdosproblems.com/1116](https://www.erdosproblems.com/1116)
