---
declaration: theorem
origin: cited
lean: Erdos1002.erdos_1002, Erdos1002.erdos_1002.variants.kesten
statement: formalized
---

# Erdős Problem 1002

> *References:*
> - [erdosproblems.com/1002](https://www.erdosproblems.com/1002)
> - [Ke60] Kesten, Harry, Uniform distribution {${\rm mod}\,1$}. Ann. of Math. (2) (1960), 445--471.

*Quoted from [FormalConjectures/ErdosProblems/1002.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1002.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/1002](https://www.erdosproblems.com/1002).

The file states 2 research or textbook statements: 1 open and 1 solved.

## `Erdos1002.erdos_1002`

Open: stated without proof.

> For any $0\lt \alpha<1$, let $f(\alpha,n)=\frac{1}{\log n}\sum_{1\leq k\leq n}(\tfrac{1}{2}-
> \{ \alpha k\})$. Does $f(\alpha,n)$ have an asymptotic distribution function?
>
> In other words, is there a non-decreasing function $g$ such that $g(-\infty)=0$, $g(\infty)=1$,
> and $\lim_{n\to \infty}\lvert \{ \alpha\in (0,1): f(\alpha,n)\leq c\}\rvert=g(c)$?

```lean
theorem erdos_1002 :
    ∃ g : ℝ → ℝ, Monotone g ∧
    Tendsto g atBot (𝓝 0) ∧
    Tendsto g atTop (𝓝 1) ∧
    letI f :=  fun (α : ℝ) (n : ℕ) ↦
      (1 / log n) * ∑ k ∈ Icc (1 : ℕ) n, (1 / 2 - Int.fract (α * k))
    ∀ c : ℝ, Tendsto (fun (n : ℕ) ↦ (volume { α | α ∈ Ioo (0 : ℝ) 1 ∧ f α n ≤ c }).toReal)
      atTop (𝓝 (g c))
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1002.lean, line 42](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1002.lean#L42).

## `Erdos1002.erdos_1002.variants.kesten`

Solved: stated here without proof.

> Kesten [Ke60] proved that if $f(\alpha,\beta,n)=\frac{1}{\log n}\sum_{1\leq k\leq n}(\tfrac{1}{2}-
> \{\beta+\alpha k\})$ then $f(\alpha,\beta,n)$ has asymptotic distribution function
> $g(c)=\frac{1}{\pi}\int_{-\infty}^{\rho c}\frac{1}{1+t^2}\mathrm{d}t$, where $\rho>0$ is an explicit
> constant.

```lean
theorem erdos_1002.variants.kesten :
    ∃ ρ > 0,
      let g := fun (c : ℝ) ↦ (1 / π) * ∫ t in Iic (ρ * c), 1 / (1 + t^2)
      ∀ c : ℝ, Tendsto (fun (n : ℕ) ↦
        (volume { p : ℝ × ℝ | let ⟨α, β⟩ := p; α ∈ Icc (0 : ℝ) 1 ∧ β ∈ Icc (0 : ℝ) 1 ∧
          (1 / log n) * ∑ k ∈ Icc (1 : ℕ) n, (1 / 2 - Int.fract (β + α * k)) ≤ c }).toReal)
        atTop (𝓝 (g c))
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1002.lean, line 59](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1002.lean#L59).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/1002.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1002.lean)
- [erdosproblems.com/1002](https://www.erdosproblems.com/1002)
