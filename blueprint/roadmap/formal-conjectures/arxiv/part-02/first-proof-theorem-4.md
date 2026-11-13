---
declaration: theorem
origin: cited
lean: Arxiv.«2602.05192».four, Arxiv.«2602.05192».four_2, Arxiv.«2602.05192».four_3
statement: formalized
---

# First Proof, Theorem 4

> *Reference:* [arxiv/2602.05192v2](https://arxiv.org/abs/2602.05192v2)
> **First Proof**
> by *Mohammed Abouzaid, Andrew J. Blumberg, Martin Hairer, Joe Kileel, Tamara G. Kolda, Paul D. Nelson, Daniel Spielman, Nikhil Srivastava, Rachel Ward, Shmuel Weinberger, Lauren Williams*

*Quoted from [FormalConjectures/Arxiv/2602.05192/FirstProof4.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Arxiv/2602.05192/FirstProof4.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 3 research or textbook statements: 3 solved. It also has 3 test statements, counted here but not shown.

## `Arxiv.«2602.05192».four`

Solved: stated here; a Lean proof is at [https://github.com/frenzymath/Archon-FirstProof-Results/blob/main/FirstProof/FirstProof4/Problem4.lean](https://github.com/frenzymath/Archon-FirstProof-Results/blob/main/FirstProof/FirstProof4/Problem4.lean).

> Is it true that if $p(x)$ and $q(x)$ are monic real-rooted polynomials of
> degree $n$, then
>
> $$\frac{1}{\Phi_n(p\boxplus_n q)} \ge \frac{1}{\Phi_n(p)}+\frac{1}{\Phi_n(q)}?$$
>
> [arxiv/2602.05192v2](https://arxiv.org/abs/2602.05192v2) contains a proof.

```lean
theorem four : ∀ (p q : ℝ[X]) (n : ℕ), FourProp p q n
```

Category `research solved`; AMS [26 Real functions](../../by-subject/part-01/26-real-functions/README.md). Declared in [FormalConjectures/Arxiv/2602.05192/FirstProof4.lean, line 158](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Arxiv/2602.05192/FirstProof4.lean#L158).

## `Arxiv.«2602.05192».four_2`

Solved: stated here without proof.

> Is it true that if $p(x)$ and $q(x)$ are monic real-rooted polynomials of
> degree $2$, then
>
> $$\frac{1}{\Phi_2(p\boxplus_n q)} \ge \frac{1}{\Phi_2(p)}+\frac{1}{\Phi_2(q)}?$$

```lean
theorem four_2 : ∀ (p q : ℝ[X]), FourProp p q 2
```

Category `research solved`; AMS [26 Real functions](../../by-subject/part-01/26-real-functions/README.md). Declared in [FormalConjectures/Arxiv/2602.05192/FirstProof4.lean, line 167](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Arxiv/2602.05192/FirstProof4.lean#L167).

## `Arxiv.«2602.05192».four_3`

Solved: stated here without proof.

> Is it true that if $p(x)$ and $q(x)$ are monic real-rooted polynomials of
> degree $3$, then
>
> $$\frac{1}{\Phi_3(p\boxplus_n q)} \ge \frac{1}{\Phi_3(p)}+\frac{1}{\Phi_3(q)}?$$

```lean
theorem four_3 : ∀ (p q : ℝ[X]), FourProp p q 3
```

Category `research solved`; AMS [26 Real functions](../../by-subject/part-01/26-real-functions/README.md). Declared in [FormalConjectures/Arxiv/2602.05192/FirstProof4.lean, line 176](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Arxiv/2602.05192/FirstProof4.lean#L176).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Arxiv/2602.05192/FirstProof4.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Arxiv/2602.05192/FirstProof4.lean)
- [arxiv/2602.05192v2](https://arxiv.org/abs/2602.05192v2)
