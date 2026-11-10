---
declaration: theorem
origin: cited
lean: GaussCircleProblem.error_le, GaussCircleProblem.error_not_isLittleO, GaussCircleProblem.error_isBigO, GaussCircleProblem.exact_form_floor
statement: formalized
---

# Gauss circle problem

> *Reference:* [Wikipedia](https://en.wikipedia.org/wiki/Gauss_circle_problem)

*Quoted from [FormalConjectures/Wikipedia/GaussCircleProblem.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/GaussCircleProblem.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 4 research or textbook statements: 1 open and 3 solved.

## `GaussCircleProblem.error_le`

Solved: stated here without proof.

> Gauss proved that
>
> $$
>   |E(r)|\leq 2\sqrt{2}\pi r,
> $$
>
> for sufficiently large $r$.
>
> [Ha59]  Hardy, G. H. (1959). _Ramanujan: Twelve Lectures on Subjects Suggested by His Life and Work_(3rd ed.). New York: Chelsea Publishing Company. p. 67

```lean
theorem error_le : ∀ᶠ r in atTop, |E r| ≤ 2 * √2 * π * r
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/GaussCircleProblem.lean, line 68](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/GaussCircleProblem.lean#L68).

## `GaussCircleProblem.error_not_isLittleO`

Solved: stated here without proof.

> Hardy and Laundau independently found a lower bound by showing that
>
> $$
>   |E(r)| \neq o\left(r^{1/2}(\log r)^{1/4}\right)
> $$

```lean
theorem error_not_isLittleO : ¬E =o[atTop] (fun r => √r * √√r.log)
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/GaussCircleProblem.lean, line 78](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/GaussCircleProblem.lean#L78).

## `GaussCircleProblem.error_isBigO`

Open: stated without proof.

> It is conjectured that the correct bound is
>
> $$
>   |E(r)| = O\left(r^{1/2 + o(1)}\right)
> $$
>
> [Ha59]  Hardy, G. H. (1959). _Ramanujan: Twelve Lectures on Subjects Suggested by His Life and Work_(3rd ed.). New York: Chelsea Publishing Company. p. 67
>
> See also https://arxiv.org/abs/2305.03549

```lean
theorem error_isBigO : ∃ (o : ℝ → ℝ) (_ : Tendsto o atTop (𝓝 0)),
    E =O[atTop] fun r => r ^ (1/2 + o r)
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/GaussCircleProblem.lean, line 92](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/GaussCircleProblem.lean#L92).

## `GaussCircleProblem.exact_form_floor`

Solved: stated here without proof.

> The value of $N(r)$ can be expressed as
>
> $$
>   N(r) = 1 + 4\sum_{i=0}^{\infty}\left(\left\lfloor\frac{r^2}{4i+1}\right\rfloor -
>     \left\lfloor\frac{r^2}{4i + 3}\right\rfloor\right).
> $$

```lean
theorem exact_form_floor (r : ℝ) (hr : 0 ≤ r) :
    N r = 1 + 4 * ∑' (i : ℕ), (⌊r ^ 2 / (4 * i + 1)⌋ - ⌊r ^ 2 / (4 * i + 3)⌋)
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/GaussCircleProblem.lean, line 104](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/GaussCircleProblem.lean#L104).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Wikipedia/GaussCircleProblem.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/GaussCircleProblem.lean)
- [Wikipedia](https://en.wikipedia.org/wiki/Gauss_circle_problem)
