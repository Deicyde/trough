---
declaration: theorem
origin: cited
lean: Erdos290.erdos_290
statement: formalized
---

# Erdős Problem 290

> *References:*
> - [erdosproblems.com/290](https://www.erdosproblems.com/290)
> - [ErGr80] Erdős, P. and Graham, R., *Old and new problems and results in combinatorial number
>   theory*. Monographies de L'Enseignement Mathématique (1980), p.34.
> - [vD24] van Doorn, W., *On the non-monotonicity of the denominator of generalized harmonic sums*.
>   arXiv:2411.03073 (2024).

*Quoted from [FormalConjectures/ErdosProblems/290.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/290.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/290](https://www.erdosproblems.com/290).

The file states 1 research or textbook statement: 1 solved.

## `Erdos290.erdos_290`

Solved: stated here; a Lean proof is at [https://github.com/Woett/Lean-files/blob/main/ErdosProblem290.lean](https://github.com/Woett/Lean-files/blob/main/ErdosProblem290.lean).

> Let $a\geq 1$. Must there exist some $b>a$ such that
>
> $$\sum_{a\leq n\leq b}\frac{1}{n}=\frac{r_1}{s_1}\textrm{ and }
> \sum_{a\leq n\leq b+1}\frac{1}{n}=\frac{r_2}{s_2},$$
>
> with $(r_i,s_i)=1$ and $s_2\lt s_1$? If so, how does this $b(a)$ grow with $a$?
>
> This was resolved in the affirmative by van Doorn [vD24], who proved $b=b(a)$ always exists, and in
> fact $b(a) \ll a$. Indeed, if $a\in (3^k,3^{k+1}]$ then one can take $b=2\cdot 3^{k+1}-1$. van Doorn
> also proves that $b(a)>a+(1/2-o(1))\log a$, and considers various generalisations of the original
> problem.

```lean
theorem erdos_290 :
    (∀ a : ℕ, 1 ≤ a → ∃ b : ℕ, a < b ∧ harmonicDen a (b + 1) < harmonicDen a b)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/290.lean, line 52](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/290.lean#L52).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/290.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/290.lean)
- [erdosproblems.com/290](https://www.erdosproblems.com/290)
