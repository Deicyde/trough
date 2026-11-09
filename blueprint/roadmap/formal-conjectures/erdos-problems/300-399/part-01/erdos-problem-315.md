---
declaration: theorem
origin: cited
lean: Erdos315.erdos_315
statement: formalized
---

# Erdős Problem 315

> *References:*
> - [erdosproblems.com/315](https://www.erdosproblems.com/315)
> - [ErGr80] Erdős, P. and Graham, R., *Old and new problems and results in combinatorial number
>   theory*. Monographies de L'Enseignement Mathematique (1980).
> - [Ka25] Y. Kamio, *Asymptotic analysis of infinite decompositions of a unit fraction into unit
>   fractions*. arXiv:2503.02317 (2025).
> - [LiTa25] Z. Li and Q. Tang, *On a conjecture of Erdős and Graham about the Sylvester's
>   sequence*. arXiv:2503.12277 (2025).

*Quoted from [FormalConjectures/ErdosProblems/315.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/315.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/315](https://www.erdosproblems.com/315).

The file states 1 research or textbook statement: 1 solved.

## `Erdos315.erdos_315`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/1d7b3f00780b85ed0462e79a1cd5650ee9055655/src/v4.29.1/ErdosProblems/Erdos315.lean](https://github.com/plby/lean-proofs/blob/1d7b3f00780b85ed0462e79a1cd5650ee9055655/src/v4.29.1/ErdosProblems/Erdos315.lean).

> Let $u_1=1$ and $u_{n+1}=u_n(u_n+1)$, so that $\sum_{k\geq 1}\frac{1}{u_k+1}$ and
> $u_k=\lfloor c_0^{2^k}+1\rfloor$ for $k\geq 1$, where
> $$c_0=\lim u_n^{1/2^n}=1.264085\cdots.$$
> Let $a_1\lt a_2\lt \cdots $ be any other sequence with $\sum \frac{1}{a_k}=1$. Is it true that
> $$\liminf a_n^{1/2^n}\lt c_0=1.264085\cdots?$$
>
> This is true, and was proved independently by Kamio [Ka25] and Li and Tang [LiTa25].
>
> An earlier interpretation of this question on this site defined $u_1=2$ and
> $u_{n+1}=u_n^2-u_n+1$ (Sylvester's sequence), which is the same sequence shifted by $1$; we use
> the phrasing above as more faithful to [ErGr80]. The constant $c_0$ is called the Vardi constant.

```lean
theorem erdos_315 :
    ∀ a : ℕ → ℕ, (∀ i, 0 < a i) → StrictMono a → (∃ i, a i ≠ u i + 1) →
      ∑' i, (1 : ℝ) / a i = 1 →
      atTop.liminf (fun i => (a i : ℝ) ^ ((1 / 2 : ℝ) ^ (i + 1))) < c₀
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/315.lean, line 66](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/315.lean#L66).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/315.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/315.lean)
- [erdosproblems.com/315](https://www.erdosproblems.com/315)
