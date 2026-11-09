---
declaration: theorem
origin: cited
lean: Arxiv.«2602.05192».epsilon_light_subset_exists
statement: formalized
---

# First Proof, Theorem 6

> *Reference:* [arxiv/2602.05192v2](https://arxiv.org/abs/2602.05192v2)
> **First Proof**
> by *Mohammed Abouzaid, Andrew J. Blumberg, Martin Hairer, Joe Kileel, Tamara G. Kolda, Paul D. Nelson, Daniel Spielman, Nikhil Srivastava, Rachel Ward, Shmuel Weinberger, Lauren Williams*

*Quoted from [FormalConjectures/Arxiv/2602.05192/FirstProof6.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Arxiv/2602.05192/FirstProof6.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 solved.

## `Arxiv.«2602.05192».epsilon_light_subset_exists`

Solved: stated here; a Lean proof is at [https://github.com/frenzymath/Archon-FirstProof-Results/blob/main/FirstProof/FirstProof6/Problem6.lean](https://github.com/frenzymath/Archon-FirstProof-Results/blob/main/FirstProof/FirstProof6/Problem6.lean).

> Does there exist a constant $c > 0$ so that for every graph $G$ and every $\epsilon$ between
> $0$ and $1$, $V$ contains an $\epsilon$-light subset $S$ of size at least $c \epsilon |V|$?

```lean
theorem epsilon_light_subset_exists :
    ∃ (c : ℝ), c > 0 ∧ ∀ (n : ℕ) (G : SimpleGraph (Fin n)) (ε : ℝ),
    0 < ε → ε < 1 →
    ∃ (S : Finset (Fin n)), IsEpsilonLight G ε S ∧ (S.card : ℝ) ≥ c * ε * n
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/Arxiv/2602.05192/FirstProof6.lean, line 61](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Arxiv/2602.05192/FirstProof6.lean#L61).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Arxiv/2602.05192/FirstProof6.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Arxiv/2602.05192/FirstProof6.lean)
- [arxiv/2602.05192v2](https://arxiv.org/abs/2602.05192v2)
