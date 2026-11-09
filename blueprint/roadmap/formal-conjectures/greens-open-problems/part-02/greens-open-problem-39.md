---
declaration: theorem
origin: cited
lean: Green39.green_39, Green39.green_39.variant_101, Green39.green_39.variant_theta
statement: formalized
---

# Green's Open Problem 39

> *References:*
> - [Gr24] [Green, Ben. "100 open problems." (2024).](https://people.maths.ox.ac.uk/greenbj/papers/open-problems.pdf#problem.39)
> - [BJR11] Bollobás, Béla, Svante Janson, and Oliver Riordan. "On covering by translates of a set."
>   Random Structures & Algorithms 38.1‐2 (2011): 33-67.

*Quoted from [FormalConjectures/GreensOpenProblems/39.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/GreensOpenProblems/39.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 3 research or textbook statements: 3 open. It also has 8 test statements, counted here but not shown.

## `Green39.green_39`

Open: stated without proof.

> If $A \subset \mathbb{Z}/p\mathbb{Z}$ is random, $|A| = \sqrt{p}$, can we almost surely cover
> $\mathbb{Z}/p\mathbb{Z}$ with $100\sqrt{p}$ translates of $A$? [Gr24]

```lean
theorem green_39 :
    Tendsto
      (fun p : {q : ℕ // q.Prime} ↦
        let k := Nat.sqrt p
        let c := 100 * k
        (proportionCoverable p k c : ℝ))
      atTop (𝓝 1)
```

Category `research open`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [60 Probability theory and stochastic processes](../../by-subject/part-02/60-probability-theory-and-stochastic-processes/README.md). Declared in [FormalConjectures/GreensOpenProblems/39.lean, line 88](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/GreensOpenProblems/39.lean#L88).

## `Green39.green_39.variant_101`

Open: stated without proof.

> "I do not know how to answer this even with 100 replaced by 1.01." [Gr24]"

```lean
theorem green_39.variant_101 :
    Tendsto
      (fun p : {q : ℕ // q.Prime} ↦
        let k := Nat.sqrt p
        let c := ⌊1.01 * (k : ℝ)⌋₊
        (proportionCoverable p k c : ℝ))
      atTop (𝓝 1)
```

Category `research open`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [60 Probability theory and stochastic processes](../../by-subject/part-02/60-probability-theory-and-stochastic-processes/README.md). Declared in [FormalConjectures/GreensOpenProblems/39.lean, line 101](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/GreensOpenProblems/39.lean#L101).

## `Green39.green_39.variant_theta`

Open: stated without proof.

> Similar questions are interesting with $\sqrt{p}$ replaced by $p^\theta$ for any $\theta \le 1/2$. [Gr24]
>
> NOTE: using $C p^\theta$ translates as stated makes the conjecture trivially false by the pigeonhole
> principle. Indeed for a set of size $p^\theta$, we cover at most $C p^{2\theta}$ elements, which is
> strictly less than $p$ for $\theta < 1/2$. We interpret the question as asking whether
> $O(p^{1-\theta})$ translates suffice. This generalizes the main conjecture where
> $\sqrt{p} = p^{1-1/2}$.

```lean
theorem green_39.variant_theta :
    ∀ (θ : ℝ), 0 < θ → θ ≤ 1/2 →
    ∃ C > 1, Tendsto
      (fun p : {q : ℕ // q.Prime} ↦
        let k := ⌊(p : ℝ) ^ θ⌋₊
        let c := ⌊C * (p : ℝ) ^ (1 - θ)⌋₊
        (proportionCoverable p k c : ℝ))
      atTop (𝓝 1)
```

Category `research open`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [60 Probability theory and stochastic processes](../../by-subject/part-02/60-probability-theory-and-stochastic-processes/README.md). Declared in [FormalConjectures/GreensOpenProblems/39.lean, line 120](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/GreensOpenProblems/39.lean#L120).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/GreensOpenProblems/39.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/GreensOpenProblems/39.lean)
- [Green, Ben. "100 open problems." (2024).](https://people.maths.ox.ac.uk/greenbj/papers/open-problems.pdf#problem.39)
