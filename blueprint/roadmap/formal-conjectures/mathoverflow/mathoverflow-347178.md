---
declaration: theorem
origin: cited
lean: Mathoverflow347178.mathoverflow_347178, Mathoverflow347178.mathoverflow_347178.variants.bounded_iff, Mathoverflow347178.mathoverflow_347178.variants.bounded_only
statement: formalized
---

# Mathoverflow 347178

> *Reference:* [mathoverflow/347178](https://mathoverflow.net/questions/347178)
> asked by user [*Biagio Ricceri*](https://mathoverflow.net/users/149235/biagio-ricceri)

*Quoted from [FormalConjectures/Mathoverflow/347178.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Mathoverflow/347178.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 3 research or textbook statements: 3 solved.

## `Mathoverflow347178.mathoverflow_347178`

Solved: stated here; a Lean proof is at [https://github.com/google-deepmind/formal-conjectures/blob/fc20c0b55eab6fc26e2bb5b24fb3005303a0910b/FormalConjectures/Mathoverflow/347178.lean#L670](https://github.com/google-deepmind/formal-conjectures/blob/fc20c0b55eab6fc26e2bb5b24fb3005303a0910b/FormalConjectures/Mathoverflow/347178.lean#L670).

> Let $f : \mathbb R^n \to \mathbb R,  n \geq 2$ be a $C^1$ function. Is it true that
> $$\sup_{x \in \mathbb R^n}f(x) = \sup_{x\in \mathbb R^n} f(x+\nabla f(x))$$?
>
> Answer: No. A counterexample in $\mathbb R^2$ is recorded in the linked formal proof.

```lean
theorem mathoverflow_347178 :
    ¬ ∀ᵉ (n ≥ 2) (f : ℝ^n → ℝ) (_ : ContDiff ℝ 1 f),
        (BddAbove (range f) ↔ BddAbove (range (fun x ↦ f (x + gradient f x)))) ∧
        (⨆ x, (f x : EReal)) = ⨆ x, (f (x + gradient f x) : EReal)
```

Category `research solved`; AMS [26 Real functions](../by-subject/part-01/26-real-functions/README.md). Declared in [FormalConjectures/Mathoverflow/347178.lean, line 44](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Mathoverflow/347178.lean#L44).

## `Mathoverflow347178.mathoverflow_347178.variants.bounded_iff`

Solved: stated here; a Lean proof is at [https://github.com/google-deepmind/formal-conjectures/blob/fc20c0b55eab6fc26e2bb5b24fb3005303a0910b/FormalConjectures/Mathoverflow/347178.lean#L690](https://github.com/google-deepmind/formal-conjectures/blob/fc20c0b55eab6fc26e2bb5b24fb3005303a0910b/FormalConjectures/Mathoverflow/347178.lean#L690).

> Let $f : \mathbb R^n \to \mathbb R,  n \geq 2$ be a $C^1$ function. Is the boundedness of
> $\sup_{x \in \mathbb R^n}f(x)$ and $\sup_{x\in \mathbb R^n} f(x+\nabla f(x))$ equivalent?
>
> Answer: No. The same counterexample is recorded in the linked formal proof.

```lean
theorem mathoverflow_347178.variants.bounded_iff :
    ¬ ∀ᵉ (n ≥ 2) (f : ℝ^n → ℝ) (_ : ContDiff ℝ 1 f),
        BddAbove (range f) ↔ BddAbove (range fun x ↦ f (x + gradient f x))
```

Category `research solved`; AMS [26 Real functions](../by-subject/part-01/26-real-functions/README.md). Declared in [FormalConjectures/Mathoverflow/347178.lean, line 60](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Mathoverflow/347178.lean#L60).

## `Mathoverflow347178.mathoverflow_347178.variants.bounded_only`

Solved: stated here; a Lean proof is at [https://github.com/inozemtsev/gradient-supremum/blob/56743ea06dd2953e02274841c16e0f56927b5a44/GradientSupremum/Mathoverflow347178.lean#L30](https://github.com/inozemtsev/gradient-supremum/blob/56743ea06dd2953e02274841c16e0f56927b5a44/GradientSupremum/Mathoverflow347178.lean#L30).

> Let $f : \mathbb R^n \to \mathbb R,  n \geq 2$ be a $C^1$ function. Does the equality
> $$\sup_{x \in \mathbb R^n}f(x) = \sup_{x\in \mathbb R^n} f(x+\nabla f(x))$$
> hold when both suprema are finite?
>
> Answer: Yes. Upper boundedness of $f$ alone suffices.

```lean
theorem mathoverflow_347178.variants.bounded_only :
    ∀ᵉ (n ≥ 2) (f : ℝ^n → ℝ) (hf : ContDiff ℝ 1 f)
        (h : BddAbove (range f)) (h' : BddAbove (range (fun x ↦ f (x + gradient f x)))),
        (⨆ x, f x) = ⨆ x, f (x + gradient f x)
```

Category `research solved`; AMS [26 Real functions](../by-subject/part-01/26-real-functions/README.md). Declared in [FormalConjectures/Mathoverflow/347178.lean, line 76](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Mathoverflow/347178.lean#L76).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Mathoverflow/347178.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Mathoverflow/347178.lean)
- [mathoverflow/347178](https://mathoverflow.net/questions/347178)
