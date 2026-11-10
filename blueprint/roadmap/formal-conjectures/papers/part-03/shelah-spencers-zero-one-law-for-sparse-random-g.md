---
declaration: theorem
origin: cited
lean: ShelahSpencerZeroOneLaw.zeroOne_irrational, ShelahSpencerZeroOneLaw.zeroOne_rational
statement: formalized
---

# Shelah-Spencer's Zero-One Law for Sparse Random Graphs

> *References*:
>
> * [Shelah and Spencer,
>   Zero-one laws for sparse random graphs](https://doi.org/10.1090/S0894-0347-1988-0924703-8),
>   Journal of the American Mathematical Society, 1(1), 97-115 (1988).
> * [Glebskii et al.,
>   Range and degree of realizability of formulas
>   in the restricted predicate calculus](https://doi.org/10.1007/BF01071084),
>   Cybernetics, 5(2), 142-154 (1969) (for $\alpha = 0$).

*Quoted from [FormalConjectures/Paper/ShelahSpencerZeroOneLaw.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/ShelahSpencerZeroOneLaw.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 2 research or textbook statements: 2 solved.

## `ShelahSpencerZeroOneLaw.zeroOne_irrational`

Solved: stated here without proof.

> If $0 < \alpha < 1$ is irrational, then for every first-order sentence $\varphi$ in the
> language of graphs, the probability that $G(n, n^{-\alpha})$ satisfies $\varphi$ tends to either
> zero or one as $n \to \infty$.

```lean
theorem zeroOne_irrational
   (α : ℝ) (hα : 0 < α ∧ α < 1) (hirr : Irrational α) (φ : Language.graph.Sentence) :
   Tendsto (fun n =>
     sparseRandomGraph n α hα.1
       {G | @Language.Sentence.Realize Language.graph (Fin n) G.structure φ}) atTop (𝓝 0) ∨
   Tendsto (fun n =>
     sparseRandomGraph n α hα.1
       {G | @Language.Sentence.Realize Language.graph (Fin n) G.structure φ}) atTop (𝓝 1)
```

Category `research solved`; AMS [03 Mathematical logic and foundations](../../by-subject/part-01/03-mathematical-logic-and-foundations/README.md), [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/Paper/ShelahSpencerZeroOneLaw.lean, line 60](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/ShelahSpencerZeroOneLaw.lean#L60).

## `ShelahSpencerZeroOneLaw.zeroOne_rational`

Solved: stated here without proof.

> If $0 < \alpha < 1$ is rational, then there is a first-order sentence $\varphi$ in the
> language of graphs whose probability in $G(n, n^{-\alpha})$ does not converge as
> $n \to \infty$.

```lean
theorem zeroOne_rational
   (α : ℝ) (hα : 0 < α ∧ α < 1) (hrat : ¬Irrational α) :
   ∃ φ : Language.graph.Sentence,
   ∀ b : ENNReal,
   ¬ Tendsto (fun n =>
     sparseRandomGraph n α hα.1
       {G | @Language.Sentence.Realize Language.graph (Fin n) G.structure φ}) atTop (𝓝 b)
```

Category `research solved`; AMS [03 Mathematical logic and foundations](../../by-subject/part-01/03-mathematical-logic-and-foundations/README.md), [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/Paper/ShelahSpencerZeroOneLaw.lean, line 74](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/ShelahSpencerZeroOneLaw.lean#L74).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Paper/ShelahSpencerZeroOneLaw.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/ShelahSpencerZeroOneLaw.lean)
- [Shelah and Spencer,
  Zero-one laws for sparse random graphs](https://doi.org/10.1090/S0894-0347-1988-0924703-8)
