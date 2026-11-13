---
declaration: theorem
origin: cited
lean: Erdos829.erdos_829, Erdos829.variants.mordell, Erdos829.variants.mahler, Erdos829.variants.stewart
statement: formalized
---

# Erdős Problem 829

> *References:*
> - [erdosproblems.com/829](https://www.erdosproblems.com/829)
> - [Er83] Erdős, P. and Dudley, U., _Some remarks and problems in number theory related to the
>   work of Euler_. Math. Mag. (1983), 292-298.

*Quoted from [FormalConjectures/ErdosProblems/829.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/829.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/829](https://www.erdosproblems.com/829).

The file states 4 research or textbook statements: 1 open and 3 solved. It also has 4 test statements and 1 API statement, counted here but not shown.

## `Erdos829.erdos_829`

Open: stated without proof.

> **Erdős Problem 829 (open).**  Let $A \subseteq \mathbb{N}$ be the set of perfect cubes.  Is
> it true that $(1_A \ast 1_A)(n) \ll (\log n)^{O(1)}$?  That is, does there exist a natural
> number $C$ such that the number of representations of $n$ as a sum of two cubes is
> $O((\log n)^C)$ as $n \to \infty$?

```lean
theorem erdos_829 :
    ∃ C : ℕ, (fun n : ℕ => (sumRep cubes n : ℝ)) =O[atTop]
      (fun n : ℕ => (Real.log n) ^ C)
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/829.lean, line 57](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/829.lean#L57).

## `Erdos829.variants.mordell`

Solved: stated here without proof.

> Mordell proved $\limsup_{n \to \infty} (1_A \ast 1_A)(n) = \infty$, where $A$ is the set of
> perfect cubes.  Equivalently, the number of representations of $n$ as a sum of two cubes is
> unbounded.

```lean
theorem mordell : limsup (fun n : ℕ => (sumRep cubes n : ℕ∞)) atTop = (⊤ : ℕ∞)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/829.lean, line 95](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/829.lean#L95).

## `Erdos829.variants.mahler`

Solved: stated here without proof.

> Mahler proved $(1_A \ast 1_A)(n) \gg (\log n)^{1/4}$ for infinitely many $n$, where $A$ is
> the set of perfect cubes.
>
> [Ma35b] Mahler, K., _On the lattice points on curves of genus 1_. Proc. London Math. Soc.
>   (2) (1935), 431-466.

```lean
theorem mahler : ∃ C > (0 : ℝ),
    ∃ᶠ (n : ℕ) in atTop, C * (Real.log n) ^ ((1 : ℝ) / 4) ≤ (sumRep cubes n : ℝ)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/829.lean, line 106](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/829.lean#L106).

## `Erdos829.variants.stewart`

Solved: stated here without proof.

> Stewart improved Mahler's lower bound to $(1_A \ast 1_A)(n) \gg (\log n)^{11/13}$ for
> infinitely many $n$, where $A$ is the set of perfect cubes.
>
> [St08] Stewart, C. L., _Cubic Thue equations with many solutions_. Int. Math. Res. Not.
>   IMRN (2008), Art. ID rnn040, 11.

```lean
theorem stewart : ∃ C > (0 : ℝ),
    ∃ᶠ (n : ℕ) in atTop, C * (Real.log n) ^ ((11 : ℝ) / 13) ≤ (sumRep cubes n : ℝ)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/829.lean, line 118](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/829.lean#L118).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/829.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/829.lean)
- [erdosproblems.com/829](https://www.erdosproblems.com/829)
