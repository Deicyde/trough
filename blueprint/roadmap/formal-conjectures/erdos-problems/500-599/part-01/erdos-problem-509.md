---
declaration: theorem
origin: cited
lean: Erdos509.erdos_509, Erdos509.erdos_509.variants.Cartan_bound, Erdos509.erdos_509.variants.Pommerenke_bound, Erdos509.erdos_509.variants.Pommerenke_connected
statement: formalized
---

# Erdős Problem 509

> *Reference:* [erdosproblems.com/509](https://www.erdosproblems.com/509)

*Quoted from [FormalConjectures/ErdosProblems/509.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/509.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/509](https://www.erdosproblems.com/509).

The file states 4 research or textbook statements: 1 open and 3 solved. It also has 1 API statement, counted here but not shown.

## `Erdos509.erdos_509`

Open: stated without proof.

> Let $f(z) ∈ ℂ[z]$ be a monic non-constant polynomial. Can the set
> $\{z ∈ ℂ : |f(z)| ≤ 1\}$
> be covered by a set of closed discs the sum of whose radii is $≤ 2$?

```lean
theorem erdos_509 : ∀ (f : ℂ[X]), f.Monic → f.natDegree ≠ 0 →
    ∃ (ι : Type), Nonempty (BoundedDiscCover {z | ‖f.eval z‖ ≤ 1} 2 ι)
```

Category `research open`; AMS [30 Functions of a complex variable](../../../by-subject/part-01/30-functions-of-a-complex-variable/README.md). Declared in [FormalConjectures/ErdosProblems/509.lean, line 85](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/509.lean#L85).

## `Erdos509.erdos_509.variants.Cartan_bound`

Solved: stated here without proof.

> Let $f(z) ∈ ℂ[z]$ be a monic non-constant polynomial. Can the set
> $\{z ∈ ℂ : |f(z)| ≤ 1\}$
> be covered by a set of closed discs the sum of whose radii is $≤ 2e$?
> Solution: True. This is due to Cartan.
> See *Sur les systèmes de fonctions holomorphes à variétés linéaires
> lacunaires et leurs applications*, Henri Cartan,
> http://www.numdam.org/article/ASENS_1928_3_45__255_0.pdf

```lean
theorem erdos_509.variants.Cartan_bound : ∀ (f : ℂ[X]), f.Monic → f.natDegree ≠ 0 →
    ∃ (ι : Type), Nonempty (BoundedDiscCover {z | ‖f.eval z‖ ≤ 1} (2*rexp 1) ι)
```

Category `research solved`; AMS [30 Functions of a complex variable](../../../by-subject/part-01/30-functions-of-a-complex-variable/README.md). Declared in [FormalConjectures/ErdosProblems/509.lean, line 99](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/509.lean#L99).

## `Erdos509.erdos_509.variants.Pommerenke_bound`

Solved: stated here without proof.

> Let $f(z) ∈ ℂ[z]$ be a monic non-constant polynomial. Can the set
> $\{z ∈ ℂ : |f(z)| ≤ 1\}$
> be covered by a set of closed discs the sum of whose radii is $≤ 2.59$?
> Solution: True. This is due to Pommerenke.

```lean
theorem erdos_509.variants.Pommerenke_bound : ∀ (f : ℂ[X]), f.Monic → f.natDegree ≠ 0 →
    ∃ (ι : Type), Nonempty (BoundedDiscCover {z | ‖f.eval z‖ ≤ 1} 2.59 ι)
```

Category `research solved`; AMS [30 Functions of a complex variable](../../../by-subject/part-01/30-functions-of-a-complex-variable/README.md). Declared in [FormalConjectures/ErdosProblems/509.lean, line 109](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/509.lean#L109).

## `Erdos509.erdos_509.variants.Pommerenke_connected`

Solved: stated here without proof.

> Let $f(z) ∈ ℂ[z]$ be a monic non-constant polynomial.
> If it is connected, can the set $\{z ∈ ℂ : |f(z)| ≤ 1\}$
> be covered by a set of circles the sum of whose radii is $≤ 2$?
> Solution: True. This is due to Pommerenke.

```lean
theorem erdos_509.variants.Pommerenke_connected : ∀ (f : ℂ[X]), f.Monic → f.natDegree ≠ 0 →
    IsConnected {z | ‖f.eval z‖ ≤ 1} →
    ∃ (ι : Type), Nonempty (BoundedDiscCover {z | ‖f.eval z‖ ≤ 1} 2 ι)
```

Category `research solved`; AMS [30 Functions of a complex variable](../../../by-subject/part-01/30-functions-of-a-complex-variable/README.md). Declared in [FormalConjectures/ErdosProblems/509.lean, line 120](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/509.lean#L120).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/509.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/509.lean)
- [erdosproblems.com/509](https://www.erdosproblems.com/509)
