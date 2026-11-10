---
declaration: theorem
origin: cited
lean: Erdos600.erdos_600.parts.i, Erdos600.erdos_600.parts.ii, Erdos600.erdos_600.variants.ruzsa_szemeredi_upper_bound
statement: formalized
---

# Erdős Problem 600

> *Reference:*
> - [erdosproblems.com/600](https://www.erdosproblems.com/600)
> - [erdosproblems.com/80](https://www.erdosproblems.com/80)
> - [Er87] Erdős, P., _Some problems on finite and infinite graphs_. Logic and combinatorics (Arcata, Calif., 1985) (1987), 223-228.
> - [RuSz78] Ruzsa, I. Z. and Szemerédi, E., _Triple systems with no six points carrying three triangles_. Combinatorics (Proc. Fifth Hungarian Colloq., Keszthely, 1976), Vol. II (1978), 939-945.

*Quoted from [FormalConjectures/ErdosProblems/600.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/600.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/600](https://www.erdosproblems.com/600).

The file states 3 research or textbook statements: 2 open and 1 solved.

## `Erdos600.erdos_600.parts.i`

Open: stated without proof.

> Let $r \geq 2$. Is it true that $e(n,r+1) - e(n,r) \to \infty$ as $n \to \infty$?

```lean
theorem erdos_600.parts.i :
    ∀ r : ℕ, 2 ≤ r →
      Tendsto (fun (n : ℕ) ↦ (eFunction n (r + 1) : ℝ) - (eFunction n r : ℝ)) atTop atTop
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/600.lean, line 53](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/600.lean#L53).

## `Erdos600.erdos_600.parts.ii`

Open: stated without proof.

> Let $r \geq 2$. Is it true that $\frac{e(n,r+1)}{e(n,r)} \to 1$ as $n \to \infty$?

```lean
theorem erdos_600.parts.ii :
    ∀ r : ℕ, 2 ≤ r →
      Tendsto (fun (n : ℕ) ↦ (eFunction n (r + 1) : ℝ) / (eFunction n r : ℝ)) atTop (𝓝 1)
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/600.lean, line 62](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/600.lean#L62).

## `Erdos600.erdos_600.variants.ruzsa_szemeredi_upper_bound`

Solved: stated here without proof.

> Ruzsa and Szemerédi [RuSz78] proved that $e(n,r)=o(n^2)$ for any fixed $r$.

```lean
theorem erdos_600.variants.ruzsa_szemeredi_upper_bound :
    ∀ r : ℕ, (fun (n : ℕ) ↦ (eFunction n r : ℝ)) =o[atTop] (fun (n : ℕ) ↦ (n : ℝ)^2)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/600.lean, line 71](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/600.lean#L71).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/600.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/600.lean)
- [erdosproblems.com/600](https://www.erdosproblems.com/600)
