---
declaration: theorem
origin: cited
lean: Erdos786.erdos_786.parts.i, Erdos786.erdos_786.parts.ii, Erdos786.erdos_786.parts.i.example, Erdos786.erdos_786.parts.i.selfridge
statement: formalized
---

# Erdős Problem 786

> *Reference:* [erdosproblems.com/786](https://www.erdosproblems.com/786)

*Quoted from [FormalConjectures/ErdosProblems/786.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/786.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/786](https://www.erdosproblems.com/786).

The file states 4 research or textbook statements: 2 open, 1 solved and 1 textbook result. It also has 2 test statements and 1 API statement, counted here but not shown.

## `Erdos786.erdos_786.parts.i`

Open: stated without proof.

> Let $\epsilon > 0$. Is there some set $A\subset\mathbb{N}$ of density $> 1 - \epsilon$
> such that $a_1\cdots a_r = b_1\cdots b_s$ with $a_i, b_j\in A$ can only hold when
> $r = s$?

```lean
theorem erdos_786.parts.i : ∀ ε > 0, ε ≤ 1 →
    ∃ (A : Set ℕ) (δ : ℝ), 0 ∉ A ∧ 1 - ε < δ ∧ A.HasDensity δ ∧ A.IsMulCardSet
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/786.lean, line 54](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/786.lean#L54).

## `Erdos786.erdos_786.parts.ii`

Open: stated without proof.

> Is there some set $A\subset\{1, ..., N\}$ of size $\geq (1 - o(1))N$ such that
> $a_1\cdots a_r = b_1\cdots b_s$ with $a_i, b_j\in A$ can only hold when
> $r = s$?

```lean
theorem erdos_786.parts.ii :
    ∃ (A : ℕ → Set ℕ) (f : ℕ → ℝ) (_ : f =o[atTop] (1 : ℕ → ℝ)),
    ∀ N, A N ⊆ Set.Icc 1 (N + 1) ∧ (1 - f N) * N ≤ (A N).ncard ∧ (A N).IsMulCardSet
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/786.lean, line 64](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/786.lean#L64).

## `Erdos786.erdos_786.parts.i.example`

Textbook result, proved here.

> An example of such a set with density $\frac 1 4$ is given by the integers $\equiv 2\pmod{4}$

```lean
theorem erdos_786.parts.i.example (A : Set ℕ) (hA : A = { n | n % 4 = 2 }) :
    A.HasDensity (1 / 4) ∧ A.IsMulCardSet
```

Category `textbook`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/786.lean, line 73](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/786.lean#L73).

## `Erdos786.erdos_786.parts.i.selfridge`

Solved: stated here without proof.

> Let $\epsilon > 0$ be given. Then, for a sufficiently large prime `p`, take the sequence of
> consecutive primes $p_1 < \cdots < p_k$ such that
>
> $$
> \sum_{i=1}^k \frac{1}{p_i} < 1 < \sum_{i=1}^{k + 1} \frac{1}{p_i},
> $$
>
> and let $A$ be the set of all naturals divisible by exactly one of $p_1, ..., p_k$ (with
> multiplicity $1$). Then $A$ has density $> \frac{1}{e} - \epsilon$ and has the property
> that $a_1\cdots a_r = b_1\cdots b_s$ with $a_i, b_j\in A$ can only hold when $r = s$.

```lean
theorem erdos_786.parts.i.selfridge (ε : ℝ) (hε : 0 < ε ∧ ε < 1 / rexp 1) :
    ∀ᶠ (p : ℕ) in atTop, p.Prime → ∃ k,
      ∑ q ∈ consecutivePrimesFrom p k, (1 : ℝ) / q < 1 ∧
        1 < ∑ q ∈ consecutivePrimesFrom p (k + 1), (1 : ℝ) / q ∧
          letI A := { n | ∑ q ∈ consecutivePrimesFrom p k, (n : ℕ).factorization q = 1 }
          ∃ δ, 1 / rexp 1 - ε < δ ∧ A.HasDensity δ ∧ A.IsMulCardSet
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/786.lean, line 187](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/786.lean#L187).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/786.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/786.lean)
- [erdosproblems.com/786](https://www.erdosproblems.com/786)
