---
declaration: theorem
origin: cited
lean: NavierStokes.navier_stokes_existence_and_smoothness_R3, NavierStokes.navier_stokes_existence_and_smoothness_periodic, NavierStokes.navier_stokes_breakdown_R3, NavierStokes.navier_stokes_breakdown_periodic
statement: formalized
---

# Existence And Smoothness Of The Navier–Stokes Equation

> This file formalizes the Clay Mathematics Institute millennium problem concerning
> the existence and smoothness of solutions to the Navier-Stokes equations in three
> spatial dimensions. While the definitions are generalized to arbitrary dimension n,
> the millennium problem specifically concerns the case n = 3.
>
> ## References
> - [Wikipedia](https://en.wikipedia.org/wiki/Navier%E2%80%93Stokes_existence_and_smoothness)
> - [Clay Mathematics Institute](https://www.claymath.org/wp-content/uploads/2022/06/navierstokes.pdf)
> - [OpenAI, *Finite Time Blowup for Navier–Stokes*](https://cdn.openai.com/pdf/32d9f210-8b73-45e0-91bc-82a30aef8a9a/navier-stokes.pdf)
>
> ## Main Theorems (Clay Millennium Problem for n = 3)
>
> The Clay Millennium Problem asks for a proof of one of the following four statements:
>
> - `navier_stokes_existence_and_smoothness_R3`: (A) Global existence on ℝ³
> - `navier_stokes_existence_and_smoothness_periodic`: (B) Global existence on ℝ³/ℤ³
> - `navier_stokes_breakdown_R3`: (C) Existence of breakdown scenario on ℝ³
> - `navier_stokes_breakdown_periodic`: (D) Existence of breakdown scenario on ℝ³/ℤ³
>
> In September 2026, an internal OpenAI model proved alternatives (C) and (D) by constructing
> solutions that develop finite-time singularities under smooth forcing.
>
> ## Variable conventions
>
> Fefferman writes the velocity as $u(x,t)$, the initial velocity as $u^\circ(x)$, the
> pressure as $p(x,t)$, the force as $f(x,t)$, and the viscosity as $\nu$. In Lean,
> `u₀ : ℝ^n → ℝ^n` denotes the initial velocity, while `v : ℝ^n → ℝ → ℝ^n`
> denotes the solution velocity. The curried order `v x t`, `p x t`, and `f x t`
> keeps the source convention that position comes before time.
>
> Since the Clay statement gives equation (1) on the closed time half-line $t \ge 0$,
> the time derivative is encoded with `derivWithin` relative to `Set.Ici 0`. The Clay
> PDF also includes errata; in particular, we include spatial 1-periodicity of the
> pressure in the periodic case. The sign correction to the weak-solution identity in
> the errata is not represented here, since this file formalizes the four prize
> alternatives rather than the later weak-solution discussion.

*Quoted from [FormalConjectures/Millennium/NavierStokes.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Millennium/NavierStokes.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 4 research or textbook statements: 2 open and 2 solved. It also has 5 API statements, counted here but not shown.

## `NavierStokes.navier_stokes_existence_and_smoothness_R3`

Open: stated without proof.

> (A) Existence and smoothness of (unforced) Navier–Stokes solutions on ℝ³.

```lean
theorem navier_stokes_existence_and_smoothness_R3 (nu : ℝ) (hnu : nu > 0)
    (u₀ : ℝ³ → ℝ³) (hu₀ : InitialVelocityConditionDecay u₀) :
    ∃ v p, NavierStokesExistenceAndSmoothnessRn nu u₀ (f := 0) v p
```

Category `research open`; AMS [35 Partial differential equations](../by-subject/part-02/35-partial-differential-equations/README.md). Declared in [FormalConjectures/Millennium/NavierStokes.lean, line 274](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Millennium/NavierStokes.lean#L274).

## `NavierStokes.navier_stokes_existence_and_smoothness_periodic`

Open: stated without proof.

> (B) Existence and smoothness of (unforced) Navier–Stokes solutions in ℝ³/ℤ³.

```lean
theorem navier_stokes_existence_and_smoothness_periodic (nu : ℝ) (hnu : nu > 0)
    (u₀ : ℝ³ → ℝ³) (hu₀ : InitialVelocityConditionPeriodic u₀) :
    ∃ v p, NavierStokesExistenceAndSmoothnessPeriodic nu u₀ (f := 0) v p
```

Category `research open`; AMS [35 Partial differential equations](../by-subject/part-02/35-partial-differential-equations/README.md). Declared in [FormalConjectures/Millennium/NavierStokes.lean, line 281](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Millennium/NavierStokes.lean#L281).

## `NavierStokes.navier_stokes_breakdown_R3`

Solved: stated here; a Lean proof is at [https://github.com/openai/NavierStokesAndEuler/commit/8937a8f4cbc7abaab5e9e97d1cc7f5d2319d9538](https://github.com/openai/NavierStokesAndEuler/commit/8937a8f4cbc7abaab5e9e97d1cc7f5d2319d9538).

> (C) Breakdown of (forced) Navier–Stokes solutions on ℝ³.
>
> This was proven by an internal OpenAI model in September 2026.

```lean
theorem navier_stokes_breakdown_R3 (nu : ℝ) (hnu : nu > 0) :
    ∃ (u₀ : ℝ³ → ℝ³) (f : ℝ³ → ℝ → ℝ³),
    InitialVelocityConditionDecay u₀ ∧ ForceConditionDecay f ∧
    ¬ (∃ v p, NavierStokesExistenceAndSmoothnessRn nu u₀ f v p)
```

Category `research solved`; AMS [35 Partial differential equations](../by-subject/part-02/35-partial-differential-equations/README.md). Declared in [FormalConjectures/Millennium/NavierStokes.lean, line 295](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Millennium/NavierStokes.lean#L295).

## `NavierStokes.navier_stokes_breakdown_periodic`

Solved: stated here; a Lean proof is at [https://github.com/openai/NavierStokesAndEuler/commit/8937a8f4cbc7abaab5e9e97d1cc7f5d2319d9538](https://github.com/openai/NavierStokesAndEuler/commit/8937a8f4cbc7abaab5e9e97d1cc7f5d2319d9538).

> (D) Breakdown of (forced) Navier–Stokes solutions on ℝ³/ℤ³.
>
> This was proven by an internal OpenAI model in September 2026.

```lean
theorem navier_stokes_breakdown_periodic (nu : ℝ) (hnu : nu > 0) :
    ∃ (u₀ : ℝ³ → ℝ³) (f : ℝ³ → ℝ → ℝ³),
    InitialVelocityConditionPeriodic u₀ ∧ ForceConditionPeriodic f ∧
    ¬ (∃ v p, NavierStokesExistenceAndSmoothnessPeriodic nu u₀ f v p)
```

Category `research solved`; AMS [35 Partial differential equations](../by-subject/part-02/35-partial-differential-equations/README.md). Declared in [FormalConjectures/Millennium/NavierStokes.lean, line 310](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Millennium/NavierStokes.lean#L310).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Millennium/NavierStokes.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Millennium/NavierStokes.lean)
- [Wikipedia](https://en.wikipedia.org/wiki/Navier%E2%80%93Stokes_existence_and_smoothness)
